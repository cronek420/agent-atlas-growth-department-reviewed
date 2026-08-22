#!/usr/bin/env python3
"""Fail-closed validator for Agent Atlas company-first lead records."""
from __future__ import annotations
import json, sys
from pathlib import Path

ALLOWED_AUTONOMY={"DISABLED","SIMULATION","ASSISTED","LIMITED_AUTONOMY"}
ALLOWED_EMAIL={"verified","risky","invalid","unknown"}
ALLOWED_CHECK={"pass","fail","unknown"}
ALLOWED_COMPLIANCE={"pass","review","fail","blocked"}

def need(obj,path):
    cur=obj
    for part in path.split('.'):
        if not isinstance(cur,dict) or part not in cur: return None
        cur=cur[part]
    return cur

def validate(d):
    e=[]
    required=["lead_id","company.name","company.website","company.fit_score","company.fit_reason","company.source_url","company.source_retrieved_at","decision_maker.name","decision_maker.role","decision_maker.role_verified","decision_maker.identity_confidence","decision_maker.verification_sources","contact.professional_email","contact.email_verification_status","safety.suppression_check","safety.compliance_status","safety.duplicate_check","outreach.autonomy_level","outreach.send_allowed"]
    for p in required:
        v=need(d,p)
        if v is None or v=="" or v==[]: e.append(f"missing:{p}")
    score=need(d,"company.fit_score")
    if not isinstance(score,(int,float)) or not 0<=score<=100: e.append("company.fit_score must be 0..100")
    if need(d,"decision_maker.role_verified") is not True: e.append("decision-maker role is not verified")
    sources=need(d,"decision_maker.verification_sources") or []
    if len(sources)<1: e.append("decision-maker verification source required")
    email=str(need(d,"contact.email_verification_status") or "").lower()
    if email not in ALLOWED_EMAIL: e.append("invalid email verification status")
    for p,allowed in [("safety.suppression_check",ALLOWED_CHECK),("safety.duplicate_check",ALLOWED_CHECK),("safety.compliance_status",ALLOWED_COMPLIANCE)]:
        if str(need(d,p) or "").lower() not in allowed: e.append(f"invalid {p}")
    autonomy=str(need(d,"outreach.autonomy_level") or "")
    if autonomy not in ALLOWED_AUTONOMY: e.append("invalid autonomy level")
    send=need(d,"outreach.send_allowed") is True
    if send:
        if autonomy!="LIMITED_AUTONOMY": e.append("send_allowed requires LIMITED_AUTONOMY")
        if email!="verified": e.append("send_allowed requires verified email")
        if str(need(d,"safety.suppression_check") or "").lower()!="pass": e.append("send_allowed requires suppression PASS")
        if str(need(d,"safety.duplicate_check") or "").lower()!="pass": e.append("send_allowed requires duplicate PASS")
        if str(need(d,"safety.compliance_status") or "").lower()!="pass": e.append("send_allowed requires compliance PASS")
    return e

def main():
    if len(sys.argv)!=2:
        print("usage: python tools/lead_pipeline_check.py lead.json"); return 2
    p=Path(sys.argv[1])
    try: d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as ex:
        print(f"BLOCKED: unreadable JSON: {ex}"); return 2
    errors=validate(d)
    if errors:
        print("BLOCKED")
        for x in errors: print(f"- {x}")
        return 1
    print("READY")
    return 0
if __name__=="__main__": raise SystemExit(main())
