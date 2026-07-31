# Agent Handoff

- Run ID: `phase-03-2026-07-30-b`
- Phase: 03 — Governance, Security, Approval, and Autonomy Policies
- Agent: Privacy Reviewer (specialist)
- Assignment: Author `DATA_RETENTION_POLICY.md` per the Phase 03 task graph (T1, parallel with
  Security Architect, Policy Designer, Marketing Operations Reviewer)
- Files owned: `DATA_RETENTION_POLICY.md`, this handoff

## Facts and evidence

- **A stale file was already sitting on disk when I started, and it was wrong in a way worth
  reporting in full.** `DATA_RETENTION_POLICY.md` and this handoff both existed before I began,
  self-labeled run `phase-03-2026-07-30-a` — the first Phase 03 attempt, built on a branch that
  predated the real merged Phase 02 and discarded by explicit Project Owner choice
  (`findings.md` F-03-01; `task_plan.md` § "Why `-b`"). `git status --short` on both files showed
  `??` (untracked) — consistent with "never committed," but the working-tree files themselves
  had not actually been cleared by the branch reset described in `task_plan.md`, so the stale
  content was still there to read and could have been mistaken for current work. I read it in
  full before deciding what to keep versus rewrite.
- **That stale draft contained a real ID collision, not just outdated framing.** It cited `D-042`
  six times as "the decision that prohibits inventing numeric thresholds." In the real, merged
  register, `D-042` is a different decision: `policy/action_registry.json` is the machine-
  readable permission source of truth, and `AGENT_PERMISSION_MATRIX.md` is generated from it,
  never hand-edited. The real "no number invented" decision is `D-047`. I verified this by
  reading `DECISIONS.md`'s Phase 03 section directly (rows `D-041`–`D-048`) rather than trusting
  the stale draft's citations, and corrected every instance in the rewritten file.
- **The stale draft also asserted, in its §10, "Phase 02 was never executed (`F-03-01`,
  `D-036`)."** This was true of the discarded branch and false of the real project, which has a
  real 141-row `CAPABILITY_REGISTRY.md` and a real `RUNTIME_AGENT` role (confirmed by reading
  `policy/POLICY_CONTRACT.md` §5 and `CAPABILITY_REGISTRY.md` directly). I corrected this
  wherever it appeared (the §10 line and a §3 table cell for personal-data readers) rather than
  silently carrying a false premise into a policy document that later phases will cite.
- Given the scope of these corrections plus a required new section, I rewrote the file rather
  than patching six scattered citations and hoping I found them all; I grepped for `D-042`,
  `D-036`, `Phase 02`, and `RUNTIME_AGENT` across the stale file first to enumerate every affected
  line before starting the rewrite, so the rewrite is a superset correction, not a guess.
- `Q-009` (data-privacy handling for lead/contact data) is `UNRESOLVED` (`OPEN_QUESTIONS.md`).
  No lead, contact, or personal data may be collected, imported, or stored today
  (`docs/PROJECT_BOUNDARIES.md` §5; `R-12`, `D-033`). This is the central constraint stated in
  my assignment and I did not weaken it anywhere in the policy.
- `policy/action_registry.json` (schema 2.0.0, this attempt) carries the rows this policy is
  built on: `ACT-R08`/`ACT-W10` (personal data, `DENY`, unchanged in substance from the first
  attempt) and the genuinely new `ACT-R09` (borrowed-authority access path, `DENY`, escalation
  `ESC-011`) — this row did not exist in the first attempt's context and is the reason §2.8 is
  new. I confirmed all four rows' exact outcome, basis, and escalation fields by reading the
  registry directly rather than from my assignment's paraphrase.
- `RISK_REGISTER.md` R-21 names the concrete capability rows behind the new §2.8 class —
  `CAPABILITY_REGISTRY.md` `C-009` (artifact publishing, borrowed Claude-account authority) and
  `C-045` (browser automation driving the operator's own authenticated session) — both
  dispositioned `PROHIBITED`/`RESTRICTED`. I cited these two IDs because they are the ones
  `R-21` itself names; I did not invent or extend the list.
- `.gitignore` (read directly, in full) pre-emptively excludes `data/private/`, `data/leads/`,
  `data/contacts/`, `*.leads.csv`, `*.contacts.csv` under a comment citing `D-033` and `Q-009`,
  and states explicitly this is "a backstop, not permission." I used this as the one concrete,
  already-operating mechanical control classified `SCAFFOLDED` rather than `PROPOSED` in §11.
- `findings.md` `F-01-06` ("exclude first, create second") and `F-01-01` (the three-element
  history-rewrite protocol: inspect, obtain owner approval, `--force-with-lease` pinned to an
  inspected commit) both directly support §4/§5's argument that Git's permanence makes
  deletion-after structurally different from exclusion-before. I verified `F-01-01`'s content
  directly (it was not one of my explicitly assigned reads, but I checked it once I decided to
  cite its "inspect first" protocol by name, to avoid citing a finding I hadn't actually read).
- `DECISIONS.md` `D-047` (not `D-042` — see above) governs every blank cell in my §3 table and
  the values in §5/§6. I left every retention period, deletion SLA, and consent-record duration
  blank and named the owner input that would fill each.
- I read `RISK_REGISTER.md` R-10, R-12, R-13, and skimmed R-20–R-23 as instructed. R-13 (secrets)
  I deliberately did not restate — it is `SECURITY_POLICY.md`'s risk to cite. R-21 is the basis
  for the new §2.8 class; R-10 (WhatsApp opt-in) and R-12 (personal data handling obligations)
  are cited in §6's boundary statement and §3's table respectively.
- I did **not** read `SECURITY_POLICY.md`'s contents, per my assignment's explicit instruction —
  I confirmed only that the file exists on disk (`git status --short` shows it untracked, which
  is expected mid-phase and not itself evidence of staleness). I removed the stale draft's
  specific section-number citations into that file (`§2–4`, `§2.2`, `§3`, `§4`) because I have not
  verified this attempt's version still uses that structure, and citing a structure I have not
  read would itself violate the instruction not to describe its contents.
- I did not access, list, or stat `C:\Users\crone\Projects\Rough-Draft-Builders-Club` at any
  point.

## Assumptions

Read genuinely self-critically, per `findings.md` F-00-05's warning that a clean assumptions
section is a red flag, not a success:

1. **I assumed the right response to finding a stale, wrong file was to rewrite it in place
   rather than flag it and stop.** My assignment says "write a document useful now, not a
   placeholder waiting on Q-009," and the stale file's core structure (11 sections, the
   classification scheme, the hard line between existing-data and personal-data rules) was
   sound — only specific citations and one section were wrong or missing. I judged a full,
   corrected rewrite served the phase better than leaving a known-wrong file in place with a
   note. A reader could reasonably prefer I had left the stale file untouched and only reported
   the defect; I chose to fix it because leaving a document with a false "Phase 02 was never
   executed" claim in a file other phases will cite seemed like the worse failure mode.
2. **I assumed the new §2.8 class belongs at the same level as the other seven data classes**
   (a peer of personal data, not a subclass of it or a note attached to §2.4). The assignment
   describes it as "one class this attempt's real Phase 02 context surfaces" without specifying
   its exact placement; I chose peer status because its defining feature (no credential, no
   import step) is genuinely different from every other class's defining feature (how the data
   got here), even though its *consequence* once triggered collapses into §2.4/§2.5. A different
   reviewer might have folded it into §2.7 (untrusted content) instead, since both involve data
   this project did not deliberately collect; I judged it distinct enough to need its own class
   because §2.7 is about content whose *provenance* is untrusted, while §2.8 is about an *access
   mechanism* that bypasses credential-based controls entirely regardless of content provenance.
3. **I assumed the Git-permanence argument (§4/§5) — a pushed blob remains reachable from
   history — generalizes correctly from the secrets case to personal data and, by extension, to
   anything a future §2.8 exercise might surface.** The underlying mechanism is a fact about Git,
   not an inference, and `F-01-06`/the real precedent in `F-01-01` already establish the
   reasoning pattern for one data class. Extending it to a second and, structurally, a third class
   is my own judgment call, not something any source document states about personal data or
   borrowed-authority data specifically.
4. **I assumed the consent-record "must outlive its subject's data" tension (§6) is still worth
   raising**, carried over from the stale draft's own reasoning, which I re-verified rather than
   accepted on faith — the tension is analysis I performed (and re-checked this run), not a fact
   drawn from any source document.
5. **I did not verify that `DECISIONS.md`, `findings.md`, and `agent_runs/` actually behave the
   way I described them in §3/§11 (append-only, indefinite retention) through any mechanism other
   than reading their current content and the project's stated rules (`D-001`, `ACT-W11`).** I
   classified this `SCAFFOLDED` rather than `IMPLEMENTED` partly for this reason.
6. **No assumption I am aware of asserts a fact about what the owner wants or what any law
   requires, or invents a numeric value.** I actively avoided naming a jurisdiction or legal
   obligation (§8). I flag this not as proof of correctness — `F-00-05` is explicit that a clean
   self-report carries no evidentiary weight — but as the check I performed most deliberately,
   given it is the failure mode most explicitly prohibited in my assignment, and given this
   exact phase already found one real defect (the `D-042`/`D-036` citations) in a document that
   presumably also claimed, on its first pass, to have made no unfounded assertions.

## Open questions

- **`Q-009`'s current wording asks for retention/storage/deletion/jurisdiction but does not
  explicitly ask for a storage *substrate*.** §5 argues that a retention-period answer is not
  actionable without also knowing where personal data would live, because Git's permanence rules
  out this repository as that substrate. I recommend the phase owner consider whether `Q-009`'s
  question text in `OPEN_QUESTIONS.md` should be sharpened to ask for a substrate explicitly. I
  did not make this edit myself — `OPEN_QUESTIONS.md` is not a file I own.
- **Should the consent-record tension in §6, and the §2.8 borrowed-authority class's interaction
  with personal data, be recorded as new or updated risk rows?** I believe both are real and not
  fully captured in `RISK_REGISTER.md` as currently worded (R-21 covers the access-path exposure
  generally but not specifically its data-classification consequence). Authoring exact `R-xx`
  register language is outside my two-file assignment; naming it here for the phase owner.
- **Whether the stale-file discovery itself (a discarded attempt's working-tree files surviving
  a branch reset, self-labeled with the wrong run ID) merits its own finding.** I treated it as
  evidence for my §4 Git/working-tree-permanence argument and corrected the file, but I did not
  write a new `findings.md` entry about it because `findings.md` is not a file I own and the
  phase owner may already plan to record this under `F-03-01`'s existing account or a new entry.
  I recommend the phase owner check whether any *other* stale untracked file from the first
  attempt (I did not audit beyond my own two files and the `policy/`/`tools/` files I saw listed
  in `git status`) needs the same scrutiny before the gate report is drafted.
- **Is my §2.4/§2.5 split (personal data vs. sensitive personal data) still useful now that §2.8
  exists?** All three resolve to identical `DENY`/`UNRESOLVED` outcomes in §3 today, so none of
  the distinctions are currently load-bearing. I kept all three because the assignment asked for
  each to be distinguished, but flag that none has an operational effect until `Q-009` and/or
  `Q-012`/`ACT-R09`'s status change.
- **I did not read `MESSAGING_POLICY.md`, `PUBLISHING_POLICY.md`, `APPROVAL_POLICY.md`,
  `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, or `SECURITY_POLICY.md`**, per my assignment's
  instruction. My §6 boundary statement and my §2.6/§10 cross-references are based only on the
  file-ownership table in `task_plan.md` and the `"policy"` field values in
  `policy/action_registry.json`, not on their actual content. If any of those files, once
  integrated, define consent, gated-category, spend, or secrets rules that conflict with anything
  I stated here, that is a defect for the phase owner to reconcile, not something I could have
  checked.

## Work completed

- Read, in full, before writing anything: `CLAUDE.md`, `policy/POLICY_CONTRACT.md`,
  `policy/action_registry.json` (in full, including `ACT-R08`, `ACT-W10`, `ACT-S04`, `ACT-S05`,
  and the new `ACT-R09`), `docs/PROJECT_BOUNDARIES.md` §5/§6, `DECISIONS.md` (in full, including
  `D-033` and the real Phase 03 section `D-041`–`D-048`), `OPEN_QUESTIONS.md` Q-009 exactly as
  written, `RISK_REGISTER.md` (R-12, R-10, R-13 in full; R-20–R-23 skimmed as instructed, with
  R-21 read closely since it grounds the new §2.8 class), `NON_GOALS.md` (in full),
  `.gitignore` (in full), `findings.md` (F-01-06, F-03-01 as instructed, plus F-02-03 skimmed for
  the borrowed-authority framing, plus F-01-01 read on demand to verify a citation), and
  `templates/AGENT_HANDOFF_TEMPLATE.md`. Did not read `SECURITY_POLICY.md`'s contents, per
  instruction — confirmed only its existence.
- Discovered a stale, self-mislabeled `DATA_RETENTION_POLICY.md` and
  `HANDOFF_PRIVACY_REVIEWER.md` already on disk from the discarded first Phase 03 attempt
  (`phase-03-2026-07-30-a`), confirmed via `git status --short` that both were untracked, and
  identified a real ID collision (`D-042` used for the wrong decision) and a false claim ("Phase
  02 was never executed") inherited from that attempt's false premise.
- Rewrote `DATA_RETENTION_POLICY.md` in full: corrected every `D-042` citation to `D-047`;
  corrected the false Phase-02-not-executed claim in two places; added §2.8 (data reachable via a
  borrowed-authority access path), a new per-class table row, a new §5 point, updated §9 with
  `ESC-011`, updated §10 and §11 to reflect the new class and the corrected citations; removed
  specific unverified section-number citations into `SECURITY_POLICY.md`, replacing them with
  name-only cross-references consistent with not having read that file this run; kept the rest
  of the structure (scope/ownership/precedence; 8 (now effectively 10, after the new class and
  renumbered excludes/fail-closed subsections) data classes; per-class rules table; concrete
  retention for artifacts that exist today including the Git-permanence argument; deletion/
  erasure structurally defined and blocked on `Q-009`; consent records with the ownership
  boundary against `MESSAGING_POLICY.md`; data minimisation; jurisdiction left `UNRESOLVED`; the
  escalation section; a "not covered here" section; and a capability-classification table with no
  `IMPLEMENTED` claims).
- Rewrote this handoff to reflect the real run, the stale-file discovery, and the corrections
  made.

## Files changed

- `DATA_RETENTION_POLICY.md` (rewritten in full — a stale version from the discarded first
  attempt existed on disk and has been replaced)
- `agent_runs/phase-03/handoffs/HANDOFF_PRIVACY_REVIEWER.md` (rewritten in full, same reason)

No other file was written, edited, or deleted. I did not touch `DECISIONS.md`, `findings.md`,
`progress.md`, `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`, `CURRENT_PHASE.md`, `task_plan.md`,
`SECURITY_POLICY.md`, or any sibling policy file.

## Tests run

None in the sense of executed code — this is a documentation-only deliverable and I ran no
script. What I did run, manually, during drafting: a re-read of every `D-`/`Q-`/`R-`/`NG-`/
`F-`/`ACT-`/`GC-`/`ESC-`/`C-` identifier I cited against the actual register or registry file
before citing it, specifically including a targeted grep of the stale draft for `D-042`,
`D-036`, `Phase 02`, and `RUNTIME_AGENT` to enumerate every line needing correction before I
started the rewrite, and a `git status --short` check on the files I touched (and on
`SECURITY_POLICY.md` and sibling policy files, to confirm their tracked/untracked state without
reading their content). None of this is a substitute for `tools/policy_check.py`'s mechanical
run at T3, which I did not execute — that is the Phase Owner's step, outside my two-file
assignment.

## Failures or risks

- **Risk: I may not have caught every stale citation.** I grepped for the specific strings I
  identified (`D-042`, `D-036`, `Phase 02`, `RUNTIME_AGENT`) but a full rewrite from that base
  means any citation I didn't specifically re-verify against a source document during the
  rewrite could still be wrong. I re-checked every ID I could recall citing against
  `DECISIONS.md`/`policy/action_registry.json`/`RISK_REGISTER.md`/`findings.md` directly rather
  than trusting the stale draft's version, but I have not run a mechanical ID-resolution pass.
- **Risk: §2.4/§2.5/§2.8's three-way split may read as more operationally distinct than it is.**
  All three currently resolve to identical `DENY`/`UNRESOLVED` outcomes. If a future reader treats
  the three-class structure as implying meaningful present-day differences, that would be a
  misreading of a document that intended the split for future-proofing, not current operation.
  Flagged in Open questions.
- **Risk: the Git-permanence argument in §4/§5 is my own reasoning, extended from the secrets
  case to personal data and, by inference, to a hypothetical future §2.8 exercise** — not a rule
  any governing document states about either class specifically. I believe it is sound and now
  have a second, concrete piece of evidence for it (this file's own stale predecessor surviving
  an uncommitted branch reset), but the extension itself remains my judgment call.
- No failure occurred in completing the assignment. Both owned files are within scope, both now
  reflect the real merged Phase 02 state rather than the discarded attempt's false premise, and I
  did not encounter a need to access `C:\Users\crone\Projects\Rough-Draft-Builders-Club` at any
  point.

## Recommended next action

Phase Owner proceeds to T2 (`tools/render_permission_matrix.py` → `AGENT_PERMISSION_MATRIX.md`)
once all four T1 specialists have completed their files. I recommend the phase owner
specifically:

1. **Check whether any other untracked file surviving from the discarded first attempt (I saw
   `policy/`, `tools/policy_check.py`, `tools/policy_check_selftest.py`,
   `tools/render_permission_matrix.py` in `git status --short` output) carries the same kind of
   stale citation I found and corrected in mine** — `policy/POLICY_CONTRACT.md` and
   `policy/action_registry.json` appear to have been freshly authored for this run (their own
   headers say `phase-03-2026-07-30-b`), so they are likely fine, but I did not verify the
   `tools/` scripts' content and recommend someone do before T3 relies on them.
2. Consider the two proposed-but-not-authored register changes in "Open questions" above —
   sharpening `Q-009`'s text to ask for a storage substrate, and whether the consent-record
   tension and the §2.8 classification consequence merit new or updated risk rows.
3. Disclose in the gate report that a stale, wrongly-cited file was found on disk and corrected,
   consistent with this project's practice of disclosing every access and every correction rather
   than rounding it down to "no issue" (`docs/PROJECT_BOUNDARIES.md` §2 Phase 00 precedent).
