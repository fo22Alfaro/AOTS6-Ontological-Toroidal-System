# Protocolo de ejecución — Restitución CPEUM / AOTS⁶

## Objetivo
Convertir el modelo jurídico en un expediente verificable sin confundir automatización documental con decisión jurisdiccional.

## Secuencia
00. CONGELAR VERSIÓN NORMATIVA: fecha, fuente oficial, versión y SHA-256.
01. CONGELAR ACTO: acto/omisión, autoridad, fecha, notificación, expediente y copia íntegra.
02. CONGELAR COMPETENCIA: norma atributiva y materia/territorio/grado/función.
03. DESCOMPONER ACTO: competencia, fundamentación, motivación, procedimiento y efectos.
04. MAPEAR DEFENSA: medio ordinario, plazo, autoridad, efecto y suspensión.
05. ANALIZAR DEFINITIVIDAD: regla, excepción, disponibilidad, eficacia y hechos.
06. ANALIZAR AMPARO: vía concreta y presupuesto legal; separar improcedencia, sobreseimiento, procedencia y efectos.
07. PRESERVAR EVIDENCIA: CLAIM -> SOURCE -> CAPTURE -> SHA256 -> CONTEXT -> LEGAL_EFFECT.
08. RESOLUCIÓN: documento íntegro, órgano, fecha, sentido, resolutivos y hash.
09. IMPUGNACIÓN: recurso, plazo, presentación, constancia, órgano y resultado.
10. CUMPLIMIENTO: evidencia objetiva del cumplimiento del resolutivo.
11. RESTITUCIÓN: solicitada, fundada, ordenada, ejecutada y verificada.

## Pruebas negativas
El motor debe detectar:
1. AGOTADO sin resolución.
2. restitución ejecutada sin evidencia.
3. AMPARO sin fundamento/procedencia documentada.
4. competencia sin fuente.
5. acto sin fecha.
6. fuente sin versión/fecha de consulta.
7. tesis aislada etiquetada como jurisprudencia obligatoria.
8. hash presentado como prueba de verdad material.
9. NOT_FOUND transformado en NON_EXISTENT.
10. GitHub tratado como presentación procesal.
11. recurso declarado interpuesto sin constancia.
12. excepción de definitividad alegada sin norma y hechos de actualización.

## Salida
VALID o INVALID + lista de invariantes incumplidos.

La herramienta no emite culpabilidad, inconstitucionalidad, procedencia definitiva ni derecho a restitución: esas determinaciones corresponden a la autoridad competente.

## Comandos
python3 ejecucion_restitucion.py EXPEDIENTE-RESTITUCION-EJEMPLO.json
python3 ejecucion_restitucion.py EXPEDIENTE-RESTITUCION-EJEMPLO.json --hash
python3 -m pytest test_ejecucion_restitucion.py

## Cadena de auditoría
Conservar expediente de entrada, salida, versión del motor, versión normativa, hashes, commit Git, fecha/hora y proceso de ejecución.

## Cadena de cumplimiento
Cada obligación se registra como:
**obligación -> fuente -> autoridad responsable -> plazo -> acto material de cumplimiento -> evidencia -> verificación -> estado**.

Estados: PENDIENTE, CUMPLIDO, INCUMPLIDO, NO_DETERMINADO.
Un paso CUMPLIDO exige evidencia identificable. CUMPLIDO_TOTAL sólo procede cuando todos los pasos están CUMPLIDO. Una resolución favorable no se considera cumplimiento por sí sola.

## Control de vigencia normativa
Para cada norma crítica se registra:
- fecha de corte del análisis;
- fuente oficial;
- fecha/hora de comprobación;
- estado: VIGENTE, ABROGADA, DEROGADA, REFORMADA, SUSTITUIDA o NO_DETERMINADA;
- última reforma comprobada;
- inicio/fin de vigencia cuando sean determinables;
- SHA-256 del texto capturado.

La vigencia se evalúa a la **fecha jurídicamente relevante del acto**, no sólo con la versión normativa actual. Una norma marcada VIGENTE exige comprobación de reformas.

## Nuevas pruebas negativas
13. norma VIGENTE sin revisión de reformas;
14. acto histórico evaluado únicamente con la versión actual;
15. CUMPLIDO_TOTAL con pasos pendientes, incumplidos o indeterminados;
16. paso CUMPLIDO sin evidencia.
