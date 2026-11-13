# Diagrama de Flujo: Investigación Penal Preparatoria (PBA)

**Régimen:** CPP PBA (Ley 11.922 y modificatorias); Ley 14.442 del Ministerio Público (a verificar); procedimiento de flagrancia (arts. 284 bis a 284 sexies; Ley 13.811); mediación penal (Ley 13.433, a verificar); Código Penal · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_penal_investigacion_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima constituida en parte (ACTORA); naranja = imputado y defensa (DEMANDADA); gris = Juzgado de Garantías, Cámara, policía, peritos u otros órganos, aclarado en el nombre del hito (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, con imputado detenido, la excarcelación y el pedido de prisión preventiva corren en paralelo con la producción de prueba y el control del plazo de la IPP.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo penal, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la intervención judicial formal (consulta, denuncia, designación de defensor, constitución como particular damnificado). La app los separa en el flujo prejudicial; en penal hay duda sobre si eso tiene sentido desde la denuncia.
* **Plazos corridos (art. 139 CPP PBA):** la mayoría de los plazos procesales penales son días continuos (CORRIDOS), no hábiles judiciales. Aplica_Gracia = NO en todos los hitos.
* **Flagrancia (arts. 284 bis a 284 sexies):** el fiscal declara el caso como de flagrancia en 48 horas; investigación en 20 días prorrogables otros 20; requisitoria en 5 días. La feria no suspende los plazos del art. 139 en flagrancia.
* **Pedidos de prueba:** cada medida se abre en paralelo y el hito de pedidos de prueba vuelve a abrirse, porque la investigación sigue mientras se produce la medida.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Investigación<br/>3 hitos"]
  FASE_3["Libertad<br/>10 hitos"]
  FASE_4["Prueba<br/>6 hitos"]
  FASE_5["Plazo IPP<br/>3 hitos"]
  FASE_6["Salidas alternativas<br/>7 hitos"]
  FASE_7["Etapa intermedia<br/>10 hitos"]
  FASE_8["Flagrancia<br/>4 hitos"]
  FASE_9["Cierre<br/>5 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_6
  FASE_2 --> FASE_3
  FASE_2 --> FASE_4
  FASE_2 --> FASE_5
  FASE_2 --> FASE_8
  FASE_3 --> FASE_9
  FASE_4 --> FASE_2
  FASE_4 --> FASE_3
  FASE_4 --> FASE_5
  FASE_4 --> FASE_6
  FASE_4 --> FASE_7
  FASE_6 --> FASE_9
  FASE_6 --> FASE_4
  FASE_6 --> FASE_8
  FASE_7 --> FASE_4
  FASE_7 --> FASE_9
  FASE_8 --> FASE_4
  FASE_8 --> FASE_5
  FASE_8 --> FASE_9
  FASE_8 --> FASE_6
  FASE_8 --> FASE_7
  FASE_8 --> FASE_3
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    IPP_010["INICIO - <b>IPP_010</b> Consulta del caso penal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_020["<b>IPP_020</b> Denuncia (policía, fiscalía o juez)<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_030["<b>IPP_030</b> Designación de defensor<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    IPP_040["<b>IPP_040</b> Constitución como particular damnificado<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_050["<b>IPP_050</b> Control de prescripción de la acción<br/>Responsable: Cualquiera de las partes<br/>6 años"]:::ambas
  end
  P_IPP_010_1(["Se abren en paralelo"]):::paralelo
  IPP_010 -->|"Se representa a la defensa"| P_IPP_010_1
  P_IPP_010_1 --> IPP_030
  P_IPP_010_1 --> IPP_050
  P_IPP_010_2(["Se abren en paralelo"]):::paralelo
  IPP_010 -->|"Se representa o asesora a la víctima"| P_IPP_010_2
  P_IPP_010_2 --> IPP_020
  P_IPP_010_2 --> IPP_040
  P_IPP_010_2 --> IPP_050
  P_IPP_010_3(["Se abren en paralelo"]):::paralelo
  IPP_010 -->|"La IPP ya se inició de oficio (fiscal o policía)"| P_IPP_010_3
  EXT_IPP_110_destino["IPP_110 Actuación de oficio del fiscal o de la policía<br/>(ver Apertura de la IPP)"]:::externo
  P_IPP_010_3 --> EXT_IPP_110_destino
  P_IPP_010_3 --> IPP_050
  EXT_IPP_100_destino["IPP_100 Apertura o radicación de la IPP ante el Fiscal<br/>(ver Apertura de la IPP)"]:::externo
  IPP_020 -->|"Denuncia radicada"| EXT_IPP_100_destino
  IPP_030 -->|"Defensor designado"| EXT_IPP_100_destino
  FIN_IPP_040_1(["Fin de este camino"]):::fin
  IPP_040 -->|"Constitución admitida, rechazada o diferida"| FIN_IPP_040_1
  FIN_IPP_050_1(["Fin de este camino"]):::fin
  IPP_050 -->|"La acción sigue vigente al concluir la IPP"| FIN_IPP_050_1
  EXT_IPP_550_destino["IPP_550 Extinción por prescripción<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_050 -->|"La acción está prescrita"| EXT_IPP_550_destino
  style IPP_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Apertura de la IPP

```mermaid
flowchart TD
  subgraph F_0["Investigación"]
    IPP_100["<b>IPP_100</b> Apertura o radicación de la IPP ante el Fiscal<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_110["<b>IPP_110</b> Actuación de oficio del fiscal o de la policía<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_120["<b>IPP_120</b> Citación y declaración del imputado no detenido<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
  end
  EXT_IPP_010_origen["IPP_010 Consulta del caso penal<br/>(ver Etapa previa)"]:::externo
  EXT_IPP_010_origen -.->|"La IPP ya se inició de oficio (fiscal o policía)"| IPP_110
  EXT_IPP_020_origen["IPP_020 Denuncia (policía, fiscalía o juez)<br/>(ver Etapa previa)"]:::externo
  EXT_IPP_020_origen -.->|"Denuncia radicada"| IPP_100
  EXT_IPP_030_origen["IPP_030 Designación de defensor<br/>(ver Etapa previa)"]:::externo
  EXT_IPP_030_origen -.->|"Defensor designado"| IPP_100
  P_IPP_100_1(["Se abren en paralelo"]):::paralelo
  IPP_100 -->|"Imputado aprehendido o detenido (trámite ordinario)"| P_IPP_100_1
  EXT_IPP_200_destino["IPP_200 Aprehensión o detención del imputado<br/>(ver Situación de libertad del imputado)"]:::externo
  P_IPP_100_1 --> EXT_IPP_200_destino
  EXT_IPP_300_destino["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  P_IPP_100_1 --> EXT_IPP_300_destino
  EXT_IPP_400_destino["IPP_400 Plazo legal de la IPP (4 meses)<br/>(ver Plazo de la investigación)"]:::externo
  P_IPP_100_1 --> EXT_IPP_400_destino
  P_IPP_100_2(["Se abren en paralelo"]):::paralelo
  IPP_100 -->|"Aprehensión en flagrancia (art. 284 bis)"| P_IPP_100_2
  P_IPP_100_2 --> EXT_IPP_200_destino
  EXT_IPP_700_destino["IPP_700 Declaración del caso como de flagrancia (48 horas)<br/>(ver Procedimiento de flagrancia)"]:::externo
  P_IPP_100_2 --> EXT_IPP_700_destino
  P_IPP_100_3(["Se abren en paralelo"]):::paralelo
  IPP_100 -->|"Imputado individualizado y no detenido: citación a declarar"| P_IPP_100_3
  P_IPP_100_3 --> IPP_120
  P_IPP_100_3 --> EXT_IPP_300_destino
  IPP_100 -->|"Sin imputado individualizado: se investiga"| EXT_IPP_300_destino
  IPP_110 -->|"IPP impulsada de oficio"| IPP_100
  IPP_120 -->|"Declaración recibida o negativa a declarar: corre el plazo de la IPP"| EXT_IPP_400_destino
  P_IPP_120_2(["Se abren en paralelo"]):::paralelo
  IPP_120 -->|"Se ordena la detención"| P_IPP_120_2
  P_IPP_120_2 --> EXT_IPP_200_destino
  P_IPP_120_2 --> EXT_IPP_400_destino
  EXT_IPP_300_origen["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  EXT_IPP_300_origen -.->|"Se individualiza y cita al imputado"| IPP_120
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Situación de libertad del imputado

```mermaid
flowchart TD
  subgraph F_0["Libertad"]
    IPP_200["<b>IPP_200</b> Aprehensión o detención del imputado<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
    IPP_210["<b>IPP_210</b> Comunicación al Juez de Garantías y puesta a disposición<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
    IPP_220["<b>IPP_220</b> Declaración del imputado (con detenido: 24 horas)<br/>Responsable: Fiscal / particular damnificado<br/>24 horas"]:::actora
    IPP_230["<b>IPP_230</b> Pedido de excarcelación o eximición de prisión<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    IPP_240["<b>IPP_240</b> Resolución del pedido de excarcelación<br/>Responsable: Juez de Garantías u órgano<br/>5 días corridos"]:::tribunal
    IPP_250["<b>IPP_250</b> Pedido de prisión preventiva por el Fiscal<br/>Responsable: Fiscal / particular damnificado<br/>15 días corridos"]:::actora
    IPP_260["<b>IPP_260</b> Auto de prisión preventiva<br/>Responsable: Juez de Garantías u órgano<br/>5 días corridos"]:::tribunal
    IPP_270["<b>IPP_270</b> Apelación de la coerción o de la denegatoria de excarcelación<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    IPP_280["<b>IPP_280</b> Alternativas a la prisión preventiva y morigeración<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    IPP_290["<b>IPP_290</b> Control del plazo máximo con detenido (2 años)<br/>Responsable: Imputado / defensa<br/>2 años"]:::demandada
  end
  EXT_IPP_100_origen["IPP_100 Apertura o radicación de la IPP ante el Fiscal<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_100_origen -.->|"Imputado aprehendido o detenido (trámite ordinario)"| IPP_200
  EXT_IPP_100_origen -.->|"Aprehensión en flagrancia (art. 284 bis)"| IPP_200
  EXT_IPP_120_origen["IPP_120 Citación y declaración del imputado no detenido<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_120_origen -.->|"Se ordena la detención"| IPP_200
  P_IPP_200_1(["Se abren en paralelo"]):::paralelo
  IPP_200 -->|"Detenido a disposición"| P_IPP_200_1
  P_IPP_200_1 --> IPP_210
  P_IPP_200_1 --> IPP_220
  P_IPP_200_1 --> IPP_230
  P_IPP_200_1 --> IPP_250
  FIN_IPP_210_1(["Fin de este camino"]):::fin
  IPP_210 -->|"Puesta a disposición cumplida"| FIN_IPP_210_1
  EXT_IPP_960_destino["IPP_960 Sigue en la matriz de hábeas corpus<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_210 -->|"Sin puesta a disposición: hábeas corpus"| EXT_IPP_960_destino
  FIN_IPP_220_1(["Fin de este camino"]):::fin
  IPP_220 -->|"Declaración recibida o negativa a declarar"| FIN_IPP_220_1
  IPP_220 -->|"Vencido el plazo sin declaración: pedir la libertad o hábeas corpus"| EXT_IPP_960_destino
  IPP_230 -->|"Pedido presentado"| IPP_240
  FIN_IPP_240_1(["Fin de este camino"]):::fin
  IPP_240 -->|"Excarcelación concedida"| FIN_IPP_240_1
  IPP_240 -->|"Excarcelación denegada: apelación"| IPP_270
  IPP_240 -->|"Excarcelación denegada: alternativas o morigeración"| IPP_280
  IPP_240 -->|"Excarcelación denegada: hábeas corpus"| EXT_IPP_960_destino
  IPP_250 -->|"El fiscal pide la prisión preventiva"| IPP_260
  FIN_IPP_250_2(["Fin de este camino"]):::fin
  IPP_250 -->|"No se pide: libertad (art. 161) o el pedido va con la requisitoria en flagrancia"| FIN_IPP_250_2
  P_IPP_260_1(["Se abren en paralelo"]):::paralelo
  IPP_260 -->|"PP dictada"| P_IPP_260_1
  P_IPP_260_1 --> IPP_270
  P_IPP_260_1 --> IPP_280
  P_IPP_260_1 --> IPP_290
  IPP_260 -->|"PP dictada: hábeas corpus ante la Cámara (art. 405)"| EXT_IPP_960_destino
  FIN_IPP_260_3(["Fin de este camino"]):::fin
  IPP_260 -->|"PP rechazada: libertad"| FIN_IPP_260_3
  FIN_IPP_270_1(["Fin de este camino"]):::fin
  IPP_270 -->|"Apelación resuelta por la Cámara, desistida o no interpuesta"| FIN_IPP_270_1
  IPP_270 -->|"Se opta por el hábeas corpus (art. 164)"| EXT_IPP_960_destino
  FIN_IPP_280_1(["Fin de este camino"]):::fin
  IPP_280 -->|"Alternativa o morigeración resuelta"| FIN_IPP_280_1
  FIN_IPP_290_1(["Fin de este camino"]):::fin
  IPP_290 -->|"El proceso terminó o la detención cesó antes del vencimiento"| FIN_IPP_290_1
  IPP_290 -->|"Vence el plazo: pedir libertad, cese o morigeración"| IPP_280
  IPP_290 -->|"Vence el plazo: hábeas corpus"| EXT_IPP_960_destino
  EXT_IPP_300_origen["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  EXT_IPP_300_origen -.->|"Se detiene al imputado, que todavía no había declarado"| IPP_200
  EXT_IPP_300_origen -.->|"Se detiene al imputado que ya declaró (el plazo de la IPP ya corre)"| IPP_200
  EXT_IPP_730_origen["IPP_730 Requisitoria en flagrancia (5 días)<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_730_origen -.->|"Requisitoria de elevación con detenido: pedido de prisión preventiva"| IPP_250
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Prueba

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    IPP_300["<b>IPP_300</b> Pedidos de prueba de las partes e investigación del fiscal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_310["<b>IPP_310</b> Registro, allanamiento, requisa o secuestro<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
    IPP_320["<b>IPP_320</b> Pericias y actos definitivos e irreproductibles<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
    IPP_330["<b>IPP_330</b> Testimoniales, reconocimientos e informes<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_340["<b>IPP_340</b> Intervención de comunicaciones y otras medidas restrictivas<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
    IPP_800["<b>IPP_800</b> Recurso de reposición<br/>Responsable: Cualquiera de las partes<br/>3 días corridos"]:::ambas
  end
  EXT_IPP_100_origen["IPP_100 Apertura o radicación de la IPP ante el Fiscal<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_100_origen -.->|"Imputado aprehendido o detenido (trámite ordinario)"| IPP_300
  EXT_IPP_100_origen -.->|"Imputado individualizado y no detenido: citación a declarar"| IPP_300
  EXT_IPP_100_origen -.->|"Sin imputado individualizado: se investiga"| IPP_300
  P_IPP_300_1(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se pide un registro, allanamiento, requisa o secuestro"| P_IPP_300_1
  P_IPP_300_1 --> IPP_310
  P_IPP_300_1 --> IPP_300
  P_IPP_300_2(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se ordena una pericia o un acto irreproductible"| P_IPP_300_2
  P_IPP_300_2 --> IPP_320
  P_IPP_300_2 --> IPP_300
  P_IPP_300_3(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se citan testigos o se piden informes"| P_IPP_300_3
  P_IPP_300_3 --> IPP_330
  P_IPP_300_3 --> IPP_300
  P_IPP_300_4(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se pide una intervención de comunicaciones u otra medida restrictiva"| P_IPP_300_4
  P_IPP_300_4 --> IPP_340
  P_IPP_300_4 --> IPP_300
  P_IPP_300_5(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se individualiza y cita al imputado"| P_IPP_300_5
  EXT_IPP_120_destino["IPP_120 Citación y declaración del imputado no detenido<br/>(ver Apertura de la IPP)"]:::externo
  P_IPP_300_5 --> EXT_IPP_120_destino
  P_IPP_300_5 --> IPP_300
  P_IPP_300_6(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se detiene al imputado, que todavía no había declarado"| P_IPP_300_6
  EXT_IPP_200_destino["IPP_200 Aprehensión o detención del imputado<br/>(ver Situación de libertad del imputado)"]:::externo
  P_IPP_300_6 --> EXT_IPP_200_destino
  P_IPP_300_6 --> IPP_300
  EXT_IPP_400_destino["IPP_400 Plazo legal de la IPP (4 meses)<br/>(ver Plazo de la investigación)"]:::externo
  P_IPP_300_6 --> EXT_IPP_400_destino
  P_IPP_300_7(["Se abren en paralelo"]):::paralelo
  IPP_300 -->|"Se detiene al imputado que ya declaró (el plazo de la IPP ya corre)"| P_IPP_300_7
  P_IPP_300_7 --> EXT_IPP_200_destino
  P_IPP_300_7 --> IPP_300
  EXT_IPP_500_destino["IPP_500 Archivo o desestimación y su revisión ante el Fiscal General<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_300 -->|"El fiscal archiva o desestima"| EXT_IPP_500_destino
  EXT_IPP_510_destino["IPP_510 Criterios especiales de archivo (principio de oportunidad)<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_300 -->|"Criterio especial de archivo (art. 56 bis)"| EXT_IPP_510_destino
  EXT_IPP_520_destino["IPP_520 Mediación penal<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_300 -->|"Derivación a mediación"| EXT_IPP_520_destino
  EXT_IPP_530_destino["IPP_530 Audiencia de suspensión del juicio a prueba<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_300 -->|"Pedido de suspensión del juicio a prueba"| EXT_IPP_530_destino
  EXT_IPP_540_destino["IPP_540 Conciliación o reparación integral<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_300 -->|"Propuesta de conciliación o reparación integral"| EXT_IPP_540_destino
  EXT_IPP_600_destino["IPP_600 Cierre de la investigación<br/>(ver Etapa intermedia)"]:::externo
  IPP_300 -->|"Investigación concluida: cierre de la IPP"| EXT_IPP_600_destino
  FIN_IPP_310_1(["Fin de este camino"]):::fin
  IPP_310 -->|"Medida cumplida, rechazada o impugnada"| FIN_IPP_310_1
  FIN_IPP_320_1(["Fin de este camino"]):::fin
  IPP_320 -->|"Pericia cumplida o impugnada"| FIN_IPP_320_1
  FIN_IPP_330_1(["Fin de este camino"]):::fin
  IPP_330 -->|"Declaración o informe incorporado"| FIN_IPP_330_1
  FIN_IPP_340_1(["Fin de este camino"]):::fin
  IPP_340 -->|"Medida cumplida, vencida o rechazada"| FIN_IPP_340_1
  IPP_340 -->|"Medida dictada sin sustanciación: reposición"| IPP_800
  EXT_IPP_500_origen["IPP_500 Archivo o desestimación y su revisión ante el Fiscal General<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_500_origen -.->|"La revisión revoca el archivo: sigue la IPP"| IPP_300
  EXT_IPP_510_origen["IPP_510 Criterios especiales de archivo (principio de oportunidad)<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_510_origen -.->|"La revisión lo revoca o se incumplen las condiciones"| IPP_300
  EXT_IPP_520_origen["IPP_520 Mediación penal<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_520_origen -.->|"Sin acuerdo o acuerdo incumplido: sigue la IPP"| IPP_300
  EXT_IPP_530_origen["IPP_530 Audiencia de suspensión del juicio a prueba<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_530_origen -.->|"Suspensión rechazada: sigue la IPP"| IPP_300
  EXT_IPP_535_origen["IPP_535 Plazo de suspensión y control de las reglas de conducta<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_535_origen -.->|"Suspensión revocada: el proceso continúa"| IPP_300
  EXT_IPP_540_origen["IPP_540 Conciliación o reparación integral<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_540_origen -.->|"Sin acuerdo: sigue la IPP"| IPP_300
  EXT_IPP_605_origen["IPP_605 Revisión de diligencias denegadas ante el Fiscal General<br/>(ver Etapa intermedia)"]:::externo
  EXT_IPP_605_origen -.->|"El Fiscal General ordena producir las diligencias"| IPP_300
  EXT_IPP_700_origen["IPP_700 Declaración del caso como de flagrancia (48 horas)<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_700_origen -.->|"No se declara la flagrancia: trámite ordinario"| IPP_300
  FIN_IPP_800_1(["Fin de este camino"]):::fin
  IPP_800 -->|"Reposición resuelta o plazo vencido"| FIN_IPP_800_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Plazo de la investigación

```mermaid
flowchart TD
  subgraph F_0["Plazo IPP"]
    IPP_400["<b>IPP_400</b> Plazo legal de la IPP (4 meses)<br/>Responsable: Fiscal / particular damnificado<br/>4 meses"]:::actora
    IPP_410["<b>IPP_410</b> Prórroga de la IPP<br/>Responsable: Fiscal / particular damnificado<br/>2 meses"]:::actora
    IPP_420["<b>IPP_420</b> Vencimiento del plazo y sustitución del fiscal<br/>Responsable: Juez de Garantías u órgano<br/>2 meses"]:::tribunal
  end
  EXT_IPP_100_origen["IPP_100 Apertura o radicación de la IPP ante el Fiscal<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_100_origen -.->|"Imputado aprehendido o detenido (trámite ordinario)"| IPP_400
  EXT_IPP_120_origen["IPP_120 Citación y declaración del imputado no detenido<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_120_origen -.->|"Declaración recibida o negativa a declarar: corre el plazo de la IPP"| IPP_400
  EXT_IPP_120_origen -.->|"Se ordena la detención"| IPP_400
  EXT_IPP_300_origen["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  EXT_IPP_300_origen -.->|"Se detiene al imputado, que todavía no había declarado"| IPP_400
  FIN_IPP_400_1(["Fin de este camino"]):::fin
  IPP_400 -->|"La IPP se cierra dentro del plazo"| FIN_IPP_400_1
  IPP_400 -->|"El fiscal dispone la prórroga"| IPP_410
  IPP_400 -->|"Vence el plazo sin cierre"| IPP_420
  FIN_IPP_410_1(["Fin de este camino"]):::fin
  IPP_410 -->|"La IPP se cierra durante la prórroga"| FIN_IPP_410_1
  IPP_410 -->|"Vence la prórroga sin cierre"| IPP_420
  FIN_IPP_420_1(["Fin de este camino"]):::fin
  IPP_420 -->|"El nuevo fiscal cierra la IPP dentro de los 2 meses"| FIN_IPP_420_1
  FIN_IPP_420_2(["Fin de este camino"]):::fin
  IPP_420 -->|"Vencen los 2 meses: la defensa pide el sobreseimiento (art. 323 inc. 6)"| FIN_IPP_420_2
  EXT_IPP_700_origen["IPP_700 Declaración del caso como de flagrancia (48 horas)<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_700_origen -.->|"No se declara la flagrancia: trámite ordinario"| IPP_400
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Salidas alternativas y anticipadas

```mermaid
flowchart TD
  subgraph F_0["Salidas alternativas"]
    IPP_500["<b>IPP_500</b> Archivo o desestimación y su revisión ante el Fiscal General<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_510["<b>IPP_510</b> Criterios especiales de archivo (principio de oportunidad)<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_520["<b>IPP_520</b> Mediación penal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_530["<b>IPP_530</b> Audiencia de suspensión del juicio a prueba<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    IPP_535["<b>IPP_535</b> Plazo de suspensión y control de las reglas de conducta<br/>Responsable: Imputado / defensa<br/>1 año"]:::demandada
    IPP_540["<b>IPP_540</b> Conciliación o reparación integral<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_550["<b>IPP_550</b> Extinción por prescripción<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_IPP_050_origen["IPP_050 Control de prescripción de la acción<br/>(ver Etapa previa)"]:::externo
  EXT_IPP_050_origen -.->|"La acción está prescrita"| IPP_550
  EXT_IPP_300_origen["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  EXT_IPP_300_origen -.->|"El fiscal archiva o desestima"| IPP_500
  EXT_IPP_300_origen -.->|"Criterio especial de archivo (art. 56 bis)"| IPP_510
  EXT_IPP_300_origen -.->|"Derivación a mediación"| IPP_520
  EXT_IPP_300_origen -.->|"Pedido de suspensión del juicio a prueba"| IPP_530
  EXT_IPP_300_origen -.->|"Propuesta de conciliación o reparación integral"| IPP_540
  EXT_IPP_900_destino["IPP_900 Regulación e impugnación de honorarios<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_500 -->|"Archivo o desestimación firmes"| EXT_IPP_900_destino
  EXT_IPP_300_destino["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  IPP_500 -->|"La revisión revoca el archivo: sigue la IPP"| EXT_IPP_300_destino
  IPP_510 -->|"Archivo firme, sin condiciones o con las condiciones cumplidas"| EXT_IPP_900_destino
  IPP_510 -->|"La revisión lo revoca o se incumplen las condiciones"| EXT_IPP_300_destino
  IPP_520 -->|"Acuerdo cumplido"| EXT_IPP_900_destino
  IPP_520 -->|"Sin acuerdo o acuerdo incumplido: sigue la IPP"| EXT_IPP_300_destino
  IPP_530 -->|"Suspensión concedida"| IPP_535
  IPP_530 -->|"Suspensión rechazada: sigue la IPP"| EXT_IPP_300_destino
  EXT_IPP_730_destino["IPP_730 Requisitoria en flagrancia (5 días)<br/>(ver Procedimiento de flagrancia)"]:::externo
  IPP_530 -->|"Suspensión rechazada en flagrancia: requisitoria"| EXT_IPP_730_destino
  IPP_535 -->|"Reglas cumplidas: extinción de la acción"| EXT_IPP_900_destino
  IPP_535 -->|"Suspensión revocada: el proceso continúa"| EXT_IPP_300_destino
  IPP_540 -->|"Reparación cumplida: extinción de la acción"| EXT_IPP_900_destino
  IPP_540 -->|"Sin acuerdo: sigue la IPP"| EXT_IPP_300_destino
  IPP_550 -->|"Extinción declarada: sobreseimiento"| EXT_IPP_900_destino
  FIN_IPP_550_2(["Fin de este camino"]):::fin
  IPP_550 -->|"Extinción rechazada"| FIN_IPP_550_2
  EXT_IPP_720_origen["IPP_720 Pedido temprano de probation, abreviado o directísimo<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_720_origen -.->|"Pedido de suspensión del juicio a prueba"| IPP_530
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Etapa intermedia

```mermaid
flowchart TD
  subgraph F_0["Etapa intermedia"]
    IPP_600["<b>IPP_600</b> Cierre de la investigación<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_605["<b>IPP_605</b> Revisión de diligencias denegadas ante el Fiscal General<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    IPP_610["<b>IPP_610</b> Pedido de sobreseimiento del fiscal<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_612["<b>IPP_612</b> Vista al Fiscal de Cámara sobre el sobreseimiento<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_614["<b>IPP_614</b> Acusación particular: vista de 15 días al particular damnificado<br/>Responsable: Fiscal / particular damnificado<br/>15 días corridos"]:::actora
    IPP_620["<b>IPP_620</b> Requerimiento de elevación a juicio<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    IPP_630["<b>IPP_630</b> Oposición de la defensa, renuncia al jurado y opción de tribunal<br/>Responsable: Imputado / defensa<br/>15 días corridos"]:::demandada
    IPP_640["<b>IPP_640</b> Resolución del Juez de Garantías<br/>Responsable: Juez de Garantías u órgano<br/>5 días corridos"]:::tribunal
    IPP_650["<b>IPP_650</b> Apelación del sobreseimiento o del auto de elevación<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    IPP_655["<b>IPP_655</b> Resolución de la Cámara de Apelación y Garantías<br/>Responsable: Juez de Garantías u órgano<br/>Sin plazo"]:::tribunal
  end
  EXT_IPP_300_origen["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  EXT_IPP_300_origen -.->|"Investigación concluida: cierre de la IPP"| IPP_600
  IPP_600 -->|"Hubo diligencias denegadas: se notifica el cierre"| IPP_605
  IPP_600 -->|"Pedido de sobreseimiento"| IPP_610
  IPP_600 -->|"Requerimiento de elevación a juicio"| IPP_620
  EXT_IPP_300_destino["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  IPP_605 -->|"El Fiscal General ordena producir las diligencias"| EXT_IPP_300_destino
  IPP_605 -->|"Revisión rechazada o no pedida: pedido de sobreseimiento"| IPP_610
  IPP_605 -->|"Revisión rechazada o no pedida: requerimiento de elevación"| IPP_620
  IPP_610 -->|"Sin particular damnificado: resuelve el Juez de Garantías"| IPP_640
  IPP_610 -->|"Con particular damnificado: vista al Fiscal de Cámara"| IPP_612
  IPP_612 -->|"No sostiene el sobreseimiento: otro fiscal requiere la elevación"| IPP_620
  IPP_612 -->|"Mantiene el sobreseimiento: vista al particular damnificado"| IPP_614
  IPP_614 -->|"El particular damnificado requiere la elevación a su costa"| IPP_630
  IPP_614 -->|"Vence sin requerimiento: sobreseimiento"| IPP_640
  IPP_620 -->|"Requerimiento notificado a la defensa"| IPP_630
  EXT_IPP_955_destino["IPP_955 Sigue en la matriz de juicio abreviado<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_620 -->|"Acuerdo de juicio abreviado"| EXT_IPP_955_destino
  IPP_630 -->|"La defensa se opone (sobreseimiento, calificación o excepciones)"| IPP_640
  EXT_IPP_950_destino["IPP_950 Sigue en la matriz de juicio oral<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_630 -->|"Vence sin oposición: elevación por simple decreto (art. 337)"| EXT_IPP_950_destino
  IPP_630 -->|"Acuerdo de juicio abreviado"| EXT_IPP_955_destino
  IPP_640 -->|"Auto de elevación a juicio"| IPP_650
  IPP_640 -->|"Sobreseimiento"| IPP_650
  IPP_640 -->|"El juez no comparte el pedido de sobreseimiento: eleva al Fiscal de Cámara (art. 326)"| IPP_612
  IPP_650 -->|"No se apela: elevación firme"| EXT_IPP_950_destino
  EXT_IPP_900_destino["IPP_900 Regulación e impugnación de honorarios<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_650 -->|"No se apela: sobreseimiento firme"| EXT_IPP_900_destino
  IPP_650 -->|"Apelación interpuesta"| IPP_655
  IPP_655 -->|"La Cámara confirma o dispone la elevación"| EXT_IPP_950_destino
  IPP_655 -->|"La Cámara confirma o dispone el sobreseimiento"| EXT_IPP_900_destino
  IPP_655 -->|"La Cámara revoca el sobreseimiento: nuevo requerimiento fiscal (a verificar)"| IPP_600
  EXT_IPP_730_origen["IPP_730 Requisitoria en flagrancia (5 días)<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_730_origen -.->|"Requisitoria de elevación"| IPP_620
  EXT_IPP_730_origen -.->|"Requisitoria de elevación con detenido: pedido de prisión preventiva"| IPP_620
  EXT_IPP_730_origen -.->|"Pedido de sobreseimiento"| IPP_610
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Procedimiento de flagrancia

```mermaid
flowchart TD
  subgraph F_0["Flagrancia"]
    IPP_700["<b>IPP_700</b> Declaración del caso como de flagrancia (48 horas)<br/>Responsable: Fiscal / particular damnificado<br/>48 horas"]:::actora
    IPP_710["<b>IPP_710</b> Plazo de investigación en flagrancia (20 días)<br/>Responsable: Fiscal / particular damnificado<br/>20 días corridos"]:::actora
    IPP_720["<b>IPP_720</b> Pedido temprano de probation, abreviado o directísimo<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_730["<b>IPP_730</b> Requisitoria en flagrancia (5 días)<br/>Responsable: Fiscal / particular damnificado<br/>5 días corridos"]:::actora
  end
  EXT_IPP_100_origen["IPP_100 Apertura o radicación de la IPP ante el Fiscal<br/>(ver Apertura de la IPP)"]:::externo
  EXT_IPP_100_origen -.->|"Aprehensión en flagrancia (art. 284 bis)"| IPP_700
  EXT_IPP_530_origen["IPP_530 Audiencia de suspensión del juicio a prueba<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_530_origen -.->|"Suspensión rechazada en flagrancia: requisitoria"| IPP_730
  IPP_700 -->|"Caso declarado de flagrancia"| IPP_710
  P_IPP_700_2(["Se abren en paralelo"]):::paralelo
  IPP_700 -->|"No se declara la flagrancia: trámite ordinario"| P_IPP_700_2
  EXT_IPP_300_destino["IPP_300 Pedidos de prueba de las partes e investigación del fiscal<br/>(ver Prueba)"]:::externo
  P_IPP_700_2 --> EXT_IPP_300_destino
  EXT_IPP_400_destino["IPP_400 Plazo legal de la IPP (4 meses)<br/>(ver Plazo de la investigación)"]:::externo
  P_IPP_700_2 --> EXT_IPP_400_destino
  IPP_710 -->|"Salida temprana dentro del plazo"| IPP_720
  IPP_710 -->|"Vence el plazo o el fiscal decide requerir"| IPP_730
  IPP_710 -->|"El juez prorroga 20 días"| IPP_710
  EXT_IPP_955_destino["IPP_955 Sigue en la matriz de juicio abreviado<br/>(ver Cierre y derivaciones)"]:::externo
  IPP_720 -->|"Acuerdo de juicio abreviado o directísimo"| EXT_IPP_955_destino
  EXT_IPP_530_destino["IPP_530 Audiencia de suspensión del juicio a prueba<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  IPP_720 -->|"Pedido de suspensión del juicio a prueba"| EXT_IPP_530_destino
  IPP_720 -->|"Sin acuerdo temprano: requisitoria"| IPP_730
  EXT_IPP_620_destino["IPP_620 Requerimiento de elevación a juicio<br/>(ver Etapa intermedia)"]:::externo
  IPP_730 -->|"Requisitoria de elevación"| EXT_IPP_620_destino
  P_IPP_730_2(["Se abren en paralelo"]):::paralelo
  IPP_730 -->|"Requisitoria de elevación con detenido: pedido de prisión preventiva"| P_IPP_730_2
  P_IPP_730_2 --> EXT_IPP_620_destino
  EXT_IPP_250_destino["IPP_250 Pedido de prisión preventiva por el Fiscal<br/>(ver Situación de libertad del imputado)"]:::externo
  P_IPP_730_2 --> EXT_IPP_250_destino
  EXT_IPP_610_destino["IPP_610 Pedido de sobreseimiento del fiscal<br/>(ver Etapa intermedia)"]:::externo
  IPP_730 -->|"Pedido de sobreseimiento"| EXT_IPP_610_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 9. Cierre y derivaciones

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    IPP_900["<b>IPP_900</b> Regulación e impugnación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    IPP_950["<b>IPP_950</b> Sigue en la matriz de juicio oral<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_955["<b>IPP_955</b> Sigue en la matriz de juicio abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    IPP_960["<b>IPP_960</b> Sigue en la matriz de hábeas corpus<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    IPP_990["<b>IPP_990</b> Archivo, extinción o sobreseimiento firme<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_IPP_210_origen["IPP_210 Comunicación al Juez de Garantías y puesta a disposición<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_210_origen -.->|"Sin puesta a disposición: hábeas corpus"| IPP_960
  EXT_IPP_220_origen["IPP_220 Declaración del imputado (con detenido: 24 horas)<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_220_origen -.->|"Vencido el plazo sin declaración: pedir la libertad o hábeas corpus"| IPP_960
  EXT_IPP_240_origen["IPP_240 Resolución del pedido de excarcelación<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_240_origen -.->|"Excarcelación denegada: hábeas corpus"| IPP_960
  EXT_IPP_260_origen["IPP_260 Auto de prisión preventiva<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_260_origen -.->|"PP dictada: hábeas corpus ante la Cámara (art. 405)"| IPP_960
  EXT_IPP_270_origen["IPP_270 Apelación de la coerción o de la denegatoria de excarcelación<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_270_origen -.->|"Se opta por el hábeas corpus (art. 164)"| IPP_960
  EXT_IPP_290_origen["IPP_290 Control del plazo máximo con detenido (2 años)<br/>(ver Situación de libertad del imputado)"]:::externo
  EXT_IPP_290_origen -.->|"Vence el plazo: hábeas corpus"| IPP_960
  EXT_IPP_500_origen["IPP_500 Archivo o desestimación y su revisión ante el Fiscal General<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_500_origen -.->|"Archivo o desestimación firmes"| IPP_900
  EXT_IPP_510_origen["IPP_510 Criterios especiales de archivo (principio de oportunidad)<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_510_origen -.->|"Archivo firme, sin condiciones o con las condiciones cumplidas"| IPP_900
  EXT_IPP_520_origen["IPP_520 Mediación penal<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_520_origen -.->|"Acuerdo cumplido"| IPP_900
  EXT_IPP_535_origen["IPP_535 Plazo de suspensión y control de las reglas de conducta<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_535_origen -.->|"Reglas cumplidas: extinción de la acción"| IPP_900
  EXT_IPP_540_origen["IPP_540 Conciliación o reparación integral<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_540_origen -.->|"Reparación cumplida: extinción de la acción"| IPP_900
  EXT_IPP_550_origen["IPP_550 Extinción por prescripción<br/>(ver Salidas alternativas y anticipadas)"]:::externo
  EXT_IPP_550_origen -.->|"Extinción declarada: sobreseimiento"| IPP_900
  EXT_IPP_620_origen["IPP_620 Requerimiento de elevación a juicio<br/>(ver Etapa intermedia)"]:::externo
  EXT_IPP_620_origen -.->|"Acuerdo de juicio abreviado"| IPP_955
  EXT_IPP_630_origen["IPP_630 Oposición de la defensa, renuncia al jurado y opción de tribunal<br/>(ver Etapa intermedia)"]:::externo
  EXT_IPP_630_origen -.->|"Vence sin oposición: elevación por simple decreto (art. 337)"| IPP_950
  EXT_IPP_630_origen -.->|"Acuerdo de juicio abreviado"| IPP_955
  EXT_IPP_650_origen["IPP_650 Apelación del sobreseimiento o del auto de elevación<br/>(ver Etapa intermedia)"]:::externo
  EXT_IPP_650_origen -.->|"No se apela: elevación firme"| IPP_950
  EXT_IPP_650_origen -.->|"No se apela: sobreseimiento firme"| IPP_900
  EXT_IPP_655_origen["IPP_655 Resolución de la Cámara de Apelación y Garantías<br/>(ver Etapa intermedia)"]:::externo
  EXT_IPP_655_origen -.->|"La Cámara confirma o dispone la elevación"| IPP_950
  EXT_IPP_655_origen -.->|"La Cámara confirma o dispone el sobreseimiento"| IPP_900
  EXT_IPP_720_origen["IPP_720 Pedido temprano de probation, abreviado o directísimo<br/>(ver Procedimiento de flagrancia)"]:::externo
  EXT_IPP_720_origen -.->|"Acuerdo de juicio abreviado o directísimo"| IPP_955
  IPP_900 -->|"Honorarios firmes, impugnación resuelta o sin regulación"| IPP_990
  style IPP_950 stroke-width:3px
  style IPP_955 stroke-width:3px
  style IPP_960 stroke-width:3px
  style IPP_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
