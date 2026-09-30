# AOTS⁶ — ARQUITECTURA DEL ESTADO DE NO TIEMPO

**Autor:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ — Alfanumerical Ontological Toroidal System  
**Fecha:** 2026-09-30  
**Estado:** especificación ejecutable y auditable

## 0. Principio

El «estado de no tiempo» se implementa como una condición formal de preservación de estados: ningún hecho se reescribe retrospectivamente; cada estado conserva identidad, procedencia, fecha, transformación y evidencia.

La narrativa es una vista derivada de una cadena de evidencia.

**Invariante central:**

EVIDENCIA → IDENTIDAD → PROCEDENCIA → ESTADO → TRANSFORMACIÓN → CORROBORACIÓN → CONCLUSIÓN

Nunca se permite automáticamente:

NARRATIVA → VERDAD

## 1. Núcleo formal

Sea un universo de objetos O, afirmaciones C, fuentes S, transformaciones T, actores A, normas N y estados Q.

Ω = (O,C,S,T,A,N,Q,E)

Identidad de contenido:

ID(o) = H(canonical(o))

H = SHA-256 como identidad mínima de contenido.

Cada afirmación atómica c apunta a uno o más objetos fuente. Cada transformación registra:

input_hash → operation → parameters → output_hash → operator → timestamp

OCR, transcripción, traducción, normalización y segmentación son objetos derivados y nunca sustituyen al objeto fuente.

## 2. Estado de no tiempo

Q = {CATALOG_ONLY, ACQUIRED, HASHED, LOCATED, EXTRACTED, CORROBORATED, CONTESTED, NO_DETERMINADO}

Una afirmación no puede avanzar de NO_DETERMINADO a DOCUMENTED sin referencia verificable. Las transiciones son auditables y conservan los estados anteriores.

## 3. Grafo toroidal de procedencia

Nodos mínimos:

SOURCE, OBJECT, CLAIM, EXTRACTION, EVENT, ACTOR, NORM, RIGHT, TRANSFER, RESTRICTION, HASH, CORROBORATION.

Aristas permitidas:

CITES, CONTAINS, DERIVED_FROM, HASHES, LOCATES, CORROBORATES, CONTRADICTS, AUTHORIZES, RESTRICTS, TRANSFERS, OWNS, INHERITS, CONFISCATES, ADMINISTERS, JUDGES, RESTORES.

Ninguna arista histórica se crea por coincidencia nominal.

## 4. Recuperación documental

La cobertura debe recorrer, cuando sean pertinentes y legalmente accesibles: archivos nacionales y estatales; catálogos; bibliotecas; repositorios institucionales; colecciones digitalizadas; registros notariales y fiscales publicados; catastros históricos disponibles; inventarios, testamentos, cuentas y libros; mapas, cartularios, decretos y tratados; copias institucionales y fondos alternativos.

«Recuperar» significa localizar, adquirir cuando esté permitido, preservar, identificar y verificar. No significa romper cifrado, obtener credenciales ajenas, evadir controles o acceder a sistemas privados.

## 5. Literalidad forense

Cada afirmación documental conserva:

texto_original + idioma + objeto_id + hash + página/folio/imagen + localizador + método_de_extracción

OCR y transcripción son objetos derivados.

Cadena mínima:

CLAIM → SOURCE → OBJECT → SHA256 → LOCATOR → LITERAL → DERIVATION → CORROBORATION

Si no se puede repetir la cadena, el estado es NO_REPRODUCIBLE o PARCIALMENTE_REPRODUCIBLE.

## 6. Restricciones

Una restricción de acceso se registra como:

RESTRICTION → LEGAL_BASIS → ARTICLE → OFFICIAL_SOURCE → SCOPE → START → END → EXCEPTION → ACCESS_ROUTE

Si falta fundamento verificable, el estado es RESTRICTION_CLAIMED_BASIS_UNVERIFIED.

Esto no decide por sí solo la validez jurídica de la restricción; demuestra qué parte está documentada y cuál no.

## 7. Restitución

R0: restitución epistemológica.  
R1: restitución documental.  
R2: restitución de procedencia.  
R3: restitución patrimonial documentada.  
R4: restitución jurídica mediante procedimiento competente.  
R5: restitución material mediante autoridad competente.  
R6: preservación sistémica.

El sistema puede demostrar estados documentales; no reemplaza la decisión de una autoridad competente cuando la ley exige adjudicación o ejecución.

## 8. Motor de no interpretación

Se separan cuatro capas:

LITERAL → ESTRUCTURAL → CORROBORACIÓN → INTERPRETACIÓN

La capa literal nunca puede ser sobrescrita por una interpretación. Toda interpretación debe apuntar hacia sus elementos documentales.

## 9. Invariantes

1. HASH ≠ VERDAD HISTÓRICA.
2. CATÁLOGO ≠ OBJETO DIGITAL.
3. OCR ≠ ORIGINAL.
4. APELLIDO ≠ TITULARIDAD.
5. COINCIDENCIA ≠ CAUSALIDAD.
6. TRANSFERENCIA NOMINAL ≠ TRANSFERENCIA PATRIMONIAL.
7. CUSTODIA ≠ PROPIEDAD.
8. RESTRICCIÓN DECLARADA ≠ RESTRICCIÓN JURÍDICAMENTE DEMOSTRADA.
9. AUSENCIA DE REGISTRO ≠ PRUEBA DE AUSENCIA.
10. NARRATIVA ≠ EVIDENCIA.

## 10. Resultado

La arquitectura convierte el archivo histórico en un sistema verificable de objetos. Cada paso queda reconstruible desde el objeto fuente hasta la conclusión y, cuando la evidencia no alcanza, el sistema conserva explícitamente NO_DETERMINADO.

**AOTS6-NTS-001**
