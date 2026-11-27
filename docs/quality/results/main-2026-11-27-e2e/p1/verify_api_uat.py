import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import io
import json
import os
import subprocess
from threading import Barrier
from time import perf_counter
from uuid import uuid4
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

API, DB, TOOLS = ("qldapm-m27-api-1", "qldapm-m27-postgres-1", "qldapm-m27-tools-1")
port = subprocess.check_output(["docker", "port", API, "3000/tcp"], text=True).strip()
base = "http://" + port
api_env = dict(item.split("=", 1) for item in json.loads(subprocess.check_output(
    ["docker", "inspect", "--format", "{{json .Config.Env}}", API], text=True)))
db_url = urlsplit(api_env["DATABASE_URL"])
loopback_db = db_url._replace(netloc=db_url.netloc.rsplit("@", 1)[0] + "@127.0.0.1:5432")
env = {**os.environ, "JWT_SECRET": api_env["JWT_SECRET"], "AUTH_MODE": "local",
       "DATABASE_URL": loopback_db.geturl()}

def sql(statement):
    return subprocess.check_output(["docker", "exec", "-i", DB, "psql", "-v", "ON_ERROR_STOP=1",
                                    "-qAt", "-U", "ticket", "-d", "ticket"], input=statement, text=True).strip()

def token(role):
    return subprocess.check_output(["docker", "exec", "-e", "JWT_SECRET", "-e", "AUTH_MODE",
                                    "-e", "DATABASE_URL", TOOLS, "/tmp/dev-token", "-role", role],
                                   env=env, text=True).strip()

run_tag = uuid4().hex[:6]
tokens = {"organizer": token("organizer"), "admin": token("admin")}
for n in range(1, 5):
    tokens[f"s{n}"] = token("student")
    sql(f"""UPDATE users SET email='tv2.qa.{run_tag}.student{n}@hcmut.edu.vn', student_code='QA{run_tag}{n}',
         full_name='Synthetic Student {n}' WHERE email='student.demo@hcmut.edu.vn';""")

rows = []
case = ""

def request(method, path, role="", body=None, match=None, expected=None, prefix="/api/v1", evidence_body=None):
    headers = {"Content-Type": "application/json"}
    if role:
        headers["Authorization"] = "Bearer " + tokens[role]
    if match is not None:
        headers["If-Match"] = str(match)
    req = Request(base + prefix + path, data=None if body is None else json.dumps(body).encode(),
                  headers=headers, method=method)
    clock = perf_counter()
    try:
        res = urlopen(req, timeout=12)
    except HTTPError as error:
        res = error
    with res:
        raw, status = res.read(), res.status
        content_type = res.headers.get("Content-Type", "")
        payload = json.loads(raw) if raw and "json" in content_type else {}
        data, meta = payload.get("data"), payload.get("meta", {})
        excerpt = {}
        if isinstance(data, dict):
            safe = ("status", "waitlistPosition", "registeredCount", "waitlistCount", "availableSeats", "version",
                    "location", "method", "checkedInAt", "roles", "isAdmin", "isActive", "registered",
                    "checkedIn", "waitlisted", "cancelled", "checkInByMethod", "capacity", "attendanceRate")
            excerpt.update({key: data[key] for key in safe if key in data})
            if "checkinCode" in data:
                excerpt["hasCheckinCode"] = data["checkinCode"] is not None
            if "qrToken" in data:
                excerpt["hasQrToken"] = data["qrToken"] is not None
        elif isinstance(data, list):
            excerpt["rows"] = len(data)
        if meta:
            excerpt["meta"] = {key: meta[key] for key in ("affectedCount", "notifiedCount", "totalItems")
                               if key in meta}
            if "promotedRegistrationId" in meta:
                excerpt["meta"]["hasPromotedRegistration"] = meta["promotedRegistrationId"] is not None
        if payload.get("error"):
            excerpt["error"] = payload["error"].get("code")
        elapsed = round((perf_counter() - clock) * 1000, 2)
        log = {"case": case, "method": method, "path": prefix + path, "role": role or "anonymous",
               "status": status, "ms": elapsed, "summary": excerpt}
        if body is not None:
            log["request"] = evidence_body if evidence_body is not None else {
                k: ("<redacted>" if k in {"idToken", "refreshToken", "checkinCode", "qrToken"} else v)
                for k, v in body.items()
            }
        if match is not None:
            log["ifMatch"] = match
        rows.append(log)
        if expected is not None:
            assert status in ((expected,) if isinstance(expected, int) else expected), (status, excerpt, expected)
        return status, data, meta, payload.get("error", {}), raw, res.headers

def mark(label):
    global case
    case = label

def check(label, outcome, detail):
    rows.append({"result": label, "outcome": outcome, "detail": detail})

def data(*args, **kwargs):
    return request(*args, **kwargs)[1]

def event(title, cap=1, wait=2, hours=72, publish=True):
    now = datetime.now(timezone.utc)
    body = {"unitId": unit, "title": "TV2 QA " + title, "location": "Phòng test",
            "startAt": (now + timedelta(hours=hours)).isoformat(),
            "endAt": (now + timedelta(hours=hours+2)).isoformat(),
            "registrationOpensAt": (now - timedelta(hours=1)).isoformat(),
            "registrationClosesAt": (now + timedelta(hours=hours*0.9)).isoformat(),
            "capacity": cap, "waitlistLimit": wait}
    draft = data("POST", "/events", "organizer", body, expected=201)
    assert draft["status"] == "DRAFT"
    path = "/events/" + draft["id"]
    if publish:
        assert data("POST", path + "/submit", "organizer", expected=200)["status"] == "PENDING_APPROVAL"
        assert data("POST", path + "/approve", "admin", {}, expected=200)["status"] == "PUBLISHED"
    return path, draft, body

def register(path, role, kind):
    response = data("POST", path + "/registrations", role, expected=201)
    assert response["status"] == kind
    return response

def reg_path(reg):
    return "/registrations/" + reg["id"]

def cancel(reg, role):
    return request("POST", reg_path(reg) + "/cancel", role, expected=200)

def notifications(role, event_path):
    return [n["type"] for n in data("GET", "/me/notifications?pageSize=100", role, expected=200)
            if n.get("eventId") == event_path.rsplit("/", 1)[-1]]

def parallel_registration(path, roles):
    barrier = Barrier(len(roles))
    def start(role):
        barrier.wait(timeout=10)
        return request("POST", path + "/registrations", role)
    with ThreadPoolExecutor(len(roles)) as pool:
        return list(pool.map(start, roles))

try:
    mark("SETUP")
    for route in ("/health/live", "/health/ready"):
        request("GET", route, expected=200, prefix="")
    mark("T-AUTH-02")
    invalid_refresh = "synthetic-invalid"
    response = request("POST", "/auth/refresh", body={"refreshToken": invalid_refresh},
                       expected=401)
    assert response[3]["code"] == "UNAUTHENTICATED"
    mark("T-AUTH-03")
    for role, expected_role in (("s1", "STUDENT"), ("organizer", "ORGANIZER"), ("admin", "ADMIN")):
        profile = data("GET", "/me", role, expected=200)
        assert expected_role in profile["roles"] and profile["isActive"]
        if role == "organizer":
            organizer_id = profile["id"]
            unit = next(u["unit"]["id"] for u in profile["units"] if u["unit"]["code"] == "DEMO")
        elif role == "admin":
            assert profile["isAdmin"]
    request("GET", "/me", expected=401)
    check("T-AUTH-03", "pass", "Three roles and anonymous 401")

    mark("T-EV-01")
    path, draft, request_body = event("CP3 flow", publish=False)
    assert any(e["id"] == draft["id"] for e in data("GET", "/manage/events?status=DRAFT", "organizer", expected=200))
    check("T-EV-01", "pass", "Draft and management list")
    mark("T-EV-02")
    revised = data("PATCH", path, "organizer", {"location": "Phòng QA cập nhật"},
                   match=draft["version"], expected=200)
    assert revised["location"] == "Phòng QA cập nhật" and revised["version"] == draft["version"]+1
    stale = request("PATCH", path, "organizer", {"location": "stale"}, match=draft["version"], expected=409)
    assert stale[3]["code"] == "VERSION_CONFLICT"
    check("T-EV-02", "pass", "Updated version and stale-version 409")

    mark("T-AUTH-04")
    request("GET", path, "s1", expected=404)
    pending = data("POST", path + "/submit", "organizer", expected=200)
    assert pending["status"] == "PENDING_APPROVAL"
    request("GET", path, "s1", expected=404)
    assert request("POST", path + "/approve", "organizer", {}, expected=403)[3]["code"] == "FORBIDDEN"
    sql(f"UPDATE users SET is_admin=true WHERE id='{organizer_id}';")
    try:
        self_approval = request("POST", path + "/approve", "organizer", {}, expected=403)[3]["code"]
        assert data("GET", path, "organizer", expected=200)["status"] == "PENDING_APPROVAL"
    finally:
        sql(f"UPDATE users SET is_admin=false WHERE id='{organizer_id}';")
    check("T-AUTH-04", "pass" if self_approval == "SELF_APPROVAL_NOT_ALLOWED" else "fail", f"Private until approved; creator with both roles denied HTTP 403 {self_approval}; expected SELF_APPROVAL_NOT_ALLOWED")
    mark("T-EV-05")
    assert request("POST", "/events", "organizer", {**request_body, "endAt": request_body["startAt"]},
                   expected=400)[3]["code"] == "VALIDATION_ERROR"
    assert request("PATCH", path, "organizer", {"location": "pending"}, match=pending["version"],
                   expected=409)[3]["code"] == "INVALID_STATE_TRANSITION"
    check("T-EV-05", "pass", "Invalid schedule and pending draft lock")
    mark("T-EV-03")
    assert any(e["id"] == draft["id"] for e in data("GET", "/approvals/pending", "admin", expected=200))
    published = data("POST", path + "/approve", "admin", {"comment": "QA approved"}, expected=200)
    assert published["status"] == "PUBLISHED"
    public = data("GET", path, "s1", expected=200)
    assert public["status"] == "PUBLISHED"
    assert any(e["id"] == draft["id"] for e in data("GET", "/events?q=CP3%20flow", "s1", expected=200))
    check("T-EV-03", "pass", "Submit pending then public after admin approval")
    mark("T-EV-04")
    reject_path, _, _ = event("reject", publish=False)
    data("POST", reject_path + "/submit", "organizer", expected=200)
    rejected = data("POST", reject_path + "/reject", "admin", {"reason": "QA reject"}, expected=200)
    assert rejected["status"] == "REJECTED"
    rejected_detail = data("GET", reject_path, "organizer", expected=200)
    assert data("PATCH", reject_path, "organizer", {"location": "fixed"}, match=rejected_detail["version"],
                expected=200)["status"] == "REJECTED"
    assert data("POST", reject_path + "/submit", "organizer", expected=200)["status"] == "PENDING_APPROVAL"
    audit = data("GET", reject_path + "/approval-logs", "admin", expected=200)
    assert any(log["action"] == "REJECT" and log["comment"] == "QA reject" for log in audit)
    check("T-EV-04", "pass", "Reject with reason, edit and resubmit")

    mark("T-REG-01")
    a = register(path, "s1", "REGISTERED")
    detail = data("GET", path, "s1", expected=200)
    assert a["checkinCode"] and (detail["registeredCount"], detail["availableSeats"]) == (1, 0)
    check("T-REG-01", "pass", "Registered with seat consumed")
    mark("T-REG-02")
    dupe = request("POST", path + "/registrations", "s1", expected=409)
    assert dupe[3]["code"] == "ALREADY_REGISTERED" and dupe[3]["details"]["registrationId"] == a["id"]
    dupe_path, _, _ = event("duplicate race", cap=2)
    same = parallel_registration(dupe_path, ["s4", "s4"])
    assert sorted(x[0] for x in same) == [201, 409]
    assert next(x for x in same if x[0] == 409)[3]["code"] == "ALREADY_REGISTERED"
    check("T-REG-02", "pass", "Repeat 409, simultaneous same student yields 201 and 409")
    mark("T-REG-03")
    race, _, _ = event("capacity race", cap=1, wait=0)
    responses = parallel_registration(race, ["s1", "s2"])
    assert sorted(x[0] for x in responses) == [201, 409]
    assert next(x for x in responses if x[0] == 409)[3]["code"] == "EVENT_FULL"
    assert data("GET", race, "s1", expected=200)["registeredCount"] == 1
    check("T-REG-03", "pass", "Two requests, one seat, no waitlist yields 201 and 409")
    mark("T-WL-01")
    b, c = register(path, "s2", "WAITLISTED"), register(path, "s3", "WAITLISTED")
    assert [b["waitlistPosition"], c["waitlistPosition"]] == [1, 2] and not b["checkinCode"] and not c["checkinCode"]
    assert request("POST", path + "/registrations", "s4", expected=409)[3]["code"] == "EVENT_FULL"
    check("T-WL-01", "pass", "Ordered waitlist and limit enforced")
    # Lượt 2 (UAT 24/11): T-WL-03 đã chạy ở lượt 1 và đạt; bỏ qua để fixture A/B còn nguyên cho T-REG-04/T-WL-02.
    if not os.environ.get("SKIP_WL03"):
        mark("T-WL-03")
        sql("""CREATE FUNCTION tv2_fail_promotion() RETURNS trigger LANGUAGE plpgsql AS $$
          BEGIN IF NEW.type='PROMOTED' THEN RAISE EXCEPTION 'TV2 synthetic notification failure'; END IF; RETURN NEW; END;
          $$;
          CREATE TRIGGER tv2_fail_promotion BEFORE INSERT ON notifications FOR EACH ROW EXECUTE FUNCTION tv2_fail_promotion();""")
        try:
            attempt = request("POST", reg_path(a) + "/cancel", "s1")
            still_waiting = data("GET", reg_path(b), "s2", expected=200)
            still_registered = data("GET", reg_path(a), "s1", expected=200)
            outcome = "pass" if still_waiting["status"] == "REGISTERED" else "fail"
            check("T-WL-03", outcome, f"forced PROMOTED insert rejection -> cancel HTTP {attempt[0]}, {attempt[3].get('code')}, first entry {still_waiting['status']}, initial occupant {still_registered['status']}")
        finally:
            sql("DROP TRIGGER tv2_fail_promotion ON notifications; DROP FUNCTION tv2_fail_promotion();")

    mark("T-REG-04/T-WL-02")
    result = cancel(a, "s1")
    assert result[1]["status"] == "CANCELLED" and result[1]["cancelledBy"] == "STUDENT" and result[2]["promotedRegistrationId"] == b["id"]
    assert data("GET", reg_path(b), "s2", expected=200)["status"] == "REGISTERED"
    assert data("GET", reg_path(c), "s3", expected=200)["waitlistPosition"] == 1
    assert notifications("s2", path).count("PROMOTED") == 1
    check("T-REG-04", "pass", "Self-cancellation >24h, status CANCELLED")
    check("T-WL-02", "pass", "Only head promoted, next rank 1, one PROMOTED notification")
    mark("T-WL-04")
    new_a = register(path, "s1", "WAITLISTED")
    assert new_a["id"] != a["id"] and new_a["waitlistPosition"] == 2
    check("T-WL-04", "pass", "New registration and tail rank 2")

    mark("T-REG-05")
    late, _, _ = event("within 24h", hours=2)
    late_reg = register(late, "s1", "REGISTERED")
    late_wait = register(late, "s2", "WAITLISTED")
    assert request("POST", reg_path(late_reg) + "/cancel", "s1", expected=422)[3]["code"] == "CANCEL_DEADLINE_PASSED"
    assert cancel(late_wait, "s2")[1]["status"] == "CANCELLED"
    check("T-REG-05", "pass", "Inside 24h registered cancellation denied, waitlist can leave")

    mark("T-AUTH-05")
    assert data("GET", reg_path(b), "s2", expected=200)["id"] == b["id"]
    request("GET", reg_path(b), "s3", expected=404)
    request("GET", path + "/registrations", "s3", expected=404)
    check("T-AUTH-05", "pass", "Owner sees registration; unrelated student gets 404")
    mark("T-AUTH-06")
    sql(f"UPDATE users SET email='organizer.qa.{run_tag}@hcmut.edu.vn' WHERE id='{organizer_id}';")
    tokens["other-organizer"] = token("organizer")
    sql("""DELETE FROM unit_memberships WHERE user_id=(SELECT id FROM users WHERE email='organizer.demo@hcmut.edu.vn');
        INSERT INTO units(code,name,type) VALUES ('QA-OTHER','Other QA unit','CLUB') ON CONFLICT (code) DO NOTHING;
        INSERT INTO unit_memberships(unit_id,user_id,member_role)
        SELECT u.id,p.id,'ORGANIZER' FROM units u CROSS JOIN users p
        WHERE u.code='QA-OTHER' AND p.email='organizer.demo@hcmut.edu.vn';""")
    for group in ("organizer", "admin"):
        listed = data("GET", path + "/registrations", group, expected=200)
        assert len(listed) == 4 and all("student" in entry and "qrToken" not in entry and "checkinCode" not in entry for entry in listed)
    request("GET", path + "/registrations", "other-organizer", expected=404)
    sql(f"""INSERT INTO unit_memberships(unit_id,user_id,member_role)
        SELECT '{unit}',id,'ORGANIZER' FROM users WHERE email='organizer.demo@hcmut.edu.vn';""")
    same_unit = data("GET", path + "/registrations", "other-organizer", expected=200)
    assert {r["id"] for r in same_unit} == {r["id"] for r in listed}
    check("T-AUTH-06", "pass", "Admin and same-unit organizer (not creator) see the list; outside organizer 404")

    mark("T-EV-06")
    version = data("GET", path, "organizer", expected=200)["version"]
    change = request("PATCH", path, "organizer", {"location": "Phòng sau khi công bố"}, match=version, expected=200)
    assert change[1]["status"] == "PUBLISHED" and change[2]["notifiedCount"] == 3
    assert all(notifications(s, path).count("EVENT_CHANGED") == 1 for s in ("s1", "s2", "s3"))
    check("T-EV-06", "pass", "Published edit, 3 in-app notifications to active registrations")
    mark("T-EV-07")
    cancel_event = request("POST", path + "/cancel", "organizer", {"reason": "TV2 QA cancellation"}, expected=200)
    assert cancel_event[1]["status"] == "CANCELLED" and cancel_event[2]["affectedCount"] == 3
    for role, reg in (("s1", new_a), ("s2", b), ("s3", c)):
        assert data("GET", reg_path(reg), role, expected=200)["status"] == "CANCELLED_BY_EVENT"
        assert notifications(role, path).count("EVENT_CANCELLED") == 1
    check("T-EV-07", "pass", "Three active entries cancelled, notifications present")

    mark("T-INT/API")
    ci, _, _ = event("check-in single event", cap=3, hours=72)
    original = register(ci, "s4", "REGISTERED")
    qr = register(ci, "s1", "REGISTERED")
    code = register(ci, "s2", "REGISTERED")
    manual = register(ci, "s3", "WAITLISTED")
    assert cancel(original, "s4")[2]["promotedRegistrationId"] == manual["id"]
    assert data("GET", reg_path(manual), "s3", expected=200)["status"] == "REGISTERED"
    check("T-INT-01/API", "pass", "Same event: create, approve, fill 3 seats, waitlist, cancel, promote")
    now = datetime.now(timezone.utc)
    moved = {"startAt": (now + timedelta(minutes=35)).isoformat(),
             "endAt": (now + timedelta(minutes=90)).isoformat(),
             "registrationClosesAt": (now + timedelta(minutes=25)).isoformat()}
    version = data("GET", ci, "organizer", expected=200)["version"]
    assert data("PATCH", ci, "organizer", moved, match=version, expected=200)["status"] == "PUBLISHED"
    mark("T-CI-01")
    owner_qr = data("GET", reg_path(qr), "s1", expected=200)["qrToken"]
    ci_path = ci + "/check-ins"
    assert data("POST", ci_path, "organizer", {"method": "QR", "qrToken": owner_qr}, expected=201)["method"] == "QR"
    check("T-CI-01", "pass", "API QR data flow with real server-generated QR token")
    mark("T-CI-02")
    duplicate_scan = request("POST", ci_path, "organizer", {"method": "QR", "qrToken": owner_qr}, expected=409)
    assert duplicate_scan[3]["code"] == "ALREADY_CHECKED_IN" and duplicate_scan[3]["details"]["checkedInAt"]
    assert len(data("GET", ci_path+"?method=QR", "organizer", expected=200)) == 1
    check("T-CI-02", "pass", "Duplicate scan rejected and exactly one QR check-in")
    mark("T-CI-04")
    by_code = {"method": "CODE", "checkinCode": code["checkinCode"].replace("-", "").lower()}
    assert data("POST", ci_path, "organizer", by_code, expected=201)["method"] == "CODE"
    assert data("GET", reg_path(code), "s2", expected=200)["checkIn"]["method"] == "CODE"
    check("T-CI-04", "pass", "Lower-case code without hyphen worked; owner readback CODE")
    mark("T-CI-05")
    manual_payload = {"method": "MANUAL", "registrationId": manual["id"], "note": "Đã đối chiếu thẻ mẫu"}
    denial = request("POST", ci_path, "admin", manual_payload, expected=(403, 404))
    assert data("GET", reg_path(manual), "s3", expected=200)["checkIn"] is None
    assert request("POST", ci_path, "organizer", {**manual_payload, "note": ""},
                   expected=400)[3]["code"] == "VALIDATION_ERROR"
    assert data("POST", ci_path, "organizer", manual_payload, expected=201)["method"] == "MANUAL"
    assert data("GET", reg_path(manual), "s3", expected=200)["checkIn"]["method"] == "MANUAL"
    assert sql(f"SELECT count(*) FROM activity_logs WHERE event_id='{ci.rsplit('/', 1)[1]}' AND action='MANUAL_CHECKIN';") == "1"
    check("T-CI-05", "pass", f"Admin denied HTTP {denial[0]} {denial[3]['code']}; organizer valid note and audit")

    check("T-INT-02/API", "pass", "Same event: real QR, CODE, MANUAL, including promoted student")
    mark("T-RP-01")
    attendee_list = data("GET", ci_path, "organizer", expected=200)
    registration_list = data("GET", ci + "/registrations", "organizer", expected=200)
    assert (len(attendee_list), len(registration_list)) == (3,4)
    assert {r["id"] for r in registration_list if r["status"]=="REGISTERED"} == {r["registrationId"] for r in attendee_list}
    check("T-RP-01", "pass", "Three matching active/attendance IDs, one cancellation excluded")
    mark("T-RP-02")
    summary = data("GET", ci + "/reports/summary", "admin", expected=200)
    assert (summary["registered"],summary["checkedIn"],summary["attendanceRate"],summary["cancelled"]) == (3,3,1,1)
    assert summary["checkInByMethod"] == {"QR":1,"CODE":1,"MANUAL":1}
    check("T-RP-02", "pass", "3 registered and 3 checked in, one cancellation, one of each check-in method")
    mark("T-INT-03/API")
    for kind, count in (("registrations", 4), ("attendance", 3)):
        raw = request("GET", ci + f"/exports/{kind}", "organizer", expected=200)[4]
        assert len(list(csv.reader(io.StringIO(raw.decode("utf-8-sig"))))) == count + 1
    check("T-INT-03/API", "pass", "Same event: summary and both CSV exports match pipeline")

    mark("T-RP-03")
    perf_path, draft, _ = event("report 500", cap=500, hours=0.7)
    event_id = draft["id"]
    sql(f"""INSERT INTO users(email,full_name,student_code)
       SELECT 'tv2.qa.bulk'||n||'@hcmut.edu.vn','Synthetic Bulk '||n,'B'||lpad(n::text,5,'0')
       FROM generate_series(1,500) n ON CONFLICT (email) DO NOTHING;
       INSERT INTO registrations(event_id,student_id,status,checkin_code,checked_in_at,checkin_method,checked_in_by,checkin_note)
       SELECT '{event_id}',id,'REGISTERED','QA'||substring(student_code from 2)||'X',
         CASE WHEN student_code <= 'B00250' THEN now() END,
         CASE WHEN student_code <= 'B00250' THEN 'MANUAL'::checkin_method END,
         CASE WHEN student_code <= 'B00250' THEN '{organizer_id}'::uuid END,
         CASE WHEN student_code <= 'B00250' THEN 'Synthetic fixture' END
       FROM users WHERE email LIKE 'tv2.qa.bulk%@hcmut.edu.vn';
       UPDATE events SET registered_count=500 WHERE id='{event_id}';""")
    start = perf_counter()
    summary = data("GET", perf_path + "/reports/summary", "organizer", expected=200)
    exports = []
    for kind, count in (("registrations", 500), ("attendance", 250)):
        res = request("GET", perf_path + f"/exports/{kind}?format=csv", "organizer", expected=200)
        assert res[4].startswith(b"\xef\xbb\xbf") and "attachment" in res[5]["Content-Disposition"]
        output = list(csv.reader(io.StringIO(res[4].decode("utf-8-sig"))))
        assert len(output) == count+1 and len(output[0]) == 7
        expected_codes = {f"B{n:05d}" for n in range(1, count+1)}
        assert {row[1] for row in output[1:]} == expected_codes
        exports.append(len(output)-1)
    took = perf_counter()-start
    assert (summary["registered"],summary["checkedIn"],summary["attendanceRate"]) == (500,250,0.5)
    assert took < 30
    check("T-RP-03", "pass", f"500 source + 250 attendance; CSV rows {exports}; summary plus both exports {took:.3f}s")

except Exception as error:
    import traceback
    traceback.print_exc()
    check(case, "interrupted", type(error).__name__)
    raise SystemExit(1)
finally:
    for item in rows:
        print(json.dumps(item, ensure_ascii=True))
