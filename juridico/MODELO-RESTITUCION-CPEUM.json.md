# Modelo de Restitución CPEUM — AOTS⁶

## Esquema computable

```
R_CPEUM =
  Derecho
  + FuenteNormativa
  + Acto
  + Autoridad
  + Competencia
  + Fundamentación
  + Motivación
  + Defensa
  + Procedencia
  + Evidencia
  + Decisión
  + Recurso
  + Cumplimiento
  + Restitución
```

## Estados

```
EXISTENCIA
  ↓
AFECTACIÓN
  ↓
LEGALIDAD
  ↓
DEFENSA
  ↓
CONTROL_CONSTITUCIONAL
  ↓
DECISIÓN
  ↓
IMPUGNACIÓN
  ↓
CUMPLIMIENTO
  ↓
RESTITUCIÓN
```

## Objeto JSON conceptual

```json
{
  "id": "",
  "right": {
    "source": "",
    "article": "",
    "text_version_date": ""
  },
  "act": {
    "type": "",
    "date": "",
    "authority": "",
    "content_hash": ""
  },
  "authority": {
    "competence_source": "",
    "competence_verified": false
  },
  "legality": {
    "legal_basis": "",
    "motivation": "",
    "procedure": ""
  },
  "defense": {
    "ordinary_route": "",
    "definitivity_required": null,
    "exception_identified": null,
    "amparo_route": ""
  },
  "evidence": [],
  "decision": {
    "status": "",
    "document_hash": ""
  },
  "appeal": {
    "available": null,
    "filed": null,
    "status": ""
  },
  "restitution": {
    "requested": "",
    "ordered": "",
    "executed": false,
    "execution_evidence": []
  },
  "epistemic_state": ""
}
```

## Invariantes

1. Ningún estado procesal se declara agotado sin constancia.
2. Ninguna obligación de promover amparo se registra sin identificar la norma que produzca ese efecto.
3. La procedencia del amparo se determina conforme a la Constitución y la Ley de Amparo vigente.
4. Una resolución no se sustituye por una inferencia del expediente.
5. La integridad criptográfica no se confunde con verdad material.
6. La restitución solicitada se distingue de la restitución efectivamente ordenada.
7. El archivo público no sustituye la presentación procesal ante autoridad competente.

## Fuentes oficiales de control normativo

- CPEUM vigente: https://www.diputados.gob.mx/LeyesBiblio/ref/cpeum.htm
- Ley de Amparo vigente: https://www.diputados.gob.mx/LeyesBiblio/ref/lamp.htm
- Biblioteca de Legislación Federal: https://www.diputados.gob.mx/LeyesBiblio/

**Versión de referencia normativa:** CPEUM con última reforma publicada el 03-03-2026; Ley de Amparo con última reforma publicada el 16-10-2025.
