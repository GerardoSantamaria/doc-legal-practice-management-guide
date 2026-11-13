```mermaid
flowchart LR
  FASE_1["Previa<br/>2 hitos"]
  FASE_2["Medidas provisorias<br/>2 hitos"]
  FASE_3["Consejero de Familia<br/>3 hitos"]
  FASE_4["Postulación<br/>6 hitos"]
  FASE_5["Audiencia preliminar<br/>1 hito"]
  FASE_6["Prueba<br/>8 hitos"]
  FASE_7["Vista de causa<br/>2 hitos"]
  FASE_8["Sentencia<br/>3 hitos"]
  FASE_9["Recursos<br/>6 hitos"]
  FASE_10["Ejecución<br/>1 hito"]
  FASE_11["Incumplimiento y modificación<br/>3 hitos"]
  FASE_12["Situaciones especiales<br/>3 hitos"]
  FASE_13["Acuerdo<br/>4 hitos"]
  FASE_14["Cierre<br/>2 hitos"]
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_14
  FASE_1 --> FASE_12
  FASE_1 --> FASE_11
  FASE_1 --> FASE_13
  FASE_3 --> FASE_4
  FASE_3 --> FASE_13
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_13
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_5 --> FASE_14
  FASE_6 --> FASE_7
  FASE_6 --> FASE_13
  FASE_7 --> FASE_6
  FASE_7 --> FASE_13
  FASE_7 --> FASE_8
  FASE_8 --> FASE_9
  FASE_9 --> FASE_10
  FASE_10 --> FASE_14
  FASE_10 --> FASE_11
  FASE_11 --> FASE_13
  FASE_11 --> FASE_10
  FASE_11 --> FASE_3
  FASE_12 --> FASE_9
  FASE_12 --> FASE_14
  FASE_13 --> FASE_4
  FASE_13 --> FASE_6
  FASE_13 --> FASE_14
  FASE_13 --> FASE_11
```
