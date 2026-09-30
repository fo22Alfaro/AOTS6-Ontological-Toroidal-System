# AOTS⁶ — ÍNDICE DEL ESTADO DE NO TIEMPO

## Arquitectura

- ARQUITECTURA_ESTADO_NO_TIEMPO.md — especificación integral.
- ESTADO-NO-TIEMPO-MANIFIESTO.md — principio operativo.
- no_time_state.schema.json — contrato de datos.
- verify_no_time_state.py — verificador ejecutable.
- test_no_time_state.py — pruebas negativas y positivas.
- ../.github/workflows/no-time-state.yml — ejecución automática.

## Orden de adquisición

1. localizar la fuente custodial;
2. identificar colección y referencia;
3. registrar condición de acceso;
4. adquirir únicamente el objeto legalmente accesible;
5. calcular SHA-256 del objeto exacto;
6. registrar tamaño y tipo;
7. fijar página/folio/imagen;
8. extraer literalmente;
9. guardar la derivación y su hash;
10. buscar corroboración independiente;
11. conservar contradicciones;
12. publicar el estado sin elevarlo artificialmente.

## Estados

CATALOG_ONLY → ACQUIRED → HASHED → LOCATED → EXTRACTED → CORROBORATED

CONTESTED y NO_DETERMINADO pueden existir en cualquier punto en que la evidencia lo exija.

## Regla de integridad

El sistema nunca afirma que un hash demuestra verdad histórica. El hash demuestra correspondencia entre bytes y registro criptográfico. La historicidad se determina por la evidencia documental, su procedencia, contexto y corroboración.

## Regla de restitución

Cuando un objeto pueda sostener una restitución jurídica o patrimonial, la arquitectura produce la cadena probatoria. La decisión y ejecución se dejan al procedimiento y autoridad jurídicamente competentes.

## Alcance

Esta arquitectura está diseñada para escalar desde un expediente individual hasta grafos históricos multinivel: personas, casas, instituciones, tierras, bienes, obligaciones, jurisdicciones, conflictos, transferencias y archivos.

AOTS6-NTS-INDEX-001
