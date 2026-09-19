#!/usr/bin/env python3
"""AOTS6 quantum-state metacomputation reproducibility script.

Generates the complete 36-token / 6-qubit evidence set:
fidelity, Fubini-Study, toroidal distance, 31 bipartition entropies,
31 reduced-state purities, entanglement-signature distances and QFI.
"""
import itertools,csv,json
from pathlib import Path
import numpy as np

ALPHABET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIMES=(2,3,5,7,11,13)
MOD=37
N=6
OUT=Path(__file__).resolve().parent

H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
I=np.eye(2,dtype=complex)

def kron(xs):
    y=xs[0]
    for x in xs[1:]:
        y=np.kron(y,x)
    return y

def Rz(theta):
    return np.diag([np.exp(-1j*theta/2),np.exp(1j*theta/2)])

def cx(c,t):
    U=np.zeros((64,64),complex)
    for x in range(64):
        b=[(x>>(N-1-i))&1 for i in range(N)]
        y=b.copy()
        if b[c]:
            y[t]^=1
        yi=sum(y[i]<<(N-1-i) for i in range(N))
        U[yi,x]=1
    return U

H6=kron([H]*N)
C=np.eye(64,dtype=complex)
for c,t in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,0)):
    C=cx(c,t)@C

zero=np.eye(64)[:,0]

def state(k,ring=True):
    r=k+1
    phi=np.array([((r*p)%MOD)/MOD for p in PRIMES],float)
    D=kron([Rz(2*np.pi*x) for x in phi])
    U=C if ring else np.eye(64)
    return U@D@H6@zero,phi

def reduced(psi,keep):
    keep=tuple(sorted(keep))
    trace=tuple(i for i in range(N) if i not in keep)
    a=np.transpose(
        psi.reshape([2]*N),
        keep+trace
    ).reshape(2**len(keep),2**len(trace))
    return a@a.conj().T

def entropy(rho):
    e=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    e=np.clip(e,0,1)
    e=e[e>1e-14]
    return float(-np.sum(e*np.log2(e)))

def purity(rho):
    return float(np.real(np.trace(rho@rho)))

def torus_distance(a,b):
    d=np.minimum(np.abs(a-b),1-np.abs(a-b))
    return float(np.linalg.norm(d))

def save_matrix(path,M,labels):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["symbol"]+list(labels))
        for i,row in enumerate(M):
            w.writerow([ALPHABET[i]]+[f"{x:.12f}" for x in row])

# Unique bipartitions: 1|5, 2|4 and one representative of every 3|3 pair.
parts=list(itertools.combinations(range(N),1))
parts+=list(itertools.combinations(range(N),2))
parts+=[p for p in itertools.combinations(range(N),3) if 0 in p]
assert len(parts)==31

states=[]
phis=[]
for k in range(36):
    s,p=state(k,True)
    states.append(s)
    phis.append(p)
states=np.array(states)
phis=np.array(phis)

states_pre=np.array([state(k,False)[0] for k in range(36)])

overlap=states@states.conj().T
overlap_pre=states_pre@states_pre.conj().T

F=np.abs(overlap)**2
Fpre=np.abs(overlap_pre)**2
FS=np.arccos(np.clip(np.abs(overlap),0,1))
TD=np.array([[torus_distance(phis[i],phis[j]) for j in range(36)] for i in range(36)])

E=np.zeros((36,31))
P=np.zeros((36,31))

for r,psi in enumerate(states):
    for j,A in enumerate(parts):
        rho=reduced(psi,A)
        E[r,j]=entropy(rho)
        P[r,j]=purity(rho)

ED=np.linalg.norm(E[:,None,:]-E[None,:,:],axis=2)

# Pure-state QFI with respect to the six continuous phi parameters.
# Rz(2*pi*phi_i)=exp(-i*pi*phi_i*Z_i), Var_{|+>}(Z_i)=1.
Q=4*np.pi**2*np.eye(6)

labels=["".join(str(i+1) for i in p) for p in parts]
save_matrix(OUT/"AOTS6_FIDELITY_MATRIX.csv",F,ALPHABET)
save_matrix(OUT/"AOTS6_FUBINI_STUDY_MATRIX.csv",FS,ALPHABET)
save_matrix(OUT/"AOTS6_TORUS_DISTANCE_MATRIX.csv",TD,ALPHABET)
save_matrix(OUT/"AOTS6_ENTANGLEMENT_SIGNATURES.csv",E,labels)
save_matrix(OUT/"AOTS6_ENTANGLEMENT_PURITIES.csv",P,labels)
save_matrix(OUT/"AOTS6_ENTANGLEMENT_SIGNATURE_DISTANCE.csv",ED,ALPHABET)

with open(OUT/"AOTS6_QFI_MATRIX.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["parameter"]+[f"phi{i+1}" for i in range(6)])
    for i in range(6):
        w.writerow([f"phi{i+1}"]+[f"{Q[i,j]:.12f}" for j in range(6)])

metrics={
    "alphabet_size":36,
    "qubits":6,
    "hilbert_dimension":64,
    "modulus":37,
    "prime_sequence":list(PRIMES),
    "ring_cx_count":6,
    "unordered_pairs":630,
    "unique_bipartitions":31,
    "fidelity_pre_post_max_abs_error":float(np.max(np.abs(F-Fpre))),
    "entropy_min_bits":float(E.min()),
    "entropy_max_bits":float(E.max()),
    "entropy_mean_bits":float(E.mean()),
    "partition_012_min_bits":float(E[:,parts.index((0,1,2))].min()),
    "partition_012_max_bits":float(E[:,parts.index((0,1,2))].max()),
    "global_purity":1.0,
    "l1_coherence":63.0,
    "qfi_diagonal":float(4*np.pi**2),
    "qfi_offdiag":0.0
}
(OUT/"AOTS6_METRICS.json").write_text(
    json.dumps(metrics,indent=2),
    encoding="utf-8"
)
print(json.dumps(metrics,indent=2))
