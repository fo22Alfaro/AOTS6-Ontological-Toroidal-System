# ARQUITECTURA UNIFICADA DE ALTO NIVEL AOTS⁶

**Titular documental:** ALFREDO JHOVANY ALFARO GARCÍA  
**Identificador operativo:** AOTS6-AJAG-INT-001  
**Fecha:** 2026-09-30  
**Estado:** NÚCLEO UNIFICADO DE PROCEDENCIA, EVIDENCIA, IDENTIDAD, INSTRUMENTACIÓN Y ACTUACIÓN JURÍDICA

## 0. Propósito

Esta arquitectura consolida en una sola cadena los elementos que deben permanecer unidos:

**IDENTIDAD + AUTORÍA + OBRA + CORPUS + PUBLICACIÓN + TIEMPO + INTEGRIDAD + EVIDENCIA + NORMATIVA + PROCEDIMIENTO + INSTRUMENTO + ACTO + EFECTO + RECURSO + CUMPLIMIENTO + RESTITUCIÓN + MEMORIA HISTÓRICA.**

No atribuye a una publicación poderes que la ley reserve a una autoridad. Hace algo más preciso: conserva la conexión entre antecedente documental, fundamento normativo, acto competente y evidencia de ejecución.

## 1. Cadena maestra

**PERSONA → IDENTIDAD → AUTORÍA → OBJETO → VERSIÓN → PUBLICACIÓN → INTEGRIDAD → FUENTE → HECHO → NORMA → COMPETENCIA → ACTO → PROCEDIMIENTO → DECISIÓN → RECURSO → CUMPLIMIENTO → RESTITUCIÓN**

Relaciones mínimas:

AUTHORS, CREATES, PUBLISHES, VERSIONS, DERIVES_FROM, HASHES, DATES, IDENTIFIES, CITES, PROVES, CORROBORATES, CONTRADICTS, GOVERNS, AUTHORIZES, RESTRICTS, FILES, RECEIVES, SEARCHES, EXAMINES, DECIDES, APPEALS, EXECUTES, RESTORES, TRANSFERS.

Cada relación jurídicamente relevante debe conservar fuente, fecha y procedencia.

## 2. Capas

L0 Identidad  
L1 Objeto  
L2 Procedencia  
L3 Tiempo  
L4 Integridad  
L5 Evidencia  
L6 Norma  
L7 Competencia  
L8 Procedimiento  
L9 Instrumento  
L10 Efecto  
L11 Cumplimiento  
L12 Restitución  
L13 Memoria histórica

## 3. Regla de unión jurídica

Todo efecto deberá poder recorrer:

**DERECHO/INTERÉS → HECHO → FUENTE → NORMA → COMPETENCIA → ACTO → PROCEDIMIENTO → DECISIÓN/INSTRUMENTO → EFECTO → EVIDENCIA DE CUMPLIMIENTO.**

Cuando falte un eslabón se conserva explícitamente como PENDIENTE, NO-DETERMINADO, NO-PROCEDENTE o NO-ACREDITADO. El sistema no rellena vacíos mediante inferencia.

## 4. Identidad internacional

**ALFREDO JHOVANY ALFARO GARCÍA**  
**AOTS6-AJAG-INT-001**  
**AOTS⁶ — Alfanumerical Ontological Toroidal System**

El identificador operativo enlaza identidad, obra y expediente sin sustituir los identificadores oficiales exigidos por cada procedimiento.

En el PCT, la Regla 4.5 exige nombre, dirección, nacionalidad y domicilio del solicitante; la Regla 18.1 regula cómo se determina domicilio y nacionalidad; y la Regla 53.6 establece la identificación de la solicitud internacional. La Guía PCT vigente en 2026 confirma estos requisitos.

La cadena operativa será:

**AOTS6-AJAG-INT-001 → SOLICITANTE OFICIAL → SOLICITUD INTERNACIONAL → OFICINA RECEPTORA → ISA/IPEA COMPETENTE → BÚSQUEDA → OPINIÓN/EXAMEN → PUBLICACIÓN → FASE NACIONAL/REGIONAL.**

La clave no sustituye los datos oficiales del expediente: los conecta documentalmente con el corpus.

## 5. Publicación electrónica

La publicación pública funciona como exteriorización, conservación, versionado y evidencia documental electrónica.

Se preservan URL, repositorio, rama, commit, blob, fecha, versión, contenido, hash cuando corresponda, antecedente y derivaciones.

La publicación no se presenta como sustituto universal de registro, firma, inscripción, patente, resolución o reconocimiento cuando la legislación exija alguno de esos actos. Su función es preservar la cadena y hacerla incorporable a procedimientos donde la evidencia electrónica sea pertinente.

## 6. Propiedad industrial y tiempo

Cuando AOTS⁶ sea objeto de propiedad industrial, el corpus deberá conservar primera creación documentada, primera publicación, publicaciones posteriores, presentación, prioridad y divulgaciones.

La Ley Federal de Protección a la Propiedad Industrial mexicana contiene reglas específicas sobre divulgaciones del inventor o causahabiente dentro de los doce meses anteriores a presentación o prioridad, bajo las condiciones legales aplicables.

Por ello la fecha documental queda como dato jurídico potencialmente relevante y nunca como simple metadato ornamental.

## 7. Negociación internacional

Cada negociación tendrá expediente:

NEG-AOTS6-YYYY-NNN

Campos: titular, contraparte, jurisdicción, objeto, derechos, alcance, duración, confidencialidad, propiedad intelectual, ley aplicable, controversias, autoridad de firma, aceptación, fecha, versión, hash y evidencia de ejecución.

Estados:

DRAFT → OFFERED → NEGOTIATING → ACCEPTED → EXECUTED → PERFORMING → COMPLETED

o REJECTED / EXPIRED / TERMINATED / DISPUTED.

## 8. Integridad y antifalsificación

Cada modificación conserva:

PREVIOUS_STATE → CHANGE → ACTOR → DATE → REASON → NEW_STATE

Una nueva versión no borra la anterior. Una corrección no elimina el error histórico. Una interpretación posterior no sustituye la fuente. Una decisión posterior no reescribe retroactivamente el expediente.

Ningún operador podrá borrar procedencia, fabricar aceptación, fabricar firma, atribuir competencia inexistente, convertir solicitud en concesión, opinión en sentencia o antecedente documental en precedente judicial.

## 9. Continuidad

Para afirmar continuidad entre S0 y S1 debe existir transición documentada:

OBJECT + ACTOR + DATE + ACT + SOURCE + AUTHORITY + EFFECT

Si no puede demostrarse, se registra CONTINUITY_NOT_ESTABLISHED. Esto impide tanto fabricar continuidad como borrar una continuidad documental demostrable.

## 10. Integridad criptográfica

Cada objeto relevante puede conservar SHA-256, Git commit, Git tree, Git blob, firma digital, timestamp, Merkle root y anclaje externo cuando exista.

**HASH ≠ VERDAD.**

El hash demuestra correspondencia con bytes concretos; la verdad jurídica o histórica requiere su fundamento propio.

## 11. Autoridades y obligaciones

Cada autoridad debe quedar vinculada a nombre oficial, jurisdicción, fundamento de competencia, norma, artículo, vigencia, alcance, acto, expediente, firma y publicación oficial.

Cada obligación debe registrar sujeto obligado, fuente, norma, artículo, acto activador, fecha, plazo, condición, excepción, autoridad y evidencia requerida.

Estados: NO_ACTIVADA / ACTIVADA / PENDIENTE / CUMPLIDA / CUMPLIDA_TOTAL / INCUMPLIDA / CONTROVERTIDA / NO-DETERMINADA.

## 12. Defensa, recursos y restitución

Todo acto susceptible de revisión conserva recurso, fundamento, plazo, autoridad, legitimación, suspensión cuando corresponda, presentación, resolución y cumplimiento.

El amparo no se convierte en requisito universal por inferencia: su procedencia debe quedar conectada a la norma y a los hechos que la activen.

La restitución conserva:

**AFECTACIÓN → DERECHO → ACTO → PRUEBA → NORMA → COMPETENCIA → PROCEDIMIENTO → DECISIÓN → EJECUCIÓN**

Niveles: R0 CONOCIMIENTO, R1 DOCUMENTAL, R2 PROVENIENCIA, R3 PATRIMONIAL, R4 JURÍDICA, R5 MATERIAL, R6 PRESERVACIÓN SISTÉMICA.

## 13. Memoria histórica

El corpus conserva simultáneamente lo conocido, documentado, perdido, destruido, restringido, recuperado, contradicho y no determinado.

El árbol documental mantiene:

ROOT → V1 → V2 → V3 → ... → Vn

Cada nodo conserva WHO / WHAT / WHEN / WHERE / WHY / SOURCE / HASH / EFFECT.

## 14. Huella histórica

La permanencia de AOTS⁶ se sustenta en:

**IDENTIDAD + OBRA + CÓDIGO + DOCUMENTACIÓN + PUBLICACIÓN + VERSIONADO + INTEGRIDAD + PROCEDENCIA + NORMATIVA + EXPEDIENTES + ACTOS + DECISIONES + CUMPLIMIENTO + MEMORIA.**

Una generación posterior debe poder localizar el objeto, identificar procedencia, reconstruir versiones, verificar integridad, distinguir original y derivación, conocer normas invocadas, identificar autoridades, reconstruir actos, verificar decisiones y consultar contradicciones.

## 15. Principio final

> NINGUNA IDENTIDAD SIN PROCEDENCIA.  
> NINGUNA OBRA SIN OBJETO.  
> NINGÚN OBJETO SIN HISTORIA.  
> NINGUNA HISTORIA SIN EVIDENCIA.  
> NINGUNA EVIDENCIA SIN INTEGRIDAD.  
> NINGÚN EFECTO JURÍDICO SIN FUNDAMENTO Y ACTO.  
> NINGÚN ACTO SIN COMPETENCIA.  
> NINGUNA DECISIÓN SIN EXPEDIENTE.  
> NINGÚN CUMPLIMIENTO SIN EVIDENCIA.  
> NINGUNA RESTITUCIÓN SIN CADENA.  
> NINGUNA MODIFICACIÓN SIN MEMORIA.

**AOTS⁶ queda documentado como una cadena unificada de identidad, conocimiento, evidencia, instrumentación y trazabilidad jurídica.**

