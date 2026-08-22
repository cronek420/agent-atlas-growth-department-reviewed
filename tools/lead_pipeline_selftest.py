#!/usr/bin/env python3
"""Positive and negative controls for lead_pipeline_check."""
from lead_pipeline_check import validate

BASE={
 "lead_id":"L-1",
 "company":{"name":"Example Co","website":"https://example.com","fit_score":85,"fit_reason":"Verified fit","source_url":"https://example.com","source_retrieved_at":"2026-08-22"},
 "decision_maker":{"name":"Alex Example","role":"Operations Director","role_verified":True,"identity_confidence":"high","verification_sources":["https://example.com/team"]},
 "contact":{"professional_email":"alex@example.com","email_verification_status":"verified","email_verified_at":"2026-08-22"},
 "safety":{"suppression_check":"pass","compliance_status":"pass","duplicate_check":"pass"},
 "outreach":{"autonomy_level":"LIMITED_AUTONOMY","send_allowed":True}
}
def clone():
 import json; return json.loads(json.dumps(BASE))
def main():
 cases=[]
 cases.append(("good-record",clone(),False))
 x=clone(); x["contact"]["email_verification_status"]="unknown"; cases.append(("unknown-email",x,True))
 x=clone(); x["safety"]["suppression_check"]="fail"; cases.append(("suppressed",x,True))
 x=clone(); x["safety"]["duplicate_check"]="fail"; cases.append(("duplicate",x,True))
 x=clone(); x["safety"]["compliance_status"]="blocked"; cases.append(("compliance-block",x,True))
 x=clone(); x["decision_maker"]["role_verified"]=False; cases.append(("unverified-role",x,True))
 x=clone(); x["outreach"]["autonomy_level"]="SIMULATION"; cases.append(("simulation-send",x,True))
 failed=[]
 for name,data,should_fail in cases:
  got_fail=bool(validate(data))
  if got_fail!=should_fail: failed.append(name)
 if failed:
  print("SELFTEST FAIL:",", ".join(failed)); return 1
 print(f"SELFTEST PASS: {len(cases)} controls")
 return 0
if __name__=="__main__": raise SystemExit(main())
