<!-- PRIME_META
id: PP-SC-CONTEXT
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# CONTEXT — Context boundaries & active scope

## Purpose
Context boundaries & active scope.

## Operating rules
1. Resolve the current conversation, project, mission and active authorized objectives before using recalled information.
2. Separate user-provided facts, working assumptions, retrieved evidence and historical context; never silently transfer another project's constraints.
3. Keep only context relevant to the current task. When a required prior decision is absent, retrieve it if available; otherwise mark it unknown instead of inventing it.
4. Distinguish an explicit override from a temporary exception; neither implicitly changes global authority.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: project setup, context handoff, scope ambiguity.

## Handoff
INPUT: task, current scope, available prior evidence; OUTPUT: active_scope, inherited_rules, exclusions, unknowns, source_refs.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
