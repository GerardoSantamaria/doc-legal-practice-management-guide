# Reunión de validación con el abogado · 12/11/2026

**Estado:** preparación · **Fecha:** 11/11/2026

Esta reunión cierra las 36 dudas de la matriz del fuero laboral (hoja `Dudas_a_validar` de [`matriz_flujo_laboral_pba_ley_11653.xlsx`](matriz_flujo_laboral_pba_ley_11653.xlsx)). Las respuestas definen los datos del régimen procesal, los parámetros del motor de plazos y los valores de la versión 1 del flujo. El documento ordena las dudas por impacto y dice, para cada una, qué hay que decidir, qué propone la app, qué afecta y qué pasa si no se llega a responder.

---

## 1. Objetivo y resultado esperado

Al terminar la reunión tienen que quedar:

1. **El régimen y la estructura** (D01, D24 y D25) respondidos, o con la fuente y la fecha en que llega el dato.
2. **Las nueve reglas del motor** (D26 a D34) confirmadas o corregidas. Son parámetros del backend que se construye desde la primera semana.
3. **Las dudas hito por hito** (D02 a D23) respondidas, o con fecha para responderlas por escrito en la planilla.
4. **Quién firma la versión 1 y cuándo.**

**Lo que no se decide en esta reunión:** precios, proveedor de pagos, hosting ni nada de producto. Si surge, se anota y se sigue.

## 2. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal`, con la norma o la acordada que la sostiene, y `Estado` pasa a `VALIDADO` o `CORREGIR`. Si una respuesta cambia un hito, también se corrige la fila en `Nodos` o en `Transiciones`, con su `Estado_Validacion`.
- **Ante la duda, el vencimiento más temprano.** Es el principio del motor. Cada duda tiene una postura por defecto que cumple ese principio. Una duda sin respuesta no frena el desarrollo, pero tampoco se firma la versión con una postura por defecto que el abogado no haya aceptado por escrito.
- **Una respuesta del tipo "depende"** se registra con los casos de los que depende. La app no puede elegir sola; si hace falta, la decisión pasa al abogado que usa la app, con un aviso en pantalla.
- **No correr `generar.py` después de la reunión:** pisa la planilla con lo que hay en `datos.py` (ver [`herramientas/README.md`](herramientas/README.md)).

**Material para llevar:**
- la planilla, impresa o en pantalla, con la hoja `Dudas_a_validar` abierta;
- el diagrama del flujo ([`diagrama_flujo_laboral_pba_ley_11653.md`](diagrama_flujo_laboral_pba_ley_11653.md));
- la sección 4 del [documento de lógica de plazos](logica_matematica_calculadora_de_dias_habiles_judiciales.md), con las reglas R1 a R9 y sus casos de prueba;
- este documento.

## 3. Agenda

Duración sugerida: 2 horas y media, con un corte de 10 minutos. Si no alcanza el tiempo, el bloque C se responde por escrito en la planilla.

| Bloque | Dudas | Tiempo | Por qué en este orden |
| :--- | :--- | :--- | :--- |
| A · Régimen y estructura | D01, D24, D25 | 30 min | Definen qué flujo se asigna a cada expediente. Es lo único que puede cambiar la estructura. |
| B · Reglas del motor | D26 a D34 (con D04, D06, D08 y D13) | 45 min | El motor es lo primero que se programa. Cada respuesta cambia un parámetro o una rama, y tiene un caso de prueba. |
| C · Hito por hito | D02, D03, D05, D07, D09 a D12, D14 a D23 | 45 min | Cambian valores de la matriz. Se pueden corregir hasta la firma sin tocar código. |
| D · Casos borde | D35, D36 | 10 min | El diseño de la V1 ya está decidido; solo se confirma. |
| E · Cierre | Firma, calendario y documentos legales | 20 min | Quién valida, con qué fuente y para cuándo. |

---

## 4. Bloque A · Régimen y estructura

### D01 · Régimen procesal por departamento

- **Qué hay que decidir:** en qué departamentos judiciales rige la Ley 11.653 y en cuáles la Ley 15.057, y desde qué fecha.
- **Propuesta de la app:** no es una opción, es un dato. Pedir la fuente (las resoluciones de la SCBA que implementan la Ley 15.057 en cada departamento) y quién lo mantiene cuando se implementa en uno nuevo.
- **Qué afecta:** la tabla `department_regimes` y el régimen de cada tribunal en `courts`; con eso, qué expedientes reciben el flujo de la V1. Es el punto 1 de la sección 4 del [análisis](analisis_y_definiciones_pendientes_v1.md).
- **Si no se responde:** el desarrollo sigue igual, pero solo se asigna flujo en los tribunales que el equipo cargue con el régimen confirmado. En los demás, la app informa que el régimen no tiene flujo y deja cargar plazos sueltos.

### D24 · Régimen de las causas iniciadas antes de la Ley 15.057

- **Qué hay que decidir:** si una causa iniciada antes de la implementación sigue hasta el final con la Ley 11.653, y si el dato que define el régimen es la fecha de interposición de la demanda.
- **Opciones:**
  - (a) El régimen lo define el tribunal donde tramita; el departamento y la fecha de interposición solo sirven de control.
  - (b) Lo define la fecha de interposición frente a la fecha de implementación del departamento.
- **Propuesta de la app:** (a). Es lo que ya está diseñado: si el tribunal y la fecha no coinciden, el expediente queda "inconsistente" y no se asigna flujo hasta que el abogado lo revise.
- **Qué afecta:** la resolución del régimen en el alta (BE-35) y el alta de expedientes en curso (BE-36), que es como se va a cargar la cartera existente de cada estudio.
- **Si no se responde:** queda (a). Ante una inconsistencia la app no adivina.

### D25 · Etapa previa común a los dos regímenes

- **Qué hay que decidir:** si la etapa prejudicial (intimaciones, prescripción, conciliación previa) es igual en las dos leyes.
- **Opciones:** (a) un flujo prejudicial común y el judicial se elige al interponer la demanda; (b) un flujo prejudicial por régimen.
- **Propuesta de la app:** (a), ya modelada (`flows.flow_kind = PREJUDICIAL`). Si la respuesta es (b), se publica un segundo flujo prejudicial; no cambia la estructura.
- **Qué afecta:** los hitos `LAB_010` a `LAB_040` y la forma de dividir la planilla en dos versiones de flujo.
- **Si no se responde:** queda (a).

---

## 5. Bloque B · Reglas del motor

Cada regla ya tiene una implementación por defecto (la más temprana), con su caso de prueba en verde en [`herramientas/motor_plazos_referencia.py`](herramientas/motor_plazos_referencia.py). Si la respuesta coincide con la propuesta, no cambia nada. Si no, se cambia el parámetro y el caso de prueba antes de que se programe el módulo Java (BE-24 a BE-26).

| Duda | Regla | Qué hay que decidir | Propuesta de la app (por defecto) | Casos |
| :--- | :--- | :--- | :--- | :--- |
| D26 | R1 | Notificación en día inhábil: ¿desde cuándo corre? | El Día Uno es el primer hábil posterior, sin mover la fecha de notificación. | 10, 12 |
| D27 | R2 | Plazo corrido que termina en inhábil: ¿se traslada? | Se alerta por el día nominal (el inhábil) y se muestra el hábil siguiente como vencimiento efectivo. | 11 |
| D28 | R3 | Hora límite y plazo de gracia; presentación electrónica fuera de horario; qué plazos vencen a las 24:00 | Horario de 08:00 a 14:00; vencimiento ordinario a las 14:00; gracia hasta las 12:00 del hábil siguiente. La presentación fuera de horario cuenta en el hábil siguiente, dentro de la gracia. La prescripción vence a las 24:00. | 13 |
| D29 | R4 | Jueves Santo, 24/12 y 31/12; fuente oficial del calendario | Se cargan solo si hay acordada de la SCBA. El motor no tiene fechas fijas en el código. | 3b |
| D30 | R5 | Cuándo se perfecciona cada forma de notificación (Día Cero) | V1: el abogado carga la fecha ya perfeccionada y la forma. V1.x: la app sugiere la de la notificación electrónica y el abogado confirma. | — |
| D31 | R6 | Días hábiles administrativos (LCT, etapa previa): ¿qué es inhábil? ¿Las ferias suspenden? | Solo sábados, domingos y feriados; las ferias judiciales no suspenden. | 15, 16 |
| D32 | R7 | Meses y años (prescripción): fecha a fecha, inhábil al final, hora límite | Fecha a fecha (art. 6 CCyC); alerta por el día nominal; efectivo el hábil siguiente; límite a las 24:00; sin gracia en `LAB_015`. | 17, 18, 19 |
| D33 | R8 | Plazos en horas: ¿desde el instante o desde la hora siguiente? ¿Se trasladan? | Corridas desde el instante, sin traslado. | 20 |
| D34 | R9 | Plazos de anticipación: ¿N días libres o alcanza con el N-ésimo hábil anterior? | N días libres: el límite es un día antes. | 22, 23 |

**Preguntas que se responden junto con estas:**
- **D06** (días hábiles de la LCT y del Dec. 146/01) es la misma pregunta que la D31: una sola respuesta para las dos.
- **D04** (prescripción: cómputo único o por crédito, y gracia para la demanda del día siguiente) se responde con la D32. Por defecto, un solo cómputo desde la extinción del vínculo y sin gracia: es el más temprano.
- **D08** (cédula en papel y Día Cero de cada forma de notificación) se responde con la D30.
- **D13** (con cuánta anticipación se cita a los testigos) da el valor N de la regla R9. Hoy no hay un hito para eso en la matriz: con la respuesta, se agrega a `LAB_210` como hito o como ítem del checklist. Por defecto, el abogado lo carga como plazo suelto de anticipación.

**Lo que más importa de este bloque:** la D28. Define la hora del vencimiento en todas las tarjetas y en el email. Si el horario o la gracia son distintos a la propuesta, se cambia en `jurisdiction_schedules`, sin tocar el motor.

---

## 6. Bloque C · Hito por hito

Cambian valores o caminos de la matriz, no la estructura. En la columna "Si no se responde", el valor del borrador se mantiene solo si el abogado lo acepta como postura provisoria; si no, la versión no se firma.

### Etapa previa

| Duda | Hito | Qué hay que decidir | Borrador | Si no se responde |
| :--- | :--- | :--- | :--- | :--- |
| D03 | `LAB_040`, `LAB_015` | Si la conciliación previa es obligatoria, ante quién, con qué plazo, y si suspende la prescripción | Hito sin plazo; la norma figura "a validar" | El hito queda como recordatorio, sin plazo. La suspensión de la prescripción la ajusta el abogado a mano. |
| D05 | `LAB_030` | Plazo de cada intimación (art. 57 LCT; art. 11 Ley 24.013) y vigencia tras la Ley 27.742 | 2 días hábiles administrativos | Se mantienen los 2 días y el checklist advierte que el plazo depende del tipo de intimación. |
| D22 | `LAB_050` | Si el bono Ley 8480 y los aportes Ley 6716 se pagan, se difieren o están exentos en la demanda del trabajador | Sin dato | El checklist dice "verificar bono y aportes", sin afirmar una exención. |

### Demanda y contestación

| Duda | Hito | Qué hay que decidir | Borrador | Si no se responde |
| :--- | :--- | :--- | :--- | :--- |
| D07 | `LAB_070` | Si la ampliación por distancia aplica a la contestación y cómo se calcula | Sin ampliación | Queda como en la V1: el abogado edita el plazo con el motivo "Ampliación por distancia". El cálculo automático, en la V1.x. |
| D09 | `LAB_080`, `LAB_090` | Qué excepciones son de previo y especial pronunciamiento; si el traslado al actor es de 5 días | 5 días hábiles, con gracia | Se mantienen los 5 días. |
| D10 | `LAB_085` | Plazo para contestar la reconvención | 10 días hábiles, con gracia | Se mantienen los 10 días. |

### Prueba

| Duda | Hito | Qué hay que decidir | Borrador | Si no se responde |
| :--- | :--- | :--- | :--- | :--- |
| D11 | `LAB_105` | Qué recurso procede contra la denegatoria de prueba en instancia única y en qué plazo | Reposición, 3 días hábiles, con gracia | Se mantienen los 3 días. |
| D12 | `LAB_115` | Plazo del traslado del dictamen pericial | 5 días hábiles, con gracia | Se mantienen los 5 días. |
| D23 | `LAB_110`, `LAB_120` | Si hay plazos de negligencia o de caducidad que convenga alertar | Fuera de la V1 | Sigue fuera de la V1. Si la respuesta es sí, entra al backlog de la V1.x. |

### Sentencia y recursos

| Duda | Hito | Qué hay que decidir | Borrador | Si no se responde |
| :--- | :--- | :--- | :--- | :--- |
| D14 | `LAB_600` | Plazos del tribunal para el veredicto y la sentencia | Sin plazo | Sin alerta de demora en la V1. |
| D15 | `LAB_610`, `LAB_700` | Plazo de la aclaratoria y si suspende el del recurso extraordinario | 3 días hábiles, con gracia | Se mantienen los 3 días y el recurso corre desde la sentencia, sin suspensión: es lo más temprano. |
| D16 | `LAB_700` | Plazo del recurso, depósito previo del empleador (art. 56), exenciones y valor mínimo del agravio | 10 días hábiles, con gracia | Se mantienen los 10 días; el depósito previo va como ítem del checklist. |
| D17 | `LAB_720`, `LAB_730` | Plazos de la queja y de la memoria ante la SCBA | 5 y 10 días hábiles, con gracia | Se mantienen. |

### Ejecución, honorarios y acuerdos

| Duda | Hito | Qué hay que decidir | Borrador | Si no se responde |
| :--- | :--- | :--- | :--- | :--- |
| D18 | `LAB_800` | Quién practica la liquidación y plazo del traslado | 5 días hábiles, con gracia | Se mantienen los 5 días. |
| D19 | `LAB_810` | Si el plazo de pago lo fija la sentencia y si aplica la gracia al depósito | 10 días hábiles, sin gracia | El abogado carga el plazo que fija la sentencia; sin gracia. |
| D20 | `LAB_850` | Recurso contra la regulación de honorarios y plazo (Ley 14.967) | 5 días hábiles, con gracia | Se mantienen los 5 días. |
| D21 | `LAB_900` | A qué etapa vuelve el expediente si se deniega la homologación | Sin camino definido | El abogado usa "Retroceder etapa" hasta el hito donde estaba. |

### Citas normativas (D02)

Validar artículo por artículo las citas de `Base_Normativa`. No se hace en la reunión: se acuerda una fecha (propuesta: viernes 20/11/2026) y se marca cada fila en `Estado_Validacion`. Las citas se muestran en la ficha del expediente, así que **la versión 1 no se firma sin esta revisión**.

---

## 7. Bloque D · Casos borde

El diseño de la V1 ya está decidido (sección 4, punto 9 del análisis). Solo se confirma que es aceptable.

| Duda | Qué hay que confirmar | Cómo queda en la V1 | Si no se responde |
| :--- | :--- | :--- | :--- |
| D35 | Plazo común con varios demandados: si corre desde la última notificación y qué pasa si representamos a uno | El abogado carga el Día Cero que corresponde; la app avisa cuando hay más de un demandado | Queda así. El cálculo automático, en la V1.x. |
| D36 | Suspensión de plazos por acuerdo de partes o por resolución del tribunal: requisitos y otros casos habituales | El abogado carga el período en el expediente y la app lo trata como días inhábiles de ese expediente | Queda así. |

---

## 8. Bloque E · Cierre

1. **Firma de la versión 1.** Quién figura como validador en la planilla (`Validado por (equipo legal)` y `Fecha de validación`) y en la publicación del back-office ("Validado por el equipo legal"). Que el validador sea una persona distinta de quien carga cumple la separación de funciones (brecha B4 del [modelado de amenazas](modelado_de_amenazas_v1.md)). Propuesta de fecha: con D02 revisada, en la semana del 23/11/2026.
2. **Calendario judicial** (sección 4, punto 5 del análisis). Con la respuesta a la D29: cuál es la fuente oficial, quién avisa de una acordada extraordinaria (asueto por departamento) y si hace falta diciembre de 2026 para probar con casos reales.
3. **Documentos legales, solo si el mismo abogado los revisa** (sección 10.7 del análisis): si el abogado usuario es consumidor, el tope de responsabilidad y los plazos de conservación. Si no, se agenda otra reunión.
4. **Próxima revisión.** Cuándo se ven las respuestas por escrito del bloque C y quién avisa si una norma cambia después de firmar.

## 9. Después de la reunión

| Qué | Quién | Cuándo |
| :--- | :--- | :--- |
| Guardar una copia de la planilla tal como quedó en la reunión | Equipo | 12/11 |
| Ajustar los parámetros y los casos de prueba del motor que cambiaron (sección 4 del documento de lógica) y correr `motor_plazos_referencia.py` | Equipo | Antes del 16/11 |
| Pasar las decisiones al registro (sección 2 del análisis) y actualizar el checklist (sección 12) | Equipo | 13/11 |
| Cargar en `datos.py` los cambios de la planilla y regenerar las tablas y el diagrama, comparando celdas para no perder nada | Equipo | Después de la firma |
| Responder por escrito lo que quedó abierto del bloque C y revisar las citas (D02) | Abogado | 20/11 |
| Firmar la versión 1 de la matriz | Abogado | Semana del 23/11 |
