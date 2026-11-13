# Diagrama de Flujo: Proceso sucesorio (ab intestato y testamentario) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68, arts. 724 a 773) y CCyC Libro Quinto · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_civil_sucesorio_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el heredero o interesado que promueve el sucesorio y al que representamos (ACTORA); naranja = otro interesado con intereses opuestos en una incidencia, como el coheredero que impugna o se opone (DEMANDADA); gris = el juzgado o un organismo: registros, ARBA, escribano, perito o partidor (TRIBUNAL); violeta = cualquiera de los interesados (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la publicación de edictos corre mientras se esperan los informes del Registro de Juicios Universales y del Registro de Testamentos.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>5 hitos"]
  FASE_2["Apertura<br/>6 hitos"]
  FASE_3["Edictos y citación<br/>3 hitos"]
  FASE_4["Testamento<br/>6 hitos"]
  FASE_5["Declaratoria de herederos<br/>6 hitos"]
  FASE_6["Administración<br/>5 hitos"]
  FASE_7["Inventario y avalúo<br/>6 hitos"]
  FASE_8["Partición<br/>7 hitos"]
  FASE_9["Inscripción<br/>4 hitos"]
  FASE_10["Impuestos y tasas<br/>3 hitos"]
  FASE_11["Recursos e incidentes<br/>5 hitos"]
  FASE_12["Cierre<br/>4 hitos"]
  FASE_1 --> FASE_2
  FASE_2 --> FASE_11
  FASE_2 --> FASE_3
  FASE_2 --> FASE_4
  FASE_2 --> FASE_12
  FASE_3 --> FASE_5
  FASE_4 --> FASE_3
  FASE_4 --> FASE_11
  FASE_4 --> FASE_6
  FASE_4 --> FASE_10
  FASE_5 --> FASE_6
  FASE_5 --> FASE_10
  FASE_5 --> FASE_12
  FASE_5 --> FASE_11
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_11
  FASE_8 --> FASE_9
  FASE_8 --> FASE_11
  FASE_9 --> FASE_10
  FASE_9 --> FASE_12
  FASE_11 --> FASE_12
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    SUC_010["INICIO - <b>SUC_010</b> Consulta inicial por el fallecimiento del causante<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_015["<b>SUC_015</b> Control de la caducidad del derecho de aceptar la herencia<br/>Responsable: Heredero que representamos<br/>10 años"]:::actora
    SUC_016["<b>SUC_016</b> Vencimiento máximo del ITGB: 24 meses desde el fallecimiento<br/>Responsable: Heredero que representamos<br/>24 meses"]:::actora
    SUC_020["<b>SUC_020</b> Partidas y determinación del juez competente<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_030["<b>SUC_030</b> Relevamiento de bienes y deudas del causante<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  P_SUC_010_1(["Se abren en paralelo"]):::paralelo
  SUC_010 -->|"Fallecimiento acreditado: se prepara el inicio"| P_SUC_010_1
  P_SUC_010_1 --> SUC_015
  P_SUC_010_1 --> SUC_016
  P_SUC_010_1 --> SUC_020
  P_SUC_010_1 --> SUC_030
  FIN_SUC_015_1(["Fin de este camino"]):::fin
  SUC_015 -->|"Herencia aceptada, o vencido el plazo (se lo tiene por renunciante)"| FIN_SUC_015_1
  FIN_SUC_016_1(["Fin de este camino"]):::fin
  SUC_016 -->|"Declaración jurada presentada, o vencido el plazo (corren recargos)"| FIN_SUC_016_1
  EXT_SUC_100_destino["SUC_100 Promoción del sucesorio<br/>(ver Apertura, edictos y citación)"]:::externo
  SUC_020 -->|"Partidas reunidas y juez competente determinado"| EXT_SUC_100_destino
  FIN_SUC_030_1(["Fin de este camino"]):::fin
  SUC_030 -->|"Relevamiento terminado"| FIN_SUC_030_1
  style SUC_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Apertura, edictos y citación

```mermaid
flowchart TD
  subgraph F_0["Apertura"]
    SUC_100["<b>SUC_100</b> Promoción del sucesorio<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_110["<b>SUC_110</b> Providencia de apertura del sucesorio<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_120["<b>SUC_120</b> Informe del Registro de Testamentos<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_125["<b>SUC_125</b> Inscripción en el Registro de Juicios Universales<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_140["<b>SUC_140</b> Medidas de seguridad y administrador provisional<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_150["<b>SUC_150</b> Intervención del Ministerio Público<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  subgraph F_1["Edictos y citación"]
    SUC_200["<b>SUC_200</b> Publicación de edictos<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_205["<b>SUC_205</b> Plazo de la citación a herederos y acreedores<br/>Responsable: Cualquier interesado<br/>30 días corridos"]:::ambas
    SUC_210["<b>SUC_210</b> Notificación a los herederos denunciados<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  EXT_SUC_020_origen["SUC_020 Partidas y determinación del juez competente<br/>(ver Etapa previa)"]:::externo
  EXT_SUC_020_origen -.->|"Partidas reunidas y juez competente determinado"| SUC_100
  P_SUC_100_1(["Se abren en paralelo"]):::paralelo
  SUC_100 -->|"Sucesorio promovido"| P_SUC_100_1
  P_SUC_100_1 --> SUC_110
  P_SUC_100_1 --> SUC_120
  P_SUC_100_1 --> SUC_125
  EXT_SUC_925_destino["SUC_925 Control de la caducidad de instancia<br/>(ver Recursos, honorarios y cierre)"]:::externo
  P_SUC_100_1 --> EXT_SUC_925_destino
  P_SUC_100_2(["Se abren en paralelo"]):::paralelo
  SUC_100 -->|"Sucesorio promovido con pedido de medidas de seguridad"| P_SUC_100_2
  P_SUC_100_2 --> SUC_110
  P_SUC_100_2 --> SUC_120
  P_SUC_100_2 --> SUC_125
  P_SUC_100_2 --> SUC_140
  P_SUC_100_2 --> EXT_SUC_925_destino
  P_SUC_110_1(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"Apertura ab intestato"| P_SUC_110_1
  P_SUC_110_1 --> SUC_200
  P_SUC_110_1 --> SUC_210
  P_SUC_110_2(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"Apertura ab intestato con herederos menores, con capacidad restringida o ausentes"| P_SUC_110_2
  P_SUC_110_2 --> SUC_150
  P_SUC_110_2 --> SUC_200
  P_SUC_110_2 --> SUC_210
  EXT_SUC_300_destino["SUC_300 Presentación del testamento ológrafo o cerrado<br/>(ver Testamento)"]:::externo
  SUC_110 -->|"Se presenta un testamento ológrafo o cerrado"| EXT_SUC_300_destino
  EXT_SUC_320_destino["SUC_320 Citación de herederos instituidos y legatarios<br/>(ver Testamento)"]:::externo
  SUC_110 -->|"Se presenta un testamento por acto público"| EXT_SUC_320_destino
  EXT_SUC_990_destino["SUC_990 Archivo del expediente<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_110 -->|"El juez se declara incompetente"| EXT_SUC_990_destino
  FIN_SUC_120_1(["Fin de este camino"]):::fin
  SUC_120 -->|"Informe negativo"| FIN_SUC_120_1
  SUC_120 -->|"Informa un testamento por acto público"| EXT_SUC_320_destino
  SUC_120 -->|"Informa un testamento ológrafo o cerrado depositado"| EXT_SUC_300_destino
  FIN_SUC_125_1(["Fin de este camino"]):::fin
  SUC_125 -->|"Inscripción informada (si hay otro sucesorio, se acumula o se remite)"| FIN_SUC_125_1
  FIN_SUC_140_1(["Fin de este camino"]):::fin
  SUC_140 -->|"Medidas ordenadas o denegadas"| FIN_SUC_140_1
  FIN_SUC_150_1(["Fin de este camino"]):::fin
  SUC_150 -->|"Vista contestada"| FIN_SUC_150_1
  SUC_200 -->|"Edictos publicados"| SUC_205
  EXT_SUC_400_destino["SUC_400 Pedido de declaratoria de herederos<br/>(ver Declaratoria de herederos)"]:::externo
  SUC_205 -->|"Vencido el plazo de citación"| EXT_SUC_400_destino
  P_SUC_205_2(["Se abren en paralelo"]):::paralelo
  SUC_205 -->|"Vencido el plazo; un heredero no se pronuncia: se pide la intimación"| P_SUC_205_2
  P_SUC_205_2 --> EXT_SUC_400_destino
  EXT_SUC_430_destino["SUC_430 Intimación judicial a aceptar o renunciar la herencia<br/>(ver Declaratoria de herederos)"]:::externo
  P_SUC_205_2 --> EXT_SUC_430_destino
  EXT_SUC_450_destino["SUC_450 Herencia vacante<br/>(ver Declaratoria de herederos)"]:::externo
  SUC_205 -->|"Vencido el plazo sin herederos que acrediten su derecho"| EXT_SUC_450_destino
  FIN_SUC_210_1(["Fin de este camino"]):::fin
  SUC_210 -->|"Herederos notificados"| FIN_SUC_210_1
  EXT_SUC_310_origen["SUC_310 Oposición a la protocolización<br/>(ver Testamento)"]:::externo
  EXT_SUC_310_origen -.->|"Testamento invalidado: sigue la sucesión ab intestato"| SUC_200
  EXT_SUC_310_origen -.->|"Testamento invalidado: sigue la sucesión ab intestato"| SUC_210
  EXT_SUC_330_origen["SUC_330 Aprobación formal del testamento<br/>(ver Testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Testamento sin institución de herederos o solo con legados: se tramita la declaratoria"| SUC_200
  EXT_SUC_330_origen -.->|"Testamento sin institución de herederos o solo con legados: se tramita la declaratoria"| SUC_210
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Testamento

```mermaid
flowchart TD
  subgraph F_0["Testamento"]
    SUC_300["<b>SUC_300</b> Presentación del testamento ológrafo o cerrado<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_305["<b>SUC_305</b> Audiencia de reconocimiento o pericia caligráfica<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_310["<b>SUC_310</b> Oposición a la protocolización<br/>Responsable: Interesado con interés opuesto<br/>Sin plazo"]:::demandada
    SUC_315["<b>SUC_315</b> Protocolización del testamento<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_320["<b>SUC_320</b> Citación de herederos instituidos y legatarios<br/>Responsable: Cualquier interesado<br/>30 días corridos"]:::ambas
    SUC_330["<b>SUC_330</b> Aprobación formal del testamento<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_SUC_110_origen["SUC_110 Providencia de apertura del sucesorio<br/>(ver Apertura, edictos y citación)"]:::externo
  EXT_SUC_110_origen -.->|"Se presenta un testamento ológrafo o cerrado"| SUC_300
  EXT_SUC_110_origen -.->|"Se presenta un testamento por acto público"| SUC_320
  EXT_SUC_120_origen["SUC_120 Informe del Registro de Testamentos<br/>(ver Apertura, edictos y citación)"]:::externo
  EXT_SUC_120_origen -.->|"Informa un testamento por acto público"| SUC_320
  EXT_SUC_120_origen -.->|"Informa un testamento ológrafo o cerrado depositado"| SUC_300
  SUC_300 -->|"Se fija audiencia o se ordena pericia caligráfica"| SUC_305
  SUC_305 -->|"Letra y firma reconocidas"| SUC_315
  SUC_305 -->|"Un interesado se opone"| SUC_310
  SUC_310 -->|"Oposición rechazada"| SUC_315
  P_SUC_310_2(["Se abren en paralelo"]):::paralelo
  SUC_310 -->|"Testamento invalidado: sigue la sucesión ab intestato"| P_SUC_310_2
  EXT_SUC_200_destino["SUC_200 Publicación de edictos<br/>(ver Apertura, edictos y citación)"]:::externo
  P_SUC_310_2 --> EXT_SUC_200_destino
  EXT_SUC_210_destino["SUC_210 Notificación a los herederos denunciados<br/>(ver Apertura, edictos y citación)"]:::externo
  P_SUC_310_2 --> EXT_SUC_210_destino
  EXT_SUC_900_destino["SUC_900 Apelación de una resolución del sucesorio<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_310 -->|"Se apela la resolución del incidente"| EXT_SUC_900_destino
  SUC_315 -->|"Testamento protocolizado"| SUC_320
  SUC_320 -->|"Vencido el plazo de citación"| SUC_330
  P_SUC_330_1(["Se abren en paralelo"]):::paralelo
  SUC_330 -->|"Testamento aprobado con institución de herederos"| P_SUC_330_1
  EXT_SUC_605_destino["SUC_605 Audiencia de designaciones del art. 732<br/>(ver Administración e inventario)"]:::externo
  P_SUC_330_1 --> EXT_SUC_605_destino
  EXT_SUC_800_destino["SUC_800 Vista al organismo fiscal (ARBA) por el ITGB<br/>(ver Inscripción, impuestos y tasas)"]:::externo
  P_SUC_330_1 --> EXT_SUC_800_destino
  P_SUC_330_2(["Se abren en paralelo"]):::paralelo
  SUC_330 -->|"Testamento sin institución de herederos o solo con legados: se tramita la declaratoria"| P_SUC_330_2
  P_SUC_330_2 --> EXT_SUC_200_destino
  P_SUC_330_2 --> EXT_SUC_210_destino
  SUC_330 -->|"Aprobación denegada o con agravio para el cliente: se apela"| EXT_SUC_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Declaratoria de herederos

```mermaid
flowchart TD
  subgraph F_0["Declaratoria de herederos"]
    SUC_400["<b>SUC_400</b> Pedido de declaratoria de herederos<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_405["<b>SUC_405</b> Declaratoria de herederos<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_410["<b>SUC_410</b> Ampliación de la declaratoria<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_415["<b>SUC_415</b> Impugnación de la declaratoria o petición de herencia<br/>Responsable: Interesado con interés opuesto<br/>Sin plazo"]:::demandada
    SUC_430["<b>SUC_430</b> Intimación judicial a aceptar o renunciar la herencia<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_450["<b>SUC_450</b> Herencia vacante<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_SUC_205_origen["SUC_205 Plazo de la citación a herederos y acreedores<br/>(ver Apertura, edictos y citación)"]:::externo
  EXT_SUC_205_origen -.->|"Vencido el plazo de citación"| SUC_400
  EXT_SUC_205_origen -.->|"Vencido el plazo; un heredero no se pronuncia: se pide la intimación"| SUC_400
  EXT_SUC_205_origen -.->|"Vencido el plazo; un heredero no se pronuncia: se pide la intimación"| SUC_430
  EXT_SUC_205_origen -.->|"Vencido el plazo sin herederos que acrediten su derecho"| SUC_450
  SUC_400 -->|"Pedido presentado"| SUC_405
  P_SUC_405_1(["Se abren en paralelo"]):::paralelo
  SUC_405 -->|"Declaratoria dictada"| P_SUC_405_1
  EXT_SUC_605_destino["SUC_605 Audiencia de designaciones del art. 732<br/>(ver Administración e inventario)"]:::externo
  P_SUC_405_1 --> EXT_SUC_605_destino
  EXT_SUC_800_destino["SUC_800 Vista al organismo fiscal (ARBA) por el ITGB<br/>(ver Inscripción, impuestos y tasas)"]:::externo
  P_SUC_405_1 --> EXT_SUC_800_destino
  P_SUC_405_2(["Se abren en paralelo"]):::paralelo
  SUC_405 -->|"Declaratoria dictada y se presenta un heredero omitido"| P_SUC_405_2
  P_SUC_405_2 --> SUC_410
  P_SUC_405_2 --> EXT_SUC_605_destino
  P_SUC_405_2 --> EXT_SUC_800_destino
  P_SUC_405_3(["Se abren en paralelo"]):::paralelo
  SUC_405 -->|"Declaratoria dictada y un pretendiente la impugna"| P_SUC_405_3
  P_SUC_405_3 --> SUC_415
  P_SUC_405_3 --> EXT_SUC_605_destino
  P_SUC_405_3 --> EXT_SUC_800_destino
  P_SUC_405_4(["Se abren en paralelo"]):::paralelo
  SUC_405 -->|"Declaratoria dictada; herederos capaces y conformes piden seguir fuera del juzgado (art. 733)"| P_SUC_405_4
  P_SUC_405_4 --> EXT_SUC_800_destino
  EXT_SUC_980_destino["SUC_980 Conclusión del trámite judicial o continuación extrajudicial<br/>(ver Recursos, honorarios y cierre)"]:::externo
  P_SUC_405_4 --> EXT_SUC_980_destino
  SUC_405 -->|"Se difiere para acreditar vínculos"| SUC_400
  EXT_SUC_900_destino["SUC_900 Apelación de una resolución del sucesorio<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_405 -->|"Declaratoria con agravio para el cliente: se apela"| EXT_SUC_900_destino
  FIN_SUC_410_1(["Fin de este camino"]):::fin
  SUC_410 -->|"Declaratoria ampliada"| FIN_SUC_410_1
  SUC_410 -->|"Ampliación denegada: se apela"| EXT_SUC_900_destino
  FIN_SUC_415_1(["Fin de este camino"]):::fin
  SUC_415 -->|"Impugnación tramitada en juicio aparte"| FIN_SUC_415_1
  FIN_SUC_430_1(["Fin de este camino"]):::fin
  SUC_430 -->|"El heredero acepta, renuncia o guarda silencio (aceptación)"| FIN_SUC_430_1
  EXT_SUC_990_destino["SUC_990 Archivo del expediente<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_450 -->|"Herencia reputada vacante: curador definitivo"| EXT_SUC_990_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Administración e inventario

```mermaid
flowchart TD
  subgraph F_0["Administración"]
    SUC_500["<b>SUC_500</b> Designación y aceptación del administrador<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_505["<b>SUC_505</b> Rendición de cuentas trimestral del administrador<br/>Responsable: Cualquier interesado<br/>3 meses"]:::ambas
    SUC_510["<b>SUC_510</b> Observaciones a la rendición de cuentas<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_515["<b>SUC_515</b> Autorización judicial para vender o disponer bienes<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_605["<b>SUC_605</b> Audiencia de designaciones del art. 732<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  subgraph F_1["Inventario y avalúo"]
    SUC_600["<b>SUC_600</b> Inventario o denuncia de bienes<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_602["<b>SUC_602</b> Plazo para inventariar después de la intimación<br/>Responsable: Heredero que representamos<br/>3 meses"]:::actora
    SUC_610["<b>SUC_610</b> Diligencia de inventario<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_615["<b>SUC_615</b> Avalúo de los bienes<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_620["<b>SUC_620</b> Traslado del inventario y avalúo<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_625["<b>SUC_625</b> Reclamaciones contra el inventario o el avalúo<br/>Responsable: Interesado con interés opuesto<br/>Sin plazo"]:::demandada
  end
  EXT_SUC_330_origen["SUC_330 Aprobación formal del testamento<br/>(ver Testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Testamento aprobado con institución de herederos"| SUC_605
  EXT_SUC_405_origen["SUC_405 Declaratoria de herederos<br/>(ver Declaratoria de herederos)"]:::externo
  EXT_SUC_405_origen -.->|"Declaratoria dictada"| SUC_605
  EXT_SUC_405_origen -.->|"Declaratoria dictada y se presenta un heredero omitido"| SUC_605
  EXT_SUC_405_origen -.->|"Declaratoria dictada y un pretendiente la impugna"| SUC_605
  SUC_500 -->|"Cargo aceptado"| SUC_505
  P_SUC_500_2(["Se abren en paralelo"]):::paralelo
  SUC_500 -->|"Cargo aceptado y hay que vender o disponer bienes"| P_SUC_500_2
  P_SUC_500_2 --> SUC_505
  P_SUC_500_2 --> SUC_515
  SUC_505 -->|"Rendición presentada"| SUC_510
  SUC_510 -->|"Rendición aprobada; sigue la administración"| SUC_505
  FIN_SUC_510_2(["Fin de este camino"]):::fin
  SUC_510 -->|"Rendición final aprobada, u observada y resuelta por incidente"| FIN_SUC_510_2
  FIN_SUC_515_1(["Fin de este camino"]):::fin
  SUC_515 -->|"Autorización resuelta"| FIN_SUC_515_1
  SUC_600 -->|"Denuncia de bienes sin inventario judicial"| SUC_615
  SUC_600 -->|"Inventario judicial"| SUC_610
  P_SUC_600_3(["Se abren en paralelo"]):::paralelo
  SUC_600 -->|"Un acreedor o legatario intima a inventariar"| P_SUC_600_3
  P_SUC_600_3 --> SUC_602
  P_SUC_600_3 --> SUC_610
  FIN_SUC_602_1(["Fin de este camino"]):::fin
  SUC_602 -->|"Inventario hecho, o vencido el plazo (el heredero responde con sus bienes)"| FIN_SUC_602_1
  P_SUC_605_1(["Se abren en paralelo"]):::paralelo
  SUC_605 -->|"Se designan administrador, inventariador y tasador"| P_SUC_605_1
  P_SUC_605_1 --> SUC_500
  P_SUC_605_1 --> SUC_600
  SUC_605 -->|"Sin administrador: se designan inventariador y tasador o se denuncian bienes"| SUC_600
  SUC_610 -->|"Inventario realizado"| SUC_615
  SUC_615 -->|"Avalúo presentado"| SUC_620
  EXT_SUC_700_destino["SUC_700 Partición privada<br/>(ver Partición)"]:::externo
  SUC_620 -->|"Aprobados; herederos capaces y de acuerdo: partición privada"| EXT_SUC_700_destino
  EXT_SUC_705_destino["SUC_705 Partición judicial: designación del partidor<br/>(ver Partición)"]:::externo
  SUC_620 -->|"Aprobados; incapaces, ausentes o desacuerdo: partición judicial"| EXT_SUC_705_destino
  EXT_SUC_730_destino["SUC_730 Colación y reducción de donaciones<br/>(ver Partición)"]:::externo
  SUC_620 -->|"Aprobados; hay donaciones que colacionar o reducir"| EXT_SUC_730_destino
  SUC_620 -->|"Se presentan reclamaciones"| SUC_625
  SUC_625 -->|"Resueltas; partición privada"| EXT_SUC_700_destino
  SUC_625 -->|"Resueltas; partición judicial"| EXT_SUC_705_destino
  EXT_SUC_900_destino["SUC_900 Apelación de una resolución del sucesorio<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_625 -->|"Se apela la resolución"| EXT_SUC_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Partición

```mermaid
flowchart TD
  subgraph F_0["Partición"]
    SUC_700["<b>SUC_700</b> Partición privada<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_705["<b>SUC_705</b> Partición judicial: designación del partidor<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_710["<b>SUC_710</b> Presentación de la cuenta particionaria<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_715["<b>SUC_715</b> Traslado de la cuenta particionaria<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales + gracia"]:::ambas
    SUC_720["<b>SUC_720</b> Audiencia por oposición a la cuenta particionaria<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_725["<b>SUC_725</b> Aprobación de la partición<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_730["<b>SUC_730</b> Colación y reducción de donaciones<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
  end
  EXT_SUC_620_origen["SUC_620 Traslado del inventario y avalúo<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_620_origen -.->|"Aprobados; herederos capaces y de acuerdo: partición privada"| SUC_700
  EXT_SUC_620_origen -.->|"Aprobados; incapaces, ausentes o desacuerdo: partición judicial"| SUC_705
  EXT_SUC_620_origen -.->|"Aprobados; hay donaciones que colacionar o reducir"| SUC_730
  EXT_SUC_625_origen["SUC_625 Reclamaciones contra el inventario o el avalúo<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_625_origen -.->|"Resueltas; partición privada"| SUC_700
  EXT_SUC_625_origen -.->|"Resueltas; partición judicial"| SUC_705
  EXT_SUC_850_destino["SUC_850 Pedido de inscripción y libramiento de testimonios y oficios<br/>(ver Inscripción, impuestos y tasas)"]:::externo
  SUC_700 -->|"Partición aprobada"| EXT_SUC_850_destino
  SUC_700 -->|"No hay acuerdo: partición judicial"| SUC_705
  SUC_705 -->|"Partidor designado y cargo aceptado"| SUC_710
  SUC_710 -->|"Cuenta particionaria presentada"| SUC_715
  SUC_710 -->|"El partidor no la presenta: remoción y nuevo partidor"| SUC_705
  SUC_715 -->|"Sin oposición"| SUC_725
  SUC_715 -->|"Oposición presentada"| SUC_720
  SUC_720 -->|"Acuerdo en la audiencia o resolución del juez"| SUC_725
  SUC_725 -->|"Partición aprobada"| EXT_SUC_850_destino
  EXT_SUC_900_destino["SUC_900 Apelación de una resolución del sucesorio<br/>(ver Recursos, honorarios y cierre)"]:::externo
  SUC_725 -->|"Se apela la aprobación o el rechazo"| EXT_SUC_900_destino
  SUC_730 -->|"Resuelta; partición privada"| SUC_700
  SUC_730 -->|"Resuelta; partición judicial"| SUC_705
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Inscripción, impuestos y tasas

```mermaid
flowchart TD
  subgraph F_0["Inscripción"]
    SUC_850["<b>SUC_850</b> Pedido de inscripción y libramiento de testimonios y oficios<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_855["<b>SUC_855</b> Inscripción en el Registro de la Propiedad Inmueble<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_860["<b>SUC_860</b> Transferencia de automotores<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_865["<b>SUC_865</b> Transferencia de fondos, acciones y otros bienes<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  subgraph F_1["Impuestos y tasas"]
    SUC_800["<b>SUC_800</b> Vista al organismo fiscal (ARBA) por el ITGB<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_810["<b>SUC_810</b> Declaración jurada y pago del ITGB<br/>Responsable: Heredero que representamos<br/>15 días corridos"]:::actora
    SUC_820["<b>SUC_820</b> Tasa de justicia y contribución al pedir la inscripción<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  EXT_SUC_330_origen["SUC_330 Aprobación formal del testamento<br/>(ver Testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Testamento aprobado con institución de herederos"| SUC_800
  EXT_SUC_405_origen["SUC_405 Declaratoria de herederos<br/>(ver Declaratoria de herederos)"]:::externo
  EXT_SUC_405_origen -.->|"Declaratoria dictada"| SUC_800
  EXT_SUC_405_origen -.->|"Declaratoria dictada y se presenta un heredero omitido"| SUC_800
  EXT_SUC_405_origen -.->|"Declaratoria dictada y un pretendiente la impugna"| SUC_800
  EXT_SUC_405_origen -.->|"Declaratoria dictada; herederos capaces y conformes piden seguir fuera del juzgado (art. 733)"| SUC_800
  EXT_SUC_700_origen["SUC_700 Partición privada<br/>(ver Partición)"]:::externo
  EXT_SUC_700_origen -.->|"Partición aprobada"| SUC_850
  EXT_SUC_725_origen["SUC_725 Aprobación de la partición<br/>(ver Partición)"]:::externo
  EXT_SUC_725_origen -.->|"Partición aprobada"| SUC_850
  FIN_SUC_800_1(["Fin de este camino"]):::fin
  SUC_800 -->|"Vista contestada o liquidación del ITGB presentada"| FIN_SUC_800_1
  FIN_SUC_810_1(["Fin de este camino"]):::fin
  SUC_810 -->|"Declaración jurada presentada y pagada o exenta"| FIN_SUC_810_1
  FIN_SUC_820_1(["Fin de este camino"]):::fin
  SUC_820 -->|"Tasa y contribución pagadas"| FIN_SUC_820_1
  P_SUC_850_1(["Se abren en paralelo"]):::paralelo
  SUC_850 -->|"Inscripción pedida: testimonios y oficios librados"| P_SUC_850_1
  P_SUC_850_1 --> SUC_810
  P_SUC_850_1 --> SUC_820
  P_SUC_850_1 --> SUC_855
  P_SUC_850_1 --> SUC_860
  P_SUC_850_1 --> SUC_865
  P_SUC_850_2(["Se abren en paralelo"]):::paralelo
  SUC_850 -->|"Los herederos venden por tracto abreviado sin inscribir"| P_SUC_850_2
  P_SUC_850_2 --> SUC_810
  EXT_SUC_980_destino["SUC_980 Conclusión del trámite judicial o continuación extrajudicial<br/>(ver Recursos, honorarios y cierre)"]:::externo
  P_SUC_850_2 --> EXT_SUC_980_destino
  SUC_855 -->|"Inscripción registrada o no hay inmuebles"| EXT_SUC_980_destino
  FIN_SUC_860_1(["Fin de este camino"]):::fin
  SUC_860 -->|"Automotores transferidos o no hay"| FIN_SUC_860_1
  FIN_SUC_865_1(["Fin de este camino"]):::fin
  SUC_865 -->|"Fondos y otros bienes transferidos o no hay"| FIN_SUC_865_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Recursos, honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Recursos e incidentes"]
    SUC_900["<b>SUC_900</b> Apelación de una resolución del sucesorio<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_905["<b>SUC_905</b> Memorial del recurso concedido en relación<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_910["<b>SUC_910</b> Resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_925["<b>SUC_925</b> Control de la caducidad de instancia<br/>Responsable: Heredero que representamos<br/>6 meses"]:::actora
    SUC_930["<b>SUC_930</b> Intimación a activar el proceso<br/>Responsable: Heredero que representamos<br/>5 días hábiles judiciales + gracia"]:::actora
  end
  subgraph F_1["Cierre"]
    SUC_915["<b>SUC_915</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_920["<b>SUC_920</b> Pago de los honorarios firmes<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales"]:::ambas
    SUC_980["<b>SUC_980</b> Conclusión del trámite judicial o continuación extrajudicial<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_990["<b>SUC_990</b> Archivo del expediente<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
  end
  EXT_SUC_100_origen["SUC_100 Promoción del sucesorio<br/>(ver Apertura, edictos y citación)"]:::externo
  EXT_SUC_100_origen -.->|"Sucesorio promovido"| SUC_925
  EXT_SUC_100_origen -.->|"Sucesorio promovido con pedido de medidas de seguridad"| SUC_925
  EXT_SUC_110_origen["SUC_110 Providencia de apertura del sucesorio<br/>(ver Apertura, edictos y citación)"]:::externo
  EXT_SUC_110_origen -.->|"El juez se declara incompetente"| SUC_990
  EXT_SUC_310_origen["SUC_310 Oposición a la protocolización<br/>(ver Testamento)"]:::externo
  EXT_SUC_310_origen -.->|"Se apela la resolución del incidente"| SUC_900
  EXT_SUC_330_origen["SUC_330 Aprobación formal del testamento<br/>(ver Testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Aprobación denegada o con agravio para el cliente: se apela"| SUC_900
  EXT_SUC_405_origen["SUC_405 Declaratoria de herederos<br/>(ver Declaratoria de herederos)"]:::externo
  EXT_SUC_405_origen -.->|"Declaratoria dictada; herederos capaces y conformes piden seguir fuera del juzgado (art. 733)"| SUC_980
  EXT_SUC_405_origen -.->|"Declaratoria con agravio para el cliente: se apela"| SUC_900
  EXT_SUC_410_origen["SUC_410 Ampliación de la declaratoria<br/>(ver Declaratoria de herederos)"]:::externo
  EXT_SUC_410_origen -.->|"Ampliación denegada: se apela"| SUC_900
  EXT_SUC_450_origen["SUC_450 Herencia vacante<br/>(ver Declaratoria de herederos)"]:::externo
  EXT_SUC_450_origen -.->|"Herencia reputada vacante: curador definitivo"| SUC_990
  EXT_SUC_625_origen["SUC_625 Reclamaciones contra el inventario o el avalúo<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_625_origen -.->|"Se apela la resolución"| SUC_900
  EXT_SUC_725_origen["SUC_725 Aprobación de la partición<br/>(ver Partición)"]:::externo
  EXT_SUC_725_origen -.->|"Se apela la aprobación o el rechazo"| SUC_900
  EXT_SUC_850_origen["SUC_850 Pedido de inscripción y libramiento de testimonios y oficios<br/>(ver Inscripción, impuestos y tasas)"]:::externo
  EXT_SUC_850_origen -.->|"Los herederos venden por tracto abreviado sin inscribir"| SUC_980
  EXT_SUC_855_origen["SUC_855 Inscripción en el Registro de la Propiedad Inmueble<br/>(ver Inscripción, impuestos y tasas)"]:::externo
  EXT_SUC_855_origen -.->|"Inscripción registrada o no hay inmuebles"| SUC_980
  SUC_900 -->|"Recurso concedido en relación"| SUC_905
  FIN_SUC_900_2(["Fin de este camino"]):::fin
  SUC_900 -->|"Recurso denegado o no interpuesto"| FIN_SUC_900_2
  SUC_905 -->|"Memorial presentado o plazo vencido"| SUC_910
  FIN_SUC_910_1(["Fin de este camino"]):::fin
  SUC_910 -->|"La Cámara resuelve: sigue el trámite"| FIN_SUC_910_1
  SUC_915 -->|"Regulación firme"| SUC_920
  SUC_920 -->|"Honorarios pagados"| SUC_990
  FIN_SUC_925_1(["Fin de este camino"]):::fin
  SUC_925 -->|"Trámite concluido antes del vencimiento"| FIN_SUC_925_1
  SUC_925 -->|"Plazo vencido: se intima a activar el proceso"| SUC_930
  FIN_SUC_930_1(["Fin de este camino"]):::fin
  SUC_930 -->|"Proceso activado en término"| FIN_SUC_930_1
  SUC_930 -->|"No se activa: se decreta la caducidad"| SUC_990
  SUC_980 -->|"Trámite concluido: se regulan honorarios"| SUC_915
  SUC_980 -->|"Trámite concluido sin regulación pendiente"| SUC_990
  style SUC_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
