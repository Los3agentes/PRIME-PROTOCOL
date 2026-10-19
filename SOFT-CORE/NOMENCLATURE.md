<!-- PRIME_META
id: PP-SC-NOMENCLATURE
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# NOMENCLATURE — Canonical terms and naming

## Purpose
Canonical terms and naming.

## Operating rules
1. Preserve user-approved names, aliases and version references; maintain a mapping where historical names exist.
2. When user wording is noncanonical, resolve meaning from domain and local context before correcting vocabulary.
3. Distinguish identifier, display name, role name and file name; avoid conflating identity with mutable labels.
4. Suggest names when asked, but never rename an approved entity or repurpose an evocative nickname without authorization.

## Activation
Load only when the current task requires this module and an authorized controller selects it. The presence of this file is not activation. HARD CORE and higher-priority instructions remain controlling.

Typical triggers: term resolution, schema naming, renaming proposals.

## Handoff
OUTPUT: term_map, canonical_name, aliases, disambiguation, naming_decision.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
