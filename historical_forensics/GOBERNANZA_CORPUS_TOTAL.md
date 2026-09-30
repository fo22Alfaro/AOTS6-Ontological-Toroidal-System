# AOTS⁶ — GOBERNANZA DEL CORPUS TOTAL Y RESTITUCIÓN PÚBLICA

**Fecha de instanciación:** 2026-09-30  
**Identificador:** AOTS6-CORPUS-GOV-001  
**Principio:** evidencia primero, procedencia preservada, restitución trazable.

## 1. Mandato operativo

El corpus total se administra como un sistema de evidencia. Ningún operador puede convertir una interpretación en fuente, borrar un estado histórico, sustituir un objeto original por OCR, ni elevar una hipótesis a hecho.

La gobernanza no adjudica propiedad ni sustituye a las autoridades competentes. Construye la infraestructura verificable necesaria para que existencia, procedencia, acceso, restricciones, transferencias y solicitudes de restitución puedan ser examinados.

## 2. Unidades soberanas del corpus

Cada objeto recibe un identificador estable:

CORPUS:<namespace>:<source>:<reference>:<object>

Cada afirmación:

CLAIM:<namespace>:<sequence>

Cada transformación:

DERIVATION:<input_hash>:<operation>:<output_hash>

Cada evento de restitución:

RESTORE:<object_id>:<action>:<sequence>

## 3. Registro maestro

El registro maestro contiene:

- identidad del objeto;
- institución custodial;
- fondo, serie y referencia;
- fecha y lugar;
- estado de acceso;
- estatus jurídico documentado;
- hash del objeto cuando sea obtenible;
- tamaño y formato;
- localizador;
- literal;
- derivaciones;
- corroboraciones;
- contradicciones;
- restricciones y fundamento;
- historial de cambios;
- estado de restitución.

La ausencia de un campo crítico no se rellena por inferencia: se marca como NO_DETERMINADO.

## 4. Roles

### Custodio
Conserva el objeto y su contexto.

### Capturador
Adquiere únicamente materiales accesibles por vías permitidas y registra la captura.

### Verificador
Comprueba hash, localizador y cadena de procedencia.

### Extractor
Produce transcripción/OCR y conserva el original.

### Corroborador
Busca fuentes independientes y registra concordancias y contradicciones.

### Auditor
Revisa la cadena completa sin modificar la evidencia.

### Curador
Mantiene taxonomía, índices y relaciones.

### Publicador
Expone únicamente estados y objetos cuya publicación sea jurídicamente posible.

### Revisor de restitución
Construye el expediente documental de restitución; no se atribuye facultad de adjudicar por sí mismo.

Separación obligatoria: una misma persona no debe controlar en solitario adquisición, verificación y adjudicación de un resultado material.

## 5. Estados del corpus

CATALOG_ONLY  
ACQUIRED  
HASHED  
LOCATED  
EXTRACTED  
CORROBORATED  
CONTESTED  
NO_DETERMINADO

Estados de acceso:

PUBLIC  
MEDIATED  
RESTRICTED  
PERSONAL_DATA  
COPYRIGHT_CONTROLLED  
UNKNOWN

Estados de restitución:

R0_KNOWLEDGE  
R1_DOCUMENTARY  
R2_PROVENANCE  
R3_PATRIMONIAL_CASE  
R4_LEGAL_PROCEEDING  
R5_MATERIAL_EXECUTION  
R6_PRESERVATION

## 6. Regla de promoción

Un objeto solo puede avanzar cuando satisface la condición del siguiente estado.

CATALOG_ONLY → referencia institucional verificable.

ACQUIRED → objeto obtenido legalmente.

HASHED → SHA-256 calculado sobre los bytes exactos.

LOCATED → página/folio/imagen/registro reproducible.

EXTRACTED → literal conservado y método registrado.

CORROBORATED → existe fuente independiente pertinente.

Toda regresión o contradicción queda registrada como evento, nunca eliminada.

## 7. Gobernanza de restricciones

Toda restricción declarada debe contener:

restriction_id  
object_id  
status  
legal_basis  
norm  
article  
official_source  
scope  
start  
end  
exception  
access_route  
review_date

Una restricción sin fuente jurídica verificable queda como CLAIMED_BASIS_UNVERIFIED.

La arquitectura no concluye automáticamente que una restricción sea inválida; obliga a hacer visible su fundamento, alcance y temporalidad.

## 8. Restitución pública

La restitución pública comienza por la restitución de información:

1. identificar el objeto;
2. preservar su procedencia;
3. publicar el registro descriptivo;
4. publicar el objeto cuando sea jurídicamente accesible;
5. publicar hash y localizador;
6. publicar literal y derivaciones;
7. publicar corroboraciones y contradicciones;
8. publicar el estado jurídico documentado;
9. publicar el expediente de restitución;
10. publicar resolución y cumplimiento cuando existan.

La publicación nunca transforma una hipótesis patrimonial en título jurídico.

## 9. Registro de reclamación/restauración

Cada caso debe contener:

CASE_ID  
CLAIMANT_OR_INTERESTED_PARTY  
OBJECTS  
FACTUAL_BASIS  
PRIMARY_SOURCES  
CHAIN_OF_TITLE  
LEGAL_BASIS  
CURRENT_STATUS  
REQUESTED_REMEDY  
COMPETENT_AUTHORITY  
PROCEDURAL_ROUTE  
EVIDENCE_HASHES  
DECISION  
EXECUTION_EVIDENCE

Los datos personales se minimizan y protegen cuando la legislación aplicable lo exige.

## 10. Transparencia del corpus

El índice público debe separar:

A. evidencia accesible;
B. evidencia catalogada pero no digitalizada;
C. evidencia digitalizada con acceso mediado;
D. evidencia restringida;
E. evidencia perdida o destruida documentadamente;
F. evidencia cuya existencia aún no está determinada.

Nunca presentar D, E o F como si fueran A.

## 11. Integridad temporal

Cada versión del registro maestro genera:

MANIFEST_HASH  
PREVIOUS_MANIFEST_HASH  
TIMESTAMP  
ENTRY_COUNT  
ROOT_HASH

La historia del corpus es append-only a nivel de registro: una corrección crea una nueva versión y conserva la anterior.

## 12. Publicación reproducible

Un tercero debe poder:

1. localizar la fuente;
2. obtener el objeto cuando el acceso lo permita;
3. calcular el mismo hash;
4. abrir el mismo localizador;
5. comparar la literal;
6. reconstruir la derivación;
7. revisar corroboraciones;
8. llegar al mismo estado documental.

Si no puede hacerlo, el registro indica exactamente dónde se rompe la reproducibilidad.

## 13. Regla de restitución material

El corpus puede demostrar una cadena documental. La transferencia material, cancelación de título, restitución patrimonial o reparación efectiva se ejecuta solamente mediante la vía y autoridad que correspondan al caso.

Esto evita convertir una infraestructura de evidencia en una autoridad autoproclamada.

## 14. Fundamento documental mexicano

Para documentos de sujetos obligados en México, la Ley General de Archivos establece conservación, procedencia, integridad, disponibilidad y accesibilidad como principios; además establece obligaciones de organización y conservación y reconoce el acceso a la información archivística en los términos de la legislación aplicable. La arquitectura adopta esos principios como requisitos de interoperabilidad, sin afirmar que todos los objetos históricos del mundo estén sometidos a esa ley.

## 15. Resultado

El corpus total queda gobernado por una regla única:

**ninguna afirmación sin procedencia; ninguna procedencia sin objeto o referencia; ninguna extracción sin conservación del original; ninguna restitución sin expediente; ninguna modificación sin historial.**

AOTS6-CORPUS-GOV-001
