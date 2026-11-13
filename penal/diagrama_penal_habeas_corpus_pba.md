# Diagrama de Flujo: Hábeas corpus (PBA)

**Régimen:** CPP PBA (Ley 11.922 y modificatorias); arts. 405 a 420 CPP PBA; art. 20 inc. 1 Constitución de la Provincia de Buenos Aires; art. 43 Constitución Nacional; Ley 23.098 (hábeas corpus federal, solo como referencia); Ley 14.967; jurisprudencia Verbitsky (CSJN, 2005) y SCBA sobre hábeas colectivo (a verificar alcance) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_penal_habeas_corpus_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = quien interpone el hábeas corpus: persona afectada o cualquiera a su favor (ACTORA); naranja = autoridad requerida: policía, servicio penitenciario u otro que restringe la libertad (DEMANDADA); gris = juez o tribunal penal que conoce, Cámara o Casación (TRIBUNAL); violeta = cualquiera de los intervinientes en la audiencia o el recurso (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, tras la radicación corren a la vez el informe de la autoridad (12 horas) y, si hay privación de libertad, la orden de presentar al detenido.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo penal, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la intervención judicial formal (consulta, denuncia, designación de defensor, constitución como particular damnificado). La app los separa en el flujo prejudicial; en penal hay duda sobre si eso tiene sentido desde la denuncia.
* **Plazos corridos (art. 139 CPP PBA):** la mayoría de los plazos procesales penales son días continuos (CORRIDOS), no hábiles judiciales. Aplica_Gracia = NO en todos los hitos.
* **Tipos de hábeas corpus:** reparador (privación actual), preventivo (amenaza inminente), correctivo (agravamiento de condiciones de detención legal) y colectivo (afectación homogénea; Verbitsky, CSJN 2005, y SCBA). El tipo se elige en la evaluación y marca el checklist.
* **Informalidad (arts. 406-407):** puede interponerse por cualquiera, sin formalidades, oralmente, por escrito o por teléfono, a cualquier hora, ante cualquier órgano jurisdiccional. Si se impugna una decisión judicial, hay que exponer agravios bajo sanción de inadmisibilidad.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>1 hito"]
  FASE_2["Interposición<br/>1 hito"]
  FASE_3["Trámite<br/>4 hitos"]
  FASE_4["Audiencia y prueba<br/>2 hitos"]
  FASE_5["Resolución<br/>6 hitos"]
  FASE_6["Recursos<br/>2 hitos"]
  FASE_7["Cierre<br/>4 hitos"]
  FASE_1 --> FASE_2
  FASE_2 --> FASE_3
  FASE_3 --> FASE_4
  FASE_3 --> FASE_5
  FASE_3 --> FASE_7
  FASE_4 --> FASE_5
  FASE_5 --> FASE_6
  FASE_5 --> FASE_7
  FASE_6 --> FASE_7
  FASE_6 --> FASE_5
```

## 1. Evaluación y tipo

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    HCO_010["INICIO - <b>HCO_010</b> Evaluación del tipo de hábeas corpus<br/>Responsable: Quien interpone<br/>Sin plazo"]:::actora
  end
  EXT_HCO_020_destino["HCO_020 Interposición del hábeas corpus<br/>(ver Interposición)"]:::externo
  HCO_010 -->|"Hábeas reparador (privación actual)"| EXT_HCO_020_destino
  HCO_010 -->|"Hábeas preventivo (amenaza inminente)"| EXT_HCO_020_destino
  HCO_010 -->|"Hábeas correctivo (condiciones de detención)"| EXT_HCO_020_destino
  HCO_010 -->|"Hábeas colectivo (afectación homogénea; Verbitsky)"| EXT_HCO_020_destino
  HCO_010 -->|"Deriva de IPP: detención, PP o denegatoria de excarcelación"| EXT_HCO_020_destino
  style HCO_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Interposición

```mermaid
flowchart TD
  subgraph F_0["Interposición"]
    HCO_020["<b>HCO_020</b> Interposición del hábeas corpus<br/>Responsable: Quien interpone<br/>Sin plazo"]:::actora
  end
  EXT_HCO_010_origen["HCO_010 Evaluación del tipo de hábeas corpus<br/>(ver Evaluación y tipo)"]:::externo
  EXT_HCO_010_origen -.->|"Hábeas reparador (privación actual)"| HCO_020
  EXT_HCO_010_origen -.->|"Hábeas preventivo (amenaza inminente)"| HCO_020
  EXT_HCO_010_origen -.->|"Hábeas correctivo (condiciones de detención)"| HCO_020
  EXT_HCO_010_origen -.->|"Hábeas colectivo (afectación homogénea; Verbitsky)"| HCO_020
  EXT_HCO_010_origen -.->|"Deriva de IPP: detención, PP o denegatoria de excarcelación"| HCO_020
  EXT_HCO_100_destino["HCO_100 Radicación y apertura del trámite<br/>(ver Informe, orden y presentación)"]:::externo
  HCO_020 -->|"Interposición formulada"| EXT_HCO_100_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Informe, orden y presentación

```mermaid
flowchart TD
  subgraph F_0["Trámite"]
    HCO_100["<b>HCO_100</b> Radicación y apertura del trámite<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_110["<b>HCO_110</b> Informe de la autoridad requerida (12 horas)<br/>Responsable: Autoridad requerida<br/>12 horas"]:::demandada
    HCO_120["<b>HCO_120</b> Orden de presentar al detenido<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_130["<b>HCO_130</b> Cumplimiento de la orden y presentación<br/>Responsable: Autoridad requerida<br/>Sin plazo"]:::demandada
  end
  EXT_HCO_020_origen["HCO_020 Interposición del hábeas corpus<br/>(ver Interposición)"]:::externo
  EXT_HCO_020_origen -.->|"Interposición formulada"| HCO_100
  P_HCO_100_1(["Se abren en paralelo"]):::paralelo
  HCO_100 -->|"Privación de libertad actual (reparador, correctivo o colectivo)"| P_HCO_100_1
  P_HCO_100_1 --> HCO_110
  P_HCO_100_1 --> HCO_120
  HCO_100 -->|"Amenaza a la libertad (preventivo)"| HCO_110
  EXT_HCO_200_destino["HCO_200 Audiencia oral (art. 412)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_110 -->|"Informe presentado: se fija audiencia"| EXT_HCO_200_destino
  EXT_HCO_220_destino["HCO_220 Resolución sin audiencia (24 horas)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_110 -->|"Informe presentado: se resuelve sin audiencia"| EXT_HCO_220_destino
  P_HCO_110_3(["Se abren en paralelo"]):::paralelo
  HCO_110 -->|"Vence sin informe: audiencia y responsabilidad de la autoridad"| P_HCO_110_3
  P_HCO_110_3 --> EXT_HCO_200_destino
  EXT_HCO_500_destino["HCO_500 Denuncia por delito o responsabilidad de la autoridad<br/>(ver Cierre y derivaciones)"]:::externo
  P_HCO_110_3 --> EXT_HCO_500_destino
  HCO_120 -->|"Orden librada: controlar presentación"| HCO_130
  FIN_HCO_130_1(["Fin de este camino"]):::fin
  HCO_130 -->|"Detenido presentado y a disposición del órgano"| FIN_HCO_130_1
  HCO_130 -->|"Incumplimiento de la orden"| EXT_HCO_500_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Audiencia, prueba y plazos de resolución

```mermaid
flowchart TD
  subgraph F_0["Audiencia y prueba"]
    HCO_200["<b>HCO_200</b> Audiencia oral (art. 412)<br/>Responsable: Cualquiera de los intervinientes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    HCO_210["<b>HCO_210</b> Continuación de la prueba (máx. 24 horas)<br/>Responsable: Juez o tribunal<br/>24 horas"]:::tribunal
  end
  subgraph F_1["Resolución"]
    HCO_220["<b>HCO_220</b> Resolución sin audiencia (24 horas)<br/>Responsable: Juez o tribunal<br/>24 horas"]:::tribunal
    HCO_230["<b>HCO_230</b> Resolución tras audiencia (48 horas)<br/>Responsable: Juez o tribunal<br/>48 horas"]:::tribunal
    HCO_300["<b>HCO_300</b> Rechazo de la petición<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_310["<b>HCO_310</b> Libertad inmediata (reparador)<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_320["<b>HCO_320</b> Cese de la amenaza (preventivo)<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_330["<b>HCO_330</b> Corrección de condiciones de detención (correctivo)<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_HCO_110_origen["HCO_110 Informe de la autoridad requerida (12 horas)<br/>(ver Informe, orden y presentación)"]:::externo
  EXT_HCO_110_origen -.->|"Informe presentado: se fija audiencia"| HCO_200
  EXT_HCO_110_origen -.->|"Informe presentado: se resuelve sin audiencia"| HCO_220
  EXT_HCO_110_origen -.->|"Vence sin informe: audiencia y responsabilidad de la autoridad"| HCO_200
  HCO_200 -->|"Audiencia celebrada sin prueba diferida"| HCO_230
  HCO_200 -->|"Se difiere prueba (máx. 24 horas)"| HCO_210
  HCO_210 -->|"Prueba incorporada: fin de la audiencia"| HCO_230
  HCO_220 -->|"Rechazo"| HCO_300
  HCO_220 -->|"Se ordena libertad inmediata"| HCO_310
  HCO_220 -->|"Se ordena el cese de la amenaza"| HCO_320
  HCO_220 -->|"Se ordena corrección de condiciones"| HCO_330
  HCO_230 -->|"Rechazo"| HCO_300
  HCO_230 -->|"Se ordena libertad inmediata"| HCO_310
  HCO_230 -->|"Se ordena el cese de la amenaza"| HCO_320
  HCO_230 -->|"Se ordena corrección de condiciones"| HCO_330
  EXT_HCO_400_destino["HCO_400 Impugnación ante Cámara o Casación (art. 417)<br/>(ver Impugnación)"]:::externo
  HCO_300 -->|"Se impugna (art. 417)"| EXT_HCO_400_destino
  EXT_HCO_900_destino["HCO_900 Costas y honorarios del hábeas corpus<br/>(ver Cierre y derivaciones)"]:::externo
  HCO_300 -->|"Rechazo firme"| EXT_HCO_900_destino
  HCO_310 -->|"Se impugna (art. 417)"| EXT_HCO_400_destino
  HCO_310 -->|"Libertad cumplida"| EXT_HCO_900_destino
  P_HCO_310_3(["Se abren en paralelo"]):::paralelo
  HCO_310 -->|"Libertad cumplida, con indicios de delito o falta grave"| P_HCO_310_3
  EXT_HCO_500_destino["HCO_500 Denuncia por delito o responsabilidad de la autoridad<br/>(ver Cierre y derivaciones)"]:::externo
  P_HCO_310_3 --> EXT_HCO_500_destino
  P_HCO_310_3 --> EXT_HCO_900_destino
  HCO_320 -->|"Se impugna (art. 417)"| EXT_HCO_400_destino
  HCO_320 -->|"Cese cumplido"| EXT_HCO_900_destino
  HCO_330 -->|"Se impugna (art. 417)"| EXT_HCO_400_destino
  HCO_330 -->|"Corrección cumplida"| EXT_HCO_900_destino
  P_HCO_330_3(["Se abren en paralelo"]):::paralelo
  HCO_330 -->|"Corrección cumplida, con indicios de delito o falta grave"| P_HCO_330_3
  P_HCO_330_3 --> EXT_HCO_500_destino
  P_HCO_330_3 --> EXT_HCO_900_destino
  EXT_HCO_410_origen["HCO_410 Resolución del recurso<br/>(ver Impugnación)"]:::externo
  EXT_HCO_410_origen -.->|"Revoca y ordena libertad"| HCO_310
  EXT_HCO_410_origen -.->|"Revoca y ordena cese de amenaza"| HCO_320
  EXT_HCO_410_origen -.->|"Revoca y ordena corrección"| HCO_330
  EXT_HCO_410_origen -.->|"Revoca y rechaza el hábeas"| HCO_300
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Impugnación

```mermaid
flowchart TD
  subgraph F_0["Recursos"]
    HCO_400["<b>HCO_400</b> Impugnación ante Cámara o Casación (art. 417)<br/>Responsable: Cualquiera de los intervinientes<br/>Sin plazo"]:::ambas
    HCO_410["<b>HCO_410</b> Resolución del recurso<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
  end
  EXT_HCO_300_origen["HCO_300 Rechazo de la petición<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_300_origen -.->|"Se impugna (art. 417)"| HCO_400
  EXT_HCO_310_origen["HCO_310 Libertad inmediata (reparador)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_310_origen -.->|"Se impugna (art. 417)"| HCO_400
  EXT_HCO_320_origen["HCO_320 Cese de la amenaza (preventivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_320_origen -.->|"Se impugna (art. 417)"| HCO_400
  EXT_HCO_330_origen["HCO_330 Corrección de condiciones de detención (correctivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_330_origen -.->|"Se impugna (art. 417)"| HCO_400
  HCO_400 -->|"Recurso interpuesto"| HCO_410
  EXT_HCO_900_destino["HCO_900 Costas y honorarios del hábeas corpus<br/>(ver Cierre y derivaciones)"]:::externo
  HCO_400 -->|"Se desiste de la impugnación"| EXT_HCO_900_destino
  HCO_410 -->|"Confirma la resolución"| EXT_HCO_900_destino
  EXT_HCO_310_destino["HCO_310 Libertad inmediata (reparador)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_410 -->|"Revoca y ordena libertad"| EXT_HCO_310_destino
  EXT_HCO_320_destino["HCO_320 Cese de la amenaza (preventivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_410 -->|"Revoca y ordena cese de amenaza"| EXT_HCO_320_destino
  EXT_HCO_330_destino["HCO_330 Corrección de condiciones de detención (correctivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_410 -->|"Revoca y ordena corrección"| EXT_HCO_330_destino
  EXT_HCO_300_destino["HCO_300 Rechazo de la petición<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  HCO_410 -->|"Revoca y rechaza el hábeas"| EXT_HCO_300_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Cierre y derivaciones

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    HCO_500["<b>HCO_500</b> Denuncia por delito o responsabilidad de la autoridad<br/>Responsable: Juez o tribunal<br/>Sin plazo"]:::tribunal
    HCO_900["<b>HCO_900</b> Costas y honorarios del hábeas corpus<br/>Responsable: Cualquiera de los intervinientes<br/>5 días corridos"]:::ambas
    HCO_950["<b>HCO_950</b> Sigue en la matriz de investigación<br/>Responsable: Cualquiera de los intervinientes<br/>Sin plazo"]:::ambas
    HCO_990["<b>HCO_990</b> Cierre del hábeas corpus<br/>Responsable: Cualquiera de los intervinientes<br/>Sin plazo"]:::ambas
  end
  EXT_HCO_110_origen["HCO_110 Informe de la autoridad requerida (12 horas)<br/>(ver Informe, orden y presentación)"]:::externo
  EXT_HCO_110_origen -.->|"Vence sin informe: audiencia y responsabilidad de la autoridad"| HCO_500
  EXT_HCO_130_origen["HCO_130 Cumplimiento de la orden y presentación<br/>(ver Informe, orden y presentación)"]:::externo
  EXT_HCO_130_origen -.->|"Incumplimiento de la orden"| HCO_500
  EXT_HCO_300_origen["HCO_300 Rechazo de la petición<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_300_origen -.->|"Rechazo firme"| HCO_900
  EXT_HCO_310_origen["HCO_310 Libertad inmediata (reparador)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_310_origen -.->|"Libertad cumplida"| HCO_900
  EXT_HCO_310_origen -.->|"Libertad cumplida, con indicios de delito o falta grave"| HCO_500
  EXT_HCO_310_origen -.->|"Libertad cumplida, con indicios de delito o falta grave"| HCO_900
  EXT_HCO_320_origen["HCO_320 Cese de la amenaza (preventivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_320_origen -.->|"Cese cumplido"| HCO_900
  EXT_HCO_330_origen["HCO_330 Corrección de condiciones de detención (correctivo)<br/>(ver Audiencia, prueba y plazos de resolución)"]:::externo
  EXT_HCO_330_origen -.->|"Corrección cumplida"| HCO_900
  EXT_HCO_330_origen -.->|"Corrección cumplida, con indicios de delito o falta grave"| HCO_500
  EXT_HCO_330_origen -.->|"Corrección cumplida, con indicios de delito o falta grave"| HCO_900
  EXT_HCO_400_origen["HCO_400 Impugnación ante Cámara o Casación (art. 417)<br/>(ver Impugnación)"]:::externo
  EXT_HCO_400_origen -.->|"Se desiste de la impugnación"| HCO_900
  EXT_HCO_410_origen["HCO_410 Resolución del recurso<br/>(ver Impugnación)"]:::externo
  EXT_HCO_410_origen -.->|"Confirma la resolución"| HCO_900
  FIN_HCO_500_1(["Fin de este camino"]):::fin
  HCO_500 -->|"Copias remitidas a la fiscalía (art. 416)"| FIN_HCO_500_1
  FIN_HCO_500_2(["Fin de este camino"]):::fin
  HCO_500 -->|"Trámite iniciado ante la autoridad competente (art. 420)"| FIN_HCO_500_2
  HCO_900 -->|"Costas y honorarios resueltos o sin regulación"| HCO_990
  HCO_900 -->|"Costas y honorarios resueltos; la causa principal sigue en la IPP"| HCO_950
  style HCO_950 stroke-width:3px
  style HCO_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
