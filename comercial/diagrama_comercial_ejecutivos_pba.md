# Diagrama de Flujo: Juicios ejecutivos y cobro de pesos - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68), arts. 518 a 593 (juicio ejecutivo) y 484 a 495 (sumario); Ley 24.452 (cheques); Decreto-Ley 5965/63 (pagaré); Ley 25.065 (tarjetas de crédito); Ley 27.440 (factura de crédito electrónica); Ley 13.951 (mediación) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_comercial_ejecutivos_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = acreedor ejecutante; naranja = deudor ejecutado (librador, suscriptor, avalistas o endosantes); gris = juzgado, oficial de justicia o martillero; violeta = cualquiera de las partes.
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, al presentar la demanda corre la caducidad de instancia mientras avanza la ejecución.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Hitos "Sigue en la matriz de ...":** son finales. El expediente continúa con el flujo de otra matriz comercial y hay que vincular los dos expedientes en la app (ver las dudas de producto de la matriz de concursos).
* **Dos puertas al juicio:** el juicio ejecutivo (título que trae aparejada ejecución) y el cobro de pesos por juicio sumario (sin título ejecutivo o con la vía ejecutiva frustrada). Las dos terminan en la sentencia firme y comparten la ejecución, la subasta y el cierre.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>6 hitos"]
  FASE_2["Preparación<br/>4 hitos"]
  FASE_3["Intimación y excepciones<br/>5 hitos"]
  FASE_4["Postulación<br/>2 hitos"]
  FASE_5["Prueba<br/>3 hitos"]
  FASE_6["Sentencia<br/>2 hitos"]
  FASE_7["Recursos<br/>7 hitos"]
  FASE_8["Ejecución<br/>12 hitos"]
  FASE_9["Acuerdo<br/>1 hito"]
  FASE_10["Cierre<br/>5 hitos"]
  FASE_1 --> FASE_10
  FASE_1 --> FASE_2
  FASE_1 --> FASE_4
  FASE_1 --> FASE_9
  FASE_2 --> FASE_3
  FASE_2 --> FASE_10
  FASE_2 --> FASE_4
  FASE_3 --> FASE_8
  FASE_3 --> FASE_10
  FASE_3 --> FASE_7
  FASE_3 --> FASE_6
  FASE_7 --> FASE_8
  FASE_7 --> FASE_6
  FASE_4 --> FASE_10
  FASE_4 --> FASE_5
  FASE_4 --> FASE_6
  FASE_4 --> FASE_9
  FASE_5 --> FASE_9
  FASE_5 --> FASE_6
  FASE_6 --> FASE_7
  FASE_6 --> FASE_10
  FASE_6 --> FASE_8
  FASE_8 --> FASE_10
  FASE_9 --> FASE_10
  FASE_9 --> FASE_8
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    EJE_010["INICIO - <b>EJE_010</b> Mora del deudor y elección de la vía<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_020["<b>EJE_020</b> Aviso del rechazo del cheque al librador y endosantes<br/>Responsable: Acreedor ejecutante<br/>2 días hábiles administrativos"]:::actora
    EJE_025["<b>EJE_025</b> Protesto del pagaré por falta de pago<br/>Responsable: Acreedor ejecutante<br/>2 días hábiles administrativos"]:::actora
    EJE_030["<b>EJE_030</b> Control de la prescripción de la acción<br/>Responsable: Acreedor ejecutante<br/>1 año"]:::actora
    EJE_040["<b>EJE_040</b> Intimación extrajudicial de pago<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_050["<b>EJE_050</b> Mediación prejudicial<br/>Responsable: Ambas partes<br/>30 días corridos"]:::ambas
  end
  EJE_010 -->|"Cheque o echeq rechazado"| EJE_020
  EJE_010 -->|"Pagaré sin cláusula 'sin protesto'"| EJE_025
  EJE_010 -->|"Pagaré 'sin protesto', tarjeta, factura de crédito electrónica u otro título"| EJE_030
  EJE_010 -->|"Crédito sin título ejecutivo (cobro de pesos)"| EJE_030
  EXT_EJE_995_destino["EJE_995 Sigue en la matriz de concursos y quiebras<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_010 -->|"El deudor está concursado o en quiebra"| EXT_EJE_995_destino
  EJE_020 -->|"Aviso enviado"| EJE_030
  EJE_025 -->|"Protesto hecho y avisos enviados"| EJE_030
  EJE_030 -->|"Acción vigente"| EJE_040
  FIN_EJE_030_2(["Fin de este camino"]):::fin
  EJE_030 -->|"Todas las acciones prescriptas: no se inicia el reclamo"| FIN_EJE_030_2
  EXT_EJE_100_destino["EJE_100 Presentación de la demanda ejecutiva<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EJE_040 -->|"Sin pago: juicio ejecutivo sin mediación (optativa, art. 5 Ley 13.951)"| EXT_EJE_100_destino
  EJE_040 -->|"Sin pago: se opta por la mediación o es cobro de pesos (obligatoria)"| EJE_050
  EXT_EJE_105_destino["EJE_105 Embargo preventivo previo: presentar la demanda<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EJE_040 -->|"Riesgo de insolvencia: embargo preventivo antes de demandar"| EXT_EJE_105_destino
  FIN_EJE_040_4(["Fin de este camino"]):::fin
  EJE_040 -->|"Pago total"| FIN_EJE_040_4
  EJE_050 -->|"Mediación cerrada sin acuerdo y hay título ejecutivo"| EXT_EJE_100_destino
  EXT_EJE_300_destino["EJE_300 Presentación de la demanda de cobro de pesos (juicio sumario)<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EJE_050 -->|"Mediación cerrada sin acuerdo en el cobro de pesos"| EXT_EJE_300_destino
  EXT_EJE_900_destino["EJE_900 Acuerdo, transacción o conciliación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_050 -->|"Acuerdo en la mediación"| EXT_EJE_900_destino
  style EJE_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Juicio ejecutivo: demanda y preparación de la vía

```mermaid
flowchart TD
  subgraph F_0["Preparación"]
    EJE_100["<b>EJE_100</b> Presentación de la demanda ejecutiva<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_105["<b>EJE_105</b> Embargo preventivo previo: presentar la demanda<br/>Responsable: Acreedor ejecutante<br/>10 días hábiles judiciales + gracia"]:::actora
    EJE_110["<b>EJE_110</b> Audiencia de reconocimiento de firma o de documentos<br/>Responsable: Deudor ejecutado<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    EJE_120["<b>EJE_120</b> Promover la ejecución después de la preparación<br/>Responsable: Acreedor ejecutante<br/>15 días hábiles judiciales + gracia"]:::actora
  end
  EXT_EJE_040_origen["EJE_040 Intimación extrajudicial de pago<br/>(ver Etapa previa)"]:::externo
  EXT_EJE_040_origen -.->|"Sin pago: juicio ejecutivo sin mediación (optativa, art. 5 Ley 13.951)"| EJE_100
  EXT_EJE_040_origen -.->|"Riesgo de insolvencia: embargo preventivo antes de demandar"| EJE_105
  EXT_EJE_050_origen["EJE_050 Mediación prejudicial<br/>(ver Etapa previa)"]:::externo
  EXT_EJE_050_origen -.->|"Mediación cerrada sin acuerdo y hay título ejecutivo"| EJE_100
  P_EJE_100_1(["Se abren en paralelo"]):::paralelo
  EJE_100 -->|"Título que trae aparejada ejecución"| P_EJE_100_1
  EXT_EJE_200_destino["EJE_200 Mandamiento de intimación de pago y embargo<br/>(ver Juicio ejecutivo: intimación, excepciones y sentencia de remate)"]:::externo
  P_EJE_100_1 --> EXT_EJE_200_destino
  EXT_EJE_950_destino["EJE_950 Control de caducidad de instancia<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  P_EJE_100_1 --> EXT_EJE_950_destino
  P_EJE_100_2(["Se abren en paralelo"]):::paralelo
  EJE_100 -->|"Título que requiere preparación (firma, tarjeta de crédito)"| P_EJE_100_2
  P_EJE_100_2 --> EJE_110
  P_EJE_100_2 --> EXT_EJE_950_destino
  EJE_105 -->|"Demanda ejecutiva presentada"| EJE_100
  EXT_EJE_300_destino["EJE_300 Presentación de la demanda de cobro de pesos (juicio sumario)<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EJE_105 -->|"Demanda de cobro de pesos presentada"| EXT_EJE_300_destino
  EJE_110 -->|"Firma reconocida, tenida por reconocida o declarada auténtica"| EJE_120
  EJE_110 -->|"Firma declarada no auténtica o vía no preparada: queda el cobro de pesos"| EXT_EJE_300_destino
  EJE_120 -->|"Ejecución promovida"| EXT_EJE_200_destino
  EJE_120 -->|"Caducaron las medidas preparatorias"| EXT_EJE_300_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Juicio ejecutivo: intimación, excepciones y sentencia de remate

```mermaid
flowchart TD
  subgraph F_0["Intimación y excepciones"]
    EJE_200["<b>EJE_200</b> Mandamiento de intimación de pago y embargo<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_220["<b>EJE_220</b> Oposición de excepciones<br/>Responsable: Deudor ejecutado<br/>5 días hábiles judiciales + gracia"]:::demandada
    EJE_230["<b>EJE_230</b> Contestación del traslado de las excepciones<br/>Responsable: Acreedor ejecutante<br/>5 días hábiles judiciales + gracia"]:::actora
    EJE_240["<b>EJE_240</b> Producción de la prueba de las excepciones<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    EJE_250["<b>EJE_250</b> Sentencia de remate<br/>Responsable: Juzgado<br/>10 días hábiles judiciales"]:::tribunal
  end
  EXT_EJE_100_origen["EJE_100 Presentación de la demanda ejecutiva<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_100_origen -.->|"Título que trae aparejada ejecución"| EJE_200
  EXT_EJE_120_origen["EJE_120 Promover la ejecución después de la preparación<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_120_origen -.->|"Ejecución promovida"| EJE_200
  EJE_200 -->|"Intimación diligenciada sin pago"| EJE_220
  EXT_EJE_870_destino["EJE_870 Liquidación final<br/>(ver Ejecución y subasta)"]:::externo
  EJE_200 -->|"Pago en el acto o dinero embargado"| EXT_EJE_870_destino
  EXT_EJE_960_destino["EJE_960 Regulación de honorarios y apelación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_200 -->|"Ejecución denegada y firme"| EXT_EJE_960_destino
  EJE_220 -->|"Excepciones opuestas"| EJE_230
  EJE_220 -->|"No se oponen excepciones"| EJE_250
  EXT_EJE_995_destino["EJE_995 Sigue en la matriz de concursos y quiebras<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_220 -->|"El deudor se concursa o quiebra"| EXT_EJE_995_destino
  EJE_230 -->|"Se ofreció prueba que no consiste en constancias del expediente"| EJE_240
  EJE_230 -->|"Excepciones de puro derecho o sin prueba"| EJE_250
  EJE_240 -->|"Prueba producida y vencidos los 5 días en secretaría"| EJE_250
  EXT_EJE_260_destino["EJE_260 Apelación de la sentencia de remate<br/>(ver Sentencia y recursos)"]:::externo
  EJE_250 -->|"Sentencia notificada y es apelable (art. 552)"| EXT_EJE_260_destino
  EXT_EJE_450_destino["EJE_450 Sentencia firme (de remate o del juicio sumario)<br/>(ver Sentencia y recursos)"]:::externo
  EJE_250 -->|"Sentencia notificada y no es apelable"| EXT_EJE_450_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Cobro de pesos: demanda y contestación

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    EJE_300["<b>EJE_300</b> Presentación de la demanda de cobro de pesos (juicio sumario)<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_320["<b>EJE_320</b> Contestación de la demanda<br/>Responsable: Deudor ejecutado<br/>10 días hábiles judiciales + gracia"]:::demandada
  end
  EXT_EJE_050_origen["EJE_050 Mediación prejudicial<br/>(ver Etapa previa)"]:::externo
  EXT_EJE_050_origen -.->|"Mediación cerrada sin acuerdo en el cobro de pesos"| EJE_300
  EXT_EJE_105_origen["EJE_105 Embargo preventivo previo: presentar la demanda<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_105_origen -.->|"Demanda de cobro de pesos presentada"| EJE_300
  EXT_EJE_110_origen["EJE_110 Audiencia de reconocimiento de firma o de documentos<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_110_origen -.->|"Firma declarada no auténtica o vía no preparada: queda el cobro de pesos"| EJE_300
  EXT_EJE_120_origen["EJE_120 Promover la ejecución después de la preparación<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_120_origen -.->|"Caducaron las medidas preparatorias"| EJE_300
  P_EJE_300_1(["Se abren en paralelo"]):::paralelo
  EJE_300 -->|"Demanda proveída y traslado notificado"| P_EJE_300_1
  P_EJE_300_1 --> EJE_320
  EXT_EJE_950_destino["EJE_950 Control de caducidad de instancia<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  P_EJE_300_1 --> EXT_EJE_950_destino
  EXT_EJE_340_destino["EJE_340 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EJE_320 -->|"Contestada la demanda (o vencido el plazo) y el juzgado fija audiencia preliminar"| EXT_EJE_340_destino
  EXT_EJE_350_destino["EJE_350 Ampliación de la prueba por hechos nuevos<br/>(ver Prueba)"]:::externo
  EJE_320 -->|"Contestada la demanda (o vencido el plazo) y hay hechos controvertidos"| EXT_EJE_350_destino
  EXT_EJE_400_destino["EJE_400 Sentencia de primera instancia<br/>(ver Sentencia y recursos)"]:::externo
  EJE_320 -->|"Cuestión de puro derecho (art. 487)"| EXT_EJE_400_destino
  EXT_EJE_900_destino["EJE_900 Acuerdo, transacción o conciliación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_320 -->|"Las partes llegan a un acuerdo"| EXT_EJE_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Prueba

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    EJE_340["<b>EJE_340</b> Audiencia preliminar<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    EJE_350["<b>EJE_350</b> Ampliación de la prueba por hechos nuevos<br/>Responsable: Acreedor ejecutante<br/>5 días hábiles judiciales + gracia"]:::actora
    EJE_365["<b>EJE_365</b> Audiencia de prueba<br/>Responsable: Ambas partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_EJE_320_origen["EJE_320 Contestación de la demanda<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EXT_EJE_320_origen -.->|"Contestada la demanda (o vencido el plazo) y el juzgado fija audiencia preliminar"| EJE_340
  EXT_EJE_320_origen -.->|"Contestada la demanda (o vencido el plazo) y hay hechos controvertidos"| EJE_350
  EJE_340 -->|"Audiencia celebrada sin acuerdo"| EJE_350
  EXT_EJE_900_destino["EJE_900 Acuerdo, transacción o conciliación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_340 -->|"Acuerdo en la audiencia"| EXT_EJE_900_destino
  EJE_350 -->|"Prueba ofrecida y proveída"| EJE_365
  EXT_EJE_400_destino["EJE_400 Sentencia de primera instancia<br/>(ver Sentencia y recursos)"]:::externo
  EJE_365 -->|"Prueba producida (en el sumario no hay alegatos, art. 493)"| EXT_EJE_400_destino
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
    EJE_400["<b>EJE_400</b> Sentencia de primera instancia<br/>Responsable: Juzgado<br/>30 días hábiles judiciales"]:::tribunal
    EJE_450["<b>EJE_450</b> Sentencia firme (de remate o del juicio sumario)<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
  end
  subgraph F_1["Recursos"]
    EJE_260["<b>EJE_260</b> Apelación de la sentencia de remate<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_270["<b>EJE_270</b> Memorial de la apelación<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_410["<b>EJE_410</b> Apelación de la sentencia<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_420["<b>EJE_420</b> Expresión de agravios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_425["<b>EJE_425</b> Contestación de agravios<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_430["<b>EJE_430</b> Sentencia de la Cámara de Apelación<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_440["<b>EJE_440</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Ambas partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_EJE_250_origen["EJE_250 Sentencia de remate<br/>(ver Juicio ejecutivo: intimación, excepciones y sentencia de remate)"]:::externo
  EXT_EJE_250_origen -.->|"Sentencia notificada y es apelable (art. 552)"| EJE_260
  EXT_EJE_250_origen -.->|"Sentencia notificada y no es apelable"| EJE_450
  P_EJE_260_1(["Se abren en paralelo"]):::paralelo
  EJE_260 -->|"Se apela y el ejecutante da fianza (efecto devolutivo)"| P_EJE_260_1
  P_EJE_260_1 --> EJE_270
  EXT_EJE_800_destino["EJE_800 Embargo ejecutorio y anotación<br/>(ver Ejecución y subasta)"]:::externo
  P_EJE_260_1 --> EXT_EJE_800_destino
  EJE_260 -->|"Se apela sin fianza"| EJE_270
  EJE_260 -->|"No se apela"| EJE_450
  EJE_270 -->|"Memorial presentado y contestado o vencido el plazo"| EJE_430
  EJE_270 -->|"Recurso declarado desierto"| EJE_450
  EXT_EJE_320_origen["EJE_320 Contestación de la demanda<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EXT_EJE_320_origen -.->|"Cuestión de puro derecho (art. 487)"| EJE_400
  EXT_EJE_365_origen["EJE_365 Audiencia de prueba<br/>(ver Prueba)"]:::externo
  EXT_EJE_365_origen -.->|"Prueba producida (en el sumario no hay alegatos, art. 493)"| EJE_400
  EJE_400 -->|"Sentencia notificada"| EJE_410
  EJE_410 -->|"Se apela"| EJE_420
  EJE_410 -->|"No se apela: queda firme"| EJE_450
  EJE_420 -->|"Agravios expresados y traslado notificado"| EJE_425
  EJE_420 -->|"Recurso declarado desierto"| EJE_450
  EJE_425 -->|"Contestados los agravios o vencido el plazo"| EJE_430
  EJE_430 -->|"Sentencia de Cámara notificada y se recurre"| EJE_440
  EJE_430 -->|"Sentencia de Cámara notificada y no se recurre"| EJE_450
  EJE_440 -->|"Recurso resuelto, denegado o desistido"| EJE_450
  EXT_EJE_960_destino["EJE_960 Regulación de honorarios y apelación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_450 -->|"Sentencia de rechazo o sin condena dineraria"| EXT_EJE_960_destino
  EJE_450 -->|"Sentencia de remate firme que manda llevar adelante la ejecución"| EXT_EJE_800_destino
  EXT_EJE_460_destino["EJE_460 Liquidación de la condena<br/>(ver Ejecución y subasta)"]:::externo
  EJE_450 -->|"Condena dineraria firme en el juicio sumario"| EXT_EJE_460_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Ejecución y subasta

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    EJE_460["<b>EJE_460</b> Liquidación de la condena<br/>Responsable: Acreedor ejecutante<br/>10 días hábiles judiciales + gracia"]:::actora
    EJE_800["<b>EJE_800</b> Embargo ejecutorio y anotación<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_805["<b>EJE_805</b> Informes previos y constatación del bien<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_815["<b>EJE_815</b> Designación y aceptación del martillero<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_820["<b>EJE_820</b> Base de la subasta: vista de la tasación<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_830["<b>EJE_830</b> Publicación de edictos de subasta<br/>Responsable: Acreedor ejecutante<br/>Sin plazo"]:::actora
    EJE_840["<b>EJE_840</b> Subasta electrónica<br/>Responsable: Juzgado<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    EJE_845["<b>EJE_845</b> Pedido de nulidad de la subasta<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_850["<b>EJE_850</b> Aprobación del remate y pago del saldo de precio<br/>Responsable: Juzgado<br/>5 días hábiles judiciales"]:::tribunal
    EJE_860["<b>EJE_860</b> Posesión, escrituración y levantamiento de medidas<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_870["<b>EJE_870</b> Liquidación final<br/>Responsable: Acreedor ejecutante<br/>5 días hábiles judiciales + gracia"]:::actora
    EJE_880["<b>EJE_880</b> Pago y distribución del producido<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
  end
  EXT_EJE_200_origen["EJE_200 Mandamiento de intimación de pago y embargo<br/>(ver Juicio ejecutivo: intimación, excepciones y sentencia de remate)"]:::externo
  EXT_EJE_200_origen -.->|"Pago en el acto o dinero embargado"| EJE_870
  EXT_EJE_260_origen["EJE_260 Apelación de la sentencia de remate<br/>(ver Sentencia y recursos)"]:::externo
  EXT_EJE_260_origen -.->|"Se apela y el ejecutante da fianza (efecto devolutivo)"| EJE_800
  EXT_EJE_450_origen["EJE_450 Sentencia firme (de remate o del juicio sumario)<br/>(ver Sentencia y recursos)"]:::externo
  EXT_EJE_450_origen -.->|"Sentencia de remate firme que manda llevar adelante la ejecución"| EJE_800
  EXT_EJE_450_origen -.->|"Condena dineraria firme en el juicio sumario"| EJE_460
  EJE_460 -->|"Liquidación aprobada sin pago"| EJE_800
  EXT_EJE_960_destino["EJE_960 Regulación de honorarios y apelación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EJE_460 -->|"Liquidación aprobada y pagada"| EXT_EJE_960_destino
  EJE_800 -->|"Embargo sobre bienes que hay que vender"| EJE_805
  EJE_800 -->|"Dinero embargado o pago en el acto"| EJE_870
  EJE_805 -->|"Informes y constatación agregados"| EJE_815
  EJE_815 -->|"Martillero aceptó el cargo (inmueble)"| EJE_820
  EJE_815 -->|"Martillero aceptó el cargo (mueble, sin base)"| EJE_830
  EJE_820 -->|"Base fijada"| EJE_830
  EJE_830 -->|"Edictos publicados"| EJE_840
  EJE_840 -->|"Subasta con postor ganador"| EJE_845
  EJE_840 -->|"Subasta fracasada por falta de postores"| EJE_830
  EJE_845 -->|"Sin nulidad o nulidad rechazada"| EJE_850
  EJE_845 -->|"Nulidad admitida: nueva subasta"| EJE_830
  P_EJE_850_1(["Se abren en paralelo"]):::paralelo
  EJE_850 -->|"Saldo pagado"| P_EJE_850_1
  P_EJE_850_1 --> EJE_860
  P_EJE_850_1 --> EJE_870
  EJE_850 -->|"Postor remiso: nuevo remate"| EJE_830
  FIN_EJE_860_1(["Fin de este camino"]):::fin
  EJE_860 -->|"Posesión y escrituración cumplidas"| FIN_EJE_860_1
  EJE_870 -->|"Liquidación aprobada"| EJE_880
  EJE_880 -->|"Crédito cancelado"| EXT_EJE_960_destino
  EJE_880 -->|"Producido insuficiente: nuevos bienes"| EJE_800
  EXT_EJE_900_origen["EJE_900 Acuerdo, transacción o conciliación<br/>(ver Acuerdo, honorarios y cierre)"]:::externo
  EXT_EJE_900_origen -.->|"Acuerdo incumplido: se ejecuta como sentencia"| EJE_800
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Acuerdo, honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Acuerdo"]
    EJE_900["<b>EJE_900</b> Acuerdo, transacción o conciliación<br/>Responsable: Ambas partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Cierre"]
    EJE_950["<b>EJE_950</b> Control de caducidad de instancia<br/>Responsable: Acreedor ejecutante<br/>3 meses"]:::actora
    EJE_960["<b>EJE_960</b> Regulación de honorarios y apelación<br/>Responsable: Ambas partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    EJE_970["<b>EJE_970</b> Pago de aportes de la Ley 6716<br/>Responsable: Acreedor ejecutante<br/>60 días corridos"]:::actora
    EJE_990["<b>EJE_990</b> Archivo del expediente<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
    EJE_995["<b>EJE_995</b> Sigue en la matriz de concursos y quiebras<br/>Responsable: Juzgado<br/>Sin plazo"]:::tribunal
  end
  EXT_EJE_010_origen["EJE_010 Mora del deudor y elección de la vía<br/>(ver Etapa previa)"]:::externo
  EXT_EJE_010_origen -.->|"El deudor está concursado o en quiebra"| EJE_995
  EXT_EJE_050_origen["EJE_050 Mediación prejudicial<br/>(ver Etapa previa)"]:::externo
  EXT_EJE_050_origen -.->|"Acuerdo en la mediación"| EJE_900
  EXT_EJE_100_origen["EJE_100 Presentación de la demanda ejecutiva<br/>(ver Juicio ejecutivo: demanda y preparación de la vía)"]:::externo
  EXT_EJE_100_origen -.->|"Título que trae aparejada ejecución"| EJE_950
  EXT_EJE_100_origen -.->|"Título que requiere preparación (firma, tarjeta de crédito)"| EJE_950
  EXT_EJE_200_origen["EJE_200 Mandamiento de intimación de pago y embargo<br/>(ver Juicio ejecutivo: intimación, excepciones y sentencia de remate)"]:::externo
  EXT_EJE_200_origen -.->|"Ejecución denegada y firme"| EJE_960
  EXT_EJE_220_origen["EJE_220 Oposición de excepciones<br/>(ver Juicio ejecutivo: intimación, excepciones y sentencia de remate)"]:::externo
  EXT_EJE_220_origen -.->|"El deudor se concursa o quiebra"| EJE_995
  EXT_EJE_300_origen["EJE_300 Presentación de la demanda de cobro de pesos (juicio sumario)<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EXT_EJE_300_origen -.->|"Demanda proveída y traslado notificado"| EJE_950
  EXT_EJE_320_origen["EJE_320 Contestación de la demanda<br/>(ver Cobro de pesos: demanda y contestación)"]:::externo
  EXT_EJE_320_origen -.->|"Las partes llegan a un acuerdo"| EJE_900
  EXT_EJE_340_origen["EJE_340 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_EJE_340_origen -.->|"Acuerdo en la audiencia"| EJE_900
  EXT_EJE_450_origen["EJE_450 Sentencia firme (de remate o del juicio sumario)<br/>(ver Sentencia y recursos)"]:::externo
  EXT_EJE_450_origen -.->|"Sentencia de rechazo o sin condena dineraria"| EJE_960
  EXT_EJE_460_origen["EJE_460 Liquidación de la condena<br/>(ver Ejecución y subasta)"]:::externo
  EXT_EJE_460_origen -.->|"Liquidación aprobada y pagada"| EJE_960
  EXT_EJE_880_origen["EJE_880 Pago y distribución del producido<br/>(ver Ejecución y subasta)"]:::externo
  EXT_EJE_880_origen -.->|"Crédito cancelado"| EJE_960
  EJE_900 -->|"Acuerdo homologado y cumplido"| EJE_960
  EXT_EJE_800_destino["EJE_800 Embargo ejecutorio y anotación<br/>(ver Ejecución y subasta)"]:::externo
  EJE_900 -->|"Acuerdo incumplido: se ejecuta como sentencia"| EXT_EJE_800_destino
  FIN_EJE_950_1(["Fin de este camino"]):::fin
  EJE_950 -->|"Se dicta sentencia o termina el proceso"| FIN_EJE_950_1
  EJE_950 -->|"Caducidad declarada"| EJE_960
  EJE_960 -->|"Regulación firme"| EJE_970
  EJE_970 -->|"Aportes pagados y acreditados"| EJE_990
  style EJE_990 stroke-width:3px
  style EJE_995 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
