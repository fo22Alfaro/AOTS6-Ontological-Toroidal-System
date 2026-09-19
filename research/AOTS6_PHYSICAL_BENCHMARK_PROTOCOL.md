# AOTS6 — Physical Benchmark Protocol

## Objective

Convert the existing AOTS6 runtime into a falsifiable physical comparison framework. A physical superiority claim is emitted only where real measured data supports it.

## Required protocol

Every system executes the same logical workload with matched output quality and declared repetitions. Record preparation, readout, total latency, fidelity, gate count/depth, error rate, coherence, throughput, memory and energy where measurable.

## Hardware adapters

External hardware records enter through an adapter using the benchmark schema. Preserve provider job identifiers, timestamps, circuit description, shots and returned counts.

## Statistical treatment

Repeated measurements report sample count and uncertainty. Missing physical measurements remain null and are never inferred from simulation.

## Decision rule

A system may be described as outperforming another only on metrics actually measured under the same task and quality constraints. A universal claim requires an explicitly defined comparison set.

## Provenance

Every report carries AOTS6-ORIGINAL-ALFARO, Alfredo Jhovany Alfaro García, the fitness trace 54/19/11/0/1, experiment definition, system records and report hash.
