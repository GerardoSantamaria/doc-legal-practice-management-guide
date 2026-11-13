# Diagrama de Flujo: Violencia familiar: medidas de protección (PBA)

**Régimen:** Ley 12.569 de violencia familiar (texto de las Leyes 14.509 y 14.657); art. 827 inc. u CPCCBA; art. 16 de la Ley 26.485 (garantías mínimas de procedimiento, según el art. 6 ter de la Ley 12.569) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_familia_violencia_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = la persona que padece la violencia o quien denuncia (ACTORA); naranja = la persona denunciada (DEMANDADA); gris = juzgado, comisaría, equipo interdisciplinario, Registro Nacional de Armas, Asesoría de Incapaces o Servicio Local, aclarado en el nombre (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, al dictarse las medidas corren a la vez la notificación a la persona denunciada, las comunicaciones, las 48 horas para tomar las audiencias y el vencimiento de las medidas.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.
* **Fase "Previa":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un registro). La app los separa en el flujo prejudicial.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>4 hitos"]
  FASE_2["Medidas urgentes<br/>6 hitos"]
  FASE_3["Audiencias<br/>5 hitos"]
  FASE_4["Vigencia y control<br/>6 hitos"]
  FASE_5["Recursos<br/>3 hitos"]
  FASE_6["Cierre<br/>5 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_6
  FASE_2 --> FASE_3
  FASE_2 --> FASE_5
  FASE_2 --> FASE_4
  FASE_3 --> FASE_4
  FASE_3 --> FASE_5
  FASE_3 --> FASE_6
  FASE_4 --> FASE_6
  FASE_4 --> FASE_5
  FASE_4 --> FASE_3
```

## 1. Etapa previa (antes de promover)

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    VIO_010["INICIO - <b>VIO_010</b> Situación de violencia en el ámbito familiar<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_020["<b>VIO_020</b> Evaluación del riesgo y plan de seguridad<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_030["<b>VIO_030</b> Denuncia<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_040["<b>VIO_040</b> Remisión de la denuncia al juzgado<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  VIO_010 -->|"Se evalúa el riesgo y se arma un plan de seguridad antes de denunciar"| VIO_020
  VIO_010 -->|"Se denuncia de inmediato"| VIO_030
  EXT_VIO_070_destino["VIO_070 Notificación de las medidas a la persona denunciada<br/>(ver Medidas urgentes de protección)"]:::externo
  VIO_010 -->|"Se representa a la persona denunciada"| EXT_VIO_070_destino
  VIO_020 -->|"Decide denunciar"| VIO_030
  EXT_VIO_990_destino["VIO_990 Archivo del expediente<br/>(ver Cese y cierre)"]:::externo
  VIO_020 -->|"Decide no denunciar por ahora"| EXT_VIO_990_destino
  VIO_030 -->|"Denuncia ante la comisaría, la fiscalía u otro organismo"| VIO_040
  EXT_VIO_050_destino["VIO_050 Plazo del juez para resolver las medidas urgentes<br/>(ver Medidas urgentes de protección)"]:::externo
  VIO_030 -->|"Denuncia ante el Juzgado de Familia o de Paz"| EXT_VIO_050_destino
  VIO_040 -->|"Denuncia recibida por el juzgado"| EXT_VIO_050_destino
  style VIO_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Medidas urgentes de protección

```mermaid
flowchart TD
  subgraph F_0["Medidas urgentes"]
    VIO_050["<b>VIO_050</b> Plazo del juez para resolver las medidas urgentes<br/>Responsable: Juzgado u organismo<br/>48 horas"]:::tribunal
    VIO_060["<b>VIO_060</b> Medidas de protección dictadas<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_070["<b>VIO_070</b> Notificación de las medidas a la persona denunciada<br/>Responsable: Persona denunciada<br/>Sin plazo"]:::demandada
    VIO_080["<b>VIO_080</b> Dispositivo de protección o custodia en el domicilio<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_090["<b>VIO_090</b> Comunicación de las medidas y oficio al Registro Nacional de Armas<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_240["<b>VIO_240</b> Intervención de la Asesoría de Incapaces y del Servicio Local (víctima menor de edad)<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_VIO_010_origen["VIO_010 Situación de violencia en el ámbito familiar<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_VIO_010_origen -.->|"Se representa a la persona denunciada"| VIO_070
  EXT_VIO_030_origen["VIO_030 Denuncia<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_VIO_030_origen -.->|"Denuncia ante el Juzgado de Familia o de Paz"| VIO_050
  EXT_VIO_040_origen["VIO_040 Remisión de la denuncia al juzgado<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_VIO_040_origen -.->|"Denuncia recibida por el juzgado"| VIO_050
  VIO_050 -->|"Medidas dictadas"| VIO_060
  P_VIO_050_2(["Se abren en paralelo"]):::paralelo
  VIO_050 -->|"Medidas dictadas y hay niños, niñas o adolescentes afectados"| P_VIO_050_2
  P_VIO_050_2 --> VIO_060
  P_VIO_050_2 --> VIO_240
  P_VIO_050_3(["Se abren en paralelo"]):::paralelo
  VIO_050 -->|"No se dicta ninguna medida"| P_VIO_050_3
  EXT_VIO_100_destino["VIO_100 Plazo para tomar las audiencias (48 horas)<br/>(ver Audiencias e informe de riesgo)"]:::externo
  P_VIO_050_3 --> EXT_VIO_100_destino
  EXT_VIO_200_destino["VIO_200 Apelación de la resolución sobre las medidas o las sanciones<br/>(ver Apelación)"]:::externo
  P_VIO_050_3 --> EXT_VIO_200_destino
  P_VIO_060_1(["Se abren en paralelo"]):::paralelo
  VIO_060 -->|"Medidas dictadas con su fecha de vencimiento"| P_VIO_060_1
  P_VIO_060_1 --> VIO_070
  P_VIO_060_1 --> VIO_090
  P_VIO_060_1 --> EXT_VIO_100_destino
  EXT_VIO_150_destino["VIO_150 Vencimiento de las medidas<br/>(ver Vigencia, control e incumplimiento)"]:::externo
  P_VIO_060_1 --> EXT_VIO_150_destino
  P_VIO_060_2(["Se abren en paralelo"]):::paralelo
  VIO_060 -->|"Medidas con dispositivo de protección o custodia en el domicilio"| P_VIO_060_2
  P_VIO_060_2 --> VIO_070
  P_VIO_060_2 --> VIO_080
  P_VIO_060_2 --> VIO_090
  P_VIO_060_2 --> EXT_VIO_100_destino
  P_VIO_060_2 --> EXT_VIO_150_destino
  VIO_070 -->|"Medidas notificadas: corre el plazo para apelar"| EXT_VIO_200_destino
  FIN_VIO_080_1(["Fin de este camino"]):::fin
  VIO_080 -->|"Dispositivo entregado, o retirado al cesar las medidas"| FIN_VIO_080_1
  FIN_VIO_090_1(["Fin de este camino"]):::fin
  VIO_090 -->|"Comunicaciones libradas e informe de armas recibido"| FIN_VIO_090_1
  FIN_VIO_240_1(["Fin de este camino"]):::fin
  VIO_240 -->|"Intervención dispuesta"| FIN_VIO_240_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Audiencias e informe de riesgo

```mermaid
flowchart TD
  subgraph F_0["Audiencias"]
    VIO_100["<b>VIO_100</b> Plazo para tomar las audiencias (48 horas)<br/>Responsable: Juzgado u organismo<br/>48 horas"]:::tribunal
    VIO_110["<b>VIO_110</b> Audiencia de la persona denunciante<br/>Responsable: Persona denunciante<br/>Fecha y hora fijadas por el tribunal"]:::actora
    VIO_120["<b>VIO_120</b> Audiencia de la persona denunciada<br/>Responsable: Persona denunciada<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    VIO_130["<b>VIO_130</b> Informe interdisciplinario de riesgo<br/>Responsable: Juzgado u organismo<br/>48 horas"]:::tribunal
    VIO_140["<b>VIO_140</b> Ratificación, modificación o ampliación de las medidas<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_VIO_050_origen["VIO_050 Plazo del juez para resolver las medidas urgentes<br/>(ver Medidas urgentes de protección)"]:::externo
  EXT_VIO_050_origen -.->|"No se dicta ninguna medida"| VIO_100
  EXT_VIO_060_origen["VIO_060 Medidas de protección dictadas<br/>(ver Medidas urgentes de protección)"]:::externo
  EXT_VIO_060_origen -.->|"Medidas dictadas con su fecha de vencimiento"| VIO_100
  EXT_VIO_060_origen -.->|"Medidas con dispositivo de protección o custodia en el domicilio"| VIO_100
  P_VIO_100_1(["Se abren en paralelo"]):::paralelo
  VIO_100 -->|"Audiencias fijadas en días y horas distintos"| P_VIO_100_1
  P_VIO_100_1 --> VIO_110
  P_VIO_100_1 --> VIO_120
  P_VIO_100_1 --> VIO_130
  FIN_VIO_110_1(["Fin de este camino"]):::fin
  VIO_110 -->|"Audiencia tomada, o la persona denunciante no comparece"| FIN_VIO_110_1
  VIO_120 -->|"Audiencia tomada: el juez resuelve sobre las medidas"| VIO_140
  VIO_120 -->|"No comparece: se lo cita con auxilio de la fuerza pública"| VIO_120
  FIN_VIO_130_1(["Fin de este camino"]):::fin
  VIO_130 -->|"Informe recibido"| FIN_VIO_130_1
  P_VIO_140_1(["Se abren en paralelo"]):::paralelo
  VIO_140 -->|"Medidas ratificadas, modificadas o ampliadas"| P_VIO_140_1
  EXT_VIO_160_destino["VIO_160 Control de eficacia de las medidas<br/>(ver Vigencia, control e incumplimiento)"]:::externo
  P_VIO_140_1 --> EXT_VIO_160_destino
  EXT_VIO_200_destino["VIO_200 Apelación de la resolución sobre las medidas o las sanciones<br/>(ver Apelación)"]:::externo
  P_VIO_140_1 --> EXT_VIO_200_destino
  P_VIO_140_2(["Se abren en paralelo"]):::paralelo
  VIO_140 -->|"Medidas ratificadas, y hay que fijar los alimentos en forma definitiva"| P_VIO_140_2
  P_VIO_140_2 --> EXT_VIO_160_destino
  P_VIO_140_2 --> EXT_VIO_200_destino
  EXT_VIO_970_destino["VIO_970 Sigue en la matriz de alimentos y compensación económica<br/>(ver Cese y cierre)"]:::externo
  P_VIO_140_2 --> EXT_VIO_970_destino
  P_VIO_140_3(["Se abren en paralelo"]):::paralelo
  VIO_140 -->|"Medidas ratificadas, y hay que fijar el cuidado de los hijos en forma definitiva"| P_VIO_140_3
  P_VIO_140_3 --> EXT_VIO_160_destino
  P_VIO_140_3 --> EXT_VIO_200_destino
  EXT_VIO_980_destino["VIO_980 Sigue en la matriz de cuidado personal y régimen de comunicación<br/>(ver Cese y cierre)"]:::externo
  P_VIO_140_3 --> EXT_VIO_980_destino
  P_VIO_140_4(["Se abren en paralelo"]):::paralelo
  VIO_140 -->|"No hay riesgo: el juez dispone el cese"| P_VIO_140_4
  P_VIO_140_4 --> EXT_VIO_200_destino
  EXT_VIO_300_destino["VIO_300 Cese de las medidas<br/>(ver Cese y cierre)"]:::externo
  P_VIO_140_4 --> EXT_VIO_300_destino
  EXT_VIO_230_origen["VIO_230 Pedido de modificación o cese de las medidas<br/>(ver Vigencia, control e incumplimiento)"]:::externo
  EXT_VIO_230_origen -.->|"El juez resuelve el pedido"| VIO_140
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Vigencia, control e incumplimiento

```mermaid
flowchart TD
  subgraph F_0["Vigencia y control"]
    VIO_150["<b>VIO_150</b> Vencimiento de las medidas<br/>Responsable: Persona denunciante<br/>Fecha y hora fijadas por el tribunal"]:::actora
    VIO_160["<b>VIO_160</b> Control de eficacia de las medidas<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_170["<b>VIO_170</b> Incumplimiento de las medidas<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_180["<b>VIO_180</b> Resolución ante el incumplimiento: medidas nuevas o sanciones<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_190["<b>VIO_190</b> Comunicación al juez penal<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_230["<b>VIO_230</b> Pedido de modificación o cese de las medidas<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_VIO_060_origen["VIO_060 Medidas de protección dictadas<br/>(ver Medidas urgentes de protección)"]:::externo
  EXT_VIO_060_origen -.->|"Medidas dictadas con su fecha de vencimiento"| VIO_150
  EXT_VIO_060_origen -.->|"Medidas con dispositivo de protección o custodia en el domicilio"| VIO_150
  EXT_VIO_140_origen["VIO_140 Ratificación, modificación o ampliación de las medidas<br/>(ver Audiencias e informe de riesgo)"]:::externo
  EXT_VIO_140_origen -.->|"Medidas ratificadas, modificadas o ampliadas"| VIO_160
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar los alimentos en forma definitiva"| VIO_160
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar el cuidado de los hijos en forma definitiva"| VIO_160
  VIO_150 -->|"Persiste el riesgo: se prorrogan las medidas con una nueva fecha"| VIO_150
  FIN_VIO_150_2(["Fin de este camino"]):::fin
  VIO_150 -->|"Vencen sin prórroga"| FIN_VIO_150_2
  VIO_160 -->|"Incumplimiento de las medidas"| VIO_170
  VIO_160 -->|"Se pide modificar o hacer cesar las medidas"| VIO_230
  EXT_VIO_300_destino["VIO_300 Cese de las medidas<br/>(ver Cese y cierre)"]:::externo
  VIO_160 -->|"Se constata que cesó el riesgo"| EXT_VIO_300_destino
  VIO_170 -->|"Incumplimiento informado al juzgado"| VIO_180
  P_VIO_180_1(["Se abren en paralelo"]):::paralelo
  VIO_180 -->|"Medidas ampliadas o sanción impuesta: sigue el control"| P_VIO_180_1
  P_VIO_180_1 --> VIO_160
  EXT_VIO_200_destino["VIO_200 Apelación de la resolución sobre las medidas o las sanciones<br/>(ver Apelación)"]:::externo
  P_VIO_180_1 --> EXT_VIO_200_destino
  P_VIO_180_2(["Se abren en paralelo"]):::paralelo
  VIO_180 -->|"El incumplimiento es desobediencia u otro delito"| P_VIO_180_2
  P_VIO_180_2 --> VIO_160
  P_VIO_180_2 --> VIO_190
  P_VIO_180_2 --> EXT_VIO_200_destino
  FIN_VIO_190_1(["Fin de este camino"]):::fin
  VIO_190 -->|"Antecedentes remitidos: la causa penal sigue fuera de esta matriz"| FIN_VIO_190_1
  EXT_VIO_140_destino["VIO_140 Ratificación, modificación o ampliación de las medidas<br/>(ver Audiencias e informe de riesgo)"]:::externo
  VIO_230 -->|"El juez resuelve el pedido"| EXT_VIO_140_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Apelación

```mermaid
flowchart TD
  subgraph F_0["Recursos"]
    VIO_200["<b>VIO_200</b> Apelación de la resolución sobre las medidas o las sanciones<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    VIO_210["<b>VIO_210</b> Fundamentación de la apelación (memorial)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    VIO_220["<b>VIO_220</b> Resolución de la Cámara<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
  end
  EXT_VIO_050_origen["VIO_050 Plazo del juez para resolver las medidas urgentes<br/>(ver Medidas urgentes de protección)"]:::externo
  EXT_VIO_050_origen -.->|"No se dicta ninguna medida"| VIO_200
  EXT_VIO_070_origen["VIO_070 Notificación de las medidas a la persona denunciada<br/>(ver Medidas urgentes de protección)"]:::externo
  EXT_VIO_070_origen -.->|"Medidas notificadas: corre el plazo para apelar"| VIO_200
  EXT_VIO_140_origen["VIO_140 Ratificación, modificación o ampliación de las medidas<br/>(ver Audiencias e informe de riesgo)"]:::externo
  EXT_VIO_140_origen -.->|"Medidas ratificadas, modificadas o ampliadas"| VIO_200
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar los alimentos en forma definitiva"| VIO_200
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar el cuidado de los hijos en forma definitiva"| VIO_200
  EXT_VIO_140_origen -.->|"No hay riesgo: el juez dispone el cese"| VIO_200
  EXT_VIO_180_origen["VIO_180 Resolución ante el incumplimiento: medidas nuevas o sanciones<br/>(ver Vigencia, control e incumplimiento)"]:::externo
  EXT_VIO_180_origen -.->|"Medidas ampliadas o sanción impuesta: sigue el control"| VIO_200
  EXT_VIO_180_origen -.->|"El incumplimiento es desobediencia u otro delito"| VIO_200
  FIN_VIO_200_1(["Fin de este camino"]):::fin
  VIO_200 -->|"No se apela"| FIN_VIO_200_1
  VIO_200 -->|"Apelación concedida en relación"| VIO_210
  VIO_210 -->|"Memorial presentado"| VIO_220
  FIN_VIO_210_2(["Fin de este camino"]):::fin
  VIO_210 -->|"No se funda: recurso desierto"| FIN_VIO_210_2
  FIN_VIO_220_1(["Fin de este camino"]):::fin
  VIO_220 -->|"Resolución de la Cámara notificada"| FIN_VIO_220_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Cese y cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    VIO_300["<b>VIO_300</b> Cese de las medidas<br/>Responsable: Juzgado u organismo<br/>Sin plazo"]:::tribunal
    VIO_310["<b>VIO_310</b> Regulación y apelación de honorarios<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    VIO_970["<b>VIO_970</b> Sigue en la matriz de alimentos y compensación económica<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_980["<b>VIO_980</b> Sigue en la matriz de cuidado personal y régimen de comunicación<br/>Responsable: Persona denunciante<br/>Sin plazo"]:::actora
    VIO_990["<b>VIO_990</b> Archivo del expediente<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_VIO_020_origen["VIO_020 Evaluación del riesgo y plan de seguridad<br/>(ver Etapa previa (antes de promover))"]:::externo
  EXT_VIO_020_origen -.->|"Decide no denunciar por ahora"| VIO_990
  EXT_VIO_140_origen["VIO_140 Ratificación, modificación o ampliación de las medidas<br/>(ver Audiencias e informe de riesgo)"]:::externo
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar los alimentos en forma definitiva"| VIO_970
  EXT_VIO_140_origen -.->|"Medidas ratificadas, y hay que fijar el cuidado de los hijos en forma definitiva"| VIO_980
  EXT_VIO_140_origen -.->|"No hay riesgo: el juez dispone el cese"| VIO_300
  EXT_VIO_160_origen["VIO_160 Control de eficacia de las medidas<br/>(ver Vigencia, control e incumplimiento)"]:::externo
  EXT_VIO_160_origen -.->|"Se constata que cesó el riesgo"| VIO_300
  VIO_300 -->|"Se regulan los honorarios"| VIO_310
  VIO_310 -->|"Honorarios firmes o apelación resuelta"| VIO_990
  style VIO_970 stroke-width:3px
  style VIO_980 stroke-width:3px
  style VIO_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
