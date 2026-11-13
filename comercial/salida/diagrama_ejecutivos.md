```mermaid
flowchart LR
  FASE_1["Previa<br/>6 hitos"]
  FASE_2["Preparación<br/>4 hitos"]
  FASE_3["Intimación y excepciones<br/>5 hitos"]
  FASE_4["Postulación<br/>2 hitos"]
  FASE_5["Prueba<br/>3 hitos"]
  FASE_6["Sentencia<br/>2 hitos"]
  FASE_7["Recursos<br/>7 hitos"]
  FASE_8["Ejecución<br/>12 hitos"]
  FASE_9["Acuerdo<br/>1 hito"]
  FASE_10["Cierre<br/>5 hitos"]
  FASE_1 --> FASE_10
  FASE_1 --> FASE_2
  FASE_1 --> FASE_4
  FASE_1 --> FASE_9
  FASE_2 --> FASE_3
  FASE_2 --> FASE_10
  FASE_2 --> FASE_4
  FASE_3 --> FASE_8
  FASE_3 --> FASE_10
  FASE_3 --> FASE_7
  FASE_3 --> FASE_6
  FASE_7 --> FASE_8
  FASE_7 --> FASE_6
  FASE_4 --> FASE_10
  FASE_4 --> FASE_5
  FASE_4 --> FASE_6
  FASE_4 --> FASE_9
  FASE_5 --> FASE_9
  FASE_5 --> FASE_6
  FASE_6 --> FASE_7
  FASE_6 --> FASE_10
  FASE_6 --> FASE_8
  FASE_8 --> FASE_10
  FASE_9 --> FASE_10
  FASE_9 --> FASE_8
```
