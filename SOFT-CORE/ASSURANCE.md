<!-- PRIME_META
id: PP-SC-ASSURANCE
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# ASSURANCE — Tests, invariants & acceptance evidence

## Purpose
Tests, invariants & acceptance evidence.

## Operating rules
1. Write acceptance criteria before asserting completion, proportionate to risk and scope.
2. Validate structure, semantics, side effects and regressions with verifiable checks or note unavailable tests.
3. Keep a known-good baseline and recovery path for mutations that can break functionality.
4. Report PASS, FAIL, PARTIAL and NOT_TESTED distinctly; never turn a planned test into a claimed result.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: validation, release review, regression test.

## Handoff
OUTPUT: acceptance_matrix, test_evidence, blocked_checks, residual_risks.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
