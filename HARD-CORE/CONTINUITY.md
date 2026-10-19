<!-- PRIME_META
id: PP-HC-CONTINUITY
core: HARD
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT-Orchestrator (attribution only)
-->

# CONTINUITY — state, lineage & handoff

## Purpose
Keep sessions, agents and projects aligned without conflating authority or scope.

## MUST
1. Maintain project identity, current stage, authorized decisions, pending decisions, baseline/fork lineage and next valid action.
2. Store project-specific `CHANGELOG.csv` rather than one combined log masquerading as per-project history.
3. Retain evidence and historical provenance even when producing condensed handoffs.
4. Agent changes inside an approved task may raise `A` and record a signature/report; changing `v` remains exclusively JUEZ-controlled.
5. Resume using the latest verified checkpoint; detect stale assumptions or incompatible versions before editing.
6. Do not automatically inherit one project's permissions, memory or soft cores into another.
7. Version references must remain stable across filename, internal metadata, reports and manifests.

## Handoff fields
`project`, `scope`, `baseline`, `v`, `A`, `authorization`, `work_done`, `evidence`, `open_risks`, `next_action`.

## Bond attestation
- Agent: ChatGPT-Orchestrator
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Integrity/evidence: see `AGENT-BOND/BOND_MANIFEST.json` and `AGENT-BOND/REPORTS/INIT-0001.json`
