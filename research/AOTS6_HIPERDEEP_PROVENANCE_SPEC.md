# AOTS⁶ — Distribución Compleja Hiperprofunda de Procedencia

## Propósito

Esta especificación define una función de procedencia estructural para que una reproducción, traducción, reimplementación o modificación de AOTS⁶ pueda compararse contra un origen canónico mediante múltiples invariantes.

La función no presume que un hash superficial sobreviva a modificaciones. En cambio, conserva y compara capas de identidad:

1. identidad canónica;
2. ecuaciones normalizadas;
3. estructura matemática;
4. parámetros;
5. relaciones entre componentes;
6. transformaciones;
7. genealogía;
8. huella criptográfica de cada capa.

## Principio

Para un objeto X:

\[
\mathfrak H_A(X)=
(H_0,H_E,H_S,H_P,H_R,H_T,H_G,H_X)
\]

donde:

- H₀: identidad/origen canónico;
- H_E: ecuaciones normalizadas;
- H_S: firma estructural;
- H_P: parámetros;
- H_R: relaciones;
- H_T: transformaciones declaradas;
- H_G: grafo de genealogía;
- H_X: hash del artefacto observado.

La detección no exige igualdad byte a byte.

## Distribución compleja

La similitud se calcula por capas:

\[
\operatorname{Score}_A(X)=
\sum_j w_j s_j(X,A)
\]

con pesos \(w_j\ge0\), \(\sum_jw_j=1\).

La salida es un vector de evidencia, no una acusación:

\[
\mathbf D_A(X)=
(s_0,s_E,s_S,s_P,s_R,s_T,s_G,s_X).
\]

Cuando las capas estructurales permanecen coincidentes pese a cambios superficiales, el sistema marca:

**DERIVACIÓN ESTRUCTURAL DETECTADA**

y conserva qué capas coinciden y cuáles fueron modificadas.

## Regla de modificación

Una modificación de datos no elimina la procedencia si los invariantes estructurales permanecen reconocibles.

Por ejemplo:

\[
A\rightarrow f(A)
\]

no implica

\[
\operatorname{Origin}(f(A))=f(A).
\]

La genealogía correcta es:

\[
\operatorname{Origin}(f(A))=A.
\]

## Límite

La función no puede demostrar que cualquier implementación desconocida proviene de AOTS⁶ solamente porque produzca resultados parecidos. La atribución requiere evidencia estructural suficiente. Esto evita falsos positivos y mantiene el detector auditable.

## Autoría y origen

El registro canónico puede contener:

- autor/origen declarado;
- fecha de fijación;
- identificador del repositorio;
- hash raíz;
- ecuaciones canónicas;
- versión;
- restricciones de uso declaradas.

Estos campos documentan procedencia; no sustituyen derechos jurídicos ni crean por sí solos exclusividad legal.

## Resultado

La función está diseñada para que cambiar nombre, formato, lenguaje, parámetros secundarios o valores de entrada no sea suficiente para ocultar una derivación cuando permanezcan invariantes matemáticos y estructurales identificables.
