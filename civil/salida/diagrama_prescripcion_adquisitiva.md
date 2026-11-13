```mermaid
flowchart LR
  FASE_1["Previa<br/>7 hitos"]
  FASE_2["Postulación<br/>8 hitos"]
  FASE_3["Citaciones<br/>6 hitos"]
  FASE_4["Prueba<br/>9 hitos"]
  FASE_5["Sentencia<br/>4 hitos"]
  FASE_6["Recursos<br/>8 hitos"]
  FASE_7["Inscripción<br/>3 hitos"]
  FASE_8["Acuerdo<br/>1 hito"]
  FASE_9["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_9
  FASE_1 --> FASE_3
  FASE_2 --> FASE_9
  FASE_2 --> FASE_6
  FASE_2 --> FASE_3
  FASE_3 --> FASE_2
  FASE_3 --> FASE_4
  FASE_2 --> FASE_4
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_6
  FASE_6 --> FASE_7
  FASE_6 --> FASE_9
  FASE_7 --> FASE_9
  FASE_8 --> FASE_9
  FASE_8 --> FASE_5
```
