# Diagrama de Flujo: Juicio oral y público (PBA)

**Régimen:** CPP PBA (Ley 11.922 y modificatorias); juicio por jurados (arts. 22 bis, 338 bis a 338 quáter, 371 bis a 371 quáter y 375 bis, Ley 14.543); Ley 14.967 (honorarios); Código Penal · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_penal_juicio_oral_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima constituida en parte (ACTORA); naranja = imputado y defensa (DEMANDADA); gris = Juzgado Correccional, Tribunal en lo Criminal, jurados, Cámara, Casación u otros órganos, aclarado en el nombre del hito (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, desde la radicación corren a la vez la preparación del juicio y el plazo de 6 meses para hacer el debate; con imputado detenido, también la excarcelación y el control del plazo máximo con detenido.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo penal, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la intervención judicial formal (consulta, denuncia, designación de defensor, constitución como particular damnificado). La app los separa en el flujo prejudicial; en penal hay duda sobre si eso tiene sentido desde la denuncia.
* **Plazos corridos (art. 139 CPP PBA):** la mayoría de los plazos procesales penales son días continuos (CORRIDOS), no hábiles judiciales. Aplica_Gracia = NO en todos los hitos.
* **Órgano de juicio (arts. 22 y 22 bis):** Juzgado Correccional o Tribunal en lo Criminal (unipersonal si la pena máxima en abstracto no supera 15 años; colegiado para funcionarios o por opción de la defensa en el plazo del art. 336). Jurados si la máxima supera 15 años, salvo renuncia ratificada en ese mismo plazo.
* **Derivación desde la IPP:** el expediente vinculado nace en la radicación tras el auto o decreto firme de elevación; no se copian relatos ni datos sensibles.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Radicación<br/>3 hitos"]
  FASE_2["Preparación<br/>6 hitos"]
  FASE_3["Jurados<br/>5 hitos"]
  FASE_4["Debate<br/>7 hitos"]
  FASE_5["Libertad<br/>5 hitos"]
  FASE_6["Sentencia<br/>5 hitos"]
  FASE_7["Recursos<br/>6 hitos"]
  FASE_8["Cierre<br/>6 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_5
  FASE_2 --> FASE_8
  FASE_2 --> FASE_7
  FASE_2 --> FASE_4
  FASE_2 --> FASE_3
  FASE_5 --> FASE_8
  FASE_3 --> FASE_4
  FASE_3 --> FASE_6
  FASE_4 --> FASE_6
  FASE_4 --> FASE_3
  FASE_6 --> FASE_3
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_2
```

## 1. Radicación y órgano de juicio

```mermaid
flowchart TD
  subgraph F_0["Radicación"]
    JOR_010["INICIO - <b>JOR_010</b> Radicación tras la elevación a juicio<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_020["<b>JOR_020</b> Integración del órgano de juicio<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_040["<b>JOR_040</b> Juicio por jurados: sorteo del juez y lista de jurados<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
  end
  P_JOR_010_1(["Se abren en paralelo"]):::paralelo
  JOR_010 -->|"Imputado en libertad"| P_JOR_010_1
  P_JOR_010_1 --> JOR_020
  EXT_JOR_160_destino["JOR_160 Plazo para realizar el debate (6 meses)<br/>(ver Preparación del juicio)"]:::externo
  P_JOR_010_1 --> EXT_JOR_160_destino
  P_JOR_010_2(["Se abren en paralelo"]):::paralelo
  JOR_010 -->|"Imputado detenido"| P_JOR_010_2
  P_JOR_010_2 --> JOR_020
  P_JOR_010_2 --> EXT_JOR_160_destino
  EXT_JOR_230_destino["JOR_230 Pedido de excarcelación o eximición de prisión<br/>(ver Situación de libertad en el juicio)"]:::externo
  P_JOR_010_2 --> EXT_JOR_230_destino
  EXT_JOR_290_destino["JOR_290 Control del plazo máximo con detenido (2 años)<br/>(ver Situación de libertad en el juicio)"]:::externo
  P_JOR_010_2 --> EXT_JOR_290_destino
  EXT_JOR_100_destino["JOR_100 Citación a juicio: recusaciones y ofrecimiento de prueba (10 días)<br/>(ver Preparación del juicio)"]:::externo
  JOR_020 -->|"Tribunal técnico (Correccional o Criminal)"| EXT_JOR_100_destino
  JOR_020 -->|"Tribunal de jurados"| JOR_040
  JOR_040 -->|"Juez sorteado y tribunal notificado"| EXT_JOR_100_destino
  style JOR_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Preparación del juicio

```mermaid
flowchart TD
  subgraph F_0["Preparación"]
    JOR_100["<b>JOR_100</b> Citación a juicio: recusaciones y ofrecimiento de prueba (10 días)<br/>Responsable: Cualquiera de las partes<br/>10 días corridos"]:::ambas
    JOR_120["<b>JOR_120</b> Audiencia preliminar<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    JOR_130["<b>JOR_130</b> Planteo de nulidades<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_140["<b>JOR_140</b> Instrucción suplementaria<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_150["<b>JOR_150</b> Fecha del debate fijada<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    JOR_160["<b>JOR_160</b> Plazo para realizar el debate (6 meses)<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>6 meses"]:::tribunal
  end
  EXT_JOR_010_origen["JOR_010 Radicación tras la elevación a juicio<br/>(ver Radicación y órgano de juicio)"]:::externo
  EXT_JOR_010_origen -.->|"Imputado en libertad"| JOR_160
  EXT_JOR_010_origen -.->|"Imputado detenido"| JOR_160
  EXT_JOR_020_origen["JOR_020 Integración del órgano de juicio<br/>(ver Radicación y órgano de juicio)"]:::externo
  EXT_JOR_020_origen -.->|"Tribunal técnico (Correccional o Criminal)"| JOR_100
  EXT_JOR_040_origen["JOR_040 Juicio por jurados: sorteo del juez y lista de jurados<br/>(ver Radicación y órgano de juicio)"]:::externo
  EXT_JOR_040_origen -.->|"Juez sorteado y tribunal notificado"| JOR_100
  JOR_100 -->|"Se pidió audiencia preliminar, o hay jurados"| JOR_120
  JOR_100 -->|"Sin audiencia preliminar: se fija el debate"| JOR_150
  JOR_120 -->|"Planteos de nulidad"| JOR_130
  JOR_120 -->|"Se ordena instrucción suplementaria"| JOR_140
  JOR_120 -->|"Se fija la fecha del debate"| JOR_150
  EXT_JOR_955_destino["JOR_955 Sigue en la matriz de juicio abreviado<br/>(ver Firmeza, cómputo y derivaciones)"]:::externo
  JOR_120 -->|"Acuerdo de juicio abreviado"| EXT_JOR_955_destino
  JOR_130 -->|"Nulidad resuelta: se fija el debate"| JOR_150
  P_JOR_130_2(["Se abren en paralelo"]):::paralelo
  JOR_130 -->|"Rechazo sin sustanciación: reposición"| P_JOR_130_2
  EXT_JOR_800_destino["JOR_800 Recurso de reposición<br/>(ver Recursos)"]:::externo
  P_JOR_130_2 --> EXT_JOR_800_destino
  P_JOR_130_2 --> JOR_150
  EXT_JOR_900_destino["JOR_900 Firmeza de la sentencia<br/>(ver Firmeza, cómputo y derivaciones)"]:::externo
  JOR_130 -->|"Nulidad o excepción que termina el juicio (sobreseimiento, art. 341)"| EXT_JOR_900_destino
  JOR_140 -->|"Instrucción cumplida: nueva audiencia preliminar"| JOR_120
  JOR_140 -->|"Instrucción cumplida: se fija el debate"| JOR_150
  EXT_JOR_400_destino["JOR_400 Apertura del debate y cuestiones preliminares<br/>(ver Debate)"]:::externo
  JOR_150 -->|"Tribunal técnico: llega la fecha del debate"| EXT_JOR_400_destino
  EXT_JOR_310_destino["JOR_310 Audiencia de selección del jurado<br/>(ver Juicio por jurados)"]:::externo
  JOR_150 -->|"Jurados: llega la fecha del juicio"| EXT_JOR_310_destino
  JOR_150 -->|"Acuerdo de juicio abreviado hasta 30 días antes"| EXT_JOR_955_destino
  FIN_JOR_160_1(["Fin de este camino"]):::fin
  JOR_160 -->|"Debate iniciado dentro del plazo"| FIN_JOR_160_1
  FIN_JOR_160_2(["Fin de este camino"]):::fin
  JOR_160 -->|"Vence sin debate: pérdida de competencia y comunicación a la SCBA"| FIN_JOR_160_2
  EXT_JOR_820_origen["JOR_820 Recurso de casación ante el Tribunal de Casación Penal (20 días)<br/>(ver Recursos)"]:::externo
  EXT_JOR_820_origen -.->|"Casación anula y reenvía a nuevo juicio (art. 473)"| JOR_150
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Juicio por jurados

```mermaid
flowchart TD
  subgraph F_0["Jurados"]
    JOR_310["<b>JOR_310</b> Audiencia de selección del jurado<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    JOR_320["<b>JOR_320</b> Audiencia de instrucciones al jurado<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_330["<b>JOR_330</b> Explicación de las instrucciones y deliberación del jurado<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_340["<b>JOR_340</b> Veredicto del jurado<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_345["<b>JOR_345</b> Jurado estancado<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
  end
  EXT_JOR_150_origen["JOR_150 Fecha del debate fijada<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_150_origen -.->|"Jurados: llega la fecha del juicio"| JOR_310
  EXT_JOR_400_destino["JOR_400 Apertura del debate y cuestiones preliminares<br/>(ver Debate)"]:::externo
  JOR_310 -->|"Jurado integrado: apertura del debate"| EXT_JOR_400_destino
  JOR_320 -->|"Instrucciones decididas"| JOR_330
  JOR_330 -->|"El jurado llega a un veredicto"| JOR_340
  JOR_330 -->|"El jurado se declara estancado"| JOR_345
  EXT_JOR_520_destino["JOR_520 Absolución<br/>(ver Veredicto y sentencia)"]:::externo
  JOR_340 -->|"No culpabilidad: absolución irrecurrible"| EXT_JOR_520_destino
  EXT_JOR_510_destino["JOR_510 Cesura del juicio (determinación de la pena)<br/>(ver Veredicto y sentencia)"]:::externo
  JOR_340 -->|"Culpabilidad o no culpabilidad por inimputabilidad: cesura obligatoria"| EXT_JOR_510_destino
  JOR_345 -->|"El fiscal desiste y no acusa el particular damnificado: absolución"| EXT_JOR_520_destino
  JOR_345 -->|"Sigue la acusación: nueva deliberación"| JOR_330
  JOR_345 -->|"Persiste el estancamiento: nuevo juicio con otro jurado"| JOR_310
  EXT_JOR_460_origen["JOR_460 Clausura del debate<br/>(ver Debate)"]:::externo
  EXT_JOR_460_origen -.->|"Jurados: audiencia de instrucciones"| JOR_320
  EXT_JOR_510_origen["JOR_510 Cesura del juicio (determinación de la pena)<br/>(ver Veredicto y sentencia)"]:::externo
  EXT_JOR_510_origen -.->|"El juez anula el veredicto de culpabilidad: nuevo juicio con otro jurado"| JOR_310
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Debate

```mermaid
flowchart TD
  subgraph F_0["Debate"]
    JOR_400["<b>JOR_400</b> Apertura del debate y cuestiones preliminares<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
    JOR_410["<b>JOR_410</b> Declaración del imputado en el debate<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JOR_420["<b>JOR_420</b> Producción de prueba en el debate<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_430["<b>JOR_430</b> Ampliación del requerimiento fiscal<br/>Responsable: Fiscal / particular damnificado<br/>Sin plazo"]:::actora
    JOR_440["<b>JOR_440</b> Discusión final (alegatos)<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_450["<b>JOR_450</b> Última palabra del imputado<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JOR_460["<b>JOR_460</b> Clausura del debate<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
  end
  EXT_JOR_150_origen["JOR_150 Fecha del debate fijada<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_150_origen -.->|"Tribunal técnico: llega la fecha del debate"| JOR_400
  EXT_JOR_310_origen["JOR_310 Audiencia de selección del jurado<br/>(ver Juicio por jurados)"]:::externo
  EXT_JOR_310_origen -.->|"Jurado integrado: apertura del debate"| JOR_400
  JOR_400 -->|"Cuestiones preliminares resueltas"| JOR_410
  JOR_410 -->|"Declaración recibida o abstención"| JOR_420
  JOR_420 -->|"Surge un hecho o agravante nuevo: ampliación"| JOR_430
  JOR_420 -->|"Prueba concluida: discusión final"| JOR_440
  JOR_430 -->|"Ampliación admitida o rechazada: sigue la prueba"| JOR_420
  JOR_440 -->|"Alegatos y réplicas concluidos"| JOR_450
  JOR_450 -->|"Última palabra ejercida o no"| JOR_460
  EXT_JOR_500_destino["JOR_500 Veredicto del tribunal y lectura de fundamentos (5 días)<br/>(ver Veredicto y sentencia)"]:::externo
  JOR_460 -->|"Tribunal técnico: deliberación y veredicto"| EXT_JOR_500_destino
  EXT_JOR_320_destino["JOR_320 Audiencia de instrucciones al jurado<br/>(ver Juicio por jurados)"]:::externo
  JOR_460 -->|"Jurados: audiencia de instrucciones"| EXT_JOR_320_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Situación de libertad en el juicio

```mermaid
flowchart TD
  subgraph F_0["Libertad"]
    JOR_230["<b>JOR_230</b> Pedido de excarcelación o eximición de prisión<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JOR_240["<b>JOR_240</b> Resolución del pedido de excarcelación<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>5 días corridos"]:::tribunal
    JOR_270["<b>JOR_270</b> Apelación de la coerción o de la denegatoria de excarcelación<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    JOR_280["<b>JOR_280</b> Alternativas a la prisión preventiva y morigeración<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JOR_290["<b>JOR_290</b> Control del plazo máximo con detenido (2 años)<br/>Responsable: Imputado / defensa<br/>2 años"]:::demandada
  end
  EXT_JOR_010_origen["JOR_010 Radicación tras la elevación a juicio<br/>(ver Radicación y órgano de juicio)"]:::externo
  EXT_JOR_010_origen -.->|"Imputado detenido"| JOR_230
  EXT_JOR_010_origen -.->|"Imputado detenido"| JOR_290
  JOR_230 -->|"Pedido presentado"| JOR_240
  FIN_JOR_240_1(["Fin de este camino"]):::fin
  JOR_240 -->|"Excarcelación concedida"| FIN_JOR_240_1
  JOR_240 -->|"Excarcelación denegada: apelación"| JOR_270
  JOR_240 -->|"Excarcelación denegada: alternativas o morigeración"| JOR_280
  EXT_JOR_960_destino["JOR_960 Sigue en la matriz de hábeas corpus<br/>(ver Firmeza, cómputo y derivaciones)"]:::externo
  JOR_240 -->|"Excarcelación denegada: hábeas corpus"| EXT_JOR_960_destino
  FIN_JOR_270_1(["Fin de este camino"]):::fin
  JOR_270 -->|"Apelación resuelta por la Cámara, desistida o no interpuesta"| FIN_JOR_270_1
  JOR_270 -->|"Se opta por el hábeas corpus (art. 164)"| EXT_JOR_960_destino
  FIN_JOR_280_1(["Fin de este camino"]):::fin
  JOR_280 -->|"Alternativa o morigeración resuelta"| FIN_JOR_280_1
  FIN_JOR_290_1(["Fin de este camino"]):::fin
  JOR_290 -->|"El proceso terminó o la detención cesó antes del vencimiento"| FIN_JOR_290_1
  JOR_290 -->|"Vence el plazo: pedir libertad, cese o morigeración"| JOR_280
  JOR_290 -->|"Vence el plazo: hábeas corpus"| EXT_JOR_960_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Veredicto y sentencia

```mermaid
flowchart TD
  subgraph F_0["Sentencia"]
    JOR_500["<b>JOR_500</b> Veredicto del tribunal y lectura de fundamentos (5 días)<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>5 días corridos"]:::tribunal
    JOR_510["<b>JOR_510</b> Cesura del juicio (determinación de la pena)<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_520["<b>JOR_520</b> Absolución<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_530["<b>JOR_530</b> Condena<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_550["<b>JOR_550</b> Regulación e impugnación de honorarios (Ley 14.967)<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
  end
  EXT_JOR_340_origen["JOR_340 Veredicto del jurado<br/>(ver Juicio por jurados)"]:::externo
  EXT_JOR_340_origen -.->|"No culpabilidad: absolución irrecurrible"| JOR_520
  EXT_JOR_340_origen -.->|"Culpabilidad o no culpabilidad por inimputabilidad: cesura obligatoria"| JOR_510
  EXT_JOR_345_origen["JOR_345 Jurado estancado<br/>(ver Juicio por jurados)"]:::externo
  EXT_JOR_345_origen -.->|"El fiscal desiste y no acusa el particular damnificado: absolución"| JOR_520
  EXT_JOR_460_origen["JOR_460 Clausura del debate<br/>(ver Debate)"]:::externo
  EXT_JOR_460_origen -.->|"Tribunal técnico: deliberación y veredicto"| JOR_500
  JOR_500 -->|"Veredicto absolutorio"| JOR_520
  JOR_500 -->|"Veredicto condenatorio: sentencia"| JOR_530
  JOR_500 -->|"Veredicto condenatorio: se difiere la pena (cesura)"| JOR_510
  JOR_510 -->|"Pena o medida de seguridad determinada"| JOR_530
  EXT_JOR_310_destino["JOR_310 Audiencia de selección del jurado<br/>(ver Juicio por jurados)"]:::externo
  JOR_510 -->|"El juez anula el veredicto de culpabilidad: nuevo juicio con otro jurado"| EXT_JOR_310_destino
  P_JOR_520_1(["Se abren en paralelo"]):::paralelo
  JOR_520 -->|"Sentencia notificada"| P_JOR_520_1
  EXT_JOR_600_destino["JOR_600 Decisión de recurrir la sentencia<br/>(ver Recursos)"]:::externo
  P_JOR_520_1 --> EXT_JOR_600_destino
  P_JOR_520_1 --> JOR_550
  P_JOR_530_1(["Se abren en paralelo"]):::paralelo
  JOR_530 -->|"Sentencia notificada"| P_JOR_530_1
  P_JOR_530_1 --> EXT_JOR_600_destino
  P_JOR_530_1 --> JOR_550
  FIN_JOR_550_1(["Fin de este camino"]):::fin
  JOR_550 -->|"Honorarios firmes, impugnación resuelta o sin regulación"| FIN_JOR_550_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Recursos

```mermaid
flowchart TD
  subgraph F_0["Recursos"]
    JOR_600["<b>JOR_600</b> Decisión de recurrir la sentencia<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_800["<b>JOR_800</b> Recurso de reposición<br/>Responsable: Cualquiera de las partes<br/>3 días corridos"]:::ambas
    JOR_810["<b>JOR_810</b> Apelación de la sentencia correccional ante la Cámara (20 días)<br/>Responsable: Cualquiera de las partes<br/>20 días corridos"]:::ambas
    JOR_820["<b>JOR_820</b> Recurso de casación ante el Tribunal de Casación Penal (20 días)<br/>Responsable: Cualquiera de las partes<br/>20 días corridos"]:::ambas
    JOR_830["<b>JOR_830</b> Recursos extraordinarios ante la SCBA (10 días hábiles)<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
    JOR_840["<b>JOR_840</b> Recurso extraordinario federal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JOR_130_origen["JOR_130 Planteo de nulidades<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_130_origen -.->|"Rechazo sin sustanciación: reposición"| JOR_800
  EXT_JOR_520_origen["JOR_520 Absolución<br/>(ver Veredicto y sentencia)"]:::externo
  EXT_JOR_520_origen -.->|"Sentencia notificada"| JOR_600
  EXT_JOR_530_origen["JOR_530 Condena<br/>(ver Veredicto y sentencia)"]:::externo
  EXT_JOR_530_origen -.->|"Sentencia notificada"| JOR_600
  JOR_600 -->|"Tribunal en lo Criminal o jurados: casación"| JOR_820
  JOR_600 -->|"Juzgado Correccional: apelación"| JOR_810
  EXT_JOR_900_destino["JOR_900 Firmeza de la sentencia<br/>(ver Firmeza, cómputo y derivaciones)"]:::externo
  JOR_600 -->|"No se recurre o la sentencia es irrecurrible"| EXT_JOR_900_destino
  FIN_JOR_800_1(["Fin de este camino"]):::fin
  JOR_800 -->|"Reposición resuelta o plazo vencido"| FIN_JOR_800_1
  JOR_810 -->|"La Cámara resuelve y no se recurre más"| EXT_JOR_900_destino
  JOR_810 -->|"Apelación denegada: queja resuelta o no interpuesta"| EXT_JOR_900_destino
  JOR_810 -->|"La Cámara resuelve: recursos extraordinarios ante la SCBA"| JOR_830
  JOR_820 -->|"Casación resuelta y no se recurre más"| EXT_JOR_900_destino
  JOR_820 -->|"Casación denegada o no manifestada en 7 días: queja resuelta o no interpuesta"| EXT_JOR_900_destino
  JOR_820 -->|"Casación resuelta: recursos extraordinarios ante la SCBA"| JOR_830
  EXT_JOR_150_destino["JOR_150 Fecha del debate fijada<br/>(ver Preparación del juicio)"]:::externo
  JOR_820 -->|"Casación anula y reenvía a nuevo juicio (art. 473)"| EXT_JOR_150_destino
  JOR_830 -->|"La SCBA resuelve o el recurso no se concede, sin cuestión federal"| EXT_JOR_900_destino
  JOR_830 -->|"Hay cuestión federal: recurso extraordinario federal"| JOR_840
  JOR_840 -->|"Recurso federal resuelto, desistido o denegado"| EXT_JOR_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Firmeza, cómputo y derivaciones

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    JOR_900["<b>JOR_900</b> Firmeza de la sentencia<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_910["<b>JOR_910</b> Cómputo de la pena<br/>Responsable: Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano<br/>Sin plazo"]:::tribunal
    JOR_955["<b>JOR_955</b> Sigue en la matriz de juicio abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_960["<b>JOR_960</b> Sigue en la matriz de hábeas corpus<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JOR_970["<b>JOR_970</b> Sigue en ejecución penal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JOR_980["<b>JOR_980</b> Absolución o sobreseimiento firme<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JOR_120_origen["JOR_120 Audiencia preliminar<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_120_origen -.->|"Acuerdo de juicio abreviado"| JOR_955
  EXT_JOR_130_origen["JOR_130 Planteo de nulidades<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_130_origen -.->|"Nulidad o excepción que termina el juicio (sobreseimiento, art. 341)"| JOR_900
  EXT_JOR_150_origen["JOR_150 Fecha del debate fijada<br/>(ver Preparación del juicio)"]:::externo
  EXT_JOR_150_origen -.->|"Acuerdo de juicio abreviado hasta 30 días antes"| JOR_955
  EXT_JOR_240_origen["JOR_240 Resolución del pedido de excarcelación<br/>(ver Situación de libertad en el juicio)"]:::externo
  EXT_JOR_240_origen -.->|"Excarcelación denegada: hábeas corpus"| JOR_960
  EXT_JOR_270_origen["JOR_270 Apelación de la coerción o de la denegatoria de excarcelación<br/>(ver Situación de libertad en el juicio)"]:::externo
  EXT_JOR_270_origen -.->|"Se opta por el hábeas corpus (art. 164)"| JOR_960
  EXT_JOR_290_origen["JOR_290 Control del plazo máximo con detenido (2 años)<br/>(ver Situación de libertad en el juicio)"]:::externo
  EXT_JOR_290_origen -.->|"Vence el plazo: hábeas corpus"| JOR_960
  EXT_JOR_600_origen["JOR_600 Decisión de recurrir la sentencia<br/>(ver Recursos)"]:::externo
  EXT_JOR_600_origen -.->|"No se recurre o la sentencia es irrecurrible"| JOR_900
  EXT_JOR_810_origen["JOR_810 Apelación de la sentencia correccional ante la Cámara (20 días)<br/>(ver Recursos)"]:::externo
  EXT_JOR_810_origen -.->|"La Cámara resuelve y no se recurre más"| JOR_900
  EXT_JOR_810_origen -.->|"Apelación denegada: queja resuelta o no interpuesta"| JOR_900
  EXT_JOR_820_origen["JOR_820 Recurso de casación ante el Tribunal de Casación Penal (20 días)<br/>(ver Recursos)"]:::externo
  EXT_JOR_820_origen -.->|"Casación resuelta y no se recurre más"| JOR_900
  EXT_JOR_820_origen -.->|"Casación denegada o no manifestada en 7 días: queja resuelta o no interpuesta"| JOR_900
  EXT_JOR_830_origen["JOR_830 Recursos extraordinarios ante la SCBA (10 días hábiles)<br/>(ver Recursos)"]:::externo
  EXT_JOR_830_origen -.->|"La SCBA resuelve o el recurso no se concede, sin cuestión federal"| JOR_900
  EXT_JOR_840_origen["JOR_840 Recurso extraordinario federal<br/>(ver Recursos)"]:::externo
  EXT_JOR_840_origen -.->|"Recurso federal resuelto, desistido o denegado"| JOR_900
  JOR_900 -->|"Absolución o sobreseimiento firme"| JOR_980
  JOR_900 -->|"Condena firme: cómputo"| JOR_910
  JOR_910 -->|"Cómputo practicado"| JOR_970
  style JOR_955 stroke-width:3px
  style JOR_960 stroke-width:3px
  style JOR_970 stroke-width:3px
  style JOR_980 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
