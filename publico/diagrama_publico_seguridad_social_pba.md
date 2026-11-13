# Diagrama de Flujo: Seguridad social (ANSES y justicia federal, con variante provincial)

**Régimen:** Ley 24.463 (art. 15 según Ley 24.655) y CPCCN; vía administrativa: Ley 19.549 reformada por la Ley 27.742; variante provincial: Decreto-Ley 9650/80 (IPS) y leyes de las cajas profesionales, que siguen en contencioso administrativo · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_publico_seguridad_social_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el particular que reclama (ACTORA); naranja = el Estado o el organismo demandado, también cuando resuelve en la vía administrativa (DEMANDADA); gris = juzgado, tribunal u organismo de control que no es parte, como la AAIP o el Tribunal Fiscal de Apelación (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la resolución denegatoria de ANSES abre a la vez el control de la caducidad para demandar y la preparación de la demanda.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el caso continúa en otra matriz de Derecho Público, en un expediente vinculado.
* **Provincial o federal:** cuando un flujo tiene las dos variantes, el nombre del hito lo dice ("provincial" o "federal") o nombra la ley que lo rige (por ejemplo, "Ley 13.928" o "Ley 16.986").
* **Vía administrativa:** sus hitos están en un diagrama aparte de los judiciales. La Administración que resuelve aparece en naranja, como parte demandada, y sus plazos son días hábiles administrativos.
* **Calendario administrativo:** la vía ante ANSES usa el calendario administrativo nacional (Ley 19.549) y la del IPS o las cajas, el provincial (Decreto-Ley 7647/70); el checklist de cada hito lo dice.
* **Alzada:** desde el fallo 'Pedraza' (CSJN, 2014) las sentencias de los juzgados federales con asiento en PBA se apelan ante la Cámara Federal de Apelaciones del distrito; las de los juzgados de la Seguridad Social de CABA, ante la Cámara Federal de la Seguridad Social.

## Vista general por fases

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

## 1. Etapa previa: encuadre, documentación y prescripción

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    SSO_010["INICIO - <b>SSO_010</b> Encuadre del reclamo previsional y del organismo<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_020["<b>SSO_020</b> Documentación previsional del cliente<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_030["<b>SSO_030</b> Control de la prescripción de las mensualidades<br/>Responsable: Particular<br/>1 año"]:::actora
    SSO_040["<b>SSO_040</b> Control de un acuerdo de Reparación Histórica (Ley 27.260)<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  P_SSO_010_1(["Se abren en paralelo"]):::paralelo
  SSO_010 -->|"Reajuste del haber inicial o de la movilidad"| P_SSO_010_1
  P_SSO_010_1 --> SSO_020
  P_SSO_010_1 --> SSO_030
  SSO_010 -->|"Denegatoria de un beneficio, reconocimiento de servicios o retenciones"| SSO_020
  SSO_010 -->|"El cliente firmó o recibió un acuerdo de Reparación Histórica"| SSO_040
  EXT_SSO_600_destino["SSO_600 Reclamo ante el IPS o la caja profesional<br/>(ver Variante provincial: IPS y cajas profesionales)"]:::externo
  SSO_010 -->|"Beneficio del IPS o de una caja profesional provincial"| EXT_SSO_600_destino
  EXT_SSO_120_destino["SSO_120 ANSES resuelve tras el pronto despacho<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  SSO_010 -->|"Trámite ya iniciado y sin resolver: pronto despacho"| EXT_SSO_120_destino
  EXT_SSO_130_destino["SSO_130 Amparo por mora contra ANSES<br/>(ver Amparo por mora contra ANSES (art. 28 Ley 19.549))"]:::externo
  SSO_010 -->|"Trámite ya iniciado y sin resolver: amparo por mora"| EXT_SSO_130_destino
  EXT_SSO_100_destino["SSO_100 Reclamo administrativo ante ANSES<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  SSO_020 -->|"Documentación reunida"| EXT_SSO_100_destino
  EXT_SSO_105_destino["SSO_105 Reconocimiento de servicios: prueba en sede administrativa<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  SSO_020 -->|"Documentación reunida: hay servicios que reconocer"| EXT_SSO_105_destino
  FIN_SSO_030_1(["Fin de este camino"]):::fin
  SSO_030 -->|"Reclamo administrativo presentado: se interrumpe la prescripción"| FIN_SSO_030_1
  SSO_040 -->|"Sin acuerdo, o acuerdo que no cubre lo que se reclama"| SSO_020
  EXT_SSO_990_destino["SSO_990 Cierre y archivo del caso<br/>(ver Honorarios y cierre)"]:::externo
  SSO_040 -->|"Acuerdo homologado que cubre el reclamo"| EXT_SSO_990_destino
  style SSO_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional)

```mermaid
flowchart TD
  subgraph F_0["Vía administrativa"]
    SSO_100["<b>SSO_100</b> Reclamo administrativo ante ANSES<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_105["<b>SSO_105</b> Reconocimiento de servicios: prueba en sede administrativa<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_110["<b>SSO_110</b> ANSES resuelve el reclamo<br/>Responsable: Estado u organismo<br/>60 días hábiles administrativos"]:::demandada
    SSO_120["<b>SSO_120</b> ANSES resuelve tras el pronto despacho<br/>Responsable: Estado u organismo<br/>30 días hábiles administrativos"]:::demandada
  end
  EXT_SSO_010_origen["SSO_010 Encuadre del reclamo previsional y del organismo<br/>(ver Etapa previa: encuadre, documentación y prescripción)"]:::externo
  EXT_SSO_010_origen -.->|"Trámite ya iniciado y sin resolver: pronto despacho"| SSO_120
  EXT_SSO_020_origen["SSO_020 Documentación previsional del cliente<br/>(ver Etapa previa: encuadre, documentación y prescripción)"]:::externo
  EXT_SSO_020_origen -.->|"Documentación reunida"| SSO_100
  EXT_SSO_020_origen -.->|"Documentación reunida: hay servicios que reconocer"| SSO_105
  SSO_100 -->|"Reclamo presentado"| SSO_110
  SSO_105 -->|"Prueba de servicios presentada"| SSO_110
  EXT_SSO_990_destino["SSO_990 Cierre y archivo del caso<br/>(ver Honorarios y cierre)"]:::externo
  SSO_110 -->|"Resolución favorable"| EXT_SSO_990_destino
  P_SSO_110_2(["Se abren en paralelo"]):::paralelo
  SSO_110 -->|"Resolución denegatoria o parcial"| P_SSO_110_2
  EXT_SSO_200_destino["SSO_200 Control del plazo de caducidad para demandar a ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  P_SSO_110_2 --> EXT_SSO_200_destino
  EXT_SSO_210_destino["SSO_210 Demanda de conocimiento pleno contra ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  P_SSO_110_2 --> EXT_SSO_210_destino
  SSO_110 -->|"Vence sin resolver: pronto despacho"| SSO_120
  EXT_SSO_130_destino["SSO_130 Amparo por mora contra ANSES<br/>(ver Amparo por mora contra ANSES (art. 28 Ley 19.549))"]:::externo
  SSO_110 -->|"Vence sin resolver: amparo por mora"| EXT_SSO_130_destino
  SSO_120 -->|"Resolución favorable"| EXT_SSO_990_destino
  P_SSO_120_2(["Se abren en paralelo"]):::paralelo
  SSO_120 -->|"Resolución denegatoria o silencio"| P_SSO_120_2
  P_SSO_120_2 --> EXT_SSO_200_destino
  P_SSO_120_2 --> EXT_SSO_210_destino
  EXT_SSO_200_origen["SSO_200 Control del plazo de caducidad para demandar a ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  EXT_SSO_200_origen -.->|"Venció el plazo sin demandar: nuevo reclamo administrativo (ver duda)"| SSO_100
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Amparo por mora contra ANSES (art. 28 Ley 19.549)

```mermaid
flowchart TD
  subgraph F_0["Amparo por mora"]
    SSO_130["<b>SSO_130</b> Amparo por mora contra ANSES<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_140["<b>SSO_140</b> Informe de ANSES sobre la demora<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    SSO_150["<b>SSO_150</b> Orden judicial de resolver y su cumplimiento por ANSES<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
  end
  EXT_SSO_010_origen["SSO_010 Encuadre del reclamo previsional y del organismo<br/>(ver Etapa previa: encuadre, documentación y prescripción)"]:::externo
  EXT_SSO_010_origen -.->|"Trámite ya iniciado y sin resolver: amparo por mora"| SSO_130
  EXT_SSO_110_origen["SSO_110 ANSES resuelve el reclamo<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  EXT_SSO_110_origen -.->|"Vence sin resolver: amparo por mora"| SSO_130
  SSO_130 -->|"Amparo por mora presentado"| SSO_140
  SSO_140 -->|"Informe presentado o vencido el plazo"| SSO_150
  EXT_SSO_990_destino["SSO_990 Cierre y archivo del caso<br/>(ver Honorarios y cierre)"]:::externo
  SSO_150 -->|"ANSES resuelve a favor"| EXT_SSO_990_destino
  P_SSO_150_2(["Se abren en paralelo"]):::paralelo
  SSO_150 -->|"ANSES resuelve en contra, no cumple la orden o se rechaza el amparo por mora"| P_SSO_150_2
  EXT_SSO_200_destino["SSO_200 Control del plazo de caducidad para demandar a ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  P_SSO_150_2 --> EXT_SSO_200_destino
  EXT_SSO_210_destino["SSO_210 Demanda de conocimiento pleno contra ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  P_SSO_150_2 --> EXT_SSO_210_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Demanda de conocimiento pleno y contestación

```mermaid
flowchart TD
  subgraph F_0["Demanda"]
    SSO_200["<b>SSO_200</b> Control del plazo de caducidad para demandar a ANSES<br/>Responsable: Particular<br/>180 días hábiles judiciales"]:::actora
    SSO_210["<b>SSO_210</b> Demanda de conocimiento pleno contra ANSES<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_230["<b>SSO_230</b> Contestación de la demanda por ANSES<br/>Responsable: Estado u organismo<br/>15 días hábiles judiciales"]:::demandada
  end
  EXT_SSO_110_origen["SSO_110 ANSES resuelve el reclamo<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  EXT_SSO_110_origen -.->|"Resolución denegatoria o parcial"| SSO_200
  EXT_SSO_110_origen -.->|"Resolución denegatoria o parcial"| SSO_210
  EXT_SSO_120_origen["SSO_120 ANSES resuelve tras el pronto despacho<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  EXT_SSO_120_origen -.->|"Resolución denegatoria o silencio"| SSO_200
  EXT_SSO_120_origen -.->|"Resolución denegatoria o silencio"| SSO_210
  EXT_SSO_150_origen["SSO_150 Orden judicial de resolver y su cumplimiento por ANSES<br/>(ver Amparo por mora contra ANSES (art. 28 Ley 19.549))"]:::externo
  EXT_SSO_150_origen -.->|"ANSES resuelve en contra, no cumple la orden o se rechaza el amparo por mora"| SSO_200
  EXT_SSO_150_origen -.->|"ANSES resuelve en contra, no cumple la orden o se rechaza el amparo por mora"| SSO_210
  FIN_SSO_200_1(["Fin de este camino"]):::fin
  SSO_200 -->|"Demanda presentada en plazo"| FIN_SSO_200_1
  EXT_SSO_100_destino["SSO_100 Reclamo administrativo ante ANSES<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  SSO_200 -->|"Venció el plazo sin demandar: nuevo reclamo administrativo (ver duda)"| EXT_SSO_100_destino
  SSO_210 -->|"Demanda presentada y traslado notificado"| SSO_230
  EXT_SSO_400_destino["SSO_400 Pedido de medida cautelar<br/>(ver Medidas cautelares contra ANSES)"]:::externo
  SSO_210 -->|"Se pide una medida cautelar"| EXT_SSO_400_destino
  EXT_SSO_240_destino["SSO_240 Prueba: pericia contable y demás medios<br/>(ver Prueba y sentencia)"]:::externo
  SSO_230 -->|"Contestada o vencido el plazo: hay hechos que probar"| EXT_SSO_240_destino
  EXT_SSO_260_destino["SSO_260 Sentencia de primera instancia<br/>(ver Prueba y sentencia)"]:::externo
  SSO_230 -->|"Cuestión de puro derecho"| EXT_SSO_260_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Medidas cautelares contra ANSES

```mermaid
flowchart TD
  subgraph F_0["Cautelares"]
    SSO_400["<b>SSO_400</b> Pedido de medida cautelar<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_415["<b>SSO_415</b> Informe previo del Estado nacional (Ley 26.854)<br/>Responsable: Estado u organismo<br/>5 días hábiles judiciales"]:::demandada
    SSO_420["<b>SSO_420</b> Resolución de la medida cautelar<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    SSO_425["<b>SSO_425</b> Cumplimiento de la medida cautelar por el demandado<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    SSO_445["<b>SSO_445</b> Apelación de la resolución cautelar (federal)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    SSO_450["<b>SSO_450</b> Vencimiento de la cautelar contra el Estado nacional<br/>Responsable: Particular<br/>6 meses"]:::actora
  end
  EXT_SSO_210_origen["SSO_210 Demanda de conocimiento pleno contra ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  EXT_SSO_210_origen -.->|"Se pide una medida cautelar"| SSO_400
  SSO_400 -->|"Se demanda al Estado nacional y no es un supuesto del art. 2 inc. 2 Ley 26.854"| SSO_415
  SSO_400 -->|"Se resuelve sin informe previo"| SSO_420
  SSO_415 -->|"Informe presentado o vencido el plazo"| SSO_420
  P_SSO_420_1(["Se abren en paralelo"]):::paralelo
  SSO_420 -->|"Cautelar otorgada"| P_SSO_420_1
  P_SSO_420_1 --> SSO_425
  P_SSO_420_1 --> SSO_450
  SSO_420 -->|"Se apela la resolución cautelar (juzgado federal)"| SSO_445
  FIN_SSO_420_3(["Fin de este camino"]):::fin
  SSO_420 -->|"Cautelar denegada y no se apela"| FIN_SSO_420_3
  FIN_SSO_425_1(["Fin de este camino"]):::fin
  SSO_425 -->|"Medida cumplida"| FIN_SSO_425_1
  EXT_SSO_550_destino["SSO_550 Cumplimiento forzado contra ANSES: intimación, astreintes o embargo<br/>(ver Ejecución contra ANSES (art. 22 Ley 24.463))"]:::externo
  SSO_425 -->|"Medida incumplida"| EXT_SSO_550_destino
  FIN_SSO_445_1(["Fin de este camino"]):::fin
  SSO_445 -->|"Apelación resuelta"| FIN_SSO_445_1
  FIN_SSO_450_1(["Fin de este camino"]):::fin
  SSO_450 -->|"Prórroga pedida y resuelta, o terminó el proceso"| FIN_SSO_450_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Prueba y sentencia

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    SSO_240["<b>SSO_240</b> Prueba: pericia contable y demás medios<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    SSO_245["<b>SSO_245</b> Observaciones o impugnación de la pericia contable<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    SSO_250["<b>SSO_250</b> Alegatos<br/>Responsable: Cualquiera de las partes<br/>6 días hábiles judiciales"]:::ambas
  end
  subgraph F_1["Sentencia"]
    SSO_260["<b>SSO_260</b> Sentencia de primera instancia<br/>Responsable: Juzgado u organismo de control<br/>40 días hábiles judiciales"]:::tribunal
    SSO_320["<b>SSO_320</b> Sentencia previsional firme<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
  end
  EXT_SSO_230_origen["SSO_230 Contestación de la demanda por ANSES<br/>(ver Demanda de conocimiento pleno y contestación)"]:::externo
  EXT_SSO_230_origen -.->|"Contestada o vencido el plazo: hay hechos que probar"| SSO_240
  EXT_SSO_230_origen -.->|"Cuestión de puro derecho"| SSO_260
  SSO_240 -->|"Pericia contable presentada"| SSO_245
  SSO_240 -->|"Prueba producida sin pericia pendiente"| SSO_250
  SSO_245 -->|"Observaciones presentadas o vencido el plazo"| SSO_250
  SSO_250 -->|"Alegatos presentados o vencido el plazo"| SSO_260
  EXT_SSO_270_destino["SSO_270 Apelación de la sentencia previsional<br/>(ver Recursos)"]:::externo
  SSO_260 -->|"Sentencia notificada y se apela"| EXT_SSO_270_destino
  SSO_260 -->|"Sentencia notificada y no se apela"| SSO_320
  EXT_SSO_270_origen["SSO_270 Apelación de la sentencia previsional<br/>(ver Recursos)"]:::externo
  EXT_SSO_270_origen -.->|"Apelación denegada o desierta"| SSO_320
  EXT_SSO_280_origen["SSO_280 Expresión de agravios<br/>(ver Recursos)"]:::externo
  EXT_SSO_280_origen -.->|"No se expresan agravios: recurso desierto"| SSO_320
  EXT_SSO_290_origen["SSO_290 Sentencia de la Cámara Federal de Apelaciones o de la Seguridad Social<br/>(ver Recursos)"]:::externo
  EXT_SSO_290_origen -.->|"Sentencia de Cámara notificada y no se recurre"| SSO_320
  EXT_SSO_310_origen["SSO_310 Recurso extraordinario federal ante la CSJN<br/>(ver Recursos)"]:::externo
  EXT_SSO_310_origen -.->|"Recurso federal resuelto, denegado (queja incluida) o desistido"| SSO_320
  EXT_SSO_500_destino["SSO_500 Sentencia firme notificada y expediente administrativo remitido a ANSES<br/>(ver Ejecución contra ANSES (art. 22 Ley 24.463))"]:::externo
  SSO_320 -->|"Condena contra ANSES"| EXT_SSO_500_destino
  EXT_SSO_950_destino["SSO_950 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Honorarios y cierre)"]:::externo
  SSO_320 -->|"Rechazo de la demanda"| EXT_SSO_950_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Recursos

```mermaid
flowchart TD
  subgraph F_0["Recursos"]
    SSO_270["<b>SSO_270</b> Apelación de la sentencia previsional<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    SSO_280["<b>SSO_280</b> Expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
    SSO_285["<b>SSO_285</b> Contestación de los agravios<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
    SSO_290["<b>SSO_290</b> Sentencia de la Cámara Federal de Apelaciones o de la Seguridad Social<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    SSO_310["<b>SSO_310</b> Recurso extraordinario federal ante la CSJN<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  EXT_SSO_260_origen["SSO_260 Sentencia de primera instancia<br/>(ver Prueba y sentencia)"]:::externo
  EXT_SSO_260_origen -.->|"Sentencia notificada y se apela"| SSO_270
  SSO_270 -->|"Apelación concedida"| SSO_280
  EXT_SSO_320_destino["SSO_320 Sentencia previsional firme<br/>(ver Prueba y sentencia)"]:::externo
  SSO_270 -->|"Apelación denegada o desierta"| EXT_SSO_320_destino
  SSO_280 -->|"Agravios presentados: traslado"| SSO_285
  SSO_280 -->|"No se expresan agravios: recurso desierto"| EXT_SSO_320_destino
  SSO_285 -->|"Contestados o vencido el plazo"| SSO_290
  SSO_290 -->|"Sentencia de Cámara notificada y se interpone recurso extraordinario"| SSO_310
  SSO_290 -->|"Sentencia de Cámara notificada y no se recurre"| EXT_SSO_320_destino
  SSO_310 -->|"Recurso federal resuelto, denegado (queja incluida) o desistido"| EXT_SSO_320_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Ejecución contra ANSES (art. 22 Ley 24.463)

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    SSO_500["<b>SSO_500</b> Sentencia firme notificada y expediente administrativo remitido a ANSES<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    SSO_510["<b>SSO_510</b> ANSES liquida y cumple la sentencia (120 días hábiles)<br/>Responsable: Estado u organismo<br/>120 días hábiles administrativos"]:::demandada
    SSO_530["<b>SSO_530</b> Liquidación de la sentencia previsional e impugnación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    SSO_540["<b>SSO_540</b> Previsión presupuestaria del crédito (Estado nacional)<br/>Responsable: Estado u organismo<br/>Sin plazo"]:::demandada
    SSO_550["<b>SSO_550</b> Cumplimiento forzado contra ANSES: intimación, astreintes o embargo<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_560["<b>SSO_560</b> ANSES paga el retroactivo y liquida el nuevo haber<br/>Responsable: Estado u organismo<br/>Sin plazo"]:::demandada
  end
  EXT_SSO_320_origen["SSO_320 Sentencia previsional firme<br/>(ver Prueba y sentencia)"]:::externo
  EXT_SSO_320_origen -.->|"Condena contra ANSES"| SSO_500
  EXT_SSO_425_origen["SSO_425 Cumplimiento de la medida cautelar por el demandado<br/>(ver Medidas cautelares contra ANSES)"]:::externo
  EXT_SSO_425_origen -.->|"Medida incumplida"| SSO_550
  SSO_500 -->|"Expediente recibido por ANSES"| SSO_510
  SSO_510 -->|"Cumplida en plazo"| SSO_560
  SSO_510 -->|"Condena dineraria: hay que liquidar"| SSO_530
  SSO_510 -->|"Vencido el plazo sin cumplir"| SSO_550
  SSO_530 -->|"Liquidación aprobada"| SSO_540
  SSO_540 -->|"Crédito previsto y pagado"| SSO_560
  SSO_540 -->|"Sin previsión o sin pago en el ejercicio"| SSO_550
  SSO_550 -->|"Cumplimiento o pago obtenido"| SSO_560
  EXT_SSO_950_destino["SSO_950 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Honorarios y cierre)"]:::externo
  SSO_560 -->|"Pago percibido y obligación cumplida"| EXT_SSO_950_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 9. Variante provincial: IPS y cajas profesionales

```mermaid
flowchart TD
  subgraph F_0["Vía administrativa provincial"]
    SSO_600["<b>SSO_600</b> Reclamo ante el IPS o la caja profesional<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    SSO_605["<b>SSO_605</b> El IPS o la caja resuelve el reclamo<br/>Responsable: Estado u organismo<br/>30 días hábiles administrativos"]:::demandada
    SSO_610["<b>SSO_610</b> Recurso de revocatoria ante el IPS o la caja<br/>Responsable: Particular<br/>10 días hábiles administrativos"]:::actora
    SSO_620["<b>SSO_620</b> Sigue en la matriz de contencioso administrativo<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  EXT_SSO_010_origen["SSO_010 Encuadre del reclamo previsional y del organismo<br/>(ver Etapa previa: encuadre, documentación y prescripción)"]:::externo
  EXT_SSO_010_origen -.->|"Beneficio del IPS o de una caja profesional provincial"| SSO_600
  SSO_600 -->|"Reclamo presentado"| SSO_605
  EXT_SSO_990_destino["SSO_990 Cierre y archivo del caso<br/>(ver Honorarios y cierre)"]:::externo
  SSO_605 -->|"Resolución favorable"| EXT_SSO_990_destino
  SSO_605 -->|"Resolución denegatoria"| SSO_610
  SSO_605 -->|"Vence sin resolver"| SSO_620
  SSO_610 -->|"Revocatoria rechazada o vencido el plazo para resolver"| SSO_620
  SSO_610 -->|"Revocatoria acogida"| EXT_SSO_990_destino
  style SSO_620 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 10. Honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    SSO_950["<b>SSO_950</b> Regulación de honorarios y apelación (federal, Ley 27.423)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    SSO_990["<b>SSO_990</b> Cierre y archivo del caso<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_SSO_040_origen["SSO_040 Control de un acuerdo de Reparación Histórica (Ley 27.260)<br/>(ver Etapa previa: encuadre, documentación y prescripción)"]:::externo
  EXT_SSO_040_origen -.->|"Acuerdo homologado que cubre el reclamo"| SSO_990
  EXT_SSO_110_origen["SSO_110 ANSES resuelve el reclamo<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  EXT_SSO_110_origen -.->|"Resolución favorable"| SSO_990
  EXT_SSO_120_origen["SSO_120 ANSES resuelve tras el pronto despacho<br/>(ver Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional))"]:::externo
  EXT_SSO_120_origen -.->|"Resolución favorable"| SSO_990
  EXT_SSO_150_origen["SSO_150 Orden judicial de resolver y su cumplimiento por ANSES<br/>(ver Amparo por mora contra ANSES (art. 28 Ley 19.549))"]:::externo
  EXT_SSO_150_origen -.->|"ANSES resuelve a favor"| SSO_990
  EXT_SSO_320_origen["SSO_320 Sentencia previsional firme<br/>(ver Prueba y sentencia)"]:::externo
  EXT_SSO_320_origen -.->|"Rechazo de la demanda"| SSO_950
  EXT_SSO_560_origen["SSO_560 ANSES paga el retroactivo y liquida el nuevo haber<br/>(ver Ejecución contra ANSES (art. 22 Ley 24.463))"]:::externo
  EXT_SSO_560_origen -.->|"Pago percibido y obligación cumplida"| SSO_950
  EXT_SSO_605_origen["SSO_605 El IPS o la caja resuelve el reclamo<br/>(ver Variante provincial: IPS y cajas profesionales)"]:::externo
  EXT_SSO_605_origen -.->|"Resolución favorable"| SSO_990
  EXT_SSO_610_origen["SSO_610 Recurso de revocatoria ante el IPS o la caja<br/>(ver Variante provincial: IPS y cajas profesionales)"]:::externo
  EXT_SSO_610_origen -.->|"Revocatoria acogida"| SSO_990
  SSO_950 -->|"Regulación firme y aportes acreditados"| SSO_990
  style SSO_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
