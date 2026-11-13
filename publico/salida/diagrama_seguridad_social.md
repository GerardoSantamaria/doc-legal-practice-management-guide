```mermaid
flowchart LR
  FASE_1["Previa<br/>4 hitos"]
  FASE_2["Vía administrativa<br/>4 hitos"]
  FASE_3["Amparo por mora<br/>3 hitos"]
  FASE_4["Demanda<br/>3 hitos"]
  FASE_5["Cautelares<br/>6 hitos"]
  FASE_6["Prueba<br/>3 hitos"]
  FASE_7["Sentencia<br/>2 hitos"]
  FASE_8["Recursos<br/>5 hitos"]
  FASE_9["Ejecución<br/>6 hitos"]
  FASE_10["Vía administrativa provincial<br/>4 hitos"]
  FASE_11["Cierre<br/>2 hitos"]
  FASE_1 --> FASE_10
  FASE_1 --> FASE_2
  FASE_1 --> FASE_3
  FASE_1 --> FASE_11
  FASE_2 --> FASE_11
  FASE_2 --> FASE_4
  FASE_2 --> FASE_3
  FASE_3 --> FASE_11
  FASE_3 --> FASE_4
  FASE_4 --> FASE_2
  FASE_4 --> FASE_5
  FASE_4 --> FASE_6
  FASE_4 --> FASE_7
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_8 --> FASE_7
  FASE_7 --> FASE_9
  FASE_7 --> FASE_11
  FASE_5 --> FASE_9
  FASE_9 --> FASE_11
  FASE_10 --> FASE_11
```
