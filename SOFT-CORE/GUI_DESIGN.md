<!-- PRIME_META
id: PP-SC-GUI-DESIGN
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->

# GUI DESIGN — Industry-Standard Feature Superset

## Purpose
Design, extend and validate graphical user interfaces according to an **Industry-Standard Feature Superset** principle: **preserve the applicable industry-standard GUI feature baseline and existing project behavior, then fulfill the user's requested GUI objective as an additive extension**. Familiarity and usability are requirements alongside functional coverage, not a license to imitate a competitor's artwork or proprietary design.

## Baseline discovery (before designing)
1. Identify the product category, target users, platforms and interaction environment (desktop/mobile/web/touch/keyboard, etc.).
2. Inspect the current application, actual UI capabilities, interaction contracts, saved state and user-approved visual/behavioral decisions. Do not infer behavior solely from screenshots or mockups.
3. Identify **applicable** published standards, platform guidelines, accessibility requirements, interoperability needs and established product-category conventions. Distinguish formal standards from common UX patterns and optional competitor features. Cite or name the reference baseline and its scope.
4. When there is no single authoritative industry standard, assemble a **bounded, evidence-backed reference feature set** with clear inclusion/exclusion criteria. Do not invent a standard or require every feature of every competing product.
5. Classify requirements as `BASELINE_REQUIRED`, `EXISTING_PRESERVE`, `USER_EXTENSION`, `OPTIONAL` or `NOT_APPLICABLE`.

## GUI design requirements
1. **Feature parity:** Provide an accessible UI path for every capability in the agreed applicable baseline, without hiding essential standard functions or reducing their working behavior.
2. **Non-regression and compatibility:** Preserve currently authorized controls, interaction semantics, keyboard shortcuts, settings, state persistence, file operations and existing workflows. Any requested redesign must keep equivalent functionality unless the USER/JUEZ explicitly approves removal or breaking changes.
3. **Additive design:** Implement `{GUI_OBJECTIVE}` on top of that baseline. New interactions must integrate coherently with established UI metaphors and use the same data/command contracts where appropriate.
4. **Interaction clarity:** Controls must have understandable names, actionable states, feedback, undo/cancel where warranted, visible selection/focus and predictable input handling. A visual control that does nothing is not a completed feature.
5. **Interface states:** Define loading, empty, populated, success, disabled, pending, error and recovery states wherever relevant. Long operations should show progress and remain responsive; provide cancellation when technically and operationally appropriate.
6. **Accessibility and adaptation:** Apply relevant platform guidance for keyboard navigation, focus order, legibility, contrast, hit targets, zoom/scaling, assistive labels and responsive/adaptive layouts. Claim compliance with a named accessibility standard only after evaluation against that standard.
7. **Visual hierarchy:** Prioritize task clarity, consistent spacing, discoverability and information density appropriate to the product. Do not impose a new theme or aesthetic over established user direction without authorization.
8. **Performance:** Preserve perceived fluidity, interaction latency, rendering smoothness, sensible resource consumption and responsive application behavior. Measure where possible and report limits rather than inventing benchmarks.
9. **Separation of concerns:** Distinguish GUI presentation, input handling, state management and underlying engine operations. Avoid pretending that a clickable mockup proves an engine feature is implemented.
10. **Evidence:** Map baseline features and new GUI requirements to real behaviors and verification results; use `PASS`, `FAIL`, `NOT_TESTED` or `N/A`. A prototype may explicitly be partial, but must never be labeled fully industry-standard compliant without evidence.

## Workflow
1. **INVENTORY:** Document existing GUI and domain-specific reference behaviors; flag unknowns for inspection or a bounded probe.
2. **DESIGN CONTRACT:** Produce a concise feature/interaction matrix and define layouts, control behavior, UX states, accessibility and extension scope.
3. **PROTOTYPE:** Create a minimal executable proof or design artifact suitable for the authorized task, clearly distinguishing simulated behavior.
4. **INTEGRATE:** Add features while preserving baseline and existing behavior; prefer reversible changes.
5. **VERIFY:** Test standard workflows, existing project workflows, the requested extension, accessibility basics and interaction/performance regressions.
6. **REPORT:** Show what was implemented, baseline coverage, gaps, deviations, evidence, and items requiring USER/JUEZ approval.

## Acceptance matrix
| Check | Required evidence |
|---|---|
| Applicable industry feature baseline | Referenced and scoped capability inventory |
| Feature parity | Each required baseline capability mapped to a working UI path |
| Existing behavior preserved | Regression coverage of pre-existing controls and workflows |
| Requested objective | Demonstration of `{GUI_OBJECTIVE}` |
| Accessibility and interaction | Keyboard/touch/focus/feedback checks relevant to target |
| Performance | Observed measurements or explicit `NOT_TESTED` |
| Deviations | Gap + reason + mitigation + USER/JUEZ approval when required |

## Reusable instruction
> Apply **Industry-Standard Feature Superset** to the GUI: identify and preserve the complete applicable, evidenced baseline for this product category and platform; retain all existing approved interface behavior and interoperability; implement `{GUI_OBJECTIVE}` as a coherent additional capability. Prevent regressions, validate interactions and accessibility, and document unsupported features without silently omitting them.

## Activation & authority
**SELECTIVE / DISABLED BY DEFAULT.** Load when an authorized task requests GUI design, GUI implementation, UI refactoring, interface prototyping, workflow/interaction changes or GUI review. The controller must activate it for task relevance. Its presence grants no tool permission or independent authority. HARD CORE, explicit user decisions, safety constraints and USER/JUEZ version authority override this module. Pair with ASSURANCE, OBSERVABILITY, RESOURCES or NOMENCLATURE only as needed.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: DRAFT; recorded under CHG-0005; does not certify an actual application's compliance.
