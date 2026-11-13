```mermaid
flowchart LR
  FASE_1["Previa<br/>17 hitos"]
  FASE_2["Postulación<br/>9 hitos"]
  FASE_3["Prueba<br/>9 hitos"]
  FASE_4["Sentencia<br/>5 hitos"]
  FASE_5["Recursos<br/>8 hitos"]
  FASE_6["Ejecución<br/>6 hitos"]
  FASE_7["Acuerdo<br/>2 hitos"]
  FASE_8["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_8
  FASE_1 --> FASE_7
  FASE_1 --> FASE_2
  FASE_2 --> FASE_8
  FASE_2 --> FASE_5
  FASE_2 --> FASE_3
  FASE_3 --> FASE_4
  FASE_3 --> FASE_7
  FASE_4 --> FASE_5
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_6 --> FASE_8
  FASE_7 --> FASE_4
  FASE_7 --> FASE_8
  FASE_7 --> FASE_6
```
