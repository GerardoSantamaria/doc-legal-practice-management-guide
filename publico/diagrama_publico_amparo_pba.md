# Diagrama de Flujo: Amparo (PBA, con variante federal)

**Régimen:** Ley 13.928 (texto Leyes 14.192 y 15.016) con el CPCCBA supletorio (art. 25); variante federal: art. 43 Constitución Nacional, Ley 16.986 y CPCCN; cautelares contra el Estado nacional: Ley 26.854 · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_publico_amparo_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el particular que reclama (ACTORA); naranja = el Estado o el organismo demandado, también cuando resuelve en la vía administrativa (DEMANDADA); gris = juzgado, tribunal u organismo de control que no es parte, como la AAIP o el Tribunal Fiscal de Apelación (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la cautelar otorgada abre a la vez el control de su cumplimiento y, contra el Estado nacional, el de su vigencia.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el caso continúa en otra matriz de Derecho Público, en un expediente vinculado.
* **Provincial o federal:** cuando un flujo tiene las dos variantes, el nombre del hito lo dice ("provincial" o "federal") o nombra la ley que lo rige (por ejemplo, "Ley 13.928" o "Ley 16.986").
* **Vía administrativa:** sus hitos están en un diagrama aparte de los judiciales. La Administración que resuelve aparece en naranja, como parte demandada, y sus plazos son días hábiles administrativos.
* **Competencia según el demandado:** los caminos provincial (hitos AMP_200 a AMP_280) y federal (hitos AMP_400 a AMP_480) comparten fases; el nombre del hito dice cuál es.

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>2 hitos"]
  FASE_2["Vía administrativa<br/>3 hitos"]
  FASE_3["Demanda<br/>6 hitos"]
  FASE_4["Cautelares<br/>8 hitos"]
  FASE_5["Prueba<br/>3 hitos"]
  FASE_6["Sentencia<br/>3 hitos"]
  FASE_7["Recursos<br/>8 hitos"]
  FASE_8["Cumplimiento<br/>2 hitos"]
  FASE_9["Ejecución<br/>3 hitos"]
  FASE_10["Cierre<br/>4 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_3
  FASE_1 --> FASE_10
  FASE_2 --> FASE_10
  FASE_2 --> FASE_3
  FASE_2 --> FASE_4
  FASE_3 --> FASE_10
  FASE_3 --> FASE_4
  FASE_3 --> FASE_7
  FASE_3 --> FASE_5
  FASE_3 --> FASE_6
  FASE_5 --> FASE_6
  FASE_5 --> FASE_10
  FASE_6 --> FASE_7
  FASE_6 --> FASE_8
  FASE_6 --> FASE_10
  FASE_7 --> FASE_8
  FASE_7 --> FASE_10
  FASE_4 --> FASE_8
  FASE_4 --> FASE_10
  FASE_4 --> FASE_3
  FASE_8 --> FASE_10
  FASE_8 --> FASE_9
  FASE_7 --> FASE_6
  FASE_9 --> FASE_10
```

## 1. Etapa previa: encuadre, competencia y amparo colectivo

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    AMP_010["INICIO - <b>AMP_010</b> Encuadre del amparo, del demandado y del juzgado competente<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_060["<b>AMP_060</b> Consulta del registro de amparos y procesos colectivos antes de demandar<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  EXT_AMP_020_destino["AMP_020 Pedido de cobertura o prestación al agente de salud<br/>(ver Reclamo previo: vía administrativa o intimación al agente de salud)"]:::externo
  AMP_010 -->|"Salud: falta de cobertura o de una prestación"| EXT_AMP_020_destino
  EXT_AMP_200_destino["AMP_200 Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  AMP_010 -->|"Acto u omisión de la Provincia, un municipio, un ente provincial o un particular: amparo provincial"| EXT_AMP_200_destino
  EXT_AMP_400_destino["AMP_400 Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  AMP_010 -->|"Acto u omisión del Estado nacional o de un ente nacional: amparo federal"| EXT_AMP_400_destino
  AMP_010 -->|"Derechos de incidencia colectiva"| AMP_060
  EXT_AMP_980_destino["AMP_980 Sigue en la matriz de contencioso administrativo<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_010 -->|"Hay otra vía idónea o la cuestión requiere mayor debate"| EXT_AMP_980_destino
  AMP_060 -->|"No hay otro proceso colectivo con el mismo objeto: amparo colectivo provincial"| EXT_AMP_200_destino
  AMP_060 -->|"No hay otro proceso colectivo con el mismo objeto: amparo colectivo federal"| EXT_AMP_400_destino
  style AMP_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Reclamo previo: vía administrativa o intimación al agente de salud

```mermaid
flowchart TD
  subgraph F_0["Vía administrativa"]
    AMP_020["<b>AMP_020</b> Pedido de cobertura o prestación al agente de salud<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_030["<b>AMP_030</b> Intimación por carta documento al agente de salud<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_040["<b>AMP_040</b> Respuesta, negativa o silencio del agente de salud<br/>Responsable: Estado u organismo<br/>Sin plazo"]:::demandada
  end
  EXT_AMP_010_origen["AMP_010 Encuadre del amparo, del demandado y del juzgado competente<br/>(ver Etapa previa: encuadre, competencia y amparo colectivo)"]:::externo
  EXT_AMP_010_origen -.->|"Salud: falta de cobertura o de una prestación"| AMP_020
  AMP_020 -->|"Pedido presentado"| AMP_040
  AMP_030 -->|"Carta documento entregada"| AMP_040
  EXT_AMP_990_destino["AMP_990 Cierre y archivo del caso<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_040 -->|"Cobertura otorgada"| EXT_AMP_990_destino
  AMP_040 -->|"Silencio o demora: intimar por carta documento"| AMP_030
  EXT_AMP_200_destino["AMP_200 Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  AMP_040 -->|"Negativa o silencio de IOMA, una caja o un hospital provincial o municipal: amparo provincial"| EXT_AMP_200_destino
  EXT_AMP_400_destino["AMP_400 Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  AMP_040 -->|"Negativa o silencio de una obra social nacional, una prepaga o el Estado nacional: amparo federal"| EXT_AMP_400_destino
  EXT_AMP_330_destino["AMP_330 Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  AMP_040 -->|"Riesgo para la vida o la salud: medida autosatisfactiva"| EXT_AMP_330_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986)

```mermaid
flowchart TD
  subgraph F_0["Demanda"]
    AMP_200["<b>AMP_200</b> Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>Responsable: Particular<br/>30 días hábiles judiciales"]:::actora
    AMP_210["<b>AMP_210</b> Admisibilidad del amparo provincial y otra vía idónea<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    AMP_220["<b>AMP_220</b> Contestación de la demanda de amparo (Ley 13.928)<br/>Responsable: Estado u organismo<br/>5 días hábiles judiciales + gracia"]:::demandada
    AMP_400["<b>AMP_400</b> Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles<br/>Responsable: Particular<br/>15 días hábiles judiciales"]:::actora
    AMP_410["<b>AMP_410</b> Admisibilidad del amparo federal y rechazo in limine<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    AMP_420["<b>AMP_420</b> Informe circunstanciado del demandado (Ley 16.986)<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
  end
  EXT_AMP_010_origen["AMP_010 Encuadre del amparo, del demandado y del juzgado competente<br/>(ver Etapa previa: encuadre, competencia y amparo colectivo)"]:::externo
  EXT_AMP_010_origen -.->|"Acto u omisión de la Provincia, un municipio, un ente provincial o un particular: amparo provincial"| AMP_200
  EXT_AMP_010_origen -.->|"Acto u omisión del Estado nacional o de un ente nacional: amparo federal"| AMP_400
  EXT_AMP_040_origen["AMP_040 Respuesta, negativa o silencio del agente de salud<br/>(ver Reclamo previo: vía administrativa o intimación al agente de salud)"]:::externo
  EXT_AMP_040_origen -.->|"Negativa o silencio de IOMA, una caja o un hospital provincial o municipal: amparo provincial"| AMP_200
  EXT_AMP_040_origen -.->|"Negativa o silencio de una obra social nacional, una prepaga o el Estado nacional: amparo federal"| AMP_400
  EXT_AMP_060_origen["AMP_060 Consulta del registro de amparos y procesos colectivos antes de demandar<br/>(ver Etapa previa: encuadre, competencia y amparo colectivo)"]:::externo
  EXT_AMP_060_origen -.->|"No hay otro proceso colectivo con el mismo objeto: amparo colectivo provincial"| AMP_200
  EXT_AMP_060_origen -.->|"No hay otro proceso colectivo con el mismo objeto: amparo colectivo federal"| AMP_400
  EXT_AMP_980_destino["AMP_980 Sigue en la matriz de contencioso administrativo<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_200 -->|"Venció el plazo sin demandar: evaluar otra vía"| EXT_AMP_980_destino
  EXT_AMP_300_destino["AMP_300 Pedido de medida cautelar<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  AMP_200 -->|"Se pide una medida cautelar con la demanda"| EXT_AMP_300_destino
  AMP_200 -->|"Demanda presentada"| AMP_210
  AMP_210 -->|"Demanda admitida: se requiere el informe"| AMP_220
  EXT_AMP_260_destino["AMP_260 Apelación en el amparo provincial (3 días)<br/>(ver Recursos)"]:::externo
  AMP_210 -->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| EXT_AMP_260_destino
  EXT_AMP_230_destino["AMP_230 Audiencia simplificadora (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  AMP_220 -->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| EXT_AMP_230_destino
  EXT_AMP_250_destino["AMP_250 Sentencia de amparo (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  AMP_220 -->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| EXT_AMP_250_destino
  EXT_AMP_330_origen["AMP_330 Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  EXT_AMP_330_origen -.->|"Rechazada: se promueve el amparo"| AMP_200
  AMP_400 -->|"Venció el plazo sin demandar: evaluar otra vía"| EXT_AMP_980_destino
  AMP_400 -->|"Se pide una medida cautelar con la demanda"| EXT_AMP_300_destino
  AMP_400 -->|"Demanda presentada"| AMP_410
  AMP_410 -->|"Demanda admitida: se requiere el informe"| AMP_420
  EXT_AMP_460_destino["AMP_460 Apelación en el amparo federal (48 horas)<br/>(ver Recursos)"]:::externo
  AMP_410 -->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| EXT_AMP_460_destino
  EXT_AMP_430_destino["AMP_430 Audiencia de prueba en el amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  AMP_420 -->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| EXT_AMP_430_destino
  EXT_AMP_450_destino["AMP_450 Sentencia de amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  AMP_420 -->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| EXT_AMP_450_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Medidas cautelares y autosatisfactiva

```mermaid
flowchart TD
  subgraph F_0["Cautelares"]
    AMP_300["<b>AMP_300</b> Pedido de medida cautelar<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_315["<b>AMP_315</b> Informe previo del Estado nacional (Ley 26.854)<br/>Responsable: Estado u organismo<br/>3 días hábiles judiciales"]:::demandada
    AMP_320["<b>AMP_320</b> Resolución de la medida cautelar<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    AMP_325["<b>AMP_325</b> Cumplimiento de la medida cautelar por el demandado<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    AMP_330["<b>AMP_330</b> Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_340["<b>AMP_340</b> Apelación de la resolución cautelar (provincial)<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    AMP_345["<b>AMP_345</b> Apelación de la resolución cautelar (federal)<br/>Responsable: Cualquiera de las partes<br/>48 horas"]:::ambas
    AMP_350["<b>AMP_350</b> Vencimiento de la cautelar contra el Estado nacional<br/>Responsable: Particular<br/>3 meses"]:::actora
  end
  EXT_AMP_040_origen["AMP_040 Respuesta, negativa o silencio del agente de salud<br/>(ver Reclamo previo: vía administrativa o intimación al agente de salud)"]:::externo
  EXT_AMP_040_origen -.->|"Riesgo para la vida o la salud: medida autosatisfactiva"| AMP_330
  EXT_AMP_200_origen["AMP_200 Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_200_origen -.->|"Se pide una medida cautelar con la demanda"| AMP_300
  AMP_300 -->|"Se demanda al Estado nacional y no es un supuesto del art. 2 inc. 2 Ley 26.854"| AMP_315
  AMP_300 -->|"Se resuelve sin informe previo"| AMP_320
  AMP_315 -->|"Informe presentado o vencido el plazo"| AMP_320
  P_AMP_320_1(["Se abren en paralelo"]):::paralelo
  AMP_320 -->|"Cautelar otorgada"| P_AMP_320_1
  P_AMP_320_1 --> AMP_325
  P_AMP_320_1 --> AMP_350
  AMP_320 -->|"Se apela la resolución cautelar (juzgado provincial)"| AMP_340
  AMP_320 -->|"Se apela la resolución cautelar (juzgado federal)"| AMP_345
  FIN_AMP_320_4(["Fin de este camino"]):::fin
  AMP_320 -->|"Cautelar denegada y no se apela"| FIN_AMP_320_4
  FIN_AMP_325_1(["Fin de este camino"]):::fin
  AMP_325 -->|"Medida cumplida"| FIN_AMP_325_1
  EXT_AMP_510_destino["AMP_510 Astreintes e intimación por incumplimiento de la orden judicial<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  AMP_325 -->|"Medida incumplida"| EXT_AMP_510_destino
  EXT_AMP_950_destino["AMP_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_330 -->|"Despachada y cumplida"| EXT_AMP_950_destino
  AMP_330 -->|"Despachada e incumplida"| EXT_AMP_510_destino
  EXT_AMP_200_destino["AMP_200 Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  AMP_330 -->|"Rechazada: se promueve el amparo"| EXT_AMP_200_destino
  FIN_AMP_340_1(["Fin de este camino"]):::fin
  AMP_340 -->|"Apelación resuelta"| FIN_AMP_340_1
  FIN_AMP_345_1(["Fin de este camino"]):::fin
  AMP_345 -->|"Apelación resuelta"| FIN_AMP_345_1
  FIN_AMP_350_1(["Fin de este camino"]):::fin
  AMP_350 -->|"Prórroga pedida y resuelta, o terminó el proceso"| FIN_AMP_350_1
  EXT_AMP_400_origen["AMP_400 Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_400_origen -.->|"Se pide una medida cautelar con la demanda"| AMP_300
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Prueba y sentencia

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    AMP_230["<b>AMP_230</b> Audiencia simplificadora (Ley 13.928)<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
    AMP_240["<b>AMP_240</b> Producción de la prueba (Ley 13.928)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    AMP_430["<b>AMP_430</b> Audiencia de prueba en el amparo federal<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  subgraph F_1["Sentencia"]
    AMP_250["<b>AMP_250</b> Sentencia de amparo (Ley 13.928)<br/>Responsable: Juzgado u organismo de control<br/>5 días hábiles judiciales"]:::tribunal
    AMP_450["<b>AMP_450</b> Sentencia de amparo federal<br/>Responsable: Juzgado u organismo de control<br/>48 horas"]:::tribunal
    AMP_520["<b>AMP_520</b> Sentencia de amparo firme tras los recursos extraordinarios<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
  end
  EXT_AMP_220_origen["AMP_220 Contestación de la demanda de amparo (Ley 13.928)<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_220_origen -.->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| AMP_230
  EXT_AMP_220_origen -.->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| AMP_250
  AMP_230 -->|"Audiencia celebrada: se abre a prueba"| AMP_240
  AMP_230 -->|"Audiencia celebrada sin prueba que producir"| AMP_250
  EXT_AMP_950_destino["AMP_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_230 -->|"La actora no comparece: se la tiene por desistida"| EXT_AMP_950_destino
  AMP_240 -->|"Prueba producida o vencido el plazo"| AMP_250
  EXT_AMP_260_destino["AMP_260 Apelación en el amparo provincial (3 días)<br/>(ver Recursos)"]:::externo
  AMP_250 -->|"Sentencia notificada y se apela"| EXT_AMP_260_destino
  EXT_AMP_500_destino["AMP_500 Cumplimiento de la sentencia de amparo en el plazo fijado<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  AMP_250 -->|"Sentencia favorable notificada y no apelada"| EXT_AMP_500_destino
  AMP_250 -->|"Sentencia de rechazo notificada y no apelada"| EXT_AMP_950_destino
  EXT_AMP_420_origen["AMP_420 Informe circunstanciado del demandado (Ley 16.986)<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_420_origen -.->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| AMP_430
  EXT_AMP_420_origen -.->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| AMP_450
  AMP_430 -->|"Audiencia de prueba realizada"| AMP_450
  EXT_AMP_955_destino["AMP_955 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_430 -->|"La actora no comparece: se la tiene por desistida"| EXT_AMP_955_destino
  EXT_AMP_460_destino["AMP_460 Apelación en el amparo federal (48 horas)<br/>(ver Recursos)"]:::externo
  AMP_450 -->|"Sentencia notificada y se apela"| EXT_AMP_460_destino
  AMP_450 -->|"Sentencia favorable notificada y no apelada"| EXT_AMP_500_destino
  AMP_450 -->|"Sentencia de rechazo notificada y no apelada"| EXT_AMP_955_destino
  AMP_520 -->|"Sentencia favorable firme"| EXT_AMP_500_destino
  AMP_520 -->|"Rechazo firme: proceso provincial"| EXT_AMP_950_destino
  AMP_520 -->|"Rechazo firme: proceso federal"| EXT_AMP_955_destino
  EXT_AMP_600_origen["AMP_600 Recursos extraordinarios ante la SCBA<br/>(ver Recursos)"]:::externo
  EXT_AMP_600_origen -.->|"Resuelto por la SCBA sin cuestión federal, denegado o desistido"| AMP_520
  EXT_AMP_610_origen["AMP_610 Recurso extraordinario federal ante la CSJN<br/>(ver Recursos)"]:::externo
  EXT_AMP_610_origen -.->|"Recurso federal resuelto, denegado (queja incluida) o desistido"| AMP_520
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
    AMP_260["<b>AMP_260</b> Apelación en el amparo provincial (3 días)<br/>Responsable: Cualquiera de las partes<br/>3 días hábiles judiciales + gracia"]:::ambas
    AMP_270["<b>AMP_270</b> Queja por apelación denegada en el amparo provincial (1 día)<br/>Responsable: Cualquiera de las partes<br/>1 días hábiles judiciales + gracia"]:::ambas
    AMP_280["<b>AMP_280</b> Sentencia de la alzada en el amparo provincial<br/>Responsable: Juzgado u organismo de control<br/>3 días hábiles judiciales"]:::tribunal
    AMP_460["<b>AMP_460</b> Apelación en el amparo federal (48 horas)<br/>Responsable: Cualquiera de las partes<br/>48 horas"]:::ambas
    AMP_470["<b>AMP_470</b> Recurso directo por apelación denegada en el amparo federal (24 horas)<br/>Responsable: Cualquiera de las partes<br/>24 horas"]:::ambas
    AMP_480["<b>AMP_480</b> Sentencia de la Cámara Federal en el amparo<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    AMP_600["<b>AMP_600</b> Recursos extraordinarios ante la SCBA<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales + gracia"]:::ambas
    AMP_610["<b>AMP_610</b> Recurso extraordinario federal ante la CSJN<br/>Responsable: Cualquiera de las partes<br/>10 días hábiles judiciales"]:::ambas
  end
  EXT_AMP_210_origen["AMP_210 Admisibilidad del amparo provincial y otra vía idónea<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_210_origen -.->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| AMP_260
  EXT_AMP_250_origen["AMP_250 Sentencia de amparo (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_250_origen -.->|"Sentencia notificada y se apela"| AMP_260
  AMP_260 -->|"Apelación concedida"| AMP_280
  AMP_260 -->|"Apelación denegada"| AMP_270
  AMP_270 -->|"Queja o recurso directo admitido"| AMP_280
  EXT_AMP_500_destino["AMP_500 Cumplimiento de la sentencia de amparo en el plazo fijado<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  AMP_270 -->|"Rechazado o no deducido: queda firme una decisión favorable"| EXT_AMP_500_destino
  EXT_AMP_950_destino["AMP_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_270 -->|"Rechazado o no deducido: queda firme el rechazo"| EXT_AMP_950_destino
  AMP_280 -->|"Sentencia favorable firme"| EXT_AMP_500_destino
  AMP_280 -->|"Rechazo firme"| EXT_AMP_950_destino
  AMP_280 -->|"Se interpone recurso extraordinario"| AMP_600
  EXT_AMP_410_origen["AMP_410 Admisibilidad del amparo federal y rechazo in limine<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_410_origen -.->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| AMP_460
  EXT_AMP_450_origen["AMP_450 Sentencia de amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_450_origen -.->|"Sentencia notificada y se apela"| AMP_460
  AMP_460 -->|"Apelación concedida"| AMP_480
  AMP_460 -->|"Apelación denegada"| AMP_470
  AMP_470 -->|"Queja o recurso directo admitido"| AMP_480
  AMP_470 -->|"Rechazado o no deducido: queda firme una decisión favorable"| EXT_AMP_500_destino
  EXT_AMP_955_destino["AMP_955 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_470 -->|"Rechazado o no deducido: queda firme el rechazo"| EXT_AMP_955_destino
  AMP_480 -->|"Sentencia favorable firme"| EXT_AMP_500_destino
  AMP_480 -->|"Rechazo firme"| EXT_AMP_955_destino
  AMP_480 -->|"Se interpone recurso extraordinario"| AMP_610
  AMP_600 -->|"Sentencia de la SCBA notificada y hay cuestión federal"| AMP_610
  EXT_AMP_520_destino["AMP_520 Sentencia de amparo firme tras los recursos extraordinarios<br/>(ver Prueba y sentencia)"]:::externo
  AMP_600 -->|"Resuelto por la SCBA sin cuestión federal, denegado o desistido"| EXT_AMP_520_destino
  AMP_610 -->|"Recurso federal resuelto, denegado (queja incluida) o desistido"| EXT_AMP_520_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 7. Cumplimiento, astreintes y ejecución contra el Estado

```mermaid
flowchart TD
  subgraph F_0["Cumplimiento"]
    AMP_500["<b>AMP_500</b> Cumplimiento de la sentencia de amparo en el plazo fijado<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    AMP_510["<b>AMP_510</b> Astreintes e intimación por incumplimiento de la orden judicial<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Ejecución"]
    AMP_830["<b>AMP_830</b> Liquidación de la condena (provincial)<br/>Responsable: Particular<br/>10 días hábiles judiciales + gracia"]:::actora
    AMP_850["<b>AMP_850</b> Cumplimiento forzado contra el Estado provincial: astreintes, embargo o ejecución directa<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_860["<b>AMP_860</b> Pago por el Estado y percepción<br/>Responsable: Estado u organismo<br/>Sin plazo"]:::demandada
  end
  EXT_AMP_250_origen["AMP_250 Sentencia de amparo (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_250_origen -.->|"Sentencia favorable notificada y no apelada"| AMP_500
  EXT_AMP_270_origen["AMP_270 Queja por apelación denegada en el amparo provincial (1 día)<br/>(ver Recursos)"]:::externo
  EXT_AMP_270_origen -.->|"Rechazado o no deducido: queda firme una decisión favorable"| AMP_500
  EXT_AMP_280_origen["AMP_280 Sentencia de la alzada en el amparo provincial<br/>(ver Recursos)"]:::externo
  EXT_AMP_280_origen -.->|"Sentencia favorable firme"| AMP_500
  EXT_AMP_325_origen["AMP_325 Cumplimiento de la medida cautelar por el demandado<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  EXT_AMP_325_origen -.->|"Medida incumplida"| AMP_510
  EXT_AMP_330_origen["AMP_330 Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  EXT_AMP_330_origen -.->|"Despachada e incumplida"| AMP_510
  EXT_AMP_450_origen["AMP_450 Sentencia de amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_450_origen -.->|"Sentencia favorable notificada y no apelada"| AMP_500
  EXT_AMP_470_origen["AMP_470 Recurso directo por apelación denegada en el amparo federal (24 horas)<br/>(ver Recursos)"]:::externo
  EXT_AMP_470_origen -.->|"Rechazado o no deducido: queda firme una decisión favorable"| AMP_500
  EXT_AMP_480_origen["AMP_480 Sentencia de la Cámara Federal en el amparo<br/>(ver Recursos)"]:::externo
  EXT_AMP_480_origen -.->|"Sentencia favorable firme"| AMP_500
  EXT_AMP_950_destino["AMP_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_500 -->|"Cumplida: proceso provincial"| EXT_AMP_950_destino
  EXT_AMP_955_destino["AMP_955 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Honorarios, derivación y cierre)"]:::externo
  AMP_500 -->|"Cumplida: proceso federal"| EXT_AMP_955_destino
  AMP_500 -->|"Vencido el plazo sin cumplir"| AMP_510
  AMP_500 -->|"La sentencia ordena pagar o reintegrar dinero a cargo del Estado provincial"| AMP_830
  AMP_510 -->|"Cumplimiento obtenido: proceso provincial"| EXT_AMP_950_destino
  AMP_510 -->|"Cumplimiento obtenido: proceso federal"| EXT_AMP_955_destino
  AMP_510 -->|"El Estado provincial persiste en el incumplimiento"| AMP_850
  EXT_AMP_520_origen["AMP_520 Sentencia de amparo firme tras los recursos extraordinarios<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_520_origen -.->|"Sentencia favorable firme"| AMP_500
  AMP_830 -->|"Liquidación aprobada"| AMP_860
  AMP_850 -->|"Cumplimiento o pago obtenido"| AMP_860
  AMP_860 -->|"Pago percibido y obligación cumplida"| EXT_AMP_950_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Honorarios, derivación y cierre

```mermaid
flowchart TD
  subgraph F_0["Cierre"]
    AMP_950["<b>AMP_950</b> Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    AMP_955["<b>AMP_955</b> Regulación de honorarios y apelación (federal, Ley 27.423)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    AMP_980["<b>AMP_980</b> Sigue en la matriz de contencioso administrativo<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    AMP_990["<b>AMP_990</b> Cierre y archivo del caso<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_AMP_010_origen["AMP_010 Encuadre del amparo, del demandado y del juzgado competente<br/>(ver Etapa previa: encuadre, competencia y amparo colectivo)"]:::externo
  EXT_AMP_010_origen -.->|"Hay otra vía idónea o la cuestión requiere mayor debate"| AMP_980
  EXT_AMP_040_origen["AMP_040 Respuesta, negativa o silencio del agente de salud<br/>(ver Reclamo previo: vía administrativa o intimación al agente de salud)"]:::externo
  EXT_AMP_040_origen -.->|"Cobertura otorgada"| AMP_990
  EXT_AMP_200_origen["AMP_200 Demanda de amparo provincial (Ley 13.928) dentro de los 30 días<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_200_origen -.->|"Venció el plazo sin demandar: evaluar otra vía"| AMP_980
  EXT_AMP_230_origen["AMP_230 Audiencia simplificadora (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_230_origen -.->|"La actora no comparece: se la tiene por desistida"| AMP_950
  EXT_AMP_250_origen["AMP_250 Sentencia de amparo (Ley 13.928)<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_250_origen -.->|"Sentencia de rechazo notificada y no apelada"| AMP_950
  EXT_AMP_270_origen["AMP_270 Queja por apelación denegada en el amparo provincial (1 día)<br/>(ver Recursos)"]:::externo
  EXT_AMP_270_origen -.->|"Rechazado o no deducido: queda firme el rechazo"| AMP_950
  EXT_AMP_280_origen["AMP_280 Sentencia de la alzada en el amparo provincial<br/>(ver Recursos)"]:::externo
  EXT_AMP_280_origen -.->|"Rechazo firme"| AMP_950
  EXT_AMP_330_origen["AMP_330 Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento<br/>(ver Medidas cautelares y autosatisfactiva)"]:::externo
  EXT_AMP_330_origen -.->|"Despachada y cumplida"| AMP_950
  EXT_AMP_400_origen["AMP_400 Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles<br/>(ver Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986))"]:::externo
  EXT_AMP_400_origen -.->|"Venció el plazo sin demandar: evaluar otra vía"| AMP_980
  EXT_AMP_430_origen["AMP_430 Audiencia de prueba en el amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_430_origen -.->|"La actora no comparece: se la tiene por desistida"| AMP_955
  EXT_AMP_450_origen["AMP_450 Sentencia de amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_450_origen -.->|"Sentencia de rechazo notificada y no apelada"| AMP_955
  EXT_AMP_470_origen["AMP_470 Recurso directo por apelación denegada en el amparo federal (24 horas)<br/>(ver Recursos)"]:::externo
  EXT_AMP_470_origen -.->|"Rechazado o no deducido: queda firme el rechazo"| AMP_955
  EXT_AMP_480_origen["AMP_480 Sentencia de la Cámara Federal en el amparo<br/>(ver Recursos)"]:::externo
  EXT_AMP_480_origen -.->|"Rechazo firme"| AMP_955
  EXT_AMP_500_origen["AMP_500 Cumplimiento de la sentencia de amparo en el plazo fijado<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  EXT_AMP_500_origen -.->|"Cumplida: proceso provincial"| AMP_950
  EXT_AMP_500_origen -.->|"Cumplida: proceso federal"| AMP_955
  EXT_AMP_510_origen["AMP_510 Astreintes e intimación por incumplimiento de la orden judicial<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  EXT_AMP_510_origen -.->|"Cumplimiento obtenido: proceso provincial"| AMP_950
  EXT_AMP_510_origen -.->|"Cumplimiento obtenido: proceso federal"| AMP_955
  EXT_AMP_520_origen["AMP_520 Sentencia de amparo firme tras los recursos extraordinarios<br/>(ver Prueba y sentencia)"]:::externo
  EXT_AMP_520_origen -.->|"Rechazo firme: proceso provincial"| AMP_950
  EXT_AMP_520_origen -.->|"Rechazo firme: proceso federal"| AMP_955
  EXT_AMP_860_origen["AMP_860 Pago por el Estado y percepción<br/>(ver Cumplimiento, astreintes y ejecución contra el Estado)"]:::externo
  EXT_AMP_860_origen -.->|"Pago percibido y obligación cumplida"| AMP_950
  AMP_950 -->|"Regulación firme y aportes acreditados"| AMP_990
  AMP_955 -->|"Regulación firme y aportes acreditados"| AMP_990
  style AMP_980 stroke-width:3px
  style AMP_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
