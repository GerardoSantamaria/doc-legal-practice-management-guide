# Diagrama de Flujo: Prescripción adquisitiva de inmuebles (usucapión) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68), juicio sumario con las reglas de los arts. 679 a 682; CCyC arts. 1897 a 1905; Ley 14.159 (art. 24) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_civil_prescripcion_adquisitiva_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el poseedor que pide la usucapión y al que representamos (ACTORA); naranja = el titular registral, sus herederos, los citados por edictos, el Defensor Oficial de Ausentes, el Fisco de Estado o la Municipalidad (DEMANDADA); gris = el juzgado o un organismo: Registro de la Propiedad, Geodesia, ARBA (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, los edictos al titular y a quienes se consideren con derecho corren mientras se cita al Fisco de Estado y a la Municipalidad.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>7 hitos"]
  FASE_2["Postulación<br/>8 hitos"]
  FASE_3["Citaciones<br/>6 hitos"]
  FASE_4["Prueba<br/>9 hitos"]
  FASE_5["Sentencia<br/>4 hitos"]
  FASE_6["Recursos<br/>8 hitos"]
  FASE_7["Inscripción<br/>3 hitos"]
  FASE_8["Acuerdo<br/>1 hito"]
  FASE_9["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_9
  FASE_1 --> FASE_3
  FASE_2 --> FASE_9
  FASE_2 --> FASE_6
  FASE_2 --> FASE_3
  FASE_3 --> FASE_2
  FASE_3 --> FASE_4
  FASE_2 --> FASE_4
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_6
  FASE_6 --> FASE_7
  FASE_6 --> FASE_9
  FASE_7 --> FASE_9
  FASE_8 --> FASE_9
  FASE_8 --> FASE_5
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    USU_010["INICIO - <b>USU_010</b> Consulta inicial por la posesión del inmueble<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_015["<b>USU_015</b> Cómputo del plazo y prueba de la posesión<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_017["<b>USU_017</b> Cumplimiento del plazo de posesión<br/>Responsable: Poseedor que representamos<br/>10 años"]:::actora
    USU_020["<b>USU_020</b> Informe de dominio y búsqueda del titular registral<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_030["<b>USU_030</b> Plano de mensura para usucapión y visado de Geodesia<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_045["<b>USU_045</b> Evaluación de la regularización dominial de la Ley 24.374<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_060["<b>USU_060</b> Oposición de la usucapión como defensa en el juicio en contra del cliente<br/>Responsable: Poseedor que representamos<br/>15 días hábiles judiciales + gracia"]:::actora
  end
  P_USU_010_1(["Se abren en paralelo"]):::paralelo
  USU_010 -->|"Posesión propia: se prepara la demanda de usucapión"| P_USU_010_1
  P_USU_010_1 --> USU_015
  P_USU_010_1 --> USU_020
  P_USU_010_1 --> USU_030
  USU_010 -->|"Vivienda única: se evalúa la Ley 24.374"| USU_045
  USU_010 -->|"El cliente fue demandado: se opone la usucapión como defensa"| USU_060
  FIN_USU_015_1(["Fin de este camino"]):::fin
  USU_015 -->|"Plazo cumplido y prueba reunida"| FIN_USU_015_1
  USU_015 -->|"Todavía no se cumplió el plazo"| USU_017
  FIN_USU_017_1(["Fin de este camino"]):::fin
  USU_017 -->|"Plazo cumplido"| FIN_USU_017_1
  FIN_USU_020_1(["Fin de este camino"]):::fin
  USU_020 -->|"Informe recibido y titular identificado o declarado ignorado"| FIN_USU_020_1
  EXT_USU_300_destino["USU_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  USU_030 -->|"Plano visado: se presenta la demanda"| EXT_USU_300_destino
  EXT_USU_990_destino["USU_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  USU_045 -->|"Se regulariza por la Ley 24.374"| EXT_USU_990_destino
  P_USU_045_2(["Se abren en paralelo"]):::paralelo
  USU_045 -->|"No reúne los requisitos: se prepara la demanda de usucapión"| P_USU_045_2
  P_USU_045_2 --> USU_015
  P_USU_045_2 --> USU_020
  P_USU_045_2 --> USU_030
  EXT_USU_332_destino["USU_332 Anotación de litis en el Registro de la Propiedad<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  USU_060 -->|"Defensa opuesta: se ordena la anotación de litis"| EXT_USU_332_destino
  style USU_010 stroke-width:3px
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
    USU_300["<b>USU_300</b> Presentación de la demanda<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_310["<b>USU_310</b> Beneficio de litigar sin gastos<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_320["<b>USU_320</b> Medidas cautelares<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_330["<b>USU_330</b> Radicación, control de admisibilidad y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_340["<b>USU_340</b> Contestación de la demanda<br/>Responsable: Titular registral o citado<br/>10 días hábiles judiciales + gracia"]:::demandada
    USU_355["<b>USU_355</b> Traslado a la actora de las excepciones previas<br/>Responsable: Poseedor que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    USU_360["<b>USU_360</b> Traslado a la actora de la documental de la contestación<br/>Responsable: Poseedor que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    USU_370["<b>USU_370</b> Contestación de la reconvención<br/>Responsable: Poseedor que representamos<br/>10 días hábiles judiciales + gracia"]:::actora
  end
  EXT_USU_030_origen["USU_030 Plano de mensura para usucapión y visado de Geodesia<br/>(ver Etapa previa)"]:::externo
  EXT_USU_030_origen -.->|"Plano visado: se presenta la demanda"| USU_300
  P_USU_300_1(["Se abren en paralelo"]):::paralelo
  USU_300 -->|"Demanda presentada"| P_USU_300_1
  P_USU_300_1 --> USU_330
  EXT_USU_900_destino["USU_900 Control de la caducidad de instancia<br/>(ver Cierre)"]:::externo
  P_USU_300_1 --> EXT_USU_900_destino
  P_USU_300_2(["Se abren en paralelo"]):::paralelo
  USU_300 -->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| P_USU_300_2
  P_USU_300_2 --> USU_330
  P_USU_300_2 --> USU_310
  P_USU_300_2 --> EXT_USU_900_destino
  P_USU_300_3(["Se abren en paralelo"]):::paralelo
  USU_300 -->|"Demanda presentada con pedido de medida cautelar"| P_USU_300_3
  P_USU_300_3 --> USU_330
  P_USU_300_3 --> USU_320
  P_USU_300_3 --> EXT_USU_900_destino
  FIN_USU_310_1(["Fin de este camino"]):::fin
  USU_310 -->|"Beneficio concedido, o denegado sin recurso (se integran tasa y aportes)"| FIN_USU_310_1
  EXT_USU_650_destino["USU_650 Memorial del recurso concedido en relación<br/>(ver Sentencia y recursos)"]:::externo
  USU_310 -->|"Beneficio denegado: se apela"| EXT_USU_650_destino
  FIN_USU_320_1(["Fin de este camino"]):::fin
  USU_320 -->|"Medida trabada o denegada sin recurso"| FIN_USU_320_1
  USU_320 -->|"Medida denegada o trabada: se apela"| EXT_USU_650_destino
  EXT_USU_990_destino["USU_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  USU_330 -->|"Demanda rechazada in limine o no subsanada"| EXT_USU_990_destino
  P_USU_330_2(["Se abren en paralelo"]):::paralelo
  USU_330 -->|"Se ordena el traslado al titular con domicilio conocido"| P_USU_330_2
  P_USU_330_2 --> USU_340
  EXT_USU_332_destino["USU_332 Anotación de litis en el Registro de la Propiedad<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  P_USU_330_2 --> EXT_USU_332_destino
  EXT_USU_336_destino["USU_336 Publicación de edictos al titular y a quienes se consideren con derecho<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  P_USU_330_2 --> EXT_USU_336_destino
  EXT_USU_342_destino["USU_342 Contestación del Fisco de Estado y de la Municipalidad<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  P_USU_330_2 --> EXT_USU_342_destino
  P_USU_330_3(["Se abren en paralelo"]):::paralelo
  USU_330 -->|"Titular o domicilio ignorados: se piden informes"| P_USU_330_3
  EXT_USU_334_destino["USU_334 Informes sobre el último domicilio del titular<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  P_USU_330_3 --> EXT_USU_334_destino
  P_USU_330_3 --> EXT_USU_332_destino
  P_USU_330_3 --> EXT_USU_342_destino
  EXT_USU_334_origen["USU_334 Informes sobre el último domicilio del titular<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  EXT_USU_334_origen -.->|"Se encuentra el domicilio: se notifica al titular"| USU_340
  USU_340 -->|"Contesta la demanda"| USU_360
  P_USU_340_2(["Se abren en paralelo"]):::paralelo
  USU_340 -->|"Contesta y opone excepciones previas"| P_USU_340_2
  P_USU_340_2 --> USU_360
  P_USU_340_2 --> USU_355
  P_USU_340_3(["Se abren en paralelo"]):::paralelo
  USU_340 -->|"Contesta y reconviene"| P_USU_340_3
  P_USU_340_3 --> USU_360
  P_USU_340_3 --> USU_370
  EXT_USU_400_destino["USU_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  USU_340 -->|"No contesta en término"| EXT_USU_400_destino
  FIN_USU_355_1(["Fin de este camino"]):::fin
  USU_355 -->|"Excepciones rechazadas o diferidas para la sentencia"| FIN_USU_355_1
  USU_355 -->|"Excepción admitida que pone fin al proceso: se apela"| EXT_USU_650_destino
  USU_355 -->|"Excepción admitida y consentida"| EXT_USU_990_destino
  USU_360 -->|"Traslado contestado o plazo vencido"| EXT_USU_400_destino
  FIN_USU_370_1(["Fin de este camino"]):::fin
  USU_370 -->|"Reconvención contestada o plazo vencido"| FIN_USU_370_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Citaciones, edictos y anotación de litis

```mermaid
flowchart TD
  subgraph F_0["Citaciones"]
    USU_332["<b>USU_332</b> Anotación de litis en el Registro de la Propiedad<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_334["<b>USU_334</b> Informes sobre el último domicilio del titular<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_336["<b>USU_336</b> Publicación de edictos al titular y a quienes se consideren con derecho<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_338["<b>USU_338</b> Plazo para comparecer de los citados por edictos<br/>Responsable: Titular registral o citado<br/>10 días hábiles judiciales + gracia"]:::demandada
    USU_339["<b>USU_339</b> Contestación del Defensor Oficial de Ausentes<br/>Responsable: Titular registral o citado<br/>10 días hábiles judiciales + gracia"]:::demandada
    USU_342["<b>USU_342</b> Contestación del Fisco de Estado y de la Municipalidad<br/>Responsable: Titular registral o citado<br/>10 días hábiles judiciales + gracia"]:::demandada
  end
  EXT_USU_060_origen["USU_060 Oposición de la usucapión como defensa en el juicio en contra del cliente<br/>(ver Etapa previa)"]:::externo
  EXT_USU_060_origen -.->|"Defensa opuesta: se ordena la anotación de litis"| USU_332
  EXT_USU_330_origen["USU_330 Radicación, control de admisibilidad y traslado de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_330_origen -.->|"Se ordena el traslado al titular con domicilio conocido"| USU_332
  EXT_USU_330_origen -.->|"Se ordena el traslado al titular con domicilio conocido"| USU_336
  EXT_USU_330_origen -.->|"Se ordena el traslado al titular con domicilio conocido"| USU_342
  EXT_USU_330_origen -.->|"Titular o domicilio ignorados: se piden informes"| USU_334
  EXT_USU_330_origen -.->|"Titular o domicilio ignorados: se piden informes"| USU_332
  EXT_USU_330_origen -.->|"Titular o domicilio ignorados: se piden informes"| USU_342
  FIN_USU_332_1(["Fin de este camino"]):::fin
  USU_332 -->|"Litis anotada"| FIN_USU_332_1
  USU_334 -->|"Informes negativos: se cita por edictos al titular y a los interesados"| USU_336
  P_USU_334_2(["Se abren en paralelo"]):::paralelo
  USU_334 -->|"Se encuentra el domicilio: se notifica al titular"| P_USU_334_2
  EXT_USU_340_destino["USU_340 Contestación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  P_USU_334_2 --> EXT_USU_340_destino
  P_USU_334_2 --> USU_336
  USU_336 -->|"Edictos publicados"| USU_338
  USU_338 -->|"Nadie comparece y el titular fue citado por edictos: interviene el Defensor Oficial"| USU_339
  FIN_USU_338_2(["Fin de este camino"]):::fin
  USU_338 -->|"Comparece un interesado, o el titular fue notificado en su domicilio"| FIN_USU_338_2
  EXT_USU_400_destino["USU_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  USU_339 -->|"Contestación del Defensor Oficial presentada o plazo vencido"| EXT_USU_400_destino
  FIN_USU_342_1(["Fin de este camino"]):::fin
  USU_342 -->|"Contestan o vence el plazo"| FIN_USU_342_1
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
    USU_400["<b>USU_400</b> Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_405["<b>USU_405</b> Reposición u oposición contra la providencia de prueba<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    USU_415["<b>USU_415</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    USU_420["<b>USU_420</b> Dictamen pericial<br/>Responsable: Juzgado u organismo<br/>5 días hábiles de anticipación"]:::tribunal
    USU_425["<b>USU_425</b> Traslado del dictamen pericial<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_430["<b>USU_430</b> Prueba informativa: contestación de los oficios<br/>Responsable: Juzgado u organismo<br/>10 días hábiles judiciales"]:::tribunal
    USU_435["<b>USU_435</b> Pedido de reiteración del oficio no contestado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_440["<b>USU_440</b> Audiencia de prueba o de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    USU_450["<b>USU_450</b> Alegatos<br/>Responsable: Cualquiera de las partes<br/>6 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_USU_339_origen["USU_339 Contestación del Defensor Oficial de Ausentes<br/>(ver Citaciones, edictos y anotación de litis)"]:::externo
  EXT_USU_339_origen -.->|"Contestación del Defensor Oficial presentada o plazo vencido"| USU_400
  EXT_USU_340_origen["USU_340 Contestación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_340_origen -.->|"No contesta en término"| USU_400
  EXT_USU_360_origen["USU_360 Traslado a la actora de la documental de la contestación<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_360_origen -.->|"Traslado contestado o plazo vencido"| USU_400
  P_USU_400_1(["Se abren en paralelo"]):::paralelo
  USU_400 -->|"Se provee la prueba ofrecida"| P_USU_400_1
  P_USU_400_1 --> USU_405
  P_USU_400_1 --> USU_420
  P_USU_400_1 --> USU_430
  P_USU_400_1 --> USU_440
  USU_400 -->|"Se fija audiencia preliminar"| USU_415
  EXT_USU_500_destino["USU_500 Llamamiento de autos y sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  USU_400 -->|"Causa declarada de puro derecho"| EXT_USU_500_destino
  FIN_USU_405_1(["Fin de este camino"]):::fin
  USU_405 -->|"Resuelta o plazo vencido"| FIN_USU_405_1
  EXT_USU_800_destino["USU_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  USU_415 -->|"Acuerdo conciliatorio en la audiencia"| EXT_USU_800_destino
  P_USU_415_2(["Se abren en paralelo"]):::paralelo
  USU_415 -->|"Se provee la prueba y se fija la audiencia de vista de causa"| P_USU_415_2
  P_USU_415_2 --> USU_405
  P_USU_415_2 --> USU_420
  P_USU_415_2 --> USU_430
  P_USU_415_2 --> USU_440
  USU_415 -->|"Causa declarada de puro derecho"| EXT_USU_500_destino
  USU_420 -->|"Dictamen presentado"| USU_425
  FIN_USU_420_2(["Fin de este camino"]):::fin
  USU_420 -->|"Pericia no ofrecida o desistida"| FIN_USU_420_2
  FIN_USU_425_1(["Fin de este camino"]):::fin
  USU_425 -->|"Observaciones presentadas o plazo vencido"| FIN_USU_425_1
  FIN_USU_430_1(["Fin de este camino"]):::fin
  USU_430 -->|"Informes contestados o prueba desistida"| FIN_USU_430_1
  USU_430 -->|"Plazo vencido sin respuesta"| USU_435
  USU_435 -->|"Reiteración pedida"| USU_430
  FIN_USU_435_2(["Fin de este camino"]):::fin
  USU_435 -->|"No se pide: prueba desistida"| FIN_USU_435_2
  USU_440 -->|"Audiencia realizada y prueba producida"| USU_450
  USU_440 -->|"Acuerdo conciliatorio en la audiencia"| EXT_USU_800_destino
  USU_450 -->|"Alegatos presentados o plazo vencido"| EXT_USU_500_destino
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
    USU_500["<b>USU_500</b> Llamamiento de autos y sentencia definitiva<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_505["<b>USU_505</b> Aclaratoria<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    USU_510["<b>USU_510</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_515["<b>USU_515</b> Pago de los honorarios firmes<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  subgraph F_1["Recursos"]
    USU_600["<b>USU_600</b> Recurso de apelación contra la sentencia definitiva<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_610["<b>USU_610</b> Expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_615["<b>USU_615</b> Contestación de la expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_620["<b>USU_620</b> Sentencia o resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_630["<b>USU_630</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    USU_640["<b>USU_640</b> Queja ante la SCBA por recurso denegado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    USU_645["<b>USU_645</b> Trámite y sentencia de la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    USU_650["<b>USU_650</b> Memorial del recurso concedido en relación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_USU_310_origen["USU_310 Beneficio de litigar sin gastos<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_310_origen -.->|"Beneficio denegado: se apela"| USU_650
  EXT_USU_320_origen["USU_320 Medidas cautelares<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_320_origen -.->|"Medida denegada o trabada: se apela"| USU_650
  EXT_USU_355_origen["USU_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_355_origen -.->|"Excepción admitida que pone fin al proceso: se apela"| USU_650
  EXT_USU_400_origen["USU_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  EXT_USU_400_origen -.->|"Causa declarada de puro derecho"| USU_500
  EXT_USU_415_origen["USU_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_USU_415_origen -.->|"Causa declarada de puro derecho"| USU_500
  EXT_USU_450_origen["USU_450 Alegatos<br/>(ver Prueba)"]:::externo
  EXT_USU_450_origen -.->|"Alegatos presentados o plazo vencido"| USU_500
  P_USU_500_1(["Se abren en paralelo"]):::paralelo
  USU_500 -->|"Sentencia notificada"| P_USU_500_1
  P_USU_500_1 --> USU_505
  P_USU_500_1 --> USU_510
  P_USU_500_1 --> USU_600
  FIN_USU_505_1(["Fin de este camino"]):::fin
  USU_505 -->|"Aclaratoria resuelta o plazo vencido"| FIN_USU_505_1
  USU_510 -->|"Regulación firme"| USU_515
  FIN_USU_515_1(["Fin de este camino"]):::fin
  USU_515 -->|"Honorarios pagados o en ejecución"| FIN_USU_515_1
  EXT_USU_750_destino["USU_750 Pedido de inscripción de la sentencia<br/>(ver Inscripción)"]:::externo
  USU_600 -->|"No se recurre: queda firme y hace lugar a la demanda"| EXT_USU_750_destino
  EXT_USU_990_destino["USU_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  USU_600 -->|"No se recurre: queda firme y rechaza la demanda"| EXT_USU_990_destino
  USU_600 -->|"Se interpone apelación"| USU_610
  USU_610 -->|"Agravios presentados"| USU_615
  USU_610 -->|"No expresa agravios: deserción"| USU_620
  USU_615 -->|"Contestados o plazo vencido"| USU_620
  USU_620 -->|"Sentencia de Cámara firme que hace lugar a la demanda"| EXT_USU_750_destino
  USU_620 -->|"Sentencia de Cámara firme que rechaza la demanda"| EXT_USU_990_destino
  FIN_USU_620_3(["Fin de este camino"]):::fin
  USU_620 -->|"Cámara resuelve la apelación de una resolución interlocutoria: sigue el trámite"| FIN_USU_620_3
  USU_620 -->|"Se interponen recursos extraordinarios"| USU_630
  USU_630 -->|"Recurso concedido"| USU_645
  USU_630 -->|"Recurso denegado"| USU_640
  USU_640 -->|"Queja admitida"| USU_645
  USU_640 -->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| EXT_USU_750_destino
  USU_640 -->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| EXT_USU_990_destino
  USU_645 -->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| EXT_USU_750_destino
  USU_645 -->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| EXT_USU_990_destino
  USU_645 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| USU_620
  USU_650 -->|"Memorial presentado o plazo vencido"| USU_620
  EXT_USU_800_origen["USU_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  EXT_USU_800_origen -.->|"Acuerdo homologado"| USU_510
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Inscripción

```mermaid
flowchart TD
  subgraph F_0["Inscripción"]
    USU_750["<b>USU_750</b> Pedido de inscripción de la sentencia<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
    USU_760["<b>USU_760</b> Inscripción en el Registro de la Propiedad<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    USU_770["<b>USU_770</b> Alta catastral y tributaria a nombre del cliente<br/>Responsable: Poseedor que representamos<br/>Sin plazo"]:::actora
  end
  EXT_USU_600_origen["USU_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_600_origen -.->|"No se recurre: queda firme y hace lugar a la demanda"| USU_750
  EXT_USU_620_origen["USU_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_620_origen -.->|"Sentencia de Cámara firme que hace lugar a la demanda"| USU_750
  EXT_USU_640_origen["USU_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_640_origen -.->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| USU_750
  EXT_USU_645_origen["USU_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| USU_750
  USU_750 -->|"Testimonio y oficio librados"| USU_760
  USU_760 -->|"Dominio inscripto a nombre del cliente"| USU_770
  USU_760 -->|"Documento observado: se subsana"| USU_750
  EXT_USU_990_destino["USU_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  USU_770 -->|"Trámites terminados"| EXT_USU_990_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Acuerdo

```mermaid
flowchart TD
  subgraph F_0["Acuerdo"]
    USU_800["<b>USU_800</b> Acuerdo, transacción o conciliación y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_USU_415_origen["USU_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_USU_415_origen -.->|"Acuerdo conciliatorio en la audiencia"| USU_800
  EXT_USU_440_origen["USU_440 Audiencia de prueba o de vista de causa<br/>(ver Prueba)"]:::externo
  EXT_USU_440_origen -.->|"Acuerdo conciliatorio en la audiencia"| USU_800
  P_USU_800_1(["Se abren en paralelo"]):::paralelo
  USU_800 -->|"Acuerdo homologado"| P_USU_800_1
  EXT_USU_990_destino["USU_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  P_USU_800_1 --> EXT_USU_990_destino
  EXT_USU_510_destino["USU_510 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_USU_800_1 --> EXT_USU_510_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    USU_900["<b>USU_900</b> Control de la caducidad de instancia<br/>Responsable: Poseedor que representamos<br/>3 meses"]:::actora
    USU_905["<b>USU_905</b> Intimación a activar el proceso<br/>Responsable: Poseedor que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    USU_990["<b>USU_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_USU_045_origen["USU_045 Evaluación de la regularización dominial de la Ley 24.374<br/>(ver Etapa previa)"]:::externo
  EXT_USU_045_origen -.->|"Se regulariza por la Ley 24.374"| USU_990
  EXT_USU_300_origen["USU_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_300_origen -.->|"Demanda presentada"| USU_900
  EXT_USU_300_origen -.->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| USU_900
  EXT_USU_300_origen -.->|"Demanda presentada con pedido de medida cautelar"| USU_900
  EXT_USU_330_origen["USU_330 Radicación, control de admisibilidad y traslado de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_330_origen -.->|"Demanda rechazada in limine o no subsanada"| USU_990
  EXT_USU_355_origen["USU_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_USU_355_origen -.->|"Excepción admitida y consentida"| USU_990
  EXT_USU_600_origen["USU_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_600_origen -.->|"No se recurre: queda firme y rechaza la demanda"| USU_990
  EXT_USU_620_origen["USU_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_620_origen -.->|"Sentencia de Cámara firme que rechaza la demanda"| USU_990
  EXT_USU_640_origen["USU_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_640_origen -.->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| USU_990
  EXT_USU_645_origen["USU_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_USU_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| USU_990
  EXT_USU_770_origen["USU_770 Alta catastral y tributaria a nombre del cliente<br/>(ver Inscripción)"]:::externo
  EXT_USU_770_origen -.->|"Trámites terminados"| USU_990
  EXT_USU_800_origen["USU_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  EXT_USU_800_origen -.->|"Acuerdo homologado"| USU_990
  FIN_USU_900_1(["Fin de este camino"]):::fin
  USU_900 -->|"Proceso terminado antes del vencimiento"| FIN_USU_900_1
  USU_900 -->|"Plazo vencido: se intima a activar el proceso"| USU_905
  FIN_USU_905_1(["Fin de este camino"]):::fin
  USU_905 -->|"Proceso activado en término"| FIN_USU_905_1
  USU_905 -->|"No se activa: se decreta la caducidad"| USU_990
  style USU_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
