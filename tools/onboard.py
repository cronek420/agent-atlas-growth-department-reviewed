#!/usr/bin/env python3
"""Safe onboarding/check utility for Agent Atlas Growth Department."""
from __future__ import annotations
import argparse, platform, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "ONBOARDING_STATUS.md"
ENV = ROOT / ".env"
ENV_EXAMPLE = ROOT / ".env.example"
REQUIRED = ["AGENTS.md","HUMAN_INSTRUCTIONS.md","APPROVAL_POLICY.md","AUTONOMY_POLICY.md","BUDGET_POLICY.md","SECURITY_POLICY.md","PUBLISHING_POLICY.md","MESSAGING_POLICY.md","DATA_RETENTION_POLICY.md","policy/action_registry.json","tools/policy_check.py","tools/policy_check_selftest.py"]
CHECKS = [
 ("Policy regression", [sys.executable,"tools/policy_check.py"]),
 ("Policy negative controls", [sys.executable,"tools/policy_check_selftest.py"]),
 ("Contract integrity", [sys.executable,"tools/contractcheck.py","CUSTOM_SKILL_BACKLOG.md","SKILL_TEST_PLAN.md"]),
 ("Registry integrity", [sys.executable,"tools/regcheck.py","CAPABILITY_REGISTRY.md"]),
 ("Permission matrix reproducibility", [sys.executable,"tools/render_permission_matrix.py","--check"]),
]
def env_names(path: Path)->set[str]:
    if not path.exists(): return set()
    out=set()
    for raw in path.read_text(encoding="utf-8",errors="replace").splitlines():
        line=raw.strip()
        if line and not line.startswith("#") and "=" in line: out.add(line.split("=",1)[0].strip())
    return out
def run(label,cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    return p.returncode==0,"\n".join((p.stdout+"\n"+p.stderr).strip().splitlines()[-5:])
def main():
    ap=argparse.ArgumentParser(description="Safely onboard/check Agent Atlas")
    ap.add_argument("--check",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--reset",action="store_true")
    a=ap.parse_args()
    if a.reset:
        if STATUS.exists(): STATUS.unlink()
        print("Reset complete. Secrets/configuration were not touched."); return 0
    blockers=[]; warnings=[]; passed=[]
    if sys.version_info < (3,11): blockers.append(f"Python 3.11+ required; found {platform.python_version()}")
    else: passed.append(f"Python {platform.python_version()}")
    if shutil.which("git"): passed.append("Git available")
    else: blockers.append("Git is not available on PATH")
    missing=[p for p in REQUIRED if not (ROOT/p).exists()]
    if missing: blockers.append("Missing required files: "+", ".join(missing))
    else: passed.append("Required governance/control files present")
    if not ENV.exists() and ENV_EXAMPLE.exists() and not (a.check or a.dry_run):
        shutil.copyfile(ENV_EXAMPLE,ENV); warnings.append("Created local .env from .env.example; fill values locally and never commit it")
    elif not ENV.exists(): warnings.append("No local .env found; no secrets were requested or created")
    missing_names=sorted(env_names(ENV_EXAMPLE)-env_names(ENV))
    if missing_names: warnings.append("Configuration variable names not yet present: "+", ".join(missing_names))
    if not blockers:
        for label,cmd in CHECKS:
            ok,detail=run(label,cmd)
            (passed if ok else blockers).append(label if ok else f"{label} failed. Last output:\n{detail}")
    state="BLOCKED" if blockers else ("NEEDS HUMAN" if warnings else "READY")
    lines=["# Agent Atlas Onboarding Status","",f"**State:** {state}","","Generated locally; secret values must never appear here.","","## Passed",*([f"- {x}" for x in passed] or ["- None"]),"","## Needs attention",*([f"- {x}" for x in warnings] or ["- None"]),"","## Blockers",*([f"- {x}" for x in blockers] or ["- None"]),"","## Safety defaults","- External sending: not enabled by onboarding","- Publishing: not enabled by onboarding","- Production deployment: not enabled by onboarding","- Spending/subscriptions: not enabled by onboarding","- Credential/account mutation: not performed by onboarding","","Read `HUMAN_INSTRUCTIONS.md` before promoting consequential capabilities."]
    STATUS.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"Agent Atlas onboarding: {state}"); print(f"Status: {STATUS}")
    return 1 if blockers else 0
if __name__=="__main__": raise SystemExit(main())
