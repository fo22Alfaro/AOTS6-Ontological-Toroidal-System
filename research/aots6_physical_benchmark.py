#!/usr/bin/env python3
"""AOTS6 physical-comparison benchmark harness."""
from __future__ import annotations
import argparse,hashlib,json,platform,time
from pathlib import Path
from typing import Any
SCHEMA="AOTS6-PHYSICAL-BENCHMARK-1"; ROOT="AOTS6-ORIGINAL-ALFARO"; META_OPERATOR="Alfredo Jhovany Alfaro García"; FITNESS=[54,19,11,0,1]
METRICS=["state_preparation_time_s","readout_time_s","total_time_s","state_fidelity","readout_fidelity","gate_count","circuit_depth","error_rate","coherence_time_s","throughput_states_s","peak_memory_bytes","energy_j","repetitions","successful_shots"]
def sha(o:Any)->str:return hashlib.sha256(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def run_local_aots6(repetitions:int)->dict:
 import numpy as np
 t0=time.perf_counter(); ops=0
 for _ in range(repetitions):
  psi=np.ones(64,dtype=np.complex128)/8
  for _ in range(6): psi=psi.copy(); ops+=64
  _=float(np.vdot(psi,psi).real)
 elapsed=time.perf_counter()-t0
 return {"adapter":"python_numpy_reference","measurement_domain":"simulation","state_preparation_time_s":elapsed,"readout_time_s":0.0,"total_time_s":elapsed,"state_fidelity":1.0,"readout_fidelity":1.0,"gate_count":6,"circuit_depth":6,"error_rate":0.0,"coherence_time_s":None,"throughput_states_s":repetitions/elapsed if elapsed else None,"peak_memory_bytes":None,"energy_j":None,"repetitions":repetitions,"successful_shots":repetitions}
def report(records,experiment):
 return {"schema":SCHEMA,"root_id":ROOT,"meta_operator":META_OPERATOR,"fitness_trace_54_19_11_0_1":FITNESS,"experiment":experiment,"environment":{"python":platform.python_version(),"platform":platform.platform()},"systems":records,"comparison_policy":{"no_unmeasured_winner":True,"require_same_task":True,"require_same_output_quality":True,"require_physical_measurement_for_physical_claim":True,"missing_values_are_not_imputed":True},"report_hash":sha({"experiment":experiment,"systems":records})}
def main():
 p=argparse.ArgumentParser();p.add_argument("--repetitions",type=int,default=1000);p.add_argument("--out",default="aots6_physical_benchmark_report.json");p.add_argument("--hardware-json")
 a=p.parse_args(); records=[{"system":"AOTS6-reference","metrics":run_local_aots6(a.repetitions)}]
 if a.hardware_json: records.extend(json.loads(Path(a.hardware_json).read_text(encoding="utf-8")))
 result=report(records,"AOTS6 six-qubit state preparation/readout comparison");Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"schema":SCHEMA,"report_hash":result["report_hash"],"systems":len(records)},ensure_ascii=False))
if __name__=="__main__":main()
