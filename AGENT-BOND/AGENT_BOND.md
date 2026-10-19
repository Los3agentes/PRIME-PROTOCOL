<!-- PRIME_META
id: PP-AB-BOND
core: GOVERNANCE
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT-Orchestrator (attribution only)
-->

# AGENT BOND — change acceptance contract

## Mission
Reject undocumented changes to managed package files before they become a trusted baseline. Every change requires a change-set ID, an actor attribution, an authorization reference, a structured report, project CHANGELOG and matching file hashes.

## Rules
1. `v` may change only with a declared authorization from USER/JUEZ. Non-JUEZ agents may only increment `A` on changed protocol documents within authorized tasks.
2. `A` counts agent-authored revision events for that document. A change set may increase A on multiple changed documents, once per file per set.
3. Each report must have `change_id`, `date`, `actor`, `authorization_id`, `reason`, `signature`, `changed_files`, `verification` and `version_approval` when applicable.
4. Every managed file must match its BOND_MANIFEST SHA-256; unregistered files fail preflight. Report paths must exist and have non-empty attribution. CHANGELOG has one row per report.
5. The validator does **not** establish that an authorization really came from the JUEZ, nor prove who typed a signature. Trust that requires signed commits, protected branches and accountable human reviews.
6. Never treat a self-edited manifest or text signature as secure cryptographic attestation. This is a **local consistency gate**, not a security boundary.

## Validation
`python scripts/validate_bond.py .` returns exit code `0` on structural PASS; `1` on failure.

## Changes
After editing, run `scripts/record_change.py` with true actor and authorization. It updates `A` in changed protocol headers, the report, per-project CHANGELOG and digest manifest, then runs validation. It refuses unauthorized `v` edits and no-op change sets. Do not use it to paper over a bad change; inspect source diffs and authorize first.

## Bond attestation
- Agent: ChatGPT-Orchestrator
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Integrity/evidence: see `AGENT-BOND/BOND_MANIFEST.json` and `AGENT-BOND/REPORTS/INIT-0001.json`
