# Diagrama de Flujo: Desalojo de inmuebles (falta de pago, vencimiento, intrusión, tenencia precaria o comodato) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68), juicio sumario (arts. 676 a 678 bis); CCyC arts. 1217 a 1225 (texto según DNU 70/2023, a verificar); Ley 13.951 (mediación optativa) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_civil_desalojo_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el locador, propietario o comodante que pide el desalojo (ACTORA); naranja = el locatario, sublocatario, intruso, tenedor precario u otro ocupante (DEMANDADA); gris = el juzgado, el oficial de justicia, el mediador o un organismo (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, el cobro ejecutivo de los alquileres adeudados se inicia mientras corre la intimación de pago previa al desalojo.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>10 hitos"]
  FASE_2["Postulación<br/>9 hitos"]
  FASE_3["Prueba<br/>9 hitos"]
  FASE_4["Sentencia<br/>4 hitos"]
  FASE_5["Recursos<br/>8 hitos"]
  FASE_6["Lanzamiento<br/>5 hitos"]
  FASE_7["Acuerdo<br/>2 hitos"]
  FASE_8["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_8
  FASE_1 --> FASE_6
  FASE_1 --> FASE_2
  FASE_1 --> FASE_7
  FASE_2 --> FASE_8
  FASE_2 --> FASE_5
  FASE_2 --> FASE_6
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
    DES_010["INICIO - <b>DES_010</b> Consulta inicial por la recuperación del inmueble<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_020["<b>DES_020</b> Intimación de pago de alquileres (art. 1222)<br/>Responsable: Locatario u ocupante<br/>10 días corridos"]:::demandada
    DES_030["<b>DES_030</b> Intimación fehaciente a restituir el inmueble<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_040["<b>DES_040</b> Restitución del inmueble por el ocupante<br/>Responsable: Locatario u ocupante<br/>Sin plazo"]:::demandada
    DES_050["<b>DES_050</b> Constatación de la ocupación del inmueble<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_055["<b>DES_055</b> Denuncia penal por usurpación y restitución en sede penal<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_070["<b>DES_070</b> Requerimiento de mediación prejudicial (optativa)<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_072["<b>DES_072</b> Audiencia de mediación<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DES_074["<b>DES_074</b> Plazo de la mediación<br/>Responsable: Juzgado u organismo<br/>30 días corridos"]:::tribunal
    DES_080["<b>DES_080</b> Cobro ejecutivo de alquileres adeudados (juicio aparte)<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
  end
  P_DES_010_1(["Se abren en paralelo"]):::paralelo
  DES_010 -->|"Falta de pago de alquileres"| P_DES_010_1
  P_DES_010_1 --> DES_020
  P_DES_010_1 --> DES_080
  DES_010 -->|"Vencimiento o resolución del contrato, tenencia precaria o comodato"| DES_030
  DES_010 -->|"Intrusión u ocupación sin título"| DES_050
  EXT_DES_990_destino["DES_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DES_020 -->|"Paga en el plazo: sigue la locación"| EXT_DES_990_destino
  DES_020 -->|"No paga en el plazo: debe restituir"| DES_040
  DES_030 -->|"Intimación recibida"| DES_040
  EXT_DES_780_destino["DES_780 Toma de posesión, llaves y destino de los muebles<br/>(ver Lanzamiento)"]:::externo
  DES_040 -->|"Restituye el inmueble"| EXT_DES_780_destino
  DES_040 -->|"No paga o no restituye: se pide la mediación optativa"| DES_070
  EXT_DES_300_destino["DES_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  DES_040 -->|"No paga o no restituye: se demanda directamente"| EXT_DES_300_destino
  DES_050 -->|"Ocupación constatada: se demanda el desalojo"| EXT_DES_300_destino
  P_DES_050_2(["Se abren en paralelo"]):::paralelo
  DES_050 -->|"Ocupación constatada: se demanda y se denuncia la usurpación"| P_DES_050_2
  P_DES_050_2 --> EXT_DES_300_destino
  P_DES_050_2 --> DES_055
  FIN_DES_055_1(["Fin de este camino"]):::fin
  DES_055 -->|"Causa penal en trámite o terminada (se informa al juez civil)"| FIN_DES_055_1
  DES_055 -->|"Restitución ordenada en sede penal"| EXT_DES_780_destino
  P_DES_070_1(["Se abren en paralelo"]):::paralelo
  DES_070 -->|"Mediador designado y audiencia fijada"| P_DES_070_1
  P_DES_070_1 --> DES_072
  P_DES_070_1 --> DES_074
  FIN_DES_072_1(["Fin de este camino"]):::fin
  DES_072 -->|"Audiencia realizada"| FIN_DES_072_1
  EXT_DES_800_destino["DES_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  DES_074 -->|"Acuerdo en la mediación"| EXT_DES_800_destino
  DES_074 -->|"Cierre sin acuerdo o por incomparecencia"| EXT_DES_300_destino
  FIN_DES_080_1(["Fin de este camino"]):::fin
  DES_080 -->|"Ejecución iniciada como otro caso"| FIN_DES_080_1
  style DES_010 stroke-width:3px
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
    DES_300["<b>DES_300</b> Presentación de la demanda<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_310["<b>DES_310</b> Beneficio de litigar sin gastos<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_320["<b>DES_320</b> Medidas cautelares<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_325["<b>DES_325</b> Entrega o desocupación inmediata bajo caución real<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_330["<b>DES_330</b> Radicación, control de admisibilidad y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_340["<b>DES_340</b> Contestación de la demanda<br/>Responsable: Locatario u ocupante<br/>10 días hábiles judiciales + gracia"]:::demandada
    DES_355["<b>DES_355</b> Traslado a la actora de las excepciones previas<br/>Responsable: Locador o propietario<br/>5 días hábiles judiciales + gracia"]:::actora
    DES_360["<b>DES_360</b> Traslado a la actora de la documental de la contestación<br/>Responsable: Locador o propietario<br/>5 días hábiles judiciales + gracia"]:::actora
    DES_370["<b>DES_370</b> Contestación de la reconvención<br/>Responsable: Locador o propietario<br/>10 días hábiles judiciales + gracia"]:::actora
  end
  EXT_DES_040_origen["DES_040 Restitución del inmueble por el ocupante<br/>(ver Etapa previa)"]:::externo
  EXT_DES_040_origen -.->|"No paga o no restituye: se demanda directamente"| DES_300
  EXT_DES_050_origen["DES_050 Constatación de la ocupación del inmueble<br/>(ver Etapa previa)"]:::externo
  EXT_DES_050_origen -.->|"Ocupación constatada: se demanda el desalojo"| DES_300
  EXT_DES_050_origen -.->|"Ocupación constatada: se demanda y se denuncia la usurpación"| DES_300
  EXT_DES_074_origen["DES_074 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_DES_074_origen -.->|"Cierre sin acuerdo o por incomparecencia"| DES_300
  P_DES_300_1(["Se abren en paralelo"]):::paralelo
  DES_300 -->|"Demanda presentada"| P_DES_300_1
  P_DES_300_1 --> DES_330
  EXT_DES_900_destino["DES_900 Control de la caducidad de instancia<br/>(ver Cierre)"]:::externo
  P_DES_300_1 --> EXT_DES_900_destino
  P_DES_300_2(["Se abren en paralelo"]):::paralelo
  DES_300 -->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| P_DES_300_2
  P_DES_300_2 --> DES_330
  P_DES_300_2 --> DES_310
  P_DES_300_2 --> EXT_DES_900_destino
  P_DES_300_3(["Se abren en paralelo"]):::paralelo
  DES_300 -->|"Demanda presentada con pedido de medida cautelar"| P_DES_300_3
  P_DES_300_3 --> DES_330
  P_DES_300_3 --> DES_320
  P_DES_300_3 --> EXT_DES_900_destino
  FIN_DES_310_1(["Fin de este camino"]):::fin
  DES_310 -->|"Beneficio concedido, o denegado sin recurso (se integran tasa y aportes)"| FIN_DES_310_1
  EXT_DES_650_destino["DES_650 Memorial del recurso concedido en relación<br/>(ver Sentencia y recursos)"]:::externo
  DES_310 -->|"Beneficio denegado: se apela"| EXT_DES_650_destino
  FIN_DES_320_1(["Fin de este camino"]):::fin
  DES_320 -->|"Medida trabada o denegada sin recurso"| FIN_DES_320_1
  DES_320 -->|"Medida denegada o trabada: se apela"| EXT_DES_650_destino
  EXT_DES_760_destino["DES_760 Pedido y libramiento del mandamiento de lanzamiento<br/>(ver Lanzamiento)"]:::externo
  DES_325 -->|"Entrega ordenada: se libra el mandamiento"| EXT_DES_760_destino
  FIN_DES_325_2(["Fin de este camino"]):::fin
  DES_325 -->|"Pedido denegado"| FIN_DES_325_2
  DES_325 -->|"Se apela la resolución"| EXT_DES_650_destino
  EXT_DES_990_destino["DES_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DES_330 -->|"Demanda rechazada in limine o no subsanada"| EXT_DES_990_destino
  DES_330 -->|"Se ordena el traslado de la demanda"| DES_340
  DES_340 -->|"Contesta la demanda"| DES_360
  P_DES_340_2(["Se abren en paralelo"]):::paralelo
  DES_340 -->|"Contesta y opone excepciones previas"| P_DES_340_2
  P_DES_340_2 --> DES_360
  P_DES_340_2 --> DES_355
  P_DES_340_3(["Se abren en paralelo"]):::paralelo
  DES_340 -->|"Contesta y reconviene"| P_DES_340_3
  P_DES_340_3 --> DES_360
  P_DES_340_3 --> DES_370
  EXT_DES_400_destino["DES_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  DES_340 -->|"No contesta en término"| EXT_DES_400_destino
  FIN_DES_355_1(["Fin de este camino"]):::fin
  DES_355 -->|"Excepciones rechazadas o diferidas para la sentencia"| FIN_DES_355_1
  DES_355 -->|"Excepción admitida que pone fin al proceso: se apela"| EXT_DES_650_destino
  DES_355 -->|"Excepción admitida y consentida"| EXT_DES_990_destino
  DES_360 -->|"Traslado contestado o plazo vencido"| EXT_DES_400_destino
  P_DES_360_2(["Se abren en paralelo"]):::paralelo
  DES_360 -->|"Traslado contestado o plazo vencido, con pedido de desocupación inmediata"| P_DES_360_2
  P_DES_360_2 --> DES_325
  P_DES_360_2 --> EXT_DES_400_destino
  FIN_DES_370_1(["Fin de este camino"]):::fin
  DES_370 -->|"Reconvención contestada o plazo vencido"| FIN_DES_370_1
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
    DES_400["<b>DES_400</b> Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_405["<b>DES_405</b> Reposición u oposición contra la providencia de prueba<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DES_415["<b>DES_415</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DES_420["<b>DES_420</b> Dictamen pericial<br/>Responsable: Juzgado u organismo<br/>5 días hábiles de anticipación"]:::tribunal
    DES_425["<b>DES_425</b> Traslado del dictamen pericial<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_430["<b>DES_430</b> Prueba informativa: contestación de los oficios<br/>Responsable: Juzgado u organismo<br/>10 días hábiles judiciales"]:::tribunal
    DES_435["<b>DES_435</b> Pedido de reiteración del oficio no contestado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_440["<b>DES_440</b> Audiencia de prueba o de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DES_450["<b>DES_450</b> Alegatos<br/>Responsable: Cualquiera de las partes<br/>6 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DES_340_origen["DES_340 Contestación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_340_origen -.->|"No contesta en término"| DES_400
  EXT_DES_360_origen["DES_360 Traslado a la actora de la documental de la contestación<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_360_origen -.->|"Traslado contestado o plazo vencido"| DES_400
  EXT_DES_360_origen -.->|"Traslado contestado o plazo vencido, con pedido de desocupación inmediata"| DES_400
  P_DES_400_1(["Se abren en paralelo"]):::paralelo
  DES_400 -->|"Se provee la prueba ofrecida"| P_DES_400_1
  P_DES_400_1 --> DES_405
  P_DES_400_1 --> DES_420
  P_DES_400_1 --> DES_430
  P_DES_400_1 --> DES_440
  DES_400 -->|"Se fija audiencia preliminar"| DES_415
  EXT_DES_500_destino["DES_500 Llamamiento de autos y sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  DES_400 -->|"Causa declarada de puro derecho"| EXT_DES_500_destino
  FIN_DES_405_1(["Fin de este camino"]):::fin
  DES_405 -->|"Resuelta o plazo vencido"| FIN_DES_405_1
  EXT_DES_800_destino["DES_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  DES_415 -->|"Acuerdo conciliatorio en la audiencia"| EXT_DES_800_destino
  P_DES_415_2(["Se abren en paralelo"]):::paralelo
  DES_415 -->|"Se provee la prueba y se fija la audiencia de vista de causa"| P_DES_415_2
  P_DES_415_2 --> DES_405
  P_DES_415_2 --> DES_420
  P_DES_415_2 --> DES_430
  P_DES_415_2 --> DES_440
  DES_415 -->|"Causa declarada de puro derecho"| EXT_DES_500_destino
  DES_420 -->|"Dictamen presentado"| DES_425
  FIN_DES_420_2(["Fin de este camino"]):::fin
  DES_420 -->|"Pericia no ofrecida o desistida"| FIN_DES_420_2
  FIN_DES_425_1(["Fin de este camino"]):::fin
  DES_425 -->|"Observaciones presentadas o plazo vencido"| FIN_DES_425_1
  FIN_DES_430_1(["Fin de este camino"]):::fin
  DES_430 -->|"Informes contestados o prueba desistida"| FIN_DES_430_1
  DES_430 -->|"Plazo vencido sin respuesta"| DES_435
  DES_435 -->|"Reiteración pedida"| DES_430
  FIN_DES_435_2(["Fin de este camino"]):::fin
  DES_435 -->|"No se pide: prueba desistida"| FIN_DES_435_2
  DES_440 -->|"Audiencia realizada y prueba producida"| DES_450
  DES_440 -->|"Acuerdo conciliatorio en la audiencia"| EXT_DES_800_destino
  DES_450 -->|"Alegatos presentados o plazo vencido"| EXT_DES_500_destino
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
    DES_500["<b>DES_500</b> Llamamiento de autos y sentencia definitiva<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_505["<b>DES_505</b> Aclaratoria<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    DES_510["<b>DES_510</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_515["<b>DES_515</b> Pago de los honorarios firmes<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  subgraph F_1["Recursos"]
    DES_600["<b>DES_600</b> Recurso de apelación contra la sentencia definitiva<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_610["<b>DES_610</b> Expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_615["<b>DES_615</b> Contestación de la expresión de agravios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_620["<b>DES_620</b> Sentencia o resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_630["<b>DES_630</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    DES_640["<b>DES_640</b> Queja ante la SCBA por recurso denegado<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    DES_645["<b>DES_645</b> Trámite y sentencia de la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    DES_650["<b>DES_650</b> Memorial del recurso concedido en relación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DES_310_origen["DES_310 Beneficio de litigar sin gastos<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_310_origen -.->|"Beneficio denegado: se apela"| DES_650
  EXT_DES_320_origen["DES_320 Medidas cautelares<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_320_origen -.->|"Medida denegada o trabada: se apela"| DES_650
  EXT_DES_325_origen["DES_325 Entrega o desocupación inmediata bajo caución real<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_325_origen -.->|"Se apela la resolución"| DES_650
  EXT_DES_355_origen["DES_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_355_origen -.->|"Excepción admitida que pone fin al proceso: se apela"| DES_650
  EXT_DES_400_origen["DES_400 Apertura a prueba, audiencia preliminar o declaración de puro derecho<br/>(ver Prueba)"]:::externo
  EXT_DES_400_origen -.->|"Causa declarada de puro derecho"| DES_500
  EXT_DES_415_origen["DES_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_DES_415_origen -.->|"Causa declarada de puro derecho"| DES_500
  EXT_DES_450_origen["DES_450 Alegatos<br/>(ver Prueba)"]:::externo
  EXT_DES_450_origen -.->|"Alegatos presentados o plazo vencido"| DES_500
  P_DES_500_1(["Se abren en paralelo"]):::paralelo
  DES_500 -->|"Sentencia notificada"| P_DES_500_1
  P_DES_500_1 --> DES_505
  P_DES_500_1 --> DES_510
  P_DES_500_1 --> DES_600
  FIN_DES_505_1(["Fin de este camino"]):::fin
  DES_505 -->|"Aclaratoria resuelta o plazo vencido"| FIN_DES_505_1
  DES_510 -->|"Regulación firme"| DES_515
  FIN_DES_515_1(["Fin de este camino"]):::fin
  DES_515 -->|"Honorarios pagados o en ejecución"| FIN_DES_515_1
  EXT_DES_750_destino["DES_750 Plazo para desocupar fijado en la sentencia<br/>(ver Lanzamiento)"]:::externo
  DES_600 -->|"No se recurre: queda firme y hace lugar a la demanda"| EXT_DES_750_destino
  EXT_DES_990_destino["DES_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DES_600 -->|"No se recurre: queda firme y rechaza la demanda"| EXT_DES_990_destino
  DES_600 -->|"Se interpone apelación"| DES_610
  DES_610 -->|"Agravios presentados"| DES_615
  DES_610 -->|"No expresa agravios: deserción"| DES_620
  DES_615 -->|"Contestados o plazo vencido"| DES_620
  DES_620 -->|"Sentencia de Cámara firme que hace lugar a la demanda"| EXT_DES_750_destino
  DES_620 -->|"Sentencia de Cámara firme que rechaza la demanda"| EXT_DES_990_destino
  FIN_DES_620_3(["Fin de este camino"]):::fin
  DES_620 -->|"Cámara resuelve la apelación de una resolución interlocutoria: sigue el trámite"| FIN_DES_620_3
  DES_620 -->|"Se interponen recursos extraordinarios"| DES_630
  DES_630 -->|"Recurso concedido"| DES_645
  DES_630 -->|"Recurso denegado"| DES_640
  DES_640 -->|"Queja admitida"| DES_645
  DES_640 -->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| EXT_DES_750_destino
  DES_640 -->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| EXT_DES_990_destino
  DES_645 -->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| EXT_DES_750_destino
  DES_645 -->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| EXT_DES_990_destino
  DES_645 -->|"La SCBA anula y reenvía para nuevo pronunciamiento"| DES_620
  DES_650 -->|"Memorial presentado o plazo vencido"| DES_620
  EXT_DES_800_origen["DES_800 Acuerdo, transacción o conciliación y homologación<br/>(ver Acuerdo)"]:::externo
  EXT_DES_800_origen -.->|"Acuerdo homologado"| DES_510
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Lanzamiento

```mermaid
flowchart TD
  subgraph F_0["Lanzamiento"]
    DES_750["<b>DES_750</b> Plazo para desocupar fijado en la sentencia<br/>Responsable: Locatario u ocupante<br/>10 días corridos"]:::demandada
    DES_760["<b>DES_760</b> Pedido y libramiento del mandamiento de lanzamiento<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
    DES_765["<b>DES_765</b> Consulta al Registro de Villas y Asentamientos y audiencia de relocalización<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DES_770["<b>DES_770</b> Diligencia de lanzamiento<br/>Responsable: Juzgado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    DES_780["<b>DES_780</b> Toma de posesión, llaves y destino de los muebles<br/>Responsable: Locador o propietario<br/>Sin plazo"]:::actora
  end
  EXT_DES_040_origen["DES_040 Restitución del inmueble por el ocupante<br/>(ver Etapa previa)"]:::externo
  EXT_DES_040_origen -.->|"Restituye el inmueble"| DES_780
  EXT_DES_055_origen["DES_055 Denuncia penal por usurpación y restitución en sede penal<br/>(ver Etapa previa)"]:::externo
  EXT_DES_055_origen -.->|"Restitución ordenada en sede penal"| DES_780
  EXT_DES_325_origen["DES_325 Entrega o desocupación inmediata bajo caución real<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_325_origen -.->|"Entrega ordenada: se libra el mandamiento"| DES_760
  EXT_DES_600_origen["DES_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_600_origen -.->|"No se recurre: queda firme y hace lugar a la demanda"| DES_750
  EXT_DES_620_origen["DES_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_620_origen -.->|"Sentencia de Cámara firme que hace lugar a la demanda"| DES_750
  EXT_DES_640_origen["DES_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_640_origen -.->|"Queja rechazada: queda firme una sentencia que hace lugar a la demanda"| DES_750
  EXT_DES_645_origen["DES_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda"| DES_750
  DES_750 -->|"Desocupa y entrega las llaves"| DES_780
  DES_750 -->|"No desocupa en el plazo"| DES_760
  DES_760 -->|"Mandamiento librado y diligencia fijada"| DES_770
  DES_760 -->|"El inmueble está en una villa o asentamiento (art. 678 bis)"| DES_765
  DES_765 -->|"No está registrado, o hay peligro inminente y plan de relocalización"| DES_770
  DES_765 -->|"Está registrado: el desalojo se suspende por el plazo legal"| DES_760
  DES_770 -->|"Lanzamiento cumplido"| DES_780
  DES_770 -->|"Diligencia frustrada o suspendida"| DES_760
  EXT_DES_990_destino["DES_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DES_780 -->|"Inmueble recuperado y proceso terminado"| EXT_DES_990_destino
  FIN_DES_780_2(["Fin de este camino"]):::fin
  DES_780 -->|"Inmueble recuperado por desocupación inmediata: sigue el juicio"| FIN_DES_780_2
  EXT_DES_805_origen["DES_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_DES_805_origen -.->|"Acuerdo incumplido: se ejecuta"| DES_760
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
    DES_800["<b>DES_800</b> Acuerdo, transacción o conciliación y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    DES_805["<b>DES_805</b> Cumplimiento del acuerdo homologado<br/>Responsable: Locatario u ocupante<br/>Sin plazo"]:::demandada
  end
  EXT_DES_074_origen["DES_074 Plazo de la mediación<br/>(ver Etapa previa)"]:::externo
  EXT_DES_074_origen -.->|"Acuerdo en la mediación"| DES_800
  EXT_DES_415_origen["DES_415 Audiencia preliminar<br/>(ver Prueba)"]:::externo
  EXT_DES_415_origen -.->|"Acuerdo conciliatorio en la audiencia"| DES_800
  EXT_DES_440_origen["DES_440 Audiencia de prueba o de vista de causa<br/>(ver Prueba)"]:::externo
  EXT_DES_440_origen -.->|"Acuerdo conciliatorio en la audiencia"| DES_800
  P_DES_800_1(["Se abren en paralelo"]):::paralelo
  DES_800 -->|"Acuerdo homologado"| P_DES_800_1
  P_DES_800_1 --> DES_805
  EXT_DES_510_destino["DES_510 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_DES_800_1 --> EXT_DES_510_destino
  EXT_DES_990_destino["DES_990 Archivo del expediente<br/>(ver Cierre)"]:::externo
  DES_805 -->|"Acuerdo cumplido"| EXT_DES_990_destino
  EXT_DES_760_destino["DES_760 Pedido y libramiento del mandamiento de lanzamiento<br/>(ver Lanzamiento)"]:::externo
  DES_805 -->|"Acuerdo incumplido: se ejecuta"| EXT_DES_760_destino
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
    DES_900["<b>DES_900</b> Control de la caducidad de instancia<br/>Responsable: Locador o propietario<br/>3 meses"]:::actora
    DES_905["<b>DES_905</b> Intimación a activar el proceso<br/>Responsable: Locador o propietario<br/>5 días hábiles judiciales + gracia"]:::actora
    DES_990["<b>DES_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_DES_020_origen["DES_020 Intimación de pago de alquileres (art. 1222)<br/>(ver Etapa previa)"]:::externo
  EXT_DES_020_origen -.->|"Paga en el plazo: sigue la locación"| DES_990
  EXT_DES_300_origen["DES_300 Presentación de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_300_origen -.->|"Demanda presentada"| DES_900
  EXT_DES_300_origen -.->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| DES_900
  EXT_DES_300_origen -.->|"Demanda presentada con pedido de medida cautelar"| DES_900
  EXT_DES_330_origen["DES_330 Radicación, control de admisibilidad y traslado de la demanda<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_330_origen -.->|"Demanda rechazada in limine o no subsanada"| DES_990
  EXT_DES_355_origen["DES_355 Traslado a la actora de las excepciones previas<br/>(ver Demanda y contestación)"]:::externo
  EXT_DES_355_origen -.->|"Excepción admitida y consentida"| DES_990
  EXT_DES_600_origen["DES_600 Recurso de apelación contra la sentencia definitiva<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_600_origen -.->|"No se recurre: queda firme y rechaza la demanda"| DES_990
  EXT_DES_620_origen["DES_620 Sentencia o resolución de la Cámara<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_620_origen -.->|"Sentencia de Cámara firme que rechaza la demanda"| DES_990
  EXT_DES_640_origen["DES_640 Queja ante la SCBA por recurso denegado<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_640_origen -.->|"Queja rechazada: queda firme una sentencia que rechaza la demanda"| DES_990
  EXT_DES_645_origen["DES_645 Trámite y sentencia de la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DES_645_origen -.->|"La SCBA resuelve: queda firme una sentencia que rechaza la demanda"| DES_990
  EXT_DES_780_origen["DES_780 Toma de posesión, llaves y destino de los muebles<br/>(ver Lanzamiento)"]:::externo
  EXT_DES_780_origen -.->|"Inmueble recuperado y proceso terminado"| DES_990
  EXT_DES_805_origen["DES_805 Cumplimiento del acuerdo homologado<br/>(ver Acuerdo)"]:::externo
  EXT_DES_805_origen -.->|"Acuerdo cumplido"| DES_990
  FIN_DES_900_1(["Fin de este camino"]):::fin
  DES_900 -->|"Proceso terminado antes del vencimiento"| FIN_DES_900_1
  DES_900 -->|"Plazo vencido: se intima a activar el proceso"| DES_905
  FIN_DES_905_1(["Fin de este camino"]):::fin
  DES_905 -->|"Proceso activado en término"| FIN_DES_905_1
  DES_905 -->|"No se activa: se decreta la caducidad"| DES_990
  style DES_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
