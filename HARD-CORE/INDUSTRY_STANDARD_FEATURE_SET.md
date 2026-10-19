<!-- PRIME_META
id: PP-HC-INDUSTRY-STANDARD-FEATURE-SET
core: HARD
v: 0.1
A: 0
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->

# INDUSTRY STANDARD FEATURE SET — Code

## Purpose
Every code implementation governed by PRIME must meet an **Industry-Standard Feature Superset** contract: retain the applicable industry-standard baseline and existing approved functionality, then achieve the user's requested objective as an additive extension. This requirement applies to code generally (apps, libraries, tools, APIs, engines, parsers, CLI, plugins), not only to graphical interfaces.

## MUST
1. **Discover the baseline:** Identify the specific software category, environment, platform, interfaces, I/O contracts, file formats and relevant published standards or prevailing industry conventions. Distinguish formal standards from optional market conventions.
2. **Document parity:** Enumerate the applicable reference functionality with sources or direct inspection and clear acceptance criteria. Never invent an industry standard or assume every feature from every competitor is mandatory.
3. **Implement the superset:** Achieve `{OBJECTIVE}` on top of that baseline without removing, disabling, silently simplifying or degrading applicable baseline capabilities.
4. **Prevent regressions:** Preserve previously approved behavior, compatibility, public API and data/file contracts, integrations and important invariants. If a breaking change is necessary, identify it and obtain explicit scope authorization.
5. **Probe uncertainty:** Prefer inspecting actual behavior and running narrowly scoped probes rather than guessing interface or feature contracts.
6. **Report exceptions:** List conflicting, infeasible, unsupported, or inapplicable baseline requirements and the reason. Do not silently omit them or claim universal compatibility.
7. **Validate separately:** Test baseline feature parity, preservation of existing functionality, requested extension and applicable interoperability, performance, resource, safety, and reliability constraints. Mark `PASS`, `FAIL`, `NOT_TESTED`, or `N/A` with evidence; unexecuted tests are NOT_TESTED.
8. **Maintain governance:** This contract grants no new tool permissions, cannot override higher-priority requirements, and cannot promote `v` without USER/JUEZ authority.

## Acceptance contract
`Industry Baseline + Existing Functionality Preservation + Requested Objective = Required Deliverable`

Deliver: BASELINE (standard/convention and evidence), FEATURE_MATRIX (baseline/existing/new), COMPATIBILITY, EXCEPTIONS, and VERIFICATION.

## Reusable instruction
> Implement {OBJECTIVE} as an Industry-Standard Feature Superset. Identify and preserve the applicable industry-standard functional baseline and all existing approved code behavior. Add the requested functionality without silent regressions, maintain compatibility, and validate baseline parity and the objective separately. If no single standard exists, document the relevant conventions and evidence. Report unsupported requirements explicitly.

## GUI specialization
`SOFT-CORE/GUI_DESIGN.md` is a separate, selectively activated GUI-design module applying the feature-superset principle to interface controls, interactions, accessibility, responsive behavior and visual design. It supplements this code-wide HARD CORE without replacing it.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Evidence: AGENT-BOND/BOND_MANIFEST.json / CHG-0006
