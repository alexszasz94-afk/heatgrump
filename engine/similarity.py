"""Verificare de asemănare înainte de export: nu repeta același set / hook / tip de hook prea des.
Rulare: python3 engine/similarity.py <set_id> <hook_key> <hook_kind>
Ieșire: OK sau AVERTISMENT cu motivele. Reguli (ultimele 30 de videouri):
 - hook nou (adapted/creative): același hook_key niciodată în ultimele 30; tipar adaptat max 2 folosiri
 - concept dovedit (hook_kind=proven): se poate repeta, dar la ≥ min_gap_days zile și niciodată cu același set
 - același set: nu în ultimele 2, max 4 în total
 - același hook_kind (problem/reaction/twist): max 40% din ultimele 10
 - același set + același hook_kind: nu în ultimele 10
"""
import sys
from common import *

def check(set_id, hook_key, hook_kind, c=None):
    c = c or cfg(); vids = jload(STATE / "videos.json", [])[-30:]; issues = []
    if hook_kind == "proven":
        # excepție: conceptele dovedite SE repetă, dar nu mai des de min_gap_days și niciodată cu același set/personaj
        import datetime
        gap_days = c["proven"]["min_gap_days"]; same = [v for v in vids if v["hook"] == hook_key]
        if same:
            last = datetime.date.fromisoformat(same[-1]["date"])
            if (datetime.date.today() - last).days < gap_days: issues.append(f"conceptul dovedit {hook_key} a fost folosit acum <{gap_days} zile ({same[-1]['date']})")
            if any(v["set"] == set_id for v in same): issues.append(f"conceptul {hook_key} a mai fost făcut cu setul {set_id} (același personaj) — ia alt set")
    elif any(v["hook"] == hook_key for v in vids): issues.append(f"hook {hook_key} a mai fost folosit în ultimele 30 de videouri")
    if hook_kind == "adapted" and sum(1 for v in vids if v["hook"] == hook_key) >= c["proven"]["adapted_max_uses"]: issues.append(f"tiparul adaptat {hook_key} e la limita de {c['proven']['adapted_max_uses']} folosiri")
    gap = c["rotation"]["min_gap_between_uses"]
    if any(v["set"] == set_id for v in vids[-gap:]): issues.append(f"setul {set_id} a fost folosit la unul din ultimele {gap} videouri")
    if sum(1 for v in vids if v["set"] == set_id) >= c["rotation"]["max_uses_per_set"]: issues.append(f"setul {set_id} e la limita de folosiri")
    last10 = vids[-10:]
    if last10 and hook_kind not in ("proven", "adapted", "creative") and sum(1 for v in last10 if v["hook_kind"] == hook_kind) / len(last10) > 0.4: issues.append(f"prea multe hook-uri de tip '{hook_kind}' în ultimele 10")
    if any(v["set"] == set_id and v["hook_kind"] == hook_kind for v in last10): issues.append(f"setul {set_id} a avut deja un hook '{hook_kind}' recent")
    return issues

if __name__ == "__main__":
    iss = check(*sys.argv[1:4])
    print("OK" if not iss else "AVERTISMENT:\n - " + "\n - ".join(iss))
