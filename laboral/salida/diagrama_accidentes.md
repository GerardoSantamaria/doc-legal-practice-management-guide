```mermaid
flowchart LR
  FASE_1["Previa<br/>6 hitos"]
  FASE_2["Comisión médica<br/>8 hitos"]
  FASE_3["Postulación<br/>8 hitos"]
  FASE_4["Prueba<br/>6 hitos"]
  FASE_5["Vista de causa<br/>2 hitos"]
  FASE_6["Sentencia<br/>3 hitos"]
  FASE_7["Recursos<br/>4 hitos"]
  FASE_8["Ejecución<br/>4 hitos"]
  FASE_9["Acuerdo<br/>2 hitos"]
  FASE_10["Cierre<br/>2 hitos"]
  FASE_1 --> FASE_9
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_10
  FASE_2 --> FASE_10
  FASE_2 --> FASE_3
  FASE_3 --> FASE_10
  FASE_3 --> FASE_4
  FASE_3 --> FASE_7
  FASE_4 --> FASE_5
  FASE_4 --> FASE_6
  FASE_5 --> FASE_6
  FASE_5 --> FASE_9
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_10
  FASE_7 --> FASE_6
  FASE_8 --> FASE_10
  FASE_9 --> FASE_10
  FASE_9 --> FASE_8
```
