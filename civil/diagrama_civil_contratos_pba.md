# Diagrama de Flujo: Incumplimiento contractual (compraventa, locación sin desalojo y fideicomiso) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68), juicio ordinario (art. 319); CCyC arts. 1031, 1077 a 1090, 1137 a 1171, 1201, 1666 a 1678; Ley 13.951 (mediación); Ley 24.240 · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_civil_contratos_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el contratante que reclama y al que representamos: comprador, vendedor, locatario, fiduciante, beneficiario o deudor que consigna (ACTORA); naranja = la contraparte incumplidora o el acreedor que no recibe el pago (DEMANDADA); gris = el juzgado, el mediador, el escribano o un registro (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la prescripción queda suspendida por la interpelación mientras corre el emplazamiento para cumplir.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>17 hitos"]
  FASE_2["Postulación<br/>9 hitos"]
  FASE_3["Prueba<br/>10 hitos"]
  FASE_4["Sentencia<br/>4 hitos"]
  FASE_5["Recursos<br/>8 hitos"]
  FASE_6["Ejecución<br/>7 hitos"]
  FASE_7["Acuerdo<br/>2 hitos"]
  FASE_8["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_8
  FASE_1 --> FASE_7
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
    CTR_010["INICIO - <b>CTR_010</b> Consulta inicial por el incumplimiento del contrato<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_015["<b>CTR_015</b> Control de prescripción de la acción<br/>Responsable: Contratante que representamos<br/>5 años"]:::actora
    CTR_017["<b>CTR_017</b> Suspensión de la prescripción por la interpelación fehaciente<br/>Responsable: Contratante que representamos<br/>6 meses"]:::actora
    CTR_020["<b>CTR_020</b> Elección entre exigir el cumplimiento o resolver el contrato<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_025["<b>CTR_025</b> Emplazamiento a cumplir bajo apercibimiento de resolución<br/>Responsable: Contraparte incumplidora<br/>15 días corridos"]:::demandada
    CTR_030["<b>CTR_030</b> Análisis de la compraventa: boleto, entrega, precio y escritura<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_032["<b>CTR_032</b> Citación a escriturar ante el escribano<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CTR_050["<b>CTR_050</b> Denuncia del defecto oculto al vendedor<br/>Responsable: Contratante que representamos<br/>60 días corridos"]:::actora
    CTR_052["<b>CTR_052</b> Prescripción del reclamo por vicios redhibitorios<br/>Responsable: Contratante que representamos<br/>1 año"]:::actora
    CTR_060["<b>CTR_060</b> Análisis del incumplimiento en la locación<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_062["<b>CTR_062</b> Plazo del locador para hacer las reparaciones<br/>Responsable: Contraparte incumplidora<br/>10 días corridos"]:::demandada
    CTR_070["<b>CTR_070</b> Rendición de cuentas del fiduciario<br/>Responsable: Contraparte incumplidora<br/>Sin plazo"]:::demandada
    CTR_080["<b>CTR_080</b> Requerimiento de mediación prejudicial obligatoria<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_082["<b>CTR_082</b> Audiencia de mediación<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CTR_084["<b>CTR_084</b> Plazo de la mediación<br/>Responsable: Juzgado u organismo<br/>60 días corridos"]:::tribunal
    CTR_086["<b>CTR_086</b> Reanudación de la prescripción después de la mediación<br/>Responsable: Contratante que representamos<br/>20 días corridos"]:::actora
    CTR_090["<b>CTR_090</b> Respuesta del acreedor a la consignación extrajudicial<br/>Responsable: Contraparte incumplidora<br/>5 días hábiles administrativos"]:::demandada
  end
  P_CTR_010_1(["Se abren en paralelo"]):::paralelo
  CTR_010 -->|"Compraventa"| P_CTR_010_1
  P_CTR_010_1 --> CTR_015
  P_CTR_010_1 --> CTR_030
  P_CTR_010_2(["Se abren en paralelo"]):::paralelo
  CTR_010 -->|"Locación sin desalojo"| P_CTR_010_2
  P_CTR_010_2 --> CTR_015
  P_CTR_010_2 --> CTR_060
  P_CTR_010_3(["Se abren en paralelo"]):::paralelo
  CTR_010 -->|"Fideicomiso"| P_CTR_010_3
  P_CTR_010_3 --> CTR_015
  P_CTR_010_3 --> CTR_070
  P_CTR_010_4(["Se abren en paralelo"]):::paralelo
  CTR_010 -->|"Otro contrato o relación de consumo"| P_CTR_010_4
  P_CTR_010_4 --> CTR_015
  P_CTR_010_4 --> CTR_020
  CTR_010 -->|"El cliente quiere pagar y el acreedor no recibe: consignación extrajudicial"| CTR_090
  EXT_CTR_300_destino["CTR_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  CTR_010 -->|"El cliente quiere pagar y el acreedor no recibe: consignación judicial"| EXT_CTR_300_destino
  FIN_CTR_015_1(["Fin de este camino"]):::fin
  CTR_015 -->|"Demanda presentada antes del vencimiento, o reclamo abandonado"| FIN_CTR_015_1
  FIN_CTR_017_1(["Fin de este camino"]):::fin
  CTR_017 -->|"Suspensión agotada o demanda presentada"| FIN_CTR_017_1
  P_CTR_020_1(["Se abren en paralelo"]):::paralelo
  CTR_020 -->|"Se emplaza a cumplir bajo apercibimiento de resolución"| P_CTR_020_1
  P_CTR_020_1 --> CTR_017
  P_CTR_020_1 --> CTR_025
  CTR_020 -->|"Hay cláusula resolutoria expresa: se comunica la resolución"| CTR_080
  CTR_020 -->|"Se pide la mediación para exigir el cumplimiento o los daños"| CTR_080
  EXT_CTR_990_destino["CTR_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  CTR_025 -->|"Cumple en el plazo"| EXT_CTR_990_destino
  CTR_025 -->|"No cumple: el contrato queda resuelto"| CTR_080
  CTR_030 -->|"Falta la escritura: se cita a escriturar"| CTR_032
  CTR_030 -->|"Falta la entrega de la cosa o el pago del precio"| CTR_020
  CTR_030 -->|"La cosa tiene defectos ocultos"| CTR_050
  CTR_032 -->|"Se otorga la escritura"| EXT_CTR_990_destino
  CTR_032 -->|"La contraparte no comparece o se niega"| CTR_080
  P_CTR_050_1(["Se abren en paralelo"]):::paralelo
  CTR_050 -->|"Defecto denunciado en término"| P_CTR_050_1
  P_CTR_050_1 --> CTR_020
  P_CTR_050_1 --> CTR_052
  FIN_CTR_050_2(["Fin de este camino"]):::fin
  CTR_050 -->|"Vencido sin denuncia: se evalúa si el vendedor conocía el defecto"| FIN_CTR_050_2
  FIN_CTR_052_1(["Fin de este camino"]):::fin
  CTR_052 -->|"Demanda presentada o reclamo resuelto"| FIN_CTR_052_1
  CTR_060 -->|"Reparación no urgente: se intima al locador"| CTR_062
  CTR_060 -->|"Otro incumplimiento: se elige cumplimiento o resolución"| CTR_020
  CTR_062 -->|"El locador repara"| EXT_CTR_990_destino
  CTR_062 -->|"No repara: el locatario repara a su cargo o resuelve"| CTR_020
  CTR_070 -->|"Rinde cuentas en forma satisfactoria"| EXT_CTR_990_destino
  CTR_070 -->|"No rinde o hay incumplimiento grave: se reclama o se pide la remoción"| CTR_080
  P_CTR_080_1(["Se abren en paralelo"]):::paralelo
  CTR_080 -->|"Mediador designado y audiencia fijada"| P_CTR_080_1
  P_CTR_080_1 --> CTR_082
  P_CTR_080_1 --> CTR_084
  FIN_CTR_082_1(["Fin de este camino"]):::fin
  CTR_082 -->|"Audiencia realizada"| FIN_CTR_082_1
  EXT_CTR_800_destino["CTR_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  CTR_084 -->|"Acuerdo en la mediación"| EXT_CTR_800_destino
  P_CTR_084_2(["Se abren en paralelo"]):::paralelo
  CTR_084 -->|"Cierre sin acuerdo o por incomparecencia"| P_CTR_084_2
  P_CTR_084_2 --> EXT_CTR_300_destino
  P_CTR_084_2 --> CTR_086
  FIN_CTR_086_1(["Fin de este camino"]):::fin
  CTR_086 -->|"Demanda presentada"| FIN_CTR_086_1
  CTR_090 -->|"Acepta o retira el depósito"| EXT_CTR_990_destino
  CTR_090 -->|"Rechaza o no se expide: se consigna judicialmente"| EXT_CTR_300_destino
  style CTR_010 stroke-width:3px
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
    CTR_300["<b>CTR_300</b> Presentación de la demanda<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_310["<b>CTR_310</b> Beneficio de litigar sin gastos<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_320["<b>CTR_320</b> Medidas cautelares<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_330["<b>CTR_330</b> Radicación, control de admisibilidad y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CTR_340["<b>CTR_340</b> Contestación de la demanda<br/>Responsable: Contraparte incumplidora<br/>15 días hábiles judiciales + gracia"]:::demandada
    CTR_350["<b>CTR_350</b> Excepciones de previo y especial pronunciamiento<br/>Responsable: Contraparte incumplidora<br/>10 días hábiles judiciales + gracia"]:::demandada
    CTR_355["<b>CTR_355</b> Traslado a la actora de las excepciones previas<br/>Responsable: Contratante que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    CTR_360["<b>CTR_360</b> Traslado a la actora de la documental de la contestación<br/>Responsable: Contratante que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    CTR_370["<b>CTR_370</b> Contestación de la reconvención<br/>Responsable: Contratante que representamos<br/>15 días hábiles judiciales + gracia"]:::actora
  end
  EXT_CTR_010_origen["CTR_010 Consulta inicial por el incumplimiento del contrato<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_010_origen -.->|"El cliente quiere pagar y el acreedor no recibe: consignación judicial"| CTR_300
  EXT_CTR_084_origen["CTR_084 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_084_origen -.->|"Cierre sin acuerdo o por incomparecencia"| CTR_300
  EXT_CTR_090_origen["CTR_090 Respuesta del acreedor a la consignación extrajudicial<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_090_origen -.->|"Rechaza o no se expide: se consigna judicialmente"| CTR_300
  P_CTR_300_1(["Se abren en paralelo"]):::paralelo
  CTR_300 -->|"Demanda presentada"| P_CTR_300_1
  P_CTR_300_1 --> CTR_330
  EXT_CTR_900_destino["CTR_900 Control de la caducidad de instancia<br/>(ver Cierre)"]:::externo
  P_CTR_300_1 --> EXT_CTR_900_destino
  P_CTR_300_2(["Se abren en paralelo"]):::paralelo
  CTR_300 -->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| P_CTR_300_2
  P_CTR_300_2 --> CTR_330
  P_CTR_300_2 --> CTR_310
  P_CTR_300_2 --> EXT_CTR_900_destino
  P_CTR_300_3(["Se abren en paralelo"]):::paralelo
  CTR_300 -->|"Demanda presentada con pedido de medida cautelar"| P_CTR_300_3
  P_CTR_300_3 --> CTR_330
  P_CTR_300_3 --> CTR_320
  P_CTR_300_3 --> EXT_CTR_900_destino
  FIN_CTR_310_1(["Fin de este camino"]):::fin
  CTR_310 -->|"Beneficio concedido, o denegado sin recurso (se integran tasa y aportes)"| FIN_CTR_310_1
  EXT_CTR_650_destino["CTR_650 Memorial del recurso concedido en relación<br/>(ver Sentencia y recursos)"]:::externo
  CTR_310 -->|"Beneficio denegado: se apela"| EXT_CTR_650_destino
  FIN_CTR_320_1(["Fin de este camino"]):::fin
  CTR_320 -->|"Medida trabada o denegada sin recurso"| FIN_CTR_320_1
  CTR_320 -->|"Medida denegada o trabada: se apela"| EXT_CTR_650_destino
  EXT_CTR_990_destino["CTR_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  CTR_330 -->|"Demanda rechazada in limine o no subsanada"| EXT_CTR_990_destino
  P_CTR_330_2(["Se abren en paralelo"]):::paralelo
  CTR_330 -->|"Se ordena el traslado de la demanda"| P_CTR_330_2
  P_CTR_330_2 --> CTR_340
  P_CTR_330_2 --> CTR_350
  CTR_340 -->|"Contesta la demanda"| CTR_360
  P_CTR_340_2(["Se abren en paralelo"]):::paralelo
  CTR_340 -->|"Contesta y reconviene"| P_CTR_340_2
  P_CTR_340_2 --> CTR_360
  P_CTR_340_2 --> CTR_370
  EXT_CTR_400_destino["CTR_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  CTR_340 -->|"No contesta en término"| EXT_CTR_400_destino
  CTR_350 -->|"Se oponen excepciones previas"| CTR_355
  FIN_CTR_350_2(["Fin de este camino"]):::fin
  CTR_350 -->|"No se oponen excepciones previas"| FIN_CTR_350_2
  FIN_CTR_355_1(["Fin de este camino"]):::fin
  CTR_355 -->|"Excepciones rechazadas o diferidas para la sentencia"| FIN_CTR_355_1
  CTR_355 -->|"Excepción admitida que pone fin al proceso: se apela"| EXT_CTR_650_destino
  CTR_355 -->|"Excepción admitida y consentida"| EXT_CTR_990_destino
  CTR_360 -->|"Traslado contestado o plazo vencido"| EXT_CTR_400_destino
  FIN_CTR_370_1(["Fin de este camino"]):::fin
  CTR_370 -->|"Reconvención contestada o plazo vencido"| FIN_CTR_370_1
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
    CTR_400["<b>CTR_400</b> Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CTR_405["<b>CTR_405</b> Reposición u oposición contra la providencia de prueba<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    CTR_410["<b>CTR_410</b> Ofrecimiento de prueba<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CTR_415["<b>CTR_415</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CTR_420["<b>CTR_420</b> Dictamen pericial<br/>Responsable: Juzgado u organismo<br/>30 días hábiles judiciales"]:::tribunal
    CTR_425["<b>CTR_425</b> Traslado del dictamen pericial<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CTR_430["<b>CTR_430</b> Prueba informativa: contestación de los oficios<br/>Responsable: Juzgado u organismo<br/>10 días hábiles judiciales"]:::tribunal
    CTR_435["<b>CTR_435</b> Pedido de reiteración del oficio no contestado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CTR_440["<b>CTR_440</b> Audiencia de prueba o de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    CTR_450["<b>CTR_450</b> Alegatos<br/>Responsable: Cualquiera de las partes<br/>6 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_CTR_340_origen["CTR_340 Contestación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_340_origen -.->|"No contesta en término"| CTR_400
  EXT_CTR_360_origen["CTR_360 Traslado a la actora de la documental de la contestación<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_360_origen -.->|"Traslado contestado o plazo vencido"| CTR_400
  P_CTR_400_1(["Se abren en paralelo"]):::paralelo
  CTR_400 -->|"Se abre a prueba"| P_CTR_400_1
  P_CTR_400_1 --> CTR_405
  P_CTR_400_1 --> CTR_410
  EXT_CTR_500_destino["CTR_500 Llamamiento de autos y sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  CTR_400 -->|"Causa declarada de puro derecho"| EXT_CTR_500_destino
  FIN_CTR_405_1(["Fin de este camino"]):::fin
  CTR_405 -->|"Resuelta o plazo vencido"| FIN_CTR_405_1
  CTR_410 -->|"Prueba ofrecida: se fija audiencia preliminar"| CTR_415
  P_CTR_410_2(["Se abren en paralelo"]):::paralelo
  CTR_410 -->|"Prueba ofrecida y proveída sin audiencia preliminar"| P_CTR_410_2
  P_CTR_410_2 --> CTR_420
  P_CTR_410_2 --> CTR_430
  P_CTR_410_2 --> CTR_440
  EXT_CTR_800_destino["CTR_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  CTR_415 -->|"Acuerdo conciliatorio en la audiencia"| EXT_CTR_800_destino
  P_CTR_415_2(["Se abren en paralelo"]):::paralelo
  CTR_415 -->|"Se provee la prueba y se fija la audiencia de vista de causa"| P_CTR_415_2
  P_CTR_415_2 --> CTR_405
  P_CTR_415_2 --> CTR_420
  P_CTR_415_2 --> CTR_430
  P_CTR_415_2 --> CTR_440
  CTR_415 -->|"Causa declarada de puro derecho"| EXT_CTR_500_destino
  CTR_420 -->|"Dictamen presentado"| CTR_425
  FIN_CTR_420_2(["Fin de este camino"]):::fin
  CTR_420 -->|"Pericia no ofrecida o desistida"| FIN_CTR_420_2
  FIN_CTR_425_1(["Fin de este camino"]):::fin
  CTR_425 -->|"Observaciones presentadas o plazo vencido"| FIN_CTR_425_1
  FIN_CTR_430_1(["Fin de este camino"]):::fin
  CTR_430 -->|"Informes contestados o prueba desistida"| FIN_CTR_430_1
  CTR_430 -->|"Plazo vencido sin respuesta"| CTR_435
  CTR_435 -->|"Reiteración pedida"| CTR_430
  FIN_CTR_435_2(["Fin de este camino"]):::fin
  CTR_435 -->|"No se pide: prueba desistida"| FIN_CTR_435_2
  CTR_440 -->|"Audiencia realizada y prueba producida"| CTR_450
  CTR_440 -->|"Acuerdo conciliatorio en la audiencia"| EXT_CTR_800_destino
  CTR_450 -->|"Alegatos presentados o plazo vencido"| EXT_CTR_500_destino
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
    CTR_500["<b>CTR_500</b> Llamamiento de autos y sentencia definitiva<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CTR_505["<b>CTR_505</b> Aclaratoria<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    CTR_510["<b>CTR_510</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CTR_515["<b>CTR_515</b> Pago de los honorarios firmes<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  subgraph F_1["Recursos"]
    CTR_600["<b>CTR_600</b> Recurso de apelación contra la sentencia definitiva<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CTR_610["<b>CTR_610</b> Expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CTR_615["<b>CTR_615</b> Contestación de la expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CTR_620["<b>CTR_620</b> Sentencia o resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    CTR_630["<b>CTR_630</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CTR_640["<b>CTR_640</b> Queja ante la SCBA por recurso denegado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    CTR_645["<b>CTR_645</b> Trámite y sentencia de la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    CTR_650["<b>CTR_650</b> Memorial del recurso concedido en relación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_CTR_310_origen["CTR_310 Beneficio de litigar sin gastos<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_310_origen -.->|"Beneficio denegado: se apela"| CTR_650
  EXT_CTR_320_origen["CTR_320 Medidas cautelares<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_320_origen -.->|"Medida denegada o trabada: se apela"| CTR_650
  EXT_CTR_355_origen["CTR_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_355_origen -.->|"Excepción admitida que pone fin al proceso: se apela"| CTR_650
  EXT_CTR_400_origen["CTR_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  EXT_CTR_400_origen -.->|"Causa declarada de puro derecho"| CTR_500
  EXT_CTR_415_origen["CTR_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_CTR_415_origen -.->|"Causa declarada de puro derecho"| CTR_500
  EXT_CTR_450_origen["CTR_450 Alegatos<br/>(ver Prueba)"]:::externo
  EXT_CTR_450_origen -.->|"Alegatos presentados o plazo vencido"| CTR_500
  P_CTR_500_1(["Se abren en paralelo"]):::paralelo
  CTR_500 -->|"Sentencia notificada"| P_CTR_500_1
  P_CTR_500_1 --> CTR_505
  P_CTR_500_1 --> CTR_510
  P_CTR_500_1 --> CTR_600
  FIN_CTR_505_1(["Fin de este camino"]):::fin
  CTR_505 -->|"Aclaratoria resuelta o plazo vencido"| FIN_CTR_505_1
  CTR_510 -->|"Regulación firme"| CTR_515
  FIN_CTR_515_1(["Fin de este camino"]):::fin
  CTR_515 -->|"Honorarios pagados o en ejecución"| FIN_CTR_515_1
  EXT_CTR_700_destino["CTR_700 Liquidación<br/>(ver Ejecución)"]:::externo
  CTR_600 -->|"No se recurre: queda firme y hace lugar a la demanda"| EXT_CTR_700_destino
  EXT_CTR_990_destino["CTR_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  CTR_600 -->|"No se recurre: queda firme y rechaza la demanda"| EXT_CTR_990_destino
  CTR_600 -->|"Se interpone apelación"| CTR_610
  EXT_CTR_735_destino["CTR_735 Plazo para escriturar fijado en la sentencia<br/>(ver Ejecución)"]:::externo
  CTR_600 -->|"No se recurre: queda firme la condena a escriturar"| EXT_CTR_735_destino
  CTR_610 -->|"Agravios presentados"| CTR_615
  CTR_610 -->|"No expresa agravios: deserción"| CTR_620
  CTR_615 -->|"Contestados o plazo vencido"| CTR_620
  CTR_620 -->|"Sentencia de Cámara firme que hace lugar a la demanda"| EXT_CTR_700_destino
  CTR_620 -->|"Sentencia de Cámara firme que rechaza la demanda"| EXT_CTR_990_destino
  FIN_CTR_620_3(["Fin de este camino"]):::fin
  CTR_620 -->|"Cámara resuelve la apelación de una resolución interlocutoria: sigue el trámite"| FIN_CTR_620_3
  CTR_620 -->|"Se interponen recursos extraordinarios"| CTR_630
  CTR_620 -->|"Cámara: queda firme la condena a escriturar"| EXT_CTR_735_destino
  CTR_630 -->|"Recurso concedido"| CTR_645
  CTR_630 -->|"Recurso denegado"| CTR_640
  CTR_640 -->|"Queja admitida"| CTR_645
  CTR_640 -->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| EXT_CTR_700_destino
  CTR_640 -->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| EXT_CTR_990_destino
  CTR_640 -->|"Queja rechazada: queda firme la condena a escriturar"| EXT_CTR_735_destino
  CTR_645 -->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| EXT_CTR_700_destino
  CTR_645 -->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| EXT_CTR_990_destino
  CTR_645 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| CTR_620
  CTR_645 -->|"La SCBA resuelve: queda firme la condena a escriturar"| EXT_CTR_735_destino
  CTR_650 -->|"Memorial presentado o plazo vencido"| CTR_620
  EXT_CTR_800_origen["CTR_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  EXT_CTR_800_origen -.->|"Acuerdo homologado"| CTR_510
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
    CTR_700["<b>CTR_700</b> Liquidación<br/>Responsable: Contratante que representamos<br/>10 días hábiles judiciales + gracia"]:::actora
    CTR_705["<b>CTR_705</b> Traslado de la liquidación<br/>Responsable: Contraparte incumplidora<br/>5 días hábiles judiciales + gracia"]:::demandada
    CTR_710["<b>CTR_710</b> Embargo y citación de venta<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_720["<b>CTR_720</b> Excepciones del ejecutado<br/>Responsable: Contraparte incumplidora<br/>5 días hábiles judiciales + gracia"]:::demandada
    CTR_730["<b>CTR_730</b> Cobro y rendición al cliente<br/>Responsable: Contratante que representamos<br/>Sin plazo"]:::actora
    CTR_735["<b>CTR_735</b> Plazo para escriturar fijado en la sentencia<br/>Responsable: Contraparte incumplidora<br/>Sin plazo"]:::demandada
    CTR_740["<b>CTR_740</b> Escrituración por el juez a costa del obligado<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_CTR_600_origen["CTR_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_600_origen -.->|"No se recurre: queda firme y hace lugar a la demanda"| CTR_700
  EXT_CTR_600_origen -.->|"No se recurre: queda firme la condena a escriturar"| CTR_735
  EXT_CTR_620_origen["CTR_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_620_origen -.->|"Sentencia de Cámara firme que hace lugar a la demanda"| CTR_700
  EXT_CTR_620_origen -.->|"Cámara: queda firme la condena a escriturar"| CTR_735
  EXT_CTR_640_origen["CTR_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_640_origen -.->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| CTR_700
  EXT_CTR_640_origen -.->|"Queja rechazada: queda firme la condena a escriturar"| CTR_735
  EXT_CTR_645_origen["CTR_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| CTR_700
  EXT_CTR_645_origen -.->|"La SCBA resuelve: queda firme la condena a escriturar"| CTR_735
  CTR_700 -->|"Liquidación presentada"| CTR_705
  CTR_705 -->|"Liquidación aprobada y pagada en término"| CTR_730
  CTR_705 -->|"Liquidación aprobada y no pagada"| CTR_710
  CTR_710 -->|"Embargo trabado y citación de venta notificada"| CTR_720
  CTR_720 -->|"Sin excepciones o excepciones rechazadas: fondos embargados o bienes subastados"| CTR_730
  EXT_CTR_990_destino["CTR_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  CTR_720 -->|"Excepción de pago admitida"| EXT_CTR_990_destino
  CTR_730 -->|"Cobro percibido y rendido al cliente"| EXT_CTR_990_destino
  CTR_735 -->|"El obligado escritura"| EXT_CTR_990_destino
  CTR_735 -->|"No escritura en el plazo: firma el juez"| CTR_740
  CTR_740 -->|"Escritura otorgada e inscripta"| EXT_CTR_990_destino
  EXT_CTR_805_origen["CTR_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_CTR_805_origen -.->|"Acuerdo incumplido: se ejecuta"| CTR_710
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
    CTR_800["<b>CTR_800</b> Acuerdo, transacción o conciliación y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    CTR_805["<b>CTR_805</b> Cumplimiento del acuerdo homologado<br/>Responsable: Contraparte incumplidora<br/>Sin plazo"]:::demandada
  end
  EXT_CTR_084_origen["CTR_084 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_084_origen -.->|"Acuerdo en la mediación"| CTR_800
  EXT_CTR_415_origen["CTR_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_CTR_415_origen -.->|"Acuerdo conciliatorio en la audiencia"| CTR_800
  EXT_CTR_440_origen["CTR_440 Audiencia de prueba o de vista de causa<br/>(ver Prueba)"]:::externo
  EXT_CTR_440_origen -.->|"Acuerdo conciliatorio en la audiencia"| CTR_800
  P_CTR_800_1(["Se abren en paralelo"]):::paralelo
  CTR_800 -->|"Acuerdo homologado"| P_CTR_800_1
  P_CTR_800_1 --> CTR_805
  EXT_CTR_510_destino["CTR_510 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_CTR_800_1 --> EXT_CTR_510_destino
  EXT_CTR_990_destino["CTR_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  CTR_805 -->|"Acuerdo cumplido"| EXT_CTR_990_destino
  EXT_CTR_710_destino["CTR_710 Embargo y citación de venta<br/>(ver Ejecución)"]:::externo
  CTR_805 -->|"Acuerdo incumplido: se ejecuta"| EXT_CTR_710_destino
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
    CTR_900["<b>CTR_900</b> Control de la caducidad de instancia<br/>Responsable: Contratante que representamos<br/>6 meses"]:::actora
    CTR_905["<b>CTR_905</b> Intimación a activar el proceso<br/>Responsable: Contratante que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
    CTR_990["<b>CTR_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_CTR_025_origen["CTR_025 Emplazamiento a cumplir bajo apercibimiento de resolución<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_025_origen -.->|"Cumple en el plazo"| CTR_990
  EXT_CTR_032_origen["CTR_032 Citación a escriturar ante el escribano<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_032_origen -.->|"Se otorga la escritura"| CTR_990
  EXT_CTR_062_origen["CTR_062 Plazo del locador para hacer las reparaciones<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_062_origen -.->|"El locador repara"| CTR_990
  EXT_CTR_070_origen["CTR_070 Rendición de cuentas del fiduciario<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_070_origen -.->|"Rinde cuentas en forma satisfactoria"| CTR_990
  EXT_CTR_090_origen["CTR_090 Respuesta del acreedor a la consignación extrajudicial<br/>(ver Etapa previa)"]:::externo
  EXT_CTR_090_origen -.->|"Acepta o retira el depósito"| CTR_990
  EXT_CTR_300_origen["CTR_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_300_origen -.->|"Demanda presentada"| CTR_900
  EXT_CTR_300_origen -.->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| CTR_900
  EXT_CTR_300_origen -.->|"Demanda presentada con pedido de medida cautelar"| CTR_900
  EXT_CTR_330_origen["CTR_330 Radicación, control de admisibilidad y traslado de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_330_origen -.->|"Demanda rechazada in limine o no subsanada"| CTR_990
  EXT_CTR_355_origen["CTR_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_CTR_355_origen -.->|"Excepción admitida y consentida"| CTR_990
  EXT_CTR_600_origen["CTR_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_600_origen -.->|"No se recurre: queda firme y rechaza la demanda"| CTR_990
  EXT_CTR_620_origen["CTR_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_620_origen -.->|"Sentencia de Cámara firme que rechaza la demanda"| CTR_990
  EXT_CTR_640_origen["CTR_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_640_origen -.->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| CTR_990
  EXT_CTR_645_origen["CTR_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_CTR_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| CTR_990
  EXT_CTR_720_origen["CTR_720 Excepciones del ejecutado<br/>(ver Ejecución)"]:::externo
  EXT_CTR_720_origen -.->|"Excepción de pago admitida"| CTR_990
  EXT_CTR_730_origen["CTR_730 Cobro y rendición al cliente<br/>(ver Ejecución)"]:::externo
  EXT_CTR_730_origen -.->|"Cobro percibido y rendido al cliente"| CTR_990
  EXT_CTR_735_origen["CTR_735 Plazo para escriturar fijado en la sentencia<br/>(ver Ejecución)"]:::externo
  EXT_CTR_735_origen -.->|"El obligado escritura"| CTR_990
  EXT_CTR_740_origen["CTR_740 Escrituración por el juez a costa del obligado<br/>(ver Ejecución)"]:::externo
  EXT_CTR_740_origen -.->|"Escritura otorgada e inscripta"| CTR_990
  EXT_CTR_805_origen["CTR_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_CTR_805_origen -.->|"Acuerdo cumplido"| CTR_990
  FIN_CTR_900_1(["Fin de este camino"]):::fin
  CTR_900 -->|"Proceso terminado antes del vencimiento"| FIN_CTR_900_1
  CTR_900 -->|"Plazo vencido: se intima a activar el proceso"| CTR_905
  FIN_CTR_905_1(["Fin de este camino"]):::fin
  CTR_905 -->|"Proceso activado en término"| FIN_CTR_905_1
  CTR_905 -->|"No se activa: se decreta la caducidad"| CTR_990
  style CTR_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
