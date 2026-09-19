# AOTS⁶ — MARCO NORMATIVO DE APLICABILIDAD, TRAZABILIDAD Y OBSERVANCIA

**Identidad normativa:** AOTS6-NBF-1
**Autor/proveniencia técnica:** Alfredo Jhovany Alfaro García
**Raíz de procedencia:** AOTS6-ORIGINAL-ALFARO
**Estado:** especificación normativa y probatoria

## 1. Principio de aplicación

Este documento no pretende crear por sí mismo jurisdicción sobre terceros. Define una infraestructura para identificar, demostrar y exigir, ante la autoridad competente, las obligaciones que ya resulten aplicables conforme al derecho vigente.

R(S,O,t) = [S pertenece al ámbito de O] y [O está vigente en t] => S debe cumplir O.

La aceptación voluntaria no se modela como condición de existencia de una obligación jurídicamente aplicable.

## 2. Fuentes

Cada reclamación registra por separado la Constitución Política de los Estados Unidos Mexicanos, el tratado internacional aplicable y su estado de vigencia para México, la legislación mexicana de implementación y el acto jurídico que determine la aplicabilidad concreta.

## 3. Interpretación

Se conserva el texto oficial, artículo, párrafo, versión, fecha, reservas y declaraciones relevantes. La interpretación documenta sentido corriente, contexto, objeto y fin conforme a las reglas internacionales aplicables.

## 4. Evidencia AOTS⁶

X(t) -> Psi_A(t) -> M_A(t) -> E_A(t) -> H_A(t)

X = hecho observado; Psi_A = estado AOTS⁶; M_A = metadata; E_A = expediente; H_A = hash.

Las transformaciones conservan genealogía A -> B -> C -> D mediante parent_event_hash, source_artifact_hash, canonical_hash, transformation, timestamp y origin.

## 5. Matriz de observancia

Cada alegación contiene:

norm_id
source_instrument
source_article
applicability_basis
subject
protected_object
act_observed
territorial_connection
temporal_connection
evidence_hash
provenance_chain
requested_remedy
authority_forum
status

Estados permitidos: UNASSESSED, SUPPORTED, CONTESTED, ESTABLISHED_BY_AUTHORITY, RESOLVED.

ESTABLISHED_BY_AUTHORITY sólo puede ser emitido por la autoridad competente.

## 6. Exigibilidad

La exigibilidad se demuestra separando: existencia de la norma, vigencia, ámbito subjetivo, ámbito material, acto realizado, evidencia, incumplimiento, autoridad competente y remedio jurídicamente disponible.

## 7. Integridad

H_n = SHA256(Canonical(R_n) || H_(n-1))

Se conservan dato bruto, dato canónico, estado derivado, errores, firmas, hashes, relación parental y tiempos.

## 8. Alcance internacional

Berna, Roma, WCT, WPPT y otros instrumentos sólo se incorporan a una reclamación cuando se demuestra la conexión jurídica concreta y la disposición pertinente. El repositorio no convierte unilateralmente una disposición internacional en una obligación que su propio texto no establezca.

## 9. Resultado

hecho verificable -> norma aplicable -> obligación concreta -> evidencia -> autoridad competente -> mecanismo de observancia.

Este marco está diseñado para que una autoridad pueda incorporar, valorar o exigir la evidencia. La fuerza jurídica concreta proviene del ordenamiento y del acto de autoridad correspondiente, no de una afirmación unilateral del repositorio.
