<!-- PRIME_META
id: PP-SC-SIGNATURES
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->


# SIGNATURES — Mandatory signed-change attribution

## Purpose
Mandatory signed-change attribution.

## Operating rules
1. Mandatory on writes to behavioral/instruction `.md` files belonging to PRIME and to `.py` source files in the governed scope. Ordinary Markdown and other formats do not automatically require full signatures.
2. Use the existing authoritative `COMMUNICATION.md` header and USER + AGENT signature structure verbatim once its canonical source has been verified. Do not invent replacement user signatures.
3. Record the actual modifying agent identity, its authorized action, previous and new version stamps, exact changes, UTC timestamp and detailed change report. AGENT BOND is validator, not the modifying agent signature.
4. Only USER/JUEZ may authorize a `v` promotion; `A` changes are scoped authorized agent revisions, serialized so concurrent writers cannot assign the same punch.
5. Append a corresponding row to the project-specific `CHANGELOG.csv`; refer to detailed diffs/reports for substantive edits. Do not fabricate approvals or cryptographic authentication.
6. For other documents, keep a version reference without imposing a full signature; automatic bookkeeping must not recurse indefinitely.

## Activation
MANDATORY when writing in-scope PRIME behavioral `.md` or governed `.py` source, subject to available tooling. For other work, load only on a relevant audit/review task. The draft cannot claim active enforcement until the final canonical header and validator are implemented.

Typical triggers: behavioral MD write, Python source write, signed change review.

## Handoff
OUTPUT: canonical_header, user_signature, agent_signature, version_chain, changelog_record, detailed_report; STATUS: DRAFT until canonical header and revised validator are verified.

## Boundaries
Do not extend tool permissions, self-authorize unrelated actions, silently revise `v`, override HARD CORE, or confuse a design draft with an implemented validator.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; documented in project CHANGELOG and integrity manifest after registration.
