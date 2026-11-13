```mermaid
flowchart LR
  FASE_1["Oportunidad<br/>2 hitos"]
  FASE_2["Acuerdo<br/>5 hitos"]
  FASE_3["Audiencia<br/>1 hito"]
  FASE_4["Resolución<br/>1 hito"]
  FASE_5["Sentencia<br/>1 hito"]
  FASE_6["Flagrancia y probation<br/>2 hitos"]
  FASE_7["Recursos<br/>5 hitos"]
  FASE_8["Cierre<br/>6 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_6
  FASE_1 --> FASE_8
  FASE_2 --> FASE_8
  FASE_2 --> FASE_3
  FASE_3 --> FASE_4
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_7
  FASE_5 --> FASE_8
  FASE_6 --> FASE_2
  FASE_6 --> FASE_8
  FASE_6 --> FASE_1
  FASE_7 --> FASE_8
```
