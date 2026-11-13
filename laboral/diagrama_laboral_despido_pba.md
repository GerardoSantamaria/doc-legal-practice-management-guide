# Diagrama de Flujo: Indemnización por despido - Provincia de Buenos Aires

**Régimen:** Ley 11.653 (Tribunales de Trabajo, instancia única) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_laboral_despido_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = Actora; naranja = Demandada; gris = Tribunal; violeta = Ambas partes.
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la prescripción corre mientras avanza el reclamo.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>13 hitos"]
  FASE_2["Postulación<br/>8 hitos"]
  FASE_3["Prueba<br/>6 hitos"]
  FASE_4["Vista de causa<br/>2 hitos"]
  FASE_5["Sentencia<br/>3 hitos"]
  FASE_6["Recursos<br/>4 hitos"]
  FASE_7["Ejecución<br/>4 hitos"]
  FASE_8["Acuerdo<br/>2 hitos"]
  FASE_9["Cierre<br/>1 hito"]
  FASE_1 --> FASE_9
  FASE_1 --> FASE_8
  FASE_1 --> FASE_2
  FASE_2 --> FASE_9
  FASE_2 --> FASE_3
  FASE_2 --> FASE_6
  FASE_3 --> FASE_4
  FASE_3 --> FASE_5
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_6
  FASE_6 --> FASE_7
  FASE_6 --> FASE_9
  FASE_6 --> FASE_5
  FASE_7 --> FASE_9
  FASE_8 --> FASE_9
  FASE_8 --> FASE_7
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    DSP_010["INICIO - <b>DSP_010</b> Extinción del vínculo o injuria laboral<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_012["<b>DSP_012</b> Rechazo de la causa invocada<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_013["<b>DSP_013</b> Respuesta a la intimación a retomar tareas<br/>Responsable: Actora<br/>48 horas"]:::actora
    DSP_015["<b>DSP_015</b> Control de prescripción de la acción<br/>Responsable: Actora<br/>2 años"]:::actora
    DSP_016["<b>DSP_016</b> Entrega de certificados de trabajo<br/>Responsable: Demandada<br/>30 días corridos"]:::demandada
    DSP_017["<b>DSP_017</b> Intimación de entrega de certificados<br/>Responsable: Demandada<br/>2 días hábiles administrativos"]:::demandada
    DSP_020["<b>DSP_020</b> Pago de la liquidación final e indemnizaciones<br/>Responsable: Demandada<br/>4 días hábiles administrativos"]:::demandada
    DSP_025["<b>DSP_025</b> Intimación de registración<br/>Responsable: Demandada<br/>30 días corridos"]:::demandada
    DSP_026["<b>DSP_026</b> Copia de la intimación a ARCA<br/>Responsable: Actora<br/>1 días hábiles administrativos"]:::actora
    DSP_030["<b>DSP_030</b> Intimación telegráfica del trabajador<br/>Responsable: Demandada<br/>2 días hábiles administrativos"]:::demandada
    DSP_032["<b>DSP_032</b> Intimación de pago de las indemnizaciones<br/>Responsable: Demandada<br/>2 días hábiles administrativos"]:::demandada
    DSP_035["<b>DSP_035</b> Comunicación del despido indirecto<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_040["<b>DSP_040</b> Instancia de conciliación laboral previa<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  P_DSP_010_1(["Se abren en paralelo"]):::paralelo
  DSP_010 -->|"Despido directo sin causa"| P_DSP_010_1
  P_DSP_010_1 --> DSP_015
  P_DSP_010_1 --> DSP_016
  P_DSP_010_1 --> DSP_020
  P_DSP_010_2(["Se abren en paralelo"]):::paralelo
  DSP_010 -->|"Despido con causa invocada"| P_DSP_010_2
  P_DSP_010_2 --> DSP_012
  P_DSP_010_2 --> DSP_015
  P_DSP_010_2 --> DSP_016
  P_DSP_010_2 --> DSP_020
  DSP_010 -->|"Intimación del empleador a retomar tareas (art. 244 LCT)"| DSP_013
  P_DSP_010_4(["Se abren en paralelo"]):::paralelo
  DSP_010 -->|"Trabajo no registrado o mal registrado, con el vínculo vigente"| P_DSP_010_4
  P_DSP_010_4 --> DSP_025
  P_DSP_010_4 --> DSP_026
  DSP_010 -->|"Otra injuria del empleador con el vínculo vigente"| DSP_030
  FIN_DSP_012_1(["Fin de este camino"]):::fin
  DSP_012 -->|"Causa rechazada por TCL"| FIN_DSP_012_1
  EXT_DSP_990_destino["DSP_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_013 -->|"Se reintegra o justifica la ausencia y no hay reclamo"| EXT_DSP_990_destino
  P_DSP_013_2(["Se abren en paralelo"]):::paralelo
  DSP_013 -->|"El empleador comunica el despido por abandono de trabajo"| P_DSP_013_2
  P_DSP_013_2 --> DSP_012
  P_DSP_013_2 --> DSP_015
  P_DSP_013_2 --> DSP_016
  P_DSP_013_2 --> DSP_020
  DSP_013 -->|"La intimación encubre una injuria (por ejemplo, negativa de tareas)"| DSP_030
  FIN_DSP_015_1(["Fin de este camino"]):::fin
  DSP_015 -->|"Demanda interpuesta en término"| FIN_DSP_015_1
  FIN_DSP_016_1(["Fin de este camino"]):::fin
  DSP_016 -->|"Certificados entregados"| FIN_DSP_016_1
  DSP_016 -->|"No entregados en 30 días"| DSP_017
  FIN_DSP_017_1(["Fin de este camino"]):::fin
  DSP_017 -->|"Certificados entregados"| FIN_DSP_017_1
  FIN_DSP_017_2(["Fin de este camino"]):::fin
  DSP_017 -->|"No entregados: se reclaman en la demanda"| FIN_DSP_017_2
  DSP_020 -->|"Pago íntegro, sin reclamo pendiente"| EXT_DSP_990_destino
  DSP_020 -->|"Falta de pago o pago insuficiente"| DSP_032
  DSP_025 -->|"El empleador registra correctamente"| EXT_DSP_990_destino
  DSP_025 -->|"Rechazo, silencio o registración incompleta"| DSP_035
  FIN_DSP_026_1(["Fin de este camino"]):::fin
  DSP_026 -->|"Copia remitida o plazo vencido"| FIN_DSP_026_1
  DSP_030 -->|"El empleador regulariza o cesa la injuria"| EXT_DSP_990_destino
  DSP_030 -->|"Rechazo o silencio"| DSP_035
  DSP_032 -->|"Paga lo intimado"| EXT_DSP_990_destino
  DSP_032 -->|"No paga o paga de menos"| DSP_040
  P_DSP_035_1(["Se abren en paralelo"]):::paralelo
  DSP_035 -->|"Despido indirecto comunicado"| P_DSP_035_1
  P_DSP_035_1 --> DSP_015
  P_DSP_035_1 --> DSP_016
  P_DSP_035_1 --> DSP_032
  EXT_DSP_900_destino["DSP_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_040 -->|"Acuerdo alcanzado"| EXT_DSP_900_destino
  EXT_DSP_050_destino["DSP_050 Interposición de la demanda<br/>(ver Demanda y contestación)"]:::externo
  DSP_040 -->|"Fracaso de la conciliación o instancia no exigida"| EXT_DSP_050_destino
  style DSP_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Demanda y contestación

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    DSP_050["<b>DSP_050</b> Interposición de la demanda<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_060["<b>DSP_060</b> Radicación y traslado de la demanda<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_065["<b>DSP_065</b> Subsanación de defectos de la demanda<br/>Responsable: Actora<br/>3 días hábiles judiciales + gracia"]:::actora
    DSP_070["<b>DSP_070</b> Contestación de la demanda<br/>Responsable: Demandada<br/>10 días hábiles judiciales + gracia"]:::demandada
    DSP_075["<b>DSP_075</b> Demanda no contestada<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_080["<b>DSP_080</b> Traslado al actor de la contestación, documental y excepciones<br/>Responsable: Actora<br/>5 días hábiles judiciales + gracia"]:::actora
    DSP_085["<b>DSP_085</b> Contestación de la reconvención<br/>Responsable: Actora<br/>10 días hábiles judiciales + gracia"]:::actora
    DSP_090["<b>DSP_090</b> Resolución de excepciones de previo pronunciamiento<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_DSP_040_origen["DSP_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_040_origen -.->|"Fracaso de la conciliación o instancia no exigida"| DSP_050
  DSP_050 -->|"Demanda interpuesta"| DSP_060
  DSP_060 -->|"Se ordena subsanar defectos"| DSP_065
  DSP_060 -->|"Se ordena el traslado de la demanda"| DSP_070
  DSP_065 -->|"Defectos subsanados en término"| DSP_070
  EXT_DSP_990_destino["DSP_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_065 -->|"No subsanados: se tiene por no presentada"| EXT_DSP_990_destino
  DSP_070 -->|"Contesta la demanda (con o sin excepciones)"| DSP_080
  P_DSP_070_2(["Se abren en paralelo"]):::paralelo
  DSP_070 -->|"Contesta y reconviene"| P_DSP_070_2
  P_DSP_070_2 --> DSP_080
  P_DSP_070_2 --> DSP_085
  DSP_070 -->|"No contesta en término"| DSP_075
  EXT_DSP_100_destino["DSP_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  DSP_075 -->|"Se tiene por no contestada la demanda"| EXT_DSP_100_destino
  DSP_080 -->|"Hay excepciones de previo y especial pronunciamiento"| DSP_090
  DSP_080 -->|"Sin excepciones de previo pronunciamiento"| EXT_DSP_100_destino
  FIN_DSP_085_1(["Fin de este camino"]):::fin
  DSP_085 -->|"Reconvención contestada o plazo vencido"| FIN_DSP_085_1
  DSP_090 -->|"Excepciones rechazadas"| EXT_DSP_100_destino
  EXT_DSP_700_destino["DSP_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  DSP_090 -->|"Excepción admitida que pone fin al proceso"| EXT_DSP_700_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Prueba y audiencia de vista de causa

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    DSP_100["<b>DSP_100</b> Auto de apertura a prueba<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_105["<b>DSP_105</b> Reposición contra la denegatoria de prueba<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DSP_110["<b>DSP_110</b> Producción de la prueba pericial<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    DSP_115["<b>DSP_115</b> Traslado del dictamen pericial<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DSP_117["<b>DSP_117</b> Respuesta del perito a las observaciones<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_120["<b>DSP_120</b> Producción de la prueba informativa<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    DSP_200["<b>DSP_200</b> Fijación de la audiencia de vista de causa<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_210["<b>DSP_210</b> Audiencia de vista de causa<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_DSP_075_origen["DSP_075 Demanda no contestada<br/>(ver Demanda y contestación)"]:::externo
  EXT_DSP_075_origen -.->|"Se tiene por no contestada la demanda"| DSP_100
  EXT_DSP_080_origen["DSP_080 Traslado al actor de la contestación, documental y excepciones<br/>(ver Demanda y contestación)"]:::externo
  EXT_DSP_080_origen -.->|"Sin excepciones de previo pronunciamiento"| DSP_100
  EXT_DSP_090_origen["DSP_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_DSP_090_origen -.->|"Excepciones rechazadas"| DSP_100
  P_DSP_100_1(["Se abren en paralelo"]):::paralelo
  DSP_100 -->|"Se provee toda la prueba ofrecida"| P_DSP_100_1
  P_DSP_100_1 --> DSP_110
  P_DSP_100_1 --> DSP_120
  P_DSP_100_1 --> DSP_200
  P_DSP_100_2(["Se abren en paralelo"]):::paralelo
  DSP_100 -->|"Se deniega parte de la prueba ofrecida"| P_DSP_100_2
  P_DSP_100_2 --> DSP_105
  P_DSP_100_2 --> DSP_110
  P_DSP_100_2 --> DSP_120
  P_DSP_100_2 --> DSP_200
  EXT_DSP_600_destino["DSP_600 Veredicto y sentencia<br/>(ver Sentencia y recursos)"]:::externo
  DSP_100 -->|"Causa declarada de puro derecho"| EXT_DSP_600_destino
  FIN_DSP_105_1(["Fin de este camino"]):::fin
  DSP_105 -->|"Reposición resuelta o plazo vencido"| FIN_DSP_105_1
  DSP_110 -->|"Dictamen pericial presentado"| DSP_115
  FIN_DSP_110_2(["Fin de este camino"]):::fin
  DSP_110 -->|"No se ofreció pericial o fue desistida"| FIN_DSP_110_2
  DSP_115 -->|"Se impugna o se piden explicaciones"| DSP_117
  FIN_DSP_115_2(["Fin de este camino"]):::fin
  DSP_115 -->|"Sin observaciones"| FIN_DSP_115_2
  FIN_DSP_117_1(["Fin de este camino"]):::fin
  DSP_117 -->|"El perito contesta las observaciones"| FIN_DSP_117_1
  FIN_DSP_120_1(["Fin de este camino"]):::fin
  DSP_120 -->|"Informes contestados o prueba desistida"| FIN_DSP_120_1
  DSP_200 -->|"Audiencia de vista de causa fijada"| DSP_210
  DSP_210 -->|"Audiencia realizada; causa en estado de veredicto"| EXT_DSP_600_destino
  DSP_210 -->|"Audiencia suspendida o reprogramada"| DSP_200
  EXT_DSP_900_destino["DSP_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_210 -->|"Acuerdo conciliatorio en la audiencia"| EXT_DSP_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Sentencia y recursos

```mermaid
flowchart TD
  subgraph F_0["Sentencia"]
    DSP_600["<b>DSP_600</b> Veredicto y sentencia<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_610["<b>DSP_610</b> Aclaratoria<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DSP_850["<b>DSP_850</b> Impugnación de la regulación de honorarios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    DSP_700["<b>DSP_700</b> Recurso extraordinario ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    DSP_710["<b>DSP_710</b> Concesión del recurso<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    DSP_720["<b>DSP_720</b> Queja por recurso denegado<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DSP_730["<b>DSP_730</b> Trámite y resolución ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DSP_090_origen["DSP_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_DSP_090_origen -.->|"Excepción admitida que pone fin al proceso"| DSP_700
  EXT_DSP_100_origen["DSP_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_DSP_100_origen -.->|"Causa declarada de puro derecho"| DSP_600
  EXT_DSP_210_origen["DSP_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_DSP_210_origen -.->|"Audiencia realizada; causa en estado de veredicto"| DSP_600
  P_DSP_600_1(["Se abren en paralelo"]):::paralelo
  DSP_600 -->|"Veredicto y sentencia notificados"| P_DSP_600_1
  P_DSP_600_1 --> DSP_610
  P_DSP_600_1 --> DSP_700
  P_DSP_600_1 --> DSP_850
  FIN_DSP_610_1(["Fin de este camino"]):::fin
  DSP_610 -->|"Aclaratoria resuelta o plazo vencido"| FIN_DSP_610_1
  EXT_DSP_800_destino["DSP_800 Liquidación de la condena<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_700 -->|"No se recurre: sentencia firme con condena"| EXT_DSP_800_destino
  EXT_DSP_990_destino["DSP_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  DSP_700 -->|"No se recurre: sentencia firme sin condena a pagar"| EXT_DSP_990_destino
  DSP_700 -->|"Se interpone recurso extraordinario"| DSP_710
  DSP_710 -->|"Recurso concedido"| DSP_730
  DSP_710 -->|"Recurso denegado"| DSP_720
  DSP_720 -->|"Queja admitida"| DSP_730
  DSP_720 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_DSP_800_destino
  DSP_730 -->|"La SCBA resuelve: sentencia firme con condena"| EXT_DSP_800_destino
  DSP_730 -->|"La SCBA resuelve: sin condena a pagar"| EXT_DSP_990_destino
  DSP_730 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| DSP_600
  FIN_DSP_850_1(["Fin de este camino"]):::fin
  DSP_850 -->|"Regulación firme o impugnación resuelta"| FIN_DSP_850_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Ejecución, acuerdo y cierre

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    DSP_800["<b>DSP_800</b> Liquidación de la condena<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DSP_810["<b>DSP_810</b> Depósito de la condena<br/>Responsable: Demandada<br/>10 días hábiles judiciales"]:::demandada
    DSP_820["<b>DSP_820</b> Ejecución de la sentencia<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    DSP_830["<b>DSP_830</b> Cobro y rendición al cliente<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    DSP_900["<b>DSP_900</b> Acuerdo conciliatorio y homologación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    DSP_910["<b>DSP_910</b> Cumplimiento del acuerdo<br/>Responsable: Demandada<br/>Sin plazo"]:::demandada
  end
  subgraph F_2["Cierre"]
    DSP_990["<b>DSP_990</b> Archivo del expediente<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  EXT_DSP_013_origen["DSP_013 Respuesta a la intimación a retomar tareas<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_013_origen -.->|"Se reintegra o justifica la ausencia y no hay reclamo"| DSP_990
  EXT_DSP_020_origen["DSP_020 Pago de la liquidación final e indemnizaciones<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_020_origen -.->|"Pago íntegro, sin reclamo pendiente"| DSP_990
  EXT_DSP_025_origen["DSP_025 Intimación de registración<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_025_origen -.->|"El empleador registra correctamente"| DSP_990
  EXT_DSP_030_origen["DSP_030 Intimación telegráfica del trabajador<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_030_origen -.->|"El empleador regulariza o cesa la injuria"| DSP_990
  EXT_DSP_032_origen["DSP_032 Intimación de pago de las indemnizaciones<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_032_origen -.->|"Paga lo intimado"| DSP_990
  EXT_DSP_040_origen["DSP_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_DSP_040_origen -.->|"Acuerdo alcanzado"| DSP_900
  EXT_DSP_065_origen["DSP_065 Subsanación de defectos de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DSP_065_origen -.->|"No subsanados: se tiene por no presentada"| DSP_990
  EXT_DSP_210_origen["DSP_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_DSP_210_origen -.->|"Acuerdo conciliatorio en la audiencia"| DSP_900
  EXT_DSP_700_origen["DSP_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DSP_700_origen -.->|"No se recurre: sentencia firme con condena"| DSP_800
  EXT_DSP_700_origen -.->|"No se recurre: sentencia firme sin condena a pagar"| DSP_990
  EXT_DSP_720_origen["DSP_720 Queja por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DSP_720_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| DSP_800
  EXT_DSP_730_origen["DSP_730 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DSP_730_origen -.->|"La SCBA resuelve: sentencia firme con condena"| DSP_800
  EXT_DSP_730_origen -.->|"La SCBA resuelve: sin condena a pagar"| DSP_990
  DSP_800 -->|"Liquidación aprobada"| DSP_810
  DSP_810 -->|"Depósito en término"| DSP_830
  DSP_810 -->|"Falta de depósito"| DSP_820
  DSP_820 -->|"Fondos embargados o depositados"| DSP_830
  DSP_830 -->|"Cobro percibido y rendido al cliente"| DSP_990
  DSP_900 -->|"Acuerdo homologado"| DSP_910
  DSP_910 -->|"Acuerdo cumplido"| DSP_990
  DSP_910 -->|"Acuerdo incumplido"| DSP_820
  style DSP_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
