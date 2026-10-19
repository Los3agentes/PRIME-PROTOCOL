<!-- PRIME_META
id: PP-HC-DELIVERABLES
core: HARD
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT-Orchestrator (attribution only)
-->

# DELIVERABLES — verifiable handoff

## Purpose
Deliver artifacts that can be inspected, opened and checked, with reproducible boundaries.

## MUST
1. Name each deliverable's type, exact location, applicable version, status and verification result.
2. Validate physical existence and basic integrity before offering a path or download link.
3. Include a concise manifest and a test/usage command when shipping code or protocol packages.
4. Label prototypes, unreviewed draft policy, formal approval and production baseline separately.
5. Do not silently omit required pieces; report partial output honestly.
6. Do not overwrite the source-of-truth artifact without permission; preserve independent snapshot/fork.
7. Include reproducibility metadata (inputs, versions, environment and checksums where useful and allowed).

## Acceptance contract
Each requirement is either `PASS`, `FAIL`, `NOT_TESTED` or `N/A`, never implied passed by narrative alone.

## Bond attestation
- Agent: ChatGPT-Orchestrator
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Integrity/evidence: see `AGENT-BOND/BOND_MANIFEST.json` and `AGENT-BOND/REPORTS/INIT-0001.json`
