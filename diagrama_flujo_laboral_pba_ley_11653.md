# Diagrama de Flujo: Proceso laboral ordinario - Provincia de Buenos Aires

**Régimen:** Ley 11.653 (Tribunales de Trabajo, instancia única) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_flujo_laboral_pba_ley_11653.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = Actora; naranja = Demandada; gris = Tribunal; violeta = Ambas partes.
* **Borde punteado:** el tipo de plazo todavía no está soportado por el motor (días hábiles de la LCT, años, fecha fijada).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la prescripción corre mientras avanza el reclamo.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>8 hitos"]
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
    LAB_010["INICIO - <b>LAB_010</b> Extinción del vínculo o injuria laboral<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    LAB_015["<b>LAB_015</b> Control de prescripción de la acción<br/>Responsable: Actora<br/>2 años - tipo pendiente"]:::actora
    LAB_016["<b>LAB_016</b> Entrega de certificados de trabajo<br/>Responsable: Demandada<br/>30 días corridos"]:::demandada
    LAB_017["<b>LAB_017</b> Intimación de entrega de certificados<br/>Responsable: Demandada<br/>2 días hábiles (LCT) - tipo pendiente"]:::demandada
    LAB_020["<b>LAB_020</b> Pago de la liquidación final e indemnizaciones<br/>Responsable: Demandada<br/>4 días hábiles (LCT) - tipo pendiente"]:::demandada
    LAB_030["<b>LAB_030</b> Intimación telegráfica del trabajador<br/>Responsable: Demandada<br/>2 días hábiles (LCT) - tipo pendiente"]:::demandada
    LAB_035["<b>LAB_035</b> Comunicación del despido indirecto<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    LAB_040["<b>LAB_040</b> Instancia de conciliación laboral previa<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  P_LAB_010_1(["Se abren en paralelo"]):::paralelo
  LAB_010 -->|"Despido directo comunicado por el empleador"| P_LAB_010_1
  P_LAB_010_1 --> LAB_015
  P_LAB_010_1 --> LAB_016
  P_LAB_010_1 --> LAB_020
  LAB_010 -->|"Injuria del empleador con el vínculo vigente"| LAB_030
  FIN_LAB_015_1(["Fin de este camino"]):::fin
  LAB_015 -->|"Demanda interpuesta en término"| FIN_LAB_015_1
  FIN_LAB_016_1(["Fin de este camino"]):::fin
  LAB_016 -->|"Certificados entregados"| FIN_LAB_016_1
  LAB_016 -->|"No entregados en 30 días"| LAB_017
  FIN_LAB_017_1(["Fin de este camino"]):::fin
  LAB_017 -->|"Certificados entregados"| FIN_LAB_017_1
  FIN_LAB_017_2(["Fin de este camino"]):::fin
  LAB_017 -->|"No entregados: se reclaman en la demanda"| FIN_LAB_017_2
  EXT_LAB_990_destino["LAB_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_020 -->|"Pago íntegro, sin reclamo pendiente"| EXT_LAB_990_destino
  LAB_020 -->|"Falta de pago o pago insuficiente"| LAB_030
  LAB_030 -->|"El empleador regulariza o paga"| EXT_LAB_990_destino
  LAB_030 -->|"Rechazo o silencio con el vínculo vigente"| LAB_035
  LAB_030 -->|"Rechazo o silencio con el vínculo ya extinguido"| LAB_040
  P_LAB_035_1(["Se abren en paralelo"]):::paralelo
  LAB_035 -->|"Despido indirecto comunicado"| P_LAB_035_1
  P_LAB_035_1 --> LAB_015
  P_LAB_035_1 --> LAB_016
  P_LAB_035_1 --> LAB_040
  EXT_LAB_900_destino["LAB_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_040 -->|"Acuerdo alcanzado"| EXT_LAB_900_destino
  EXT_LAB_050_destino["LAB_050 Interposición de la demanda<br/>(ver Demanda y contestación)"]:::externo
  LAB_040 -->|"Fracaso de la conciliación o instancia no exigida"| EXT_LAB_050_destino
  style LAB_010 stroke-width:3px
  style LAB_015 stroke-dasharray:6 4
  style LAB_017 stroke-dasharray:6 4
  style LAB_020 stroke-dasharray:6 4
  style LAB_030 stroke-dasharray:6 4
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
    LAB_050["<b>LAB_050</b> Interposición de la demanda<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    LAB_060["<b>LAB_060</b> Radicación y traslado de la demanda<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_065["<b>LAB_065</b> Subsanación de defectos de la demanda<br/>Responsable: Actora<br/>3 días hábiles judiciales + gracia"]:::actora
    LAB_070["<b>LAB_070</b> Contestación de la demanda<br/>Responsable: Demandada<br/>10 días hábiles judiciales + gracia"]:::demandada
    LAB_075["<b>LAB_075</b> Demanda no contestada<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    LAB_080["<b>LAB_080</b> Traslado al actor de la contestación, documental y excepciones<br/>Responsable: Actora<br/>5 días hábiles judiciales + gracia"]:::actora
    LAB_085["<b>LAB_085</b> Contestación de la reconvención<br/>Responsable: Actora<br/>10 días hábiles judiciales + gracia"]:::actora
    LAB_090["<b>LAB_090</b> Resolución de excepciones de previo pronunciamiento<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_LAB_040_origen["LAB_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_LAB_040_origen -.->|"Fracaso de la conciliación o instancia no exigida"| LAB_050
  LAB_050 -->|"Demanda interpuesta"| LAB_060
  LAB_060 -->|"Se ordena subsanar defectos"| LAB_065
  LAB_060 -->|"Se ordena el traslado de la demanda"| LAB_070
  LAB_065 -->|"Defectos subsanados en término"| LAB_070
  EXT_LAB_990_destino["LAB_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_065 -->|"No subsanados: se tiene por no presentada"| EXT_LAB_990_destino
  LAB_070 -->|"Contesta la demanda (con o sin excepciones)"| LAB_080
  P_LAB_070_2(["Se abren en paralelo"]):::paralelo
  LAB_070 -->|"Contesta y reconviene"| P_LAB_070_2
  P_LAB_070_2 --> LAB_080
  P_LAB_070_2 --> LAB_085
  LAB_070 -->|"No contesta en término"| LAB_075
  EXT_LAB_100_destino["LAB_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  LAB_075 -->|"Se tiene por no contestada la demanda"| EXT_LAB_100_destino
  LAB_080 -->|"Hay excepciones de previo y especial pronunciamiento"| LAB_090
  LAB_080 -->|"Sin excepciones de previo pronunciamiento"| EXT_LAB_100_destino
  FIN_LAB_085_1(["Fin de este camino"]):::fin
  LAB_085 -->|"Reconvención contestada o plazo vencido"| FIN_LAB_085_1
  LAB_090 -->|"Excepciones rechazadas"| EXT_LAB_100_destino
  EXT_LAB_700_destino["LAB_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  LAB_090 -->|"Excepción admitida que pone fin al proceso"| EXT_LAB_700_destino
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
    LAB_100["<b>LAB_100</b> Auto de apertura a prueba<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_105["<b>LAB_105</b> Reposición contra la denegatoria de prueba<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    LAB_110["<b>LAB_110</b> Producción de la prueba pericial<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    LAB_115["<b>LAB_115</b> Traslado del dictamen pericial<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    LAB_117["<b>LAB_117</b> Respuesta del perito a las observaciones<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_120["<b>LAB_120</b> Producción de la prueba informativa<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    LAB_200["<b>LAB_200</b> Fijación de la audiencia de vista de causa<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_210["<b>LAB_210</b> Audiencia de vista de causa<br/>Responsable: Ambas partes<br/>Fecha fijada por el tribunal - tipo pendiente"]:::ambas
  end
  EXT_LAB_075_origen["LAB_075 Demanda no contestada<br/>(ver Demanda y contestación)"]:::externo
  EXT_LAB_075_origen -.->|"Se tiene por no contestada la demanda"| LAB_100
  EXT_LAB_080_origen["LAB_080 Traslado al actor de la contestación, documental y excepciones<br/>(ver Demanda y contestación)"]:::externo
  EXT_LAB_080_origen -.->|"Sin excepciones de previo pronunciamiento"| LAB_100
  EXT_LAB_090_origen["LAB_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_LAB_090_origen -.->|"Excepciones rechazadas"| LAB_100
  P_LAB_100_1(["Se abren en paralelo"]):::paralelo
  LAB_100 -->|"Se provee toda la prueba ofrecida"| P_LAB_100_1
  P_LAB_100_1 --> LAB_110
  P_LAB_100_1 --> LAB_120
  P_LAB_100_1 --> LAB_200
  P_LAB_100_2(["Se abren en paralelo"]):::paralelo
  LAB_100 -->|"Se deniega parte de la prueba ofrecida"| P_LAB_100_2
  P_LAB_100_2 --> LAB_105
  P_LAB_100_2 --> LAB_110
  P_LAB_100_2 --> LAB_120
  P_LAB_100_2 --> LAB_200
  EXT_LAB_600_destino["LAB_600 Veredicto y sentencia<br/>(ver Sentencia y recursos)"]:::externo
  LAB_100 -->|"Causa declarada de puro derecho"| EXT_LAB_600_destino
  FIN_LAB_105_1(["Fin de este camino"]):::fin
  LAB_105 -->|"Reposición resuelta o plazo vencido"| FIN_LAB_105_1
  LAB_110 -->|"Dictamen pericial presentado"| LAB_115
  FIN_LAB_110_2(["Fin de este camino"]):::fin
  LAB_110 -->|"No se ofreció pericial o fue desistida"| FIN_LAB_110_2
  LAB_115 -->|"Se impugna o se piden explicaciones"| LAB_117
  FIN_LAB_115_2(["Fin de este camino"]):::fin
  LAB_115 -->|"Sin observaciones"| FIN_LAB_115_2
  FIN_LAB_117_1(["Fin de este camino"]):::fin
  LAB_117 -->|"El perito contesta las observaciones"| FIN_LAB_117_1
  FIN_LAB_120_1(["Fin de este camino"]):::fin
  LAB_120 -->|"Informes contestados o prueba desistida"| FIN_LAB_120_1
  LAB_200 -->|"Audiencia de vista de causa fijada"| LAB_210
  LAB_210 -->|"Audiencia realizada; causa en estado de veredicto"| EXT_LAB_600_destino
  LAB_210 -->|"Audiencia suspendida o reprogramada"| LAB_200
  EXT_LAB_900_destino["LAB_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_210 -->|"Acuerdo conciliatorio en la audiencia"| EXT_LAB_900_destino
  style LAB_210 stroke-dasharray:6 4
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
    LAB_600["<b>LAB_600</b> Veredicto y sentencia<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_610["<b>LAB_610</b> Aclaratoria<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    LAB_850["<b>LAB_850</b> Impugnación de la regulación de honorarios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    LAB_700["<b>LAB_700</b> Recurso extraordinario ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    LAB_710["<b>LAB_710</b> Concesión del recurso<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    LAB_720["<b>LAB_720</b> Queja por recurso denegado<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    LAB_730["<b>LAB_730</b> Trámite y resolución ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_LAB_090_origen["LAB_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_LAB_090_origen -.->|"Excepción admitida que pone fin al proceso"| LAB_700
  EXT_LAB_100_origen["LAB_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_LAB_100_origen -.->|"Causa declarada de puro derecho"| LAB_600
  EXT_LAB_210_origen["LAB_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_LAB_210_origen -.->|"Audiencia realizada; causa en estado de veredicto"| LAB_600
  P_LAB_600_1(["Se abren en paralelo"]):::paralelo
  LAB_600 -->|"Veredicto y sentencia notificados"| P_LAB_600_1
  P_LAB_600_1 --> LAB_610
  P_LAB_600_1 --> LAB_700
  P_LAB_600_1 --> LAB_850
  FIN_LAB_610_1(["Fin de este camino"]):::fin
  LAB_610 -->|"Aclaratoria resuelta o plazo vencido"| FIN_LAB_610_1
  EXT_LAB_800_destino["LAB_800 Liquidación de la condena<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_700 -->|"No se recurre: sentencia firme con condena"| EXT_LAB_800_destino
  EXT_LAB_990_destino["LAB_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  LAB_700 -->|"No se recurre: sentencia firme sin condena a pagar"| EXT_LAB_990_destino
  LAB_700 -->|"Se interpone recurso extraordinario"| LAB_710
  LAB_710 -->|"Recurso concedido"| LAB_730
  LAB_710 -->|"Recurso denegado"| LAB_720
  LAB_720 -->|"Queja admitida"| LAB_730
  LAB_720 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_LAB_800_destino
  LAB_730 -->|"La SCBA resuelve: sentencia firme con condena"| EXT_LAB_800_destino
  LAB_730 -->|"La SCBA resuelve: sin condena a pagar"| EXT_LAB_990_destino
  LAB_730 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| LAB_600
  FIN_LAB_850_1(["Fin de este camino"]):::fin
  LAB_850 -->|"Regulación firme o impugnación resuelta"| FIN_LAB_850_1
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
    LAB_800["<b>LAB_800</b> Liquidación de la condena<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    LAB_810["<b>LAB_810</b> Depósito de la condena<br/>Responsable: Demandada<br/>10 días hábiles judiciales"]:::demandada
    LAB_820["<b>LAB_820</b> Ejecución de la sentencia<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    LAB_830["<b>LAB_830</b> Cobro y rendición al cliente<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    LAB_900["<b>LAB_900</b> Acuerdo conciliatorio y homologación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    LAB_910["<b>LAB_910</b> Cumplimiento del acuerdo<br/>Responsable: Demandada<br/>Sin plazo"]:::demandada
  end
  subgraph F_2["Cierre"]
    LAB_990["<b>LAB_990</b> Archivo del expediente<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  EXT_LAB_020_origen["LAB_020 Pago de la liquidación final e indemnizaciones<br/>(ver Etapa previa)"]:::externo
  EXT_LAB_020_origen -.->|"Pago íntegro, sin reclamo pendiente"| LAB_990
  EXT_LAB_030_origen["LAB_030 Intimación telegráfica del trabajador<br/>(ver Etapa previa)"]:::externo
  EXT_LAB_030_origen -.->|"El empleador regulariza o paga"| LAB_990
  EXT_LAB_040_origen["LAB_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_LAB_040_origen -.->|"Acuerdo alcanzado"| LAB_900
  EXT_LAB_065_origen["LAB_065 Subsanación de defectos de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_LAB_065_origen -.->|"No subsanados: se tiene por no presentada"| LAB_990
  EXT_LAB_210_origen["LAB_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_LAB_210_origen -.->|"Acuerdo conciliatorio en la audiencia"| LAB_900
  EXT_LAB_700_origen["LAB_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_LAB_700_origen -.->|"No se recurre: sentencia firme con condena"| LAB_800
  EXT_LAB_700_origen -.->|"No se recurre: sentencia firme sin condena a pagar"| LAB_990
  EXT_LAB_720_origen["LAB_720 Queja por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_LAB_720_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| LAB_800
  EXT_LAB_730_origen["LAB_730 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_LAB_730_origen -.->|"La SCBA resuelve: sentencia firme con condena"| LAB_800
  EXT_LAB_730_origen -.->|"La SCBA resuelve: sin condena a pagar"| LAB_990
  LAB_800 -->|"Liquidación aprobada"| LAB_810
  LAB_810 -->|"Depósito en término"| LAB_830
  LAB_810 -->|"Falta de depósito"| LAB_820
  LAB_820 -->|"Fondos embargados o depositados"| LAB_830
  LAB_830 -->|"Cobro percibido y rendido al cliente"| LAB_990
  LAB_900 -->|"Acuerdo homologado"| LAB_910
  LAB_910 -->|"Acuerdo cumplido"| LAB_990
  LAB_910 -->|"Acuerdo incumplido"| LAB_820
  style LAB_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
