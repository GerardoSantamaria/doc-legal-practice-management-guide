# Diagrama de Flujo: Cuidado personal y régimen de comunicación (PBA)

**Régimen:** CPCCBA (Decreto-Ley 7425/68), Libro VIII: proceso ante los Juzgados de Familia (arts. 827 a 853, texto de las Leyes 13.634 y 15.513); CCyC, arts. 555 a 557, 643, 645, 648 a 657, 706, 707, 716 y 2642; Ley 14.568 (abogado del niño) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_familia_cuidado_personal_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el progenitor o pariente que promueve (ACTORA); naranja = el otro progenitor o quien tiene el cuidado (DEMANDADA); gris = juzgado, Consejero, equipo técnico, Asesoría de Incapaces o abogado del niño, aclarado en el nombre (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, cuando hay urgencia, corren a la vez las medidas provisorias y la etapa previa ante el Consejero.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un registro). La app los separa en el flujo prejudicial.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>2 hitos"]
  FASE_2["Medidas provisorias<br/>2 hitos"]
  FASE_3["Consejero de Familia<br/>3 hitos"]
  FASE_4["Postulación<br/>6 hitos"]
  FASE_5["Audiencia preliminar<br/>1 hito"]
  FASE_6["Prueba<br/>8 hitos"]
  FASE_7["Vista de causa<br/>2 hitos"]
  FASE_8["Sentencia<br/>3 hitos"]
  FASE_9["Recursos<br/>6 hitos"]
  FASE_10["Ejecución<br/>1 hito"]
  FASE_11["Incumplimiento y modificación<br/>3 hitos"]
  FASE_12["Situaciones especiales<br/>3 hitos"]
  FASE_13["Acuerdo<br/>4 hitos"]
  FASE_14["Cierre<br/>2 hitos"]
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_14
  FASE_1 --> FASE_12
  FASE_1 --> FASE_11
  FASE_1 --> FASE_13
  FASE_3 --> FASE_4
  FASE_3 --> FASE_13
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_13
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_5 --> FASE_14
  FASE_6 --> FASE_7
  FASE_6 --> FASE_13
  FASE_7 --> FASE_6
  FASE_7 --> FASE_13
  FASE_7 --> FASE_8
  FASE_8 --> FASE_9
  FASE_9 --> FASE_10
  FASE_10 --> FASE_14
  FASE_10 --> FASE_11
  FASE_11 --> FASE_13
  FASE_11 --> FASE_10
  FASE_11 --> FASE_3
  FASE_12 --> FASE_9
  FASE_12 --> FASE_14
  FASE_13 --> FASE_4
  FASE_13 --> FASE_6
  FASE_13 --> FASE_14
  FASE_13 --> FASE_11
```

## 1. Etapa previa (antes de promover)

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    CUI_010["INICIO - <b>CUI_010</b> Consulta sobre el cuidado o la comunicación con el hijo<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_030["<b>CUI_030</b> Plan de parentalidad acordado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  CUI_010 -->|"Los progenitores acuerdan un plan de parentalidad"| CUI_030
  EXT_CUI_100_destino["CUI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  CUI_010 -->|"Sin acuerdo sobre el cuidado o la comunicación"| EXT_CUI_100_destino
  P_CUI_010_3(["Se abren en paralelo"]):::paralelo
  CUI_010 -->|"Urgencia: hay que fijar ya el cuidado o la comunicación"| P_CUI_010_3
  EXT_CUI_050_destino["CUI_050 Medidas provisorias sobre el cuidado y la comunicación<br/>(ver Medidas provisorias)"]:::externo
  P_CUI_010_3 --> EXT_CUI_050_destino
  P_CUI_010_3 --> EXT_CUI_100_destino
  P_CUI_010_4(["Se abren en paralelo"]):::paralelo
  CUI_010 -->|"Sin acuerdo, y además hay que reclamar alimentos para el hijo"| P_CUI_010_4
  P_CUI_010_4 --> EXT_CUI_100_destino
  EXT_CUI_970_destino["CUI_970 Sigue en la matriz de alimentos y compensación económica<br/>(ver Acuerdo y cierre)"]:::externo
  P_CUI_010_4 --> EXT_CUI_970_destino
  EXT_CUI_820_destino["CUI_820 Autorización judicial para salir del país o cambiar la residencia<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  CUI_010 -->|"Hay que autorizar un viaje al exterior o un cambio de residencia"| EXT_CUI_820_destino
  EXT_CUI_830_destino["CUI_830 Restitución internacional del niño<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  CUI_010 -->|"Traslado o retención ilícitos del hijo a través de la frontera"| EXT_CUI_830_destino
  EXT_CUI_840_destino["CUI_840 Delegación del ejercicio o guarda a un pariente (plazo de un año)<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  CUI_010 -->|"Delegación del ejercicio en un pariente"| EXT_CUI_840_destino
  EXT_CUI_720_destino["CUI_720 Incumplimiento del régimen o impedimento de contacto<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  CUI_010 -->|"Ya hay un régimen fijado y no se cumple"| EXT_CUI_720_destino
  EXT_CUI_800_destino["CUI_800 Modificación del cuidado personal o del régimen de comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  CUI_010 -->|"Ya hay un régimen fijado y cambiaron las circunstancias"| EXT_CUI_800_destino
  EXT_CUI_900_destino["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_030 -->|"Plan acordado: se pide la homologación"| EXT_CUI_900_destino
  CUI_030 -->|"No se llega a firmar el plan"| EXT_CUI_100_destino
  style CUI_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Medidas provisorias

```mermaid
flowchart TD
  subgraph F_0["Medidas provisorias"]
    CUI_050["<b>CUI_050</b> Medidas provisorias sobre el cuidado y la comunicación<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_060["<b>CUI_060</b> Vencimiento o revisión de las medidas provisorias<br/>Responsable: Quien promueve<br/>Fecha y hora fijadas por el tribunal"]:::actora
  end
  EXT_CUI_010_origen["CUI_010 Consulta sobre el cuidado o la comunicación con el hijo<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_010_origen -.->|"Urgencia: hay que fijar ya el cuidado o la comunicación"| CUI_050
  CUI_050 -->|"Medidas dictadas con fecha de vencimiento o de revisión"| CUI_060
  FIN_CUI_050_2(["Fin de este camino"]):::fin
  CUI_050 -->|"Medidas rechazadas"| FIN_CUI_050_2
  CUI_060 -->|"Medidas prorrogadas o modificadas: nueva fecha"| CUI_060
  FIN_CUI_060_2(["Fin de este camino"]):::fin
  CUI_060 -->|"Reemplazadas por la sentencia o el acuerdo, o vencidas"| FIN_CUI_060_2
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Etapa previa ante el Consejero de Familia

```mermaid
flowchart TD
  subgraph F_0["Consejero de Familia"]
    CUI_100["<b>CUI_100</b> Solicitud de trámite de la etapa previa<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_110["<b>CUI_110</b> Audiencias ante el Consejero de Familia<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CUI_120["<b>CUI_120</b> Acta de cierre de la etapa previa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_CUI_010_origen["CUI_010 Consulta sobre el cuidado o la comunicación con el hijo<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_010_origen -.->|"Sin acuerdo sobre el cuidado o la comunicación"| CUI_100
  EXT_CUI_010_origen -.->|"Urgencia: hay que fijar ya el cuidado o la comunicación"| CUI_100
  EXT_CUI_010_origen -.->|"Sin acuerdo, y además hay que reclamar alimentos para el hijo"| CUI_100
  EXT_CUI_030_origen["CUI_030 Plan de parentalidad acordado<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_030_origen -.->|"No se llega a firmar el plan"| CUI_100
  CUI_100 -->|"Etapa previa admitida: el Consejero cita a las partes"| CUI_110
  EXT_CUI_200_destino["CUI_200 Demanda de cuidado personal o régimen de comunicación<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  CUI_100 -->|"Asunto urgente o etapa improcedente: el juez dispone la radicación directa"| EXT_CUI_200_destino
  CUI_110 -->|"Conciliación, fracaso o intervención agotada: el Consejero labra el acta"| CUI_120
  CUI_110 -->|"Una parte pide concluir la etapa y el juez la da por concluida"| CUI_120
  CUI_110 -->|"El juez dispone continuar la etapa (hasta 15 días)"| CUI_110
  EXT_CUI_900_destino["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_120 -->|"Acuerdo"| EXT_CUI_900_destino
  CUI_120 -->|"Sin acuerdo: quedan expeditas las acciones"| EXT_CUI_200_destino
  EXT_CUI_800_origen["CUI_800 Modificación del cuidado personal o del régimen de comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  EXT_CUI_800_origen -.->|"Sin acuerdo: etapa previa ante el Consejero"| CUI_100
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Demanda, contestación y audiencia preliminar

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    CUI_200["<b>CUI_200</b> Demanda de cuidado personal o régimen de comunicación<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_220["<b>CUI_220</b> Providencia inicial y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_230["<b>CUI_230</b> Citación por edictos al demandado con domicilio desconocido<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_240["<b>CUI_240</b> Contestación de la demanda<br/>Responsable: Otro progenitor<br/>10 días hábiles judiciales + gracia"]:::demandada
    CUI_250["<b>CUI_250</b> Demanda no contestada<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_260["<b>CUI_260</b> Ampliación de la prueba del actor por hechos nuevos<br/>Responsable: Quien promueve<br/>5 días hábiles judiciales + gracia"]:::actora
  end
  subgraph F_1["Audiencia preliminar"]
    CUI_300["<b>CUI_300</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_CUI_100_origen["CUI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_CUI_100_origen -.->|"Asunto urgente o etapa improcedente: el juez dispone la radicación directa"| CUI_200
  EXT_CUI_120_origen["CUI_120 Acta de cierre de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_CUI_120_origen -.->|"Sin acuerdo: quedan expeditas las acciones"| CUI_200
  CUI_200 -->|"Demanda presentada"| CUI_220
  CUI_220 -->|"Traslado ordenado al domicilio conocido del demandado"| CUI_240
  CUI_220 -->|"Demandado con domicilio desconocido"| CUI_230
  CUI_230 -->|"Edictos publicados: comparece el demandado o se nombra al Defensor Oficial"| CUI_240
  P_CUI_240_1(["Se abren en paralelo"]):::paralelo
  CUI_240 -->|"Contesta la demanda (con o sin reconvención)"| P_CUI_240_1
  P_CUI_240_1 --> CUI_260
  P_CUI_240_1 --> CUI_300
  CUI_240 -->|"No contesta en término"| CUI_250
  EXT_CUI_490_destino["CUI_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  CUI_250 -->|"El juez dicta sentencia sin más trámite (art. 840)"| EXT_CUI_490_destino
  CUI_250 -->|"Se convoca a la audiencia preliminar"| CUI_300
  FIN_CUI_260_1(["Fin de este camino"]):::fin
  CUI_260 -->|"Prueba ampliada o plazo vencido"| FIN_CUI_260_1
  EXT_CUI_900_destino["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_300 -->|"Acuerdo en la audiencia"| EXT_CUI_900_destino
  EXT_CUI_310_destino["CUI_310 Apertura a prueba y proveído de la prueba<br/>(ver Prueba, escucha del niño y vista de causa)"]:::externo
  CUI_300 -->|"Hechos controvertidos: se abre la causa a prueba"| EXT_CUI_310_destino
  CUI_300 -->|"Cuestión de puro derecho"| EXT_CUI_490_destino
  EXT_CUI_990_destino["CUI_990 Archivo del expediente<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_300 -->|"El actor no comparece sin justa causa: se lo tiene por desistido"| EXT_CUI_990_destino
  CUI_300 -->|"Audiencia diferida por fuerza mayor (única vez)"| CUI_300
  EXT_CUI_900_origen["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  EXT_CUI_900_origen -.->|"Homologación denegada antes de la demanda"| CUI_200
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Prueba, escucha del niño y vista de causa

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    CUI_310["<b>CUI_310</b> Apertura a prueba y proveído de la prueba<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_320["<b>CUI_320</b> Reposición contra la denegatoria de prueba<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    CUI_330["<b>CUI_330</b> Equipo técnico: pericia psicológica o psiquiátrica<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_340["<b>CUI_340</b> Equipo técnico: informe socioambiental<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_350["<b>CUI_350</b> Prueba informativa (oficios)<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    CUI_360["<b>CUI_360</b> Escucha del niño, niña o adolescente por el juez<br/>Responsable: Juzgado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    CUI_370["<b>CUI_370</b> Incorporación de la prueba previa a la vista de causa<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles de anticipación"]:::ambas
    CUI_380["<b>CUI_380</b> Designación del abogado del niño<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  subgraph F_1["Vista de causa"]
    CUI_400["<b>CUI_400</b> Fijación de la audiencia de vista de causa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_410["<b>CUI_410</b> Audiencia de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_CUI_300_origen["CUI_300 Audiencia preliminar<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  EXT_CUI_300_origen -.->|"Hechos controvertidos: se abre la causa a prueba"| CUI_310
  P_CUI_310_1(["Se abren en paralelo"]):::paralelo
  CUI_310 -->|"Se provee la prueba ofrecida"| P_CUI_310_1
  P_CUI_310_1 --> CUI_330
  P_CUI_310_1 --> CUI_340
  P_CUI_310_1 --> CUI_350
  P_CUI_310_1 --> CUI_360
  P_CUI_310_1 --> CUI_400
  EXT_CUI_950_destino["CUI_950 Control de caducidad de instancia<br/>(ver Acuerdo y cierre)"]:::externo
  P_CUI_310_1 --> EXT_CUI_950_destino
  P_CUI_310_2(["Se abren en paralelo"]):::paralelo
  CUI_310 -->|"Se provee la prueba y se deniega una parte"| P_CUI_310_2
  P_CUI_310_2 --> CUI_320
  P_CUI_310_2 --> CUI_330
  P_CUI_310_2 --> CUI_340
  P_CUI_310_2 --> CUI_350
  P_CUI_310_2 --> CUI_360
  P_CUI_310_2 --> CUI_400
  P_CUI_310_2 --> EXT_CUI_950_destino
  FIN_CUI_320_1(["Fin de este camino"]):::fin
  CUI_320 -->|"Reposición resuelta o plazo vencido"| FIN_CUI_320_1
  FIN_CUI_330_1(["Fin de este camino"]):::fin
  CUI_330 -->|"Dictamen presentado, no ordenado o desistido"| FIN_CUI_330_1
  FIN_CUI_340_1(["Fin de este camino"]):::fin
  CUI_340 -->|"Informe agregado, no ordenado o desistido"| FIN_CUI_340_1
  FIN_CUI_350_1(["Fin de este camino"]):::fin
  CUI_350 -->|"Informes contestados o prueba desistida"| FIN_CUI_350_1
  FIN_CUI_360_1(["Fin de este camino"]):::fin
  CUI_360 -->|"Entrevista realizada o no corresponde por la edad del niño"| FIN_CUI_360_1
  CUI_360 -->|"El niño pide un abogado del niño"| CUI_380
  FIN_CUI_370_1(["Fin de este camino"]):::fin
  CUI_370 -->|"Prueba incorporada o se prescinde de la pendiente"| FIN_CUI_370_1
  FIN_CUI_380_1(["Fin de este camino"]):::fin
  CUI_380 -->|"Abogado del niño designado"| FIN_CUI_380_1
  P_CUI_400_1(["Se abren en paralelo"]):::paralelo
  CUI_400 -->|"Audiencia fijada"| P_CUI_400_1
  P_CUI_400_1 --> CUI_370
  P_CUI_400_1 --> CUI_410
  EXT_CUI_900_destino["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_410 -->|"Acuerdo en la audiencia"| EXT_CUI_900_destino
  EXT_CUI_490_destino["CUI_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  CUI_410 -->|"Audiencia concluida: causa para sentencia"| EXT_CUI_490_destino
  CUI_410 -->|"Audiencia suspendida por fuerza mayor"| CUI_400
  EXT_CUI_900_origen["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  EXT_CUI_900_origen -.->|"Homologación denegada con el juicio en trámite"| CUI_310
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Sentencia y recursos

```mermaid
flowchart TD
  subgraph F_0["Sentencia"]
    CUI_490["<b>CUI_490</b> Asesoría de Incapaces: vista previa a la sentencia<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_500["<b>CUI_500</b> Sentencia<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_520["<b>CUI_520</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    CUI_600["<b>CUI_600</b> Recurso de apelación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CUI_610["<b>CUI_610</b> Fundamentación de la apelación (expresión de agravios o memorial)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CUI_620["<b>CUI_620</b> Sentencia de la Cámara (Sala de Familia)<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_630["<b>CUI_630</b> Recurso extraordinario ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CUI_640["<b>CUI_640</b> Queja ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CUI_650["<b>CUI_650</b> Trámite y resolución ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_CUI_250_origen["CUI_250 Demanda no contestada<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  EXT_CUI_250_origen -.->|"El juez dicta sentencia sin más trámite (art. 840)"| CUI_490
  EXT_CUI_300_origen["CUI_300 Audiencia preliminar<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  EXT_CUI_300_origen -.->|"Cuestión de puro derecho"| CUI_490
  EXT_CUI_410_origen["CUI_410 Audiencia de vista de causa<br/>(ver Prueba, escucha del niño y vista de causa)"]:::externo
  EXT_CUI_410_origen -.->|"Audiencia concluida: causa para sentencia"| CUI_490
  CUI_490 -->|"Dictamen emitido o no corresponde la intervención"| CUI_500
  P_CUI_500_1(["Se abren en paralelo"]):::paralelo
  CUI_500 -->|"Sentencia notificada"| P_CUI_500_1
  P_CUI_500_1 --> CUI_520
  P_CUI_500_1 --> CUI_600
  FIN_CUI_520_1(["Fin de este camino"]):::fin
  CUI_520 -->|"Regulación firme o apelación resuelta"| FIN_CUI_520_1
  EXT_CUI_700_destino["CUI_700 Cumplimiento del régimen de cuidado y comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  CUI_600 -->|"No se apela o se deniega la apelación: sentencia firme"| EXT_CUI_700_destino
  CUI_600 -->|"Apelación concedida"| CUI_610
  CUI_610 -->|"Recurso fundado: resuelve la Cámara"| CUI_620
  CUI_610 -->|"No se funda: recurso desierto y sentencia firme"| EXT_CUI_700_destino
  CUI_620 -->|"Sentencia de la Cámara notificada"| CUI_630
  CUI_630 -->|"No se recurre: sentencia firme"| EXT_CUI_700_destino
  CUI_630 -->|"Recurso concedido"| CUI_650
  CUI_630 -->|"Recurso denegado"| CUI_640
  CUI_640 -->|"Queja admitida"| CUI_650
  CUI_640 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_CUI_700_destino
  CUI_650 -->|"La SCBA resuelve: sentencia firme"| EXT_CUI_700_destino
  CUI_650 -->|"La SCBA anula y reenvía para un nuevo pronunciamiento"| CUI_620
  EXT_CUI_820_origen["CUI_820 Autorización judicial para salir del país o cambiar la residencia<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  EXT_CUI_820_origen -.->|"Resolución sobre la autorización notificada"| CUI_600
  EXT_CUI_830_origen["CUI_830 Restitución internacional del niño<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  EXT_CUI_830_origen -.->|"Resolución sobre la restitución notificada"| CUI_600
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Cumplimiento, incumplimiento y modificación

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    CUI_700["<b>CUI_700</b> Cumplimiento del régimen de cuidado y comunicación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Incumplimiento y modificación"]
    CUI_720["<b>CUI_720</b> Incumplimiento del régimen o impedimento de contacto<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_730["<b>CUI_730</b> Medidas del juez ante el incumplimiento reiterado<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CUI_800["<b>CUI_800</b> Modificación del cuidado personal o del régimen de comunicación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_CUI_010_origen["CUI_010 Consulta sobre el cuidado o la comunicación con el hijo<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_010_origen -.->|"Ya hay un régimen fijado y no se cumple"| CUI_720
  EXT_CUI_010_origen -.->|"Ya hay un régimen fijado y cambiaron las circunstancias"| CUI_800
  EXT_CUI_600_origen["CUI_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CUI_600_origen -.->|"No se apela o se deniega la apelación: sentencia firme"| CUI_700
  EXT_CUI_610_origen["CUI_610 Fundamentación de la apelación (expresión de agravios o memorial)<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CUI_610_origen -.->|"No se funda: recurso desierto y sentencia firme"| CUI_700
  EXT_CUI_630_origen["CUI_630 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CUI_630_origen -.->|"No se recurre: sentencia firme"| CUI_700
  EXT_CUI_640_origen["CUI_640 Queja ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CUI_640_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| CUI_700
  EXT_CUI_650_origen["CUI_650 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CUI_650_origen -.->|"La SCBA resuelve: sentencia firme"| CUI_700
  EXT_CUI_990_destino["CUI_990 Archivo del expediente<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_700 -->|"Régimen cumplido hasta la mayoría de edad del hijo"| EXT_CUI_990_destino
  CUI_700 -->|"Incumplimiento o impedimento de contacto"| CUI_720
  CUI_700 -->|"Cambio de circunstancias"| CUI_800
  CUI_720 -->|"Se pide al juez que intime y aplique medidas"| CUI_730
  EXT_CUI_900_destino["CUI_900 Acuerdo y homologación<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_720 -->|"Acuerdo para reanudar el régimen"| EXT_CUI_900_destino
  CUI_730 -->|"Régimen restablecido"| CUI_700
  CUI_730 -->|"El incumplimiento persiste: se pide la modificación del cuidado"| CUI_800
  CUI_800 -->|"Acuerdo sobre la modificación"| EXT_CUI_900_destino
  EXT_CUI_100_destino["CUI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  CUI_800 -->|"Sin acuerdo: etapa previa ante el Consejero"| EXT_CUI_100_destino
  EXT_CUI_910_origen["CUI_910 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo y cierre)"]:::externo
  EXT_CUI_910_origen -.->|"Incumplimiento o impedimento de contacto"| CUI_720
  EXT_CUI_910_origen -.->|"Cambio de circunstancias"| CUI_800
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Viajes, restitución internacional y delegación

```mermaid
flowchart TD
  subgraph F_0["Situaciones especiales"]
    CUI_820["<b>CUI_820</b> Autorización judicial para salir del país o cambiar la residencia<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_830["<b>CUI_830</b> Restitución internacional del niño<br/>Responsable: Quien promueve<br/>1 año"]:::actora
    CUI_840["<b>CUI_840</b> Delegación del ejercicio o guarda a un pariente (plazo de un año)<br/>Responsable: Cualquiera de las partes<br/>1 año"]:::ambas
  end
  EXT_CUI_010_origen["CUI_010 Consulta sobre el cuidado o la comunicación con el hijo<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_010_origen -.->|"Hay que autorizar un viaje al exterior o un cambio de residencia"| CUI_820
  EXT_CUI_010_origen -.->|"Traslado o retención ilícitos del hijo a través de la frontera"| CUI_830
  EXT_CUI_010_origen -.->|"Delegación del ejercicio en un pariente"| CUI_840
  EXT_CUI_600_destino["CUI_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  CUI_820 -->|"Resolución sobre la autorización notificada"| EXT_CUI_600_destino
  EXT_CUI_990_destino["CUI_990 Archivo del expediente<br/>(ver Acuerdo y cierre)"]:::externo
  CUI_820 -->|"El otro progenitor consiente: no hace falta la autorización"| EXT_CUI_990_destino
  CUI_830 -->|"Resolución sobre la restitución notificada"| EXT_CUI_600_destino
  CUI_830 -->|"Regreso voluntario o acuerdo"| EXT_CUI_990_destino
  CUI_840 -->|"Se renueva o prorroga judicialmente por un período más"| CUI_840
  CUI_840 -->|"Vence o cesa la delegación o la guarda"| EXT_CUI_990_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 9. Acuerdo y cierre

```mermaid
flowchart TD
  subgraph F_0["Acuerdo"]
    CUI_900["<b>CUI_900</b> Acuerdo y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    CUI_910["<b>CUI_910</b> Cumplimiento del acuerdo homologado<br/>Responsable: Otro progenitor<br/>Sin plazo"]:::demandada
    CUI_950["<b>CUI_950</b> Control de caducidad de instancia<br/>Responsable: Quien promueve<br/>3 meses"]:::actora
    CUI_960["<b>CUI_960</b> Intimación previa a la caducidad de instancia<br/>Responsable: Quien promueve<br/>5 días hábiles judiciales + gracia"]:::actora
  end
  subgraph F_1["Cierre"]
    CUI_970["<b>CUI_970</b> Sigue en la matriz de alimentos y compensación económica<br/>Responsable: Quien promueve<br/>Sin plazo"]:::actora
    CUI_990["<b>CUI_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_CUI_010_origen["CUI_010 Consulta sobre el cuidado o la comunicación con el hijo<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_010_origen -.->|"Sin acuerdo, y además hay que reclamar alimentos para el hijo"| CUI_970
  EXT_CUI_030_origen["CUI_030 Plan de parentalidad acordado<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_CUI_030_origen -.->|"Plan acordado: se pide la homologación"| CUI_900
  EXT_CUI_120_origen["CUI_120 Acta de cierre de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_CUI_120_origen -.->|"Acuerdo"| CUI_900
  EXT_CUI_300_origen["CUI_300 Audiencia preliminar<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  EXT_CUI_300_origen -.->|"Acuerdo en la audiencia"| CUI_900
  EXT_CUI_300_origen -.->|"El actor no comparece sin justa causa: se lo tiene por desistido"| CUI_990
  EXT_CUI_310_origen["CUI_310 Apertura a prueba y proveído de la prueba<br/>(ver Prueba, escucha del niño y vista de causa)"]:::externo
  EXT_CUI_310_origen -.->|"Se provee la prueba ofrecida"| CUI_950
  EXT_CUI_310_origen -.->|"Se provee la prueba y se deniega una parte"| CUI_950
  EXT_CUI_410_origen["CUI_410 Audiencia de vista de causa<br/>(ver Prueba, escucha del niño y vista de causa)"]:::externo
  EXT_CUI_410_origen -.->|"Acuerdo en la audiencia"| CUI_900
  EXT_CUI_700_origen["CUI_700 Cumplimiento del régimen de cuidado y comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  EXT_CUI_700_origen -.->|"Régimen cumplido hasta la mayoría de edad del hijo"| CUI_990
  EXT_CUI_720_origen["CUI_720 Incumplimiento del régimen o impedimento de contacto<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  EXT_CUI_720_origen -.->|"Acuerdo para reanudar el régimen"| CUI_900
  EXT_CUI_800_origen["CUI_800 Modificación del cuidado personal o del régimen de comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  EXT_CUI_800_origen -.->|"Acuerdo sobre la modificación"| CUI_900
  EXT_CUI_820_origen["CUI_820 Autorización judicial para salir del país o cambiar la residencia<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  EXT_CUI_820_origen -.->|"El otro progenitor consiente: no hace falta la autorización"| CUI_990
  EXT_CUI_830_origen["CUI_830 Restitución internacional del niño<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  EXT_CUI_830_origen -.->|"Regreso voluntario o acuerdo"| CUI_990
  EXT_CUI_840_origen["CUI_840 Delegación del ejercicio o guarda a un pariente (plazo de un año)<br/>(ver Viajes, restitución internacional y delegación)"]:::externo
  EXT_CUI_840_origen -.->|"Vence o cesa la delegación o la guarda"| CUI_990
  CUI_900 -->|"Acuerdo homologado"| CUI_910
  EXT_CUI_200_destino["CUI_200 Demanda de cuidado personal o régimen de comunicación<br/>(ver Demanda, contestación y audiencia preliminar)"]:::externo
  CUI_900 -->|"Homologación denegada antes de la demanda"| EXT_CUI_200_destino
  EXT_CUI_310_destino["CUI_310 Apertura a prueba y proveído de la prueba<br/>(ver Prueba, escucha del niño y vista de causa)"]:::externo
  CUI_900 -->|"Homologación denegada con el juicio en trámite"| EXT_CUI_310_destino
  CUI_910 -->|"Acuerdo cumplido hasta la mayoría de edad del hijo"| CUI_990
  EXT_CUI_720_destino["CUI_720 Incumplimiento del régimen o impedimento de contacto<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  CUI_910 -->|"Incumplimiento o impedimento de contacto"| EXT_CUI_720_destino
  EXT_CUI_800_destino["CUI_800 Modificación del cuidado personal o del régimen de comunicación<br/>(ver Cumplimiento, incumplimiento y modificación)"]:::externo
  CUI_910 -->|"Cambio de circunstancias"| EXT_CUI_800_destino
  CUI_950 -->|"Se impulsa el proceso: se actualiza el Día Cero al último acto"| CUI_950
  FIN_CUI_950_2(["Fin de este camino"]):::fin
  CUI_950 -->|"Se dicta sentencia o termina el proceso"| FIN_CUI_950_2
  CUI_950 -->|"La contraria pide la caducidad"| CUI_960
  CUI_960 -->|"Actividad útil en término"| CUI_950
  CUI_960 -->|"No hay actividad útil: se decreta la caducidad"| CUI_990
  style CUI_970 stroke-width:3px
  style CUI_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
