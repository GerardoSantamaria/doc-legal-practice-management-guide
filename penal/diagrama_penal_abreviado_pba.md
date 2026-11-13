# Diagrama de Flujo: Juicio abreviado (PBA)

**Régimen:** CPP PBA (Ley 11.922 y modificatorias); arts. 395 a 403 CPP PBA; Ley 13.811 (flagrancia, a verificar); Código Penal (suspensión del juicio a prueba, arts. 76 bis y 76 ter) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_penal_abreviado_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima (ACTORA); naranja = imputado y defensa (DEMANDADA); gris = juez o tribunal de juicio, Cámara o Casación (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, tras la sentencia del abreviado corren a la vez el recurso (casación o apelación), la impugnación de honorarios y el control de firmeza hacia ejecución.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo penal, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la intervención judicial formal (consulta, denuncia, designación de defensor, constitución como particular damnificado). La app los separa en el flujo prejudicial; en penal hay duda sobre si eso tiene sentido desde la denuncia.
* **Plazos corridos (art. 139 CPP PBA):** la mayoría de los plazos procesales penales son días continuos (CORRIDOS), no hábiles judiciales. Aplica_Gracia = NO en todos los hitos.
* **Tope de pena (art. 395):** la pena pedida por el fiscal no puede superar 15 años de prisión (o una pena no privativa de libertad, aún conjunta). Es pena concreta pedida, no máximo abstracto.
* **Rechazo del acuerdo (art. 398):** si se desestima, el proceso sigue en juicio oral; las conformidades no valen como reconocimiento de culpabilidad. Resolución inimpugnable.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Oportunidad<br/>2 hitos"]
  FASE_2["Acuerdo<br/>5 hitos"]
  FASE_3["Audiencia<br/>1 hito"]
  FASE_4["Resolución<br/>1 hito"]
  FASE_5["Sentencia<br/>1 hito"]
  FASE_6["Flagrancia y probation<br/>2 hitos"]
  FASE_7["Recursos<br/>5 hitos"]
  FASE_8["Cierre<br/>6 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_6
  FASE_1 --> FASE_8
  FASE_2 --> FASE_8
  FASE_2 --> FASE_3
  FASE_3 --> FASE_4
  FASE_4 --> FASE_5
  FASE_4 --> FASE_8
  FASE_5 --> FASE_7
  FASE_5 --> FASE_8
  FASE_6 --> FASE_2
  FASE_6 --> FASE_8
  FASE_6 --> FASE_1
  FASE_7 --> FASE_8
```

## 1. Oportunidad del abreviado

```mermaid
flowchart TD
  subgraph F_0["Oportunidad"]
    JAB_010["INICIO - <b>JAB_010</b> Evaluación de oportunidad del juicio abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_020["<b>JAB_020</b> Control de oportunidad: hasta 30 días antes del debate<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  JAB_010 -->|"Hay fecha de debate: controlar los 30 días"| JAB_020
  EXT_JAB_100_destino["JAB_100 Propuesta de acuerdo (fiscal, imputado o defensa)<br/>(ver Acuerdo y víctimas)"]:::externo
  JAB_010 -->|"Impulsar el acuerdo (IPP, elevación o juicio)"| EXT_JAB_100_destino
  EXT_JAB_400_destino["JAB_400 Abreviado en flagrancia o pedido temprano<br/>(ver Flagrancia y relación con probation)"]:::externo
  JAB_010 -->|"Pedido temprano en flagrancia"| EXT_JAB_400_destino
  EXT_JAB_410_destino["JAB_410 Relación con suspensión del juicio a prueba<br/>(ver Flagrancia y relación con probation)"]:::externo
  JAB_010 -->|"Evaluar probation como alternativa"| EXT_JAB_410_destino
  JAB_020 -->|"Dentro del plazo: negociar el acuerdo"| EXT_JAB_100_destino
  EXT_JAB_320_destino["JAB_320 Sigue en la matriz de juicio oral<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_020 -->|"Plazo vencido: sigue el juicio oral"| EXT_JAB_320_destino
  EXT_JAB_410_origen["JAB_410 Relación con suspensión del juicio a prueba<br/>(ver Flagrancia y relación con probation)"]:::externo
  EXT_JAB_410_origen -.->|"Probation no viable: volver a evaluar la oportunidad"| JAB_010
  style JAB_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Acuerdo y víctimas

```mermaid
flowchart TD
  subgraph F_0["Acuerdo"]
    JAB_100["<b>JAB_100</b> Propuesta de acuerdo (fiscal, imputado o defensa)<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_110["<b>JAB_110</b> Conformidad de hecho, calificación y pena (tope ≤ 15 años)<br/>Responsable: Imputado / defensa<br/>Sin plazo"]:::demandada
    JAB_120["<b>JAB_120</b> Notificación al particular damnificado y convocatoria a la víctima<br/>Responsable: Fiscal / particular damnificado / víctima<br/>Sin plazo"]:::actora
    JAB_130["<b>JAB_130</b> Presentación del acuerdo ante el órgano judicial<br/>Responsable: Fiscal / particular damnificado / víctima<br/>Sin plazo"]:::actora
    JAB_500["<b>JAB_500</b> Acción civil en el juicio abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JAB_010_origen["JAB_010 Evaluación de oportunidad del juicio abreviado<br/>(ver Oportunidad del abreviado)"]:::externo
  EXT_JAB_010_origen -.->|"Impulsar el acuerdo (IPP, elevación o juicio)"| JAB_100
  EXT_JAB_020_origen["JAB_020 Control de oportunidad: hasta 30 días antes del debate<br/>(ver Oportunidad del abreviado)"]:::externo
  EXT_JAB_020_origen -.->|"Dentro del plazo: negociar el acuerdo"| JAB_100
  JAB_100 -->|"Propuesta de pena y calificación"| JAB_110
  P_JAB_100_2(["Se abren en paralelo"]):::paralelo
  JAB_100 -->|"Propuesta de pena y calificación, con pretensión civil"| P_JAB_100_2
  P_JAB_100_2 --> JAB_110
  P_JAB_100_2 --> JAB_500
  JAB_110 -->|"Conformidad prestada: notificar a la víctima y al particular damnificado"| JAB_120
  EXT_JAB_330_destino["JAB_330 Sigue en la matriz de investigación<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_110 -->|"Sin conformidad, causa en la IPP: sigue la investigación"| EXT_JAB_330_destino
  EXT_JAB_320_destino["JAB_320 Sigue en la matriz de juicio oral<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_110 -->|"Sin conformidad, causa en juicio: sigue el juicio oral"| EXT_JAB_320_destino
  JAB_120 -->|"Notificaciones cumplidas: presentar el acuerdo"| JAB_130
  EXT_JAB_200_destino["JAB_200 Audiencia de conocimiento personal del imputado<br/>(ver Audiencia de conocimiento personal)"]:::externo
  JAB_130 -->|"Acuerdo presentado: audiencia de conocimiento personal"| EXT_JAB_200_destino
  EXT_JAB_400_origen["JAB_400 Abreviado en flagrancia o pedido temprano<br/>(ver Flagrancia y relación con probation)"]:::externo
  EXT_JAB_400_origen -.->|"Acuerdo en flagrancia: conformidad"| JAB_110
  EXT_JAB_410_origen["JAB_410 Relación con suspensión del juicio a prueba<br/>(ver Flagrancia y relación con probation)"]:::externo
  EXT_JAB_410_origen -.->|"Se elige el abreviado"| JAB_100
  FIN_JAB_500_1(["Fin de este camino"]):::fin
  JAB_500 -->|"Acción civil acordada, remitida a sede civil o desistida"| FIN_JAB_500_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Audiencia de conocimiento personal

```mermaid
flowchart TD
  subgraph F_0["Audiencia"]
    JAB_200["<b>JAB_200</b> Audiencia de conocimiento personal del imputado<br/>Responsable: Juez o tribunal de juicio / Casación / Cámara<br/>Fecha y hora fijadas por el tribunal"]:::tribunal
  end
  EXT_JAB_130_origen["JAB_130 Presentación del acuerdo ante el órgano judicial<br/>(ver Acuerdo y víctimas)"]:::externo
  EXT_JAB_130_origen -.->|"Acuerdo presentado: audiencia de conocimiento personal"| JAB_200
  EXT_JAB_300_destino["JAB_300 Resolución de admisión o rechazo del acuerdo<br/>(ver Admisión, rechazo y sentencia)"]:::externo
  JAB_200 -->|"Audiencia cumplida: resolver"| EXT_JAB_300_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Admisión, rechazo y sentencia

```mermaid
flowchart TD
  subgraph F_0["Resolución"]
    JAB_300["<b>JAB_300</b> Resolución de admisión o rechazo del acuerdo<br/>Responsable: Juez o tribunal de juicio / Casación / Cámara<br/>Sin plazo"]:::tribunal
  end
  subgraph F_1["Sentencia"]
    JAB_310["<b>JAB_310</b> Sentencia de juicio abreviado<br/>Responsable: Juez o tribunal de juicio / Casación / Cámara<br/>5 días corridos"]:::tribunal
  end
  EXT_JAB_200_origen["JAB_200 Audiencia de conocimiento personal del imputado<br/>(ver Audiencia de conocimiento personal)"]:::externo
  EXT_JAB_200_origen -.->|"Audiencia cumplida: resolver"| JAB_300
  JAB_300 -->|"Admisión del acuerdo: sentencia"| JAB_310
  EXT_JAB_330_destino["JAB_330 Sigue en la matriz de investigación<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_300 -->|"Desestimación con la causa en la IPP: sigue la investigación"| EXT_JAB_330_destino
  EXT_JAB_320_destino["JAB_320 Sigue en la matriz de juicio oral<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_300 -->|"Desestimación con la causa en juicio: sigue el juicio oral"| EXT_JAB_320_destino
  P_JAB_310_1(["Se abren en paralelo"]):::paralelo
  JAB_310 -->|"Sentencia notificada"| P_JAB_310_1
  EXT_JAB_600_destino["JAB_600 Recurso contra la sentencia del abreviado<br/>(ver Recursos)"]:::externo
  P_JAB_310_1 --> EXT_JAB_600_destino
  EXT_JAB_900_destino["JAB_900 Regulación e impugnación de honorarios<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  P_JAB_310_1 --> EXT_JAB_900_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Flagrancia y relación con probation

```mermaid
flowchart TD
  subgraph F_0["Flagrancia y probation"]
    JAB_400["<b>JAB_400</b> Abreviado en flagrancia o pedido temprano<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_410["<b>JAB_410</b> Relación con suspensión del juicio a prueba<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JAB_010_origen["JAB_010 Evaluación de oportunidad del juicio abreviado<br/>(ver Oportunidad del abreviado)"]:::externo
  EXT_JAB_010_origen -.->|"Pedido temprano en flagrancia"| JAB_400
  EXT_JAB_010_origen -.->|"Evaluar probation como alternativa"| JAB_410
  EXT_JAB_110_destino["JAB_110 Conformidad de hecho, calificación y pena (tope ≤ 15 años)<br/>(ver Acuerdo y víctimas)"]:::externo
  JAB_400 -->|"Acuerdo en flagrancia: conformidad"| EXT_JAB_110_destino
  EXT_JAB_330_destino["JAB_330 Sigue en la matriz de investigación<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_400 -->|"Sin acuerdo temprano: sigue el procedimiento de flagrancia"| EXT_JAB_330_destino
  EXT_JAB_100_destino["JAB_100 Propuesta de acuerdo (fiscal, imputado o defensa)<br/>(ver Acuerdo y víctimas)"]:::externo
  JAB_410 -->|"Se elige el abreviado"| EXT_JAB_100_destino
  JAB_410 -->|"Se elige la probation: sigue en la investigación"| EXT_JAB_330_destino
  EXT_JAB_010_destino["JAB_010 Evaluación de oportunidad del juicio abreviado<br/>(ver Oportunidad del abreviado)"]:::externo
  JAB_410 -->|"Probation no viable: volver a evaluar la oportunidad"| EXT_JAB_010_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Recursos

```mermaid
flowchart TD
  subgraph F_0["Recursos"]
    JAB_600["<b>JAB_600</b> Recurso contra la sentencia del abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_810["<b>JAB_810</b> Apelación de la sentencia correccional ante la Cámara (20 días)<br/>Responsable: Cualquiera de las partes<br/>20 días corridos"]:::ambas
    JAB_820["<b>JAB_820</b> Recurso de casación ante el Tribunal de Casación Penal (20 días)<br/>Responsable: Cualquiera de las partes<br/>20 días corridos"]:::ambas
    JAB_830["<b>JAB_830</b> Recursos extraordinarios ante la SCBA (10 días hábiles)<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
    JAB_840["<b>JAB_840</b> Recurso extraordinario federal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JAB_310_origen["JAB_310 Sentencia de juicio abreviado<br/>(ver Admisión, rechazo y sentencia)"]:::externo
  EXT_JAB_310_origen -.->|"Sentencia notificada"| JAB_600
  JAB_600 -->|"Abreviado en lo criminal: casación"| JAB_820
  JAB_600 -->|"Abreviado en lo correccional: apelación"| JAB_810
  EXT_JAB_700_destino["JAB_700 Firmeza de la sentencia del abreviado<br/>(ver Honorarios, firmeza y cierre)"]:::externo
  JAB_600 -->|"No se recurre"| EXT_JAB_700_destino
  JAB_810 -->|"La Cámara resuelve y no se recurre más"| EXT_JAB_700_destino
  JAB_810 -->|"Apelación denegada: queja resuelta o no interpuesta"| EXT_JAB_700_destino
  JAB_810 -->|"La Cámara resuelve: recursos extraordinarios ante la SCBA"| JAB_830
  JAB_820 -->|"Casación resuelta y no se recurre más"| EXT_JAB_700_destino
  JAB_820 -->|"Casación denegada o no manifestada en 7 días: queja resuelta o no interpuesta"| EXT_JAB_700_destino
  JAB_820 -->|"Casación resuelta: recursos extraordinarios ante la SCBA"| JAB_830
  JAB_830 -->|"La SCBA resuelve o el recurso no se concede, sin cuestión federal"| EXT_JAB_700_destino
  JAB_830 -->|"Hay cuestión federal: recurso extraordinario federal"| JAB_840
  JAB_840 -->|"Recurso federal resuelto, desistido o denegado"| EXT_JAB_700_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Honorarios, firmeza y cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    JAB_320["<b>JAB_320</b> Sigue en la matriz de juicio oral<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_330["<b>JAB_330</b> Sigue en la matriz de investigación<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_700["<b>JAB_700</b> Firmeza de la sentencia del abreviado<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_900["<b>JAB_900</b> Regulación e impugnación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días corridos"]:::ambas
    JAB_970["<b>JAB_970</b> Sigue en ejecución penal<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    JAB_990["<b>JAB_990</b> Archivo o absolución firme<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_JAB_020_origen["JAB_020 Control de oportunidad: hasta 30 días antes del debate<br/>(ver Oportunidad del abreviado)"]:::externo
  EXT_JAB_020_origen -.->|"Plazo vencido: sigue el juicio oral"| JAB_320
  EXT_JAB_110_origen["JAB_110 Conformidad de hecho, calificación y pena (tope ≤ 15 años)<br/>(ver Acuerdo y víctimas)"]:::externo
  EXT_JAB_110_origen -.->|"Sin conformidad, causa en la IPP: sigue la investigación"| JAB_330
  EXT_JAB_110_origen -.->|"Sin conformidad, causa en juicio: sigue el juicio oral"| JAB_320
  EXT_JAB_300_origen["JAB_300 Resolución de admisión o rechazo del acuerdo<br/>(ver Admisión, rechazo y sentencia)"]:::externo
  EXT_JAB_300_origen -.->|"Desestimación con la causa en la IPP: sigue la investigación"| JAB_330
  EXT_JAB_300_origen -.->|"Desestimación con la causa en juicio: sigue el juicio oral"| JAB_320
  EXT_JAB_310_origen["JAB_310 Sentencia de juicio abreviado<br/>(ver Admisión, rechazo y sentencia)"]:::externo
  EXT_JAB_310_origen -.->|"Sentencia notificada"| JAB_900
  EXT_JAB_400_origen["JAB_400 Abreviado en flagrancia o pedido temprano<br/>(ver Flagrancia y relación con probation)"]:::externo
  EXT_JAB_400_origen -.->|"Sin acuerdo temprano: sigue el procedimiento de flagrancia"| JAB_330
  EXT_JAB_410_origen["JAB_410 Relación con suspensión del juicio a prueba<br/>(ver Flagrancia y relación con probation)"]:::externo
  EXT_JAB_410_origen -.->|"Se elige la probation: sigue en la investigación"| JAB_330
  EXT_JAB_600_origen["JAB_600 Recurso contra la sentencia del abreviado<br/>(ver Recursos)"]:::externo
  EXT_JAB_600_origen -.->|"No se recurre"| JAB_700
  JAB_700 -->|"Condena firme con pena o reglas a ejecutar"| JAB_970
  JAB_700 -->|"Absolución firme o cierre sin ejecución"| JAB_990
  EXT_JAB_810_origen["JAB_810 Apelación de la sentencia correccional ante la Cámara (20 días)<br/>(ver Recursos)"]:::externo
  EXT_JAB_810_origen -.->|"La Cámara resuelve y no se recurre más"| JAB_700
  EXT_JAB_810_origen -.->|"Apelación denegada: queja resuelta o no interpuesta"| JAB_700
  EXT_JAB_820_origen["JAB_820 Recurso de casación ante el Tribunal de Casación Penal (20 días)<br/>(ver Recursos)"]:::externo
  EXT_JAB_820_origen -.->|"Casación resuelta y no se recurre más"| JAB_700
  EXT_JAB_820_origen -.->|"Casación denegada o no manifestada en 7 días: queja resuelta o no interpuesta"| JAB_700
  EXT_JAB_830_origen["JAB_830 Recursos extraordinarios ante la SCBA (10 días hábiles)<br/>(ver Recursos)"]:::externo
  EXT_JAB_830_origen -.->|"La SCBA resuelve o el recurso no se concede, sin cuestión federal"| JAB_700
  EXT_JAB_840_origen["JAB_840 Recurso extraordinario federal<br/>(ver Recursos)"]:::externo
  EXT_JAB_840_origen -.->|"Recurso federal resuelto, desistido o denegado"| JAB_700
  FIN_JAB_900_1(["Fin de este camino"]):::fin
  JAB_900 -->|"Honorarios firmes, impugnación resuelta o sin regulación"| FIN_JAB_900_1
  style JAB_320 stroke-width:3px
  style JAB_330 stroke-width:3px
  style JAB_970 stroke-width:3px
  style JAB_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
