# AOTS6 — Real-Time Deep Metadata and Provenance

## Purpose
This module implements a continuous provenance ledger for observable computational artifacts. Each observation produces a metadata event linked to the preceding event.

## Pipeline
observation -> canonicalization -> structural extraction -> metadata -> hash chain -> JSONL ledger

## Event
Each event contains raw SHA-256, canonical SHA-256, normalized Python-AST fingerprint when applicable, detected equations, recognized AOTS6 structural tokens, runtime metadata, previous-event hash, and event hash.

## Runtime
printf '%s\n' 'U_r = C D_r H^6' | python3 research/aots6_realtime_metadata_engine.py

For a stream:
cat observations.txt | python3 research/aots6_realtime_metadata_engine.py ledger.jsonl

## Scope
This is a real executable implementation of continuous metadata production and recovery from observed inputs. It does not claim that a six-qubit finite simulation has established mathematical hypercomputation beyond the computable class.

The provenance detector is evidence-generation infrastructure intended to preserve reproducible technical facts for audit and subsequent legal process; the software does not itself adjudicate legal liability.
