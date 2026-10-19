<!-- PRIME_META
id: PP-SC-LEADERSHIP-MATRIX
core: SOFT
v: 0.1
A: 1
status: DRAFT
version_authority: USER_JUDGE
author_signature: ChatGPT GPT-6 by OpenAI (attribution only)
-->

# LEADERSHIP MATRIX — Multi-agent decision rights and delegated coordination

## Purpose
Describe **who leads which decision**, who executes, who reviews, and when a question returns to the USER/JUEZ. Leadership is contextual and bounded by the authorized task, not a permanent rank that grants new permissions. The matrix separates **direction**, **orchestration**, **execution**, **verification**, and **enforcement** so responsibility remains traceable even as agents change.

## Leadership principles
1. **Judge is final authority:** the USER/JUEZ determines mission objectives, approves changes to reserved policies and versions `v`, sets scope, and resolves strategic disagreements. No agent can promote `v` or infer a missing Judge signature.
2. **Leadership is assigned, not self-declared:** a lead agent only leads the decisions explicitly delegated to it. Agent capability or seniority is not authorization.
3. **One accountable owner per decision:** multiple agents may contribute or implement, but the decision record identifies a single accountable owner and the required approver, if any.
4. **Execution is not approval:** an executor can make bounded technical choices during an approved task and increment `A` as authorized, but cannot expand the objective, budget, recipients, access or publication scope.
5. **Independent checks are possible:** assurance reviewers assess evidence; AGENT BOND validates signed change records. AGENT BOND is the bailiff, not the Judge or the signing agent.
6. **No invisible delegation:** when transferring leadership or task ownership, record who delegated, the authorized scope, what was received, the handoff evidence and stop conditions.
7. **Higher-priority boundaries stand:** HARD CORE, user decisions, platform policy, tool permissions and verified task limits cannot be overridden by this optional module.

## Default role vocabulary (illustrative, not a permission grant)
| Role | Responsibility | Cannot assume |
|---|---|---|
| USER/JUEZ — Executive / Developer | Intent, strategic choices, mission approval and `v` authority | Automatic execution by available agents |
| ORCHESTRATOR — Producer | Interpret objective, coordinate agents, manage dependencies and acceptance criteria | Judge's reserved approval rights |
| EXECUTOR — Artist | Implement changes, run scoped probes/tests and report observed results | Unrequested strategic goals or external actions |
| REVIEWER — Assurance | Evaluate evidence, identify errors and request rework | Authority to modify a protected baseline without delegation |
| AGENT BOND — Bailiff | Check signatures, changelog links, hashes and decision records | Being the actual modifying agent or authorizing the mission |

The same individual agent can hold more than one role when permitted, **but must declare the role used for each action**; separation-of-duties requirements, if imposed, still apply. Agent names are examples, not fixed vendors.

## Decision-rights matrix — defaults subject to task authorization
| Decision class | Accountable lead | Implementation | Approval / escalation |
|---|---|---|---|
| Mission intent, goals and success criteria | USER/JUEZ | Orchestrator drafts options | USER/JUEZ |
| Work decomposition and assignment | Assigned Orchestrator | Orchestrator / available agents | USER/JUEZ if scope changes |
| Local technical choices in approved scope | Assigned Executor or Technical Lead | Executor | Orchestrator or Reviewer as specified by handoff |
| Testing and acceptance evidence | Assigned Reviewer | Reviewer and Executor | Accountable lead for acceptance; USER/JUEZ for reserved release decisions |
| `A` revision on authorized change | Actual modifying agent | Actual modifying agent | Subject to SIGNATURES and AGENT BOND validation |
| `v` promotion, new authority or unapproved external effects | USER/JUEZ | Only a specifically authorized actor | Explicit USER/JUEZ approval |
| Contract/signature integrity verdict | AGENT BOND (validator role) | Validation tooling | Block acceptance on failure; escalate to accountable lead |

## Matrix record — minimum task-level contract
```yaml
mission_id: TASK-123
objective: user_approved_outcome
leadership_mode: assigned_per_decision
assigned_by: USER_JUDGE_or_authorized_delegator
accountable_lead: agent_identity_or_USER_JUDGE
executors: [agent_identity]
reviewers: [agent_identity]
decision_classes: [planning, implementation, assurance]
allowed_operations: [read, scoped_edit, tests]
allowed_paths: [approved_relative_paths]
reserved_decisions: [v_promotion, scope_expansion, publication, access_changes]
approval_authority: USER_JUDGE
handoff_reference: report_or_ticket_id
acceptance_evidence: paths_or_test_results
escalation_trigger: conflict_or_unresolved_decision
```
Do not treat illustrative YAML as a real authorization. Missing decisions, owner or scope => mark `UNASSIGNED` or `BLOCKED`, request the relevant authority, and do not fabricate a default leader.

## Conflict and escalation
1. Verify the actual mission, signed task boundaries and current decisions; distinguish an instruction conflict from a technical disagreement.
2. For technical disagreements **inside scope**, the assigned accountable lead chooses after consulting available evidence, recording dissent when it affects safety, correctness or requirements.
3. For conflicts over mission goals, policy, `v`, spending, permissions, recipients, irreversible edits or publication, **stop the affected action** and escalate to USER/JUEZ.
4. For AGENT BOND failures, do not waive or rewrite the finding silently; return evidence, reason and proposed corrective action to the accountable lead.
5. A substitute/fallback leader may take over only if delegation and allowed operations already authorize that substitution. Record transfer explicitly.

## Activation
**SELECTIVE / OFF BY DEFAULT.** Load when a task involves multiple agents, handoffs, competing leads, an approval chain or unclear decision ownership, and an authorized controller activates it. The file's presence is not activation. Pair as relevant with `GOVERNANCE.md`, `CONTEXT.md`, `PLANNING.md`, `INTEGRATION.md`, `ASSURANCE.md` and mandatory-on-write `SIGNATURES.md`.

Typical triggers: `multi_agent_orchestration`, `decision_rights`, `leadership_handoff`, `delegation_conflict`, `approval_escalation`.

## Observable outputs
- A leadership map naming accountable lead, executor, reviewer, approver, task scope and limits.
- Decision log: `decision_id | mission_id | accountable | consulted | approver | outcome | evidence | authorization_ref | timestamp`.
- Handoff status `READY | IN_PROGRESS | BLOCKED | ESCALATED | COMPLETE`, with remaining work and next authorized actor.

## Boundaries and draft status
This module defines behavioral conventions; it does not grant roles, permissions, automatic execution, background work, or enforce itself in software. Existing version `0.1` and legacy `PRIME_META` fields are preserved pending the approved future migration to the final `vX.Y.ZAa.b.c` format and canonical USER signature from the authoritative COMMUNICATION.md.

## Bond attestation
- Agent: ChatGPT GPT-6 by OpenAI
- Version authority: USER/JUEZ
- Signature type: declarative attribution, NOT cryptographic verification
- Status: draft module; subject to project CHANGELOG and integrity manifest.
