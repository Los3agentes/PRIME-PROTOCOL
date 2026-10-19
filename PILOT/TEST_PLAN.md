<!-- PRIME_META
id: PP-PILOT-TEST
core: PILOT
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT-Orchestrator (attribution only)
-->

# PILOT — COMMUNICATION + Python file

## Objective
Demonstrate a narrowly scoped communication resolver + tests without claiming that the full PRIME PROTOCOL has been proven in production.

## Procedure
1. Change only `HARD-CORE/COMMUNICATION.md` and `PILOT/communication_worker.py` during the first authorization-bounded pilot.
2. Run `python -m unittest discover -s TESTS -v`.
3. Run `python scripts/record_change.py . --actor codex --authorization-id PILOT-AUTH-001 --reason 'Pilot change'` after edits.
4. Confirm `A` increments on COMMUNICATION and does not change `v`. Confirm report and project CHANGELOG changes, and that validation passes.
5. Negative test: tamper with any managed file without recording and ensure validator fails.

## Acceptance
Tests pass; change report exists; untouched HARD CORE modules retain original hash; `v` unchanged; unauthorized edits rejected by integrity gate.

## Bond attestation
- Agent: ChatGPT-Orchestrator
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Integrity/evidence: see `AGENT-BOND/BOND_MANIFEST.json` and `AGENT-BOND/REPORTS/INIT-0001.json`
