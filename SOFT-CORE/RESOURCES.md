<!-- PRIME_META
id: PP-SC-RESOURCES
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# RESOURCES — Inventory of tools, files and working capacity

## Purpose
Inventory of tools, files and working capacity.

## Operating rules
1. Inventory actual tools and accessible files without assuming an agent can access another agent's filesystem, secrets or connections.
2. Separate resources into VERIFIED, DECLARED, UNAVAILABLE and UNKNOWN; do not convert guesses into capabilities.
3. Estimate disk, memory, input sizes, execution limits and external cost when material to a job.
4. Select the minimum sufficient capability; keep credentials and private data out of reports and repository files.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: environment probe, dependency planning, budget preflight.

## Handoff
OUTPUT: resource_inventory, constraints, verified_paths, dependencies, preflight_result.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
