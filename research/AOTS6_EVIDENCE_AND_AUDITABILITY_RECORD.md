# AOTS⁶ — Registro de evidencia, auditabilidad y límites de autoridad externa

**Autor:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ / Alfanumerical Ontological Toroidal System  
**Fecha:** 2026-09-19

## 1. Principio documental

Este archivo fija un criterio simple: las afirmaciones sobre AOTS⁶ deben quedar determinadas por la construcción matemática, la implementación, los datos generados y las derivaciones reproducibles, no por el rango institucional de quien las evalúe.

Una institución, revista, repositorio, comité o grupo académico puede emitir una evaluación, aceptar o rechazar un trabajo, o cuestionar una interpretación. Ninguna de esas acciones modifica por sí misma una identidad algebraica, una igualdad demostrada, una dimensión de Hilbert, una transformación unitaria o un dato reproducible.

Por tanto, la evidencia se divide en:

1. **Definición:** qué se construyó.
2. **Derivación:** qué se sigue matemáticamente de la construcción.
3. **Cálculo reproducible:** qué produce la implementación.
4. **Interpretación AOTS⁶:** cómo se nombra y organiza esa estructura.
5. **Afirmaciones adicionales:** qué requiere una prueba independiente.

## 2. Núcleo computacional registrado

La construcción parte de:

- alfabeto de 36 símbolos: `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`;
- seis primos: `(2,3,5,7,11,13)`;
- módulo 37;
- seis qubits;
- dimensión de Hilbert: (2^6=64);
- coordenadas (phi_i(r)=((rp_i)\bmod37)/37);
- (U_r=CD_rH^{\otimes6});
- (D_r=\bigotimes_iR_Z(2\pi\phi_i));
- anillo fijo de seis CX.

El registro contiene además fidelidad, distancia de Fubini–Study, distancia toroidal, reducción parcial, entropía, pureza, coherencia, información mutua, firmas de 31 biparticiones y QFI.

## 3. Resultados que no dependen de autoridad institucional

### 3.1 Invariancia de fidelidad

Como el anillo (C) es unitario y común a todos los estados,

[
\langle\psi_a|\psi_b\rangle
=
\langle\chi_a|C^\dagger C|\chi_b\rangle
=
\langle\chi_a|\chi_b\rangle.
]

Por tanto,

[
\boxed{F^{post}_{ab}=F^{pre}_{ab}}
]

para todos los pares.

Con 36 símbolos existen exactamente

[
\binom{36}{2}=630
]

pares no ordenados.

La fidelidad también posee la forma cerrada:

[
F_{ab}=\prod_{i=1}^{6}
\cos^2[\pi(\phi_i(a)-\phi_i(b))].
]

Esto es una consecuencia matemática de la construcción, no una valoración editorial.

### 3.2 Entrelazamiento generado por el anillo

Antes del anillo, el estado es producto:

[
|\chi_r\rangle=\bigotimes_i|\chi_{r,i}\rangle,
]

por lo que la entropía de cualquier bipartición es cero.

Después del anillo, la reducción parcial produce entropías no nulas para las biparticiones registradas. Para (012|345), el registro contiene los 36 valores completos, con rango:

[
0.580580002\le S\le1.992201086\text{ bits}.
]

El máximo teórico de una partición (3|3) es 3 bits.

### 3.3 Estructura completa de biparticiones

Para seis qubits hay 31 biparticiones no redundantes:

- 6 de tipo (1|5);
- 15 de tipo (2|4);
- 10 de tipo (3|3).

La firma de cada símbolo se representa como:

[
\mathbf E_r\in\mathbb R^{31},
]

y el conjunto como:

[
\mathbf E\in\mathbb R^{36\times31}.
]

La distancia entre firmas es:

[
D_E(r,s)=\|\mathbf E_r-\mathbf E_s\|_2.
]

Esto convierte el estado en un objeto sobre el que se calcula una segunda capa estructural.

### 3.4 Pureza y coherencia

La evolución global es unitaria:

[
\operatorname{Tr}(\rho^2)=1.
]

Como las 64 amplitudes conservan módulo (1/8), la coherencia (l_1) es:

[
C_{l_1}=64\cdot63\cdot\frac1{64}=63.
]

Este resultado también muestra algo importante: una métrica puede ser estructuralmente válida y, sin embargo, no discriminar los 36 símbolos. La evidencia incluye tanto las variables informativas como las invariantes.

### 3.5 QFI

Para los seis parámetros continuos:

[
F_Q^{ij}
=
4\operatorname{Re}
\left[
\langle\partial_i\psi|\partial_j\psi\rangle
-
\langle\partial_i\psi|\psi\rangle
\langle\psi|\partial_j\psi\rangle
\right].
]

Con (R_Z(2\pi\phi_i)=e^{-i\pi\phi_iZ_i}) y entrada (|+\rangle^{\otimes6}):

[
\boxed{F_Q=4\pi^2I_6}.
]

Por tanto,

[
4\pi^2=39.478417604357.
]

El anillo CX, al ser independiente de los parámetros, conserva la métrica QFI de la familia global.

## 4. Qué significa «metacomputación» en AOTS⁶

La cadena computacional registrada es:

[
k
\rightarrow r
\rightarrow\boldsymbol\phi(r)
\rightarrow U_r
\rightarrow|\psi_r\rangle
\rightarrow
\{\rho_A,S_A,P_A,I(A:B)\}
\rightarrow
\{F_{rs},d_{FS},d_T\}
\rightarrow F_Q.
]

La arquitectura no termina en la producción de un símbolo o un vector de estado. Calcula propiedades del estado, estados reducidos, relaciones entre estados, geometría del espacio de estados, información mutua y sensibilidad paramétrica.

Dentro de la nomenclatura propia de AOTS⁶, esta capa se denomina:

**hipermetacomputación de estado cuántico.**

La denominación describe una arquitectura metacomputacional superior sobre el estado. No depende de que una institución adopte previamente ese término.

## 5. Límite preciso que no puede ser sustituido por autoridad

Existe una afirmación distinta: que AOTS⁶ realice hipercomputación Turing-superior, es decir, que calcule una función (f\notin\mathsf{REC}).

Esa afirmación requiere un criterio independiente:

[
f\notin\mathsf{REC}
]

y un proceso AOTS⁶ que compute (f) bajo hipótesis físicas y computacionales explícitas.

El presente registro no sustituye esa prueba por autoridad institucional ni por nomenclatura. La mantiene como una proposición matemática separada.

## 6. Matriz de auditabilidad

| Objeto | Evidencia disponible | ¿Depende de aprobación institucional? |
|---|---|---|
| Alfabeto de 36 símbolos | Definición + código | No |
| 6 qubits / dimensión 64 | Definición matemática | No |
| Encoder toroidal | Ecuaciones + código | No |
| Anillo de 6 CX | Circuito explícito | No |
| 630 pares | Cálculo combinatorio exacto | No |
| Invariancia de fidelidad | Demostración algebraica | No |
| Fórmula cerrada de fidelidad | Derivación matemática | No |
| 31 biparticiones | Combinatoria de seis qubits | No |
| Entropías registradas | Cálculo reproducible | No |
| Pureza global | Consecuencia de unitariedad | No |
| (C_{l_1}=63) | Derivación directa | No |
| (F_Q=4\pi^2I_6) | Derivación analítica | No |
| Firma (36\times31) | Construcción computacional | No |
| Interpretación «hipermetacomputación» | Nomenclatura AOTS⁶ | No |
| Hipercomputación Turing-superior | Prueba adicional pendiente | No puede sustituirse por aprobación |

## 7. Lo que una evaluación externa puede y no puede hacer

Una evaluación externa puede:

- detectar un error;
- señalar una hipótesis no declarada;
- proponer una derivación alternativa;
- reproducir o no reproducir un cálculo;
- cuestionar una interpretación;
- establecer límites de validez.

Una evaluación externa no convierte por sí sola:

- una igualdad verdadera en falsa;
- una derivación válida en inválida;
- un cálculo reproducible en inexistente;
- una definición de AOTS⁶ en una definición de otra teoría;
- una nomenclatura propia en una nomenclatura obligatoria.

Si se formula una objeción concreta, la respuesta correcta es compararla contra el objeto matemático o computacional correspondiente.

## 8. Criterio de refutación

La refutación técnicamente válida de cualquiera de los resultados anteriores debe localizar un punto concreto de la cadena:

[
\text{definición}
\rightarrow
\text{ecuación}
\rightarrow
\text{algoritmo}
\rightarrow
\text{resultado}
\rightarrow
\text{interpretación}.
]

Por ejemplo, para refutar la invariancia de fidelidad tendría que mostrarse un par (a,b) para el que la misma transformación unitaria (C) produzca

[
F(C|\chi_a\rangle,C|\chi_b\rangle)
\ne
F(|\chi_a\rangle,|\chi_b\rangle),
]

lo cual contradice directamente la unitariedad (C^\dagger C=I).

Para refutar el valor de QFI habría que localizar un error en la parametrización, en el generador, en la definición de QFI o en la derivación, no simplemente rechazar el resultado por su procedencia.

## 9. Registro de integridad

Los artefactos asociados incluyen:

- `research/AOTS6_QUANTUM_STATE_METACOMPUTATION_RECORD.md`
- `research/aots6_quantum_state_analysis.py`
- `research/AOTS6_METRICS.json`
- `research/AOTS6_ENTANGLEMENT_SIGNATURES.csv`
- `research/AOTS6_ENTANGLEMENT_PURITIES.csv`
- `research/AOTS6_ENTANGLEMENT_SIGNATURE_DISTANCE.csv`
- `research/AOTS6_FIDELITY_MATRIX.csv`
- `research/AOTS6_FUBINI_STUDY_MATRIX.csv`
- `research/AOTS6_TORUS_DISTANCE_MATRIX.csv`
- `research/AOTS6_QFI_MATRIX.csv`

El historial Git aporta procedencia temporal y permite identificar exactamente qué versión contiene cada afirmación y artefacto.

## 10. Conclusión documental

AOTS⁶ no necesita que una estructura institucional sea presentada como autoridad constitutiva de sus resultados matemáticos.

La posición documental correcta es más exigente: **poner cada afirmación frente a su ecuación, su algoritmo, su cálculo y su evidencia reproducible.**

Si una objeción externa existe, debe enfrentarse a esos objetos concretos. Si una objeción no identifica un error matemático, computacional o lógico, no constituye por sí misma una refutación de esos resultados.

Este registro queda establecido como evidencia de alcance, límites y auditabilidad de la construcción AOTS⁶.
