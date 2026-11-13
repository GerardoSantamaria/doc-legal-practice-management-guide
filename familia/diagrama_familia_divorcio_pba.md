# Diagrama de Flujo: Divorcio (PBA)

**Régimen:** CPCCBA (Decreto-Ley 7425/68), Libro VIII: proceso ante los Juzgados de Familia (arts. 827 a 853, texto de las Leyes 13.634 y 15.513); CCyC, arts. 435 a 445, 480, 496 a 500, 717, 721, 722, 2621 y 2626 · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_familia_divorcio_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el cónyuge que pide el divorcio o promueve la cuestión (ACTORA); naranja = el otro cónyuge (DEMANDADA); gris = juzgado, Consejero, Asesoría de Incapaces o Registro de las Personas, aclarado en el nombre (TRIBUNAL); violeta = los dos cónyuges o cualquiera de ellos (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, al dictarse la sentencia de divorcio corren a la vez la apelación, la apelación de los honorarios, la caducidad de la compensación económica y las cuestiones que quedaron pendientes.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un registro). La app los separa en el flujo prejudicial.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Petición de divorcio<br/>6 hitos"]
  FASE_3["Efectos del divorcio<br/>5 hitos"]
  FASE_4["Consejero de Familia<br/>3 hitos"]
  FASE_5["Postulación<br/>4 hitos"]
  FASE_6["Audiencia preliminar<br/>1 hito"]
  FASE_7["Prueba<br/>4 hitos"]
  FASE_8["Vista de causa<br/>2 hitos"]
  FASE_9["Sentencia<br/>3 hitos"]
  FASE_10["Recursos<br/>6 hitos"]
  FASE_11["Ejecución<br/>2 hitos"]
  FASE_12["Acuerdo<br/>4 hitos"]
  FASE_13["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_13
  FASE_1 --> FASE_2
  FASE_4 --> FASE_5
  FASE_4 --> FASE_12
  FASE_2 --> FASE_5
  FASE_2 --> FASE_9
  FASE_2 --> FASE_10
  FASE_2 --> FASE_3
  FASE_2 --> FASE_12
  FASE_5 --> FASE_2
  FASE_5 --> FASE_6
  FASE_6 --> FASE_12
  FASE_6 --> FASE_7
  FASE_6 --> FASE_9
  FASE_6 --> FASE_13
  FASE_7 --> FASE_8
  FASE_7 --> FASE_12
  FASE_8 --> FASE_7
  FASE_8 --> FASE_12
  FASE_8 --> FASE_9
  FASE_9 --> FASE_10
  FASE_10 --> FASE_11
  FASE_11 --> FASE_3
  FASE_11 --> FASE_13
  FASE_3 --> FASE_13
  FASE_3 --> FASE_4
  FASE_3 --> FASE_12
  FASE_12 --> FASE_5
  FASE_12 --> FASE_7
  FASE_12 --> FASE_13
  FASE_12 --> FASE_11
  FASE_12 --> FASE_3
  FASE_12 --> FASE_4
```

## 1. Etapa previa (antes de promover)

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    DIV_010["INICIO - <b>DIV_010</b> Consulta sobre el divorcio<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_020["<b>DIV_020</b> Matrimonio celebrado en el extranjero: jurisdicción y ley aplicable<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_030["<b>DIV_030</b> Relevamiento y redacción de la propuesta reguladora<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_040["<b>DIV_040</b> Medidas provisionales urgentes antes de la petición<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_050["<b>DIV_050</b> Plazo para presentar la petición después de trabadas las medidas<br/>Responsable: Cónyuge que pide<br/>10 días hábiles judiciales"]:::actora
  end
  DIV_010 -->|"Matrimonio celebrado en el extranjero"| DIV_020
  DIV_010 -->|"Se prepara la petición (unilateral o conjunta)"| DIV_030
  P_DIV_010_3(["Se abren en paralelo"]):::paralelo
  DIV_010 -->|"Urgencia: hay que proteger personas o bienes antes de presentar la petición"| P_DIV_010_3
  P_DIV_010_3 --> DIV_030
  P_DIV_010_3 --> DIV_040
  DIV_020 -->|"Hay jurisdicción en la provincia"| DIV_030
  EXT_DIV_990_destino["DIV_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_020 -->|"No hay jurisdicción en la provincia: se informa al cliente"| EXT_DIV_990_destino
  EXT_DIV_140_destino["DIV_140 Petición unilateral de divorcio con propuesta reguladora<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  DIV_030 -->|"Petición unilateral"| EXT_DIV_140_destino
  EXT_DIV_150_destino["DIV_150 Petición conjunta de divorcio con convenio regulador<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  DIV_030 -->|"Petición conjunta con convenio regulador"| EXT_DIV_150_destino
  DIV_040 -->|"Medidas dictadas y trabadas"| DIV_050
  FIN_DIV_040_2(["Fin de este camino"]):::fin
  DIV_040 -->|"Medidas rechazadas"| FIN_DIV_040_2
  FIN_DIV_050_1(["Fin de este camino"]):::fin
  DIV_050 -->|"Petición presentada, o plazo vencido (las medidas caducan)"| FIN_DIV_050_1
  style DIV_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Petición, audiencia y sentencia de divorcio

```mermaid
flowchart TD
  subgraph F_0["Petición de divorcio"]
    DIV_140["<b>DIV_140</b> Petición unilateral de divorcio con propuesta reguladora<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_150["<b>DIV_150</b> Petición conjunta de divorcio con convenio regulador<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
    DIV_160["<b>DIV_160</b> Providencia inicial y traslado de la propuesta reguladora<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_170["<b>DIV_170</b> Contrapropuesta reguladora del otro cónyuge<br/>Responsable: Otro cónyuge<br/>5 días hábiles judiciales + gracia"]:::demandada
    DIV_180["<b>DIV_180</b> Audiencia del art. 438 CCyC<br/>Responsable: Ambos cónyuges o cualquiera<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DIV_190["<b>DIV_190</b> Sentencia de divorcio<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_DIV_030_origen["DIV_030 Relevamiento y redacción de la propuesta reguladora<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_DIV_030_origen -.->|"Petición unilateral"| DIV_140
  EXT_DIV_030_origen -.->|"Petición conjunta con convenio regulador"| DIV_150
  DIV_140 -->|"Petición presentada"| DIV_160
  DIV_150 -->|"Petición presentada"| DIV_160
  DIV_160 -->|"Petición unilateral: traslado al otro cónyuge en su domicilio real"| DIV_170
  EXT_DIV_230_destino["DIV_230 Citación por edictos al demandado con domicilio desconocido<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  DIV_160 -->|"Petición unilateral con el otro cónyuge en domicilio desconocido"| EXT_DIV_230_destino
  DIV_160 -->|"Petición conjunta: se fija la audiencia"| DIV_180
  DIV_160 -->|"Falta la propuesta reguladora o los elementos: no se da trámite hasta completarla"| DIV_140
  DIV_170 -->|"Contrapropuesta presentada, adhesión o plazo vencido: se fija la audiencia"| DIV_180
  DIV_180 -->|"Audiencia celebrada (con acuerdo total, parcial o sin acuerdo)"| DIV_190
  DIV_180 -->|"Audiencia diferida"| DIV_180
  P_DIV_190_1(["Se abren en paralelo"]):::paralelo
  DIV_190 -->|"Divorcio decretado con el convenio regulador homologado en todos sus puntos"| P_DIV_190_1
  EXT_DIV_520_destino["DIV_520 Apelación de la regulación de honorarios<br/>(ver Sentencia y recursos)"]:::externo
  P_DIV_190_1 --> EXT_DIV_520_destino
  EXT_DIV_600_destino["DIV_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  P_DIV_190_1 --> EXT_DIV_600_destino
  EXT_DIV_820_destino["DIV_820 Control de caducidad de la compensación económica<br/>(ver Efectos del divorcio)"]:::externo
  P_DIV_190_1 --> EXT_DIV_820_destino
  EXT_DIV_910_destino["DIV_910 Cumplimiento del acuerdo homologado<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  P_DIV_190_1 --> EXT_DIV_910_destino
  P_DIV_190_2(["Se abren en paralelo"]):::paralelo
  DIV_190 -->|"Divorcio decretado con cuestiones pendientes (desacuerdo o convenio parcial)"| P_DIV_190_2
  P_DIV_190_2 --> EXT_DIV_520_destino
  P_DIV_190_2 --> EXT_DIV_600_destino
  P_DIV_190_2 --> EXT_DIV_820_destino
  EXT_DIV_830_destino["DIV_830 Cuestiones pendientes del convenio regulador<br/>(ver Efectos del divorcio)"]:::externo
  P_DIV_190_2 --> EXT_DIV_830_destino
  EXT_DIV_230_origen["DIV_230 Citación por edictos al demandado con domicilio desconocido<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_DIV_230_origen -.->|"Edictos publicados en la petición unilateral de divorcio"| DIV_170
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Efectos del divorcio

```mermaid
flowchart TD
  subgraph F_0["Efectos del divorcio"]
    DIV_810["<b>DIV_810</b> Inscripción de la sentencia de divorcio en el Registro de las Personas<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_820["<b>DIV_820</b> Control de caducidad de la compensación económica<br/>Responsable: Cónyuge que pide<br/>6 meses"]:::actora
    DIV_830["<b>DIV_830</b> Cuestiones pendientes del convenio regulador<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
    DIV_840["<b>DIV_840</b> Vigencia de la atribución del uso de la vivienda familiar<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_850["<b>DIV_850</b> Liquidación y partición de la comunidad<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
  end
  EXT_DIV_190_origen["DIV_190 Sentencia de divorcio<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  EXT_DIV_190_origen -.->|"Divorcio decretado con el convenio regulador homologado en todos sus puntos"| DIV_820
  EXT_DIV_190_origen -.->|"Divorcio decretado con cuestiones pendientes (desacuerdo o convenio parcial)"| DIV_820
  EXT_DIV_190_origen -.->|"Divorcio decretado con cuestiones pendientes (desacuerdo o convenio parcial)"| DIV_830
  EXT_DIV_700_origen["DIV_700 Sentencia firme: inscripción del divorcio o cumplimiento de lo resuelto<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_DIV_700_origen -.->|"Sentencia de divorcio firme: se ordena su inscripción"| DIV_810
  EXT_DIV_700_origen -.->|"Se atribuyó el uso de la vivienda: se controla su vigencia"| DIV_840
  FIN_DIV_810_1(["Fin de este camino"]):::fin
  DIV_810 -->|"Sentencia inscripta"| FIN_DIV_810_1
  EXT_DIV_970_destino["DIV_970 Sigue en la matriz de alimentos y compensación económica<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_820 -->|"Se va a reclamar la compensación económica"| EXT_DIV_970_destino
  FIN_DIV_820_2(["Fin de este camino"]):::fin
  DIV_820 -->|"Vence sin reclamo, o la compensación ya se resolvió en el convenio"| FIN_DIV_820_2
  DIV_830 -->|"Alimentos o compensación económica pendientes"| EXT_DIV_970_destino
  EXT_DIV_980_destino["DIV_980 Sigue en la matriz de cuidado personal y régimen de comunicación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_830 -->|"Cuidado personal o régimen de comunicación pendientes"| EXT_DIV_980_destino
  P_DIV_830_3(["Se abren en paralelo"]):::paralelo
  DIV_830 -->|"Alimentos y cuidado de los hijos pendientes"| P_DIV_830_3
  P_DIV_830_3 --> EXT_DIV_970_destino
  P_DIV_830_3 --> EXT_DIV_980_destino
  EXT_DIV_100_destino["DIV_100 Solicitud de trámite de la etapa previa<br/>(ver Cuestiones pendientes: etapa previa ante el Consejero de Familia)"]:::externo
  DIV_830 -->|"Atribución de la vivienda familiar pendiente"| EXT_DIV_100_destino
  DIV_830 -->|"Distribución de los bienes pendiente"| DIV_850
  EXT_DIV_900_destino["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_830 -->|"Acuerdo posterior sobre lo pendiente"| EXT_DIV_900_destino
  EXT_DIV_990_destino["DIV_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_840 -->|"Cesa la atribución (plazo cumplido, cambio de circunstancias o indignidad)"| EXT_DIV_990_destino
  DIV_840 -->|"Se discute el cese o la modificación de la atribución"| EXT_DIV_100_destino
  DIV_850 -->|"Partición acordada"| EXT_DIV_900_destino
  DIV_850 -->|"Sin acuerdo: se promueve la liquidación ante el juzgado"| EXT_DIV_100_destino
  EXT_DIV_910_origen["DIV_910 Cumplimiento del acuerdo homologado<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_DIV_910_origen -.->|"El convenio atribuye el uso de la vivienda: se controla su vigencia"| DIV_840
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Cuestiones pendientes: etapa previa ante el Consejero de Familia

```mermaid
flowchart TD
  subgraph F_0["Consejero de Familia"]
    DIV_100["<b>DIV_100</b> Solicitud de trámite de la etapa previa<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_110["<b>DIV_110</b> Audiencias ante el Consejero de Familia<br/>Responsable: Ambos cónyuges o cualquiera<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    DIV_120["<b>DIV_120</b> Acta de cierre de la etapa previa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  DIV_100 -->|"Etapa previa admitida: el Consejero cita a las partes"| DIV_110
  EXT_DIV_200_destino["DIV_200 Demanda sobre las cuestiones pendientes del divorcio (vivienda o bienes)<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  DIV_100 -->|"Asunto urgente o etapa improcedente: el juez dispone la radicación directa"| EXT_DIV_200_destino
  DIV_110 -->|"Conciliación, fracaso o intervención agotada: el Consejero labra el acta"| DIV_120
  DIV_110 -->|"Una parte pide concluir la etapa y el juez la da por concluida"| DIV_120
  DIV_110 -->|"El juez dispone continuar la etapa (hasta 15 días)"| DIV_110
  EXT_DIV_900_destino["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_120 -->|"Acuerdo"| EXT_DIV_900_destino
  DIV_120 -->|"Sin acuerdo: quedan expeditas las acciones"| EXT_DIV_200_destino
  EXT_DIV_830_origen["DIV_830 Cuestiones pendientes del convenio regulador<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_830_origen -.->|"Atribución de la vivienda familiar pendiente"| DIV_100
  EXT_DIV_840_origen["DIV_840 Vigencia de la atribución del uso de la vivienda familiar<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_840_origen -.->|"Se discute el cese o la modificación de la atribución"| DIV_100
  EXT_DIV_850_origen["DIV_850 Liquidación y partición de la comunidad<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_850_origen -.->|"Sin acuerdo: se promueve la liquidación ante el juzgado"| DIV_100
  EXT_DIV_910_origen["DIV_910 Cumplimiento del acuerdo homologado<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_DIV_910_origen -.->|"Cambio sustancial de la situación: se pide la revisión del convenio (art. 440)"| DIV_100
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Cuestiones pendientes: demanda, contestación y audiencia preliminar

```mermaid
flowchart TD
  subgraph F_0["Postulación"]
    DIV_200["<b>DIV_200</b> Demanda sobre las cuestiones pendientes del divorcio (vivienda o bienes)<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_220["<b>DIV_220</b> Providencia inicial y traslado de la demanda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_230["<b>DIV_230</b> Citación por edictos al demandado con domicilio desconocido<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_240["<b>DIV_240</b> Contestación de la demanda<br/>Responsable: Otro cónyuge<br/>10 días hábiles judiciales + gracia"]:::demandada
  end
  subgraph F_1["Audiencia preliminar"]
    DIV_300["<b>DIV_300</b> Audiencia preliminar<br/>Responsable: Ambos cónyuges o cualquiera<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_DIV_100_origen["DIV_100 Solicitud de trámite de la etapa previa<br/>(ver Cuestiones pendientes: etapa previa ante el Consejero de Familia)"]:::externo
  EXT_DIV_100_origen -.->|"Asunto urgente o etapa improcedente: el juez dispone la radicación directa"| DIV_200
  EXT_DIV_120_origen["DIV_120 Acta de cierre de la etapa previa<br/>(ver Cuestiones pendientes: etapa previa ante el Consejero de Familia)"]:::externo
  EXT_DIV_120_origen -.->|"Sin acuerdo: quedan expeditas las acciones"| DIV_200
  EXT_DIV_160_origen["DIV_160 Providencia inicial y traslado de la propuesta reguladora<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  EXT_DIV_160_origen -.->|"Petición unilateral con el otro cónyuge en domicilio desconocido"| DIV_230
  DIV_200 -->|"Demanda presentada"| DIV_220
  DIV_220 -->|"Traslado ordenado al domicilio conocido del demandado"| DIV_240
  DIV_220 -->|"Demandado con domicilio desconocido"| DIV_230
  EXT_DIV_170_destino["DIV_170 Contrapropuesta reguladora del otro cónyuge<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  DIV_230 -->|"Edictos publicados en la petición unilateral de divorcio"| EXT_DIV_170_destino
  DIV_230 -->|"Edictos publicados en la demanda sobre cuestiones pendientes"| DIV_240
  DIV_240 -->|"Contesta (con o sin reconvención) o vence el plazo: se convoca a la audiencia preliminar"| DIV_300
  EXT_DIV_900_destino["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_300 -->|"Acuerdo en la audiencia"| EXT_DIV_900_destino
  EXT_DIV_310_destino["DIV_310 Apertura a prueba y proveído de la prueba<br/>(ver Cuestiones pendientes: prueba y vista de causa)"]:::externo
  DIV_300 -->|"Hechos controvertidos: se abre la causa a prueba"| EXT_DIV_310_destino
  EXT_DIV_490_destino["DIV_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  DIV_300 -->|"Cuestión de puro derecho"| EXT_DIV_490_destino
  EXT_DIV_990_destino["DIV_990 Archivo del expediente<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_300 -->|"El actor no comparece sin justa causa: se lo tiene por desistido"| EXT_DIV_990_destino
  DIV_300 -->|"Audiencia diferida por fuerza mayor (única vez)"| DIV_300
  EXT_DIV_900_origen["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_DIV_900_origen -.->|"Homologación denegada antes de la demanda"| DIV_200
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Cuestiones pendientes: prueba y vista de causa

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    DIV_310["<b>DIV_310</b> Apertura a prueba y proveído de la prueba<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_330["<b>DIV_330</b> Asesoría Pericial: tasación de bienes<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_350["<b>DIV_350</b> Prueba informativa (oficios)<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
    DIV_370["<b>DIV_370</b> Incorporación de la prueba previa a la vista de causa<br/>Responsable: Ambos cónyuges o cualquiera<br/>10 días hábiles de anticipación"]:::ambas
  end
  subgraph F_1["Vista de causa"]
    DIV_400["<b>DIV_400</b> Fijación de la audiencia de vista de causa<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_410["<b>DIV_410</b> Audiencia de vista de causa<br/>Responsable: Ambos cónyuges o cualquiera<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  EXT_DIV_300_origen["DIV_300 Audiencia preliminar<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_DIV_300_origen -.->|"Hechos controvertidos: se abre la causa a prueba"| DIV_310
  P_DIV_310_1(["Se abren en paralelo"]):::paralelo
  DIV_310 -->|"Se provee la prueba"| P_DIV_310_1
  P_DIV_310_1 --> DIV_330
  P_DIV_310_1 --> DIV_350
  P_DIV_310_1 --> DIV_400
  EXT_DIV_950_destino["DIV_950 Control de caducidad de instancia<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  P_DIV_310_1 --> EXT_DIV_950_destino
  FIN_DIV_330_1(["Fin de este camino"]):::fin
  DIV_330 -->|"Dictamen presentado, no ordenado o desistido"| FIN_DIV_330_1
  FIN_DIV_350_1(["Fin de este camino"]):::fin
  DIV_350 -->|"Informes contestados o prueba desistida"| FIN_DIV_350_1
  FIN_DIV_370_1(["Fin de este camino"]):::fin
  DIV_370 -->|"Prueba incorporada o se prescinde de la pendiente"| FIN_DIV_370_1
  P_DIV_400_1(["Se abren en paralelo"]):::paralelo
  DIV_400 -->|"Audiencia fijada"| P_DIV_400_1
  P_DIV_400_1 --> DIV_370
  P_DIV_400_1 --> DIV_410
  EXT_DIV_900_destino["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_410 -->|"Acuerdo en la audiencia"| EXT_DIV_900_destino
  EXT_DIV_490_destino["DIV_490 Asesoría de Incapaces: vista previa a la sentencia<br/>(ver Sentencia y recursos)"]:::externo
  DIV_410 -->|"Audiencia concluida: causa para sentencia"| EXT_DIV_490_destino
  DIV_410 -->|"Audiencia suspendida por fuerza mayor"| DIV_400
  EXT_DIV_900_origen["DIV_900 Acuerdo y homologación<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  EXT_DIV_900_origen -.->|"Homologación denegada con el juicio en trámite"| DIV_310
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Sentencia y recursos

```mermaid
flowchart TD
  subgraph F_0["Sentencia"]
    DIV_490["<b>DIV_490</b> Asesoría de Incapaces: vista previa a la sentencia<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_500["<b>DIV_500</b> Sentencia sobre las cuestiones pendientes<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_520["<b>DIV_520</b> Apelación de la regulación de honorarios<br/>Responsable: Ambos cónyuges o cualquiera<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  subgraph F_1["Recursos"]
    DIV_600["<b>DIV_600</b> Recurso de apelación<br/>Responsable: Ambos cónyuges o cualquiera<br/>5 días hábiles judiciales + gracia"]:::ambas
    DIV_610["<b>DIV_610</b> Fundamentación de la apelación (expresión de agravios o memorial)<br/>Responsable: Ambos cónyuges o cualquiera<br/>5 días hábiles judiciales + gracia"]:::ambas
    DIV_620["<b>DIV_620</b> Sentencia de la Cámara (Sala de Familia)<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    DIV_630["<b>DIV_630</b> Recurso extraordinario ante la SCBA<br/>Responsable: Ambos cónyuges o cualquiera<br/>10 días hábiles judiciales + gracia"]:::ambas
    DIV_640["<b>DIV_640</b> Queja ante la SCBA<br/>Responsable: Ambos cónyuges o cualquiera<br/>5 días hábiles judiciales + gracia"]:::ambas
    DIV_650["<b>DIV_650</b> Trámite y resolución ante la SCBA<br/>Responsable: Ambos cónyuges o cualquiera<br/>10 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_DIV_190_origen["DIV_190 Sentencia de divorcio<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  EXT_DIV_190_origen -.->|"Divorcio decretado con el convenio regulador homologado en todos sus puntos"| DIV_520
  EXT_DIV_190_origen -.->|"Divorcio decretado con el convenio regulador homologado en todos sus puntos"| DIV_600
  EXT_DIV_190_origen -.->|"Divorcio decretado con cuestiones pendientes (desacuerdo o convenio parcial)"| DIV_520
  EXT_DIV_190_origen -.->|"Divorcio decretado con cuestiones pendientes (desacuerdo o convenio parcial)"| DIV_600
  EXT_DIV_300_origen["DIV_300 Audiencia preliminar<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_DIV_300_origen -.->|"Cuestión de puro derecho"| DIV_490
  EXT_DIV_410_origen["DIV_410 Audiencia de vista de causa<br/>(ver Cuestiones pendientes: prueba y vista de causa)"]:::externo
  EXT_DIV_410_origen -.->|"Audiencia concluida: causa para sentencia"| DIV_490
  DIV_490 -->|"Dictamen emitido o no corresponde la intervención"| DIV_500
  P_DIV_500_1(["Se abren en paralelo"]):::paralelo
  DIV_500 -->|"Sentencia notificada"| P_DIV_500_1
  P_DIV_500_1 --> DIV_520
  P_DIV_500_1 --> DIV_600
  FIN_DIV_520_1(["Fin de este camino"]):::fin
  DIV_520 -->|"Regulación firme o apelación resuelta"| FIN_DIV_520_1
  EXT_DIV_700_destino["DIV_700 Sentencia firme: inscripción del divorcio o cumplimiento de lo resuelto<br/>(ver Cumplimiento, acuerdo y cierre)"]:::externo
  DIV_600 -->|"No se apela o se deniega la apelación: sentencia firme"| EXT_DIV_700_destino
  DIV_600 -->|"Apelación concedida"| DIV_610
  DIV_610 -->|"Recurso fundado: resuelve la Cámara"| DIV_620
  DIV_610 -->|"No se funda: recurso desierto y sentencia firme"| EXT_DIV_700_destino
  DIV_620 -->|"Sentencia de la Cámara notificada"| DIV_630
  DIV_630 -->|"No se recurre: sentencia firme"| EXT_DIV_700_destino
  DIV_630 -->|"Recurso concedido"| DIV_650
  DIV_630 -->|"Recurso denegado"| DIV_640
  DIV_640 -->|"Queja admitida"| DIV_650
  DIV_640 -->|"Queja rechazada o no interpuesta: sentencia firme"| EXT_DIV_700_destino
  DIV_650 -->|"La SCBA resuelve: sentencia firme"| EXT_DIV_700_destino
  DIV_650 -->|"La SCBA anula y reenvía para un nuevo pronunciamiento"| DIV_620
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
    DIV_700["<b>DIV_700</b> Sentencia firme: inscripción del divorcio o cumplimiento de lo resuelto<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
    DIV_710["<b>DIV_710</b> Ejecución de la sentencia<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Acuerdo"]
    DIV_900["<b>DIV_900</b> Acuerdo y homologación<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
    DIV_910["<b>DIV_910</b> Cumplimiento del acuerdo homologado<br/>Responsable: Otro cónyuge<br/>Sin plazo"]:::demandada
    DIV_950["<b>DIV_950</b> Control de caducidad de instancia<br/>Responsable: Cónyuge que pide<br/>3 meses"]:::actora
    DIV_960["<b>DIV_960</b> Intimación previa a la caducidad de instancia<br/>Responsable: Cónyuge que pide<br/>5 días hábiles judiciales + gracia"]:::actora
  end
  subgraph F_2["Cierre"]
    DIV_970["<b>DIV_970</b> Sigue en la matriz de alimentos y compensación económica<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_980["<b>DIV_980</b> Sigue en la matriz de cuidado personal y régimen de comunicación<br/>Responsable: Cónyuge que pide<br/>Sin plazo"]:::actora
    DIV_990["<b>DIV_990</b> Archivo del expediente<br/>Responsable: Ambos cónyuges o cualquiera<br/>Sin plazo"]:::ambas
  end
  EXT_DIV_020_origen["DIV_020 Matrimonio celebrado en el extranjero: jurisdicción y ley aplicable<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_DIV_020_origen -.->|"No hay jurisdicción en la provincia: se informa al cliente"| DIV_990
  EXT_DIV_120_origen["DIV_120 Acta de cierre de la etapa previa<br/>(ver Cuestiones pendientes: etapa previa ante el Consejero de Familia)"]:::externo
  EXT_DIV_120_origen -.->|"Acuerdo"| DIV_900
  EXT_DIV_190_origen["DIV_190 Sentencia de divorcio<br/>(ver Petición, audiencia y sentencia de divorcio)"]:::externo
  EXT_DIV_190_origen -.->|"Divorcio decretado con el convenio regulador homologado en todos sus puntos"| DIV_910
  EXT_DIV_300_origen["DIV_300 Audiencia preliminar<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  EXT_DIV_300_origen -.->|"Acuerdo en la audiencia"| DIV_900
  EXT_DIV_300_origen -.->|"El actor no comparece sin justa causa: se lo tiene por desistido"| DIV_990
  EXT_DIV_310_origen["DIV_310 Apertura a prueba y proveído de la prueba<br/>(ver Cuestiones pendientes: prueba y vista de causa)"]:::externo
  EXT_DIV_310_origen -.->|"Se provee la prueba"| DIV_950
  EXT_DIV_410_origen["DIV_410 Audiencia de vista de causa<br/>(ver Cuestiones pendientes: prueba y vista de causa)"]:::externo
  EXT_DIV_410_origen -.->|"Acuerdo en la audiencia"| DIV_900
  EXT_DIV_600_origen["DIV_600 Recurso de apelación<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DIV_600_origen -.->|"No se apela o se deniega la apelación: sentencia firme"| DIV_700
  EXT_DIV_610_origen["DIV_610 Fundamentación de la apelación (expresión de agravios o memorial)<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DIV_610_origen -.->|"No se funda: recurso desierto y sentencia firme"| DIV_700
  EXT_DIV_630_origen["DIV_630 Recurso extraordinario ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DIV_630_origen -.->|"No se recurre: sentencia firme"| DIV_700
  EXT_DIV_640_origen["DIV_640 Queja ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DIV_640_origen -.->|"Queja rechazada o no interpuesta: sentencia firme"| DIV_700
  EXT_DIV_650_origen["DIV_650 Trámite y resolución ante la SCBA<br/>(ver Sentencia y recursos)"]:::externo
  EXT_DIV_650_origen -.->|"La SCBA resuelve: sentencia firme"| DIV_700
  EXT_DIV_810_destino["DIV_810 Inscripción de la sentencia de divorcio en el Registro de las Personas<br/>(ver Efectos del divorcio)"]:::externo
  DIV_700 -->|"Sentencia de divorcio firme: se ordena su inscripción"| EXT_DIV_810_destino
  EXT_DIV_840_destino["DIV_840 Vigencia de la atribución del uso de la vivienda familiar<br/>(ver Efectos del divorcio)"]:::externo
  DIV_700 -->|"Se atribuyó el uso de la vivienda: se controla su vigencia"| EXT_DIV_840_destino
  DIV_700 -->|"Sentencia sobre las cuestiones pendientes cumplida"| DIV_990
  DIV_700 -->|"Sentencia sobre las cuestiones pendientes incumplida"| DIV_710
  DIV_710 -->|"Sentencia cumplida o crédito cobrado"| DIV_990
  EXT_DIV_820_origen["DIV_820 Control de caducidad de la compensación económica<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_820_origen -.->|"Se va a reclamar la compensación económica"| DIV_970
  EXT_DIV_830_origen["DIV_830 Cuestiones pendientes del convenio regulador<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_830_origen -.->|"Alimentos o compensación económica pendientes"| DIV_970
  EXT_DIV_830_origen -.->|"Cuidado personal o régimen de comunicación pendientes"| DIV_980
  EXT_DIV_830_origen -.->|"Alimentos y cuidado de los hijos pendientes"| DIV_970
  EXT_DIV_830_origen -.->|"Alimentos y cuidado de los hijos pendientes"| DIV_980
  EXT_DIV_830_origen -.->|"Acuerdo posterior sobre lo pendiente"| DIV_900
  EXT_DIV_840_origen["DIV_840 Vigencia de la atribución del uso de la vivienda familiar<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_840_origen -.->|"Cesa la atribución (plazo cumplido, cambio de circunstancias o indignidad)"| DIV_990
  EXT_DIV_850_origen["DIV_850 Liquidación y partición de la comunidad<br/>(ver Efectos del divorcio)"]:::externo
  EXT_DIV_850_origen -.->|"Partición acordada"| DIV_900
  DIV_900 -->|"Acuerdo homologado"| DIV_910
  EXT_DIV_200_destino["DIV_200 Demanda sobre las cuestiones pendientes del divorcio (vivienda o bienes)<br/>(ver Cuestiones pendientes: demanda, contestación y audiencia preliminar)"]:::externo
  DIV_900 -->|"Homologación denegada antes de la demanda"| EXT_DIV_200_destino
  EXT_DIV_310_destino["DIV_310 Apertura a prueba y proveído de la prueba<br/>(ver Cuestiones pendientes: prueba y vista de causa)"]:::externo
  DIV_900 -->|"Homologación denegada con el juicio en trámite"| EXT_DIV_310_destino
  DIV_910 -->|"Convenio cumplido"| DIV_990
  DIV_910 -->|"Convenio incumplido: se ejecuta"| DIV_710
  DIV_910 -->|"El convenio atribuye el uso de la vivienda: se controla su vigencia"| EXT_DIV_840_destino
  EXT_DIV_100_destino["DIV_100 Solicitud de trámite de la etapa previa<br/>(ver Cuestiones pendientes: etapa previa ante el Consejero de Familia)"]:::externo
  DIV_910 -->|"Cambio sustancial de la situación: se pide la revisión del convenio (art. 440)"| EXT_DIV_100_destino
  DIV_950 -->|"Se impulsa el proceso: se actualiza el Día Cero al último acto"| DIV_950
  FIN_DIV_950_2(["Fin de este camino"]):::fin
  DIV_950 -->|"Se dicta sentencia o termina el proceso"| FIN_DIV_950_2
  DIV_950 -->|"La contraria pide la caducidad"| DIV_960
  DIV_960 -->|"Actividad útil en término"| DIV_950
  DIV_960 -->|"No hay actividad útil: se decreta la caducidad"| DIV_990
  style DIV_970 stroke-width:3px
  style DIV_980 stroke-width:3px
  style DIV_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
