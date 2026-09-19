# AOTS⁶ — Registro integral de hipermetacomputación de estado cuántico

**Autor:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ / Alfanumerical Ontological Toroidal System  
**Fecha del registro:** 2026-09-19

## 1. Objeto y criterio de evidencia

Este registro consolida la línea desarrollada hasta esta fase: codificación toroidal de 36 símbolos, estados de seis qubits, anillo CX, fidelidad, geometría, entrelazamiento, 31 biparticiones, firmas completas, pureza, coherencia, mutual information, QFI y extensión metacomputacional.

Se separan cuatro capas: **definición**, **derivación matemática**, **cálculo reproducible** e **interpretación AOTS⁶**.

El nombre operativo «hipermetacomputación de estado cuántico» se emplea aquí para el cálculo jerárquico de propiedades y relaciones de estados. No se presenta como demostración de hipercomputación en el sentido estricto de computar funciones no Turing-computables. La literatura distingue ambas cuestiones y las propuestas de quantum hypercomputation han recibido críticas de realizabilidad física.

## 2. Encoder toroidal

Alfabeto:
`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`|Σ|=36`.

Primos:
`P=(2,3,5,7,11,13)`.

Módulo:
`m=37`.

Para `k=0,...,35`:
[
r=k+1,qquad
phi_i(r)=rac{(rp_i)\bmod37}{37}.
]

El registro es:
[
mathcal H=(mathbb C^2)^{otimes6},qquad dimmathcal H=64.
]

El circuito es:
[
U_r=C D_rH^{otimes6},
qquad
D_r=igotimes_{i=1}^6R_Z(2piphi_i).
]

`C` es el anillo de seis CX:
`0→1→2→3→4→5→0`.

## 3. Fidelidad: resultado estructural exacto

Definiendo:
[
|chi_rangle=D_rH^{otimes6}|0^6angle,qquad
|psi_rangle=C|chi_rangle,
]
la unitariedad de `C` da:
[
langlepsi_a|psi_bangle=langlechi_a|chi_bangle.
]

Por tanto:
[
oxed{F^{post}_{ab}=F^{pre}_{ab}}
]
para los 36×36 pares.

Hay:
[
inom{36}{2}=630
]
pares no ordenados.

La fórmula cerrada es:
[
oxed{
F_{ab}=prod_{i=1}^6
cos^2[pi(phi_i(a)-phi_i(b))]
}
]

El script adjunto comprueba la invariancia numéricamente y genera la matriz completa.

## 4. Geometría

Distancia toroidal:
[
d_T(a,b)=
sqrt{sum_imin(|phi_i(a)-phi_i(b)|,1-|phi_i(a)-phi_i(b)|)^2}.
]

Ángulo de Fubini–Study:
[
d_{FS}(a,b)=arccossqrt{F_{ab}}.
]

Localmente:
[
Fsimeq1-pi^2d_T^2,qquad d_{FS}simeqpi d_T.
]

La distancia toroidal no determina por sí sola la fidelidad global.

## 5. Entrelazamiento

Antes de `C`, cada estado es producto:
[
|chi_rangle=igotimes_i|chi_{r,i}angle,
]
por lo que:
[
S(ho_A)=0.
]

Después de `C`:
[
ho_A=operatorname{Tr}_{ar A}(|psi_ranglelanglepsi_r|),
qquad
E_A(r)=-operatorname{Tr}(ho_Alog_2ho_A).
]

Se evaluaron las 31 biparticiones no redundantes de seis qubits:

- 6 de tipo 1|5;
- 15 de tipo 2|4;
- 10 de tipo 3|3.

Total: **31**.

La firma completa:
[
mathbf E_rinmathbb R^{31},
qquad
mathbf Einmathbb R^{36	imes31}.
]

La comparación entre tokens se define mediante:
[
D_E(r,s)=|mathbf E_r-mathbf E_s|_2.
]

Esto distingue correctamente una distancia entre **firmas completas** de una diferencia de una sola entropía.

## 6. Resultado 012|345

Para la partición `{0,1,2}|{3,4,5}`, los 36 valores son:

| Símbolo | S bits |
|---|---:|
|0|1.328452100|
|1|1.458061743|
|2|1.261694172|
|3|1.992201086|
|4|1.179121230|
|5|1.506470471|
|6|1.508544384|
|7|0.795416204|
|8|1.925646999|
|9|1.406803292|
|A|1.016165850|
|B|1.723961697|
|C|1.063433961|
|D|1.726694917|
|E|1.786984950|
|F|1.034372940|
|G|1.658338206|
|H|0.580580002|
|I|0.580580002|
|J|1.658338206|
|K|1.034372940|
|L|1.786984950|
|M|1.726694917|
|N|1.063433961|
|O|1.723961697|
|P|1.016165850|
|Q|1.406803292|
|R|1.925646999|
|S|0.795416204|
|T|1.508544384|
|U|1.506470471|
|V|1.179121230|
|W|1.992201086|
|X|1.261694172|
|Y|1.458061743|
|Z|1.328452100|

Rango:
[
0.580580002le Sle1.992201086	ext{ bits}.
]

La simetría `r↔37-r` produce pares iguales como:
`A↔P, B↔O, C↔N, D↔M, E↔L, F↔K, G↔J, H↔I`.

El máximo teórico para una partición 3|3 es 3 bits.

## 7. Pureza y coherencia

La evolución es unitaria:
[
operatorname{Tr}(ho^2)=1.
]

Las 64 amplitudes tienen módulo `1/8`; el anillo CX solo permuta amplitudes.

Por ello:
[
C_{l_1}=sum_{i
e j}|ho_{ij}|=63.
]

Resultado: la coherencia (l_1) es constante para los 36 tokens y no discrimina el alfabeto en esta implementación.

## 8. Mutual information

Para una bipartición (A|B):
[
I(A:B)=S(A)+S(B)-S(AB).
]

Como el estado global es puro:
[
S(AB)=0,qquad S(A)=S(B),
]
de modo que:
[
oxed{I(A:B)=2S(A)}.
]

## 9. QFI

Para los seis parámetros continuos (oldsymbolphi):
[
F_Q^{ij}=4operatorname{Re}
[langlepartial_ipsi|partial_jpsiangle-
langlepartial_ipsi|psiangle
langlepsi|partial_jpsiangle].
]

Como:
[
R_Z(2piphi_i)=e^{-ipiphi_iZ_i},
]
el generador es (pi Z_i). Sobre `|+angle`:
[
langle Z_iangle=0,quad operatorname{Var}(Z_i)=1.
]

Resultado exacto:
[
oxed{F_Q=4pi^2I_6}
]
con:
[
4pi^2=39.478417604357.
]

El anillo CX es independiente de los parámetros y no cambia la métrica QFI de la familia global.

## 10. Espacio de estados

Los estados puros de dimensión 64, salvo fase global, viven en:
[
mathbb{CP}^{63}.
]

El encoder induce:
[
f:T^6	omathbb{CP}^{63}.
]

Esto establece una relación matemática entre coordenadas toroidales y geometría proyectiva del estado. La inyectividad global de esa aplicación queda como propiedad a demostrar, no como supuesto.

## 11. Jerarquía metacomputacional AOTS⁶

[
L_0:	ext{dato/símbolo}
]
[
L_1:	ext{coordenada toroidal}
]
[
L_2:|psi_rangle
]
[
L_3:ho_r
]
[
L_4:	ext{reducciones/entrelazamiento}
]
[
L_5:	ext{fidelidad/relaciones}
]
[
L_6:	ext{geometría}
]
[
L_7:	ext{QFI}
]
[
L_8:	ext{dinámica}
]
[
L_9:	ext{tomografía}
]
[
L_{10}:	ext{comparación modelo-observación}
]
[
L_{11}:	ext{metaestado}.
]

Son niveles de representación y cálculo AOTS⁶, no 11 dimensiones físicas.

Operador metacomputacional:
[
mathfrak M(|psi_rangle)=
{ho_r,mathbf E_r,F_{rs},d_{FS},d_B,I,C_{l_1},F_Q,	ext{dinámica},	ext{observación}}.
]

## 12. Dinámica y tomografía

Extensión dinámica:
[
ho_r(t)=mathcal E_t[ho_r(0)].
]

Estructura:
[
mathbb M_{r,a,b,t}.
]

Una realización experimental requiere:
[
ho_{m ideal}	o	ext{preparación}	o	ext{medición}	ohatho	oDeltaho,
]
incluyendo incertidumbres y error de reconstrucción.

## 13. Estado de evidencia

### Establecido por derivación/cálculo

- 36 símbolos;
- 6 qubits;
- dimensión de Hilbert 64;
- módulo 37;
- seis primos;
- anillo de 6 CX;
- invariancia exacta de fidelidad bajo el anillo común;
- fórmula cerrada de fidelidad;
- 630 pares no ordenados;
- 31 biparticiones no redundantes;
- generación de entrelazamiento después del anillo para las particiones estudiadas;
- pureza global 1;
- coherencia (l_1=63);
- QFI global (4pi^2I_6);
- firma completa 36×31;
- distancia entre firmas.

### Requiere nueva evidencia

- inyectividad global (T^6	omathbb{CP}^{63});
- ruido y canales no unitarios;
- dinámica temporal;
- tomografía física;
- intervalos de confianza;
- ejecución en hardware cuántico;
- comparación sistemática con otros encoders;
- cualquier afirmación de hipercomputación estricta.

## 14. Artefactos incorporados

- `research/AOTS6_QUANTUM_STATE_METACOMPUTATION_RECORD.md`
- `research/aots6_quantum_state_analysis.py`
- `research/AOTS6_METRICS.json`

El script genera las matrices completas de fidelidad, Fubini–Study, distancia toroidal, firmas 36×31, purezas, distancia entre firmas y QFI.

## 15. Fuentes técnicas

- Stanford Encyclopedia of Philosophy, *Quantum Computing*: computabilidad, complejidad y quantum hypercomputation.
- Stanford Encyclopedia of Philosophy, *Computation in Physical Systems*: hipercomputación y restricciones físicas.
- Bourgeois, Blasi & Haack, *Transport Approach to Quantum State Tomography*, PRL 136, 010802 (2026), DOI 10.1103/zk56-jn7t.
- Faist & Renner, *Practical and Reliable Error Bars in Quantum Tomography*, PRL 117, 010404 (2016), DOI 10.1103/PhysRevLett.117.010404.
- Rath et al., *Quantum Fisher Information from Randomized Measurements*, PRL 127, 260501 (2021), DOI 10.1103/PhysRevLett.127.260501.
- *Asymptotic Theory of Quantum Channel Estimation*, PRX Quantum 2, 010343 (2021).
- *Uncertainty Relations between Quantum Fisher Information and Entanglement Monotones*, PRL 136, 110806 (2026), DOI 10.1103/54mc-2yl3.
- Horodecki et al., *Quantum entanglement*, Reviews of Modern Physics 81, 865 (2009).

## 16. Integridad

Este snapshot separa procedimiento, resultados e interpretación. El script constituye el procedimiento reproducible; las métricas constituyen el resumen numérico; el historial Git constituye la procedencia temporal una vez confirmado el commit.
