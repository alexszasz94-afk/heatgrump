"""Paznic de buget. Claude Code îl apelează înainte de fiecare lot și îi dă soldul Higgsfield curent (din tool-ul `balance`).
Rulare: python3 engine/budget.py check <credite_higgsfield_acum> [apify_usd_azi]
        python3 engine/budget.py note "<ce s-a făcut>"   → jurnal
Ține în state/budget.json soldul de la începutul zilei și calculează consumul.
"""
import sys
from common import *

def check(credits_now, apify_usd=0.0):
    c = cfg()["budget"]; b = jload(STATE / "budget.json", {})
    day = b.get(today()) or {"start_credits": credits_now, "apify_usd": 0.0, "log": []}
    day["apify_usd"] = max(day.get("apify_usd", 0.0), float(apify_usd))
    used = day["start_credits"] - credits_now
    b[today()] = day; jsave(STATE / "budget.json", b)
    pct = 100 * used / c["higgsfield_credits_per_day"] if c["higgsfield_credits_per_day"] else 0
    msg = f"Higgsfield azi: {used:.0f}/{c['higgsfield_credits_per_day']} credite ({pct:.0f}%), sold {credits_now:.0f} · Apify azi: {day['apify_usd']:.2f}$/{c['apify_usd_per_day']}$"
    if pct >= 100 or day["apify_usd"] >= c["apify_usd_per_day"]: return "STOP: " + msg
    if pct >= c["warn_at_percent"]: return "ATENȚIE (aproape de limită): " + msg
    return "OK: " + msg

if __name__ == "__main__":
    if sys.argv[1] == "check": print(check(float(sys.argv[2]), float(sys.argv[3]) if len(sys.argv) > 3 else 0))
    else:
        b = jload(STATE / "budget.json", {}); b.setdefault(today(), {"start_credits": None, "apify_usd": 0.0, "log": []})["log"].append(sys.argv[2]); jsave(STATE / "budget.json", b); print("notat")
