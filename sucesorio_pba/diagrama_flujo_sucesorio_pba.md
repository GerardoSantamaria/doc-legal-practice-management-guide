# Diagrama de Flujo: Proceso sucesorio (ab intestato y testamentario) - Provincia de Buenos Aires

**Régimen:** CPCCBA (Decreto-Ley 7425/68, arts. 724 a 773) y CCyC Libro Quinto · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_flujo_sucesorio_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el heredero o interesado que promueve y al que representamos (ACTORA); naranja = otros interesados con intereses opuestos en una incidencia: coherederos que impugnan, acreedores, el cónyuge en la liquidación de los gananciales (DEMANDADA); gris = el juzgado o la espera de un organismo, como un registro o ARBA (TRIBUNAL); violeta = cualquiera de los interesados (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la publicación de edictos corre mientras se esperan los informes del Registro de Juicios Universales y del Registro de Testamentos.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>7 hitos"]
  FASE_2["Apertura<br/>9 hitos"]
  FASE_3["Edictos y citación<br/>3 hitos"]
  FASE_4["Declaratoria o aprobación del testamento<br/>6 hitos"]
  FASE_5["Administración<br/>4 hitos"]
  FASE_6["Inventario y avalúo<br/>6 hitos"]
  FASE_7["Partición<br/>5 hitos"]
  FASE_8["Inscripción<br/>7 hitos"]
  FASE_9["Impuestos y tasas<br/>5 hitos"]
  FASE_10["Cierre<br/>2 hitos"]
  FASE_11["Recursos e incidentes<br/>7 hitos"]
  FASE_1 --> FASE_9
  FASE_1 --> FASE_2
  FASE_2 --> FASE_3
  FASE_2 --> FASE_11
  FASE_3 --> FASE_4
  FASE_4 --> FASE_11
  FASE_4 --> FASE_6
  FASE_4 --> FASE_5
  FASE_4 --> FASE_7
  FASE_4 --> FASE_10
  FASE_5 --> FASE_6
  FASE_5 --> FASE_11
  FASE_6 --> FASE_11
  FASE_6 --> FASE_8
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_11
  FASE_7 --> FASE_5
  FASE_8 --> FASE_9
  FASE_8 --> FASE_10
  FASE_11 --> FASE_2
  FASE_11 --> FASE_4
  FASE_11 --> FASE_3
```

## 1. Etapa previa

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    SUC_010["INICIO - <b>SUC_010</b> Consulta inicial por el fallecimiento del causante<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_015["<b>SUC_015</b> Control de la caducidad del derecho de aceptar la herencia<br/>Responsable: Heredero que representamos<br/>10 años"]:::actora
    SUC_016["<b>SUC_016</b> Vencimiento máximo del ITGB: 24 meses desde el fallecimiento<br/>Responsable: Heredero que representamos<br/>24 meses"]:::actora
    SUC_020["<b>SUC_020</b> Reunión de las partidas que acreditan el fallecimiento y el vínculo<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_030["<b>SUC_030</b> Último domicilio del causante y juzgado competente<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_040["<b>SUC_040</b> Búsqueda de testamento<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_050["<b>SUC_050</b> Relevamiento del acervo: bienes y deudas<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  P_SUC_010_1(["Se abren en paralelo"]):::paralelo
  SUC_010 -->|"Consulta tomada: se prepara la sucesión"| P_SUC_010_1
  P_SUC_010_1 --> SUC_015
  P_SUC_010_1 --> SUC_016
  P_SUC_010_1 --> SUC_020
  P_SUC_010_1 --> SUC_040
  P_SUC_010_1 --> SUC_050
  FIN_SUC_015_1(["Fin de este camino"]):::fin
  SUC_015 -->|"Herencia aceptada, o plazo vencido: quien no aceptó es tenido por renunciante"| FIN_SUC_015_1
  FIN_SUC_016_1(["Fin de este camino"]):::fin
  SUC_016 -->|"ITGB declarado y pagado antes de los 24 meses"| FIN_SUC_016_1
  EXT_SUC_910_destino["SUC_910 Declaración jurada y pago del ITGB ante ARBA<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  SUC_016 -->|"Se cumplen 24 meses sin haber pedido la inscripción"| EXT_SUC_910_destino
  SUC_020 -->|"Partidas reunidas"| SUC_030
  EXT_SUC_100_destino["SUC_100 Escrito de inicio del sucesorio<br/>(ver Apertura)"]:::externo
  SUC_030 -->|"Juzgado competente definido"| EXT_SUC_100_destino
  FIN_SUC_040_1(["Fin de este camino"]):::fin
  SUC_040 -->|"Búsqueda terminada, con o sin testamento"| FIN_SUC_040_1
  FIN_SUC_050_1(["Fin de este camino"]):::fin
  SUC_050 -->|"Relevamiento terminado"| FIN_SUC_050_1
  style SUC_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Apertura

```mermaid
flowchart TD
  subgraph F_0["Apertura"]
    SUC_100["<b>SUC_100</b> Escrito de inicio del sucesorio<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_105["<b>SUC_105</b> Cumplimiento de los recaudos observados por el juzgado<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_110["<b>SUC_110</b> Providencia de apertura del sucesorio<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_112["<b>SUC_112</b> Radicación ante el juez competente<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_120["<b>SUC_120</b> Informe del Registro de Juicios Universales<br/>Responsable: Juzgado u organismo<br/>10 días hábiles judiciales"]:::tribunal
    SUC_130["<b>SUC_130</b> Informe del Registro de Testamentos del Colegio de Escribanos<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_140["<b>SUC_140</b> Vista al Ministerio Público<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_150["<b>SUC_150</b> Audiencia de reconocimiento del testamento ológrafo o cerrado<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_160["<b>SUC_160</b> Protocolización del testamento o agregación del testimonio<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_SUC_030_origen["SUC_030 Último domicilio del causante y juzgado competente<br/>(ver Etapa previa)"]:::externo
  EXT_SUC_030_origen -.->|"Juzgado competente definido"| SUC_100
  SUC_100 -->|"Escrito de inicio presentado"| SUC_110
  SUC_105 -->|"Recaudos cumplidos"| SUC_110
  P_SUC_110_1(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"Apertura ab intestato: se ordenan edictos, cédulas y oficios"| P_SUC_110_1
  P_SUC_110_1 --> SUC_120
  P_SUC_110_1 --> SUC_130
  P_SUC_110_1 --> SUC_140
  EXT_SUC_200_destino["SUC_200 Publicación de edictos y plazo de citación de herederos y acreedores<br/>(ver Edictos y citación)"]:::externo
  P_SUC_110_1 --> EXT_SUC_200_destino
  P_SUC_110_2(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"Se presentó un testamento ológrafo o cerrado"| P_SUC_110_2
  P_SUC_110_2 --> SUC_120
  P_SUC_110_2 --> SUC_130
  P_SUC_110_2 --> SUC_140
  P_SUC_110_2 --> SUC_150
  P_SUC_110_3(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"Se presentó o se informó un testamento por acto público"| P_SUC_110_3
  P_SUC_110_3 --> SUC_120
  P_SUC_110_3 --> SUC_130
  P_SUC_110_3 --> SUC_140
  P_SUC_110_3 --> SUC_160
  P_SUC_110_4(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"El juzgado observa recaudos previos"| P_SUC_110_4
  P_SUC_110_4 --> SUC_105
  EXT_SUC_800_destino["SUC_800 Reposición contra una providencia simple<br/>(ver Recursos e incidentes)"]:::externo
  P_SUC_110_4 --> EXT_SUC_800_destino
  P_SUC_110_5(["Se abren en paralelo"]):::paralelo
  SUC_110 -->|"El juez se declara incompetente"| P_SUC_110_5
  P_SUC_110_5 --> SUC_112
  EXT_SUC_810_destino["SUC_810 Apelación de una resolución del sucesorio<br/>(ver Recursos e incidentes)"]:::externo
  P_SUC_110_5 --> EXT_SUC_810_destino
  SUC_112 -->|"Causa radicada ante el juez competente"| SUC_110
  FIN_SUC_120_1(["Fin de este camino"]):::fin
  SUC_120 -->|"Informe agregado (si hay otro sucesorio, se pide la acumulación)"| FIN_SUC_120_1
  FIN_SUC_130_1(["Fin de este camino"]):::fin
  SUC_130 -->|"Informe negativo"| FIN_SUC_130_1
  SUC_130 -->|"Informe positivo: testamento ológrafo depositado"| SUC_150
  SUC_130 -->|"Informe positivo: testamento por acto público"| SUC_160
  FIN_SUC_140_1(["Fin de este camino"]):::fin
  SUC_140 -->|"Dictamen sin observaciones, u observaciones cumplidas"| FIN_SUC_140_1
  SUC_150 -->|"Letra y firma reconocidas, y objeciones resueltas"| SUC_160
  EXT_SUC_850_destino["SUC_850 Acción de nulidad o impugnación del testamento<br/>(ver Recursos e incidentes)"]:::externo
  SUC_150 -->|"Se impugna la autenticidad o la validez del testamento"| EXT_SUC_850_destino
  P_SUC_160_1(["Se abren en paralelo"]):::paralelo
  SUC_160 -->|"Testamento protocolizado o testimonio agregado"| P_SUC_160_1
  P_SUC_160_1 --> EXT_SUC_200_destino
  EXT_SUC_220_destino["SUC_220 Citación de herederos instituidos, beneficiarios y albacea<br/>(ver Edictos y citación)"]:::externo
  P_SUC_160_1 --> EXT_SUC_220_destino
  EXT_SUC_850_origen["SUC_850 Acción de nulidad o impugnación del testamento<br/>(ver Recursos e incidentes)"]:::externo
  EXT_SUC_850_origen -.->|"Sentencia firme: testamento válido y todavía sin protocolizar"| SUC_160
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Edictos y citación

```mermaid
flowchart TD
  subgraph F_0["Edictos y citación"]
    SUC_200["<b>SUC_200</b> Publicación de edictos y plazo de citación de herederos y acreedores<br/>Responsable: Cualquier interesado<br/>30 días corridos"]:::ambas
    SUC_220["<b>SUC_220</b> Citación de herederos instituidos, beneficiarios y albacea<br/>Responsable: Cualquier interesado<br/>30 días corridos"]:::ambas
    SUC_230["<b>SUC_230</b> Intimación a un heredero a aceptar o renunciar la herencia<br/>Responsable: Otros interesados<br/>1 mes"]:::demandada
  end
  EXT_SUC_110_origen["SUC_110 Providencia de apertura del sucesorio<br/>(ver Apertura)"]:::externo
  EXT_SUC_110_origen -.->|"Apertura ab intestato: se ordenan edictos, cédulas y oficios"| SUC_200
  EXT_SUC_160_origen["SUC_160 Protocolización del testamento o agregación del testimonio<br/>(ver Apertura)"]:::externo
  EXT_SUC_160_origen -.->|"Testamento protocolizado o testimonio agregado"| SUC_200
  EXT_SUC_160_origen -.->|"Testamento protocolizado o testimonio agregado"| SUC_220
  EXT_SUC_300_destino["SUC_300 Pedido de la declaratoria de herederos<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  SUC_200 -->|"Vencida la citación: sucesión ab intestato, o testamento que no dispone de todos los bienes"| EXT_SUC_300_destino
  FIN_SUC_200_2(["Fin de este camino"]):::fin
  SUC_200 -->|"Vencida la citación: el testamento instituye herederos por todos los bienes"| FIN_SUC_200_2
  SUC_200 -->|"Un heredero citado no acepta ni renuncia: se lo intima"| SUC_230
  EXT_SUC_320_destino["SUC_320 Aprobación formal del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  SUC_220 -->|"Vencido el plazo o presentados los instituidos"| EXT_SUC_320_destino
  SUC_220 -->|"Un heredero instituido no acepta ni renuncia: se lo intima"| SUC_230
  FIN_SUC_230_1(["Fin de este camino"]):::fin
  SUC_230 -->|"Acepta o renuncia, o vence sin respuesta y se lo tiene por aceptante"| FIN_SUC_230_1
  SUC_230 -->|"Prórroga por justa causa (una sola vez)"| SUC_230
  EXT_SUC_850_origen["SUC_850 Acción de nulidad o impugnación del testamento<br/>(ver Recursos e incidentes)"]:::externo
  EXT_SUC_850_origen -.->|"Sentencia firme: testamento nulo, sigue como sucesión ab intestato"| SUC_200
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Declaratoria y aprobación del testamento

```mermaid
flowchart TD
  subgraph F_0["Declaratoria o aprobación del testamento"]
    SUC_300["<b>SUC_300</b> Pedido de la declaratoria de herederos<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_310["<b>SUC_310</b> Dictado de la declaratoria de herederos<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_320["<b>SUC_320</b> Aprobación formal del testamento<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_330["<b>SUC_330</b> Elección del trámite posterior a la declaratoria o a la aprobación del testamento<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_340["<b>SUC_340</b> Ampliación de la declaratoria de herederos<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_350["<b>SUC_350</b> Herencia vacante y designación del curador<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_SUC_200_origen["SUC_200 Publicación de edictos y plazo de citación de herederos y acreedores<br/>(ver Edictos y citación)"]:::externo
  EXT_SUC_200_origen -.->|"Vencida la citación: sucesión ab intestato, o testamento que no dispone de todos los bienes"| SUC_300
  EXT_SUC_220_origen["SUC_220 Citación de herederos instituidos, beneficiarios y albacea<br/>(ver Edictos y citación)"]:::externo
  EXT_SUC_220_origen -.->|"Vencido el plazo o presentados los instituidos"| SUC_320
  SUC_300 -->|"Pedido presentado"| SUC_310
  P_SUC_310_1(["Se abren en paralelo"]):::paralelo
  SUC_310 -->|"Declaratoria dictada y notificada"| P_SUC_310_1
  P_SUC_310_1 --> SUC_330
  EXT_SUC_810_destino["SUC_810 Apelación de una resolución del sucesorio<br/>(ver Recursos e incidentes)"]:::externo
  P_SUC_310_1 --> EXT_SUC_810_destino
  SUC_310 -->|"Se difiere la declaratoria por un vínculo no acreditado"| SUC_300
  SUC_310 -->|"Ningún heredero acredita su título: herencia vacante"| SUC_350
  P_SUC_320_1(["Se abren en paralelo"]):::paralelo
  SUC_320 -->|"Testamento aprobado y notificado"| P_SUC_320_1
  P_SUC_320_1 --> SUC_330
  P_SUC_320_1 --> EXT_SUC_810_destino
  EXT_SUC_510_destino["SUC_510 Denuncia de bienes y valuación por los herederos<br/>(ver Administración e inventario)"]:::externo
  SUC_330 -->|"Herederos capaces y de acuerdo: denuncia de bienes"| EXT_SUC_510_destino
  EXT_SUC_400_destino["SUC_400 Audiencia de designación de administrador, inventariador y tasador<br/>(ver Administración e inventario)"]:::externo
  SUC_330 -->|"Inventario y avalúo judiciales"| EXT_SUC_400_destino
  P_SUC_330_3(["Se abren en paralelo"]):::paralelo
  SUC_330 -->|"Un acreedor o legatario intima a inventariar"| P_SUC_330_3
  P_SUC_330_3 --> EXT_SUC_400_destino
  EXT_SUC_505_destino["SUC_505 Inventario intimado por acreedores o legatarios<br/>(ver Administración e inventario)"]:::externo
  P_SUC_330_3 --> EXT_SUC_505_destino
  EXT_SUC_660_destino["SUC_660 Continuación extrajudicial del sucesorio<br/>(ver Partición)"]:::externo
  SUC_330 -->|"Continuación extrajudicial (art. 733 CPCCBA)"| EXT_SUC_660_destino
  SUC_330 -->|"Aparece un heredero omitido"| SUC_340
  EXT_SUC_860_destino["SUC_860 Impugnación de la declaratoria o petición de herencia<br/>(ver Recursos e incidentes)"]:::externo
  SUC_330 -->|"Un tercero impugna la declaratoria o reclama la herencia"| EXT_SUC_860_destino
  EXT_SUC_850_destino["SUC_850 Acción de nulidad o impugnación del testamento<br/>(ver Recursos e incidentes)"]:::externo
  SUC_330 -->|"Un interesado impugna el testamento aprobado"| EXT_SUC_850_destino
  SUC_340 -->|"Declaratoria ampliada"| SUC_330
  EXT_SUC_990_destino["SUC_990 Archivo del expediente<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  SUC_350 -->|"Bienes liquidados y entregados al Estado"| EXT_SUC_990_destino
  SUC_350 -->|"Se presenta quien invoca derecho a la herencia"| EXT_SUC_860_destino
  EXT_SUC_850_origen["SUC_850 Acción de nulidad o impugnación del testamento<br/>(ver Recursos e incidentes)"]:::externo
  EXT_SUC_850_origen -.->|"Sentencia firme: testamento válido y ya aprobado"| SUC_330
  EXT_SUC_860_origen["SUC_860 Impugnación de la declaratoria o petición de herencia<br/>(ver Recursos e incidentes)"]:::externo
  EXT_SUC_860_origen -.->|"Sentencia firme: se amplía o modifica la declaratoria"| SUC_340
  EXT_SUC_860_origen -.->|"Demanda rechazada por sentencia firme"| SUC_330
  EXT_SUC_860_origen -.->|"Demanda rechazada en una herencia vacante"| SUC_350
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
    SUC_400["<b>SUC_400</b> Audiencia de designación de administrador, inventariador y tasador<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_410["<b>SUC_410</b> Aceptación del cargo de administrador<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_420["<b>SUC_420</b> Rendición de cuentas del administrador<br/>Responsable: Cualquier interesado<br/>3 meses"]:::ambas
    SUC_440["<b>SUC_440</b> Pago de deudas y legados, y venta de bienes con autorización<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
  end
  subgraph F_1["Inventario y avalúo"]
    SUC_500["<b>SUC_500</b> Inventario y avalúo judiciales<br/>Responsable: Cualquier interesado<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    SUC_505["<b>SUC_505</b> Inventario intimado por acreedores o legatarios<br/>Responsable: Heredero que representamos<br/>3 meses"]:::actora
    SUC_510["<b>SUC_510</b> Denuncia de bienes y valuación por los herederos<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_520["<b>SUC_520</b> Liquidación de los gananciales con el cónyuge supérstite<br/>Responsable: Otros interesados<br/>Sin plazo"]:::demandada
    SUC_530["<b>SUC_530</b> Traslado del inventario y avalúo o de la denuncia de bienes<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_540["<b>SUC_540</b> Aprobación del inventario y avalúo<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_SUC_330_origen["SUC_330 Elección del trámite posterior a la declaratoria o a la aprobación del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Herederos capaces y de acuerdo: denuncia de bienes"| SUC_510
  EXT_SUC_330_origen -.->|"Inventario y avalúo judiciales"| SUC_400
  EXT_SUC_330_origen -.->|"Un acreedor o legatario intima a inventariar"| SUC_400
  EXT_SUC_330_origen -.->|"Un acreedor o legatario intima a inventariar"| SUC_505
  P_SUC_400_1(["Se abren en paralelo"]):::paralelo
  SUC_400 -->|"Se designan administrador, inventariador y tasador"| P_SUC_400_1
  P_SUC_400_1 --> SUC_410
  P_SUC_400_1 --> SUC_500
  SUC_400 -->|"Se designan inventariador y tasador, sin administrador"| SUC_500
  P_SUC_410_1(["Se abren en paralelo"]):::paralelo
  SUC_410 -->|"Cargo aceptado"| P_SUC_410_1
  P_SUC_410_1 --> SUC_420
  P_SUC_410_1 --> SUC_440
  SUC_420 -->|"Rendición aprobada sin observaciones"| SUC_420
  P_SUC_420_2(["Se abren en paralelo"]):::paralelo
  SUC_420 -->|"Rendición observada: se resuelve por incidente"| P_SUC_420_2
  P_SUC_420_2 --> SUC_420
  EXT_SUC_870_destino["SUC_870 Control de la caducidad de instancia en un incidente con controversia<br/>(ver Recursos e incidentes)"]:::externo
  P_SUC_420_2 --> EXT_SUC_870_destino
  FIN_SUC_420_3(["Fin de este camino"]):::fin
  SUC_420 -->|"Cuenta final aprobada: termina la administración"| FIN_SUC_420_3
  FIN_SUC_440_1(["Fin de este camino"]):::fin
  SUC_440 -->|"Deudas, cargas y legados pagados"| FIN_SUC_440_1
  SUC_500 -->|"Inventario y avalúo presentados"| SUC_530
  P_SUC_500_2(["Se abren en paralelo"]):::paralelo
  SUC_500 -->|"Inventario y avalúo presentados, con bienes gananciales"| P_SUC_500_2
  P_SUC_500_2 --> SUC_530
  P_SUC_500_2 --> SUC_520
  FIN_SUC_505_1(["Fin de este camino"]):::fin
  SUC_505 -->|"Inventario hecho, o vencido el plazo (el heredero responde con sus propios bienes)"| FIN_SUC_505_1
  SUC_510 -->|"Denuncia presentada"| SUC_530
  P_SUC_510_2(["Se abren en paralelo"]):::paralelo
  SUC_510 -->|"Denuncia presentada, con bienes gananciales"| P_SUC_510_2
  P_SUC_510_2 --> SUC_530
  P_SUC_510_2 --> SUC_520
  FIN_SUC_520_1(["Fin de este camino"]):::fin
  SUC_520 -->|"Calificación de los bienes acordada o resuelta"| FIN_SUC_520_1
  SUC_530 -->|"Sin oposición, o reclamaciones resueltas"| SUC_540
  P_SUC_530_2(["Se abren en paralelo"]):::paralelo
  SUC_530 -->|"Hay oposición: incidente o audiencia con el perito (art. 760)"| P_SUC_530_2
  P_SUC_530_2 --> SUC_530
  P_SUC_530_2 --> EXT_SUC_870_destino
  EXT_SUC_700_destino["SUC_700 Pedido de la orden de inscripción<br/>(ver Inscripción)"]:::externo
  SUC_540 -->|"Inscripción de la declaratoria o del testamento en condominio, sin partición"| EXT_SUC_700_destino
  EXT_SUC_600_destino["SUC_600 Partición privada<br/>(ver Partición)"]:::externo
  SUC_540 -->|"Partición privada"| EXT_SUC_600_destino
  EXT_SUC_610_destino["SUC_610 Designación del partidor y presentación de la cuenta particionaria<br/>(ver Partición)"]:::externo
  SUC_540 -->|"Partición judicial"| EXT_SUC_610_destino
  EXT_SUC_650_destino["SUC_650 Colación y reducción para proteger la legítima<br/>(ver Partición)"]:::externo
  SUC_540 -->|"Un coheredero reclama colación o reducción"| EXT_SUC_650_destino
  EXT_SUC_660_origen["SUC_660 Continuación extrajudicial del sucesorio<br/>(ver Partición)"]:::externo
  EXT_SUC_660_origen -.->|"Desinteligencias entre herederos u organismos: vuelve al juez"| SUC_400
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
    SUC_600["<b>SUC_600</b> Partición privada<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_610["<b>SUC_610</b> Designación del partidor y presentación de la cuenta particionaria<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_620["<b>SUC_620</b> Traslado de la cuenta particionaria<br/>Responsable: Cualquier interesado<br/>10 días hábiles judiciales + gracia"]:::ambas
    SUC_650["<b>SUC_650</b> Colación y reducción para proteger la legítima<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
    SUC_660["<b>SUC_660</b> Continuación extrajudicial del sucesorio<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  EXT_SUC_330_origen["SUC_330 Elección del trámite posterior a la declaratoria o a la aprobación del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Continuación extrajudicial (art. 733 CPCCBA)"| SUC_660
  EXT_SUC_540_origen["SUC_540 Aprobación del inventario y avalúo<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_540_origen -.->|"Partición privada"| SUC_600
  EXT_SUC_540_origen -.->|"Partición judicial"| SUC_610
  EXT_SUC_540_origen -.->|"Un coheredero reclama colación o reducción"| SUC_650
  EXT_SUC_700_destino["SUC_700 Pedido de la orden de inscripción<br/>(ver Inscripción)"]:::externo
  SUC_600 -->|"Partición presentada y aprobada"| EXT_SUC_700_destino
  SUC_600 -->|"No hay acuerdo: partición judicial"| SUC_610
  SUC_610 -->|"Cuenta particionaria presentada"| SUC_620
  SUC_610 -->|"El partidor no la presenta en término: remoción y nueva designación"| SUC_610
  SUC_620 -->|"Cuenta aprobada, con o sin oposición"| EXT_SUC_700_destino
  P_SUC_620_2(["Se abren en paralelo"]):::paralelo
  SUC_620 -->|"Cuenta rechazada"| P_SUC_620_2
  P_SUC_620_2 --> SUC_610
  EXT_SUC_810_destino["SUC_810 Apelación de una resolución del sucesorio<br/>(ver Recursos e incidentes)"]:::externo
  P_SUC_620_2 --> EXT_SUC_810_destino
  SUC_650 -->|"Sentencia firme o acuerdo: se ajusta la masa partible"| SUC_610
  SUC_660 -->|"Operaciones cumplidas y copias agregadas al expediente"| EXT_SUC_700_destino
  EXT_SUC_400_destino["SUC_400 Audiencia de designación de administrador, inventariador y tasador<br/>(ver Administración e inventario)"]:::externo
  SUC_660 -->|"Desinteligencias entre herederos u organismos: vuelve al juez"| EXT_SUC_400_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Inscripción

```mermaid
flowchart TD
  subgraph F_0["Inscripción"]
    SUC_700["<b>SUC_700</b> Pedido de la orden de inscripción<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_740["<b>SUC_740</b> Orden de inscripción y libramiento de oficios y testimonios<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_750["<b>SUC_750</b> Inscripción en el Registro de la Propiedad Inmueble de PBA<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_752["<b>SUC_752</b> Inscripción de automotores en el DNRPA<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_754["<b>SUC_754</b> Transferencia de fondos y de participaciones societarias<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_756["<b>SUC_756</b> Venta por los herederos con tracto abreviado<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_758["<b>SUC_758</b> Inscripción de bienes en otra jurisdicción por oficio Ley 22.172<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
  end
  EXT_SUC_540_origen["SUC_540 Aprobación del inventario y avalúo<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_540_origen -.->|"Inscripción de la declaratoria o del testamento en condominio, sin partición"| SUC_700
  EXT_SUC_600_origen["SUC_600 Partición privada<br/>(ver Partición)"]:::externo
  EXT_SUC_600_origen -.->|"Partición presentada y aprobada"| SUC_700
  EXT_SUC_620_origen["SUC_620 Traslado de la cuenta particionaria<br/>(ver Partición)"]:::externo
  EXT_SUC_620_origen -.->|"Cuenta aprobada, con o sin oposición"| SUC_700
  EXT_SUC_660_origen["SUC_660 Continuación extrajudicial del sucesorio<br/>(ver Partición)"]:::externo
  EXT_SUC_660_origen -.->|"Operaciones cumplidas y copias agregadas al expediente"| SUC_700
  P_SUC_700_1(["Se abren en paralelo"]):::paralelo
  SUC_700 -->|"Inscripción pedida"| P_SUC_700_1
  P_SUC_700_1 --> SUC_740
  EXT_SUC_900_destino["SUC_900 Pago de la tasa de justicia y de la contribución para la Caja de Abogados<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  P_SUC_700_1 --> EXT_SUC_900_destino
  EXT_SUC_910_destino["SUC_910 Declaración jurada y pago del ITGB ante ARBA<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  P_SUC_700_1 --> EXT_SUC_910_destino
  EXT_SUC_920_destino["SUC_920 Regulación de honorarios<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  P_SUC_700_1 --> EXT_SUC_920_destino
  P_SUC_740_1(["Se abren en paralelo"]):::paralelo
  SUC_740 -->|"Orden de inscripción dictada"| P_SUC_740_1
  P_SUC_740_1 --> SUC_750
  P_SUC_740_1 --> SUC_752
  P_SUC_740_1 --> SUC_754
  EXT_SUC_980_destino["SUC_980 Entrega de hijuelas y testimonios, y rendición al cliente<br/>(ver Impuestos, tasas, honorarios y cierre)"]:::externo
  P_SUC_740_1 --> EXT_SUC_980_destino
  SUC_740 -->|"Los herederos venden con tracto abreviado"| SUC_756
  FIN_SUC_750_1(["Fin de este camino"]):::fin
  SUC_750 -->|"Inscripción registrada, o no hay inmuebles en PBA"| FIN_SUC_750_1
  SUC_750 -->|"Observada por el Registro: subsanar y reingresar"| SUC_750
  SUC_750 -->|"Hay inmuebles en otra jurisdicción"| SUC_758
  FIN_SUC_752_1(["Fin de este camino"]):::fin
  SUC_752 -->|"Inscripción registrada, o no hay automotores"| FIN_SUC_752_1
  FIN_SUC_754_1(["Fin de este camino"]):::fin
  SUC_754 -->|"Fondos y participaciones transferidos, o no hay"| FIN_SUC_754_1
  SUC_756 -->|"Escritura otorgada e inscripta"| EXT_SUC_980_destino
  FIN_SUC_758_1(["Fin de este camino"]):::fin
  SUC_758 -->|"Inscripción registrada en la otra jurisdicción"| FIN_SUC_758_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Impuestos, tasas, honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Impuestos y tasas"]
    SUC_900["<b>SUC_900</b> Pago de la tasa de justicia y de la contribución para la Caja de Abogados<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_910["<b>SUC_910</b> Declaración jurada y pago del ITGB ante ARBA<br/>Responsable: Heredero que representamos<br/>15 días corridos"]:::actora
    SUC_920["<b>SUC_920</b> Regulación de honorarios<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    SUC_925["<b>SUC_925</b> Apelación de la regulación de honorarios<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_930["<b>SUC_930</b> Pago de honorarios y depósito de los aportes de la Ley 6716<br/>Responsable: Heredero que representamos<br/>60 días corridos"]:::actora
  end
  subgraph F_1["Cierre"]
    SUC_980["<b>SUC_980</b> Entrega de hijuelas y testimonios, y rendición al cliente<br/>Responsable: Heredero que representamos<br/>Sin plazo"]:::actora
    SUC_990["<b>SUC_990</b> Archivo del expediente<br/>Responsable: Cualquier interesado<br/>Sin plazo"]:::ambas
  end
  EXT_SUC_016_origen["SUC_016 Vencimiento máximo del ITGB: 24 meses desde el fallecimiento<br/>(ver Etapa previa)"]:::externo
  EXT_SUC_016_origen -.->|"Se cumplen 24 meses sin haber pedido la inscripción"| SUC_910
  EXT_SUC_350_origen["SUC_350 Herencia vacante y designación del curador<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_350_origen -.->|"Bienes liquidados y entregados al Estado"| SUC_990
  EXT_SUC_700_origen["SUC_700 Pedido de la orden de inscripción<br/>(ver Inscripción)"]:::externo
  EXT_SUC_700_origen -.->|"Inscripción pedida"| SUC_900
  EXT_SUC_700_origen -.->|"Inscripción pedida"| SUC_910
  EXT_SUC_700_origen -.->|"Inscripción pedida"| SUC_920
  EXT_SUC_740_origen["SUC_740 Orden de inscripción y libramiento de oficios y testimonios<br/>(ver Inscripción)"]:::externo
  EXT_SUC_740_origen -.->|"Orden de inscripción dictada"| SUC_980
  EXT_SUC_756_origen["SUC_756 Venta por los herederos con tracto abreviado<br/>(ver Inscripción)"]:::externo
  EXT_SUC_756_origen -.->|"Escritura otorgada e inscripta"| SUC_980
  FIN_SUC_900_1(["Fin de este camino"]):::fin
  SUC_900 -->|"Tasa y contribución pagadas sin observaciones"| FIN_SUC_900_1
  SUC_900 -->|"El juzgado observa la liquidación: integrar la diferencia"| SUC_900
  FIN_SUC_910_1(["Fin de este camino"]):::fin
  SUC_910 -->|"Declaración jurada presentada y pagada, o no corresponde"| FIN_SUC_910_1
  SUC_910 -->|"ARBA observa: rectificar la declaración jurada"| SUC_910
  P_SUC_920_1(["Se abren en paralelo"]):::paralelo
  SUC_920 -->|"Regulación notificada"| P_SUC_920_1
  P_SUC_920_1 --> SUC_925
  P_SUC_920_1 --> SUC_930
  FIN_SUC_925_1(["Fin de este camino"]):::fin
  SUC_925 -->|"Regulación firme: no apelada o resuelta por la Cámara"| FIN_SUC_925_1
  FIN_SUC_930_1(["Fin de este camino"]):::fin
  SUC_930 -->|"Honorarios y aportes pagados"| FIN_SUC_930_1
  SUC_980 -->|"Inscripciones terminadas y documentación entregada"| SUC_990
  style SUC_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 9. Recursos e incidentes

```mermaid
flowchart TD
  subgraph F_0["Recursos e incidentes"]
    SUC_800["<b>SUC_800</b> Reposición contra una providencia simple<br/>Responsable: Cualquier interesado<br/>3 días hábiles judiciales + gracia"]:::ambas
    SUC_810["<b>SUC_810</b> Apelación de una resolución del sucesorio<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_815["<b>SUC_815</b> Memorial de la apelación en relación<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
    SUC_850["<b>SUC_850</b> Acción de nulidad o impugnación del testamento<br/>Responsable: Otros interesados<br/>Sin plazo"]:::demandada
    SUC_860["<b>SUC_860</b> Impugnación de la declaratoria o petición de herencia<br/>Responsable: Otros interesados<br/>Sin plazo"]:::demandada
    SUC_870["<b>SUC_870</b> Control de la caducidad de instancia en un incidente con controversia<br/>Responsable: Cualquier interesado<br/>3 meses"]:::ambas
    SUC_875["<b>SUC_875</b> Intimación a activar el incidente bajo apercibimiento de caducidad<br/>Responsable: Cualquier interesado<br/>5 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_SUC_110_origen["SUC_110 Providencia de apertura del sucesorio<br/>(ver Apertura)"]:::externo
  EXT_SUC_110_origen -.->|"El juzgado observa recaudos previos"| SUC_800
  EXT_SUC_110_origen -.->|"El juez se declara incompetente"| SUC_810
  EXT_SUC_150_origen["SUC_150 Audiencia de reconocimiento del testamento ológrafo o cerrado<br/>(ver Apertura)"]:::externo
  EXT_SUC_150_origen -.->|"Se impugna la autenticidad o la validez del testamento"| SUC_850
  EXT_SUC_310_origen["SUC_310 Dictado de la declaratoria de herederos<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_310_origen -.->|"Declaratoria dictada y notificada"| SUC_810
  EXT_SUC_320_origen["SUC_320 Aprobación formal del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_320_origen -.->|"Testamento aprobado y notificado"| SUC_810
  EXT_SUC_330_origen["SUC_330 Elección del trámite posterior a la declaratoria o a la aprobación del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_330_origen -.->|"Un tercero impugna la declaratoria o reclama la herencia"| SUC_860
  EXT_SUC_330_origen -.->|"Un interesado impugna el testamento aprobado"| SUC_850
  EXT_SUC_350_origen["SUC_350 Herencia vacante y designación del curador<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  EXT_SUC_350_origen -.->|"Se presenta quien invoca derecho a la herencia"| SUC_860
  EXT_SUC_420_origen["SUC_420 Rendición de cuentas del administrador<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_420_origen -.->|"Rendición observada: se resuelve por incidente"| SUC_870
  EXT_SUC_530_origen["SUC_530 Traslado del inventario y avalúo o de la denuncia de bienes<br/>(ver Administración e inventario)"]:::externo
  EXT_SUC_530_origen -.->|"Hay oposición: incidente o audiencia con el perito (art. 760)"| SUC_870
  EXT_SUC_620_origen["SUC_620 Traslado de la cuenta particionaria<br/>(ver Partición)"]:::externo
  EXT_SUC_620_origen -.->|"Cuenta rechazada"| SUC_810
  FIN_SUC_800_1(["Fin de este camino"]):::fin
  SUC_800 -->|"Reposición resuelta (o la apelación en subsidio), o plazo vencido sin recurrir"| FIN_SUC_800_1
  FIN_SUC_810_1(["Fin de este camino"]):::fin
  SUC_810 -->|"No se apela, o se deniega el recurso (queja o queda firme)"| FIN_SUC_810_1
  SUC_810 -->|"Apelación concedida en relación"| SUC_815
  FIN_SUC_815_1(["Fin de este camino"]):::fin
  SUC_815 -->|"La Cámara resuelve, o el recurso se declara desierto"| FIN_SUC_815_1
  EXT_SUC_160_destino["SUC_160 Protocolización del testamento o agregación del testimonio<br/>(ver Apertura)"]:::externo
  SUC_850 -->|"Sentencia firme: testamento válido y todavía sin protocolizar"| EXT_SUC_160_destino
  EXT_SUC_330_destino["SUC_330 Elección del trámite posterior a la declaratoria o a la aprobación del testamento<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  SUC_850 -->|"Sentencia firme: testamento válido y ya aprobado"| EXT_SUC_330_destino
  EXT_SUC_200_destino["SUC_200 Publicación de edictos y plazo de citación de herederos y acreedores<br/>(ver Edictos y citación)"]:::externo
  SUC_850 -->|"Sentencia firme: testamento nulo, sigue como sucesión ab intestato"| EXT_SUC_200_destino
  EXT_SUC_340_destino["SUC_340 Ampliación de la declaratoria de herederos<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  SUC_860 -->|"Sentencia firme: se amplía o modifica la declaratoria"| EXT_SUC_340_destino
  SUC_860 -->|"Demanda rechazada por sentencia firme"| EXT_SUC_330_destino
  EXT_SUC_350_destino["SUC_350 Herencia vacante y designación del curador<br/>(ver Declaratoria y aprobación del testamento)"]:::externo
  SUC_860 -->|"Demanda rechazada en una herencia vacante"| EXT_SUC_350_destino
  FIN_SUC_870_1(["Fin de este camino"]):::fin
  SUC_870 -->|"El incidente se resolvió"| FIN_SUC_870_1
  SUC_870 -->|"Se pide la caducidad: el juez intima a activar"| SUC_875
  SUC_875 -->|"Se activa el incidente en término"| SUC_870
  FIN_SUC_875_2(["Fin de este camino"]):::fin
  SUC_875 -->|"No se activa: se decreta la caducidad"| FIN_SUC_875_2
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
