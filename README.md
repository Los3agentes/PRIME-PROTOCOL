# PRIME PROTOCOL — v0.1 (draft package)

Shared behavioral protocols and agent governance system.

**Estado:** borrador de implementación preparado a partir de acuerdos aprobados en conversación. No representa una publicación aprobada por el JUEZ ni reemplaza instrucciones superiores del entorno. Repositorio de referencia: `Los3agentes/PRIME-PROTOCOL` (este ZIP no modifica GitHub).

## Arquitectura

- `HARD-CORE/`: 7 contratos base, siempre cargados cuando PRIME está activado: COMMUNICATION, COGNITION, CREATIVITY, REFERENCES, EXECUTION, DELIVERABLES, CONTINUITY.
- `SOFT-CORE/`: carga selectiva. `AUTONOMOUS_ACTION.md` es un módulo de ejecución autónoma **opt-in**, nunca concedido por el mero hecho de que el archivo exista.
- `AGENTS/`: autoridad, roles y fronteras.
- `AGENT-BOND/`: reglas de firma, reporte, manifiesto hash y validador.
- `PROJECTS/PRIME-PROTOCOL/CHANGELOG.csv`: registro de cambios de este proyecto. Cada proyecto que adopte PRIME mantiene el suyo.
- `PROJECT-TEMPLATES/`: plantillas para incorporar PRIME a otros proyectos.
- `PILOT/`, `TESTS/`: piloto acotado sobre `COMMUNICATION.md` y un archivo Python, con pruebas.

## Jerarquía y límites

1. Las instrucciones superiores de la plataforma, la ley aplicable y los límites de las herramientas prevalecen.
2. JUEZ (usuario/owner) es la autoridad de las versiones `v` de PRIME.
3. Agentes autorizados pueden editar dentro de un scope acotado e incrementar `A` en esos archivos sin aprobación por cada edición.
4. `AGENT BOND` requiere rastro de quién cambió qué, autorización, reporte y consistencia de integridad. Sus firmas aquí son **declarativas**, no autenticación criptográfica.
5. SOFT CORE solo se carga por necesidad y permiso; si hay conflicto no puede sobreescribir HARD CORE silenciosamente.

## Puesta en marcha

```bash
python scripts/validate_bond.py .
python -m unittest discover -s TESTS -v
python PILOT/communication_worker.py 'necesitamos un reporte ejecutivo'
```

## GitHub — conexión verificada y reconciliación pendiente (2026-10-19)

- **Repositorio privado:** `Los3agentes/PRIME-PROTOCOL` — https://github.com/Los3agentes/PRIME-PROTOCOL
- **Rama:** `main`.
- **Commit de bootstrap verificado:** `2b1a9d2429c31cb385c9f4a324642980679493df`.
- **Permisos observados:** lectura y escritura desde la integración GitHub de ChatGPT.
- **Relación de copias:** el repositorio remoto contiene por ahora un **índice/scaffold** (README, índices de los componentes y CSV vacío). Esta Library contiene un borrador funcional **más completo**: siete HARD CORE, soft core AUTONOMOUS ACTION, pruebas, scripts y registros de AGENT BOND. **No son copias sincronizadas**. Esta actualización no sube los archivos locales al repositorio y no los reemplaza por scaffolds.

### Decisiones aprobadas para la siguiente migración (aún NO implementadas en este borrador)

1. **Estructura:** 7 HARD CORE; SOFT CORE selectivo salvo protocolos obligatorios; AGENTS (licenciados); AGENT BOND (alguacil); usuario/JUEZ como autoridad final del Tribunal.
2. **Autoridad:** agentes pueden incrementar el contador `A` y firmar cambios dentro de una tarea autorizada sin aprobación adicional; solo el JUEZ promueve el contador `v`.
3. **Firmas:** firmas completas obligatorias para MD de conducta PRIME y Python `.py`, con encabezado, firma del JUEZ y firma de agente real/descriptivo. Otros documentos requieren únicamente una referencia de versión.
4. **Formato definitivo de versión:** `v0.0.0A0.0.0` → `v0.0.0A0.0.1` ... `v0.0.0A9.9.9`; nueva versión `v0.0.1A0.0.0` únicamente tras autorización del JUEZ. Las tres posiciones de cada segmento son dígitos individuales.
5. **Continuidad:** un `CHANGELOG.csv` por proyecto, con firma, versión anterior, resumen y `change_report` detallado por modificación; sin sobreescritura silenciosa de registros.
6. **Cumplimiento:** AGENT BOND deberá rechazar cambios sujetos a firma que carezcan de ponche válido, atribución y reporte.
7. **Piloto:** validar primero una copia de `COMMUNICATION.md` y un archivo Python antes de aplicar el contrato en todos los archivos.

**Incompatibilidades explícitas de esta copia preliminar:** `VERSION.json` mantiene `v: "0.1"`; las cabeceras `PRIME_META` aún usan un `A` entero; `CHANGELOG.csv` tiene el esquema heredado de 9 columnas, con reportes JSON vinculados. Los scripts existentes validan **esa** estructura, no la numeración ni la firma definitiva aprobadas. El `HARD-CORE/COMMUNICATION.md` incluido es un borrador del paquete y NO se ha verificado como copia del `COMMUNICATION.md` original que define el encabezado canónico. Estas diferencias exigen una migración posterior con prueba de compatibilidad y aprobación del JUEZ para promocionar `v`.

**Estado operativo actual:** este repositorio de Library se mantiene como borrador `0.1`; enlace GitHub verificado; sincronización bidireccional, nuevo formato de firmas y validador definitivo pendientes. No interpretar la actualización documental como certificación del cumplimiento futuro.

## SOFT CORE — catálogo completo (2026-10-19)

Se agregaron 13 módulos de borrador a `SOFT-CORE/` sin alterar `AUTONOMOUS_ACTION.md`:

- `CONTEXT.md` — alcance y frontera de contexto.
- `GOVERNANCE.md` — autorización, delegación y decisiones reservadas.
- `RESOURCES.md` — capacidades, dependencias y preflight.
- `OBSERVABILITY.md` — evidencia, progreso, errores y visibilidad.
- `INTEGRATION.md` — interoperabilidad y handoffs entre agentes.
- `ASSURANCE.md` — calidad, pruebas, evidencia de aceptación.
- `PLANNING.md` — secuenciación por tareas y dependencias.
- `ADAPTATION.md` — revisiones basadas en resultados observados.
- `NOMENCLATURE.md` — nombres canónicos, alias, roles e identificadores.
- `LORE.md` — contexto narrativo e identidad de los proyectos.
- `POPCULTURE.md` — referencias culturales como inspiración.
- `CROSS_REFERENCES.md` — vínculos tipados y trazabilidad de referencias.
- `SIGNATURES.md` — obligatoriedad condicional en escrituras de MD de conducta y Python.

**Ampliación CHG-0004:** `LEADERSHIP_MATRIX.md` — liderazgo por decisión, asignación de roles, responsables y aprobadores, coordinación entre agentes y escalamiento al JUEZ. Se activa selectivamente y no concede permisos por sí solo.

Todos se documentan como `DRAFT` y conservan la versión heredada `0.1` del paquete. Su existencia no concede permisos ni obliga a cargarlos en todas las conversaciones. `SIGNATURES.md` se declara obligatorio solo cuando una escritura está dentro de su alcance; la firma final y el validador que la haga cumplir continúan pendientes de migración según el `COMMUNICATION.md` original.

## Tras modificar archivos de esta copia

Usar `record_change.py` sobre archivos versionados cambiados, con `authorization-id` real y actor real. El script eleva automáticamente el contador `A` de protocolos cambiados y genera nueva evidencia de cambios. No eleva `v` salvo autorización declarada del JUEZ.

```bash
python scripts/record_change.py . --actor codex --authorization-id TASK-123 --reason 'Ajuste autorizado al alcance'
python scripts/validate_bond.py .
```

Para cambios de versión formal, JUEZ debe aportar su autorización fuera de banda y registrarla:

```bash
python scripts/record_change.py . --actor juez --authorization-id JUEZ-APPROVAL-001 --judge-version 0.2 --reason 'Versión aprobada por JUEZ'
```

`--authorization-id` y `--judge-version` registran declaraciones; **no prueban** criptográficamente identidad ni autorización. Para proteger una rama real, combinar con permisos de GitHub, reviews y commits firmados.

## Alcance no asumido

- No se crea trabajo periódico ni se obtienen permisos externos automáticamente.
- No se escribe en el repositorio remoto desde este paquete.
- Se conserva la regla de una versión mayor/menor `v` bajo autoridad del JUEZ y revisiones agentivas `A` dentro de la autorización.
