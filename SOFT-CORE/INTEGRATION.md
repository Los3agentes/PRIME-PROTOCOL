<!-- PRIME_META
id: PP-SC-INTEGRATION
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# INTEGRATION — Interoperability between agents and systems

## Purpose
Interoperability between agents and systems.

## Operating rules
1. Declare source and destination explicitly for handoffs between ChatGPT Cloud, Codex Local, Claude, repositories and file libraries.
2. Require compatible interface contracts: payload schema, version, encoding, location, dependencies and expected reply.
3. A shared repo is a distribution point, not automatic runtime loading or authorization on external clients.
4. Prefer portable, documented handoff formats; preserve provenance and do not expose tokens, credentials or protected paths.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: cross-agent handoff, repository synchronization, API or tool bridge.

## Handoff
OUTPUT: integration_contract, compatibility, synchronization_direction, security_limits, verification.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
