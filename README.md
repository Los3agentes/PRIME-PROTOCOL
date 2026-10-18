# PRIME PROTOCOL

**Status:** BOOTSTRAP / PARTIAL  
**Control reference:** `v0.0.0A0.0.0`  
**Authority:** User (Judge)

Shared behavioral-protocol architecture for ChatGPT Cloud, Codex Local, Claude and other agents. GitHub is the central protocol source; local coding projects do **not** have to be Git-linked.

## Court architecture

| Layer | Court role | Scope |
|---|---|---|
| USER | Judge | Final decisions; sole authority for `v` promotions |
| HARD CORE | Tribunal | Seven foundational behavioral contracts |
| SOFT CORE | Secretaria | Selectively loaded support protocols |
| AGENTS | Licenciados | Distinct agent roles and implementations |
| AGENT BOND | Alguacil | Contract enforcement and validation |

## HARD CORE (7 pieces)

`COMMUNICATION.md` (MASTER), `COGNITION.md`, `CREATIVITY.md`, `REFERENCES.md`, `EXECUTION.md`, `DELIVERABLES.md`, `CONTINUITY.md`.

## Approved principles

- Authorized agents may increment their file's `A` revision counter and sign edits without requesting a separate approval for every edit. Only the Judge promotes `v`.
- The revision format is `v0.0.0A0.0.0`; each position is one decimal digit (0–9). The first agent modification becomes `v0.0.0A0.0.1`, and the final allowed punch for that user version is `A9.9.9`.
- Full signature, user signature, and header apply to behavioral MD files and Python source files. Their exact format must be reused from the existing canonical `COMMUNICATION.md`.
- Other documents only need a version reference.
- `CONTINUITY.md` maintains an append-only, per-project `CHANGELOG.csv` containing complete signature data and a change report.
- AGENT BOND must reject changes to signed files without the required signatures and change report, once the validator is implemented.
- SOFT CORE is selectively loaded except mandatory protocols, including `SIGNATURES.md` on applicable writes.
- The pilot must exercise a copy of `COMMUNICATION.md` and one Python file before wider rollout.

## Bootstrap limits

This commit creates **documentation scaffolding only**. It does not publish finalized behavioral protocols or an active signature validator. The original `COMMUNICATION.md` was not available to verify its mandatory header and signature template. Until it is available, the seven conduct files, `SIGNATURES.md`, `AGENTS.md` instruction entrypoint, and validator Python are intentionally not generated or represented as operative.

See the folder READMEs for the planned layout.
