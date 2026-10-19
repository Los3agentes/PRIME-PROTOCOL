<!-- PRIME_META
id: PP-AG-ROLES
core: GOVERNANCE
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT-Orchestrator (attribution only)
-->

# AGENTS — authority and roles

## Authority
- **USER / JUEZ:** sets direction, approves the `v` series, changes baselines, grants and revokes scopes, resolves authority conflicts.
- **ORCHESTRATOR / PRODUCER:** resolves specification, translates user objectives, delegates limited tasks, checks tests and AGENT BOND, reports results. Cannot overrule JUEZ.
- **EXECUTOR / ARTIST:** writes/tests code and artifacts only inside explicit task boundaries; may increment agent revision `A` and attest changes.
- **VALIDATOR / AGENT BOND:** an automated structural check, not a human or identity-proof authority. Rejects untracked/missing/unsigned (declarative) changes.

Roles are assignable per project; the MAGIDreamer working example uses user=Executive/Developer, ChatGPT=Producer/Orchestrator, Codex=Artist/Executor. This example is not a universal hard binding.

## Boundaries
An agent cannot approve its own expansion of project scope, permanently modify hard-core authority or silently inherit unrelated project permissions. External action capabilities require tool-level permissions in addition to any PRIME text policy.

## Bond attestation
- Agent: ChatGPT-Orchestrator
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Integrity/evidence: see `AGENT-BOND/BOND_MANIFEST.json` and `AGENT-BOND/REPORTS/INIT-0001.json`
