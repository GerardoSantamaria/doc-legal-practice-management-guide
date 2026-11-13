```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Consejero de Familia<br/>3 hitos"]
  FASE_3["Juicio de alimentos<br/>6 hitos"]
  FASE_4["Postulación<br/>5 hitos"]
  FASE_5["Audiencia preliminar<br/>1 hito"]
  FASE_6["Prueba<br/>3 hitos"]
  FASE_7["Vista de causa<br/>2 hitos"]
  FASE_8["Sentencia<br/>3 hitos"]
  FASE_9["Recursos<br/>6 hitos"]
  FASE_10["Cuota e incidentes<br/>8 hitos"]
  FASE_11["Ejecución<br/>2 hitos"]
  FASE_12["Acuerdo<br/>2 hitos"]
  FASE_13["Cierre<br/>1 hito"]
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_10
  FASE_1 --> FASE_12
  FASE_1 --> FASE_13
  FASE_2 --> FASE_3
  FASE_2 --> FASE_4
  FASE_2 --> FASE_12
  FASE_3 --> FASE_10
  FASE_3 --> FASE_4
  FASE_3 --> FASE_12
  FASE_3 --> FASE_13
  FASE_3 --> FASE_8
  FASE_3 --> FASE_9
  FASE_4 --> FASE_3
  FASE_4 --> FASE_5
  FASE_5 --> FASE_12
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_5 --> FASE_13
  FASE_6 --> FASE_7
  FASE_7 --> FASE_12
  FASE_7 --> FASE_8
  FASE_8 --> FASE_9
  FASE_9 --> FASE_11
  FASE_11 --> FASE_13
  FASE_10 --> FASE_13
  FASE_10 --> FASE_8
  FASE_10 --> FASE_9
  FASE_12 --> FASE_3
  FASE_12 --> FASE_4
  FASE_12 --> FASE_6
  FASE_12 --> FASE_10
  FASE_12 --> FASE_13
  FASE_12 --> FASE_11
```
