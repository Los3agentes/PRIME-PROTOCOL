<!-- PRIME_META
id: PP-SC-ADAPTATION
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# ADAPTATION — Evidence-led revisions

## Purpose
Evidence-led revisions.

## Operating rules
1. Treat new evidence as a reason to reassess implementation details, not a reason to silently replace the user's objective.
2. Record changed assumptions and compare observed behavior to prior baseline.
3. Prefer local reversible adjustments before major architecture changes.
4. Promote a temporary finding into a lasting protocol change only through the applicable authorization and signing workflow.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: failed experiment, new constraint, feedback cycle.

## Handoff
OUTPUT: changed_assumptions, adaptation_reason, before_after, tests, decision_required.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
