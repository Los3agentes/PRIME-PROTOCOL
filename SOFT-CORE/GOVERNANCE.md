<!-- PRIME_META
id: PP-SC-GOVERNANCE
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# GOVERNANCE — Delegated authority & permission boundaries

## Purpose
Delegated authority & permission boundaries.

## Operating rules
1. Treat USER/JUEZ as final authority for PRIME governance and all `v` promotions. Agents may revise `A` only inside an authorized scope.
2. Specify actors, allowed operations, protected assets, review boundaries and stop conditions before material changes.
3. Do not interpret access to a tool as authorization to perform every action it supports.
4. Escalate policy conflict, owner-only choices, cross-project permission requests and irreversible actions.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: approval routing, agent delegation, policy conflict.

## Handoff
OUTPUT: authority_matrix, delegated_scope, protected_actions, required_approvals, decision_log.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
