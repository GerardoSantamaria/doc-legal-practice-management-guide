# Diagrama de Flujo: Alimentos y compensación económica (PBA)

**Régimen:** CPCCBA (Decreto-Ley 7425/68), Libro VIII: proceso ante los Juzgados de Familia (arts. 827 a 853, texto de las Leyes 13.634 y 15.513); juicio de alimentos, arts. 635 a 648 CPCCBA (texto Ley 15.513); CCyC, arts. 432 a 434, 441, 442, 519, 524, 525, 537 a 554 y 658 a 670 · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_familia_alimentos_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = quien reclama alimentos o compensación (ACTORA); naranja = el alimentante u obligado (DEMANDADA); gris = juzgado, Consejero, Asesoría de Incapaces u organismo que informa, aclarado en el nombre (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, cuando el primer auto fija la audiencia y los alimentos provisorios, corren a la vez la audiencia y el control del pago de la cuota.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un registro). La app los separa en el flujo prejudicial.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Consejero de Familia<br/>3 hitos"]
  FASE_3["Juicio de alimentos<br/>6 hitos"]
  FASE_4["Postulación<br/>5 hitos"]
  FASE_5["Audiencia preliminar<br/>1 hito"]
  FASE_6["Prueba<br/>3 hitos"]
  FASE_7["Vista de causa<br/>2 hitos"]
  FASE_8["Sentencia<br/>3 hitos"]
  FASE_9["Recursos<br/>6 hitos"]
  FASE_10["Cuota e incidentes<br/>8 hitos"]
  FASE_11["Ejecución<br/>2 hitos"]
  FASE_12["Acuerdo<br/>2 hitos"]
  FASE_13["Cierre<br/>1 hito"]
  FASE_1 --> FASE_3
  FASE_1 --> FASE_2
  FASE_1 --> FASE_10
  FASE_1 --> FASE_12
  FASE_1 --> FASE_13
  FASE_2 --> FASE_3
  FASE_2 --> FASE_4
  FASE_2 --> FASE_12
  FASE_3 --> FASE_10
  FASE_3 --> FASE_4
  FASE_3 --> FASE_12
  FASE_3 --> FASE_13
  FASE_3 --> FASE_8
  FASE_3 --> FASE_9
  FASE_4 --> FASE_3
  FASE_4 --> FASE_5
  FASE_5 --> FASE_12
  FASE_5 --> FASE_6
  FASE_5 --> FASE_8
  FASE_5 --> FASE_13
  FASE_6 --> FASE_7
  FASE_7 --> FASE_12
  FASE_7 --> FASE_8
  FASE_8 --> FASE_9
  FASE_9 --> FASE_11
  FASE_11 --> FASE_13
  FASE_10 --> FASE_13
  FASE_10 --> FASE_8
  FASE_10 --> FASE_9
  FASE_12 --> FASE_3
  FASE_12 --> FASE_4
  FASE_12 --> FASE_6
  FASE_12 --> FASE_10
  FASE_12 --> FASE_13
  FASE_12 --> FASE_11
```

## 1. Etapa previa (antes de promover)

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    ALI_010["INICIO - <b>ALI_010</b> Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_020["<b>ALI_020</b> Interpelación fehaciente al alimentante<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_030["<b>ALI_030</b> Plazo para demandar con efecto retroactivo a la interpelación<br/>Responsable: Quien reclama<br/>6 meses"]:::actora
    ALI_040["<b>ALI_040</b> Control de caducidad de la compensación económica<br/>Responsable: Quien reclama<br/>6 meses"]:::actora
    ALI_050["<b>ALI_050</b> Elección de la vía: etapa previa o demanda directa<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
  end
  ALI_010 -->|"Reclamo de alimentos con interpelación previa"| ALI_020
  ALI_010 -->|"Reclamo de alimentos sin interpelación previa"| ALI_050
  EXT_ALI_130_destino["ALI_130 Demanda de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  ALI_010 -->|"Reclamo urgente (persona por nacer o necesidad inmediata): demanda directa"| EXT_ALI_130_destino
  P_ALI_010_4(["Se abren en paralelo"]):::paralelo
  ALI_010 -->|"Compensación económica tras el divorcio o el cese de la convivencia"| P_ALI_010_4
  P_ALI_010_4 --> ALI_040
  EXT_ALI_100_destino["ALI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  P_ALI_010_4 --> EXT_ALI_100_destino
  EXT_ALI_740_destino["ALI_740 Ejecución de cuotas atrasadas<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  ALI_010 -->|"Convenio con firmas certificadas incumplido (art. 521 inc. 7)"| EXT_ALI_740_destino
  EXT_ALI_900_destino["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_010 -->|"Convenio fuera del expediente que se quiere homologar"| EXT_ALI_900_destino
  EXT_ALI_720_destino["ALI_720 Pago de la cuota alimentaria<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  ALI_010 -->|"Ya hay una cuota fijada por sentencia o acuerdo homologado"| EXT_ALI_720_destino
  P_ALI_020_1(["Se abren en paralelo"]):::paralelo
  ALI_020 -->|"Interpelación recibida"| P_ALI_020_1
  P_ALI_020_1 --> ALI_030
  P_ALI_020_1 --> ALI_050
  ALI_020 -->|"El alimentante propone un acuerdo"| EXT_ALI_900_destino
  FIN_ALI_030_1(["Fin de este camino"]):::fin
  ALI_030 -->|"Reclamo iniciado, o plazo vencido (la retroactividad se limita al inicio del reclamo)"| FIN_ALI_030_1
  FIN_ALI_040_1(["Fin de este camino"]):::fin
  ALI_040 -->|"Demanda presentada o compensación acordada en término"| FIN_ALI_040_1
  EXT_ALI_990_destino["ALI_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_040 -->|"Vencido sin demanda: la acción caducó"| EXT_ALI_990_destino
  ALI_050 -->|"Etapa previa ante el Consejero"| EXT_ALI_100_destino
  ALI_050 -->|"Demanda directa ante el Juzgado de Familia o de Paz"| EXT_ALI_130_destino
  style ALI_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Etapa previa ante el Consejero de Familia

```mermaid
flowchart TD
  subgraph F_0["Consejero de Familia"]
    ALI_100["<b>ALI_100</b> Solicitud de trámite de la etapa previa<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_110["<b>ALI_110</b> Audiencias ante el Consejero de Familia<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    ALI_120["<b>ALI_120</b> Acta de cierre de la etapa previa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_ALI_010_origen["ALI_010 Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_010_origen -.->|"Compensación económica tras el divorcio o el cese de la convivencia"| ALI_100
  EXT_ALI_050_origen["ALI_050 Elección de la vía: etapa previa o demanda directa<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_050_origen -.->|"Etapa previa ante el Consejero"| ALI_100
  ALI_100 -->|"Etapa previa admitida: el Consejero cita a las partes"| ALI_110
  EXT_ALI_130_destino["ALI_130 Demanda de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  ALI_100 -->|"Urgencia: radicación directa del reclamo de alimentos"| EXT_ALI_130_destino
  EXT_ALI_200_destino["ALI_200 Demanda de compensación económica<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  ALI_100 -->|"Urgencia o riesgo de caducidad: radicación directa de la compensación económica"| EXT_ALI_200_destino
  ALI_110 -->|"Conciliación, fracaso o intervención agotada: el Consejero labra el acta"| ALI_120
  ALI_110 -->|"Una parte pide concluir la etapa y el juez la da por concluida"| ALI_120
  ALI_110 -->|"El juez dispone continuar la etapa (hasta 15 días)"| ALI_110
  EXT_ALI_900_destino["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_120 -->|"Acuerdo"| EXT_ALI_900_destino
  ALI_120 -->|"Sin acuerdo sobre los alimentos"| EXT_ALI_130_destino
  ALI_120 -->|"Sin acuerdo sobre la compensación económica"| EXT_ALI_200_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Juicio de alimentos

```mermaid
flowchart TD
  subgraph F_0["Juicio de alimentos"]
    ALI_130["<b>ALI_130</b> Demanda de alimentos<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_140["<b>ALI_140</b> Primer auto: audiencia y alimentos provisorios<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_150["<b>ALI_150</b> Audiencia del juicio de alimentos<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    ALI_160["<b>ALI_160</b> Multa y nueva audiencia por incomparecencia del alimentante<br/>Responsable: Alimentante u obligado<br/>3 días hábiles judiciales"]:::demandada
    ALI_170["<b>ALI_170</b> Prueba del juicio de alimentos (informes)<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ALI_180["<b>ALI_180</b> Sentencia de alimentos<br/>Responsable: Juzgado u organismo<br/>5 días hábiles judiciales"]:::tribunal
  end
  EXT_ALI_010_origen["ALI_010 Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_010_origen -.->|"Reclamo urgente (persona por nacer o necesidad inmediata): demanda directa"| ALI_130
  EXT_ALI_050_origen["ALI_050 Elección de la vía: etapa previa o demanda directa<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_050_origen -.->|"Demanda directa ante el Juzgado de Familia o de Paz"| ALI_130
  EXT_ALI_100_origen["ALI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_ALI_100_origen -.->|"Urgencia: radicación directa del reclamo de alimentos"| ALI_130
  EXT_ALI_120_origen["ALI_120 Acta de cierre de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_ALI_120_origen -.->|"Sin acuerdo sobre los alimentos"| ALI_130
  P_ALI_130_1(["Se abren en paralelo"]):::paralelo
  ALI_130 -->|"Demanda de alimentos para un hijo"| P_ALI_130_1
  P_ALI_130_1 --> ALI_140
  EXT_ALI_760_destino["ALI_760 Control de los 21 años del hijo alimentado<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  P_ALI_130_1 --> EXT_ALI_760_destino
  ALI_130 -->|"Demanda de alimentos entre cónyuges, convivientes o para la persona por nacer"| ALI_140
  P_ALI_140_1(["Se abren en paralelo"]):::paralelo
  ALI_140 -->|"Audiencia fijada (con o sin alimentos provisorios)"| P_ALI_140_1
  P_ALI_140_1 --> ALI_150
  EXT_ALI_720_destino["ALI_720 Pago de la cuota alimentaria<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  P_ALI_140_1 --> EXT_ALI_720_destino
  EXT_ALI_230_destino["ALI_230 Citación por edictos al demandado con domicilio desconocido<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  ALI_140 -->|"Alimentante con domicilio desconocido"| EXT_ALI_230_destino
  EXT_ALI_910_destino["ALI_910 Cumplimiento del acuerdo homologado<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_150 -->|"Acuerdo: el juez lo homologa en el acto"| EXT_ALI_910_destino
  ALI_150 -->|"Sin acuerdo: se produce la prueba"| ALI_170
  ALI_150 -->|"El alimentante no comparece sin justa causa"| ALI_160
  ALI_150 -->|"Nueva audiencia (incomparecencia justificada, o de la actora por primera vez)"| ALI_150
  EXT_ALI_990_destino["ALI_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_150 -->|"La actora no comparece a la segunda audiencia: se la tiene por desistida"| EXT_ALI_990_destino
  ALI_160 -->|"Se celebra la nueva audiencia"| ALI_150
  ALI_160 -->|"No comparece a la nueva audiencia: la cuota se fija según lo pedido por la actora"| ALI_180
  ALI_170 -->|"Prueba de la actora producida"| ALI_180
  P_ALI_180_1(["Se abren en paralelo"]):::paralelo
  ALI_180 -->|"Sentencia notificada (la cuota fijada sigue en el control de pago)"| P_ALI_180_1
  EXT_ALI_520_destino["ALI_520 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_ALI_180_1 --> EXT_ALI_520_destino
  EXT_ALI_600_destino["ALI_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  P_ALI_180_1 --> EXT_ALI_600_destino
  EXT_ALI_230_origen["ALI_230 Citación por edictos al demandado con domicilio desconocido<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_ALI_230_origen -.->|"Edictos publicados en el juicio de alimentos"| ALI_150
  EXT_ALI_900_origen["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_ALI_900_origen -.->|"Homologación denegada antes de la demanda de alimentos"| ALI_130
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Compensación económica: demanda, contestación y audiencia preliminar

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    ALI_200["<b>ALI_200</b> Demanda de compensación económica<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_210["<b>ALI_210</b> Beneficio de litigar sin gastos<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ALI_220["<b>ALI_220</b> Providencia inicial y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_230["<b>ALI_230</b> Citación por edictos al demandado con domicilio desconocido<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_240["<b>ALI_240</b> Contestación de la demanda<br/>Responsable: Alimentante u obligado<br/>10 días hábiles judiciales + gracia"]:::demandada
  end
  subgraph F_1["Audiencia preliminar"]
    ALI_300["<b>ALI_300</b> Audiencia preliminar<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_ALI_100_origen["ALI_100 Solicitud de trámite de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_ALI_100_origen -.->|"Urgencia o riesgo de caducidad: radicación directa de la compensación económica"| ALI_200
  EXT_ALI_120_origen["ALI_120 Acta de cierre de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_ALI_120_origen -.->|"Sin acuerdo sobre la compensación económica"| ALI_200
  EXT_ALI_140_origen["ALI_140 Primer auto: audiencia y alimentos provisorios<br/>(ver Juicio de alimentos)"]:::externo
  EXT_ALI_140_origen -.->|"Alimentante con domicilio desconocido"| ALI_230
  ALI_200 -->|"Demanda presentada"| ALI_220
  P_ALI_200_2(["Se abren en paralelo"]):::paralelo
  ALI_200 -->|"Demanda presentada con pedido de beneficio de litigar sin gastos"| P_ALI_200_2
  P_ALI_200_2 --> ALI_210
  P_ALI_200_2 --> ALI_220
  FIN_ALI_210_1(["Fin de este camino"]):::fin
  ALI_210 -->|"Beneficio resuelto"| FIN_ALI_210_1
  ALI_220 -->|"Traslado ordenado al domicilio conocido del demandado"| ALI_240
  ALI_220 -->|"Demandado con domicilio desconocido"| ALI_230
  EXT_ALI_150_destino["ALI_150 Audiencia del juicio de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  ALI_230 -->|"Edictos publicados en el juicio de alimentos"| EXT_ALI_150_destino
  ALI_230 -->|"Edictos publicados en el reclamo de compensación económica"| ALI_240
  ALI_240 -->|"Contesta la demanda o vence el plazo: se convoca a la audiencia preliminar"| ALI_300
  EXT_ALI_900_destino["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_300 -->|"Acuerdo en la audiencia"| EXT_ALI_900_destino
  EXT_ALI_310_destino["ALI_310 Apertura a prueba y proveído de la prueba<br/>(ver Compensación económica: prueba y vista de causa)"]:::externo
  ALI_300 -->|"Hechos controvertidos: se abre la causa a prueba"| EXT_ALI_310_destino
  EXT_ALI_490_destino["ALI_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  ALI_300 -->|"Cuestión de puro derecho"| EXT_ALI_490_destino
  EXT_ALI_990_destino["ALI_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_300 -->|"El actor no comparece sin justa causa: se lo tiene por desistido"| EXT_ALI_990_destino
  ALI_300 -->|"Audiencia diferida por fuerza mayor (única vez)"| ALI_300
  EXT_ALI_900_origen["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_ALI_900_origen -.->|"Homologación denegada antes de la demanda de compensación económica"| ALI_200
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Compensación económica: prueba y vista de causa

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    ALI_310["<b>ALI_310</b> Apertura a prueba y proveído de la prueba<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_330["<b>ALI_330</b> Asesoría Pericial: pericia contable o de tasación<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_350["<b>ALI_350</b> Prueba informativa (oficios)<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    ALI_400["<b>ALI_400</b> Fijación de la audiencia de vista de causa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_410["<b>ALI_410</b> Audiencia de vista de causa<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_ALI_300_origen["ALI_300 Audiencia preliminar<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_ALI_300_origen -.->|"Hechos controvertidos: se abre la causa a prueba"| ALI_310
  P_ALI_310_1(["Se abren en paralelo"]):::paralelo
  ALI_310 -->|"Se provee la prueba"| P_ALI_310_1
  P_ALI_310_1 --> ALI_330
  P_ALI_310_1 --> ALI_350
  P_ALI_310_1 --> ALI_400
  FIN_ALI_330_1(["Fin de este camino"]):::fin
  ALI_330 -->|"Dictamen presentado, no ordenado o desistido"| FIN_ALI_330_1
  FIN_ALI_350_1(["Fin de este camino"]):::fin
  ALI_350 -->|"Informes contestados o prueba desistida"| FIN_ALI_350_1
  ALI_400 -->|"Audiencia fijada"| ALI_410
  EXT_ALI_900_destino["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_410 -->|"Acuerdo en la audiencia"| EXT_ALI_900_destino
  EXT_ALI_490_destino["ALI_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  ALI_410 -->|"Audiencia concluida: causa para sentencia"| EXT_ALI_490_destino
  ALI_410 -->|"Audiencia suspendida por fuerza mayor"| ALI_400
  EXT_ALI_900_origen["ALI_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_ALI_900_origen -.->|"Homologación denegada con el reclamo de compensación en trámite"| ALI_310
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
    ALI_490["<b>ALI_490</b> Asesoría de Incapaces: vista previa a la sentencia<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_500["<b>ALI_500</b> Sentencia sobre la compensación económica<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_520["<b>ALI_520</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    ALI_600["<b>ALI_600</b> Recurso de apelación<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ALI_610["<b>ALI_610</b> Fundamentación de la apelación (expresión de agravios o memorial)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ALI_620["<b>ALI_620</b> Sentencia de la Cámara (Sala de Familia)<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ALI_630["<b>ALI_630</b> Recurso extraordinario ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    ALI_640["<b>ALI_640</b> Queja ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ALI_650["<b>ALI_650</b> Trámite y resolución ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_ALI_180_origen["ALI_180 Sentencia de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  EXT_ALI_180_origen -.->|"Sentencia notificada (la cuota fijada sigue en el control de pago)"| ALI_520
  EXT_ALI_180_origen -.->|"Sentencia notificada (la cuota fijada sigue en el control de pago)"| ALI_600
  EXT_ALI_300_origen["ALI_300 Audiencia preliminar<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_ALI_300_origen -.->|"Cuestión de puro derecho"| ALI_490
  EXT_ALI_410_origen["ALI_410 Audiencia de vista de causa<br/>(ver Compensación económica: prueba y vista de causa)"]:::externo
  EXT_ALI_410_origen -.->|"Audiencia concluida: causa para sentencia"| ALI_490
  ALI_490 -->|"Dictamen emitido o no corresponde la intervención"| ALI_500
  P_ALI_500_1(["Se abren en paralelo"]):::paralelo
  ALI_500 -->|"Sentencia notificada"| P_ALI_500_1
  P_ALI_500_1 --> ALI_520
  P_ALI_500_1 --> ALI_600
  FIN_ALI_520_1(["Fin de este camino"]):::fin
  ALI_520 -->|"Regulación firme o apelación resuelta"| FIN_ALI_520_1
  EXT_ALI_700_destino["ALI_700 Cumplimiento de la sentencia firme<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_600 -->|"No se apela o se deniega la apelación: sentencia firme"| EXT_ALI_700_destino
  ALI_600 -->|"Apelación concedida"| ALI_610
  ALI_610 -->|"Recurso fundado: resuelve la Cámara"| ALI_620
  ALI_610 -->|"No se funda: recurso desierto y sentencia firme"| EXT_ALI_700_destino
  ALI_620 -->|"Sentencia de la Cámara notificada"| ALI_630
  ALI_630 -->|"No se recurre: sentencia firme"| EXT_ALI_700_destino
  ALI_630 -->|"Recurso concedido"| ALI_650
  ALI_630 -->|"Recurso denegado"| ALI_640
  ALI_640 -->|"Queja admitida"| ALI_650
  ALI_640 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_ALI_700_destino
  ALI_650 -->|"La SCBA resuelve: sentencia firme"| EXT_ALI_700_destino
  ALI_650 -->|"La SCBA anula y reenvía para un nuevo pronunciamiento"| ALI_620
  EXT_ALI_820_origen["ALI_820 Resolución del incidente de cuota<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  EXT_ALI_820_origen -.->|"Resolución notificada"| ALI_520
  EXT_ALI_820_origen -.->|"Resolución notificada"| ALI_600
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Cuota, incumplimiento e incidentes

```mermaid
flowchart TD
  subgraph F_0["Cuota e incidentes"]
    ALI_720["<b>ALI_720</b> Pago de la cuota alimentaria<br/>Responsable: Alimentante u obligado<br/>Sin plazo"]:::demandada
    ALI_730["<b>ALI_730</b> Intimación de pago de cuotas atrasadas<br/>Responsable: Alimentante u obligado<br/>5 días hábiles judiciales"]:::demandada
    ALI_740["<b>ALI_740</b> Ejecución de cuotas atrasadas<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_750["<b>ALI_750</b> Empleador que no retiene o no deposita la cuota<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
    ALI_760["<b>ALI_760</b> Control de los 21 años del hijo alimentado<br/>Responsable: Quien reclama<br/>21 años"]:::actora
    ALI_800["<b>ALI_800</b> Incidente de aumento, reducción, cese o coparticipación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ALI_810["<b>ALI_810</b> Contestación del incidente<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    ALI_820["<b>ALI_820</b> Resolución del incidente de cuota<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_ALI_010_origen["ALI_010 Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_010_origen -.->|"Convenio con firmas certificadas incumplido (art. 521 inc. 7)"| ALI_740
  EXT_ALI_010_origen -.->|"Ya hay una cuota fijada por sentencia o acuerdo homologado"| ALI_720
  EXT_ALI_130_origen["ALI_130 Demanda de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  EXT_ALI_130_origen -.->|"Demanda de alimentos para un hijo"| ALI_760
  EXT_ALI_140_origen["ALI_140 Primer auto: audiencia y alimentos provisorios<br/>(ver Juicio de alimentos)"]:::externo
  EXT_ALI_140_origen -.->|"Audiencia fijada (con o sin alimentos provisorios)"| ALI_720
  ALI_720 -->|"Incumplimiento de una o más cuotas"| ALI_730
  ALI_720 -->|"El empleador no retiene o no deposita"| ALI_750
  P_ALI_720_3(["Se abren en paralelo"]):::paralelo
  ALI_720 -->|"Cambio de circunstancias: se promueve un incidente y la cuota sigue"| P_ALI_720_3
  P_ALI_720_3 --> ALI_720
  P_ALI_720_3 --> ALI_800
  EXT_ALI_990_destino["ALI_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  ALI_720 -->|"Cesa la cuota (rechazo firme, cese o fin de la obligación)"| EXT_ALI_990_destino
  ALI_730 -->|"Paga dentro del plazo"| ALI_720
  ALI_730 -->|"No paga: embargo, venta y registro de deudores"| ALI_740
  ALI_740 -->|"Deuda cancelada: la cuota sigue en curso"| ALI_720
  ALI_740 -->|"Deuda cancelada y no hay cuota en curso"| EXT_ALI_990_destino
  ALI_750 -->|"El empleador deposita"| ALI_720
  ALI_750 -->|"No deposita: se lo ejecuta junto con el alimentante"| ALI_740
  ALI_760 -->|"El hijo estudia: se pide la extensión hasta los 25 años"| ALI_800
  FIN_ALI_760_2(["Fin de este camino"]):::fin
  ALI_760 -->|"Cesa la obligación a los 21 años, o el reclamo terminó antes"| FIN_ALI_760_2
  ALI_800 -->|"Incidente promovido: se corre traslado"| ALI_810
  ALI_810 -->|"Contestado o plazo vencido"| ALI_820
  P_ALI_820_1(["Se abren en paralelo"]):::paralelo
  ALI_820 -->|"Resolución notificada"| P_ALI_820_1
  EXT_ALI_520_destino["ALI_520 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_ALI_820_1 --> EXT_ALI_520_destino
  EXT_ALI_600_destino["ALI_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  P_ALI_820_1 --> EXT_ALI_600_destino
  EXT_ALI_910_origen["ALI_910 Cumplimiento del acuerdo homologado<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_ALI_910_origen -.->|"Acuerdo de alimentos homologado antes de la demanda"| ALI_720
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Cumplimiento, acuerdo y cierre

```mermaid
flowchart TD
  subgraph F_0["Ejecución"]
    ALI_700["<b>ALI_700</b> Cumplimiento de la sentencia firme<br/>Responsable: Alimentante u obligado<br/>Sin plazo"]:::demandada
    ALI_710["<b>ALI_710</b> Ejecución de la sentencia<br/>Responsable: Quien reclama<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    ALI_900["<b>ALI_900</b> Acuerdo y homologación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ALI_910["<b>ALI_910</b> Cumplimiento del acuerdo homologado<br/>Responsable: Alimentante u obligado<br/>Sin plazo"]:::demandada
  end
  subgraph F_2["Cierre"]
    ALI_990["<b>ALI_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_ALI_010_origen["ALI_010 Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_010_origen -.->|"Convenio fuera del expediente que se quiere homologar"| ALI_900
  EXT_ALI_020_origen["ALI_020 Interpelación fehaciente al alimentante<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_020_origen -.->|"El alimentante propone un acuerdo"| ALI_900
  EXT_ALI_040_origen["ALI_040 Control de caducidad de la compensación económica<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ALI_040_origen -.->|"Vencido sin demanda: la acción caducó"| ALI_990
  EXT_ALI_120_origen["ALI_120 Acta de cierre de la etapa previa<br/>(ver Etapa previa ante el Consejero de Familia)"]:::externo
  EXT_ALI_120_origen -.->|"Acuerdo"| ALI_900
  EXT_ALI_150_origen["ALI_150 Audiencia del juicio de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  EXT_ALI_150_origen -.->|"Acuerdo: el juez lo homologa en el acto"| ALI_910
  EXT_ALI_150_origen -.->|"La actora no comparece a la segunda audiencia: se la tiene por desistida"| ALI_990
  EXT_ALI_300_origen["ALI_300 Audiencia preliminar<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_ALI_300_origen -.->|"Acuerdo en la audiencia"| ALI_900
  EXT_ALI_300_origen -.->|"El actor no comparece sin justa causa: se lo tiene por desistido"| ALI_990
  EXT_ALI_410_origen["ALI_410 Audiencia de vista de causa<br/>(ver Compensación económica: prueba y vista de causa)"]:::externo
  EXT_ALI_410_origen -.->|"Acuerdo en la audiencia"| ALI_900
  EXT_ALI_600_origen["ALI_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ALI_600_origen -.->|"No se apela o se deniega la apelación: sentencia firme"| ALI_700
  EXT_ALI_610_origen["ALI_610 Fundamentación de la apelación (expresión de agravios o memorial)<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ALI_610_origen -.->|"No se funda: recurso desierto y sentencia firme"| ALI_700
  EXT_ALI_630_origen["ALI_630 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ALI_630_origen -.->|"No se recurre: sentencia firme"| ALI_700
  EXT_ALI_640_origen["ALI_640 Queja ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ALI_640_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| ALI_700
  EXT_ALI_650_origen["ALI_650 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_ALI_650_origen -.->|"La SCBA resuelve: sentencia firme"| ALI_700
  ALI_700 -->|"Compensación económica cumplida"| ALI_990
  ALI_700 -->|"Compensación económica incumplida"| ALI_710
  FIN_ALI_700_3(["Fin de este camino"]):::fin
  ALI_700 -->|"Alimentos: la cuota sigue en curso con lo resuelto en firme"| FIN_ALI_700_3
  ALI_710 -->|"Sentencia cumplida o crédito cobrado"| ALI_990
  EXT_ALI_720_origen["ALI_720 Pago de la cuota alimentaria<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  EXT_ALI_720_origen -.->|"Cesa la cuota (rechazo firme, cese o fin de la obligación)"| ALI_990
  EXT_ALI_740_origen["ALI_740 Ejecución de cuotas atrasadas<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  EXT_ALI_740_origen -.->|"Deuda cancelada y no hay cuota en curso"| ALI_990
  ALI_900 -->|"Acuerdo homologado"| ALI_910
  EXT_ALI_130_destino["ALI_130 Demanda de alimentos<br/>(ver Juicio de alimentos)"]:::externo
  ALI_900 -->|"Homologación denegada antes de la demanda de alimentos"| EXT_ALI_130_destino
  EXT_ALI_200_destino["ALI_200 Demanda de compensación económica<br/>(ver Compensación económica: demanda, contestación y audiencia preliminar)"]:::externo
  ALI_900 -->|"Homologación denegada antes de la demanda de compensación económica"| EXT_ALI_200_destino
  EXT_ALI_310_destino["ALI_310 Apertura a prueba y proveído de la prueba<br/>(ver Compensación económica: prueba y vista de causa)"]:::externo
  ALI_900 -->|"Homologación denegada con el reclamo de compensación en trámite"| EXT_ALI_310_destino
  FIN_ALI_910_1(["Fin de este camino"]):::fin
  ALI_910 -->|"Acuerdo de alimentos homologado en la audiencia: sigue el control de la cuota"| FIN_ALI_910_1
  EXT_ALI_720_destino["ALI_720 Pago de la cuota alimentaria<br/>(ver Cuota, incumplimiento e incidentes)"]:::externo
  ALI_910 -->|"Acuerdo de alimentos homologado antes de la demanda"| EXT_ALI_720_destino
  ALI_910 -->|"Acuerdo de compensación económica cumplido"| ALI_990
  ALI_910 -->|"Acuerdo de compensación económica incumplido: se ejecuta"| ALI_710
  style ALI_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
