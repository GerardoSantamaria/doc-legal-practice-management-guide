# Diagrama de Flujo: Daños y perjuicios (tránsito, mala praxis, contractual y daños a bienes) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68), juicio sumario (art. 320 inc. 2 k); CCyC arts. 1708 a 1780; Ley 17.418 (art. 118); Ley 13.951 (mediación) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_civil_danos_y_perjuicios_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el damnificado que reclama (ACTORA); naranja = el responsable del daño o su aseguradora, también la citada en garantía (DEMANDADA); gris = el juzgado, el mediador o un organismo (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la prescripción de 3 años sigue corriendo mientras se reclama a la aseguradora.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>17 hitos"]
  FASE_2["Postulación<br/>9 hitos"]
  FASE_3["Prueba<br/>9 hitos"]
  FASE_4["Sentencia<br/>5 hitos"]
  FASE_5["Recursos<br/>8 hitos"]
  FASE_6["Ejecución<br/>6 hitos"]
  FASE_7["Acuerdo<br/>2 hitos"]
  FASE_8["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_8
  FASE_1 --> FASE_7
  FASE_1 --> FASE_2
  FASE_2 --> FASE_8
  FASE_2 --> FASE_5
  FASE_2 --> FASE_3
  FASE_3 --> FASE_4
  FASE_3 --> FASE_7
  FASE_4 --> FASE_5
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_6 --> FASE_8
  FASE_7 --> FASE_4
  FASE_7 --> FASE_8
  FASE_7 --> FASE_6
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    DYP_010["INICIO - <b>DYP_010</b> Consulta inicial por el daño sufrido<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_015["<b>DYP_015</b> Control de prescripción de la acción<br/>Responsable: Damnificado<br/>3 años"]:::actora
    DYP_017["<b>DYP_017</b> Suspensión de la prescripción por la interpelación fehaciente<br/>Responsable: Damnificado<br/>6 meses"]:::actora
    DYP_020["<b>DYP_020</b> Relevamiento del siniestro de tránsito<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_024["<b>DYP_024</b> Respuesta de la aseguradora del responsable al reclamo<br/>Responsable: Responsable o aseguradora<br/>30 días corridos"]:::demandada
    DYP_030["<b>DYP_030</b> Seguimiento de la causa penal<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_042["<b>DYP_042</b> Entrega de la copia de la historia clínica<br/>Responsable: Responsable o aseguradora<br/>48 horas"]:::demandada
    DYP_044["<b>DYP_044</b> Evaluación médico-legal del caso de mala praxis<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_046["<b>DYP_046</b> Prueba anticipada: secuestro de la historia clínica, pericia o reconocimiento<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_050["<b>DYP_050</b> Análisis del contrato y del incumplimiento<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_060["<b>DYP_060</b> Constatación del daño al inmueble o a otros bienes<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_070["<b>DYP_070</b> Respuesta del responsable a la carta documento<br/>Responsable: Responsable o aseguradora<br/>Sin plazo"]:::demandada
    DYP_080["<b>DYP_080</b> Requerimiento de mediación prejudicial obligatoria<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_082["<b>DYP_082</b> Audiencia de mediación<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DYP_084["<b>DYP_084</b> Plazo de la mediación<br/>Responsable: Juzgado u organismo<br/>60 días corridos"]:::tribunal
    DYP_086["<b>DYP_086</b> Reanudación de la prescripción después de la mediación<br/>Responsable: Damnificado<br/>20 días corridos"]:::actora
    DYP_090["<b>DYP_090</b> Convenio extrajudicial y cobro<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  P_DYP_010_1(["Se abren en paralelo"]):::paralelo
  DYP_010 -->|"Accidente de tránsito"| P_DYP_010_1
  P_DYP_010_1 --> DYP_015
  P_DYP_010_1 --> DYP_020
  P_DYP_010_2(["Se abren en paralelo"]):::paralelo
  DYP_010 -->|"Mala praxis médica"| P_DYP_010_2
  P_DYP_010_2 --> DYP_015
  P_DYP_010_2 --> DYP_042
  P_DYP_010_3(["Se abren en paralelo"]):::paralelo
  DYP_010 -->|"Daño por incumplimiento contractual"| P_DYP_010_3
  P_DYP_010_3 --> DYP_015
  P_DYP_010_3 --> DYP_050
  P_DYP_010_4(["Se abren en paralelo"]):::paralelo
  DYP_010 -->|"Daño a un inmueble o a otros bienes"| P_DYP_010_4
  P_DYP_010_4 --> DYP_015
  P_DYP_010_4 --> DYP_060
  FIN_DYP_015_1(["Fin de este camino"]):::fin
  DYP_015 -->|"Demanda presentada antes del vencimiento, o reclamo abandonado"| FIN_DYP_015_1
  FIN_DYP_017_1(["Fin de este camino"]):::fin
  DYP_017 -->|"Suspensión agotada o demanda presentada"| FIN_DYP_017_1
  P_DYP_020_1(["Se abren en paralelo"]):::paralelo
  DYP_020 -->|"Hay lesiones o muerte: se sigue la causa penal"| P_DYP_020_1
  P_DYP_020_1 --> DYP_024
  P_DYP_020_1 --> DYP_030
  DYP_020 -->|"Solo daños materiales: se reclama a la aseguradora"| DYP_024
  DYP_020 -->|"El responsable no tiene seguro: se lo intima"| DYP_070
  DYP_024 -->|"Oferta aceptada"| DYP_090
  DYP_024 -->|"Rechazo, silencio u oferta insuficiente"| DYP_080
  FIN_DYP_030_1(["Fin de este camino"]):::fin
  DYP_030 -->|"Causa penal concluida, archivada o en trámite (se informa al juez civil)"| FIN_DYP_030_1
  DYP_042 -->|"Historia clínica entregada"| DYP_044
  DYP_042 -->|"No entregada o incompleta"| DYP_046
  DYP_044 -->|"Caso viable: se intima al responsable"| DYP_070
  EXT_DYP_990_destino["DYP_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DYP_044 -->|"Caso no viable: se informa al cliente"| EXT_DYP_990_destino
  DYP_046 -->|"Historia clínica obtenida"| DYP_044
  DYP_046 -->|"Pericia o reconocimiento judicial producido"| DYP_070
  DYP_050 -->|"Incumplimiento y daños identificados: se intima"| DYP_070
  DYP_060 -->|"Daño constatado: se intima al responsable"| DYP_070
  DYP_060 -->|"Hace falta prueba anticipada"| DYP_046
  DYP_070 -->|"Acuerdo extrajudicial"| DYP_090
  P_DYP_070_2(["Se abren en paralelo"]):::paralelo
  DYP_070 -->|"Rechazo o silencio: se pide la mediación"| P_DYP_070_2
  P_DYP_070_2 --> DYP_017
  P_DYP_070_2 --> DYP_080
  P_DYP_080_1(["Se abren en paralelo"]):::paralelo
  DYP_080 -->|"Mediador designado y audiencia fijada"| P_DYP_080_1
  P_DYP_080_1 --> DYP_082
  P_DYP_080_1 --> DYP_084
  FIN_DYP_082_1(["Fin de este camino"]):::fin
  DYP_082 -->|"Audiencia realizada"| FIN_DYP_082_1
  EXT_DYP_800_destino["DYP_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  DYP_084 -->|"Acuerdo en la mediación"| EXT_DYP_800_destino
  P_DYP_084_2(["Se abren en paralelo"]):::paralelo
  DYP_084 -->|"Cierre sin acuerdo o por incomparecencia"| P_DYP_084_2
  EXT_DYP_300_destino["DYP_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  P_DYP_084_2 --> EXT_DYP_300_destino
  P_DYP_084_2 --> DYP_086
  FIN_DYP_086_1(["Fin de este camino"]):::fin
  DYP_086 -->|"Demanda presentada"| FIN_DYP_086_1
  DYP_090 -->|"Convenio cumplido"| EXT_DYP_990_destino
  DYP_090 -->|"Convenio incumplido"| DYP_080
  style DYP_010 stroke-width:3px
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
    DYP_300["<b>DYP_300</b> Presentación de la demanda<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_310["<b>DYP_310</b> Beneficio de litigar sin gastos<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_320["<b>DYP_320</b> Medidas cautelares<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_330["<b>DYP_330</b> Radicación, control de admisibilidad y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_340["<b>DYP_340</b> Contestación de la demanda<br/>Responsable: Responsable o aseguradora<br/>10 días hábiles judiciales + gracia"]:::demandada
    DYP_345["<b>DYP_345</b> Contestación de la citación en garantía por la aseguradora<br/>Responsable: Responsable o aseguradora<br/>10 días hábiles judiciales + gracia"]:::demandada
    DYP_355["<b>DYP_355</b> Traslado a la actora de las excepciones previas<br/>Responsable: Damnificado<br/>5 días hábiles judiciales + gracia"]:::actora
    DYP_360["<b>DYP_360</b> Traslado a la actora de la documental de la contestación<br/>Responsable: Damnificado<br/>5 días hábiles judiciales + gracia"]:::actora
    DYP_370["<b>DYP_370</b> Contestación de la reconvención<br/>Responsable: Damnificado<br/>10 días hábiles judiciales + gracia"]:::actora
  end
  EXT_DYP_084_origen["DYP_084 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_DYP_084_origen -.->|"Cierre sin acuerdo o por incomparecencia"| DYP_300
  P_DYP_300_1(["Se abren en paralelo"]):::paralelo
  DYP_300 -->|"Demanda presentada"| P_DYP_300_1
  P_DYP_300_1 --> DYP_330
  EXT_DYP_900_destino["DYP_900 Control de la caducidad de instancia<br/>(ver Cierre)"]:::externo
  P_DYP_300_1 --> EXT_DYP_900_destino
  P_DYP_300_2(["Se abren en paralelo"]):::paralelo
  DYP_300 -->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| P_DYP_300_2
  P_DYP_300_2 --> DYP_330
  P_DYP_300_2 --> DYP_310
  P_DYP_300_2 --> EXT_DYP_900_destino
  P_DYP_300_3(["Se abren en paralelo"]):::paralelo
  DYP_300 -->|"Demanda presentada con pedido de medida cautelar"| P_DYP_300_3
  P_DYP_300_3 --> DYP_330
  P_DYP_300_3 --> DYP_320
  P_DYP_300_3 --> EXT_DYP_900_destino
  FIN_DYP_310_1(["Fin de este camino"]):::fin
  DYP_310 -->|"Beneficio concedido, o denegado sin recurso (se integran tasa y aportes)"| FIN_DYP_310_1
  EXT_DYP_650_destino["DYP_650 Memorial del recurso concedido en relación<br/>(ver Sentencia y recursos)"]:::externo
  DYP_310 -->|"Beneficio denegado: se apela"| EXT_DYP_650_destino
  FIN_DYP_320_1(["Fin de este camino"]):::fin
  DYP_320 -->|"Medida trabada o denegada sin recurso"| FIN_DYP_320_1
  DYP_320 -->|"Medida denegada o trabada: se apela"| EXT_DYP_650_destino
  EXT_DYP_990_destino["DYP_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DYP_330 -->|"Demanda rechazada in limine o no subsanada"| EXT_DYP_990_destino
  DYP_330 -->|"Se ordena el traslado de la demanda"| DYP_340
  P_DYP_330_3(["Se abren en paralelo"]):::paralelo
  DYP_330 -->|"Se ordena el traslado de la demanda y la citación en garantía"| P_DYP_330_3
  P_DYP_330_3 --> DYP_340
  P_DYP_330_3 --> DYP_345
  DYP_340 -->|"Contesta la demanda"| DYP_360
  P_DYP_340_2(["Se abren en paralelo"]):::paralelo
  DYP_340 -->|"Contesta y opone excepciones previas"| P_DYP_340_2
  P_DYP_340_2 --> DYP_360
  P_DYP_340_2 --> DYP_355
  P_DYP_340_3(["Se abren en paralelo"]):::paralelo
  DYP_340 -->|"Contesta y reconviene"| P_DYP_340_3
  P_DYP_340_3 --> DYP_360
  P_DYP_340_3 --> DYP_370
  EXT_DYP_400_destino["DYP_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  DYP_340 -->|"No contesta en término"| EXT_DYP_400_destino
  FIN_DYP_345_1(["Fin de este camino"]):::fin
  DYP_345 -->|"Contesta aceptando o declinando la cobertura, o vence el plazo"| FIN_DYP_345_1
  FIN_DYP_355_1(["Fin de este camino"]):::fin
  DYP_355 -->|"Excepciones rechazadas o diferidas para la sentencia"| FIN_DYP_355_1
  DYP_355 -->|"Excepción admitida que pone fin al proceso: se apela"| EXT_DYP_650_destino
  DYP_355 -->|"Excepción admitida y consentida"| EXT_DYP_990_destino
  DYP_360 -->|"Traslado contestado o plazo vencido"| EXT_DYP_400_destino
  FIN_DYP_370_1(["Fin de este camino"]):::fin
  DYP_370 -->|"Reconvención contestada o plazo vencido"| FIN_DYP_370_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Prueba

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    DYP_400["<b>DYP_400</b> Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_405["<b>DYP_405</b> Reposición u oposición contra la providencia de prueba<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DYP_415["<b>DYP_415</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DYP_420["<b>DYP_420</b> Dictamen pericial<br/>Responsable: Juzgado u organismo<br/>5 días hábiles de anticipación"]:::tribunal
    DYP_425["<b>DYP_425</b> Traslado del dictamen pericial<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_430["<b>DYP_430</b> Prueba informativa: contestación de los oficios<br/>Responsable: Juzgado u organismo<br/>10 días hábiles judiciales"]:::tribunal
    DYP_435["<b>DYP_435</b> Pedido de reiteración del oficio no contestado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_440["<b>DYP_440</b> Audiencia de prueba o de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DYP_450["<b>DYP_450</b> Alegatos<br/>Responsable: Cualquiera de las partes<br/>6 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DYP_340_origen["DYP_340 Contestación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_340_origen -.->|"No contesta en término"| DYP_400
  EXT_DYP_360_origen["DYP_360 Traslado a la actora de la documental de la contestación<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_360_origen -.->|"Traslado contestado o plazo vencido"| DYP_400
  P_DYP_400_1(["Se abren en paralelo"]):::paralelo
  DYP_400 -->|"Se provee la prueba ofrecida"| P_DYP_400_1
  P_DYP_400_1 --> DYP_405
  P_DYP_400_1 --> DYP_420
  P_DYP_400_1 --> DYP_430
  P_DYP_400_1 --> DYP_440
  DYP_400 -->|"Se fija audiencia preliminar"| DYP_415
  EXT_DYP_500_destino["DYP_500 Llamamiento de autos y sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  DYP_400 -->|"Causa declarada de puro derecho"| EXT_DYP_500_destino
  FIN_DYP_405_1(["Fin de este camino"]):::fin
  DYP_405 -->|"Resuelta o plazo vencido"| FIN_DYP_405_1
  EXT_DYP_800_destino["DYP_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  DYP_415 -->|"Acuerdo conciliatorio en la audiencia"| EXT_DYP_800_destino
  P_DYP_415_2(["Se abren en paralelo"]):::paralelo
  DYP_415 -->|"Se provee la prueba y se fija la audiencia de vista de causa"| P_DYP_415_2
  P_DYP_415_2 --> DYP_405
  P_DYP_415_2 --> DYP_420
  P_DYP_415_2 --> DYP_430
  P_DYP_415_2 --> DYP_440
  DYP_415 -->|"Causa declarada de puro derecho"| EXT_DYP_500_destino
  DYP_420 -->|"Dictamen presentado"| DYP_425
  FIN_DYP_420_2(["Fin de este camino"]):::fin
  DYP_420 -->|"Pericia no ofrecida o desistida"| FIN_DYP_420_2
  FIN_DYP_425_1(["Fin de este camino"]):::fin
  DYP_425 -->|"Observaciones presentadas o plazo vencido"| FIN_DYP_425_1
  FIN_DYP_430_1(["Fin de este camino"]):::fin
  DYP_430 -->|"Informes contestados o prueba desistida"| FIN_DYP_430_1
  DYP_430 -->|"Plazo vencido sin respuesta"| DYP_435
  DYP_435 -->|"Reiteración pedida"| DYP_430
  FIN_DYP_435_2(["Fin de este camino"]):::fin
  DYP_435 -->|"No se pide: prueba desistida"| FIN_DYP_435_2
  DYP_440 -->|"Audiencia realizada y prueba producida"| DYP_450
  DYP_440 -->|"Acuerdo conciliatorio en la audiencia"| EXT_DYP_800_destino
  DYP_450 -->|"Alegatos presentados o plazo vencido"| EXT_DYP_500_destino
  EXT_DYP_495_destino["DYP_495 Suspensión del dictado de la sentencia por la causa penal<br/>(ver Sentencia y recursos)"]:::externo
  DYP_450 -->|"Alegatos presentados o plazo vencido, con causa penal en trámite"| EXT_DYP_495_destino
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
    DYP_495["<b>DYP_495</b> Suspensión del dictado de la sentencia por la causa penal<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_500["<b>DYP_500</b> Llamamiento de autos y sentencia definitiva<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_505["<b>DYP_505</b> Aclaratoria<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DYP_510["<b>DYP_510</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_515["<b>DYP_515</b> Pago de los honorarios firmes<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  subgraph F_1["Recursos"]
    DYP_600["<b>DYP_600</b> Recurso de apelación contra la sentencia definitiva<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_610["<b>DYP_610</b> Expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_615["<b>DYP_615</b> Contestación de la expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_620["<b>DYP_620</b> Sentencia o resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DYP_630["<b>DYP_630</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    DYP_640["<b>DYP_640</b> Queja ante la SCBA por recurso denegado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DYP_645["<b>DYP_645</b> Trámite y sentencia de la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    DYP_650["<b>DYP_650</b> Memorial del recurso concedido en relación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DYP_310_origen["DYP_310 Beneficio de litigar sin gastos<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_310_origen -.->|"Beneficio denegado: se apela"| DYP_650
  EXT_DYP_320_origen["DYP_320 Medidas cautelares<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_320_origen -.->|"Medida denegada o trabada: se apela"| DYP_650
  EXT_DYP_355_origen["DYP_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_355_origen -.->|"Excepción admitida que pone fin al proceso: se apela"| DYP_650
  EXT_DYP_400_origen["DYP_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  EXT_DYP_400_origen -.->|"Causa declarada de puro derecho"| DYP_500
  EXT_DYP_415_origen["DYP_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_DYP_415_origen -.->|"Causa declarada de puro derecho"| DYP_500
  EXT_DYP_450_origen["DYP_450 Alegatos<br/>(ver Prueba)"]:::externo
  EXT_DYP_450_origen -.->|"Alegatos presentados o plazo vencido"| DYP_500
  EXT_DYP_450_origen -.->|"Alegatos presentados o plazo vencido, con causa penal en trámite"| DYP_495
  DYP_495 -->|"Causa penal concluida o se aplica una excepción del art. 1775"| DYP_500
  P_DYP_500_1(["Se abren en paralelo"]):::paralelo
  DYP_500 -->|"Sentencia notificada"| P_DYP_500_1
  P_DYP_500_1 --> DYP_505
  P_DYP_500_1 --> DYP_510
  P_DYP_500_1 --> DYP_600
  FIN_DYP_505_1(["Fin de este camino"]):::fin
  DYP_505 -->|"Aclaratoria resuelta o plazo vencido"| FIN_DYP_505_1
  DYP_510 -->|"Regulación firme"| DYP_515
  FIN_DYP_515_1(["Fin de este camino"]):::fin
  DYP_515 -->|"Honorarios pagados o en ejecución"| FIN_DYP_515_1
  EXT_DYP_700_destino["DYP_700 Liquidación<br/>(ver Ejecución)"]:::externo
  DYP_600 -->|"No se recurre: queda firme y hace lugar a la demanda"| EXT_DYP_700_destino
  EXT_DYP_990_destino["DYP_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DYP_600 -->|"No se recurre: queda firme y rechaza la demanda"| EXT_DYP_990_destino
  DYP_600 -->|"Se interpone apelación"| DYP_610
  DYP_610 -->|"Agravios presentados"| DYP_615
  DYP_610 -->|"No expresa agravios: deserción"| DYP_620
  DYP_615 -->|"Contestados o plazo vencido"| DYP_620
  DYP_620 -->|"Sentencia de Cámara firme que hace lugar a la demanda"| EXT_DYP_700_destino
  DYP_620 -->|"Sentencia de Cámara firme que rechaza la demanda"| EXT_DYP_990_destino
  FIN_DYP_620_3(["Fin de este camino"]):::fin
  DYP_620 -->|"Cámara resuelve la apelación de una resolución interlocutoria: sigue el trámite"| FIN_DYP_620_3
  DYP_620 -->|"Se interponen recursos extraordinarios"| DYP_630
  DYP_630 -->|"Recurso concedido"| DYP_645
  DYP_630 -->|"Recurso denegado"| DYP_640
  DYP_640 -->|"Queja admitida"| DYP_645
  DYP_640 -->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| EXT_DYP_700_destino
  DYP_640 -->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| EXT_DYP_990_destino
  DYP_645 -->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| EXT_DYP_700_destino
  DYP_645 -->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| EXT_DYP_990_destino
  DYP_645 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| DYP_620
  DYP_650 -->|"Memorial presentado o plazo vencido"| DYP_620
  EXT_DYP_800_origen["DYP_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  EXT_DYP_800_origen -.->|"Acuerdo homologado"| DYP_510
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Ejecución

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    DYP_700["<b>DYP_700</b> Liquidación<br/>Responsable: Damnificado<br/>10 días hábiles judiciales + gracia"]:::actora
    DYP_705["<b>DYP_705</b> Traslado de la liquidación<br/>Responsable: Responsable o aseguradora<br/>5 días hábiles judiciales + gracia"]:::demandada
    DYP_710["<b>DYP_710</b> Embargo y citación de venta<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
    DYP_720["<b>DYP_720</b> Excepciones del ejecutado<br/>Responsable: Responsable o aseguradora<br/>5 días hábiles judiciales + gracia"]:::demandada
    DYP_725["<b>DYP_725</b> Pago de la aseguradora citada: límite de cobertura y franquicia<br/>Responsable: Responsable o aseguradora<br/>Sin plazo"]:::demandada
    DYP_730["<b>DYP_730</b> Cobro y rendición al cliente<br/>Responsable: Damnificado<br/>Sin plazo"]:::actora
  end
  EXT_DYP_600_origen["DYP_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_600_origen -.->|"No se recurre: queda firme y hace lugar a la demanda"| DYP_700
  EXT_DYP_620_origen["DYP_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_620_origen -.->|"Sentencia de Cámara firme que hace lugar a la demanda"| DYP_700
  EXT_DYP_640_origen["DYP_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_640_origen -.->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| DYP_700
  EXT_DYP_645_origen["DYP_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| DYP_700
  DYP_700 -->|"Liquidación presentada"| DYP_705
  DYP_705 -->|"Liquidación aprobada y pagada en término"| DYP_730
  DYP_705 -->|"Liquidación aprobada y no pagada"| DYP_710
  DYP_705 -->|"Liquidación aprobada: se intima el pago a la demandada y a la aseguradora citada"| DYP_725
  DYP_710 -->|"Embargo trabado y citación de venta notificada"| DYP_720
  DYP_720 -->|"Sin excepciones o excepciones rechazadas: fondos embargados o bienes subastados"| DYP_730
  EXT_DYP_990_destino["DYP_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DYP_720 -->|"Excepción de pago admitida"| EXT_DYP_990_destino
  DYP_725 -->|"La aseguradora paga todo"| DYP_730
  P_DYP_725_2(["Se abren en paralelo"]):::paralelo
  DYP_725 -->|"Paga hasta el límite o la franquicia, o no paga: se ejecuta el saldo"| P_DYP_725_2
  P_DYP_725_2 --> DYP_710
  P_DYP_725_2 --> DYP_730
  DYP_730 -->|"Cobro percibido y rendido al cliente"| EXT_DYP_990_destino
  EXT_DYP_805_origen["DYP_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_DYP_805_origen -.->|"Acuerdo incumplido: se ejecuta"| DYP_710
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Acuerdo

```mermaid
flowchart TD
  subgraph F_0["Acuerdo"]
    DYP_800["<b>DYP_800</b> Acuerdo, transacción o conciliación y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    DYP_805["<b>DYP_805</b> Cumplimiento del acuerdo homologado<br/>Responsable: Responsable o aseguradora<br/>Sin plazo"]:::demandada
  end
  EXT_DYP_084_origen["DYP_084 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_DYP_084_origen -.->|"Acuerdo en la mediación"| DYP_800
  EXT_DYP_415_origen["DYP_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_DYP_415_origen -.->|"Acuerdo conciliatorio en la audiencia"| DYP_800
  EXT_DYP_440_origen["DYP_440 Audiencia de prueba o de vista de causa<br/>(ver Prueba)"]:::externo
  EXT_DYP_440_origen -.->|"Acuerdo conciliatorio en la audiencia"| DYP_800
  P_DYP_800_1(["Se abren en paralelo"]):::paralelo
  DYP_800 -->|"Acuerdo homologado"| P_DYP_800_1
  P_DYP_800_1 --> DYP_805
  EXT_DYP_510_destino["DYP_510 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_DYP_800_1 --> EXT_DYP_510_destino
  EXT_DYP_990_destino["DYP_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DYP_805 -->|"Acuerdo cumplido"| EXT_DYP_990_destino
  EXT_DYP_710_destino["DYP_710 Embargo y citación de venta<br/>(ver Ejecución)"]:::externo
  DYP_805 -->|"Acuerdo incumplido: se ejecuta"| EXT_DYP_710_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    DYP_900["<b>DYP_900</b> Control de la caducidad de instancia<br/>Responsable: Damnificado<br/>3 meses"]:::actora
    DYP_905["<b>DYP_905</b> Intimación a activar el proceso<br/>Responsable: Damnificado<br/>5 días hábiles judiciales + gracia"]:::actora
    DYP_990["<b>DYP_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_DYP_044_origen["DYP_044 Evaluación médico-legal del caso de mala praxis<br/>(ver Etapa previa)"]:::externo
  EXT_DYP_044_origen -.->|"Caso no viable: se informa al cliente"| DYP_990
  EXT_DYP_090_origen["DYP_090 Convenio extrajudicial y cobro<br/>(ver Etapa previa)"]:::externo
  EXT_DYP_090_origen -.->|"Convenio cumplido"| DYP_990
  EXT_DYP_300_origen["DYP_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_300_origen -.->|"Demanda presentada"| DYP_900
  EXT_DYP_300_origen -.->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| DYP_900
  EXT_DYP_300_origen -.->|"Demanda presentada con pedido de medida cautelar"| DYP_900
  EXT_DYP_330_origen["DYP_330 Radicación, control de admisibilidad y traslado de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_330_origen -.->|"Demanda rechazada in limine o no subsanada"| DYP_990
  EXT_DYP_355_origen["DYP_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_DYP_355_origen -.->|"Excepción admitida y consentida"| DYP_990
  EXT_DYP_600_origen["DYP_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_600_origen -.->|"No se recurre: queda firme y rechaza la demanda"| DYP_990
  EXT_DYP_620_origen["DYP_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_620_origen -.->|"Sentencia de Cámara firme que rechaza la demanda"| DYP_990
  EXT_DYP_640_origen["DYP_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_640_origen -.->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| DYP_990
  EXT_DYP_645_origen["DYP_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DYP_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| DYP_990
  EXT_DYP_720_origen["DYP_720 Excepciones del ejecutado<br/>(ver Ejecución)"]:::externo
  EXT_DYP_720_origen -.->|"Excepción de pago admitida"| DYP_990
  EXT_DYP_730_origen["DYP_730 Cobro y rendición al cliente<br/>(ver Ejecución)"]:::externo
  EXT_DYP_730_origen -.->|"Cobro percibido y rendido al cliente"| DYP_990
  EXT_DYP_805_origen["DYP_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_DYP_805_origen -.->|"Acuerdo cumplido"| DYP_990
  FIN_DYP_900_1(["Fin de este camino"]):::fin
  DYP_900 -->|"Proceso terminado antes del vencimiento"| FIN_DYP_900_1
  DYP_900 -->|"Plazo vencido: se intima a activar el proceso"| DYP_905
  FIN_DYP_905_1(["Fin de este camino"]):::fin
  DYP_905 -->|"Proceso activado en término"| FIN_DYP_905_1
  DYP_905 -->|"No se activa: se decreta la caducidad"| DYP_990
  style DYP_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
