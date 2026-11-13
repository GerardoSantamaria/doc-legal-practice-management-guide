# Diagrama de Flujo: Adopción (PBA)

**Régimen:** Ley 14.528 de procedimiento de adopción (texto Ley 15.610); Ley 13.298, art. 35 bis (texto Ley 14.537); CCyC, arts. 594 a 637; CPCCBA en forma supletoria (art. 30 Ley 14.528) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_familia_adopcion_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = aspirantes, guardadores o pretensos adoptantes (ACTORA); naranja = progenitores y familia de origen (DEMANDADA); gris = juzgado, Servicio Local o Zonal, Registro Central de Aspirantes, equipo técnico o Ministerio Público, aclarado en el nombre (TRIBUNAL); violeta = cualquiera de las partes, incluido el niño con su abogado (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, al dictarse el dictamen del Servicio corren a la vez la audiencia con la familia de origen y los 90 días que tiene el juez para resolver la situación de adoptabilidad.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un registro). La app los separa en el flujo prejudicial.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Medidas de protección<br/>4 hitos"]
  FASE_3["Situación de adoptabilidad<br/>10 hitos"]
  FASE_4["Guarda con fines de adopción<br/>8 hitos"]
  FASE_5["Juicio de adopción<br/>7 hitos"]
  FASE_6["Acciones posteriores<br/>2 hitos"]
  FASE_7["Cierre<br/>2 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_3
  FASE_1 --> FASE_5
  FASE_1 --> FASE_6
  FASE_1 --> FASE_7
  FASE_1 --> FASE_4
  FASE_2 --> FASE_7
  FASE_2 --> FASE_3
  FASE_3 --> FASE_7
  FASE_3 --> FASE_4
  FASE_4 --> FASE_5
  FASE_5 --> FASE_4
  FASE_5 --> FASE_7
  FASE_6 --> FASE_7
```

## 1. Etapa previa (antes de promover)

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    ADO_010["INICIO - <b>ADO_010</b> Consulta sobre una adopción<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ADO_020["<b>ADO_020</b> Inscripción en el Registro Central de Aspirantes a Guardas con Fines de Adopción<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_030["<b>ADO_030</b> Impugnación de la no admisión en el Registro<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_040["<b>ADO_040</b> Espera de la convocatoria<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_050["<b>ADO_050</b> Entrega directa o guarda de hecho<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  ADO_010 -->|"Se quieren inscribir como aspirantes a guarda con fines de adopción"| ADO_020
  EXT_ADO_100_destino["ADO_100 Comunicación de la medida de abrigo al juez<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  ADO_010 -->|"Hay una medida de abrigo del Servicio Local o Zonal"| EXT_ADO_100_destino
  EXT_ADO_130_destino["ADO_130 Búsqueda de la familia de origen<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  ADO_010 -->|"Niño sin filiación establecida o con progenitores fallecidos"| EXT_ADO_130_destino
  EXT_ADO_200_destino["ADO_200 Manifestación de los progenitores de autorizar la adopción<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  ADO_010 -->|"Los progenitores quieren autorizar la adopción"| EXT_ADO_200_destino
  EXT_ADO_400_destino["ADO_400 Demanda de adopción<br/>(ver Juicio de adopción)"]:::externo
  ADO_010 -->|"Adopción de integración (hijo del cónyuge o conviviente)"| EXT_ADO_400_destino
  ADO_010 -->|"Hay una entrega directa o una guarda de hecho"| ADO_050
  EXT_ADO_500_destino["ADO_500 Conversión, revocación o nulidad de la adopción<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_010 -->|"Conversión, revocación o nulidad de una adopción"| EXT_ADO_500_destino
  EXT_ADO_510_destino["ADO_510 Acceso a los orígenes<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_010 -->|"La persona adoptada quiere conocer sus orígenes"| EXT_ADO_510_destino
  ADO_020 -->|"Inscripción admitida"| ADO_040
  ADO_020 -->|"Inscripción no admitida"| ADO_030
  ADO_030 -->|"Se admite la inscripción"| ADO_040
  EXT_ADO_990_destino["ADO_990 Archivo del expediente<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_030 -->|"Se confirma la no admisión"| EXT_ADO_990_destino
  EXT_ADO_300_destino["ADO_300 Selección de los postulantes<br/>(ver Guarda con fines de adopción)"]:::externo
  ADO_040 -->|"El juzgado convoca a los aspirantes"| EXT_ADO_300_destino
  ADO_040 -->|"Baja o renuncia a la inscripción"| EXT_ADO_990_destino
  EXT_ADO_970_destino["ADO_970 Otra figura jurídica: termina el procedimiento de adopción<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_050 -->|"Se prueba el vínculo con el guardador: el juez evalúa otra figura"| EXT_ADO_970_destino
  ADO_050 -->|"El juez separa al niño: se dispone una medida de protección"| EXT_ADO_100_destino
  style ADO_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Medida de abrigo y búsqueda de la familia de origen

```mermaid
flowchart TD
  subgraph F_0["Medidas de protección"]
    ADO_100["<b>ADO_100</b> Comunicación de la medida de abrigo al juez<br/>Responsable: Juzgado u organismo<br/>24 horas"]:::tribunal
    ADO_110["<b>ADO_110</b> Control de legalidad de la medida de abrigo<br/>Responsable: Juzgado u organismo<br/>72 horas"]:::tribunal
    ADO_120["<b>ADO_120</b> Plazo máximo de la medida de abrigo<br/>Responsable: Juzgado u organismo<br/>180 días corridos"]:::tribunal
    ADO_130["<b>ADO_130</b> Búsqueda de la familia de origen<br/>Responsable: Juzgado u organismo<br/>30 días corridos"]:::tribunal
  end
  EXT_ADO_010_origen["ADO_010 Consulta sobre una adopción<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_010_origen -.->|"Hay una medida de abrigo del Servicio Local o Zonal"| ADO_100
  EXT_ADO_010_origen -.->|"Niño sin filiación establecida o con progenitores fallecidos"| ADO_130
  EXT_ADO_050_origen["ADO_050 Entrega directa o guarda de hecho<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_050_origen -.->|"El juez separa al niño: se dispone una medida de protección"| ADO_100
  ADO_100 -->|"Medida comunicada al juez y al Asesor de Incapaces"| ADO_110
  ADO_110 -->|"Medida declarada legal"| ADO_120
  EXT_ADO_990_destino["ADO_990 Archivo del expediente<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_110 -->|"Medida no legal: el niño vuelve con su familia"| EXT_ADO_990_destino
  ADO_120 -->|"Se revierten las causas: el niño vuelve con su familia"| EXT_ADO_990_destino
  EXT_ADO_220_destino["ADO_220 Dictamen del Servicio sobre la situación de adoptabilidad<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  ADO_120 -->|"Vence el plazo sin revertir las causas"| EXT_ADO_220_destino
  EXT_ADO_270_destino["ADO_270 Resolución sobre la situación de adoptabilidad<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  ADO_120 -->|"Fracasan las medidas antes del vencimiento: el juez decreta la adoptabilidad (art. 14)"| EXT_ADO_270_destino
  EXT_ADO_970_destino["ADO_970 Otra figura jurídica: termina el procedimiento de adopción<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_120 -->|"Un familiar o referente afectivo asume la guarda o tutela"| EXT_ADO_970_destino
  ADO_130 -->|"Se identifica a los progenitores o a la familia: medidas de revinculación"| ADO_120
  ADO_130 -->|"Un familiar o referente afectivo asume la guarda o tutela"| EXT_ADO_970_destino
  ADO_130 -->|"Búsqueda agotada sin resultado: el Servicio informa"| EXT_ADO_220_destino
  ADO_130 -->|"Prórroga por igual plazo por razón fundada"| ADO_130
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Declaración de la situación de adoptabilidad

```mermaid
flowchart TD
  subgraph F_0["Situación de adoptabilidad"]
    ADO_200["<b>ADO_200</b> Manifestación de los progenitores de autorizar la adopción<br/>Responsable: Familia de origen<br/>Sin plazo"]:::demandada
    ADO_210["<b>ADO_210</b> Audiencia con los progenitores que autorizan la adopción<br/>Responsable: Familia de origen<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    ADO_220["<b>ADO_220</b> Dictamen del Servicio sobre la situación de adoptabilidad<br/>Responsable: Juzgado u organismo<br/>24 horas"]:::tribunal
    ADO_230["<b>ADO_230</b> Audiencia con los progenitores y la familia de origen<br/>Responsable: Familia de origen<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    ADO_240["<b>ADO_240</b> Estudios psicológicos, de salud y socioambientales<br/>Responsable: Juzgado u organismo<br/>10 días corridos"]:::tribunal
    ADO_250["<b>ADO_250</b> Contacto personal del juez con el niño<br/>Responsable: Juzgado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    ADO_260["<b>ADO_260</b> Plazo máximo para resolver la situación de adoptabilidad<br/>Responsable: Juzgado u organismo<br/>90 días corridos"]:::tribunal
    ADO_270["<b>ADO_270</b> Resolución sobre la situación de adoptabilidad<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ADO_280["<b>ADO_280</b> Apelación de la resolución de adoptabilidad<br/>Responsable: Cualquiera de las partes<br/>2 días hábiles judiciales + gracia"]:::ambas
    ADO_290["<b>ADO_290</b> Comunicación al Registro Central y remisión de la nómina<br/>Responsable: Juzgado u organismo<br/>24 horas"]:::tribunal
  end
  EXT_ADO_010_origen["ADO_010 Consulta sobre una adopción<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_010_origen -.->|"Los progenitores quieren autorizar la adopción"| ADO_200
  EXT_ADO_120_origen["ADO_120 Plazo máximo de la medida de abrigo<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  EXT_ADO_120_origen -.->|"Vence el plazo sin revertir las causas"| ADO_220
  EXT_ADO_120_origen -.->|"Fracasan las medidas antes del vencimiento: el juez decreta la adoptabilidad (art. 14)"| ADO_270
  EXT_ADO_130_origen["ADO_130 Búsqueda de la familia de origen<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  EXT_ADO_130_origen -.->|"Búsqueda agotada sin resultado: el Servicio informa"| ADO_220
  ADO_200 -->|"Manifestación presentada después de los 45 días del nacimiento"| ADO_210
  P_ADO_210_1(["Se abren en paralelo"]):::paralelo
  ADO_210 -->|"Audiencia celebrada: se ordenan los estudios"| P_ADO_210_1
  P_ADO_210_1 --> ADO_240
  P_ADO_210_1 --> ADO_260
  EXT_ADO_990_destino["ADO_990 Archivo del expediente<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_210 -->|"Los progenitores se retractan o desisten"| EXT_ADO_990_destino
  P_ADO_220_1(["Se abren en paralelo"]):::paralelo
  ADO_220 -->|"Dictamen presentado: se fija la audiencia"| P_ADO_220_1
  P_ADO_220_1 --> ADO_230
  P_ADO_220_1 --> ADO_260
  P_ADO_230_1(["Se abren en paralelo"]):::paralelo
  ADO_230 -->|"Audiencia celebrada: se ordenan los estudios"| P_ADO_230_1
  P_ADO_230_1 --> ADO_240
  P_ADO_230_1 --> ADO_250
  ADO_230 -->|"Incomparecencia injustificada y reiterada de la familia"| ADO_270
  ADO_240 -->|"Informes agregados: vista al Ministerio Público"| ADO_270
  FIN_ADO_250_1(["Fin de este camino"]):::fin
  ADO_250 -->|"Contacto realizado"| FIN_ADO_250_1
  FIN_ADO_260_1(["Fin de este camino"]):::fin
  ADO_260 -->|"El juez resuelve dentro del plazo"| FIN_ADO_260_1
  P_ADO_270_1(["Se abren en paralelo"]):::paralelo
  ADO_270 -->|"Se declara la situación de adoptabilidad"| P_ADO_270_1
  P_ADO_270_1 --> ADO_280
  P_ADO_270_1 --> ADO_290
  ADO_270 -->|"Se dispone otra figura (guarda o tutela de un familiar o referente afectivo)"| ADO_280
  ADO_270 -->|"Se rechaza: el niño vuelve con su familia de origen"| ADO_280
  FIN_ADO_280_1(["Fin de este camino"]):::fin
  ADO_280 -->|"Adoptabilidad firme: no se apela o la Cámara la confirma"| FIN_ADO_280_1
  EXT_ADO_970_destino["ADO_970 Otra figura jurídica: termina el procedimiento de adopción<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_280 -->|"Otra figura firme"| EXT_ADO_970_destino
  ADO_280 -->|"Rechazo firme, o la Cámara revoca la adoptabilidad"| EXT_ADO_990_destino
  EXT_ADO_300_destino["ADO_300 Selección de los postulantes<br/>(ver Guarda con fines de adopción)"]:::externo
  ADO_290 -->|"Nómina de postulantes recibida"| EXT_ADO_300_destino
  ADO_290 -->|"No hay postulantes para el caso: el juez evalúa otra figura"| EXT_ADO_970_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Guarda con fines de adopción

```mermaid
flowchart TD
  subgraph F_0["Guarda con fines de adopción"]
    ADO_300["<b>ADO_300</b> Selección de los postulantes<br/>Responsable: Juzgado u organismo<br/>5 días corridos"]:::tribunal
    ADO_310["<b>ADO_310</b> Audiencia con los postulantes<br/>Responsable: Pretensos adoptantes<br/>Fecha y hora fijadas por el tribunal"]:::actora
    ADO_320["<b>ADO_320</b> Vinculación con el niño<br/>Responsable: Pretensos adoptantes<br/>3 meses"]:::actora
    ADO_330["<b>ADO_330</b> Resolución que otorga la guarda con fines de adopción<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ADO_340["<b>ADO_340</b> Audiencia de otorgamiento de la guarda<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    ADO_350["<b>ADO_350</b> Plazo de la guarda con fines de adopción<br/>Responsable: Pretensos adoptantes<br/>6 meses"]:::actora
    ADO_360["<b>ADO_360</b> Seguimiento de la guarda<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_370["<b>ADO_370</b> Revocación de la guarda<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_ADO_040_origen["ADO_040 Espera de la convocatoria<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_040_origen -.->|"El juzgado convoca a los aspirantes"| ADO_300
  EXT_ADO_290_origen["ADO_290 Comunicación al Registro Central y remisión de la nómina<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  EXT_ADO_290_origen -.->|"Nómina de postulantes recibida"| ADO_300
  ADO_300 -->|"Postulantes seleccionados: se fija la audiencia"| ADO_310
  ADO_310 -->|"Ratifican su voluntad: comienza la vinculación"| ADO_320
  ADO_310 -->|"No concurren o declinan: se seleccionan otros aspirantes"| ADO_300
  ADO_320 -->|"El juez amplía la vinculación por un período igual"| ADO_320
  ADO_320 -->|"Informe final favorable del equipo técnico"| ADO_330
  ADO_320 -->|"La vinculación no prospera: se seleccionan otros aspirantes"| ADO_300
  P_ADO_330_1(["Se abren en paralelo"]):::paralelo
  ADO_330 -->|"Guarda otorgada"| P_ADO_330_1
  P_ADO_330_1 --> ADO_340
  P_ADO_330_1 --> ADO_350
  ADO_330 -->|"Guarda denegada: se seleccionan otros aspirantes"| ADO_300
  ADO_340 -->|"Audiencia de otorgamiento celebrada"| ADO_360
  EXT_ADO_400_destino["ADO_400 Demanda de adopción<br/>(ver Juicio de adopción)"]:::externo
  ADO_350 -->|"Cumplido el período de guarda: se inicia el juicio de adopción"| EXT_ADO_400_destino
  FIN_ADO_360_1(["Fin de este camino"]):::fin
  ADO_360 -->|"Seguimiento favorable hasta el fin de la guarda"| FIN_ADO_360_1
  ADO_360 -->|"Guardadores remisos o no aptos"| ADO_370
  ADO_370 -->|"Guarda revocada: se seleccionan nuevos postulantes"| ADO_300
  ADO_370 -->|"No se revoca: sigue el seguimiento"| ADO_360
  EXT_ADO_420_origen["ADO_420 Audiencia de comparecencia y consentimiento del niño<br/>(ver Juicio de adopción)"]:::externo
  EXT_ADO_420_origen -.->|"El niño no quiere ser adoptado: se seleccionan nuevos postulantes"| ADO_300
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Juicio de adopción

```mermaid
flowchart TD
  subgraph F_0["Juicio de adopción"]
    ADO_400["<b>ADO_400</b> Demanda de adopción<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_410["<b>ADO_410</b> Vista al Ministerio Público y notificación al Servicio<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ADO_420["<b>ADO_420</b> Audiencia de comparecencia y consentimiento del niño<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    ADO_430["<b>ADO_430</b> Sentencia de adopción<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ADO_440["<b>ADO_440</b> Apelación de la sentencia de adopción<br/>Responsable: Cualquiera de las partes<br/>2 días hábiles judiciales + gracia"]:::ambas
    ADO_450["<b>ADO_450</b> Inscripción en el Registro de las Personas y comunicación al Registro Central<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
    ADO_460["<b>ADO_460</b> Regulación y apelación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_ADO_010_origen["ADO_010 Consulta sobre una adopción<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_010_origen -.->|"Adopción de integración (hijo del cónyuge o conviviente)"| ADO_400
  EXT_ADO_350_origen["ADO_350 Plazo de la guarda con fines de adopción<br/>(ver Guarda con fines de adopción)"]:::externo
  EXT_ADO_350_origen -.->|"Cumplido el período de guarda: se inicia el juicio de adopción"| ADO_400
  ADO_400 -->|"Demanda presentada"| ADO_410
  ADO_410 -->|"Vista evacuada: se fija la audiencia"| ADO_420
  ADO_420 -->|"Audiencia celebrada (con el consentimiento del niño, si corresponde)"| ADO_430
  EXT_ADO_300_destino["ADO_300 Selección de los postulantes<br/>(ver Guarda con fines de adopción)"]:::externo
  ADO_420 -->|"El niño no quiere ser adoptado: se seleccionan nuevos postulantes"| EXT_ADO_300_destino
  EXT_ADO_970_destino["ADO_970 Otra figura jurídica: termina el procedimiento de adopción<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_420 -->|"El niño no quiere ser adoptado: el juez evalúa otra figura"| EXT_ADO_970_destino
  P_ADO_430_1(["Se abren en paralelo"]):::paralelo
  ADO_430 -->|"Sentencia notificada"| P_ADO_430_1
  P_ADO_430_1 --> ADO_440
  P_ADO_430_1 --> ADO_450
  P_ADO_430_1 --> ADO_460
  FIN_ADO_440_1(["Fin de este camino"]):::fin
  ADO_440 -->|"No se apela, o la Cámara resuelve el recurso"| FIN_ADO_440_1
  EXT_ADO_990_destino["ADO_990 Archivo del expediente<br/>(ver Acciones posteriores y cierre)"]:::externo
  ADO_450 -->|"Sentencia inscripta"| EXT_ADO_990_destino
  FIN_ADO_460_1(["Fin de este camino"]):::fin
  ADO_460 -->|"Honorarios firmes o apelación resuelta"| FIN_ADO_460_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Acciones posteriores y cierre

```mermaid
flowchart TD
  subgraph F_0["Acciones posteriores"]
    ADO_500["<b>ADO_500</b> Conversión, revocación o nulidad de la adopción<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    ADO_510["<b>ADO_510</b> Acceso a los orígenes<br/>Responsable: Pretensos adoptantes<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Cierre"]
    ADO_970["<b>ADO_970</b> Otra figura jurídica: termina el procedimiento de adopción<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    ADO_990["<b>ADO_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_ADO_010_origen["ADO_010 Consulta sobre una adopción<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_010_origen -.->|"Conversión, revocación o nulidad de una adopción"| ADO_500
  EXT_ADO_010_origen -.->|"La persona adoptada quiere conocer sus orígenes"| ADO_510
  EXT_ADO_030_origen["ADO_030 Impugnación de la no admisión en el Registro<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_030_origen -.->|"Se confirma la no admisión"| ADO_990
  EXT_ADO_040_origen["ADO_040 Espera de la convocatoria<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_040_origen -.->|"Baja o renuncia a la inscripción"| ADO_990
  EXT_ADO_050_origen["ADO_050 Entrega directa o guarda de hecho<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_ADO_050_origen -.->|"Se prueba el vínculo con el guardador: el juez evalúa otra figura"| ADO_970
  EXT_ADO_110_origen["ADO_110 Control de legalidad de la medida de abrigo<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  EXT_ADO_110_origen -.->|"Medida no legal: el niño vuelve con su familia"| ADO_990
  EXT_ADO_120_origen["ADO_120 Plazo máximo de la medida de abrigo<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  EXT_ADO_120_origen -.->|"Se revierten las causas: el niño vuelve con su familia"| ADO_990
  EXT_ADO_120_origen -.->|"Un familiar o referente afectivo asume la guarda o tutela"| ADO_970
  EXT_ADO_130_origen["ADO_130 Búsqueda de la familia de origen<br/>(ver Medida de abrigo y búsqueda de la familia de origen)"]:::externo
  EXT_ADO_130_origen -.->|"Un familiar o referente afectivo asume la guarda o tutela"| ADO_970
  EXT_ADO_210_origen["ADO_210 Audiencia con los progenitores que autorizan la adopción<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  EXT_ADO_210_origen -.->|"Los progenitores se retractan o desisten"| ADO_990
  EXT_ADO_280_origen["ADO_280 Apelación de la resolución de adoptabilidad<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  EXT_ADO_280_origen -.->|"Otra figura firme"| ADO_970
  EXT_ADO_280_origen -.->|"Rechazo firme, o la Cámara revoca la adoptabilidad"| ADO_990
  EXT_ADO_290_origen["ADO_290 Comunicación al Registro Central y remisión de la nómina<br/>(ver Declaración de la situación de adoptabilidad)"]:::externo
  EXT_ADO_290_origen -.->|"No hay postulantes para el caso: el juez evalúa otra figura"| ADO_970
  EXT_ADO_420_origen["ADO_420 Audiencia de comparecencia y consentimiento del niño<br/>(ver Juicio de adopción)"]:::externo
  EXT_ADO_420_origen -.->|"El niño no quiere ser adoptado: el juez evalúa otra figura"| ADO_970
  EXT_ADO_450_origen["ADO_450 Inscripción en el Registro de las Personas y comunicación al Registro Central<br/>(ver Juicio de adopción)"]:::externo
  EXT_ADO_450_origen -.->|"Sentencia inscripta"| ADO_990
  ADO_500 -->|"Sentencia firme sobre la conversión, la revocación o la nulidad"| ADO_990
  ADO_510 -->|"Acceso otorgado o acción resuelta"| ADO_990
  style ADO_970 stroke-width:3px
  style ADO_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
