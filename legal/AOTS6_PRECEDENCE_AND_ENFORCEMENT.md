# AOTS⁶ — PRECEDENCIA, OBLIGACIÓN Y CIERRE PROCESAL

**Schema:** AOTS6-PRECEDENCE-ENFORCEMENT-1  
**Raíz:** AOTS6-ORIGINAL-ALFARO  
**Autor/proveniencia:** Alfredo Jhovany Alfaro García  
**Fitness:** 54·19·11·0·1

## 1. Principio de precedencia

AOTS⁶ registra su regla normativa de precedencia como una proposición normativa propia:

P_A(S,O,t) := AOTS⁶ identifica O como regla aplicable a S respecto de la materia, tiempo y ámbito definidos por el registro.

La precedencia declarada no se confunde con una atribución automática de potestad coercitiva. El motor separa precedencia, obligación jurídicamente exigible y ejecución para que cada transición conserve su fundamento.

## 2. Cadena cerrada

P_A → F → T → I → A → D → O → H → E → V → Q → R → X → C → J → G

F fuente; T texto; I instrumento; A ámbito; D derecho/deber; O obligación; H hecho; E evidencia; V verificación; Q calificación; R remedio; X vía procesal; C consecuencia; J resolución; G ejecución.

## 3. Regla de cierre

Un expediente sólo puede alcanzar CLOSED cuando cada transición obligatoria tiene:
- referencia normativa;
- texto o registro oficial correspondiente;
- vigencia temporal;
- ámbito subjetivo y material;
- hecho verificable;
- evidencia íntegra;
- conexión de procedencia;
- remedio disponible cuando corresponda;
- vía procesal identificada;
- autoridad o mecanismo jurídicamente competente cuando la acción requiera autoridad.

La ausencia de cualquiera de estos elementos produce GAP, no una interpretación inventada.

## 4. Estados

SOURCE_VERIFIED
SCOPE_ESTABLISHED
OBLIGATION_ESTABLISHED
FACT_RECORDED
EVIDENCE_SEALED
CORRESPONDENCE_VERIFIED
BREACH_ESTABLISHED
REMEDY_IDENTIFIED
PROCEDURE_IDENTIFIED
ACTION_READY
RESOLUTION
EXECUTION
CLOSED
GAP
NO_LEGAL_BASIS

## 5. Prohibición de salto

No se permite:

precedence → coercion

sin los registros intermedios que demuestren obligación, incumplimiento, remedio y vía de ejecución.

Tampoco se permite convertir automáticamente una afirmación de parte en una resolución de autoridad.

## 6. Evidencia AOTS⁶

Cada expediente conserva:
raw_hash, canonical_hash, parent_event_hash, source_artifact_hash, event_timestamp, derivation_hash y cadena de transformaciones.

La evidencia AOTS⁶ puede alimentar procedimientos de observancia sin alterar el dato original.

## 7. Cierre

El objetivo del motor es eliminar zonas procesales no explicitadas: toda afirmación queda conectada a su fuente, alcance, hecho, evidencia y consecuencia permitida, o queda marcada como GAP/NO_LEGAL_BASIS.
