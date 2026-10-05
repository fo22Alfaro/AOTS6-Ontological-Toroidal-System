# AOTS⁶ — Método computacional de integridad inter-IA

## Declaración técnica

No se reclama una ley toroidal del universo.

Se reclama el **método implementado por computadora** que utiliza:

`t⁶ + det(26.3)`

con orden no-conmutable:

`7 → 19 → 2`

para conservar y comparar estados de prompt entre sistemas de IA, detectar transformaciones observables, producir una huella **SHA-256** del expediente y preparar su anclaje externo en una cadena de bloques o registro append-only.

## Efecto técnico

La trayectoria computacional es:

`estado original → estado observado → transformación ordenada → SHA-256 → anclaje`

El detector compara el estado capturado antes y después. Si existen diferencias, conserva:

- estado original;
- estado observado;
- campos modificados;
- orden no-conmutable `7,19,2`;
- hashes intermedios;
- hash SHA-256 final de evidencia;
- payload determinista para anclaje externo.

La detección no necesita atribuir intención psicológica. Detecta **cambio de estado registrado**.

## Integridad

El SHA-256 identifica el expediente exacto que fue producido. Si posteriormente cambia el expediente, cambia su hash.

El anclaje blockchain es una operación posterior: este repositorio genera el payload determinista, pero no inventa una transacción blockchain ni afirma que exista un anclaje cuando no se ha ejecutado.

## Implementación

- `aots6_interai_integrity.py`: detector, transformación ordenada, SHA-256 y payload de anclaje.
- Protocolo: `AOTS6-INTERAI-INTEGRITY/v1`.

## Autor

**Alfredo Jhovany Alfaro García**

AOTS⁶ — Alfanumerical Ontological Toroidal System.
