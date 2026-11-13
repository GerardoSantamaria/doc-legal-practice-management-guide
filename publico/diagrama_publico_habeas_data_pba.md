# Diagrama de Flujo: Hábeas data (PBA, con variante federal)

**Régimen:** Ley 14.214 con el CPCCBA supletorio (sumarísimo, art. 8); variante federal: Ley 25.326 (arts. 33 a 44), con el procedimiento del amparo común y el sumarísimo del CPCCN supletorios (art. 37) · **Versión:** 1 (borrador)

> Este documento se genera a partir de `matriz_publico_habeas_data_pba.xlsx`. No se edita a mano: las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.

## Cómo leer los diagramas

* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.
* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.
* **Color de la caja según el responsable:** celeste = el particular que reclama (ACTORA); naranja = el Estado o el organismo demandado, también cuando resuelve en la vía administrativa (DEMANDADA); gris = juzgado, tribunal u organismo de control que no es parte, como la AAIP o el Tribunal Fiscal de Apelación (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).
* **Borde grueso:** hito inicial o hito final.
* **"Se abren en paralelo"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la negativa o el silencio del responsable abren a la vez la demanda y la denuncia ante la AAIP.
* **"Fin de este camino"** (gris claro): el camino paralelo termina sin abrir otro hito.
* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. Las flechas punteadas muestran desde dónde se llega a esta etapa.
* **Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "Sigue en la matriz de ...": el caso continúa en otra matriz de Derecho Público, en un expediente vinculado.
* **Provincial o federal:** cuando un flujo tiene las dos variantes, el nombre del hito lo dice ("provincial" o "federal") o nombra la ley que lo rige (por ejemplo, "Ley 13.928" o "Ley 16.986").
* **Vía administrativa:** sus hitos están en un diagrama aparte de los judiciales. La Administración que resuelve aparece en naranja, como parte demandada, y sus plazos son días hábiles administrativos.
* **Fuero según el banco de datos:** bancos privados provinciales, juzgado Civil y Comercial o de Paz; públicos provinciales, Contencioso Administrativo (art. 4 Ley 14.214); públicos nacionales o interconectados, justicia federal (art. 36 Ley 25.326).

## Vista general por fases

```mermaid
flowchart LR
  FASE_1["Previa<br/>3 hitos"]
  FASE_2["Vía administrativa<br/>4 hitos"]
  FASE_3["Organismo de control<br/>1 hito"]
  FASE_4["Demanda<br/>7 hitos"]
  FASE_5["Cautelares<br/>2 hitos"]
  FASE_6["Prueba<br/>2 hitos"]
  FASE_7["Sentencia<br/>2 hitos"]
  FASE_8["Recursos<br/>5 hitos"]
  FASE_9["Cumplimiento<br/>2 hitos"]
  FASE_10["Cierre<br/>3 hitos"]
  FASE_1 --> FASE_2
  FASE_1 --> FASE_4
  FASE_2 --> FASE_10
  FASE_2 --> FASE_4
  FASE_2 --> FASE_3
  FASE_1 --> FASE_10
  FASE_4 --> FASE_5
  FASE_4 --> FASE_2
  FASE_4 --> FASE_8
  FASE_5 --> FASE_8
  FASE_4 --> FASE_6
  FASE_4 --> FASE_7
  FASE_6 --> FASE_7
  FASE_7 --> FASE_8
  FASE_7 --> FASE_9
  FASE_7 --> FASE_10
  FASE_8 --> FASE_9
  FASE_8 --> FASE_10
  FASE_6 --> FASE_10
  FASE_9 --> FASE_10
```

## 1. Etapa previa: encuadre, datos crediticios y Central de Deudores

```mermaid
flowchart TD
  subgraph F_0["Previa"]
    HDA_010["INICIO - <b>HDA_010</b> Encuadre del hábeas data, del banco de datos y del fuero<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    HDA_060["<b>HDA_060</b> Control del plazo de conservación del dato crediticio<br/>Responsable: Particular<br/>2 años"]:::actora
    HDA_070["<b>HDA_070</b> Central de Deudores del BCRA: identificación de la entidad informante<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  EXT_HDA_020_destino["HDA_020 Solicitud fehaciente de acceso a los datos<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  HDA_010 -->|"Acceso a los datos"| EXT_HDA_020_destino
  EXT_HDA_040_destino["HDA_040 Reclamo de rectificación, actualización, supresión o confidencialidad<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  HDA_010 -->|"Rectificación, actualización, supresión o confidencialidad"| EXT_HDA_040_destino
  HDA_010 -->|"Dato crediticio de una deuda cancelada o antigua"| HDA_060
  HDA_010 -->|"Dato informado en la Central de Deudores del BCRA"| HDA_070
  EXT_HDA_200_destino["HDA_200 Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  HDA_010 -->|"Perjuicio de imposible reparación: demanda sin reclamo previo en la provincia (art. 5 Ley 14.214)"| EXT_HDA_200_destino
  EXT_HDA_400_destino["HDA_400 Demanda de hábeas data federal (Ley 25.326)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  HDA_010 -->|"Perjuicio de imposible reparación: demanda sin reclamo previo contra un banco nacional o interconectado"| EXT_HDA_400_destino
  HDA_060 -->|"Venció el plazo y el dato sigue informado: reclamar la supresión"| EXT_HDA_040_destino
  EXT_HDA_990_destino["HDA_990 Cierre y archivo del caso<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_060 -->|"El dato dejó de informarse"| EXT_HDA_990_destino
  HDA_070 -->|"Entidad informante identificada y constancia reunida"| EXT_HDA_040_destino
  style HDA_010 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 2. Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214)

```mermaid
flowchart TD
  subgraph F_0["Vía administrativa"]
    HDA_020["<b>HDA_020</b> Solicitud fehaciente de acceso a los datos<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    HDA_030["<b>HDA_030</b> Respuesta del responsable al pedido de acceso<br/>Responsable: Estado u organismo<br/>10 días corridos"]:::demandada
    HDA_040["<b>HDA_040</b> Reclamo de rectificación, actualización, supresión o confidencialidad<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    HDA_050["<b>HDA_050</b> Respuesta del responsable al reclamo de rectificación o supresión<br/>Responsable: Estado u organismo<br/>5 días hábiles administrativos"]:::demandada
  end
  EXT_HDA_010_origen["HDA_010 Encuadre del hábeas data, del banco de datos y del fuero<br/>(ver Etapa previa: encuadre, datos crediticios y Central de Deudores)"]:::externo
  EXT_HDA_010_origen -.->|"Acceso a los datos"| HDA_020
  EXT_HDA_010_origen -.->|"Rectificación, actualización, supresión o confidencialidad"| HDA_040
  HDA_020 -->|"Solicitud entregada"| HDA_030
  EXT_HDA_990_destino["HDA_990 Cierre y archivo del caso<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_030 -->|"Información suficiente y correcta"| EXT_HDA_990_destino
  HDA_030 -->|"La información muestra datos falsos, inexactos o desactualizados"| HDA_040
  EXT_HDA_200_destino["HDA_200 Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  HDA_030 -->|"Silencio o respuesta insuficiente: banco provincial"| EXT_HDA_200_destino
  EXT_HDA_400_destino["HDA_400 Demanda de hábeas data federal (Ley 25.326)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  HDA_030 -->|"Silencio o respuesta insuficiente: banco nacional o interconectado"| EXT_HDA_400_destino
  HDA_040 -->|"Reclamo entregado"| HDA_050
  HDA_050 -->|"Dato rectificado, actualizado, suprimido o declarado confidencial"| EXT_HDA_990_destino
  P_HDA_050_2(["Se abren en paralelo"]):::paralelo
  HDA_050 -->|"Negativa o silencio: banco provincial"| P_HDA_050_2
  P_HDA_050_2 --> EXT_HDA_200_destino
  EXT_HDA_080_destino["HDA_080 Denuncia ante la Agencia de Acceso a la Información Pública (AAIP)<br/>(ver Denuncia ante la AAIP)"]:::externo
  P_HDA_050_2 --> EXT_HDA_080_destino
  P_HDA_050_3(["Se abren en paralelo"]):::paralelo
  HDA_050 -->|"Negativa o silencio: banco nacional o interconectado"| P_HDA_050_3
  P_HDA_050_3 --> EXT_HDA_400_destino
  P_HDA_050_3 --> EXT_HDA_080_destino
  EXT_HDA_060_origen["HDA_060 Control del plazo de conservación del dato crediticio<br/>(ver Etapa previa: encuadre, datos crediticios y Central de Deudores)"]:::externo
  EXT_HDA_060_origen -.->|"Venció el plazo y el dato sigue informado: reclamar la supresión"| HDA_040
  EXT_HDA_070_origen["HDA_070 Central de Deudores del BCRA: identificación de la entidad informante<br/>(ver Etapa previa: encuadre, datos crediticios y Central de Deudores)"]:::externo
  EXT_HDA_070_origen -.->|"Entidad informante identificada y constancia reunida"| HDA_040
  EXT_HDA_200_origen["HDA_200 Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_200_origen -.->|"Venció el plazo: reiterar el reclamo o la intimación previa (art. 7)"| HDA_040
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 3. Denuncia ante la AAIP

```mermaid
flowchart TD
  subgraph F_0["Organismo de control"]
    HDA_080["<b>HDA_080</b> Denuncia ante la Agencia de Acceso a la Información Pública (AAIP)<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  EXT_HDA_050_origen["HDA_050 Respuesta del responsable al reclamo de rectificación o supresión<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  EXT_HDA_050_origen -.->|"Negativa o silencio: banco provincial"| HDA_080
  EXT_HDA_050_origen -.->|"Negativa o silencio: banco nacional o interconectado"| HDA_080
  FIN_HDA_080_1(["Fin de este camino"]):::fin
  HDA_080 -->|"Denuncia presentada"| FIN_HDA_080_1
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 4. Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326)

```mermaid
flowchart TD
  subgraph F_0["Demanda"]
    HDA_200["<b>HDA_200</b> Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles<br/>Responsable: Particular<br/>60 días hábiles judiciales"]:::actora
    HDA_210["<b>HDA_210</b> Admisión formal de la demanda de hábeas data provincial<br/>Responsable: Juzgado u organismo de control<br/>2 días hábiles judiciales"]:::tribunal
    HDA_230["<b>HDA_230</b> Informe del banco de datos (Ley 14.214)<br/>Responsable: Estado u organismo<br/>5 días hábiles judiciales + gracia"]:::demandada
    HDA_400["<b>HDA_400</b> Demanda de hábeas data federal (Ley 25.326)<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    HDA_410["<b>HDA_410</b> Admisión del hábeas data federal y rechazo in limine<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    HDA_420["<b>HDA_420</b> Informe del banco de datos (Ley 25.326)<br/>Responsable: Estado u organismo<br/>5 días hábiles judiciales"]:::demandada
    HDA_425["<b>HDA_425</b> Ampliación de la demanda tras el informe (federal)<br/>Responsable: Particular<br/>3 días hábiles judiciales"]:::actora
  end
  EXT_HDA_010_origen["HDA_010 Encuadre del hábeas data, del banco de datos y del fuero<br/>(ver Etapa previa: encuadre, datos crediticios y Central de Deudores)"]:::externo
  EXT_HDA_010_origen -.->|"Perjuicio de imposible reparación: demanda sin reclamo previo en la provincia (art. 5 Ley 14.214)"| HDA_200
  EXT_HDA_010_origen -.->|"Perjuicio de imposible reparación: demanda sin reclamo previo contra un banco nacional o interconectado"| HDA_400
  EXT_HDA_030_origen["HDA_030 Respuesta del responsable al pedido de acceso<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  EXT_HDA_030_origen -.->|"Silencio o respuesta insuficiente: banco provincial"| HDA_200
  EXT_HDA_030_origen -.->|"Silencio o respuesta insuficiente: banco nacional o interconectado"| HDA_400
  EXT_HDA_050_origen["HDA_050 Respuesta del responsable al reclamo de rectificación o supresión<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  EXT_HDA_050_origen -.->|"Negativa o silencio: banco provincial"| HDA_200
  EXT_HDA_050_origen -.->|"Negativa o silencio: banco nacional o interconectado"| HDA_400
  HDA_200 -->|"Demanda presentada"| HDA_210
  EXT_HDA_220_destino["HDA_220 Anotación de litigiosidad o bloqueo provisional del dato<br/>(ver Anotación de litigiosidad y bloqueo provisional)"]:::externo
  HDA_200 -->|"Se pide anotación de litigiosidad o bloqueo provisional"| EXT_HDA_220_destino
  EXT_HDA_040_destino["HDA_040 Reclamo de rectificación, actualización, supresión o confidencialidad<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  HDA_200 -->|"Venció el plazo: reiterar el reclamo o la intimación previa (art. 7)"| EXT_HDA_040_destino
  HDA_210 -->|"Demanda admitida: se emplaza a informar"| HDA_230
  EXT_HDA_260_destino["HDA_260 Apelación de la sentencia de hábeas data provincial<br/>(ver Recursos)"]:::externo
  HDA_210 -->|"Demanda rechazada in limine: se apela"| EXT_HDA_260_destino
  EXT_HDA_240_destino["HDA_240 Prueba en el hábeas data provincial<br/>(ver Prueba y sentencia)"]:::externo
  HDA_230 -->|"Informe presentado o vencido: hay hechos controvertidos"| EXT_HDA_240_destino
  EXT_HDA_250_destino["HDA_250 Sentencia de hábeas data provincial<br/>(ver Prueba y sentencia)"]:::externo
  HDA_230 -->|"Informe presentado o vencido: no hay hechos controvertidos"| EXT_HDA_250_destino
  HDA_400 -->|"Se pide anotación de litigiosidad o bloqueo provisional"| EXT_HDA_220_destino
  HDA_400 -->|"Demanda presentada"| HDA_410
  HDA_410 -->|"Demanda admitida: se requiere el informe"| HDA_420
  EXT_HDA_460_destino["HDA_460 Apelación en el amparo federal (48 horas)<br/>(ver Recursos)"]:::externo
  HDA_410 -->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| EXT_HDA_460_destino
  HDA_420 -->|"Informe contestado: se amplía la demanda (art. 42)"| HDA_425
  EXT_HDA_430_destino["HDA_430 Audiencia de prueba en el amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  HDA_420 -->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| EXT_HDA_430_destino
  EXT_HDA_450_destino["HDA_450 Sentencia de hábeas data federal<br/>(ver Prueba y sentencia)"]:::externo
  HDA_420 -->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| EXT_HDA_450_destino
  HDA_425 -->|"Ampliación contestada o vencido el traslado: hay prueba que producir"| EXT_HDA_430_destino
  HDA_425 -->|"Ampliación contestada o vencido el traslado: sin prueba pendiente"| EXT_HDA_450_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 5. Anotación de litigiosidad y bloqueo provisional

```mermaid
flowchart TD
  subgraph F_0["Cautelares"]
    HDA_220["<b>HDA_220</b> Anotación de litigiosidad o bloqueo provisional del dato<br/>Responsable: Particular<br/>Sin plazo"]:::actora
    HDA_225["<b>HDA_225</b> Apelación de la resolución cautelar (provincial)<br/>Responsable: Cualquiera de las partes<br/>2 días hábiles judiciales + gracia"]:::ambas
  end
  EXT_HDA_200_origen["HDA_200 Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_200_origen -.->|"Se pide anotación de litigiosidad o bloqueo provisional"| HDA_220
  HDA_220 -->|"Medida resuelta por el juzgado provincial y se apela"| HDA_225
  EXT_HDA_460_destino["HDA_460 Apelación en el amparo federal (48 horas)<br/>(ver Recursos)"]:::externo
  HDA_220 -->|"Medida resuelta por el juzgado federal y se apela"| EXT_HDA_460_destino
  FIN_HDA_220_3(["Fin de este camino"]):::fin
  HDA_220 -->|"Medida resuelta y no se apela"| FIN_HDA_220_3
  FIN_HDA_225_1(["Fin de este camino"]):::fin
  HDA_225 -->|"Apelación resuelta"| FIN_HDA_225_1
  EXT_HDA_400_origen["HDA_400 Demanda de hábeas data federal (Ley 25.326)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_400_origen -.->|"Se pide anotación de litigiosidad o bloqueo provisional"| HDA_220
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 6. Prueba y sentencia

```mermaid
flowchart TD
  subgraph F_0["Prueba"]
    HDA_240["<b>HDA_240</b> Prueba en el hábeas data provincial<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
    HDA_430["<b>HDA_430</b> Audiencia de prueba en el amparo federal<br/>Responsable: Cualquiera de las partes<br/>Fecha y hora fijadas por el tribunal"]:::ambas
  end
  subgraph F_1["Sentencia"]
    HDA_250["<b>HDA_250</b> Sentencia de hábeas data provincial<br/>Responsable: Juzgado u organismo de control<br/>10 días hábiles judiciales"]:::tribunal
    HDA_450["<b>HDA_450</b> Sentencia de hábeas data federal<br/>Responsable: Juzgado u organismo de control<br/>48 horas"]:::tribunal
  end
  EXT_HDA_230_origen["HDA_230 Informe del banco de datos (Ley 14.214)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_230_origen -.->|"Informe presentado o vencido: hay hechos controvertidos"| HDA_240
  EXT_HDA_230_origen -.->|"Informe presentado o vencido: no hay hechos controvertidos"| HDA_250
  HDA_240 -->|"Prueba producida o vencido su plazo"| HDA_250
  EXT_HDA_260_destino["HDA_260 Apelación de la sentencia de hábeas data provincial<br/>(ver Recursos)"]:::externo
  HDA_250 -->|"Sentencia notificada y se apela"| EXT_HDA_260_destino
  EXT_HDA_500_destino["HDA_500 Cumplimiento de la sentencia por el banco de datos<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_250 -->|"Sentencia favorable no apelada"| EXT_HDA_500_destino
  EXT_HDA_950_destino["HDA_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_250 -->|"Rechazo no apelado"| EXT_HDA_950_destino
  EXT_HDA_420_origen["HDA_420 Informe del banco de datos (Ley 25.326)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_420_origen -.->|"Contestación o informe presentados, o vencido el plazo: hay hechos que probar"| HDA_430
  EXT_HDA_420_origen -.->|"Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente"| HDA_450
  EXT_HDA_425_origen["HDA_425 Ampliación de la demanda tras el informe (federal)<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_425_origen -.->|"Ampliación contestada o vencido el traslado: hay prueba que producir"| HDA_430
  EXT_HDA_425_origen -.->|"Ampliación contestada o vencido el traslado: sin prueba pendiente"| HDA_450
  HDA_430 -->|"Audiencia de prueba realizada"| HDA_450
  EXT_HDA_955_destino["HDA_955 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_430 -->|"La actora no comparece: se la tiene por desistida"| EXT_HDA_955_destino
  EXT_HDA_460_destino["HDA_460 Apelación en el amparo federal (48 horas)<br/>(ver Recursos)"]:::externo
  HDA_450 -->|"Sentencia notificada y se apela"| EXT_HDA_460_destino
  HDA_450 -->|"Sentencia favorable notificada y no apelada"| EXT_HDA_500_destino
  HDA_450 -->|"Sentencia de rechazo notificada y no apelada"| EXT_HDA_955_destino
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
    HDA_260["<b>HDA_260</b> Apelación de la sentencia de hábeas data provincial<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    HDA_270["<b>HDA_270</b> Sentencia de la alzada en el hábeas data provincial<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
    HDA_460["<b>HDA_460</b> Apelación en el amparo federal (48 horas)<br/>Responsable: Cualquiera de las partes<br/>48 horas"]:::ambas
    HDA_470["<b>HDA_470</b> Recurso directo por apelación denegada en el amparo federal (24 horas)<br/>Responsable: Cualquiera de las partes<br/>24 horas"]:::ambas
    HDA_480["<b>HDA_480</b> Sentencia de la Cámara Federal en el amparo<br/>Responsable: Juzgado u organismo de control<br/>Sin plazo"]:::tribunal
  end
  EXT_HDA_210_origen["HDA_210 Admisión formal de la demanda de hábeas data provincial<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_210_origen -.->|"Demanda rechazada in limine: se apela"| HDA_260
  EXT_HDA_220_origen["HDA_220 Anotación de litigiosidad o bloqueo provisional del dato<br/>(ver Anotación de litigiosidad y bloqueo provisional)"]:::externo
  EXT_HDA_220_origen -.->|"Medida resuelta por el juzgado federal y se apela"| HDA_460
  EXT_HDA_250_origen["HDA_250 Sentencia de hábeas data provincial<br/>(ver Prueba y sentencia)"]:::externo
  EXT_HDA_250_origen -.->|"Sentencia notificada y se apela"| HDA_260
  HDA_260 -->|"Apelación concedida"| HDA_270
  EXT_HDA_500_destino["HDA_500 Cumplimiento de la sentencia por el banco de datos<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_260 -->|"Apelación denegada: queda firme una decisión favorable"| EXT_HDA_500_destino
  EXT_HDA_950_destino["HDA_950 Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_260 -->|"Apelación denegada: queda firme el rechazo"| EXT_HDA_950_destino
  HDA_270 -->|"Sentencia favorable firme"| EXT_HDA_500_destino
  HDA_270 -->|"Rechazo firme"| EXT_HDA_950_destino
  EXT_HDA_410_origen["HDA_410 Admisión del hábeas data federal y rechazo in limine<br/>(ver Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326))"]:::externo
  EXT_HDA_410_origen -.->|"Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)"| HDA_460
  EXT_HDA_450_origen["HDA_450 Sentencia de hábeas data federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_HDA_450_origen -.->|"Sentencia notificada y se apela"| HDA_460
  HDA_460 -->|"Apelación concedida"| HDA_480
  HDA_460 -->|"Apelación denegada"| HDA_470
  HDA_470 -->|"Queja o recurso directo admitido"| HDA_480
  HDA_470 -->|"Rechazado o no deducido: queda firme una decisión favorable"| EXT_HDA_500_destino
  EXT_HDA_955_destino["HDA_955 Regulación de honorarios y apelación (federal, Ley 27.423)<br/>(ver Cumplimiento, honorarios y cierre)"]:::externo
  HDA_470 -->|"Rechazado o no deducido: queda firme el rechazo"| EXT_HDA_955_destino
  HDA_480 -->|"Sentencia favorable firme"| EXT_HDA_500_destino
  HDA_480 -->|"Rechazo firme"| EXT_HDA_955_destino
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```

## 8. Cumplimiento, honorarios y cierre

```mermaid
flowchart TD
  subgraph F_0["Cumplimiento"]
    HDA_500["<b>HDA_500</b> Cumplimiento de la sentencia por el banco de datos<br/>Responsable: Estado u organismo<br/>Fecha y hora fijadas por el tribunal"]:::demandada
    HDA_510["<b>HDA_510</b> Incumplimiento: astreintes y comunicación a la AAIP<br/>Responsable: Particular<br/>Sin plazo"]:::actora
  end
  subgraph F_1["Cierre"]
    HDA_950["<b>HDA_950</b> Regulación de honorarios y apelación (provincial, Ley 14.967)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales + gracia"]:::ambas
    HDA_955["<b>HDA_955</b> Regulación de honorarios y apelación (federal, Ley 27.423)<br/>Responsable: Cualquiera de las partes<br/>5 días hábiles judiciales"]:::ambas
    HDA_990["<b>HDA_990</b> Cierre y archivo del caso<br/>Responsable: Cualquiera de las partes<br/>Sin plazo"]:::ambas
  end
  EXT_HDA_030_origen["HDA_030 Respuesta del responsable al pedido de acceso<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  EXT_HDA_030_origen -.->|"Información suficiente y correcta"| HDA_990
  EXT_HDA_050_origen["HDA_050 Respuesta del responsable al reclamo de rectificación o supresión<br/>(ver Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214))"]:::externo
  EXT_HDA_050_origen -.->|"Dato rectificado, actualizado, suprimido o declarado confidencial"| HDA_990
  EXT_HDA_060_origen["HDA_060 Control del plazo de conservación del dato crediticio<br/>(ver Etapa previa: encuadre, datos crediticios y Central de Deudores)"]:::externo
  EXT_HDA_060_origen -.->|"El dato dejó de informarse"| HDA_990
  EXT_HDA_250_origen["HDA_250 Sentencia de hábeas data provincial<br/>(ver Prueba y sentencia)"]:::externo
  EXT_HDA_250_origen -.->|"Sentencia favorable no apelada"| HDA_500
  EXT_HDA_250_origen -.->|"Rechazo no apelado"| HDA_950
  EXT_HDA_260_origen["HDA_260 Apelación de la sentencia de hábeas data provincial<br/>(ver Recursos)"]:::externo
  EXT_HDA_260_origen -.->|"Apelación denegada: queda firme una decisión favorable"| HDA_500
  EXT_HDA_260_origen -.->|"Apelación denegada: queda firme el rechazo"| HDA_950
  EXT_HDA_270_origen["HDA_270 Sentencia de la alzada en el hábeas data provincial<br/>(ver Recursos)"]:::externo
  EXT_HDA_270_origen -.->|"Sentencia favorable firme"| HDA_500
  EXT_HDA_270_origen -.->|"Rechazo firme"| HDA_950
  EXT_HDA_430_origen["HDA_430 Audiencia de prueba en el amparo federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_HDA_430_origen -.->|"La actora no comparece: se la tiene por desistida"| HDA_955
  EXT_HDA_450_origen["HDA_450 Sentencia de hábeas data federal<br/>(ver Prueba y sentencia)"]:::externo
  EXT_HDA_450_origen -.->|"Sentencia favorable notificada y no apelada"| HDA_500
  EXT_HDA_450_origen -.->|"Sentencia de rechazo notificada y no apelada"| HDA_955
  EXT_HDA_470_origen["HDA_470 Recurso directo por apelación denegada en el amparo federal (24 horas)<br/>(ver Recursos)"]:::externo
  EXT_HDA_470_origen -.->|"Rechazado o no deducido: queda firme una decisión favorable"| HDA_500
  EXT_HDA_470_origen -.->|"Rechazado o no deducido: queda firme el rechazo"| HDA_955
  EXT_HDA_480_origen["HDA_480 Sentencia de la Cámara Federal en el amparo<br/>(ver Recursos)"]:::externo
  EXT_HDA_480_origen -.->|"Sentencia favorable firme"| HDA_500
  EXT_HDA_480_origen -.->|"Rechazo firme"| HDA_955
  HDA_500 -->|"Cumplida: proceso provincial"| HDA_950
  HDA_500 -->|"Cumplida: proceso federal"| HDA_955
  HDA_500 -->|"Vencido el plazo sin cumplir"| HDA_510
  HDA_510 -->|"Cumplimiento obtenido: proceso provincial"| HDA_950
  HDA_510 -->|"Cumplimiento obtenido: proceso federal"| HDA_955
  HDA_950 -->|"Regulación firme y aportes acreditados"| HDA_990
  HDA_955 -->|"Regulación firme y aportes acreditados"| HDA_990
  style HDA_990 stroke-width:3px
  classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000
  classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000
  classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000
  classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000
  classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3
  classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000
  classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040
```
