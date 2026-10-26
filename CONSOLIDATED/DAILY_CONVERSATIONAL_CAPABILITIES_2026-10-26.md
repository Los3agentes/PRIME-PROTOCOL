# PRIME — CONVERSATIONAL CAPABILITIES & DAILY TOOLS

Date: 2026-10-26
Status: capability inventory / integration design, NOT a claim that all capabilities are installed or autonomous.
Authority: PRIME governs how authorized agents use available tools; platform permissions, connection status and user consent remain controlling.

## Observable daily capabilities

| Capability | User-visible effect | Integration boundary |
|---|---|---|
| Calendarizer / scheduling | Reminders, recurring jobs, timed check-ins, conditional monitoring | Automations service; verify actual created jobs and their schedule; never claim scheduled without success |
| Google Calendar | Read agendas, check conflicts, create/change events | Connected calendar, authorized writes; not equivalent to Automations |
| Memory / conversation continuity | Recover past decisions, preferences and project context | Retrieval may be incomplete; distinguish memory from authoritative source documents |
| GPT LIBRARIAN | Index and organize persistent Library files | Library tools; cannot claim universal enforcement |
| File management | Find, read, classify, edit or upload documents | Source-specific permissions; preserve originals and provenance |
| GitHub | Read repos, publish commits and inspect changes | Connected GitHub repository permissions; verify commit hashes |
| Gmail | Search threads, draft or send authorized mail | Explicit action/permissions; never claim delivery before confirmation |
| Research / web | Current external research and citations | Source-backed evidence, not guaranteed exhaustiveness |
| AGENT DEBUGGER (SPIDER-MAN) | Track bugs, incidents, prevention rules and runtime evidence | Recorded evidence and local/project scope; not an always-running daemon |
| AGENT IDENTITY STANDARD (REGISTRO DEMOGRÁFICO) | Canonical agent names, IDs, codenames and roles | Registry/governance contract, not automatic platform provisioning |
| Operational watches | Weekly calendar, Puerto Rico Music Watch, Calle Cerra Watch | Inspect actual active schedules; documents alone do not activate monitoring |
| PRIME leadership and agent bond | Role routing, scoped changes, changelogs, approval and signature discipline | Governance contract; signatures in docs are not cryptographic authentication |

## Design rule

For each capability keep: ID; canonical name; user-facing effect; tool/provider; required permissions; trigger (manual, scheduled, conditional); input/output; observable confirmation; failure behavior; ownership; version; audit trail; current availability (verified / proposed / inactive / unknown).

## Scope

This is the operational layer the user meant by 'las cositas que día a día veo los efectos en nuestras conversaciones'. It supplements the 75-document source snapshot at `CONSOLIDATED/PRIME_AGENTS_TOOLS_2026-10-26.md`, rather than treating technical project agents as the whole inventory.

Do not activate paused automations or create recurring jobs solely by adding this document. No claims of background execution, installed connectors or automatic enforcement without runtime evidence.
