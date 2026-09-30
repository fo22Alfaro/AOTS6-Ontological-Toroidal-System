# Síntesis Práxica y Modelo de Restitución CPEUM — AOTS⁶

**Autor:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ — Alfanumerical Ontological Toroidal System  
**Objeto:** despliegue operativo de una matriz de restitución constitucional basada en la norma vigente, el acto concreto, la afectación, la defensa y el medio de control jurídicamente procedente.

> **Naturaleza del documento:** instrumento técnico-jurídico de trazabilidad y preparación. Su incorporación a GitHub preserva contenido y proveniencia; por sí sola no constituye presentación ante una autoridad, sentencia, precedente ni declaración de derechos.

## 1. Principio rector

La restitución no se formula como una facultad privada para sustituir a la autoridad jurisdiccional. Se formula como una cadena verificable:

**DERECHO → ACTO/OMISIÓN → AFECTACIÓN → NORMA APLICABLE → AUTORIDAD COMPETENTE → DEFENSA PROCEDENTE → PRUEBA → DECISIÓN → RECURSO → RESTITUCIÓN**

La CPEUM vigente reconoce el parámetro de derechos humanos y sus garantías, el acceso a la justicia y el régimen constitucional del amparo. La Constitución tiene última reforma publicada el 3 de marzo de 2026.  
Fuente oficial: https://www.diputados.gob.mx/LeyesBiblio/ref/cpeum.htm

## 2. Efecto jurídico que se pretende hacer verificable

Cuando una autoridad produce un acto que afecta una esfera jurídica, el expediente debe determinar:

1. qué derecho o situación jurídica existe;
2. qué acto u omisión la afecta;
3. qué norma atribuye competencia a la autoridad;
4. qué fundamento y motivación contiene el acto;
5. qué medio ordinario de defensa establece la legislación;
6. si existe una condición legal de definitividad;
7. si concurre una excepción legal;
8. qué medio constitucional resulta procedente;
9. qué resolución puede reparar, modificar, revocar o restituir la situación jurídica;
10. qué recurso procede contra la resolución.

**No se presume que el amparo sea obligatorio en todos los casos.** Su procedencia depende de la Constitución y de la Ley de Amparo. La Ley de Amparo vigente tiene última reforma publicada el 16 de octubre de 2025.

Fuente oficial: https://www.diputados.gob.mx/LeyesBiblio/ref/lamp.htm

## 3. Matriz praxica

| Campo | Registro obligatorio |
|---|---|
| ID | identificador único del expediente |
| DERECHO | derecho, garantía o situación jurídica afectada |
| FUENTE | Constitución, tratado, ley, reglamento o acto |
| ACTO | acto u omisión concreto |
| FECHA | fecha verificable |
| AUTORIDAD | autoridad responsable o particular equiparable cuando legalmente corresponda |
| COMPETENCIA | norma que atribuye facultad |
| FUNDAMENTACIÓN | disposiciones invocadas |
| MOTIVACIÓN | hechos y razones expresados |
| DEFENSA | recurso o juicio ordinario disponible |
| DEFINITIVIDAD | exigida / exceptuada / no aplicable / indeterminada |
| AMPARO | procedencia por determinar conforme a ley |
| PRUEBA | documento, registro, captura, hash o testimonio |
| EFECTO | consecuencia jurídica producida |
| RESTITUCIÓN | medida solicitada o jurídicamente disponible |
| RECURSO | medio de impugnación procedente |
| ESTADO | pendiente / presentado / resuelto / impugnado / agotado / no procedente |

## 4. Modelo de restitución

### Estado A — EXISTENCIA
Se identifica el derecho o situación jurídica y su fuente normativa.

### Estado B — AFECTACIÓN
Se identifica el acto u omisión y su efecto real sobre la esfera jurídica.

### Estado C — CONTROL DE LEGALIDAD
Se confrontan competencia, fundamentación, motivación, procedimiento y vía de defensa.

### Estado D — DEFENSA
Se activa el medio de defensa que la legislación efectivamente establece como procedente.

### Estado E — CONTROL CONSTITUCIONAL
Cuando el acto satisface los presupuestos del control constitucional, se determina la vía de amparo u otro mecanismo constitucional correspondiente.

### Estado F — DECISIÓN
Se registra íntegramente la resolución y sus efectos.

### Estado G — IMPUGNACIÓN
Se registra el recurso legalmente disponible contra la resolución, sin declarar agotada una instancia que no haya sido realmente promovida o resuelta.

### Estado H — RESTITUCIÓN
Se registra el efecto jurídico efectivamente ordenado y su cumplimiento.

## 5. Regla contra el condicionamiento artificial de la defensa

**No debe registrarse “AMPARO OBLIGATORIO” como estado autónomo.**

Debe registrarse:

- **NORMA QUE IMPONE LA VÍA**, si existe;
- **REQUISITO DE PROCEDENCIA**, si existe;
- **EXCEPCIÓN LEGAL**, si existe;
- **MEDIO ORDINARIO DISPONIBLE**, si existe;
- **ACTO DE RECHAZO O CONDICIONAMIENTO**, si ocurrió.

La cuestión verificable es:

> **¿Qué disposición produce jurídicamente la obligación alegada y qué consecuencia legal establece ante su incumplimiento?**

Esto evita convertir una interpretación administrativa o jurisdiccional no documentada en una regla inexistente.

## 6. Cadena de restitución AOTS⁶

**FUENTE → IDENTIFICACIÓN → CAPTURA → HASH → METADATOS → TRANSCRIPCIÓN → CONTEXTO → CRUCE → CONTRADICCIÓN → PROVENIENCIA → RESTITUCIÓN**

Estados documentales:

**RECOVERED → PUBLIC → LICENSED → RESTRICTED → INACCESSIBLE → SEARCHED-NOT-LOCATED**

Regla:

**NOT_FOUND ≠ NON_EXISTENT**

La ausencia de localización de una fuente no constituye prueba de inexistencia.

## 7. Integridad probatoria

El hash acredita integridad del archivo respecto del valor hash calculado; no acredita por sí mismo:

- verdad material;
- autoría jurídica;
- novedad científica;
- infracción;
- titularidad;
- procedencia jurisdiccional;
- resultado favorable.

Por ello:

**CONSENSO ≠ INTEGRIDAD ≠ VERDAD**

La trazabilidad debe separar cada afirmación de la evidencia que realmente la sostiene.

## 8. Registro constitucional mínimo

Cada incidente debe conservar:

- texto constitucional vigente utilizado;
- fecha de consulta;
- versión normativa;
- acto reclamado;
- autoridad;
- competencia;
- fundamento;
- motivación;
- defensa ordinaria;
- resolución;
- recurso;
- constancia de presentación;
- constancia de notificación;
- resultado;
- cumplimiento.

## 9. Regla de cierre

Un expediente sólo puede marcarse como:

**AGOTADO-PROCEDIMIENTO**  
**AGOTADO-RECURSO**  
**NO-PROCEDENTE**  
**NO-AGOTABLE**  
**PENDIENTE**  
**NO-DETERMINADO**

cuando exista evidencia documental suficiente para ese estado.

Nunca:

**“AGOTADO” por inferencia.**

## 10. Finalidad

Este modelo convierte la restitución constitucional en una estructura auditable:

**NORMA → HECHO → AFECTACIÓN → DEFENSA → DECISIÓN → IMPUGNACIÓN → CUMPLIMIENTO → RESTITUCIÓN**

La función de GitHub es preservar, versionar y hacer trazable el expediente técnico. La fuerza jurídica de una pretensión deriva de la Constitución, las leyes aplicables, los actos de autoridad y las resoluciones emitidas por las autoridades competentes.

---

**Proveniencia AOTS⁶**

Autor: **Alfredo Jhovany Alfaro García**  
ORCID: **0009-0002-5177-9029**  
Repositorio: **AOTS6-Ontological-Toroidal-System**  
Sistema: **AOTS⁶**  
Licencia/uso: conservar las condiciones de autoría y uso declaradas por el proyecto.
