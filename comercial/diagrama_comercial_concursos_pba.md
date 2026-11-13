# Diagrama de Flujo: Concursos y quiebras - Provincia de Buenos Aires

**Régimen:** Ley 24.522 de Concursos y Quiebras; CPCCBA (Decreto-Ley 7425/68) supletorio (art. 278 LCQ) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_comercial_concursos_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = deudor (concursado o fallido); naranja = acreedores; gris = juzgado, síndico, comité de control o enajenador; violeta = cualquier interesado.
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, al abrirse el concurso corren a la vez la publicación de edictos, la entrega de libros, la carta del síndico, el plazo de verificación y los efectos sobre los juicios.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Hitos "Sigue en la matriz de ...":** son finales. El expediente continúa con el flujo de otra matriz comercial y hay que vincular los dos expedientes en la app (ver las dudas de producto de la matriz de concursos).
* **Cronograma del juez ("Fecha y hora fijadas por el tribunal"):** el auto de apertura o la sentencia de quiebra fija de una vez las fechas de verificación, informes y audiencia informativa; cada fecha se carga en su hito al abrirse (duda D03).
* **Hitos compartidos:** la verificación y el informe general valen para el concurso preventivo y para la quiebra; la condición de salida dice por qué camino sigue.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>3 hitos"]
  FASE_2["Apertura<br/>11 hitos"]
  FASE_3["Verificación<br/>6 hitos"]
  FASE_4["Informe general<br/>4 hitos"]
  FASE_5["Exclusividad y acuerdo<br/>5 hitos"]
  FASE_6["Homologación y cumplimiento<br/>5 hitos"]
  FASE_7["Cramdown<br/>3 hitos"]
  FASE_8["APE<br/>3 hitos"]
  FASE_9["Quiebra<br/>4 hitos"]
  FASE_10["Efectos de la quiebra<br/>7 hitos"]
  FASE_11["Acciones de la quiebra<br/>4 hitos"]
  FASE_12["Liquidación<br/>6 hitos"]
  FASE_13["Conclusión<br/>4 hitos"]
  FASE_14["Cierre<br/>4 hitos"]
  FASE_1 --> FASE_9
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_8
  FASE_2 --> FASE_3
  FASE_2 --> FASE_14
  FASE_3 --> FASE_4
  FASE_4 --> FASE_11
  FASE_4 --> FASE_5
  FASE_5 --> FASE_7
  FASE_5 --> FASE_9
  FASE_5 --> FASE_6
  FASE_6 --> FASE_14
  FASE_6 --> FASE_7
  FASE_6 --> FASE_9
  FASE_7 --> FASE_9
  FASE_7 --> FASE_5
  FASE_8 --> FASE_14
  FASE_8 --> FASE_1
  FASE_9 --> FASE_14
  FASE_9 --> FASE_3
  FASE_9 --> FASE_10
  FASE_10 --> FASE_14
  FASE_10 --> FASE_2
  FASE_10 --> FASE_12
  FASE_12 --> FASE_13
  FASE_12 --> FASE_14
  FASE_13 --> FASE_14
  FASE_13 --> FASE_12
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    CYQ_010["INICIO - <b>CYQ_010</b> Diagnóstico de la insolvencia y elección de la vía<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
    CYQ_020["<b>CYQ_020</b> Resolución del órgano de administración y armado de la presentación<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
    CYQ_030["<b>CYQ_030</b> Negociación del acuerdo preventivo extrajudicial<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
  end
  CYQ_010 -->|"Deudor: negociar un acuerdo extrajudicial"| CYQ_030
  CYQ_010 -->|"Deudor: pedir el concurso preventivo"| CYQ_020
  EXT_CYQ_710_destino["CYQ_710 Pedido de quiebra propia<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  CYQ_010 -->|"Deudor: pedir su propia quiebra"| EXT_CYQ_710_destino
  EXT_CYQ_700_destino["CYQ_700 Pedido de quiebra por un acreedor<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  CYQ_010 -->|"Acreedor: pedir la quiebra del deudor"| EXT_CYQ_700_destino
  EXT_CYQ_200_destino["CYQ_200 Pedidos de verificación ante el síndico<br/>(ver Verificación de créditos (concurso preventivo y quiebra))"]:::externo
  CYQ_010 -->|"Acreedor: el deudor ya está en concurso o en quiebra"| EXT_CYQ_200_destino
  EXT_CYQ_100_destino["CYQ_100 Presentación en concurso preventivo<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  CYQ_020 -->|"Presentación lista"| EXT_CYQ_100_destino
  EXT_CYQ_600_destino["CYQ_600 Pedido de homologación del acuerdo extrajudicial<br/>(ver Acuerdo preventivo extrajudicial)"]:::externo
  CYQ_030 -->|"Mayorías obtenidas"| EXT_CYQ_600_destino
  CYQ_030 -->|"No se obtienen las mayorías"| CYQ_020
  EXT_CYQ_630_origen["CYQ_630 Resolución sobre la homologación del APE<br/>(ver Acuerdo preventivo extrajudicial)"]:::externo
  EXT_CYQ_630_origen -.->|"Homologación rechazada"| CYQ_010
  style CYQ_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Concurso preventivo: presentación y apertura

```mermaid
flowchart TD
  subgraph F_0["Apertura"]
    CYQ_100["<b>CYQ_100</b> Presentación en concurso preventivo<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
    CYQ_105["<b>CYQ_105</b> Ratificación por el órgano de gobierno<br/>Responsable: Deudor<br/>30 días hábiles judiciales + gracia"]:::actora
    CYQ_110["<b>CYQ_110</b> Completar los requisitos del art. 11<br/>Responsable: Deudor<br/>10 días hábiles judiciales + gracia"]:::actora
    CYQ_120["<b>CYQ_120</b> Resolución de apertura o rechazo<br/>Responsable: Juzgado o síndico<br/>5 días hábiles judiciales"]:::tribunal
    CYQ_125["<b>CYQ_125</b> Apelación del rechazo de la apertura<br/>Responsable: Deudor<br/>5 días hábiles judiciales + gracia"]:::actora
    CYQ_130["<b>CYQ_130</b> Publicación de edictos del concurso<br/>Responsable: Deudor<br/>5 días hábiles judiciales + gracia"]:::actora
    CYQ_140["<b>CYQ_140</b> Presentación de libros y depósito de gastos de correspondencia<br/>Responsable: Deudor<br/>3 días hábiles judiciales + gracia"]:::actora
    CYQ_150["<b>CYQ_150</b> Aceptación del cargo del síndico y cartas a los acreedores<br/>Responsable: Juzgado o síndico<br/>5 días hábiles judiciales"]:::tribunal
    CYQ_155["<b>CYQ_155</b> Informe sobre pasivos laborales y pronto pago<br/>Responsable: Juzgado o síndico<br/>10 días hábiles judiciales"]:::tribunal
    CYQ_160["<b>CYQ_160</b> Suspensión de juicios y fuero de atracción<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    CYQ_165["<b>CYQ_165</b> Contratos con prestaciones recíprocas pendientes<br/>Responsable: Deudor<br/>30 días hábiles judiciales + gracia"]:::actora
  end
  EXT_CYQ_020_origen["CYQ_020 Resolución del órgano de administración y armado de la presentación<br/>(ver Etapa previa)"]:::externo
  EXT_CYQ_020_origen -.->|"Presentación lista"| CYQ_100
  P_CYQ_100_1(["Se abren en paralelo"]):::paralelo
  CYQ_100 -->|"Presentación realizada"| P_CYQ_100_1
  P_CYQ_100_1 --> CYQ_105
  P_CYQ_100_1 --> CYQ_120
  EXT_CYQ_250_destino["CYQ_250 Verificación tardía<br/>(ver Verificación de créditos (concurso preventivo y quiebra))"]:::externo
  P_CYQ_100_1 --> EXT_CYQ_250_destino
  CYQ_100 -->|"Faltan requisitos y el juez concede plazo"| CYQ_110
  FIN_CYQ_105_1(["Fin de este camino"]):::fin
  CYQ_105 -->|"Ratificación acreditada o persona humana"| FIN_CYQ_105_1
  EXT_CYQ_990_destino["CYQ_990 Archivo del expediente<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_105 -->|"No se acredita: cese del procedimiento"| EXT_CYQ_990_destino
  CYQ_110 -->|"Requisitos completados o plazo vencido"| CYQ_120
  P_CYQ_120_1(["Se abren en paralelo"]):::paralelo
  CYQ_120 -->|"Concurso abierto"| P_CYQ_120_1
  P_CYQ_120_1 --> CYQ_130
  P_CYQ_120_1 --> CYQ_140
  P_CYQ_120_1 --> CYQ_150
  P_CYQ_120_1 --> CYQ_160
  P_CYQ_120_1 --> CYQ_165
  EXT_CYQ_200_destino["CYQ_200 Pedidos de verificación ante el síndico<br/>(ver Verificación de créditos (concurso preventivo y quiebra))"]:::externo
  P_CYQ_120_1 --> EXT_CYQ_200_destino
  CYQ_120 -->|"Apertura rechazada"| CYQ_125
  CYQ_125 -->|"La Cámara revoca y ordena la apertura"| CYQ_120
  CYQ_125 -->|"Rechazo firme"| EXT_CYQ_990_destino
  FIN_CYQ_130_1(["Fin de este camino"]):::fin
  CYQ_130 -->|"Edictos publicados y acreditados"| FIN_CYQ_130_1
  CYQ_130 -->|"No se publican en término: desistimiento"| EXT_CYQ_990_destino
  FIN_CYQ_140_1(["Fin de este camino"]):::fin
  CYQ_140 -->|"Libros presentados y gastos depositados"| FIN_CYQ_140_1
  CYQ_140 -->|"No se deposita en término: desistimiento"| EXT_CYQ_990_destino
  CYQ_150 -->|"Cartas enviadas"| CYQ_155
  FIN_CYQ_155_1(["Fin de este camino"]):::fin
  CYQ_155 -->|"Informe presentado y pronto pago resuelto"| FIN_CYQ_155_1
  FIN_CYQ_160_1(["Fin de este camino"]):::fin
  CYQ_160 -->|"Juicios suspendidos o radicados"| FIN_CYQ_160_1
  FIN_CYQ_165_1(["Fin de este camino"]):::fin
  CYQ_165 -->|"Autorización resuelta o plazo vencido"| FIN_CYQ_165_1
  EXT_CYQ_740_origen["CYQ_740 Conversión de la quiebra en concurso preventivo<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  EXT_CYQ_740_origen -.->|"Conversión admitida"| CYQ_120
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Verificación de créditos (concurso preventivo y quiebra)

```mermaid
flowchart TD
  subgraph F_0["Verificación"]
    CYQ_200["<b>CYQ_200</b> Pedidos de verificación ante el síndico<br/>Responsable: Acreedores<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    CYQ_210["<b>CYQ_210</b> Período de observación de los pedidos<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales + gracia"]:::ambas
    CYQ_220["<b>CYQ_220</b> Informe individual del síndico<br/>Responsable: Juzgado o síndico<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    CYQ_230["<b>CYQ_230</b> Resolución de verificación de créditos (art. 36)<br/>Responsable: Juzgado o síndico<br/>10 días hábiles judiciales"]:::tribunal
    CYQ_240["<b>CYQ_240</b> Incidente de revisión<br/>Responsable: Cualquier interesado<br/>20 días hábiles judiciales + gracia"]:::ambas
    CYQ_250["<b>CYQ_250</b> Verificación tardía<br/>Responsable: Acreedores<br/>2 años"]:::demandada
  end
  EXT_CYQ_010_origen["CYQ_010 Diagnóstico de la insolvencia y elección de la vía<br/>(ver Etapa previa)"]:::externo
  EXT_CYQ_010_origen -.->|"Acreedor: el deudor ya está en concurso o en quiebra"| CYQ_200
  EXT_CYQ_100_origen["CYQ_100 Presentación en concurso preventivo<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_100_origen -.->|"Presentación realizada"| CYQ_250
  EXT_CYQ_120_origen["CYQ_120 Resolución de apertura o rechazo<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_120_origen -.->|"Concurso abierto"| CYQ_200
  CYQ_200 -->|"Vencido el plazo de verificación"| CYQ_210
  CYQ_210 -->|"Vencido el período de observación"| CYQ_220
  CYQ_220 -->|"Informe individual presentado"| CYQ_230
  P_CYQ_230_1(["Se abren en paralelo"]):::paralelo
  CYQ_230 -->|"Resolución dictada en el concurso preventivo"| P_CYQ_230_1
  P_CYQ_230_1 --> CYQ_240
  EXT_CYQ_300_destino["CYQ_300 Propuesta de categorización de los acreedores<br/>(ver Informe general y categorización)"]:::externo
  P_CYQ_230_1 --> EXT_CYQ_300_destino
  EXT_CYQ_310_destino["CYQ_310 Informe general del síndico<br/>(ver Informe general y categorización)"]:::externo
  P_CYQ_230_1 --> EXT_CYQ_310_destino
  P_CYQ_230_2(["Se abren en paralelo"]):::paralelo
  CYQ_230 -->|"Resolución dictada en la quiebra"| P_CYQ_230_2
  P_CYQ_230_2 --> CYQ_240
  P_CYQ_230_2 --> EXT_CYQ_310_destino
  FIN_CYQ_240_1(["Fin de este camino"]):::fin
  CYQ_240 -->|"Revisión resuelta o no deducida"| FIN_CYQ_240_1
  FIN_CYQ_250_1(["Fin de este camino"]):::fin
  CYQ_250 -->|"Pedido tardío presentado o plazo vencido"| FIN_CYQ_250_1
  EXT_CYQ_720_origen["CYQ_720 Sentencia de quiebra<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  EXT_CYQ_720_origen -.->|"Quiebra declarada"| CYQ_200
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Informe general y categorización

```mermaid
flowchart TD
  subgraph F_0["Informe general"]
    CYQ_300["<b>CYQ_300</b> Propuesta de categorización de los acreedores<br/>Responsable: Deudor<br/>10 días hábiles judiciales + gracia"]:::actora
    CYQ_310["<b>CYQ_310</b> Informe general del síndico<br/>Responsable: Juzgado o síndico<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    CYQ_320["<b>CYQ_320</b> Observaciones al informe general<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales + gracia"]:::ambas
    CYQ_330["<b>CYQ_330</b> Resolución de categorización y comité de control<br/>Responsable: Juzgado o síndico<br/>10 días hábiles judiciales"]:::tribunal
  end
  EXT_CYQ_230_origen["CYQ_230 Resolución de verificación de créditos (art. 36)<br/>(ver Verificación de créditos (concurso preventivo y quiebra))"]:::externo
  EXT_CYQ_230_origen -.->|"Resolución dictada en el concurso preventivo"| CYQ_300
  EXT_CYQ_230_origen -.->|"Resolución dictada en el concurso preventivo"| CYQ_310
  EXT_CYQ_230_origen -.->|"Resolución dictada en la quiebra"| CYQ_310
  FIN_CYQ_300_1(["Fin de este camino"]):::fin
  CYQ_300 -->|"Propuesta de categorización presentada"| FIN_CYQ_300_1
  CYQ_310 -->|"Informe presentado en el concurso preventivo"| CYQ_320
  P_CYQ_310_2(["Se abren en paralelo"]):::paralelo
  CYQ_310 -->|"Informe presentado en la quiebra"| P_CYQ_310_2
  P_CYQ_310_2 --> CYQ_320
  EXT_CYQ_760_destino["CYQ_760 Observación de la fecha de cesación de pagos<br/>(ver Quiebra: acciones de recomposición)"]:::externo
  P_CYQ_310_2 --> EXT_CYQ_760_destino
  EXT_CYQ_765_destino["CYQ_765 Ineficacia de actos y acción revocatoria concursal<br/>(ver Quiebra: acciones de recomposición)"]:::externo
  P_CYQ_310_2 --> EXT_CYQ_765_destino
  EXT_CYQ_770_destino["CYQ_770 Pedido de extensión de la quiebra<br/>(ver Quiebra: acciones de recomposición)"]:::externo
  P_CYQ_310_2 --> EXT_CYQ_770_destino
  EXT_CYQ_775_destino["CYQ_775 Acción de responsabilidad de administradores y terceros<br/>(ver Quiebra: acciones de recomposición)"]:::externo
  P_CYQ_310_2 --> EXT_CYQ_775_destino
  CYQ_320 -->|"Vencido el plazo en el concurso preventivo"| CYQ_330
  FIN_CYQ_320_2(["Fin de este camino"]):::fin
  CYQ_320 -->|"Vencido el plazo en la quiebra"| FIN_CYQ_320_2
  P_CYQ_330_1(["Se abren en paralelo"]):::paralelo
  CYQ_330 -->|"Resolución de categorización notificada"| P_CYQ_330_1
  EXT_CYQ_400_destino["CYQ_400 Vencimiento del período de exclusividad: acompañar las conformidades<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  P_CYQ_330_1 --> EXT_CYQ_400_destino
  EXT_CYQ_410_destino["CYQ_410 Propuesta de acuerdo pública en el expediente<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  P_CYQ_330_1 --> EXT_CYQ_410_destino
  EXT_CYQ_420_destino["CYQ_420 Audiencia informativa<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  P_CYQ_330_1 --> EXT_CYQ_420_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Período de exclusividad y acuerdo

```mermaid
flowchart TD
  subgraph F_0["Exclusividad y acuerdo"]
    CYQ_400["<b>CYQ_400</b> Vencimiento del período de exclusividad: acompañar las conformidades<br/>Responsable: Deudor<br/>Fecha y hora fijadas por el tribunal"]:::actora
    CYQ_410["<b>CYQ_410</b> Propuesta de acuerdo pública en el expediente<br/>Responsable: Deudor<br/>20 días hábiles de anticipación"]:::actora
    CYQ_420["<b>CYQ_420</b> Audiencia informativa<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CYQ_440["<b>CYQ_440</b> Resolución sobre la existencia de acuerdo<br/>Responsable: Juzgado o síndico<br/>3 días hábiles judiciales"]:::tribunal
    CYQ_450["<b>CYQ_450</b> Impugnación del acuerdo<br/>Responsable: Acreedores<br/>5 días hábiles judiciales + gracia"]:::demandada
  end
  EXT_CYQ_330_origen["CYQ_330 Resolución de categorización y comité de control<br/>(ver Informe general y categorización)"]:::externo
  EXT_CYQ_330_origen -.->|"Resolución de categorización notificada"| CYQ_400
  EXT_CYQ_330_origen -.->|"Resolución de categorización notificada"| CYQ_410
  EXT_CYQ_330_origen -.->|"Resolución de categorización notificada"| CYQ_420
  CYQ_400 -->|"Conformidades acreditadas en término"| CYQ_440
  EXT_CYQ_500_destino["CYQ_500 Registro de interesados en el salvataje (art. 48)<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  CYQ_400 -->|"Sin conformidades, sociedad comprendida en el art. 48"| EXT_CYQ_500_destino
  EXT_CYQ_720_destino["CYQ_720 Sentencia de quiebra<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  CYQ_400 -->|"Sin conformidades, otros deudores o pequeño concurso"| EXT_CYQ_720_destino
  FIN_CYQ_410_1(["Fin de este camino"]):::fin
  CYQ_410 -->|"Propuesta presentada"| FIN_CYQ_410_1
  FIN_CYQ_420_1(["Fin de este camino"]):::fin
  CYQ_420 -->|"Audiencia celebrada"| FIN_CYQ_420_1
  CYQ_440 -->|"Acuerdo declarado existente"| CYQ_450
  EXT_CYQ_460_destino["CYQ_460 Homologación del acuerdo<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  CYQ_450 -->|"Sin impugnaciones o impugnaciones rechazadas"| EXT_CYQ_460_destino
  CYQ_450 -->|"Impugnación admitida, sociedad comprendida en el art. 48"| EXT_CYQ_500_destino
  CYQ_450 -->|"Impugnación admitida, otros deudores"| EXT_CYQ_720_destino
  EXT_CYQ_520_origen["CYQ_520 Período para obtener las conformidades en el salvataje<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_520_origen -.->|"El deudor o un inscripto acredita las conformidades"| CYQ_440
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Homologación, cumplimiento y salvataje (art. 48)

```mermaid
flowchart TD
  subgraph F_0["Homologación y cumplimiento"]
    CYQ_460["<b>CYQ_460</b> Homologación del acuerdo<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_475["<b>CYQ_475</b> Pago de los honorarios del concurso<br/>Responsable: Deudor<br/>90 días hábiles judiciales"]:::actora
    CYQ_480["<b>CYQ_480</b> Conclusión del concurso y cumplimiento del acuerdo<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_485["<b>CYQ_485</b> Nulidad del acuerdo homologado<br/>Responsable: Acreedores<br/>6 meses"]:::demandada
    CYQ_490["<b>CYQ_490</b> Incumplimiento del acuerdo<br/>Responsable: Acreedores<br/>Sin plazo"]:::demandada
  end
  subgraph F_1["Cramdown"]
    CYQ_500["<b>CYQ_500</b> Registro de interesados en el salvataje (art. 48)<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    CYQ_510["<b>CYQ_510</b> Valuación de las cuotas o acciones<br/>Responsable: Juzgado o síndico<br/>30 días hábiles judiciales"]:::tribunal
    CYQ_520["<b>CYQ_520</b> Período para obtener las conformidades en el salvataje<br/>Responsable: Cualquier interesado<br/>20 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_CYQ_400_origen["CYQ_400 Vencimiento del período de exclusividad: acompañar las conformidades<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  EXT_CYQ_400_origen -.->|"Sin conformidades, sociedad comprendida en el art. 48"| CYQ_500
  EXT_CYQ_450_origen["CYQ_450 Impugnación del acuerdo<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  EXT_CYQ_450_origen -.->|"Sin impugnaciones o impugnaciones rechazadas"| CYQ_460
  EXT_CYQ_450_origen -.->|"Impugnación admitida, sociedad comprendida en el art. 48"| CYQ_500
  P_CYQ_460_1(["Se abren en paralelo"]):::paralelo
  CYQ_460 -->|"Acuerdo homologado"| P_CYQ_460_1
  P_CYQ_460_1 --> CYQ_475
  P_CYQ_460_1 --> CYQ_480
  P_CYQ_460_1 --> CYQ_485
  EXT_CYQ_900_destino["CYQ_900 Regulación de honorarios del concurso o la quiebra<br/>(ver Honorarios y cierre)"]:::externo
  P_CYQ_460_1 --> EXT_CYQ_900_destino
  CYQ_460 -->|"Homologación rechazada, sociedad comprendida en el art. 48"| CYQ_500
  EXT_CYQ_720_destino["CYQ_720 Sentencia de quiebra<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  CYQ_460 -->|"Homologación rechazada, otros deudores"| EXT_CYQ_720_destino
  FIN_CYQ_475_1(["Fin de este camino"]):::fin
  CYQ_475 -->|"Honorarios pagados"| FIN_CYQ_475_1
  CYQ_475 -->|"Falta de pago: se pide la quiebra"| EXT_CYQ_720_destino
  EXT_CYQ_990_destino["CYQ_990 Archivo del expediente<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_480 -->|"Acuerdo cumplido y declarado"| EXT_CYQ_990_destino
  CYQ_480 -->|"Obligación del acuerdo impaga"| CYQ_490
  FIN_CYQ_485_1(["Fin de este camino"]):::fin
  CYQ_485 -->|"Plazo vencido sin pedido o nulidad rechazada"| FIN_CYQ_485_1
  CYQ_485 -->|"Nulidad declarada"| EXT_CYQ_720_destino
  CYQ_490 -->|"Quiebra declarada por incumplimiento"| EXT_CYQ_720_destino
  CYQ_490 -->|"Pedido rechazado o incumplimiento subsanado"| CYQ_480
  CYQ_500 -->|"Hay inscriptos"| CYQ_510
  CYQ_500 -->|"Sin inscriptos"| EXT_CYQ_720_destino
  CYQ_510 -->|"Valor fijado por el juez"| CYQ_520
  EXT_CYQ_440_destino["CYQ_440 Resolución sobre la existencia de acuerdo<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  CYQ_520 -->|"El deudor o un inscripto acredita las conformidades"| EXT_CYQ_440_destino
  CYQ_520 -->|"Nadie obtiene las conformidades"| EXT_CYQ_720_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Acuerdo preventivo extrajudicial

```mermaid
flowchart TD
  subgraph F_0["APE"]
    CYQ_600["<b>CYQ_600</b> Pedido de homologación del acuerdo extrajudicial<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
    CYQ_620["<b>CYQ_620</b> Oposiciones a la homologación del APE<br/>Responsable: Acreedores<br/>10 días hábiles judiciales + gracia"]:::demandada
    CYQ_630["<b>CYQ_630</b> Resolución sobre la homologación del APE<br/>Responsable: Juzgado o síndico<br/>10 días hábiles judiciales"]:::tribunal
  end
  EXT_CYQ_030_origen["CYQ_030 Negociación del acuerdo preventivo extrajudicial<br/>(ver Etapa previa)"]:::externo
  EXT_CYQ_030_origen -.->|"Mayorías obtenidas"| CYQ_600
  CYQ_600 -->|"Edictos publicados"| CYQ_620
  CYQ_620 -->|"Sin oposiciones o resueltas"| CYQ_630
  EXT_CYQ_900_destino["CYQ_900 Regulación de honorarios del concurso o la quiebra<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_630 -->|"APE homologado"| EXT_CYQ_900_destino
  EXT_CYQ_010_destino["CYQ_010 Diagnóstico de la insolvencia y elección de la vía<br/>(ver Etapa previa)"]:::externo
  CYQ_630 -->|"Homologación rechazada"| EXT_CYQ_010_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Quiebra: pedido y sentencia

```mermaid
flowchart TD
  subgraph F_0["Quiebra"]
    CYQ_700["<b>CYQ_700</b> Pedido de quiebra por un acreedor<br/>Responsable: Acreedores<br/>Sin plazo"]:::demandada
    CYQ_705["<b>CYQ_705</b> Citación al deudor (art. 84)<br/>Responsable: Deudor<br/>5 días hábiles judiciales + gracia"]:::actora
    CYQ_710["<b>CYQ_710</b> Pedido de quiebra propia<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
    CYQ_720["<b>CYQ_720</b> Sentencia de quiebra<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
  end
  EXT_CYQ_010_origen["CYQ_010 Diagnóstico de la insolvencia y elección de la vía<br/>(ver Etapa previa)"]:::externo
  EXT_CYQ_010_origen -.->|"Deudor: pedir su propia quiebra"| CYQ_710
  EXT_CYQ_010_origen -.->|"Acreedor: pedir la quiebra del deudor"| CYQ_700
  EXT_CYQ_400_origen["CYQ_400 Vencimiento del período de exclusividad: acompañar las conformidades<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  EXT_CYQ_400_origen -.->|"Sin conformidades, otros deudores o pequeño concurso"| CYQ_720
  EXT_CYQ_450_origen["CYQ_450 Impugnación del acuerdo<br/>(ver Período de exclusividad y acuerdo)"]:::externo
  EXT_CYQ_450_origen -.->|"Impugnación admitida, otros deudores"| CYQ_720
  EXT_CYQ_460_origen["CYQ_460 Homologación del acuerdo<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_460_origen -.->|"Homologación rechazada, otros deudores"| CYQ_720
  EXT_CYQ_475_origen["CYQ_475 Pago de los honorarios del concurso<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_475_origen -.->|"Falta de pago: se pide la quiebra"| CYQ_720
  EXT_CYQ_485_origen["CYQ_485 Nulidad del acuerdo homologado<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_485_origen -.->|"Nulidad declarada"| CYQ_720
  EXT_CYQ_490_origen["CYQ_490 Incumplimiento del acuerdo<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_490_origen -.->|"Quiebra declarada por incumplimiento"| CYQ_720
  EXT_CYQ_500_origen["CYQ_500 Registro de interesados en el salvataje (art. 48)<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_500_origen -.->|"Sin inscriptos"| CYQ_720
  EXT_CYQ_520_origen["CYQ_520 Período para obtener las conformidades en el salvataje<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_520_origen -.->|"Nadie obtiene las conformidades"| CYQ_720
  CYQ_700 -->|"Pedido admitido formalmente"| CYQ_705
  CYQ_705 -->|"Quiebra declarada"| CYQ_720
  EXT_CYQ_990_destino["CYQ_990 Archivo del expediente<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_705 -->|"Pedido rechazado o desistido"| EXT_CYQ_990_destino
  CYQ_710 -->|"Pedido presentado"| CYQ_720
  P_CYQ_720_1(["Se abren en paralelo"]):::paralelo
  CYQ_720 -->|"Quiebra declarada"| P_CYQ_720_1
  EXT_CYQ_200_destino["CYQ_200 Pedidos de verificación ante el síndico<br/>(ver Verificación de créditos (concurso preventivo y quiebra))"]:::externo
  P_CYQ_720_1 --> EXT_CYQ_200_destino
  EXT_CYQ_725_destino["CYQ_725 Entrega de libros y constitución de domicilio por el fallido<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  P_CYQ_720_1 --> EXT_CYQ_725_destino
  EXT_CYQ_730_destino["CYQ_730 Publicación de edictos de la quiebra<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  P_CYQ_720_1 --> EXT_CYQ_730_destino
  EXT_CYQ_745_destino["CYQ_745 Incautación, inventario y desapoderamiento<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  P_CYQ_720_1 --> EXT_CYQ_745_destino
  EXT_CYQ_750_destino["CYQ_750 Inhabilitación del fallido<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  P_CYQ_720_1 --> EXT_CYQ_750_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 9. Quiebra: efectos de la sentencia

```mermaid
flowchart TD
  subgraph F_0["Efectos de la quiebra"]
    CYQ_725["<b>CYQ_725</b> Entrega de libros y constitución de domicilio por el fallido<br/>Responsable: Deudor<br/>24 horas"]:::actora
    CYQ_730["<b>CYQ_730</b> Publicación de edictos de la quiebra<br/>Responsable: Juzgado o síndico<br/>24 horas"]:::tribunal
    CYQ_735["<b>CYQ_735</b> Reposición o levantamiento sin trámite de la quiebra<br/>Responsable: Deudor<br/>5 días hábiles judiciales + gracia"]:::actora
    CYQ_740["<b>CYQ_740</b> Conversión de la quiebra en concurso preventivo<br/>Responsable: Deudor<br/>10 días hábiles judiciales + gracia"]:::actora
    CYQ_745["<b>CYQ_745</b> Incautación, inventario y desapoderamiento<br/>Responsable: Juzgado o síndico<br/>30 días hábiles judiciales"]:::tribunal
    CYQ_750["<b>CYQ_750</b> Inhabilitación del fallido<br/>Responsable: Juzgado o síndico<br/>1 año"]:::tribunal
    CYQ_755["<b>CYQ_755</b> Continuación de la explotación y cooperativa de trabajo<br/>Responsable: Juzgado o síndico<br/>20 días corridos"]:::tribunal
  end
  EXT_CYQ_720_origen["CYQ_720 Sentencia de quiebra<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  EXT_CYQ_720_origen -.->|"Quiebra declarada"| CYQ_725
  EXT_CYQ_720_origen -.->|"Quiebra declarada"| CYQ_730
  EXT_CYQ_720_origen -.->|"Quiebra declarada"| CYQ_745
  EXT_CYQ_720_origen -.->|"Quiebra declarada"| CYQ_750
  FIN_CYQ_725_1(["Fin de este camino"]):::fin
  CYQ_725 -->|"Libros entregados y domicilio constituido"| FIN_CYQ_725_1
  P_CYQ_730_1(["Se abren en paralelo"]):::paralelo
  CYQ_730 -->|"Edictos publicados"| P_CYQ_730_1
  P_CYQ_730_1 --> CYQ_735
  P_CYQ_730_1 --> CYQ_740
  EXT_CYQ_990_destino["CYQ_990 Archivo del expediente<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_735 -->|"Quiebra revocada o levantada"| EXT_CYQ_990_destino
  FIN_CYQ_735_2(["Fin de este camino"]):::fin
  CYQ_735 -->|"Recurso rechazado, no interpuesto o no procede"| FIN_CYQ_735_2
  EXT_CYQ_120_destino["CYQ_120 Resolución de apertura o rechazo<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  CYQ_740 -->|"Conversión admitida"| EXT_CYQ_120_destino
  FIN_CYQ_740_2(["Fin de este camino"]):::fin
  CYQ_740 -->|"No se pide o se rechaza"| FIN_CYQ_740_2
  P_CYQ_745_1(["Se abren en paralelo"]):::paralelo
  CYQ_745 -->|"Inventario presentado y bienes incautados"| P_CYQ_745_1
  P_CYQ_745_1 --> CYQ_755
  EXT_CYQ_800_destino["CYQ_800 Realización de los bienes<br/>(ver Quiebra: liquidación, distribución y conclusión)"]:::externo
  P_CYQ_745_1 --> EXT_CYQ_800_destino
  FIN_CYQ_750_1(["Fin de este camino"]):::fin
  CYQ_750 -->|"Inhabilitación cesada o prorrogada"| FIN_CYQ_750_1
  FIN_CYQ_755_1(["Fin de este camino"]):::fin
  CYQ_755 -->|"Continuación resuelta o descartada"| FIN_CYQ_755_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 10. Quiebra: acciones de recomposición

```mermaid
flowchart TD
  subgraph F_0["Acciones de la quiebra"]
    CYQ_760["<b>CYQ_760</b> Observación de la fecha de cesación de pagos<br/>Responsable: Cualquier interesado<br/>30 días hábiles judiciales + gracia"]:::ambas
    CYQ_765["<b>CYQ_765</b> Ineficacia de actos y acción revocatoria concursal<br/>Responsable: Juzgado o síndico<br/>3 años"]:::tribunal
    CYQ_770["<b>CYQ_770</b> Pedido de extensión de la quiebra<br/>Responsable: Cualquier interesado<br/>6 meses"]:::ambas
    CYQ_775["<b>CYQ_775</b> Acción de responsabilidad de administradores y terceros<br/>Responsable: Juzgado o síndico<br/>2 años"]:::tribunal
  end
  EXT_CYQ_310_origen["CYQ_310 Informe general del síndico<br/>(ver Informe general y categorización)"]:::externo
  EXT_CYQ_310_origen -.->|"Informe presentado en la quiebra"| CYQ_760
  EXT_CYQ_310_origen -.->|"Informe presentado en la quiebra"| CYQ_765
  EXT_CYQ_310_origen -.->|"Informe presentado en la quiebra"| CYQ_770
  EXT_CYQ_310_origen -.->|"Informe presentado en la quiebra"| CYQ_775
  FIN_CYQ_760_1(["Fin de este camino"]):::fin
  CYQ_760 -->|"Fecha de cesación de pagos fijada"| FIN_CYQ_760_1
  FIN_CYQ_765_1(["Fin de este camino"]):::fin
  CYQ_765 -->|"Acción resuelta o caducada"| FIN_CYQ_765_1
  FIN_CYQ_770_1(["Fin de este camino"]):::fin
  CYQ_770 -->|"Pedido resuelto o plazo vencido"| FIN_CYQ_770_1
  FIN_CYQ_775_1(["Fin de este camino"]):::fin
  CYQ_775 -->|"Acción resuelta o prescripta"| FIN_CYQ_775_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 11. Quiebra: liquidación, distribución y conclusión

```mermaid
flowchart TD
  subgraph F_0["Liquidación"]
    CYQ_800["<b>CYQ_800</b> Realización de los bienes<br/>Responsable: Juzgado o síndico<br/>4 meses"]:::tribunal
    CYQ_805["<b>CYQ_805</b> Subasta de bienes del fallido<br/>Responsable: Juzgado o síndico<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    CYQ_810["<b>CYQ_810</b> Informe final y proyecto de distribución<br/>Responsable: Juzgado o síndico<br/>10 días hábiles judiciales"]:::tribunal
    CYQ_815["<b>CYQ_815</b> Observaciones al informe final<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales + gracia"]:::ambas
    CYQ_820["<b>CYQ_820</b> Distribución y pago de dividendos<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_825["<b>CYQ_825</b> Cobro del dividendo concursal<br/>Responsable: Acreedores<br/>1 año"]:::demandada
  end
  subgraph F_1["Conclusión"]
    CYQ_830["<b>CYQ_830</b> Clausura por distribución final<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_835["<b>CYQ_835</b> Conclusión de la quiebra después de la clausura<br/>Responsable: Juzgado o síndico<br/>2 años"]:::tribunal
    CYQ_840["<b>CYQ_840</b> Clausura por falta de activo<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_850["<b>CYQ_850</b> Avenimiento, pago total o carta de pago<br/>Responsable: Deudor<br/>Sin plazo"]:::actora
  end
  EXT_CYQ_745_origen["CYQ_745 Incautación, inventario y desapoderamiento<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  EXT_CYQ_745_origen -.->|"Inventario presentado y bienes incautados"| CYQ_800
  CYQ_800 -->|"Subasta ordenada"| CYQ_805
  CYQ_800 -->|"Enajenación por otra vía aprobada (empresa en marcha, venta directa o licitación)"| CYQ_810
  CYQ_800 -->|"Activo insuficiente para los gastos"| CYQ_840
  CYQ_800 -->|"Avenimiento, pago total o carta de pago"| CYQ_850
  CYQ_805 -->|"Última enajenación aprobada"| CYQ_810
  CYQ_805 -->|"Quedan bienes por vender o subasta fracasada"| CYQ_800
  P_CYQ_810_1(["Se abren en paralelo"]):::paralelo
  CYQ_810 -->|"Informe presentado y edictos publicados"| P_CYQ_810_1
  P_CYQ_810_1 --> CYQ_815
  EXT_CYQ_900_destino["CYQ_900 Regulación de honorarios del concurso o la quiebra<br/>(ver Honorarios y cierre)"]:::externo
  P_CYQ_810_1 --> EXT_CYQ_900_destino
  CYQ_815 -->|"Proyecto de distribución aprobado"| CYQ_820
  P_CYQ_820_1(["Se abren en paralelo"]):::paralelo
  CYQ_820 -->|"Dividendos puestos a disposición"| P_CYQ_820_1
  P_CYQ_820_1 --> CYQ_825
  P_CYQ_820_1 --> CYQ_830
  FIN_CYQ_825_1(["Fin de este camino"]):::fin
  CYQ_825 -->|"Dividendo cobrado o caducado"| FIN_CYQ_825_1
  CYQ_830 -->|"Clausura dispuesta"| CYQ_835
  EXT_CYQ_990_destino["CYQ_990 Archivo del expediente<br/>(ver Honorarios y cierre)"]:::externo
  CYQ_835 -->|"Pasaron 2 años sin reapertura"| EXT_CYQ_990_destino
  CYQ_835 -->|"Reapertura por bienes nuevos"| CYQ_800
  CYQ_840 -->|"Clausura firme"| EXT_CYQ_990_destino
  CYQ_840 -->|"Reapertura por bienes nuevos"| CYQ_800
  CYQ_850 -->|"Conclusión declarada"| EXT_CYQ_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 12. Honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    CYQ_900["<b>CYQ_900</b> Regulación de honorarios del concurso o la quiebra<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
    CYQ_905["<b>CYQ_905</b> Apelación de honorarios<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    CYQ_910["<b>CYQ_910</b> Pago de aportes de la Ley 6716<br/>Responsable: Cualquier interesado<br/>60 días corridos"]:::ambas
    CYQ_990["<b>CYQ_990</b> Archivo del expediente<br/>Responsable: Juzgado o síndico<br/>Sin plazo"]:::tribunal
  end
  EXT_CYQ_105_origen["CYQ_105 Ratificación por el órgano de gobierno<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_105_origen -.->|"No se acredita: cese del procedimiento"| CYQ_990
  EXT_CYQ_125_origen["CYQ_125 Apelación del rechazo de la apertura<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_125_origen -.->|"Rechazo firme"| CYQ_990
  EXT_CYQ_130_origen["CYQ_130 Publicación de edictos del concurso<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_130_origen -.->|"No se publican en término: desistimiento"| CYQ_990
  EXT_CYQ_140_origen["CYQ_140 Presentación de libros y depósito de gastos de correspondencia<br/>(ver Concurso preventivo: presentación y apertura)"]:::externo
  EXT_CYQ_140_origen -.->|"No se deposita en término: desistimiento"| CYQ_990
  EXT_CYQ_460_origen["CYQ_460 Homologación del acuerdo<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_460_origen -.->|"Acuerdo homologado"| CYQ_900
  EXT_CYQ_480_origen["CYQ_480 Conclusión del concurso y cumplimiento del acuerdo<br/>(ver Homologación, cumplimiento y salvataje (art. 48))"]:::externo
  EXT_CYQ_480_origen -.->|"Acuerdo cumplido y declarado"| CYQ_990
  EXT_CYQ_630_origen["CYQ_630 Resolución sobre la homologación del APE<br/>(ver Acuerdo preventivo extrajudicial)"]:::externo
  EXT_CYQ_630_origen -.->|"APE homologado"| CYQ_900
  EXT_CYQ_705_origen["CYQ_705 Citación al deudor (art. 84)<br/>(ver Quiebra: pedido y sentencia)"]:::externo
  EXT_CYQ_705_origen -.->|"Pedido rechazado o desistido"| CYQ_990
  EXT_CYQ_735_origen["CYQ_735 Reposición o levantamiento sin trámite de la quiebra<br/>(ver Quiebra: efectos de la sentencia)"]:::externo
  EXT_CYQ_735_origen -.->|"Quiebra revocada o levantada"| CYQ_990
  EXT_CYQ_810_origen["CYQ_810 Informe final y proyecto de distribución<br/>(ver Quiebra: liquidación, distribución y conclusión)"]:::externo
  EXT_CYQ_810_origen -.->|"Informe presentado y edictos publicados"| CYQ_900
  EXT_CYQ_835_origen["CYQ_835 Conclusión de la quiebra después de la clausura<br/>(ver Quiebra: liquidación, distribución y conclusión)"]:::externo
  EXT_CYQ_835_origen -.->|"Pasaron 2 años sin reapertura"| CYQ_990
  EXT_CYQ_840_origen["CYQ_840 Clausura por falta de activo<br/>(ver Quiebra: liquidación, distribución y conclusión)"]:::externo
  EXT_CYQ_840_origen -.->|"Clausura firme"| CYQ_990
  EXT_CYQ_850_origen["CYQ_850 Avenimiento, pago total o carta de pago<br/>(ver Quiebra: liquidación, distribución y conclusión)"]:::externo
  EXT_CYQ_850_origen -.->|"Conclusión declarada"| CYQ_900
  CYQ_900 -->|"Regulación notificada"| CYQ_905
  CYQ_905 -->|"Regulación firme"| CYQ_910
  CYQ_910 -->|"Aportes pagados y acreditados"| CYQ_990
  style CYQ_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
