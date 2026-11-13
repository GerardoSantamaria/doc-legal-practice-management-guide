```mermaid
flowchart LR
  FASE_1["Previa<br/>7 hitos"]
  FASE_2["Apertura<br/>9 hitos"]
  FASE_3["Edictos y citación<br/>3 hitos"]
  FASE_4["Declaratoria o aprobación del testamento<br/>6 hitos"]
  FASE_5["Administración<br/>4 hitos"]
  FASE_6["Inventario y avalúo<br/>6 hitos"]
  FASE_7["Partición<br/>5 hitos"]
  FASE_8["Inscripción<br/>7 hitos"]
  FASE_9["Impuestos y tasas<br/>5 hitos"]
  FASE_10["Cierre<br/>2 hitos"]
  FASE_11["Recursos e incidentes<br/>7 hitos"]
  FASE_1 --> FASE_9
  FASE_1 --> FASE_2
  FASE_2 --> FASE_3
  FASE_2 --> FASE_11
  FASE_3 --> FASE_4
  FASE_4 --> FASE_11
  FASE_4 --> FASE_6
  FASE_4 --> FASE_5
  FASE_4 --> FASE_7
  FASE_4 --> FASE_10
  FASE_5 --> FASE_6
  FASE_5 --> FASE_11
  FASE_6 --> FASE_11
  FASE_6 --> FASE_8
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_11
  FASE_7 --> FASE_5
  FASE_8 --> FASE_9
  FASE_8 --> FASE_10
  FASE_11 --> FASE_2
  FASE_11 --> FASE_4
  FASE_11 --> FASE_3
```
