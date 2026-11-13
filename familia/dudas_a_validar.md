# Dudas y puntos a validar · Fuero de Familia PBA

**Estado:** borrador para validar · **Fecha:** 13/11/2026 · **Versión de las matrices:** 1 (borrador)

Este documento reúne lo que el abogado tiene que validar en las cinco matrices de familia: las dudas de la hoja `Dudas_a_validar` de cada planilla, las citas que quedaron marcadas "(a verificar)" en los hitos y las decisiones de modelado que conviene confirmar. El texto de cada duda es el mismo que el de la planilla.

| Matriz | Planilla | Hitos | Transiciones | Dudas |
| :--- | :--- | ---: | ---: | ---: |
| Alimentos | [`matriz_familia_alimentos_pba.xlsx`](matriz_familia_alimentos_pba.xlsx) | 47 | 109 | 50 |
| Divorcio | [`matriz_familia_divorcio_pba.xlsx`](matriz_familia_divorcio_pba.xlsx) | 48 | 105 | 18 |
| Cuidado personal y régimen de comunicación | [`matriz_familia_cuidado_personal_pba.xlsx`](matriz_familia_cuidado_personal_pba.xlsx) | 46 | 107 | 17 |
| Violencia familiar: medidas de protección | [`matriz_familia_violencia_pba.xlsx`](matriz_familia_violencia_pba.xlsx) | 29 | 63 | 20 |
| Adopción | [`matriz_familia_adopcion_pba.xlsx`](matriz_familia_adopcion_pba.xlsx) | 38 | 76 | 20 |

---

## 1. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal`, con la norma o la acordada que la sostiene, y `Estado` pasa a `VALIDADO` o `CORREGIR`. Si la respuesta cambia un hito, se corrige también la fila en `Nodos` o en `Transiciones`, con su `Estado_Validacion`.
- **Además de las dudas, cada fila se valida.** Hay 668 filas de hitos y transiciones con `Estado_Validacion = PENDIENTE` (156 en alimentos, 153 en divorcio, 153 en cuidado personal, 92 en violencia, 114 en adopcion). El control "filas pendientes" de la hoja `Flujo` las cuenta.
- **Las dudas compartidas se responden una sola vez, en la matriz de alimentos.** Las marcadas `[ETAPA COMÚN]` valen para la etapa contenciosa común que usan alimentos, divorcio y cuidado personal. Las marcadas `[PRODUCTO]` son para el equipo de producto y valen para las cinco. Las otras cuatro matrices terminan con una duda que remite a alimentos. Las reglas del motor se validan en las dudas D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx` y no se repiten acá.
- **Ante la duda, el vencimiento más temprano.** Es el principio del motor: cada duda trae una propuesta por defecto que cumple ese principio. Una propuesta por defecto no se da por buena hasta que el abogado la acepte por escrito.
- **No se cargan datos personales.** Ni en las respuestas ni en los ejemplos: los documentos se nombran ("partida de nacimiento del hijo"), no se transcribe su contenido.
- **No correr `generar.py` sobre una planilla una vez que el abogado empiece a completarla:** la pisa con lo que hay en `datos/` (ver [`README.md`](README.md)).

## 2. Las de mayor impacto

| Matriz y duda | Tema | Por qué primero |
| :--- | :--- | :--- |
| Alimentos D47 | Régimen procesal en el catálogo | Sin un régimen para el proceso de familia del CPCCBA, la Ley 12.569 y la Ley 14.528, ninguna de las cinco matrices se puede importar. |
| Alimentos D39 y D40 | Roles del fuero y rol representado | En familia el estudio puede representar a cualquiera de las partes o al niño; si el rol queda mal, los avisos de "te toca a vos" quedan invertidos. |
| Alimentos D43 y D46 | Expediente reservado y avisos en dispositivos compartidos | Un aviso que revele datos de una víctima o llegue a un dispositivo que comparte con la persona denunciada es un riesgo concreto para ella. |
| Alimentos D33 | Plazos en horas | Los plazos de 24, 48 y 72 horas son el camino principal de violencia y de la medida de abrigo en adopción. |
| Violencia D01 | Plazo de 48 horas para las medidas | Define desde cuándo corre el primer vencimiento del flujo. |
| Adopción D01 | Cómputo de los días | Cambia el tipo de plazo de casi todos los hitos de adopción (corridos o hábiles). |
| Divorcio D01 | Etapa previa en la petición de divorcio | Si se exige la etapa ante el Consejero, cambia la entrada del flujo. |
| Alimentos D02 | Retroactividad a la interpelación | Define el plazo para demandar sin perder cuotas. |

## 3. Alimentos (prefijo `ALI`)

### 3.1 Dudas propias de alimentos

#### D01 · Etapa previa en alimentos

Desde la Ley 15.513 la actora elige entre la etapa previa y la demanda directa (art. 828). ¿Se sigue usando la etapa previa en alimentos en la práctica? ¿Corresponde cuando el reclamo es urgente (persona por nacer)? Propuesta de la app: el abogado elige el camino en ALI_050. Fuente consultada: Ley 15.513 (B.O. 03/01/2025) en normas.gba.gob.ar.

**Hitos afectados:** ALI_050 (Elección de la vía: etapa previa o demanda directa), ALI_100 (Solicitud de trámite de la etapa previa)

#### D02 · Retroactividad a la interpelación

El art. 669 CCyC y el art. 641 CPCCBA exigen demandar dentro de los 6 meses de la interpelación. ¿Alcanza con iniciar la etapa previa dentro de ese plazo? ¿Los 6 meses se cuentan desde la recepción de la carta documento? Propuesta de la app: 6 meses desde la recepción, y solo la demanda cumple el plazo (es lo más temprano). Fuente consultada: art. 669 CCyC en leyes-ar.com.

**Hitos afectados:** ALI_020 (Interpelación fehaciente al alimentante), ALI_030 (Plazo para demandar con efecto retroactivo a la interpelación)

#### D03 · Alimentos provisorios

El art. 636 bis obliga a fijar los provisorios en el primer auto o dentro de 5 días si se piden después. ¿Son 5 días hábiles judiciales desde el pedido? ¿La resolución que fija los provisorios es apelable y con qué efecto? Propuesta de la app: plazo suelto de 5 días hábiles judiciales desde el pedido, y apelación con efecto devolutivo.

**Hitos afectados:** ALI_140 (Primer auto: audiencia y alimentos provisorios)

#### D04 · Audiencia del art. 636

La audiencia se fija 'dentro de un plazo que no podrá exceder de diez días, contado desde la fecha de presentación de la demanda'. ¿Son hábiles judiciales? ¿Conviene un hito con ese plazo para alertar demoras del juzgado? Propuesta de la app: no; queda en el checklist del primer auto.

**Hitos afectados:** ALI_140 (Primer auto: audiencia y alimentos provisorios), ALI_150 (Audiencia del juicio de alimentos)

#### D05 · Multa por incomparecencia

La multa del art. 637 inc. 1 se deposita 'dentro del tercer día'. ¿Son hábiles judiciales desde la notificación de la providencia? ¿Admite plazo de gracia aunque sea un pago? Propuesta de la app: 3 días hábiles judiciales, sin gracia (es lo más temprano).

**Hitos afectados:** ALI_160 (Multa y nueva audiencia por incomparecencia del alimentante)

#### D06 · Plazo de la sentencia de alimentos

El juez debe dictar sentencia dentro de 5 días 'contados desde que se encuentre producida la prueba ofrecida por la parte actora' (art. 641). ¿Desde qué acto lo cuenta el abogado (agregación del último informe, providencia de autos)? Propuesta de la app: 5 días hábiles judiciales desde la agregación de la última prueba de la actora, solo como alerta.

**Hitos afectados:** ALI_180 (Sentencia de alimentos)

#### D07 · Intimación de pago de cuotas

Art. 645: si dentro del quinto día de intimado el alimentante no paga, se embarga. ¿Son 5 días hábiles judiciales desde la notificación de la intimación? Propuesta de la app: sí, sin gracia porque es un pago.

**Hitos afectados:** ALI_730 (Intimación de pago de cuotas atrasadas)

#### D08 · Notificación por mensajería instantánea

El art. 635 bis permite notificar por mensajería instantánea y la diligencia se acredita con un acta del actuario. ¿Qué fecha toma la app como Día Cero: el envío, la confirmación de lectura o el acta? ¿La SCBA reglamentó el procedimiento? Propuesta de la app: la fecha del acta.

**Hitos afectados:** ALI_130 (Demanda de alimentos), ALI_140 (Primer auto: audiencia y alimentos provisorios)

#### D09 · Oficios en alimentos

En alimentos los oficios se contestan en 7 días hábiles (oficinas públicas) y 5 (privadas), según el art. 396 (texto Ley 15.513). ¿Conviene un hito por oficio o alcanza con plazos sueltos? Propuesta de la app: plazos sueltos.

**Hitos afectados:** ALI_170 (Prueba del juicio de alimentos (informes))

#### D10 · Hijo de 21 a 25 años

¿El cese a los 21 años es automático o requiere pedido del alimentante (art. 658)? ¿La extensión hasta los 25 (art. 663) se pide por incidente en el mismo expediente? Propuesta de la app: alertar los 21 años desde la fecha de nacimiento y que el abogado decida.

**Hitos afectados:** ALI_760 (Control de los 21 años del hijo alimentado), ALI_800 (Incidente de aumento, reducción, cese o coparticipación)

#### D11 · Caducidad de la compensación en el divorcio

Art. 442: la acción 'caduca a los seis meses de haberse dictado la sentencia de divorcio'. ¿Se cuenta desde el dictado, la notificación o la firmeza? ¿La solicitud de la etapa previa impide la caducidad (art. 2569 CCyC) o hace falta la demanda? Propuesta de la app: desde el dictado y solo la demanda la impide (es lo más temprano); si falta poco, pedir la radicación directa. Fuente consultada: art. 442 CCyC en leyes-ar.com.

**Hitos afectados:** ALI_040 (Control de caducidad de la compensación económica), ALI_100 (Solicitud de trámite de la etapa previa), ALI_200 (Demanda de compensación económica)

#### D12 · Caducidad de la compensación entre convivientes

Art. 525: caduca a los 6 meses de cualquiera de las causas de cese del art. 523. ¿Cómo se acredita la fecha de cese cuando la unión no estaba inscripta? Propuesta de la app: el abogado carga la fecha que pueda probar y el checklist lo advierte.

**Hitos afectados:** ALI_040 (Control de caducidad de la compensación económica)

#### D13 · Proceso de la compensación económica

¿La compensación económica tramita por el plenario abreviado del art. 838 o por el juicio de alimentos? ¿Se puede acumular a la demanda de alimentos o a las cuestiones del divorcio? Propuesta de la app: plenario abreviado, por separado.

**Hitos afectados:** ALI_200 (Demanda de compensación económica) a ALI_500 (Sentencia sobre la compensación económica)

#### D14 · Alimentos entre cónyuges y convivientes

El art. 646 (texto Ley 15.513) extiende el trámite a la asistencia entre cónyuges. ¿Los alimentos entre convivientes (art. 519) y los posteriores al divorcio (art. 434) siguen el mismo juicio de alimentos? Propuesta de la app: sí.

**Hitos afectados:** ALI_010 (Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes), ALI_130 (Demanda de alimentos)

#### D15 · Registro de Deudores Alimentarios Morosos

¿Cuántas cuotas impagas exige la Ley 13.074 para inscribir al deudor? ¿El juez lo ordena de oficio después de la Ley 15.513 (arts. 636 bis y 645)? ¿Qué efectos tiene la inscripción? Propuesta de la app: solo un ítem del checklist.

**Hitos afectados:** ALI_140 (Primer auto: audiencia y alimentos provisorios), ALI_740 (Ejecución de cuotas atrasadas)

#### D16 · Medidas ante el incumplimiento reiterado

¿Qué medidas razonables del art. 553 CCyC admite la jurisprudencia de la SCBA y de las Cámaras de la provincia (por ejemplo, restricciones a la licencia de conducir o a la salida del país)? Propuesta de la app: el checklist no nombra medidas concretas hasta que el equipo legal las valide.

**Hitos afectados:** ALI_740 (Ejecución de cuotas atrasadas)

#### D17 · Responsabilidad del empleador

¿La responsabilidad solidaria del empleador que no deposita (art. 551) se reclama en el mismo expediente de alimentos o en uno aparte? Propuesta de la app: en el mismo.

**Hitos afectados:** ALI_750 (Empleador que no retiene o no deposita la cuota)

#### D18 · Efecto de la apelación

La apelación de la sentencia que admite alimentos tiene efecto devolutivo (art. 644 CPCCBA, art. 547 CCyC). ¿Qué efecto tiene la que los rechaza y la del incidente de reducción o cese? Propuesta de la app: el checklist del recurso lo indica y la cuota sigue en ALI_720 mientras se apela.

**Hitos afectados:** ALI_600 (Recurso de apelación), ALI_720 (Pago de la cuota alimentaria), ALI_820 (Resolución del incidente de cuota)

#### D19 · Trámite de los incidentes

El incidente de aumento, reducción o cese (art. 647) ¿sigue el trámite de los arts. 180 a 183, con traslado de 5 días y audiencia dentro de 10? ¿Corresponde la etapa previa antes del incidente? Propuesta de la app: incidente sin etapa previa, traslado de 5 días hábiles judiciales.

**Hitos afectados:** ALI_800 (Incidente de aumento, reducción, cese o coparticipación), ALI_810 (Contestación del incidente), ALI_820 (Resolución del incidente de cuota)

#### D20 · Alimentos y violencia

Cuando hay violencia, ¿se fija la cuota provisoria como medida de protección (art. 7 inc. g Ley 12.569) y después se sigue en esta matriz? Propuesta de la app: la matriz de violencia deriva a esta, y el checklist de la audiencia advierte que se pidan audiencias separadas.

**Hitos afectados:** ALI_010 (Necesidad alimentaria o reclamo patrimonial entre ex cónyuges o ex convivientes), ALI_150 (Audiencia del juicio de alimentos)

### 3.2 Etapa común del proceso de familia

Valen también para divorcio y cuidado personal, que usan la misma etapa contenciosa.

#### D21 · [ETAPA COMÚN] Etapa previa ante el Consejero

El art. 835 CPCCBA dice que la etapa previa es 'previa e imprescindible' para las materias del art. 827, salvo urgencia, y la Ley 15.513 la hizo optativa solo en alimentos (art. 828, último párrafo). ¿En qué materias se exige hoy en la práctica de cada departamento (cuidado personal, régimen de comunicación, compensación económica, cuestiones del divorcio)? ¿Cuántas audiencias suele haber y cuánto dura? Propuesta de la app: la etapa previa es el camino por defecto y la radicación directa es una salida del primer hito. Fuente consultada: texto de los arts. 828 a 837 en leyes-ar.com (actualizado al 16/10/2026) y Ley 15.513 (B.O. 03/01/2025).

**Hitos afectados:** ALI_100 (Solicitud de trámite de la etapa previa), ALI_110 (Audiencias ante el Consejero de Familia), ALI_120 (Acta de cierre de la etapa previa)

#### D22 · [ETAPA COMÚN] Tipo de proceso y plazos

El art. 838 remite al proceso plenario abreviado (sumario) y permite al juez cambiarlo. Confirmar los plazos que usa la matriz: contestación y reconvención 10 días (arts. 484 y 485), ampliación de prueba 5 días (art. 484), audiencia preliminar dentro de 10 días (art. 842), todos en días hábiles judiciales. ¿Qué materias tramitan como sumarísimo (art. 496: contestación en 5 días)? Propuesta de la app: los plazos del sumario, editables por expediente.

**Hitos afectados:** ALI_220 (Providencia inicial y traslado de la demanda), ALI_240 (Contestación de la demanda), ALI_300 (Audiencia preliminar)

#### D23 · [ETAPA COMÚN] Mediación previa

La Ley 13.951 (art. 4 inc. 2) excluye de la mediación obligatoria el divorcio, la nulidad de matrimonio, la filiación y la patria potestad, los alimentos, las guardas y las adopciones. ¿El régimen de comunicación, la compensación económica, la atribución de la vivienda y la liquidación de la comunidad también quedan fuera? Propuesta de la app: en familia no hay mediación previa; la etapa previa es la del Consejero. Fuente consultada: texto de la Ley 13.951 en normas.gba.gob.ar.

**Hitos afectados:** ALI_100 (Solicitud de trámite de la etapa previa), ALI_200 (Demanda de compensación económica)

#### D24 · [ETAPA COMÚN] Juzgados de Paz

El art. 828 permite optar por los Juzgados de Paz y remite a sus procedimientos. ¿En qué materias de familia son competentes los Juzgados de Paz Letrados (art. 61 Ley 5827, a verificar: alimentos, régimen de comunicación, violencia, divorcio por presentación conjunta) y sus plazos son los mismos? Propuesta de la app: la misma matriz sirve para el Juzgado de Paz, sin la etapa previa ante el Consejero.

**Hitos afectados:** ALI_100 (Solicitud de trámite de la etapa previa), ALI_200 (Demanda de compensación económica)

#### D25 · [ETAPA COMÚN] Prueba previa a la vista de causa

Los arts. 844, 846 y 848 exigen que pericias, informes y prueba previa estén agregados 10 días antes de la vista de causa. ¿Son días hábiles judiciales contados hacia atrás? ¿Tienen que quedar 10 días libres (regla R9 de la matriz general, D34)? Propuesta de la app: 10 días hábiles judiciales libres antes de la audiencia (es lo más temprano).

**Hitos afectados:** ALI_330 (Asesoría Pericial: pericia contable o de tasación)

#### D26 · [ETAPA COMÚN] Plazo para dictar sentencia

¿Qué plazo tiene el juez de familia para dictar sentencia después de la vista de causa (art. 494: 30 días, u otro del Libro VIII)? Sirve solo para alertar demoras. Propuesta de la app: sin plazo; el abogado puede cargar uno suelto.

**Hitos afectados:** ALI_500 (Sentencia sobre la compensación económica)

#### D27 · [ETAPA COMÚN] Apelación y su efecto

Confirmar: apelación en 5 días (art. 244), fundamentación en 5 días (expresión de agravios en el sumario, art. 254, o memorial en relación, art. 246) y contestación de agravios (¿plazo?). ¿La Sala de Familia del art. 852 existe en todos los departamentos? ¿Qué efecto tiene la apelación en cuidado personal y régimen de comunicación (la regla del art. 243 es suspensiva)? Propuesta de la app: 5 + 5 días hábiles judiciales con gracia; el efecto se anota en el checklist.

**Hitos afectados:** ALI_600 (Recurso de apelación), ALI_610 (Fundamentación de la apelación (expresión de agravios o memorial))

#### D28 · [ETAPA COMÚN] Queja por apelación denegada

La matriz no tiene un hito para la queja ante la Cámara cuando se deniega la apelación (art. 275 CPCCBA, a verificar). ¿Qué plazo tiene? ¿Conviene agregar el hito? Propuesta de la app: plazo suelto de 5 días hábiles judiciales desde la denegatoria (a confirmar).

**Hitos afectados:** ALI_600 (Recurso de apelación)

#### D29 · [ETAPA COMÚN] Caducidad de instancia

¿Rige la caducidad de instancia (arts. 310 a 316) en los procesos de familia: alimentos, cuidado personal, cuestiones del divorcio, compensación económica? ¿El plazo es de 3 meses por ser sumario (art. 310 inc. 3)? La intimación previa del art. 315 es de 5 días. Propuesta de la app: control de 3 meses desde el último acto de impulso, que el abogado reinicia con cada acto.

**Hitos afectados:** Los mismos hitos de las otras matrices de familia

#### D30 · [ETAPA COMÚN] Asesoría de Incapaces

¿En qué momentos hay que dar vista a la Asesoría de Incapaces (demanda, acuerdos, prueba, antes de la sentencia) y qué artículo de la Ley 14.442 fija su intervención en familia? La falta de intervención causa la nulidad relativa (art. 103 CCyC). Propuesta de la app: vista antes de la sentencia y de cada homologación, como hitos del juzgado.

**Hitos afectados:** ALI_200 (Demanda de compensación económica), ALI_490 (Asesoría de Incapaces: vista previa a la sentencia), ALI_900 (Acuerdo y homologación)

#### D31 · [ETAPA COMÚN] Abogado del niño

Ley 14.568: ¿desde qué edad se informa al niño su derecho a un abogado del niño? ¿Cómo se pide la designación en cada departamento (Registro Provincial del Colegio de Abogados)? ¿Es obligatorio en cuidado personal, como lo hizo la Ley 15.610 en adopción (art. 6 Ley 14.528)? Fuente consultada: texto de la Ley 14.568 en normas.gba.gob.ar.

**Hitos afectados:** Los mismos hitos de las otras matrices de familia

#### D32 · [ETAPA COMÚN] Feria judicial

¿Qué plazos de familia se suspenden durante las ferias de enero y de invierno, y cuáles corren porque el juez habilitó días y horas (art. 153 CPCCBA; art. 4 Ley 14.528 en adopción; art. 637 en alimentos)? La SCBA fija juzgados de familia de turno para lo urgente (Acuerdos 4213 y 4214 de 2025 para 2026). Propuesta de la app: la feria suspende todos los plazos en días hábiles judiciales, salvo que el expediente tenga cargada una habilitación (ver la duda de producto sobre habilitación). Fuente consultada: Acuerdo SCBA 4214/25.

**Hitos afectados:** Todos los de días hábiles judiciales

#### D33 · [ETAPA COMÚN] Plazos en horas

Los plazos de 24, 48 y 72 horas de familia (Consejero, art. 831; medidas de protección, art. 7 Ley 12.569; control de legalidad, art. 35 bis Ley 13.298; comunicaciones de la Ley 14.528) ¿corren en días inhábiles, feriados y feria? La regla R8 de la matriz general (D33) propone horas corridas desde el instante, sin traslado. Propuesta de la app: la misma regla, que es la más temprana; en familia tiene sentido porque son plazos para el juzgado o un organismo en situaciones urgentes.

**Hitos afectados:** Todos los de horas

#### D34 · [ETAPA COMÚN] Plazo de gracia

¿Qué plazos de familia admiten el plazo de gracia del art. 124 CPCCBA (hasta las 12:00 del hábil siguiente)? Propuesta de la app: solo los escritos de parte en días hábiles judiciales; sin gracia en los plazos del juzgado y de organismos, en los pagos (multas, depósitos), en las caducidades y en los plazos en horas.

**Hitos afectados:** Todos

#### D35 · [ETAPA COMÚN] Notificaciones electrónicas

Reglamento del Acuerdo SCBA 4013 (texto ordenado Ac. 4039): la notificación se perfecciona el martes o viernes posterior a quedar disponible, o en el momento en que queda disponible si el juez la declara urgente (art. 13). ¿Qué resoluciones de familia suelen notificarse como urgentes? El traslado de la demanda queda diferido hasta que se pida (art. 11 inc. c). Propuesta de la app: el abogado carga la fecha ya perfeccionada (como en la D30 de la matriz general). Fuente consultada: digesto de la SCBA.

**Hitos afectados:** ALI_220 (Providencia inicial y traslado de la demanda), ALI_240 (Contestación de la demanda) todos los que empiezan con una notificación

#### D36 · [ETAPA COMÚN] Tasa de justicia, bono y aportes

Código Fiscal: exentos el actor en alimentos (art. 330 inc. 7), las actuaciones de familia sin carácter patrimonial, la adopción y la tenencia (art. 343 inc. 5) y los alimentos con cuotas bajas (art. 343 inc. 10). El divorcio tiene una tasa propia en la Ley Impositiva del año, mayor si se liquida la comunidad (a verificar con la Ley Impositiva vigente). ¿El bono Ley 8480 y los aportes Ley 6716 se pagan en alimentos, violencia y adopción? Propuesta de la app: solo un ítem del checklist, sin montos. Fuente consultada: arts. 330 y 343 del Código Fiscal en leyes-ar.com.

**Hitos afectados:** ALI_200 (Demanda de compensación económica)

#### D37 · [ETAPA COMÚN] Honorarios

Ley 14.967: mínimos por proceso de familia en el art. 9 (divorcio 40 Jus, violencia 20, cuidado personal y régimen de comunicación 45, adopción 40, entre otros), base de dos años en alimentos (art. 39) y apelación en 5 días (art. 57). ¿La etapa previa se regula como una etapa del proceso? ¿Qué plazo tiene la Cámara para resolver (art. 57: 10 días)? Propuesta de la app: un hito de apelación de honorarios de 5 días hábiles judiciales con gracia. Fuente consultada: texto de la Ley 14.967 en normas.gba.gob.ar.

**Hitos afectados:** ALI_520 (Apelación de la regulación de honorarios)

#### D38 · [ETAPA COMÚN] Vigencia del régimen procesal

Al 13/11/2026 sigue vigente el Decreto-Ley 7425/68 con reformas parciales: no hay un código procesal de familia nuevo (hubo un proyecto de reforma integral en 2025, sin sanción conocida). ¿Hay reformas posteriores a la Ley 15.513 (2025) y a la Ley 15.610 (2026) que cambien estos plazos? Propuesta de la app: la matriz se versiona; una reforma genera una versión nueva. Fuente consultada: normas.gba.gob.ar y legislativa.senado-ba.gov.ar.

**Hitos afectados:** Todos

### 3.3 Producto

Para el equipo de producto. No cambian el contrato de API ni el modelo de datos: registran lo que habría que decidir. Las que tocan datos sensibles piden registrar la amenaza en `modelado_de_amenazas_v1.md` y revisar la política de privacidad; esos documentos no se modificaron.

#### D39 · [PRODUCTO] Roles del fuero

[PRODUCTO] El rol responsable es un enum cerrado (ACTORA, DEMANDADA, TRIBUNAL, AMBAS). En familia actúan además el niño (con o sin abogado del niño), el Ministerio Público (Asesoría de Incapaces) y organismos (Servicio Local o Zonal, equipo técnico, Registro de aspirantes, comisaría). Hoy se nombran en el hito y quedan como TRIBUNAL. ¿Hacen falta roles propios (por ejemplo NNA, MINISTERIO_PUBLICO u ORGANISMO), o alcanza con el nombre del hito? Propuesta: no ampliar el enum en la V1.

**Hitos afectados:** Todos

#### D40 · [PRODUCTO] Rol representado

[PRODUCTO] legal_cases.represented_role admite ACTORA o DEMANDADA. En violencia el abogado puede representar a la persona denunciada (DEMANDADA) y en adopción a los progenitores de origen (DEMANDADA, aunque consientan la adopción). En la petición conjunta de divorcio representa a los dos cónyuges (AMBAS). ¿Cómo se carga el rol representado en esos casos y cómo cambia la vista 'paso propio, de la contraparte o del juzgado'?

**Hitos afectados:** Todos

#### D41 · [PRODUCTO] Flujo prejudicial y judicial

[PRODUCTO] Las matrices marcan con la fase 'Previa' lo que pasa antes de promover (partidas, intimación, denuncia policial, inscripción en el registro de aspirantes). La etapa ante el Consejero de Familia ya está radicada en un juzgado, así que se propone dejarla en el flujo judicial. Las medidas de abrigo del Servicio Local son administrativas pero con control judicial inmediato: se propone dejarlas en el judicial. ¿Es correcto? ¿Qué régimen procesal tiene un expediente que empieza en la comisaría (violencia)?

**Hitos afectados:** Hitos de la fase Previa; ADO_100 (Comunicación de la medida de abrigo al juez) a ADO_130 (Búsqueda de la familia de origen); VIO_030 (Denuncia) a VIO_050 (Plazo del juez para resolver las medidas urgentes)

#### D42 · [PRODUCTO] Derivación entre matrices

[PRODUCTO] Cuando un flujo sigue en otro (divorcio hacia compensación económica o alimentos, violencia hacia alimentos o cuidado personal, cuidado personal hacia alimentos), la matriz termina en un hito final 'Sigue en la matriz de ...'. ¿Cómo se crea y se vincula el expediente nuevo (mismo cliente, misma carátula de origen, plazos ya corriendo como la caducidad de la compensación)? ¿Un hito final en un camino paralelo cierra todo el expediente o solo ese camino? Propuesta: la app ofrece crear el expediente vinculado y el hito final cierra solo su camino si quedan otros abiertos.

**Hitos afectados:** Hitos 'Sigue en la matriz de ...'

#### D43 · [PRODUCTO] Expediente reservado

[PRODUCTO] El expediente de familia tiene acceso limitado a las partes y sus letrados (art. 708 CCyC) y en adopción es reservado (art. 617 inc. e CCyC). ¿Cómo se marca un expediente reservado en la app? ¿Qué cambia: quién lo ve dentro del estudio, si aparece la carátula en el dashboard, en el resumen diario y en las exportaciones? Propuesta: todo expediente del fuero de familia es reservado por defecto. Relacionarlo con el activo A1 y la amenaza JOB-02 de modelado_de_amenazas_v1.md.

**Hitos afectados:** Todos

#### D44 · [PRODUCTO] Datos de niños y víctimas

[PRODUCTO] ¿Qué datos de niños, niñas y adolescentes y de víctimas se guardan (por ejemplo, la fecha de nacimiento del hijo para el control de los 21 años en alimentos, la fecha y hora de la denuncia en violencia) y quién los ve dentro del estudio? Propuesta: solo las fechas que el motor necesita, sin nombres ni relato de hechos, y visibles solo para los miembros asignados al expediente. La política de privacidad hoy no menciona datos de terceros de esta sensibilidad.

**Hitos afectados:** ALI_760 (Control de los 21 años del hijo alimentado) y todos los de violencia y adopción

#### D45 · [PRODUCTO] Datos de salud

[PRODUCTO] Pericias psicológicas y psiquiátricas, informes del equipo interdisciplinario, historia clínica y certificados médicos son datos sensibles (Ley 25.326). La V1 no guarda adjuntos ni notas, pero el abogado puede escribirlos en campos libres (motivos, plazos sueltos). ¿Alcanza con el aviso que ya prevé el análisis (sección de datos sensibles) o hace falta algo más para el fuero de familia? Es la misma pregunta que la D14 de la matriz de accidentes de trabajo.

**Hitos afectados:** CUI_330 (Equipo técnico: pericia psicológica o psiquiátrica), CUI_340 (Equipo técnico: informe socioambiental), VIO_130 (Informe interdisciplinario de riesgo), ADO_240 (Estudios psicológicos, de salud y socioambientales) y todos los informes de equipos técnicos

#### D46 · [PRODUCTO] Avisos y dispositivos compartidos

[PRODUCTO] Un recordatorio por email o push no puede revelar datos de una víctima ni llegar a un dispositivo o cuenta que comparte con la persona denunciada. Hoy el resumen diario trae solo cantidades y números de expediente salvo que el usuario active la carátula (JOB-02). ¿Hace falta un modo discreto por expediente (sin carátula, sin nombre del hito, sin fuero) y bloquear la activación de la carátula en expedientes de violencia? Registrarlo como amenaza nueva en modelado_de_amenazas_v1.md y revisar la política de privacidad; no se modificaron esos documentos.

**Hitos afectados:** Todos; en especial violencia

#### D47 · [PRODUCTO] Régimen procesal en el catálogo

[PRODUCTO] procedural_regimes tiene hoy PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057 (y el sucesorio pidió uno civil). Para familia haría falta al menos uno (por ejemplo, el Libro VIII del CPCCBA), y quizá aparte la Ley 12.569 para violencia y la Ley 14.528 para adopción, que tienen procedimiento propio. courts.court_type tampoco tiene Juzgado de Familia ni Juzgado de Paz. ¿Uno para los cinco flujos o uno por régimen? No se modificaron el contrato de API ni el modelo de datos.

**Hitos afectados:** Todos

#### D48 · [PRODUCTO] Expediente que empieza en un hito intermedio

[PRODUCTO] Si el abogado representa al denunciado en violencia, el expediente empieza en la notificación de las medidas; si representa a postulantes convocados para una guarda, empieza en la selección. ¿La app permite crear el expediente en un hito que no es el inicial? Propuesta: sí, eligiendo el hito actual al crear el expediente.

**Hitos afectados:** VIO_070 (Notificación de las medidas a la persona denunciada), ADO_300 (Selección de los postulantes), ADO_400 (Demanda de adopción)

#### D49 · [PRODUCTO] Plazos que se reinician y plazos mínimos

[PRODUCTO] La caducidad de instancia vuelve a correr con cada acto de impulso (se modeló como una transición del hito a sí mismo) y algunos plazos son mínimos, no máximos (la manifestación de los progenitores en adopción solo vale después de 45 días del nacimiento). En violencia, además, la apelación se abre con cada resolución apelable y puede volver a abrirse mientras sigue abierta. El motor calcula vencimientos. ¿Se aceptan estas soluciones (hito que vuelve sobre sí, un ítem del checklist para los mínimos y un plazo suelto para el segundo plazo del mismo hito)?

**Hitos afectados:** CUI_950 (Control de caducidad de instancia), DIV_950 (Control de caducidad de instancia), ADO_200 (Manifestación de los progenitores de autorizar la adopción), VIO_200 (Apelación de la resolución sobre las medidas o las sanciones)

#### D50 · [PRODUCTO] Habilitación de días y horas por expediente

[PRODUCTO] En adopción el juez puede habilitar días y horas inhábiles (art. 4 Ley 14.528) y en violencia y alimentos es habitual. Con habilitación, los días inhábiles cuentan para ese expediente. Hoy el motor solo permite agregar inhábiles (suspensiones), no quitarlos. ¿Hace falta una marca de 'habilitación' por expediente o por plazo?

**Hitos afectados:** Todos los de violencia y adopción

## 4. Divorcio (prefijo `DIV`)

### D01 · Etapa previa en la petición de divorcio

El divorcio es materia del art. 827 inc. a CPCCBA y el art. 835 hace 'previa e imprescindible' la etapa ante el Consejero, pero el art. 438 CCyC da a la petición un trámite propio (propuesta, audiencia y sentencia) y el art. 838 exceptúa los procesos con trámite especial. ¿La petición de divorcio se radica directamente ante el juez en todos los departamentos? Propuesta de la app: radicación directa; la etapa previa se usa solo para las cuestiones pendientes. Fuente consultada: arts. 827, 828 y 838 CPCCBA en leyes-ar.com (actualizado al 16/10/2026) y art. 438 CCyC.

**Hitos afectados:** DIV_140 (Petición unilateral de divorcio con propuesta reguladora), DIV_150 (Petición conjunta de divorcio con convenio regulador), DIV_100 (Solicitud de trámite de la etapa previa)

### D02 · Plazo de la contrapropuesta

El art. 438 CCyC permite al otro cónyuge ofrecer una propuesta distinta, pero no fija el plazo. ¿Rige el plazo general de 5 días para contestar traslados (art. 150 CPCCBA) o el que fije el juez en la providencia? ¿Se cuentan desde la notificación en el domicilio real? Propuesta de la app: 5 días hábiles judiciales con gracia desde la notificación (es lo más temprano), editables si el juez fija otro. Fuente consultada: art. 150 CPCCBA en leyes-ar.com.

**Hitos afectados:** DIV_170 (Contrapropuesta reguladora del otro cónyuge)

### D03 · Audiencia del art. 438

¿La comparecencia de los cónyuges es personal? ¿Qué pasa si el otro cónyuge no comparece: se dicta la sentencia igual, se fija otra audiencia? ¿Hay un plazo para fijarla? Propuesta de la app: la incomparecencia no impide la sentencia (el desacuerdo no la suspende, art. 438) y la audiencia diferida vuelve al mismo hito.

**Hitos afectados:** DIV_180 (Audiencia del art. 438 CCyC), DIV_190 (Sentencia de divorcio)

### D04 · Apelación de la sentencia de divorcio

Como el divorcio no requiere causa y el desacuerdo no lo suspende, ¿qué puede apelarse de la sentencia (la homologación o el rechazo del convenio, las costas, cuestiones formales)? ¿En qué efecto? ¿Desde cuándo está firme para inscribirla? Propuesta de la app: apelación en 5 días hábiles judiciales con gracia por la etapa común, y la inscripción se pide recién con la sentencia firme.

**Hitos afectados:** DIV_190 (Sentencia de divorcio), DIV_600 (Recurso de apelación), DIV_700 (Sentencia firme: inscripción del divorcio o cumplimiento de lo resuelto), DIV_810 (Inscripción de la sentencia de divorcio en el Registro de las Personas)

### D05 · Inscripción de la sentencia

¿Qué artículo de la Ley 26.413 rige la inscripción marginal del divorcio? ¿El juzgado libra el oficio de oficio o lo pide la parte? Si el matrimonio se celebró en otra provincia o en el extranjero, ¿cómo se comunica (oficio entre jurisdicciones, exhorto o vía consular)? Propuesta de la app: hito sin plazo a cargo de la parte, cerrado con la constancia de inscripción.

**Hitos afectados:** DIV_810 (Inscripción de la sentencia de divorcio en el Registro de las Personas), DIV_020 (Matrimonio celebrado en el extranjero: jurisdicción y ley aplicable)

### D06 · Matrimonio celebrado en el extranjero

Arts. 2621 y 2626 CCyC: jurisdicción del último domicilio conyugal efectivo o del domicilio del demandado, y ley del último domicilio de los cónyuges. ¿Qué requisitos de legalización, apostilla y traducción exige el juzgado? ¿Hace falta inscribir antes el matrimonio extranjero en el Registro provincial? Propuesta de la app: un hito previo sin plazo con esos controles en el checklist. Fuente consultada: arts. 2621 y 2626 CCyC en leyes-ar.com.

**Hitos afectados:** DIV_020 (Matrimonio celebrado en el extranjero: jurisdicción y ley aplicable)

### D07 · Medidas provisionales antes de la petición

El art. 722 CCyC exige que la decisión que acoge las medidas sobre los bienes fije un plazo de duración. ¿Se aplica además la caducidad de 10 días del art. 207 CPCCBA a las medidas trabadas antes de la petición? ¿Rige también para las medidas sobre las personas del art. 721? Propuesta de la app: 10 días hábiles judiciales desde la traba, sin gracia (es lo más temprano), y el plazo de duración del art. 722 como plazo suelto. Fuente consultada: arts. 721 y 722 CCyC y art. 207 CPCCBA en leyes-ar.com.

**Hitos afectados:** DIV_040 (Medidas provisionales urgentes antes de la petición), DIV_050 (Plazo para presentar la petición después de trabadas las medidas)

### D08 · Procedimiento de las cuestiones pendientes

El art. 438 CCyC remite al 'procedimiento previsto en la ley local'. En la provincia, ¿las cuestiones pendientes tramitan por el plenario abreviado del art. 838 CPCCBA con etapa previa? ¿En el mismo expediente del divorcio (como incidente) o en uno conexo ante el mismo juzgado? Propuesta de la app: proceso conexo, con etapa previa y luego la etapa contenciosa común.

**Hitos afectados:** DIV_830 (Cuestiones pendientes del convenio regulador), DIV_100 (Solicitud de trámite de la etapa previa), DIV_200 (Demanda sobre las cuestiones pendientes del divorcio (vivienda o bienes))

### D09 · Trámite de la liquidación de la comunidad

El art. 500 CCyC remite a la forma de la partición de las herencias. ¿Qué artículos del CPCCBA se aplican a la partición de la comunidad (inventario, avalúo, partidor)? ¿Conviene reusar los hitos de la fase Partición de la matriz sucesoria (SUC_600 a SUC_620 de matriz_flujo_sucesorio_pba.xlsx) en lugar del sumario? Propuesta de la app: por ahora pasa por la etapa contenciosa común; el equipo legal decide si se agrega una fase de partición propia.

**Hitos afectados:** DIV_850 (Liquidación y partición de la comunidad), DIV_200 (Demanda sobre las cuestiones pendientes del divorcio (vivienda o bienes))

### D10 · Extinción retroactiva de la comunidad

La comunidad se extingue con efecto retroactivo a la notificación de la petición unilateral o a la presentación conjunta, o a la separación de hecho anterior (art. 480 CCyC). ¿La app debe pedir y guardar esa fecha en el expediente o alcanza con el checklist? Propuesta de la app: solo el checklist en la V1. Fuente consultada: art. 480 CCyC en leyes-ar.com.

**Hitos afectados:** DIV_160 (Providencia inicial y traslado de la propuesta reguladora), DIV_190 (Sentencia de divorcio), DIV_850 (Liquidación y partición de la comunidad)

### D11 · Atribución de la vivienda

El juez fija el plazo de la atribución (art. 443 CCyC) y la decisión produce efectos frente a terceros desde su inscripción (art. 444). ¿Conviene un hito con el plazo fijado por el juez o alcanza con un plazo suelto? ¿Cómo se pide el cese (art. 445): incidente o nuevo proceso? Propuesta de la app: plazo suelto y el cese por la etapa común. Fuente consultada: arts. 443 a 445 CCyC en leyes-ar.com.

**Hitos afectados:** DIV_840 (Vigencia de la atribución del uso de la vivienda familiar)

### D12 · Revisión del convenio regulador

El convenio homologado o la decisión judicial pueden revisarse si la situación cambió sustancialmente (art. 440 CCyC). ¿La revisión pasa por la etapa previa ante el Consejero o va por incidente en el mismo expediente? Propuesta de la app: vuelve a la etapa previa.

**Hitos afectados:** DIV_910 (Cumplimiento del acuerdo homologado), DIV_100 (Solicitud de trámite de la etapa previa)

### D13 · Garantías para aprobar el convenio

El juez puede exigir garantías reales o personales para aprobar el convenio (art. 440). ¿Lo hace en la sentencia o antes, con un plazo para ofrecerlas? Propuesta de la app: ítem del checklist de la sentencia; si el juez fija un plazo, se carga como plazo suelto.

**Hitos afectados:** DIV_190 (Sentencia de divorcio)

### D14 · Un letrado para los dos cónyuges

En la petición conjunta, ¿pueden los dos cónyuges tener el mismo letrado patrocinante o cada uno necesita el suyo? ¿Cambia si hay hijos o bienes? Relacionarlo con la duda de producto sobre el rol representado (AMBAS). Propuesta de la app: se admite un letrado común y el checklist lo advierte.

**Hitos afectados:** DIV_150 (Petición conjunta de divorcio con convenio regulador)

### D15 · Asesoría de Incapaces en el divorcio

¿En qué momento interviene la Asesoría de Incapaces en la petición de divorcio con hijos menores de edad: en la providencia inicial, antes de la audiencia o antes de homologar el convenio? Propuesta de la app: vista antes de homologar, como ítem del checklist de la sentencia y de la providencia inicial.

**Hitos afectados:** DIV_160 (Providencia inicial y traslado de la propuesta reguladora), DIV_190 (Sentencia de divorcio)

### D16 · Divorcio y violencia

Si hay violencia en el grupo familiar, ¿se hace igual la audiencia del art. 438 o el juez la reemplaza por entrevistas separadas? La Ley 12.569 prohíbe la mediación y la conciliación en esos casos (art. 11). Propuesta de la app: el checklist advierte que se pidan audiencias separadas y se abre en paralelo la matriz de violencia.

**Hitos afectados:** DIV_010 (Consulta sobre el divorcio), DIV_180 (Audiencia del art. 438 CCyC)

### D17 · Caducidad de instancia en la petición

¿Puede caducar la instancia en la petición de divorcio si la parte no impulsa el traslado o la audiencia (arts. 310 a 316 CPCCBA)? Propuesta de la app: no se modeló caducidad en la petición; solo en las cuestiones pendientes, con el control de 3 meses.

**Hitos afectados:** DIV_140 (Petición unilateral de divorcio con propuesta reguladora), DIV_160 (Providencia inicial y traslado de la propuesta reguladora), DIV_950 (Control de caducidad de instancia)

### D18 · Etapa común y producto

Las dudas marcadas [ETAPA COMÚN] (etapa contenciosa común del proceso de familia) y [PRODUCTO] (dudas técnicas para el equipo de producto) se responden una sola vez, en matriz_familia_alimentos_pba.xlsx, y valen para esta matriz. Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx) también valen para familia: en esta matriz solo se abrieron dudas donde el fuero de familia se aparta.

**Hitos afectados:** Todos

## 5. Cuidado personal y régimen de comunicación (prefijo `CUI`)

### D01 · Medidas provisorias

¿Qué plazo de vigencia suelen fijar los juzgados para el régimen provisorio de cuidado o de comunicación, y cada cuánto lo revisan? ¿La resolución es apelable y con qué efecto? Propuesta de la app: el vencimiento o la revisión se cargan como fecha fijada y la prórroga vuelve al mismo hito.

**Hitos afectados:** CUI_050 (Medidas provisorias sobre el cuidado y la comunicación), CUI_060 (Vencimiento o revisión de las medidas provisorias)

### D02 · Homologación del plan de parentalidad

¿El plan de parentalidad acordado se presenta directo al juez para homologar o pasa por la etapa previa ante el Consejero? ¿Hace falta la escucha del hijo y la vista a la Asesoría antes de homologar? Propuesta de la app: homologación directa, con vista a la Asesoría y escucha del hijo si tiene edad y madurez suficiente. Fuente consultada: art. 655 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_030 (Plan de parentalidad acordado), CUI_900 (Acuerdo y homologación)

### D03 · Cuidado compartido como primera alternativa

Los arts. 651 y 656 CCyC obligan a priorizar el cuidado compartido indistinto. ¿Cambia en algo el trámite cuando se pide el cuidado unilateral (por ejemplo, pericia obligatoria o informe socioambiental de oficio)? Propuesta de la app: el mismo trámite, con la pericia y el informe como prueba ofrecida. Fuente consultada: arts. 651, 653 y 656 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_200 (Demanda de cuidado personal o régimen de comunicación), CUI_330 (Equipo técnico: pericia psicológica o psiquiátrica), CUI_340 (Equipo técnico: informe socioambiental)

### D04 · Escucha del niño

¿Desde qué edad escuchan los juzgados al niño y en qué momento (antes de la audiencia preliminar, en la vista de causa, antes de la sentencia)? ¿Se puede repetir en la modificación? Propuesta de la app: una entrevista con fecha fijada durante la prueba, que el abogado puede repetir cargando una nueva fecha.

**Hitos afectados:** CUI_360 (Escucha del niño, niña o adolescente por el juez)

### D05 · Abogado del niño como hito

La designación del abogado del niño (Ley 14.568) se modeló como un hito propio que se abre cuando el niño lo pide en la entrevista. ¿Conviene abrirlo también desde la providencia inicial o desde el pedido directo del niño? ¿Qué edad exige la ley para pedirlo? Propuesta de la app: el hito se abre desde la escucha y el abogado puede abrirlo antes si el niño lo pide.

**Hitos afectados:** CUI_360 (Escucha del niño, niña o adolescente por el juez), CUI_380 (Designación del abogado del niño)

### D06 · Informes del equipo técnico

¿Qué plazo tienen el equipo técnico y la Asesoría Pericial para presentar la pericia psicológica y el informe socioambiental, más allá de los 10 días antes de la vista de causa (arts. 844 y 848 CPCCBA)? Propuesta de la app: sin plazo propio; el control es el de la prueba previa a la vista de causa. Sobre los datos de salud de estos informes, ver la duda de producto en la matriz de alimentos.

**Hitos afectados:** CUI_330 (Equipo técnico: pericia psicológica o psiquiátrica), CUI_340 (Equipo técnico: informe socioambiental), CUI_370 (Incorporación de la prueba previa a la vista de causa)

### D07 · Medidas ante el incumplimiento

¿Qué medidas razonables del art. 557 CCyC admiten los juzgados de la provincia (multas, intervención del equipo técnico, cambio de la modalidad de cuidado)? ¿Hay un plazo para que el juez resuelva el pedido? Propuesta de la app: el checklist no nombra medidas concretas hasta que el equipo legal las valide. Fuente consultada: art. 557 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_720 (Incumplimiento del régimen o impedimento de contacto), CUI_730 (Medidas del juez ante el incumplimiento reiterado)

### D08 · Impedimento de contacto como delito

La Ley 24.270 (a verificar) castiga el impedimento de contacto y prevé que el juez penal restablezca el contacto en un plazo breve. ¿Qué artículos y plazos rigen? ¿Conviene una matriz o un hito propio para la denuncia penal? Propuesta de la app: la causa penal queda fuera de esta matriz y solo se menciona en el checklist.

**Hitos afectados:** CUI_720 (Incumplimiento del régimen o impedimento de contacto)

### D09 · Incumplimiento con causa protectoria

Cuando el progenitor que tiene el cuidado impide el contacto porque hay violencia o riesgo para el hijo, ¿cómo se coordina este expediente con el de violencia (medidas de protección que suspenden el régimen)? Propuesta de la app: el checklist del incumplimiento advierte que se evalúe la causa y se abra la matriz de violencia.

**Hitos afectados:** CUI_720 (Incumplimiento del régimen o impedimento de contacto), CUI_010 (Consulta sobre el cuidado o la comunicación con el hijo)

### D10 · Modificación del régimen

¿La modificación del cuidado o de la comunicación se pide por incidente en el mismo expediente o por un proceso nuevo con etapa previa ante el Consejero (art. 835 CPCCBA)? Propuesta de la app: proceso nuevo con etapa previa, salvo urgencia.

**Hitos afectados:** CUI_800 (Modificación del cuidado personal o del régimen de comunicación), CUI_100 (Solicitud de trámite de la etapa previa)

### D11 · Autorización para salir del país o cambiar la residencia

¿Por qué trámite se pide la autorización del art. 645 inc. c CCyC (sumarísimo, incidente, medida urgente sin etapa previa)? ¿Hay un plazo para resolver cuando el viaje tiene fecha? Propuesta de la app: hito sin plazo, con la fecha del viaje cargada como plazo suelto para alertar. Fuente consultada: art. 645 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_820 (Autorización judicial para salir del país o cambiar la residencia)

### D12 · Restitución internacional

Confirmar: Convención de La Haya de 1980 aprobada por Ley 23.857 (a verificar), restitución inmediata si el pedido se hace antes de un año (a verificar el artículo), Convención Interamericana de 1989 para los países que la ratificaron (a verificar), autoridad central y procedimiento en la provincia (protocolo de la SCBA, si existe). ¿El plazo de un año se cuenta desde el traslado o desde la retención? Propuesta de la app: 1 año desde el traslado o la retención, el que sea anterior (es lo más temprano). Fuente consultada: art. 2642 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_830 (Restitución internacional del niño)

### D13 · Delegación y guarda a un pariente

Delegación del ejercicio (art. 643 CCyC) y guarda a un pariente (art. 657): ¿el año se cuenta desde la homologación o desde que el niño empieza a convivir con el pariente? ¿La renovación se pide antes del vencimiento? Propuesta de la app: 1 año desde la homologación o la resolución, y la renovación vuelve al mismo hito. Fuente consultada: arts. 643 y 657 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_840 (Delegación del ejercicio o guarda a un pariente (plazo de un año))

### D14 · Comunicación con abuelos y otros parientes

El art. 555 CCyC manda resolver la oposición 'por el procedimiento más breve que prevea la ley local'. ¿Cuál es en la provincia: el sumarísimo, el sumario del art. 838 CPCCBA con etapa previa? Propuesta de la app: el mismo flujo que entre progenitores, con la etapa previa. Fuente consultada: arts. 555 y 556 CCyC en leyes-ar.com.

**Hitos afectados:** CUI_010 (Consulta sobre el cuidado o la comunicación con el hijo), CUI_100 (Solicitud de trámite de la etapa previa), CUI_200 (Demanda de cuidado personal o régimen de comunicación)

### D15 · Cambio del centro de vida durante el proceso

Si el hijo se muda de departamento judicial durante el proceso, ¿cambia la competencia (art. 716 CCyC) o sigue el juez que previno (art. 830 CPCCBA)? Propuesta de la app: sigue el mismo expediente y el abogado edita el juzgado si hay un cambio.

**Hitos afectados:** CUI_010 (Consulta sobre el cuidado o la comunicación con el hijo), CUI_200 (Demanda de cuidado personal o régimen de comunicación)

### D16 · Fin del régimen

El régimen de cuidado y comunicación termina con la mayoría de edad del hijo. ¿Conviene un hito de control de los 18 años, como el de los 21 años en alimentos? Propuesta de la app: no en la V1; el cumplimiento queda abierto hasta que el abogado lo cierra.

**Hitos afectados:** CUI_700 (Cumplimiento del régimen de cuidado y comunicación), CUI_910 (Cumplimiento del acuerdo homologado)

### D17 · Etapa común y producto

Las dudas marcadas [ETAPA COMÚN] (etapa contenciosa común del proceso de familia) y [PRODUCTO] (dudas técnicas para el equipo de producto) se responden una sola vez, en matriz_familia_alimentos_pba.xlsx, y valen para esta matriz. Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx) también valen para familia: en esta matriz solo se abrieron dudas donde el fuero de familia se aparta.

**Hitos afectados:** Todos

## 6. Violencia familiar: medidas de protección (prefijo `VIO`)

### D01 · Plazo de 48 horas para las medidas

El art. 7 obliga al juez a adoptar las medidas 'dentro de las cuarenta y ocho (48) horas de haber tomado conocimiento de la situación de violencia'. ¿El conocimiento es la recepción de la denuncia en el juzgado o la denuncia en la comisaría? ¿Las 48 horas corren en días inhábiles y en feria? Propuesta de la app: 48 horas corridas desde la fecha y hora en que el juzgado recibe la denuncia (regla R8). Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_040 (Remisión de la denuncia al juzgado), VIO_050 (Plazo del juez para resolver las medidas urgentes)

### D02 · Remisión desde la comisaría

¿Qué plazo tiene la comisaría u otro organismo para remitir la denuncia al juzgado (la Ley 12.569 no lo fija; ver su reglamentación, a verificar)? ¿Conviene un hito con plazo en horas para alertar demoras? Propuesta de la app: hito sin plazo, y las 48 horas del juez corren desde la recepción.

**Hitos afectados:** VIO_030 (Denuncia), VIO_040 (Remisión de la denuncia al juzgado)

### D03 · Plazo de las audiencias

El art. 11 manda tomar las audiencias 'dentro de las 48 horas de ordenadas las medidas del artículo 7º, o si no se adoptara ninguna de ellas, desde el momento que tomó conocimiento de la denuncia'. ¿Es el plazo para tomar las dos audiencias o para fijarlas? ¿Qué consecuencia tiene si no se cumple, además de la falta grave del art. 24? Propuesta de la app: las dos audiencias deben estar tomadas dentro de las 48 horas; el hito alerta el vencimiento. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_100 (Plazo para tomar las audiencias (48 horas)), VIO_110 (Audiencia de la persona denunciante), VIO_120 (Audiencia de la persona denunciada)

### D04 · Incomparecencia de la persona denunciante

La ley prevé la fuerza pública solo para la persona denunciada. Si la persona denunciante no comparece, ¿se mantienen las medidas? ¿Se la vuelve a citar? Propuesta de la app: las medidas siguen y ese camino se cierra; el abogado puede pedir una nueva audiencia.

**Hitos afectados:** VIO_110 (Audiencia de la persona denunciante)

### D05 · Informe interdisciplinario

Art. 8: el informe se remite al juez 'en un plazo de cuarenta y ocho (48) horas'. ¿Se cuentan desde el requerimiento? ¿Qué pasa si se acompaña uno con la denuncia (art. 8, segundo párrafo)? Propuesta de la app: 48 horas desde el requerimiento, y el hito se cierra si se acompañó un informe con la denuncia. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_130 (Informe interdisciplinario de riesgo)

### D06 · Duración y prórroga de las medidas

El juez fija el término de duración (art. 12). ¿Qué plazos usan los juzgados en la práctica? ¿Con cuánta anticipación conviene alertar el vencimiento para pedir la prórroga? Propuesta de la app: fecha fijada con el aviso estándar del motor y la prórroga vuelve al mismo hito con la nueva fecha.

**Hitos afectados:** VIO_150 (Vencimiento de las medidas)

### D07 · Plazo de apelación

Art. 10: las resoluciones sobre las medidas y las sanciones son apelables 'dentro del plazo de tres (3) días hábiles'. ¿Son hábiles judiciales y admiten el plazo de gracia del art. 124 CPCCBA? ¿El recurso se funda en el mismo escrito o con un memorial posterior en 5 días (art. 246 CPCCBA)? Propuesta de la app: 3 días hábiles judiciales con gracia y memorial de 5 días hábiles judiciales con gracia. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_200 (Apelación de la resolución sobre las medidas o las sanciones), VIO_210 (Fundamentación de la apelación (memorial))

### D08 · Efecto de la apelación de las sanciones

El art. 10 dice que la apelación de las sanciones por incumplimiento tiene efecto devolutivo, 'salvo en el caso del Inc. d) del Art. 7º que tendrá efecto suspensivo'. El inc. d del art. 7 es el reintegro al hogar y no es una sanción; las sanciones están en el art. 7 bis, cuyo inc. d son los trabajos comunitarios. ¿A cuál se refiere la excepción? Propuesta de la app: el checklist remite a esta duda y no afirma el efecto hasta que el equipo legal lo confirme. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_180 (Resolución ante el incumplimiento: medidas nuevas o sanciones), VIO_200 (Apelación de la resolución sobre las medidas o las sanciones)

### D09 · Una apelación que se abre de nuevo

La apelación se abre con cada resolución apelable (notificación de las medidas, ratificación o modificación, sanciones, cese). Si llegan dos resoluciones seguidas, el hito de apelación puede abrirse mientras sigue abierto. ¿El motor tiene que manejar dos plazos del mismo hito a la vez? Propuesta de la app: el abogado carga el segundo plazo como plazo suelto (ver la duda de producto sobre plazos que se reinician, en la matriz de alimentos).

**Hitos afectados:** VIO_070 (Notificación de las medidas a la persona denunciada), VIO_140 (Ratificación, modificación o ampliación de las medidas), VIO_180 (Resolución ante el incumplimiento: medidas nuevas o sanciones), VIO_200 (Apelación de la resolución sobre las medidas o las sanciones)

### D10 · Incumplimiento y sanciones

Art. 7 bis: ante el incumplimiento se da cuenta inmediatamente al juez, y ante un nuevo incumplimiento puede sancionar. ¿Hay un plazo para que el juez resuelva? ¿El primer incumplimiento ya habilita la comunicación al juez penal por desobediencia? Propuesta de la app: hitos sin plazo y la comunicación penal como salida de la resolución. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_170 (Incumplimiento de las medidas), VIO_180 (Resolución ante el incumplimiento: medidas nuevas o sanciones), VIO_190 (Comunicación al juez penal)

### D11 · Control de eficacia

Art. 14: el juez controla la eficacia con comparecencias periódicas o informes. ¿Las comparecencias se cargan como fechas fijadas? ¿Quién las impulsa? ¿Cuándo se considera que cesó el riesgo? Propuesta de la app: hito del juzgado sin plazo, y cada comparecencia como plazo suelto. Fuente consultada: texto actualizado de la Ley 12.569 (Leyes 14.509 y 14.657) en normas.gba.gob.ar.

**Hitos afectados:** VIO_160 (Control de eficacia de las medidas), VIO_300 (Cese de las medidas)

### D12 · Ley 26.485 y Ley 12.569

Cuando la violencia es contra una mujer, ¿se aplica además el procedimiento de la Ley nacional 26.485 (medidas preventivas y audiencia, a verificar los artículos y plazos) o rige solo la Ley 12.569 con las garantías del art. 16 de la Ley 26.485 (art. 6 ter)? Propuesta de la app: una sola matriz con la Ley 12.569; si la Ley 26.485 fija plazos más cortos, se usan esos.

**Hitos afectados:** VIO_030 (Denuncia), VIO_050 (Plazo del juez para resolver las medidas urgentes), VIO_100 (Plazo para tomar las audiencias (48 horas))

### D13 · Denuncia sin patrocinio

Para la denuncia de violencia contra mujeres no se requiere patrocinio letrado (art. 6 bis). Si el abogado toma el caso después de la denuncia o de las medidas, ¿la app permite crear el expediente en VIO_060 o VIO_140? Relacionarlo con la duda de producto sobre expedientes que empiezan en un hito intermedio. Propuesta de la app: sí.

**Hitos afectados:** VIO_030 (Denuncia), VIO_060 (Medidas de protección dictadas), VIO_140 (Ratificación, modificación o ampliación de las medidas)

### D14 · Representación de la persona denunciada

Si el estudio representa a la persona denunciada, el expediente empieza en la notificación de las medidas (VIO_070) y su paso propio es la apelación, la audiencia y el pedido de cese. ¿Es correcto? ¿Se usa el rol representado DEMANDADA? Ver la duda de producto sobre el rol representado.

**Hitos afectados:** VIO_070 (Notificación de las medidas a la persona denunciada), VIO_120 (Audiencia de la persona denunciada), VIO_200 (Apelación de la resolución sobre las medidas o las sanciones), VIO_230 (Pedido de modificación o cese de las medidas)

### D15 · Víctimas menores de edad

Cuando hay niños afectados, ¿quién da intervención al Servicio Local y a la Asesoría de Incapaces, y en qué plazo (Ley 13.298)? ¿Cómo se aplica hoy el art. 22 (remisión de antecedentes del Tribunal de Menores)? Propuesta de la app: hito del juzgado sin plazo, abierto con las medidas.

**Hitos afectados:** VIO_240 (Intervención de la Asesoría de Incapaces y del Servicio Local (víctima menor de edad))

### D16 · Datos que guarda la app

¿Qué datos de las medidas puede guardar la app sin aumentar el riesgo para la víctima? Propuesta: solo el tipo de medida (por ejemplo, 'prohibición de acercamiento') y su fecha de vencimiento; nunca domicilios, perímetros, lugares de trabajo, horarios, datos del dispositivo ni relato de hechos. Ver las dudas de producto sobre datos de víctimas y avisos en dispositivos compartidos.

**Hitos afectados:** VIO_060 (Medidas de protección dictadas), VIO_080 (Dispositivo de protección o custodia en el domicilio), VIO_090 (Comunicación de las medidas y oficio al Registro Nacional de Armas)

### D17 · Medidas sobre alimentos y cuidado

Las medidas del art. 7 incs. g, h e i (cuota alimentaria, cuidado y guarda provisorios, suspensión del régimen de comunicación) duran lo que fije el juez. ¿Cuándo conviene promover el reclamo definitivo en las matrices de alimentos o de cuidado personal? ¿Se tramitan en el mismo juzgado (art. 830 CPCCBA)? Propuesta de la app: la derivación se ofrece al ratificar las medidas.

**Hitos afectados:** VIO_140 (Ratificación, modificación o ampliación de las medidas), VIO_970 (Sigue en la matriz de alimentos y compensación económica), VIO_980 (Sigue en la matriz de cuidado personal y régimen de comunicación)

### D18 · Nuevo hecho durante la vigencia

Si hay un hecho nuevo mientras las medidas están vigentes, ¿se denuncia en el mismo expediente (incumplimiento) o se abre uno nuevo? Propuesta de la app: en el mismo expediente, como incumplimiento.

**Hitos afectados:** VIO_170 (Incumplimiento de las medidas), VIO_230 (Pedido de modificación o cese de las medidas)

### D19 · Honorarios en violencia

Ley 14.967: mínimo del art. 9 para la violencia familiar. Con la gratuidad del art. 6 bis Ley 12.569, ¿quién paga los honorarios del letrado de la denunciante? ¿En qué momento se regulan (al cese, al archivo)? Propuesta de la app: regulación al cese, con apelación de 5 días hábiles judiciales con gracia.

**Hitos afectados:** VIO_300 (Cese de las medidas), VIO_310 (Regulación y apelación de honorarios)

### D20 · Etapa común y producto

Las dudas marcadas [ETAPA COMÚN] (etapa contenciosa común del proceso de familia) y [PRODUCTO] (dudas técnicas para el equipo de producto) se responden una sola vez, en matriz_familia_alimentos_pba.xlsx, y valen para esta matriz. Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx) también valen para familia: en esta matriz solo se abrieron dudas donde el fuero de familia se aparta.

**Hitos afectados:** Todos

## 7. Adopción (prefijo `ADO`)

### D01 · Cómputo de los días

La Ley 14.528 dice 'días corridos' solo para la selección de postulantes (art. 17). Los demás plazos en días (30 de búsqueda, 10 de estudios, 90 para resolver la adoptabilidad) y los 180 días de la medida de abrigo (art. 35 bis Ley 13.298) no aclaran. ¿Son corridos (art. 6 CCyC) o hábiles (CPCCBA supletorio, art. 30)? Propuesta de la app: corridos, que es lo más temprano. Fuente consultada: texto actualizado de la Ley 14.528 (Ley 15.610, B.O. 13/01/2026) en normas.gba.gob.ar.

**Hitos afectados:** ADO_120 (Plazo máximo de la medida de abrigo), ADO_130 (Búsqueda de la familia de origen), ADO_240 (Estudios psicológicos, de salud y socioambientales), ADO_260 (Plazo máximo para resolver la situación de adoptabilidad), ADO_300 (Selección de los postulantes)

### D02 · Desde cuándo corren los 90 días

Los arts. 7 y 13 obligan al juez a resolver la adoptabilidad 'en el plazo máximo de noventa (90) días', sin decir desde cuándo. ¿Desde el dictamen del Servicio, desde la manifestación de los progenitores, desde el inicio de la medida de abrigo? Propuesta de la app: desde el dictamen o la manifestación, como alerta de demora. Fuente consultada: texto actualizado de la Ley 14.528 (Ley 15.610, B.O. 13/01/2026) en normas.gba.gob.ar.

**Hitos afectados:** ADO_260 (Plazo máximo para resolver la situación de adoptabilidad)

### D03 · Plazo de la apelación

El art. 27 hace apelables todas las resoluciones, en relación y con efecto devolutivo, pero no fija el plazo. ¿Rige el general de 5 días (art. 244 CPCCBA) o el de 2 días del sumarísimo (art. 496 inc. 2) cuando el juez aplicó esos plazos (art. 4 Ley 14.528)? ¿Y el memorial (art. 246)? Propuesta de la app: 2 días hábiles judiciales con gracia (es lo más temprano), editables. Fuente consultada: arts. 4 y 27 Ley 14.528 en normas.gba.gob.ar y art. 496 CPCCBA en leyes-ar.com.

**Hitos afectados:** ADO_280 (Apelación de la resolución de adoptabilidad), ADO_440 (Apelación de la sentencia de adopción)

### D04 · Guarda de hecho y vínculo afectivo

El art. 611 CCyC exceptúa de la separación solo el vínculo de parentesco entre los progenitores y el guardador. El art. 16 de la Ley 14.528 agrega el vínculo afectivo. ¿Cuál aplican los juzgados? Propuesta de la app: el checklist cita los dos y el equipo legal decide. Fuente consultada: art. 611 CCyC en leyes-ar.com y art. 16 Ley 14.528 en normas.gba.gob.ar.

**Hitos afectados:** ADO_050 (Entrega directa o guarda de hecho)

### D05 · Control de legalidad de la medida de abrigo

Art. 35 bis Ley 13.298: el Servicio comunica en 24 horas y el juez resuelve la legalidad en 72 horas. ¿Las horas corren en días inhábiles y en feria? ¿Las 72 horas se cuentan desde la recepción de la comunicación? ¿La resolución es apelable y por quién? Propuesta de la app: horas corridas desde la fecha y hora de la comunicación (regla R8). Fuente consultada: art. 35 bis Ley 13.298 en normas.gba.gob.ar.

**Hitos afectados:** ADO_100 (Comunicación de la medida de abrigo al juez), ADO_110 (Control de legalidad de la medida de abrigo)

### D06 · Plazo máximo de la medida de abrigo

Los 180 días del art. 35 bis ¿corren desde la adopción de la medida por el Servicio o desde el control de legalidad? ¿Pueden prorrogarse? Propuesta de la app: desde la adopción de la medida y sin prórroga (es lo más temprano).

**Hitos afectados:** ADO_120 (Plazo máximo de la medida de abrigo)

### D07 · Informes del Servicio cada 30 días

El art. 10 obliga al Servicio a informar al juez cada 30 días sobre las medidas. ¿Conviene un hito propio con plazo que se repite, o alcanza con plazos sueltos? Propuesta de la app: plazos sueltos.

**Hitos afectados:** ADO_120 (Plazo máximo de la medida de abrigo)

### D08 · Búsqueda de la familia de origen

Arts. 7 inc. a y 8: búsqueda en un plazo máximo de 30 días, prorrogable por igual plazo y por razón fundada. ¿Desde cuándo corre: desde que el Servicio toma conocimiento o desde que notifica al juez? ¿Se admite más de una prórroga? Propuesta de la app: desde el conocimiento, con una sola prórroga.

**Hitos afectados:** ADO_130 (Búsqueda de la familia de origen)

### D09 · Manifestación de los progenitores

La manifestación de autorizar la adopción solo es válida después de 45 días del nacimiento (art. 11 Ley 14.528, art. 607 inc. b CCyC) y la audiencia se fija 'a los tres (3) días'. ¿Son días hábiles? ¿Hasta cuándo pueden retractarse los progenitores? Propuesta de la app: la audiencia como fecha fijada y el plazo mínimo de 45 días como ítem del checklist (ver la duda de producto sobre plazos mínimos).

**Hitos afectados:** ADO_200 (Manifestación de los progenitores de autorizar la adopción), ADO_210 (Audiencia con los progenitores que autorizan la adopción)

### D10 · Audiencia con la familia de origen

El art. 10 manda fijar la audiencia dentro de 10 días de recibido el dictamen. ¿Conviene un hito con ese plazo para alertar si el juez no la fija? ¿Qué se considera incomparecencia 'injustificada y reiterada' para declarar la adoptabilidad? Propuesta de la app: fecha fijada y el plazo de 10 días en el checklist del dictamen.

**Hitos afectados:** ADO_220 (Dictamen del Servicio sobre la situación de adoptabilidad), ADO_230 (Audiencia con los progenitores y la familia de origen)

### D11 · Abogado del niño

La Ley 15.610 hizo obligatoria la asistencia del abogado del niño en el control de legalidad, la adoptabilidad y la adopción (art. 6), pero en el juicio de adopción el art. 23 dice que el niño 'podrá' comparecer con asistencia letrada. ¿Es obligatoria en el juicio de adopción? ¿Cómo se registra en la app su intervención (rol, notificaciones)? Si el estudio es el abogado del niño, ¿qué hitos son su paso propio? Ver la duda de producto sobre roles del fuero.

**Hitos afectados:** ADO_110 (Control de legalidad de la medida de abrigo), ADO_250 (Contacto personal del juez con el niño), ADO_420 (Audiencia de comparecencia y consentimiento del niño)

### D12 · Selección de los postulantes

Art. 17: el juez selecciona 'en un plazo máximo de cinco (5) días corridos' una vez declarada la adoptabilidad. ¿Corren desde la declaración o desde que recibe la nómina del Registro (art. 15)? Propuesta de la app: desde la declaración (es lo más temprano). Fuente consultada: texto actualizado de la Ley 14.528 (Ley 15.610, B.O. 13/01/2026) en normas.gba.gob.ar.

**Hitos afectados:** ADO_290 (Comunicación al Registro Central y remisión de la nómina), ADO_300 (Selección de los postulantes)

### D13 · Vinculación

Art. 19 (texto Ley 15.610): vinculación 'en principio de hasta tres (3) meses', ampliable por un período igual. ¿Desde la audiencia con los postulantes o desde el primer encuentro? Propuesta de la app: desde la audiencia, con una sola ampliación que vuelve al mismo hito. Fuente consultada: texto actualizado de la Ley 14.528 (Ley 15.610, B.O. 13/01/2026) en normas.gba.gob.ar.

**Hitos afectados:** ADO_320 (Vinculación con el niño)

### D14 · Plazo de la guarda y comienzo del juicio

La guarda no puede exceder de 6 meses (art. 614 CCyC, art. 20 Ley 14.528). ¿Desde la resolución o desde la audiencia de otorgamiento? Si vence y nadie inicia el juicio (art. 22: de oficio o a pedido), ¿qué pasa con la guarda? Propuesta de la app: desde la resolución, y el vencimiento alerta para pedir el inicio del juicio.

**Hitos afectados:** ADO_350 (Plazo de la guarda con fines de adopción), ADO_400 (Demanda de adopción)

### D15 · Adopción de integración

En la adopción del hijo del cónyuge o conviviente, ¿se omiten la declaración de adoptabilidad, la inscripción en el Registro y la guarda (art. 632 CCyC, a verificar)? La sentencia tiene efecto desde la promoción de la acción (art. 618 CCyC). Propuesta de la app: el expediente empieza directamente en la demanda de adopción. Fuente consultada: art. 618 CCyC en leyes-ar.com.

**Hitos afectados:** ADO_010 (Consulta sobre una adopción), ADO_400 (Demanda de adopción)

### D16 · Trámite del juicio de adopción

El art. 22 remite al sumario, salvo que el juez aplique el sumarísimo (art. 4). ¿Qué plazos usan los juzgados para la vista al Ministerio Público y la audiencia del art. 25? ¿Hay contestación de demanda? Propuesta de la app: hitos sin plazo para la vista y fecha fijada para la audiencia.

**Hitos afectados:** ADO_400 (Demanda de adopción), ADO_410 (Vista al Ministerio Público y notificación al Servicio), ADO_420 (Audiencia de comparecencia y consentimiento del niño)

### D17 · Registro Central de Aspirantes

¿Qué requisitos, vigencia y recursos fija el reglamento del Registro (Acordada SCBA 3607/2012 y modificatorias; el art. 33 bis menciona además la Resolución SCBA 2922/2022)? ¿Hay un plazo para impugnar la no admisión? Propuesta de la app: hitos sin plazo hasta que el equipo legal confirme el reglamento vigente.

**Hitos afectados:** ADO_020 (Inscripción en el Registro Central de Aspirantes a Guardas con Fines de Adopción), ADO_030 (Impugnación de la no admisión en el Registro), ADO_040 (Espera de la convocatoria)

### D18 · Contenido reservado del expediente

El expediente de adopción es reservado (art. 617 inc. e CCyC) y debe contener la mayor cantidad de datos de origen, incluidas las enfermedades transmisibles (art. 596 CCyC), y datos de salud y registros fotográficos (art. 8 inc. c Ley 14.528). ¿La app debe impedir que se cargue cualquier dato de origen en campos libres? Propuesta: sí, con un aviso en los hitos de este flujo. Ver las dudas de producto sobre expediente reservado y datos de salud.

**Hitos afectados:** ADO_240 (Estudios psicológicos, de salud y socioambientales), ADO_430 (Sentencia de adopción), ADO_510 (Acceso a los orígenes)

### D19 · Acciones posteriores a la adopción

¿Qué trámite y qué juez corresponden a la conversión (art. 622 CCyC), la revocación y la nulidad (arts. 634 y 635)? ¿Qué artículo fija las causales de revocación de la adopción simple? Propuesta de la app: un solo hito sin plazo hasta que el equipo legal defina si conviene una matriz propia.

**Hitos afectados:** ADO_500 (Conversión, revocación o nulidad de la adopción)

### D20 · Etapa común y producto

Las dudas marcadas [ETAPA COMÚN] (etapa contenciosa común del proceso de familia) y [PRODUCTO] (dudas técnicas para el equipo de producto) se responden una sola vez, en matriz_familia_alimentos_pba.xlsx, y valen para esta matriz. Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx) también valen para familia: en esta matriz solo se abrieron dudas donde el fuero de familia se aparta.

**Hitos afectados:** Todos

## 8. Citas marcadas "(a verificar)" en los hitos

No se usan hasta que el abogado las confirme. Las de la etapa común aparecen en cada matriz que la usa.

**Alimentos**

- `ALI_490` (Asesoría de Incapaces: vista previa a la sentencia): Art. 103 CCyC; art. 850 inc. 3 CPCCBA; Ley 14.442 (a verificar artículo)
- `ALI_500` (Sentencia sobre la compensación económica): Art. 494 CPCCBA (plazo del juez, a verificar en el proceso de familia)
- `ALI_610` (Fundamentación de la apelación (expresión de agravios o memorial)): Contestar el traslado de los agravios de la contraria (plazo a verificar)
- `ALI_630` (Recurso extraordinario ante la SCBA): Verificar si corresponde el depósito previo y sus exenciones en familia (art. 280, a verificar)
- `ALI_650` (Trámite y resolución ante la SCBA): Art. 284 CPCCBA (a verificar)
- `ALI_740` (Ejecución de cuotas atrasadas): El incumplimiento puede ser además un delito (Ley 13.944, a verificar): la causa penal sigue fuera de esta matriz
- `ALI_900` (Acuerdo y homologación): Arts. 835 y 843 inc. 3 CPCCBA; arts. 308 y 309 CPCCBA (a verificar)

**Divorcio**

- `DIV_050` (Plazo para presentar la petición después de trabadas las medidas): Art. 207 CPCCBA (su aplicación en familia, a verificar)
- `DIV_140` (Petición unilateral de divorcio con propuesta reguladora): Tasa de justicia del divorcio según la Ley Impositiva vigente (a verificar), bono Ley 8480 y aportes Ley 6716
- `DIV_150` (Petición conjunta de divorcio con convenio regulador): Tasa de justicia del divorcio según la Ley Impositiva vigente (a verificar), bono Ley 8480 y aportes Ley 6716
- `DIV_170` (Contrapropuesta reguladora del otro cónyuge): Art. 438 CCyC; art. 150 CPCCBA (plazo general de los traslados; su aplicación, a verificar)
- `DIV_810` (Inscripción de la sentencia de divorcio en el Registro de las Personas): Ley 26.413 (a verificar artículo)
- `DIV_850` (Liquidación y partición de la comunidad): Verificar si corresponde una tasa de justicia mayor por la liquidación (Ley Impositiva vigente, a verificar)
- `DIV_490` (Asesoría de Incapaces: vista previa a la sentencia): Art. 103 CCyC; art. 850 inc. 3 CPCCBA; Ley 14.442 (a verificar artículo)
- `DIV_500` (Sentencia sobre las cuestiones pendientes): Art. 494 CPCCBA (plazo del juez, a verificar en el proceso de familia)
- `DIV_610` (Fundamentación de la apelación (expresión de agravios o memorial)): Contestar el traslado de los agravios de la contraria (plazo a verificar)
- `DIV_630` (Recurso extraordinario ante la SCBA): Verificar si corresponde el depósito previo y sus exenciones en familia (art. 280, a verificar)
- `DIV_650` (Trámite y resolución ante la SCBA): Art. 284 CPCCBA (a verificar)
- `DIV_900` (Acuerdo y homologación): Arts. 835 y 843 inc. 3 CPCCBA; arts. 308 y 309 CPCCBA (a verificar)

**Cuidado personal y régimen de comunicación**

- `CUI_260` (Ampliación de la prueba del actor por hechos nuevos): Revisar la documental agregada con la contestación y desconocerla si corresponde (art. 356, a verificar el plazo en el proceso de familia)
- `CUI_490` (Asesoría de Incapaces: vista previa a la sentencia): Art. 103 CCyC; art. 850 inc. 3 CPCCBA; Ley 14.442 (a verificar artículo)
- `CUI_500` (Sentencia): Art. 494 CPCCBA (plazo del juez, a verificar en el proceso de familia)
- `CUI_610` (Fundamentación de la apelación (expresión de agravios o memorial)): Contestar el traslado de los agravios de la contraria (plazo a verificar)
- `CUI_630` (Recurso extraordinario ante la SCBA): Verificar si corresponde el depósito previo y sus exenciones en familia (art. 280, a verificar)
- `CUI_650` (Trámite y resolución ante la SCBA): Art. 284 CPCCBA (a verificar)
- `CUI_720` (Incumplimiento del régimen o impedimento de contacto): Art. 557 CCyC; Ley 24.270 (a verificar)
- `CUI_720` (Incumplimiento del régimen o impedimento de contacto): El impedimento de contacto puede ser además un delito (Ley 24.270, a verificar): la causa penal sigue fuera de esta matriz
- `CUI_830` (Restitución internacional del niño): Art. 2642 CCyC; Convención de La Haya de 1980 sobre los aspectos civiles de la sustracción internacional de menores, Ley 23.857 (a verificar)
- `CUI_830` (Restitución internacional del niño): Si el pedido se presenta antes de que pase un año del traslado o la retención, la restitución debería ser inmediata (a verificar el artículo de la Convención)
- `CUI_830` (Restitución internacional del niño): Iniciar el pedido ante la autoridad central o ante el juez (a verificar el procedimiento en la provincia)
- `CUI_900` (Acuerdo y homologación): Arts. 835 y 843 inc. 3 CPCCBA; arts. 308 y 309 CPCCBA (a verificar)

**Violencia familiar: medidas de protección**

- `VIO_040` (Remisión de la denuncia al juzgado): Art. 6 Ley 12.569; plazo de remisión según su reglamentación (a verificar)
- `VIO_210` (Fundamentación de la apelación (memorial)): Art. 246 CPCCBA (su aplicación en violencia, a verificar)
- `VIO_210` (Fundamentación de la apelación (memorial)): Contestar el memorial de la contraria (plazo a verificar)

**Adopción**

- `ADO_020` (Inscripción en el Registro Central de Aspirantes a Guardas con Fines de Adopción): Completar la inscripción con los requisitos del reglamento del Registro (a verificar)
- `ADO_030` (Impugnación de la no admisión en el Registro): Acordada SCBA 3607/2012 y su reglamento (a verificar el recurso y su plazo)
- `ADO_260` (Plazo máximo para resolver la situación de adoptabilidad): Recepción del dictamen del Servicio o de la manifestación de los progenitores (a verificar)
- `ADO_280` (Apelación de la resolución de adoptabilidad): Art. 27 Ley 14.528; arts. 244, 246 y 496 inc. 2 CPCCBA (plazo a verificar)
- `ADO_440` (Apelación de la sentencia de adopción): Art. 27 Ley 14.528; arts. 244, 246 y 496 inc. 2 CPCCBA (plazo a verificar)
- `ADO_500` (Conversión, revocación o nulidad de la adopción): Arts. 622, 633, 634 y 635 CCyC; revocación de la adopción simple (artículo a verificar)

## 9. Decisiones de modelado a confirmar

- **Divorcio:** la petición del art. 438 CCyC tiene trámite propio y la etapa común se usa solo para las cuestiones pendientes (vivienda y bienes). Alimentos, compensación económica y cuidado de los hijos siguen en sus matrices.
- **Caducidad de la compensación económica:** el plazo de 6 meses se abre al dictarse la sentencia de divorcio, en las dos salidas posibles, para no perder el vencimiento más temprano.
- **Violencia:** las audiencias de la persona denunciante y el informe interdisciplinario cierran su propio camino; solo la audiencia de la persona denunciada sigue a la ratificación o el cese de las medidas.
- **Adopción:** los plazos en días que la Ley 14.528 no califica se cargaron como días corridos; las apelaciones, en 2 días hábiles judiciales con gracia; los 90 días para resolver la adoptabilidad, como alerta desde el dictamen o la manifestación de los progenitores.
- **Plazos de juzgados y organismos:** se cargaron sin gracia, porque no son presentaciones de parte.
- **Expedientes que empiezan en un hito intermedio:** según a quién represente el estudio (aspirantes a adoptar en ADO_300 o ADO_400, persona denunciada en VIO_070).
- **Derivaciones:** son hitos finales "Sigue en la matriz de ..."; cómo se vinculan los dos expedientes es la duda de producto D42 de alimentos.

## 10. Después de validar

1. Cargar cada respuesta en la planilla y marcar `Estado` en `Dudas_a_validar`.
2. Corregir las filas de `Nodos` y `Transiciones` afectadas y su `Estado_Validacion`.
3. Regenerar solo los diagramas desde la planilla, con `diagrama.py` (ver [`README.md`](README.md)).
4. Llevar los cambios también a `datos/` para no perderlos si se rehace el borrador.
5. Completar `Validado por (equipo legal)` en la hoja `Flujo` y subir la versión.
