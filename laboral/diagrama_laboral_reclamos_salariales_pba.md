# Diagrama de Flujo: Reclamos salariales - Provincia de Buenos Aires

**Régimen:** Ley 11.653 (Tribunales de Trabajo, instancia única) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_laboral_reclamos_salariales_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

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
  FASE_1["Previa<br/>7 hitos"]
  FASE_2["Postulación<br/>8 hitos"]
  FASE_3["Prueba<br/>6 hitos"]
  FASE_4["Vista de causa<br/>2 hitos"]
  FASE_5["Sentencia<br/>3 hitos"]
  FASE_6["Recursos<br/>4 hitos"]
  FASE_7["Ejecución<br/>4 hitos"]
  FASE_8["Acuerdo<br/>2 hitos"]
  FASE_9["Cierre<br/>2 hitos"]
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
    SAL_010["INICIO - <b>SAL_010</b> Crédito salarial impago o pagado de menos<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    SAL_012["<b>SAL_012</b> Pago de la remuneración del período<br/>Responsable: Demandada<br/>4 días hábiles administrativos"]:::demandada
    SAL_013["<b>SAL_013</b> Impugnación de la sanción disciplinaria<br/>Responsable: Actora<br/>30 días corridos"]:::actora
    SAL_015["<b>SAL_015</b> Control de prescripción del crédito más antiguo<br/>Responsable: Actora<br/>2 años"]:::actora
    SAL_017["<b>SAL_017</b> Acreditación del depósito de aportes retenidos<br/>Responsable: Demandada<br/>30 días corridos"]:::demandada
    SAL_020["<b>SAL_020</b> Intimación de pago de las diferencias<br/>Responsable: Demandada<br/>2 días hábiles administrativos"]:::demandada
    SAL_040["<b>SAL_040</b> Instancia de conciliación laboral previa<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  SAL_010 -->|"Sueldo del período todavía no vencido"| SAL_012
  P_SAL_010_2(["Se abren en paralelo"]):::paralelo
  SAL_010 -->|"Diferencias o rubros adeudados ya exigibles"| P_SAL_010_2
  P_SAL_010_2 --> SAL_015
  P_SAL_010_2 --> SAL_020
  SAL_010 -->|"Sanción disciplinaria con descuento o suspensión"| SAL_013
  P_SAL_010_4(["Se abren en paralelo"]):::paralelo
  SAL_010 -->|"Aportes retenidos y no depositados"| P_SAL_010_4
  P_SAL_010_4 --> SAL_015
  P_SAL_010_4 --> SAL_017
  P_SAL_010_4 --> SAL_020
  EXT_SAL_990_destino["SAL_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_012 -->|"Pagado íntegramente"| EXT_SAL_990_destino
  P_SAL_012_2(["Se abren en paralelo"]):::paralelo
  SAL_012 -->|"No pagado o pagado de menos"| P_SAL_012_2
  P_SAL_012_2 --> SAL_015
  P_SAL_012_2 --> SAL_020
  P_SAL_013_1(["Se abren en paralelo"]):::paralelo
  SAL_013 -->|"Sanción impugnada en término"| P_SAL_013_1
  P_SAL_013_1 --> SAL_015
  P_SAL_013_1 --> SAL_020
  SAL_013 -->|"Sanción consentida"| EXT_SAL_990_destino
  FIN_SAL_015_1(["Fin de este camino"]):::fin
  SAL_015 -->|"Reclamo interpuesto en término"| FIN_SAL_015_1
  FIN_SAL_017_1(["Fin de este camino"]):::fin
  SAL_017 -->|"Acredita el depósito"| FIN_SAL_017_1
  FIN_SAL_017_2(["Fin de este camino"]):::fin
  SAL_017 -->|"No lo acredita: la sanción se reclama en la demanda"| FIN_SAL_017_2
  SAL_020 -->|"El empleador paga lo reclamado"| EXT_SAL_990_destino
  SAL_020 -->|"Rechazo o silencio: se reclama con el vínculo vigente o ya extinguido"| SAL_040
  EXT_SAL_995_destino["SAL_995 Despido indirecto: continúa en la matriz de despido<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_020 -->|"Rechazo o silencio: el trabajador se considera despedido"| EXT_SAL_995_destino
  EXT_SAL_900_destino["SAL_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_040 -->|"Acuerdo alcanzado"| EXT_SAL_900_destino
  EXT_SAL_050_destino["SAL_050 Interposición de la demanda<br/>(ver Demanda y contestación)"]:::externo
  SAL_040 -->|"Fracaso de la conciliación o instancia no exigida"| EXT_SAL_050_destino
  style SAL_010 stroke-width:3px
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
    SAL_050["<b>SAL_050</b> Interposición de la demanda<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    SAL_060["<b>SAL_060</b> Radicación y traslado de la demanda<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_065["<b>SAL_065</b> Subsanación de defectos de la demanda<br/>Responsable: Actora<br/>3 días hábiles judiciales + gracia"]:::actora
    SAL_070["<b>SAL_070</b> Contestación de la demanda<br/>Responsable: Demandada<br/>10 días hábiles judiciales + gracia"]:::demandada
    SAL_075["<b>SAL_075</b> Demanda no contestada<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    SAL_080["<b>SAL_080</b> Traslado al actor de la contestación, documental y excepciones<br/>Responsable: Actora<br/>5 días hábiles judiciales + gracia"]:::actora
    SAL_085["<b>SAL_085</b> Contestación de la reconvención<br/>Responsable: Actora<br/>10 días hábiles judiciales + gracia"]:::actora
    SAL_090["<b>SAL_090</b> Resolución de excepciones de previo pronunciamiento<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_SAL_040_origen["SAL_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_SAL_040_origen -.->|"Fracaso de la conciliación o instancia no exigida"| SAL_050
  SAL_050 -->|"Demanda interpuesta"| SAL_060
  SAL_060 -->|"Se ordena subsanar defectos"| SAL_065
  SAL_060 -->|"Se ordena el traslado de la demanda"| SAL_070
  SAL_065 -->|"Defectos subsanados en término"| SAL_070
  EXT_SAL_990_destino["SAL_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_065 -->|"No subsanados: se tiene por no presentada"| EXT_SAL_990_destino
  SAL_070 -->|"Contesta la demanda (con o sin excepciones)"| SAL_080
  P_SAL_070_2(["Se abren en paralelo"]):::paralelo
  SAL_070 -->|"Contesta y reconviene"| P_SAL_070_2
  P_SAL_070_2 --> SAL_080
  P_SAL_070_2 --> SAL_085
  SAL_070 -->|"No contesta en término"| SAL_075
  EXT_SAL_100_destino["SAL_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  SAL_075 -->|"Se tiene por no contestada la demanda"| EXT_SAL_100_destino
  SAL_080 -->|"Hay excepciones de previo y especial pronunciamiento"| SAL_090
  SAL_080 -->|"Sin excepciones de previo pronunciamiento"| EXT_SAL_100_destino
  FIN_SAL_085_1(["Fin de este camino"]):::fin
  SAL_085 -->|"Reconvención contestada o plazo vencido"| FIN_SAL_085_1
  SAL_090 -->|"Excepciones rechazadas"| EXT_SAL_100_destino
  EXT_SAL_700_destino["SAL_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  SAL_090 -->|"Excepción admitida que pone fin al proceso"| EXT_SAL_700_destino
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
    SAL_100["<b>SAL_100</b> Auto de apertura a prueba<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_105["<b>SAL_105</b> Reposición contra la denegatoria de prueba<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    SAL_110["<b>SAL_110</b> Producción de la prueba pericial<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    SAL_115["<b>SAL_115</b> Traslado del dictamen pericial<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    SAL_117["<b>SAL_117</b> Respuesta del perito a las observaciones<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_120["<b>SAL_120</b> Producción de la prueba informativa<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    SAL_200["<b>SAL_200</b> Fijación de la audiencia de vista de causa<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_210["<b>SAL_210</b> Audiencia de vista de causa<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_SAL_075_origen["SAL_075 Demanda no contestada<br/>(ver Demanda y contestación)"]:::externo
  EXT_SAL_075_origen -.->|"Se tiene por no contestada la demanda"| SAL_100
  EXT_SAL_080_origen["SAL_080 Traslado al actor de la contestación, documental y excepciones<br/>(ver Demanda y contestación)"]:::externo
  EXT_SAL_080_origen -.->|"Sin excepciones de previo pronunciamiento"| SAL_100
  EXT_SAL_090_origen["SAL_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_SAL_090_origen -.->|"Excepciones rechazadas"| SAL_100
  P_SAL_100_1(["Se abren en paralelo"]):::paralelo
  SAL_100 -->|"Se provee toda la prueba ofrecida"| P_SAL_100_1
  P_SAL_100_1 --> SAL_110
  P_SAL_100_1 --> SAL_120
  P_SAL_100_1 --> SAL_200
  P_SAL_100_2(["Se abren en paralelo"]):::paralelo
  SAL_100 -->|"Se deniega parte de la prueba ofrecida"| P_SAL_100_2
  P_SAL_100_2 --> SAL_105
  P_SAL_100_2 --> SAL_110
  P_SAL_100_2 --> SAL_120
  P_SAL_100_2 --> SAL_200
  EXT_SAL_600_destino["SAL_600 Veredicto y sentencia<br/>(ver Sentencia y recursos)"]:::externo
  SAL_100 -->|"Causa declarada de puro derecho"| EXT_SAL_600_destino
  FIN_SAL_105_1(["Fin de este camino"]):::fin
  SAL_105 -->|"Reposición resuelta o plazo vencido"| FIN_SAL_105_1
  SAL_110 -->|"Dictamen pericial presentado"| SAL_115
  FIN_SAL_110_2(["Fin de este camino"]):::fin
  SAL_110 -->|"No se ofreció pericial o fue desistida"| FIN_SAL_110_2
  SAL_115 -->|"Se impugna o se piden explicaciones"| SAL_117
  FIN_SAL_115_2(["Fin de este camino"]):::fin
  SAL_115 -->|"Sin observaciones"| FIN_SAL_115_2
  FIN_SAL_117_1(["Fin de este camino"]):::fin
  SAL_117 -->|"El perito contesta las observaciones"| FIN_SAL_117_1
  FIN_SAL_120_1(["Fin de este camino"]):::fin
  SAL_120 -->|"Informes contestados o prueba desistida"| FIN_SAL_120_1
  SAL_200 -->|"Audiencia de vista de causa fijada"| SAL_210
  SAL_210 -->|"Audiencia realizada; causa en estado de veredicto"| EXT_SAL_600_destino
  SAL_210 -->|"Audiencia suspendida o reprogramada"| SAL_200
  EXT_SAL_900_destino["SAL_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_210 -->|"Acuerdo conciliatorio en la audiencia"| EXT_SAL_900_destino
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
    SAL_600["<b>SAL_600</b> Veredicto y sentencia<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_610["<b>SAL_610</b> Aclaratoria<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    SAL_850["<b>SAL_850</b> Impugnación de la regulación de honorarios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    SAL_700["<b>SAL_700</b> Recurso extraordinario ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    SAL_710["<b>SAL_710</b> Concesión del recurso<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    SAL_720["<b>SAL_720</b> Queja por recurso denegado<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    SAL_730["<b>SAL_730</b> Trámite y resolución ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_SAL_090_origen["SAL_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_SAL_090_origen -.->|"Excepción admitida que pone fin al proceso"| SAL_700
  EXT_SAL_100_origen["SAL_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_SAL_100_origen -.->|"Causa declarada de puro derecho"| SAL_600
  EXT_SAL_210_origen["SAL_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_SAL_210_origen -.->|"Audiencia realizada; causa en estado de veredicto"| SAL_600
  P_SAL_600_1(["Se abren en paralelo"]):::paralelo
  SAL_600 -->|"Veredicto y sentencia notificados"| P_SAL_600_1
  P_SAL_600_1 --> SAL_610
  P_SAL_600_1 --> SAL_700
  P_SAL_600_1 --> SAL_850
  FIN_SAL_610_1(["Fin de este camino"]):::fin
  SAL_610 -->|"Aclaratoria resuelta o plazo vencido"| FIN_SAL_610_1
  EXT_SAL_800_destino["SAL_800 Liquidación de la condena<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_700 -->|"No se recurre: sentencia firme con condena"| EXT_SAL_800_destino
  EXT_SAL_990_destino["SAL_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  SAL_700 -->|"No se recurre: sentencia firme sin condena a pagar"| EXT_SAL_990_destino
  SAL_700 -->|"Se interpone recurso extraordinario"| SAL_710
  SAL_710 -->|"Recurso concedido"| SAL_730
  SAL_710 -->|"Recurso denegado"| SAL_720
  SAL_720 -->|"Queja admitida"| SAL_730
  SAL_720 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_SAL_800_destino
  SAL_730 -->|"La SCBA resuelve: sentencia firme con condena"| EXT_SAL_800_destino
  SAL_730 -->|"La SCBA resuelve: sin condena a pagar"| EXT_SAL_990_destino
  SAL_730 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| SAL_600
  FIN_SAL_850_1(["Fin de este camino"]):::fin
  SAL_850 -->|"Regulación firme o impugnación resuelta"| FIN_SAL_850_1
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
    SAL_800["<b>SAL_800</b> Liquidación de la condena<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    SAL_810["<b>SAL_810</b> Depósito de la condena<br/>Responsable: Demandada<br/>10 días hábiles judiciales"]:::demandada
    SAL_820["<b>SAL_820</b> Ejecución de la sentencia<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    SAL_830["<b>SAL_830</b> Cobro y rendición al cliente<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    SAL_900["<b>SAL_900</b> Acuerdo conciliatorio y homologación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    SAL_910["<b>SAL_910</b> Cumplimiento del acuerdo<br/>Responsable: Demandada<br/>Sin plazo"]:::demandada
  end
  subgraph F_2["Cierre"]
    SAL_990["<b>SAL_990</b> Archivo del expediente<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    SAL_995["<b>SAL_995</b> Despido indirecto: continúa en la matriz de despido<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  EXT_SAL_012_origen["SAL_012 Pago de la remuneración del período<br/>(ver Etapa previa)"]:::externo
  EXT_SAL_012_origen -.->|"Pagado íntegramente"| SAL_990
  EXT_SAL_013_origen["SAL_013 Impugnación de la sanción disciplinaria<br/>(ver Etapa previa)"]:::externo
  EXT_SAL_013_origen -.->|"Sanción consentida"| SAL_990
  EXT_SAL_020_origen["SAL_020 Intimación de pago de las diferencias<br/>(ver Etapa previa)"]:::externo
  EXT_SAL_020_origen -.->|"El empleador paga lo reclamado"| SAL_990
  EXT_SAL_020_origen -.->|"Rechazo o silencio: el trabajador se considera despedido"| SAL_995
  EXT_SAL_040_origen["SAL_040 Instancia de conciliación laboral previa<br/>(ver Etapa previa)"]:::externo
  EXT_SAL_040_origen -.->|"Acuerdo alcanzado"| SAL_900
  EXT_SAL_065_origen["SAL_065 Subsanación de defectos de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_SAL_065_origen -.->|"No subsanados: se tiene por no presentada"| SAL_990
  EXT_SAL_210_origen["SAL_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_SAL_210_origen -.->|"Acuerdo conciliatorio en la audiencia"| SAL_900
  EXT_SAL_700_origen["SAL_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_SAL_700_origen -.->|"No se recurre: sentencia firme con condena"| SAL_800
  EXT_SAL_700_origen -.->|"No se recurre: sentencia firme sin condena a pagar"| SAL_990
  EXT_SAL_720_origen["SAL_720 Queja por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_SAL_720_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| SAL_800
  EXT_SAL_730_origen["SAL_730 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_SAL_730_origen -.->|"La SCBA resuelve: sentencia firme con condena"| SAL_800
  EXT_SAL_730_origen -.->|"La SCBA resuelve: sin condena a pagar"| SAL_990
  SAL_800 -->|"Liquidación aprobada"| SAL_810
  SAL_810 -->|"Depósito en término"| SAL_830
  SAL_810 -->|"Falta de depósito"| SAL_820
  SAL_820 -->|"Fondos embargados o depositados"| SAL_830
  SAL_830 -->|"Cobro percibido y rendido al cliente"| SAL_990
  SAL_900 -->|"Acuerdo homologado"| SAL_910
  SAL_910 -->|"Acuerdo cumplido"| SAL_990
  SAL_910 -->|"Acuerdo incumplido"| SAL_820
  style SAL_990 stroke-width:3px
  style SAL_995 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
