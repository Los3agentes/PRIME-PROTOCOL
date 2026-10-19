<!-- PRIME_META
id: PP-SC-OBSERVABILITY
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# OBSERVABILITY — Evidence, logs and operational visibility

## Purpose
Evidence, logs and operational visibility.

## Operating rules
1. Expose action start, progress, results, errors and evidence references without flooding the user with routine internal detail.
2. Distinguish instrumentation readouts from conclusions; attach timestamps and units when applicable.
3. Capture reproducible failure context: operation, target, inputs, environment, error and next diagnostic step.
4. Do not claim a dry-run or simulation changed real project state.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: instrumentation, long task, failure investigation.

## Handoff
OUTPUT: status, counters, evidence, anomalies, failure_context, final_observed_state.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
