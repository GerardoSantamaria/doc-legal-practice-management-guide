# Diagrama de Flujo: Accidentes de trabajo y enfermedades profesionales - Provincia de Buenos Aires

**Régimen:** Ley 11.653 (Tribunales de Trabajo, instancia única) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_laboral_accidentes_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

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

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    ACC_010["INICIO - <b>ACC_010</b> Accidente de trabajo o primera manifestación de la enfermedad profesional<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_015["<b>ACC_015</b> Control de prescripción de la acción<br/>Responsable: Actora<br/>2 años"]:::actora
    ACC_017["<b>ACC_017</b> Reclamo al empleador no asegurado<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_020["<b>ACC_020</b> Denuncia del siniestro a la ART<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_022["<b>ACC_022</b> Aceptación o rechazo del siniestro por la ART<br/>Responsable: Demandada<br/>10 días corridos"]:::demandada
    ACC_025["<b>ACC_025</b> Prestaciones médicas e incapacidad laboral temporaria<br/>Responsable: Demandada<br/>Sin plazo"]:::demandada
  end
  P_ACC_010_1(["Se abren en paralelo"]):::paralelo
  ACC_010 -->|"Empleador con ART y trabajador registrado"| P_ACC_010_1
  P_ACC_010_1 --> ACC_015
  P_ACC_010_1 --> ACC_020
  P_ACC_010_2(["Se abren en paralelo"]):::paralelo
  ACC_010 -->|"Empleador sin ART o trabajador no registrado"| P_ACC_010_2
  P_ACC_010_2 --> ACC_015
  P_ACC_010_2 --> ACC_017
  FIN_ACC_015_1(["Fin de este camino"]):::fin
  ACC_015 -->|"Acción interpuesta en término"| FIN_ACC_015_1
  EXT_ACC_900_destino["ACC_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_017 -->|"Acuerdo con el empleador"| EXT_ACC_900_destino
  EXT_ACC_050_destino["ACC_050 Demanda ante el Tribunal de Trabajo<br/>(ver Demanda y contestación)"]:::externo
  ACC_017 -->|"Sin acuerdo: se demanda"| EXT_ACC_050_destino
  ACC_020 -->|"Denuncia recibida por la ART"| ACC_022
  ACC_022 -->|"Aceptado o sin respuesta en término"| ACC_025
  EXT_ACC_030_destino["ACC_030 Inicio del trámite ante la Comisión Médica Jurisdiccional<br/>(ver Comisión médica)"]:::externo
  ACC_022 -->|"Rechazado por la ART"| EXT_ACC_030_destino
  EXT_ACC_990_destino["ACC_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_025 -->|"Alta sin secuelas, aceptada por el trabajador"| EXT_ACC_990_destino
  ACC_025 -->|"Alta con secuelas o divergencia con el alta"| EXT_ACC_030_destino
  EXT_ACC_040_destino["ACC_040 Pago de la indemnización por la ART<br/>(ver Comisión médica)"]:::externo
  ACC_025 -->|"Fallecimiento del trabajador"| EXT_ACC_040_destino
  style ACC_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Comisión médica

```mermaid
flowchart TD
  subgraph F_0["Comisión médica"]
    ACC_030["<b>ACC_030</b> Inicio del trámite ante la Comisión Médica Jurisdiccional<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_032["<b>ACC_032</b> Audiencia médica ante la Comisión Médica<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    ACC_035["<b>ACC_035</b> Plazo de la Comisión Médica para expedirse<br/>Responsable: Tribunal<br/>60 días hábiles administrativos"]:::tribunal
    ACC_036["<b>ACC_036</b> Dictamen de la Comisión Médica<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_038["<b>ACC_038</b> Acuerdo y homologación ante el Servicio de Homologación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    ACC_040["<b>ACC_040</b> Pago de la indemnización por la ART<br/>Responsable: Demandada<br/>15 días corridos"]:::demandada
    ACC_045["<b>ACC_045</b> Recurso o acción contra el dictamen<br/>Responsable: Actora<br/>15 días hábiles administrativos"]:::actora
    ACC_047["<b>ACC_047</b> Recurso ante la Comisión Médica Central<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_ACC_022_origen["ACC_022 Aceptación o rechazo del siniestro por la ART<br/>(ver Etapa previa)"]:::externo
  EXT_ACC_022_origen -.->|"Rechazado por la ART"| ACC_030
  EXT_ACC_025_origen["ACC_025 Prestaciones médicas e incapacidad laboral temporaria<br/>(ver Etapa previa)"]:::externo
  EXT_ACC_025_origen -.->|"Alta con secuelas o divergencia con el alta"| ACC_030
  EXT_ACC_025_origen -.->|"Fallecimiento del trabajador"| ACC_040
  P_ACC_030_1(["Se abren en paralelo"]):::paralelo
  ACC_030 -->|"Trámite iniciado"| P_ACC_030_1
  P_ACC_030_1 --> ACC_032
  P_ACC_030_1 --> ACC_035
  ACC_032 -->|"Audiencia realizada"| ACC_036
  FIN_ACC_035_1(["Fin de este camino"]):::fin
  ACC_035 -->|"Dictamen emitido en término"| FIN_ACC_035_1
  ACC_035 -->|"Vencido sin dictamen"| ACC_045
  ACC_036 -->|"Se acepta el dictamen"| ACC_038
  ACC_036 -->|"No se acepta el dictamen"| ACC_045
  EXT_ACC_995_destino["ACC_995 Opción por la acción civil contra el empleador<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_036 -->|"Se opta por la acción civil"| EXT_ACC_995_destino
  ACC_038 -->|"Acuerdo homologado"| ACC_040
  ACC_038 -->|"Sin acuerdo"| ACC_045
  EXT_ACC_990_destino["ACC_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_040 -->|"Pago en término"| EXT_ACC_990_destino
  EXT_ACC_050_destino["ACC_050 Demanda ante el Tribunal de Trabajo<br/>(ver Demanda y contestación)"]:::externo
  ACC_040 -->|"Falta de pago o pago insuficiente"| EXT_ACC_050_destino
  ACC_045 -->|"Recurso ante la Comisión Médica Central"| ACC_047
  ACC_045 -->|"Acción ante el Tribunal de Trabajo"| EXT_ACC_050_destino
  ACC_045 -->|"No se recurre: el dictamen queda firme"| ACC_040
  ACC_047 -->|"Resolución aceptada"| ACC_040
  ACC_047 -->|"Resolución apelada ante la justicia"| EXT_ACC_050_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Demanda y contestación

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    ACC_050["<b>ACC_050</b> Demanda ante el Tribunal de Trabajo<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_060["<b>ACC_060</b> Radicación y traslado de la demanda<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_065["<b>ACC_065</b> Subsanación de defectos de la demanda<br/>Responsable: Actora<br/>3 días hábiles judiciales + gracia"]:::actora
    ACC_070["<b>ACC_070</b> Contestación de la demanda<br/>Responsable: Demandada<br/>10 días hábiles judiciales + gracia"]:::demandada
    ACC_075["<b>ACC_075</b> Demanda no contestada<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_080["<b>ACC_080</b> Traslado al actor de la contestación, documental y excepciones<br/>Responsable: Actora<br/>5 días hábiles judiciales + gracia"]:::actora
    ACC_085["<b>ACC_085</b> Contestación de la reconvención<br/>Responsable: Actora<br/>10 días hábiles judiciales + gracia"]:::actora
    ACC_090["<b>ACC_090</b> Resolución de excepciones de previo pronunciamiento<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_ACC_017_origen["ACC_017 Reclamo al empleador no asegurado<br/>(ver Etapa previa)"]:::externo
  EXT_ACC_017_origen -.->|"Sin acuerdo: se demanda"| ACC_050
  EXT_ACC_040_origen["ACC_040 Pago de la indemnización por la ART<br/>(ver Comisión médica)"]:::externo
  EXT_ACC_040_origen -.->|"Falta de pago o pago insuficiente"| ACC_050
  EXT_ACC_045_origen["ACC_045 Recurso o acción contra el dictamen<br/>(ver Comisión médica)"]:::externo
  EXT_ACC_045_origen -.->|"Acción ante el Tribunal de Trabajo"| ACC_050
  EXT_ACC_047_origen["ACC_047 Recurso ante la Comisión Médica Central<br/>(ver Comisión médica)"]:::externo
  EXT_ACC_047_origen -.->|"Resolución apelada ante la justicia"| ACC_050
  ACC_050 -->|"Demanda interpuesta"| ACC_060
  ACC_060 -->|"Se ordena subsanar defectos"| ACC_065
  ACC_060 -->|"Se ordena el traslado de la demanda"| ACC_070
  ACC_065 -->|"Defectos subsanados en término"| ACC_070
  EXT_ACC_990_destino["ACC_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_065 -->|"No subsanados: se tiene por no presentada"| EXT_ACC_990_destino
  ACC_070 -->|"Contesta la demanda (con o sin excepciones)"| ACC_080
  P_ACC_070_2(["Se abren en paralelo"]):::paralelo
  ACC_070 -->|"Contesta y reconviene"| P_ACC_070_2
  P_ACC_070_2 --> ACC_080
  P_ACC_070_2 --> ACC_085
  ACC_070 -->|"No contesta en término"| ACC_075
  EXT_ACC_100_destino["ACC_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  ACC_075 -->|"Se tiene por no contestada la demanda"| EXT_ACC_100_destino
  ACC_080 -->|"Hay excepciones de previo y especial pronunciamiento"| ACC_090
  ACC_080 -->|"Sin excepciones de previo pronunciamiento"| EXT_ACC_100_destino
  FIN_ACC_085_1(["Fin de este camino"]):::fin
  ACC_085 -->|"Reconvención contestada o plazo vencido"| FIN_ACC_085_1
  ACC_090 -->|"Excepciones rechazadas"| EXT_ACC_100_destino
  EXT_ACC_700_destino["ACC_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  ACC_090 -->|"Excepción admitida que pone fin al proceso"| EXT_ACC_700_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Prueba y audiencia de vista de causa

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    ACC_100["<b>ACC_100</b> Auto de apertura a prueba<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_105["<b>ACC_105</b> Reposición contra la denegatoria de prueba<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    ACC_110["<b>ACC_110</b> Producción de la prueba pericial<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    ACC_115["<b>ACC_115</b> Traslado del dictamen pericial<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ACC_117["<b>ACC_117</b> Respuesta del perito a las observaciones<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_120["<b>ACC_120</b> Producción de la prueba informativa<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    ACC_200["<b>ACC_200</b> Fijación de la audiencia de vista de causa<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_210["<b>ACC_210</b> Audiencia de vista de causa<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_ACC_075_origen["ACC_075 Demanda no contestada<br/>(ver Demanda y contestación)"]:::externo
  EXT_ACC_075_origen -.->|"Se tiene por no contestada la demanda"| ACC_100
  EXT_ACC_080_origen["ACC_080 Traslado al actor de la contestación, documental y excepciones<br/>(ver Demanda y contestación)"]:::externo
  EXT_ACC_080_origen -.->|"Sin excepciones de previo pronunciamiento"| ACC_100
  EXT_ACC_090_origen["ACC_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_ACC_090_origen -.->|"Excepciones rechazadas"| ACC_100
  P_ACC_100_1(["Se abren en paralelo"]):::paralelo
  ACC_100 -->|"Se provee toda la prueba ofrecida"| P_ACC_100_1
  P_ACC_100_1 --> ACC_110
  P_ACC_100_1 --> ACC_120
  P_ACC_100_1 --> ACC_200
  P_ACC_100_2(["Se abren en paralelo"]):::paralelo
  ACC_100 -->|"Se deniega parte de la prueba ofrecida"| P_ACC_100_2
  P_ACC_100_2 --> ACC_105
  P_ACC_100_2 --> ACC_110
  P_ACC_100_2 --> ACC_120
  P_ACC_100_2 --> ACC_200
  EXT_ACC_600_destino["ACC_600 Veredicto y sentencia<br/>(ver Sentencia y recursos)"]:::externo
  ACC_100 -->|"Causa declarada de puro derecho"| EXT_ACC_600_destino
  FIN_ACC_105_1(["Fin de este camino"]):::fin
  ACC_105 -->|"Reposición resuelta o plazo vencido"| FIN_ACC_105_1
  ACC_110 -->|"Dictamen pericial presentado"| ACC_115
  FIN_ACC_110_2(["Fin de este camino"]):::fin
  ACC_110 -->|"No se ofreció pericial o fue desistida"| FIN_ACC_110_2
  ACC_115 -->|"Se impugna o se piden explicaciones"| ACC_117
  FIN_ACC_115_2(["Fin de este camino"]):::fin
  ACC_115 -->|"Sin observaciones"| FIN_ACC_115_2
  FIN_ACC_117_1(["Fin de este camino"]):::fin
  ACC_117 -->|"El perito contesta las observaciones"| FIN_ACC_117_1
  FIN_ACC_120_1(["Fin de este camino"]):::fin
  ACC_120 -->|"Informes contestados o prueba desistida"| FIN_ACC_120_1
  ACC_200 -->|"Audiencia de vista de causa fijada"| ACC_210
  ACC_210 -->|"Audiencia realizada; causa en estado de veredicto"| EXT_ACC_600_destino
  ACC_210 -->|"Audiencia suspendida o reprogramada"| ACC_200
  EXT_ACC_900_destino["ACC_900 Acuerdo conciliatorio y homologación<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_210 -->|"Acuerdo conciliatorio en la audiencia"| EXT_ACC_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Sentencia y recursos

```mermaid
flowchart TD
  subgraph F_0["Sentencia"]
    ACC_600["<b>ACC_600</b> Veredicto y sentencia<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_610["<b>ACC_610</b> Aclaratoria<br/>Responsable: Ambas partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    ACC_850["<b>ACC_850</b> Impugnación de la regulación de honorarios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    ACC_700["<b>ACC_700</b> Recurso extraordinario ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    ACC_710["<b>ACC_710</b> Concesión del recurso<br/>Responsable: Tribunal<br/>Sin plazo"]:::tribunal
    ACC_720["<b>ACC_720</b> Queja por recurso denegado<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ACC_730["<b>ACC_730</b> Trámite y resolución ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_ACC_090_origen["ACC_090 Resolución de excepciones de previo pronunciamiento<br/>(ver Demanda y contestación)"]:::externo
  EXT_ACC_090_origen -.->|"Excepción admitida que pone fin al proceso"| ACC_700
  EXT_ACC_100_origen["ACC_100 Auto de apertura a prueba<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_ACC_100_origen -.->|"Causa declarada de puro derecho"| ACC_600
  EXT_ACC_210_origen["ACC_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_ACC_210_origen -.->|"Audiencia realizada; causa en estado de veredicto"| ACC_600
  P_ACC_600_1(["Se abren en paralelo"]):::paralelo
  ACC_600 -->|"Veredicto y sentencia notificados"| P_ACC_600_1
  P_ACC_600_1 --> ACC_610
  P_ACC_600_1 --> ACC_700
  P_ACC_600_1 --> ACC_850
  FIN_ACC_610_1(["Fin de este camino"]):::fin
  ACC_610 -->|"Aclaratoria resuelta o plazo vencido"| FIN_ACC_610_1
  EXT_ACC_800_destino["ACC_800 Liquidación de la condena<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_700 -->|"No se recurre: sentencia firme con condena"| EXT_ACC_800_destino
  EXT_ACC_990_destino["ACC_990 Archivo del expediente<br/>(ver Ejecución, acuerdo y cierre)"]:::externo
  ACC_700 -->|"No se recurre: sentencia firme sin condena a pagar"| EXT_ACC_990_destino
  ACC_700 -->|"Se interpone recurso extraordinario"| ACC_710
  ACC_710 -->|"Recurso concedido"| ACC_730
  ACC_710 -->|"Recurso denegado"| ACC_720
  ACC_720 -->|"Queja admitida"| ACC_730
  ACC_720 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_ACC_800_destino
  ACC_730 -->|"La SCBA resuelve: sentencia firme con condena"| EXT_ACC_800_destino
  ACC_730 -->|"La SCBA resuelve: sin condena a pagar"| EXT_ACC_990_destino
  ACC_730 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| ACC_600
  FIN_ACC_850_1(["Fin de este camino"]):::fin
  ACC_850 -->|"Regulación firme o impugnación resuelta"| FIN_ACC_850_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Ejecución, acuerdo y cierre

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    ACC_800["<b>ACC_800</b> Liquidación de la condena<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ACC_810["<b>ACC_810</b> Depósito de la condena<br/>Responsable: Demandada<br/>10 días hábiles judiciales"]:::demandada
    ACC_820["<b>ACC_820</b> Ejecución de la sentencia<br/>Responsable: Actora<br/>Sin plazo"]:::actora
    ACC_830["<b>ACC_830</b> Cobro y rendición al cliente<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    ACC_900["<b>ACC_900</b> Acuerdo conciliatorio y homologación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    ACC_910["<b>ACC_910</b> Cumplimiento del acuerdo<br/>Responsable: Demandada<br/>Sin plazo"]:::demandada
  end
  subgraph F_2["Cierre"]
    ACC_990["<b>ACC_990</b> Archivo del expediente<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
    ACC_995["<b>ACC_995</b> Opción por la acción civil contra el empleador<br/>Responsable: Actora<br/>Sin plazo"]:::actora
  end
  EXT_ACC_017_origen["ACC_017 Reclamo al empleador no asegurado<br/>(ver Etapa previa)"]:::externo
  EXT_ACC_017_origen -.->|"Acuerdo con el empleador"| ACC_900
  EXT_ACC_025_origen["ACC_025 Prestaciones médicas e incapacidad laboral temporaria<br/>(ver Etapa previa)"]:::externo
  EXT_ACC_025_origen -.->|"Alta sin secuelas, aceptada por el trabajador"| ACC_990
  EXT_ACC_036_origen["ACC_036 Dictamen de la Comisión Médica<br/>(ver Comisión médica)"]:::externo
  EXT_ACC_036_origen -.->|"Se opta por la acción civil"| ACC_995
  EXT_ACC_040_origen["ACC_040 Pago de la indemnización por la ART<br/>(ver Comisión médica)"]:::externo
  EXT_ACC_040_origen -.->|"Pago en término"| ACC_990
  EXT_ACC_065_origen["ACC_065 Subsanación de defectos de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_ACC_065_origen -.->|"No subsanados: se tiene por no presentada"| ACC_990
  EXT_ACC_210_origen["ACC_210 Audiencia de vista de causa<br/>(ver Prueba y audiencia de vista de causa)"]:::externo
  EXT_ACC_210_origen -.->|"Acuerdo conciliatorio en la audiencia"| ACC_900
  EXT_ACC_700_origen["ACC_700 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ACC_700_origen -.->|"No se recurre: sentencia firme con condena"| ACC_800
  EXT_ACC_700_origen -.->|"No se recurre: sentencia firme sin condena a pagar"| ACC_990
  EXT_ACC_720_origen["ACC_720 Queja por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ACC_720_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| ACC_800
  EXT_ACC_730_origen["ACC_730 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ACC_730_origen -.->|"La SCBA resuelve: sentencia firme con condena"| ACC_800
  EXT_ACC_730_origen -.->|"La SCBA resuelve: sin condena a pagar"| ACC_990
  ACC_800 -->|"Liquidación aprobada"| ACC_810
  ACC_810 -->|"Depósito en término"| ACC_830
  ACC_810 -->|"Falta de depósito"| ACC_820
  ACC_820 -->|"Fondos embargados o depositados"| ACC_830
  ACC_830 -->|"Cobro percibido y rendido al cliente"| ACC_990
  ACC_900 -->|"Acuerdo homologado"| ACC_910
  ACC_910 -->|"Acuerdo cumplido"| ACC_990
  ACC_910 -->|"Acuerdo incumplido"| ACC_820
  style ACC_990 stroke-width:3px
  style ACC_995 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
