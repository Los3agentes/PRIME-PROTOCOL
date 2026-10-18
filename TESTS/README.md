# PILOT TESTS

Control reference: `v0.0.0A0.0.0`  
Status: PLANNED; no tests executed.

Pilot inputs: a copy of the canonical `COMMUNICATION.md` and one signed Python fixture.

Acceptance cases:
1. Single-character edit creates exactly one `A` punch, signature and changelog report.
2. Valid consecutive revisions preserve the previous-version chain.
3. Missing agent signature or change report is rejected.
4. Only the Judge authorizes an increment to `v`.
5. Multiple agents must not assign duplicate revision stamps.
6. Existing signed files are preserved and not rewritten with invented header formats.

Do not treat these planned cases as passed tests.
