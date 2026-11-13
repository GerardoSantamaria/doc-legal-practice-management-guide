# Dudas y puntos a validar · Derecho Comercial PBA

**Estado:** borrador para validar · **Fecha:** 13/11/2026 · **Versión de las matrices:** 1 (borrador)

Este documento reúne lo que el abogado tiene que validar en las tres matrices comerciales: las dudas de la hoja `Dudas_a_validar` de cada planilla, ordenadas por bloque, las citas que quedaron marcadas "(a verificar)" en los hitos y algunas decisiones de modelado que conviene confirmar. El texto de cada duda es el mismo que el de la planilla.

| Matriz | Planilla | Hitos | Transiciones | Dudas |
| :--- | :--- | ---: | ---: | ---: |
| Concursos y quiebras | [`matriz_comercial_concursos_pba.xlsx`](matriz_comercial_concursos_pba.xlsx) | 69 | 131 | 31 |
| Juicios ejecutivos y cobro de pesos | [`matriz_comercial_ejecutivos_pba.xlsx`](matriz_comercial_ejecutivos_pba.xlsx) | 47 | 91 | 18 |
| Conflictos societarios | [`matriz_comercial_societarios_pba.xlsx`](matriz_comercial_societarios_pba.xlsx) | 44 | 91 | 19 |

---

## 1. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal`, con la norma o la acordada que la sostiene, y `Estado` pasa a `VALIDADO` o `CORREGIR`. Si la respuesta cambia un hito, se corrige también la fila en `Nodos` o en `Transiciones`, con su `Estado_Validacion`.
- **Además de las dudas, cada fila se valida.** Hay 473 filas de hitos y transiciones con `Estado_Validacion = PENDIENTE` (200 en concursos, 138 en ejecutivos y 135 en societarios). El control "filas pendientes" de la hoja `Flujo` las cuenta.
- **Las dudas compartidas se responden una sola vez.** Las transversales (vigencia, tasa de justicia, honorarios y aportes, ferias, plazo de gracia, notificaciones, tasa de interés) y las de producto están en la matriz de **concursos**. Las de la etapa contenciosa común del CPCCBA están en la matriz de **societarios**. Las reglas del motor se validan en las dudas D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx`.
- **Ante la duda, el vencimiento más temprano.** Es el principio del motor: cada duda trae una propuesta por defecto que cumple ese principio. Una propuesta por defecto no se da por buena hasta que el abogado la acepte por escrito.
- **No correr `generar.py` sobre una planilla una vez que el abogado empiece a completarla:** la pisa con lo que hay en `datos/` (ver [`README.md`](README.md)).

## 2. Las de mayor impacto

| Matriz y duda | Tema | Por qué primero |
| :--- | :--- | :--- |
| Concursos D30 | Catálogos de la app | Sin un régimen para la LCQ y el CPCCBA, el fuero Civil y Comercial y el tipo de juzgado, ninguna de las tres matrices se puede importar. |
| Concursos D25 y D26 | Roles y rol representado | Si el estudio representa a un acreedor, los avisos de "te toca a vos" pueden quedar invertidos en todo el concurso. |
| Concursos D03 y D05 | Cronograma del juez y Día Cero | Definen cómo se cargan las fechas de verificación, informes y exclusividad, que son el camino principal del concurso. |
| Societarios D02 | Mediación y caducidad de 3 meses | Si la mediación no suspende el plazo del art. 251, la impugnación caduca mientras se media. |
| Ejecutivos D04 | Prescripción según el título | El plazo cargado es de 1 año; con otro título puede ser de 3 o 5 años, o correr desde otro hecho. |
| Ejecutivos D05 | Aceptación de la factura de crédito electrónica | Una resolución de octubre de 2026 cambió el plazo de 15 a 21 días corridos hasta octubre de 2027. |

## 3. Concursos y quiebras (prefijo `CYQ`)

### 3.1 Bloque A · Régimen y fuentes

Definen qué normas cubre el flujo.

#### D01 · Régimen y vigencia

¿Sigue vigente al 13/11/2026 la Ley 24.522 con las últimas reformas encontradas (Ley 27.170 de 2015 y Decreto 62/2019, que agregó el inc. 4 del art. 21)? ¿Hay alguna reforma de 2025 o 2026 en trámite o sancionada? El CPCCBA rige de forma supletoria (art. 278 LCQ); su última reforma encontrada es la Ley 15.513 (BO 03/01/2025). Propuesta: la matriz se arma sobre el texto actualizado de InfoLEG. Fuentes: InfoLEG (Ley 24.522, texto actualizado) y normas.gba.gob.ar.

**Hitos afectados:** Todos

#### D02 · Citas normativas

Validar artículo por artículo las citas de la LCQ, del CPCCBA, de la LGS y de las Leyes 6716, 8480 y 14.967. Las marcadas '(a verificar)' no se pudieron confirmar en el texto oficial.

**Hitos afectados:** Todos

### 3.2 Bloque B · Plazos y cómputo

Cada respuesta cambia un valor, un tipo de plazo, un disparador o la gracia de un hito, y con eso la fecha de vencimiento.

#### D04 · Cómputo de los plazos de la LCQ

El art. 273 inc. 2 dice que los plazos se cuentan en días hábiles judiciales salvo disposición en contrario. ¿Hay plazos de la ley que sean corridos además del art. 190 (20 días corridos)? ¿Los de meses y años (2 años de la verificación tardía, 6 meses de la nulidad y de la extensión, 3 años de la ineficacia) se cuentan por calendario? Propuesta: así están cargados.

**Hitos afectados:** CYQ_250 (Verificación tardía), CYQ_485 (Nulidad del acuerdo homologado), CYQ_755 (Continuación de la explotación y cooperativa de trabajo), CYQ_765 (Ineficacia de actos y acción revocatoria concursal), CYQ_770 (Pedido de extensión de la quiebra)

#### D05 · Notificación por ministerio de la ley

Muchos plazos corren desde la notificación por ministerio de la ley (arts. 26 y 273 inc. 5): edictos, libros, exclusividad, impugnación. ¿El Día Cero es el martes o viernes siguiente al dictado de la resolución (art. 133 CPCCBA, a verificar)? ¿Cómo lo carga el abogado: como fecha del disparador? Propuesta: el abogado carga como disparador el día de nota siguiente.

**Hitos afectados:** CYQ_130 (Publicación de edictos del concurso), CYQ_140 (Presentación de libros y depósito de gastos de correspondencia), CYQ_330 (Resolución de categorización y comité de control), CYQ_450 (Impugnación del acuerdo)

#### D06 · Plazo de gracia

La matriz aplica la gracia del art. 124 CPCCBA (por el art. 278 LCQ) solo a las presentaciones de parte en días hábiles judiciales, y no a los plazos de los órganos del concurso ni a los de meses y años. ¿Es correcto en el concurso, donde los plazos son perentorios (art. 273 inc. 1)? Vale también para ejecutivos y societarios.

**Hitos afectados:** Todos

#### D18 · Entrega de libros y edictos

Los plazos de 24 y 48 horas del art. 88 y las 24 horas del art. 89 se cargaron como HORAS. ¿Corren desde la notificación o desde la sentencia? ¿Cuentan las horas inhábiles? Propuesta: desde la notificación, en horas corridas.

**Hitos afectados:** CYQ_725 (Entrega de libros y constitución de domicilio por el fallido), CYQ_730 (Publicación de edictos de la quiebra)

#### D19 · Reposición de la quiebra

El art. 94 da 5 días desde que el fallido conoció la sentencia o, si no la conoció antes, hasta el quinto día de la última publicación. Son dos disparadores. Propuesta (la más temprana): desde el conocimiento, que el abogado carga como fecha del disparador.

**Hitos afectados:** CYQ_735 (Reposición o levantamiento sin trámite de la quiebra)

#### D22 · Ferias judiciales

La SCBA fija por acordada la feria de enero y la de invierno. Propuesta: los plazos en días hábiles judiciales se congelan; los corridos, las horas y los plazos de meses y años no se suspenden. ¿Hay habilitación de feria automática en los concursos? Las reglas del motor se validan en las dudas D26 a D34 de la matriz laboral general y valen también para las tres matrices comerciales.

**Hitos afectados:** Todos

#### D23 · Notificaciones electrónicas

Según el reglamento de la SCBA (Acuerdo 4013, texto ordenado por el Acuerdo 4039, art. 13), la notificación electrónica se perfecciona el martes o viernes siguiente a quedar disponible. ¿Qué notificaciones del concurso siguen siendo por cédula papel (art. 273 inc. 5: citación a las partes) o por carta del síndico (art. 29)?

**Hitos afectados:** CYQ_150 (Aceptación del cargo del síndico y cartas a los acreedores), CYQ_705 (Citación al deudor (art. 84))

### 3.3 Bloque C · Trámite hito por hito

Confirman cómo se modeló cada etapa del concurso, del APE y de la quiebra.

#### D07 · Arancel de verificación

El art. 32 (texto Ley 27.170) fija un arancel del 10% del SMVM por pedido, que se suma al crédito. ¿Qué exenciones rigen hoy (créditos laborales y créditos chicos, a verificar)? ¿Lo paga también el tardío y el incidental? El texto dice que sí.

**Hitos afectados:** CYQ_200 (Pedidos de verificación ante el síndico), CYQ_250 (Verificación tardía)

#### D08 · Pronto pago laboral

¿Conviene un hito propio para el pedido de pronto pago del trabajador (art. 16), con su plazo, o alcanza con el checklist del informe del art. 14 inc. 11? Propuesta: checklist en la V1.

**Hitos afectados:** CYQ_155 (Informe sobre pasivos laborales y pronto pago)

#### D09 · Fuero de atracción y juicios del estudio

Si el estudio lleva un juicio contra quien se concursa, ¿se modela la radicación en el concurso como derivación desde la matriz de ejecutivos o de societarios (hitos 'Sigue en la matriz de concursos')? Los juicios excluidos del art. 21 (garantías reales, conocimiento en trámite, laborales) siguen en su tribunal y verifican con la sentencia. Propuesta: derivación en la matriz de origen y checklist acá.

**Hitos afectados:** CYQ_160 (Suspensión de juicios y fuero de atracción), CYQ_250 (Verificación tardía)

#### D10 · Período de exclusividad y propuesta

El art. 43 pide hacer pública la propuesta 20 días antes del vencimiento. ¿Son 20 días hábiles judiciales (art. 273 inc. 2)? Se cargó como anticipación en días hábiles judiciales. ¿Quién fija la fecha de vencimiento de la exclusividad: el juez en el auto de categorización o el abogado calculando 90 días? Propuesta: fecha fijada.

**Hitos afectados:** CYQ_400 (Vencimiento del período de exclusividad: acompañar las conformidades), CYQ_410 (Propuesta de acuerdo pública en el expediente)

#### D11 · Homologación sin plazo

La LCQ no fija plazo para homologar (art. 52). ¿Corresponde SIN_PLAZO o el plazo general de 5 días del art. 273 inc. 1? Propuesta: SIN_PLAZO, porque el plazo del art. 273 inc. 1 es para las partes.

**Hitos afectados:** CYQ_460 (Homologación del acuerdo)

#### D12 · Salvataje (art. 48)

¿Desde qué hecho corren los 20 días para obtener conformidades (art. 48 inc. 4): la resolución que fija el valor o su notificación? ¿Cómo se modela la competencia entre el deudor y los inscriptos (el primero que acredita gana)? Propuesta: un solo hito con el plazo más temprano y el detalle en el checklist.

**Hitos afectados:** CYQ_500 (Registro de interesados en el salvataje (art. 48)), CYQ_510 (Valuación de las cuotas o acciones), CYQ_520 (Período para obtener las conformidades en el salvataje)

#### D13 · Pequeños concursos y persona humana

¿Conviene un flujo aparte para los pequeños concursos (arts. 288 y 289: sin comité ni art. 48) y para la persona humana que no realiza actividad empresarial? Propuesta: el mismo flujo, con el checklist de CYQ_010 y las salidas que excluyen el art. 48.

**Hitos afectados:** CYQ_010 (Diagnóstico de la insolvencia y elección de la vía), CYQ_400 (Vencimiento del período de exclusividad: acompañar las conformidades), CYQ_500 (Registro de interesados en el salvataje (art. 48))

#### D14 · APE

¿Desde cuándo se suspenden las acciones en el APE (art. 72, a verificar: orden de publicar edictos)? ¿El incumplimiento del APE homologado lleva a la quiebra igual que en el concurso (art. 76 remite a las reglas de nulidad e incumplimiento)? Falta un hito de cumplimiento: ¿se agrega?

**Hitos afectados:** CYQ_600 (Pedido de homologación del acuerdo extrajudicial), CYQ_620 (Oposiciones a la homologación del APE), CYQ_630 (Resolución sobre la homologación del APE)

#### D17 · Pedido de quiebra: defensa del deudor

¿El depósito en pago o a embargo del crédito del peticionante dentro del quinto día (art. 84) evita la quiebra según la práctica de los juzgados de PBA? ¿Conviene un hito propio para las medidas precautorias del art. 85?

**Hitos afectados:** CYQ_700 (Pedido de quiebra por un acreedor), CYQ_705 (Citación al deudor (art. 84))

#### D20 · Realización de bienes

El plazo de 4 meses del art. 217 corre desde la quiebra o desde que quedó firme si hubo reposición. ¿Se edita el disparador cuando hay reposición? ¿Se usa la subasta electrónica de la SCBA en la quiebra o rige solo el art. 208 LCQ?

**Hitos afectados:** CYQ_800 (Realización de los bienes), CYQ_805 (Subasta de bienes del fallido)

#### D21 · Distribución y conclusión

¿La conclusión a los 2 años (art. 231) se aplica también a la clausura por falta de activo (art. 232)? La matriz la aplica solo a la distribución final. ¿Desde qué fecha corre la caducidad del dividendo (art. 224): aprobación del proyecto o puesta a disposición?

**Hitos afectados:** CYQ_825 (Cobro del dividendo concursal), CYQ_835 (Conclusión de la quiebra después de la clausura), CYQ_840 (Clausura por falta de activo)

### 3.4 Bloque D · Costos e intereses (transversales a las tres matrices)

Se responden una sola vez acá y valen también para ejecutivos y societarios.

#### D15 · Tasa de justicia en concursos y quiebras

¿Cuándo y sobre qué base se paga la tasa en el concurso preventivo (¿al homologar, sobre el monto del acuerdo?), en el APE y en la quiebra (¿al distribuir?), según el Código Fiscal y la Ley Impositiva 2026 (Ley 15.558)? ¿El acreedor que pide la quiebra paga tasa? ¿La contribución del art. 12 inc. g Ley 6716 es del 5% de la tasa, como dice el texto vigente? Transversal: en ejecutivos y societarios se paga al iniciar.

**Hitos afectados:** CYQ_020 (Resolución del órgano de administración y armado de la presentación), CYQ_100 (Presentación en concurso preventivo), CYQ_700 (Pedido de quiebra por un acreedor)

#### D16 · Honorarios, aportes y bono

En el concurso rigen los arts. 265 a 272 LCQ y no las leyes arancelarias locales (art. 271), salvo en los incidentes (art. 287, Ley 14.967). ¿Se pagan aportes de la Ley 6716 (art. 14: 60 días corridos de firme) sobre los honorarios concursales? ¿El bono de la Ley 8480 se paga por cada incidente? En ejecutivos y societarios: apelación en 5 días fundada (art. 57 Ley 14.967) y aportes en 60 días corridos (art. 14 Ley 6716).

**Hitos afectados:** CYQ_900 (Regulación de honorarios del concurso o la quiebra), CYQ_905 (Apelación de honorarios), CYQ_910 (Pago de aportes de la Ley 6716)

#### D24 · Tasa de interés

En las liquidaciones se usa la tasa de la sentencia o, en su defecto, la doctrina legal de la SCBA (tasa pasiva digital del Banco Provincia a 30 días; interés puro sobre valores actualizados según 'Vera' y 'Nidera'; actualización del crédito según 'Barrios'; números de causa a verificar). Desde la Res. BCRA 1/2026 (BO 09/01/2026) existe la tasa de intereses moratorios del art. 768 inc. c CCyC y algunas Cámaras la aplican. ¿Qué tasa se carga por defecto en el checklist? En el concurso, los intereses quirografarios se suspenden desde la presentación (art. 19).

**Hitos afectados:** CYQ_100 (Presentación en concurso preventivo), CYQ_200 (Pedidos de verificación ante el síndico)

### 3.5 Bloque E · Producto (transversales a las tres matrices)

Las responde el equipo de producto con el abogado. Solo se registran: no se modifican el contrato de API ni el modelo de datos.

#### D03 · Producto: cronograma fijado por el juez

El auto de apertura (art. 14 incs. 3, 9 y 10) y la sentencia de quiebra (art. 88) fijan de una vez las fechas de verificación, de los informes y de la audiencia informativa. Con la app actual, cada fecha se carga cuando se abre su hito (CYQ_200, CYQ_220, CYQ_310, CYQ_400, CYQ_420), semanas o meses después. ¿Se necesita cargar todo el cronograma al registrar el auto de apertura? Propuesta para la V1: el checklist de CYQ_120 y CYQ_720 pide anotarlas; evaluar para la V2 una carga conjunta.

**Hitos afectados:** CYQ_120 (Resolución de apertura o rechazo), CYQ_200 (Pedidos de verificación ante el síndico), CYQ_220 (Informe individual del síndico), CYQ_310 (Informe general del síndico), CYQ_400 (Vencimiento del período de exclusividad: acompañar las conformidades), CYQ_420 (Audiencia informativa), CYQ_720 (Sentencia de quiebra)

#### D25 · Producto: roles del concurso

El enum Rol_Responsable se usó así: ACTORA = deudor; DEMANDADA = acreedores; TRIBUNAL = juzgado, síndico, comité de control, evaluador y enajenador; AMBAS = cualquier interesado. El síndico actúa mucho y queda mezclado con el juzgado. ¿Hacen falta roles propios (SINDICO, ACREEDOR, INTERVENTOR, ORGANISMO) para las tres matrices comerciales? Propuesta para la V1: mantener el enum y aclarar en el nombre del hito. Solo se registra; no se modifica el contrato de API.

**Hitos afectados:** Todos

#### D26 · Producto: el estudio representa a un acreedor

legal_cases.represented_role solo admite ACTORA o DEMANDADA. Si el estudio representa a un acreedor (verificación, impugnación, pedido de quiebra), ¿se elige DEMANDADA? Con eso los hitos del deudor quedan como 'de la otra parte' y los del acreedor como propios, que es lo correcto; pero en el pedido de quiebra el acreedor es quien promueve. ¿Se acepta para la V1? Solo se registra.

**Hitos afectados:** CYQ_010 (Diagnóstico de la insolvencia y elección de la vía), CYQ_200 (Pedidos de verificación ante el síndico), CYQ_450 (Impugnación del acuerdo), CYQ_700 (Pedido de quiebra por un acreedor)

#### D27 · Producto: incidentes como expedientes vinculados

La revisión, la verificación tardía, el pronto pago, la ineficacia, la extensión y la responsabilidad tramitan en pieza separada con número propio (art. 280). ¿Se cargan como expedientes vinculados al principal, cada uno con su flujo, o como hitos del principal? Propuesta para la V1: hitos del principal con el plazo de inicio; el trámite interno del incidente (traslado de 10 días y prueba de 20) va en el checklist.

**Hitos afectados:** CYQ_240 (Incidente de revisión), CYQ_250 (Verificación tardía), CYQ_765 (Ineficacia de actos y acción revocatoria concursal), CYQ_770 (Pedido de extensión de la quiebra), CYQ_775 (Acción de responsabilidad de administradores y terceros)

#### D28 · Producto: vinculación de expedientes en las derivaciones

Las matrices de ejecutivos y de societarios terminan en 'Sigue en la matriz de concursos' cuando el deudor se concursa o quiebra, y societarios deriva a ejecutivos para cobrar la condena. ¿La app permite vincular el expediente de origen con el nuevo y copiar las partes? Solo se registra.

**Hitos afectados:** CYQ_010 (Diagnóstico de la insolvencia y elección de la vía), CYQ_160 (Suspensión de juicios y fuero de atracción)

#### D29 · Producto: flujo prejudicial y judicial

La fase Previa (CYQ_010 a CYQ_030) va al flujo PREJUDICIAL. CYQ_030 (APE) lleva a CYQ_600, que es judicial, y CYQ_010 lleva directo a la quiebra o a la verificación. ¿Se admite una transición entre flujos, como en el laboral? Propuesta: sí.

**Hitos afectados:** CYQ_010 (Diagnóstico de la insolvencia y elección de la vía), CYQ_020 (Resolución del órgano de administración y armado de la presentación), CYQ_030 (Negociación del acuerdo preventivo extrajudicial)

#### D30 · Producto: catálogo de regímenes y fueros

El catálogo solo tiene regímenes laborales. Hace falta uno para la LCQ (por ejemplo, NAC_LEY_24522, porque la ley es nacional aunque la apliquen los juzgados de PBA) y otro para el CPCCBA (PBA_CIV_DL_7425, ya pedido en la matriz sucesoria), que usarían ejecutivos y societarios. También faltan el fuero CIVIL_COMERCIAL, el Juzgado Civil y Comercial en courts.court_type y motivos de cierre como homologación, conclusión o clausura. Solo se registra; no se modifican el contrato de API ni el modelo de datos.

**Hitos afectados:** Todos

#### D31 · Producto: hitos que esperan a otros

La categorización (CYQ_330) necesita la propuesta del deudor (CYQ_300) y las observaciones (CYQ_320); la conclusión de la quiebra necesita los dividendos y los honorarios. La app abre caminos en paralelo pero no espera a que terminen todos. Propuesta para la V1: lo controla el checklist.

**Hitos afectados:** CYQ_330 (Resolución de categorización y comité de control), CYQ_830 (Clausura por distribución final)

## 4. Juicios ejecutivos y cobro de pesos (prefijo `EJE`)

### 4.1 Bloque A · Competencia y títulos

Definen ante qué juzgado se inicia y qué títulos entran por la vía ejecutiva.

#### D01 · Competencia por monto: Juzgados de Paz

¿Hasta qué monto (en Jus) y en qué partidos los juicios ejecutivos y de cobro de pesos tramitan ante los Juzgados de Paz Letrados (art. 61 Ley 5827, a verificar el inciso y el monto vigente)? Allí no hay mediación previa (art. 4 inc. 12 Ley 13.951). ¿Cambia algún plazo de la matriz? Propuesta: el mismo flujo, con la aclaración en el checklist de EJE_010.

**Hitos afectados:** EJE_010 (Mora del deudor y elección de la vía), EJE_050 (Mediación prejudicial), EJE_100 (Presentación de la demanda ejecutiva)

#### D02 · Pagaré de consumo

La SCBA admitió declarar de oficio la incompetencia por el domicilio real del consumidor en ejecuciones de pagarés de consumo ('Cuevas', C. 109.305, resolución del 1/9/2010; el fallo también cita la C. 109.193: verificar cuál es el número correcto), y exigió integrar el pagaré con el contrato para cumplir el art. 36 de la Ley 24.240, acompañando la documentación en primera instancia ('Asociación Mutual Asís c/ Cubilla', C. 121.684, 14/8/2019). ¿Es la doctrina vigente al 13/11/2026? ¿Conviene un hito propio para la intimación a integrar el título, con plazo? Propuesta: checklist en EJE_010 y EJE_100.

**Hitos afectados:** EJE_010 (Mora del deudor y elección de la vía), EJE_100 (Presentación de la demanda ejecutiva)

#### D05 · Factura de crédito electrónica: plazo de aceptación

El art. 6 de la Ley 27.440 prevé la aceptación tácita a los 15 días corridos. Una resolución publicada en el BO el 29/10/2026 (argentina.gob.ar, norma 431777; número 424/2026 según la búsqueda, a verificar) llevó el plazo a 21 días corridos entre el 01/11/2026 y el 31/10/2027 para los arts. 4, 5, 6 y 8. ¿Se agrega un hito previo de espera de la aceptación? ¿Qué plazo se carga? Propuesta: checklist en EJE_010 con el plazo vigente a la fecha de emisión de la factura.

**Hitos afectados:** EJE_010 (Mora del deudor y elección de la vía)

#### D06 · Factura conformada

El art. 521 inc. 5 del CPCCBA sigue nombrando la factura conformada y remite al Código de Comercio, derogado por la Ley 26.994. ¿Sigue siendo título ejecutivo en PBA y bajo qué norma? Propuesta: no incluirla como variante hasta que se confirme.

**Hitos afectados:** EJE_010 (Mora del deudor y elección de la vía)

#### D07 · Tarjeta de crédito

Los arts. 39 a 47 de la Ley 25.065 (preparación de la vía ejecutiva y prescripción) no figuran entre los modificados por el DNU 70/2023 (a verificar). ¿La preparación sigue la audiencia de reconocimiento del art. 523 CPCCBA? ¿El art. 42 (no cobro ejecutivo directo del resumen) obliga siempre a preparar la vía?

**Hitos afectados:** EJE_100 (Presentación de la demanda ejecutiva), EJE_110 (Audiencia de reconocimiento de firma o de documentos), EJE_030 (Control de la prescripción de la acción)

### 4.2 Bloque B · Plazos y cómputo

Cada respuesta cambia un valor, un tipo de plazo o un disparador.

#### D03 · Plazos bancarios

El aviso del rechazo del cheque (2 días hábiles bancarios, art. 39 Ley 24.452) y el protesto del pagaré (2 días hábiles, art. 48 Decreto-Ley 5965/63) se cargaron como días hábiles administrativos, porque el motor no tiene días hábiles bancarios. ¿Es aceptable? Si no, hace falta un tipo de plazo nuevo (solo se registra).

**Hitos afectados:** EJE_020 (Aviso del rechazo del cheque al librador y endosantes), EJE_025 (Protesto del pagaré por falta de pago)

#### D04 · Prescripción según el título

EJE_030 usa el plazo más corto (1 año). Confirmar: cheque 1 año desde el fin del plazo de presentación y cheque de pago diferido desde el rechazo (art. 61 Ley 24.452, texto Ley 27.444); pagaré 3 años contra el suscriptor desde el vencimiento y 1 año contra endosantes (art. 96 Decreto-Ley 5965/63); pagaré a la vista con presentación dentro de 1 año (art. 36); tarjeta 1 año ejecutivo y 3 ordinario (art. 47 Ley 25.065); factura de crédito electrónica (a verificar si remite al régimen del pagaré); genérico 5 años (art. 2560 CCyC). ¿Conviene un hito por título o el abogado ajusta el plazo?

**Hitos afectados:** EJE_030 (Control de la prescripción de la acción)

#### D08 · Mediación en ejecutivos y cobro de pesos

En el juicio ejecutivo la mediación es optativa para el reclamante (art. 5 Ley 13.951) y el plazo es de 30 días corridos (art. 12); en el cobro de pesos es obligatoria y el plazo es de 60. EJE_050 carga 30 (el más corto). ¿Se usa en la práctica la mediación optativa? ¿La exención por cautelar previa (art. 4 inc. 6) alcanza a la demanda posterior al embargo preventivo?

**Hitos afectados:** EJE_050 (Mediación prejudicial), EJE_105 (Embargo preventivo previo: presentar la demanda)

#### D12 · Caducidad de instancia en el ejecutivo

La caducidad es de 3 meses en el ejecutivo y el sumario (art. 310 inc. 2). ¿Corre durante la preparación de la vía? ¿Y en la ejecución de la sentencia de remate (el art. 313 inc. 1 la excluye en la ejecución de sentencia)? Propuesta: corre desde la demanda hasta la sentencia de remate.

**Hitos afectados:** EJE_100 (Presentación de la demanda ejecutiva), EJE_950 (Control de caducidad de instancia)

### 4.3 Bloque C · Trámite hito por hito

Confirman cómo se modeló el juicio ejecutivo y su cumplimiento.

#### D09 · Prueba y sentencia en el ejecutivo

El plazo de prueba lo fija el juez (art. 547): se cargó como fecha fijada. Después, el expediente queda 5 días en secretaría y el juez sentencia en 10 (art. 548). ¿Conviene un hito para los 5 días en secretaría (la práctica es presentar un alegato breve)? Sin excepciones, ¿qué artículo manda dictar sentencia de remate sin más trámite? No se encontró en el texto revisado.

**Hitos afectados:** EJE_240 (Producción de la prueba de las excepciones), EJE_250 (Sentencia de remate)

#### D10 · Apelación de la sentencia de remate

Se cargó apelación en 5 días (art. 244) y memorial en 5 días en relación (art. 246, a verificar que la sentencia de remate se concede en relación). ¿Es correcto? ¿Se admite recurso extraordinario contra la sentencia de remate, que en general no es definitiva? El camino EJE_430 → EJE_440 de la etapa común lo permite.

**Hitos afectados:** EJE_260 (Apelación de la sentencia de remate), EJE_270 (Memorial de la apelación), EJE_430 (Sentencia de la Cámara de Apelación), EJE_440 (Recursos extraordinarios ante la SCBA)

#### D11 · Juicio ordinario posterior

El ordinario posterior (art. 551) lo promueve cualquiera de las partes después de cumplida la condena. No se modeló como camino: ¿se abre como expediente nuevo con el flujo de cobro de pesos y vinculado al ejecutivo? Propuesta: expediente nuevo (duda de producto de vinculación en la matriz de concursos).

**Hitos afectados:** EJE_250 (Sentencia de remate)

#### D13 · Ejecución anticipada con fianza

Si el ejecutante da fianza, el recurso se concede en efecto devolutivo y la ejecución sigue (art. 553): la matriz abre a la vez el memorial y el embargo ejecutorio. Cuando la sentencia queda firme, EJE_450 vuelve a abrir EJE_800. ¿El motor admite abrir de nuevo un hito que ya está abierto, o hay que evitarlo?

**Hitos afectados:** EJE_260 (Apelación de la sentencia de remate), EJE_450 (Sentencia firme (de remate o del juicio sumario)), EJE_800 (Embargo ejecutorio y anotación)

#### D14 · Intereses del título y tasa judicial

En el cheque y el pagaré, ¿se liquidan los intereses pactados en el título o la tasa de la doctrina legal de la SCBA? ¿Se aplica de oficio la morigeración de tasas usurarias (art. 771 CCyC)? La tasa por defecto es la duda transversal de la matriz de concursos.

**Hitos afectados:** EJE_460 (Liquidación de la condena), EJE_870 (Liquidación final)

#### D15 · Subasta electrónica

Confirmar el reglamento vigente de subastas electrónicas de la SCBA (número de acordada a verificar), la duración de la puja (art. 562: 10 días) y si los plazos del bloque de subasta son correctos en PBA.

**Hitos afectados:** EJE_830 (Publicación de edictos de subasta), EJE_840 (Subasta electrónica), EJE_845 (Pedido de nulidad de la subasta), EJE_850 (Aprobación del remate y pago del saldo de precio)

#### D16 · Deudor concursado

Si el deudor se concursa o quiebra durante el juicio, el expediente termina en 'Sigue en la matriz de concursos y quiebras'. Solo se dibujaron las entradas desde EJE_010 y EJE_220, pero puede pasar en cualquier hito. ¿Alcanza con eso o se agrega la salida en todos los hitos? Las ejecuciones con garantía real no se suspenden (art. 21 inc. 1 LCQ).

**Hitos afectados:** EJE_010 (Mora del deudor y elección de la vía), EJE_220 (Oposición de excepciones), EJE_995 (Sigue en la matriz de concursos y quiebras)

### 4.4 Bloque D · Remisiones

Recuerdan dónde se responden las dudas compartidas.

#### D17 · Dudas transversales y de producto

Las dudas que valen para las tres matrices comerciales (vigencia del CPCCBA y de las leyes de fondo, tasa de justicia, bono, aportes, honorarios, ferias, plazo de gracia, notificaciones electrónicas) y las de producto (roles, rol representado, cronogramas, incidentes, vinculación de expedientes, catálogos) se responden una sola vez en matriz_comercial_concursos_pba.xlsx. Las reglas del motor se validan en las dudas D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx y valen también acá. ¿Hay algo de esta matriz que se aparte de esas respuestas?

**Hitos afectados:** Todos

#### D18 · Etapa contenciosa común

La demanda, la contestación, la prueba, la sentencia, los recursos, la caducidad y los honorarios del cobro de pesos son la etapa contenciosa común del CPCCBA. Sus dudas (audiencia preliminar, plazos del sumario, traslado de la pericia, recursos extraordinarios) se responden en matriz_comercial_societarios_pba.xlsx.

**Hitos afectados:** EJE_300 a EJE_460

## 5. Conflictos societarios (prefijo `SOC`)

### 5.1 Bloque A · Régimen y tipo de proceso

Definen qué normas y qué trámite cubre el flujo.

#### D01 · Régimen y vigencia

¿Sigue vigente al 13/11/2026 la Ley 19.550 con las reformas encontradas (Leyes 26.994 y 27.077, Decreto 70/2023 y Resolución MJ 10/2024, que fijó en ARS 2.000.000.000 el capital del art. 299 inc. 2)? ¿Qué normas de la DPPJ rigen la convocatoria administrativa y las inscripciones (Decreto-Ley 8671/76 y disposiciones, a verificar)? ¿Se incluyen las SAS (Ley 27.349), donde la LGS es supletoria? Fuentes: InfoLEG (Ley 19.550, texto actualizado).

**Hitos afectados:** Todos

#### D04 · Tipo de proceso

El art. 15 LGS manda el procedimiento sumario y la matriz usa la etapa contenciosa sumaria del CPCCBA. ¿Hay acciones societarias que tramitan por ordinario en PBA (por ejemplo, la de responsabilidad por su complejidad) o por sumarísimo? Propuesta: sumario, que tiene los plazos más cortos.

**Hitos afectados:** SOC_300 a SOC_460

### 5.2 Bloque B · Plazos y caducidad

Cada respuesta cambia un valor, un tipo de plazo o un disparador; varias definen si una acción caduca.

#### D02 · Mediación y caducidad de 3 meses

La impugnación caduca a los 3 meses de clausurada la asamblea (art. 251) y la mediación obligatoria dura hasta 60 días corridos. El art. 40 de la Ley 13.951 habla de la prescripción; la caducidad, en principio, no se suspende (art. 2567 CCyC, a verificar). ¿La mediación suspende el plazo del art. 251? ¿Está la impugnación excluida de la mediación? Propuesta (lo más seguro): iniciar la mediación de inmediato y presentar la demanda antes de los 3 meses aunque la mediación no haya terminado. Vale también para los 90 días de la exclusión.

**Hitos afectados:** SOC_050 (Plazo de caducidad para impugnar la decisión), SOC_055 (Plazo de caducidad para excluir a un socio), SOC_070 (Mediación prejudicial obligatoria)

#### D03 · Cómputo de los plazos de la LGS

Los plazos en días de la LGS (40 del art. 236, 90 del art. 91, 30 del art. 102 y del art. 103, 15 y 60 del art. 110) se cargaron como días corridos (art. 6 CCyC) y los de meses, por calendario. ¿Es correcto? ¿El plazo de 3 días hábiles del art. 238 es de días hábiles administrativos?

**Hitos afectados:** SOC_030 (Plazo para celebrar la asamblea pedida por accionistas), SOC_055 (Plazo de caducidad para excluir a un socio), SOC_610 (Designación e inscripción del liquidador), SOC_620 (Inventario y balance inicial de liquidación), SOC_640 (Impugnación del balance final), SOC_645 (Acción judicial de impugnación del balance final)

#### D05 · Exclusión de socios

¿En qué tipos sociales procede la exclusión del art. 91 (sociedades de personas, SRL; no en las sociedades por acciones, a verificar)? El plazo de 90 días corre desde que se conoció el hecho: ¿se carga como fecha del disparador ese conocimiento?

**Hitos afectados:** SOC_055 (Plazo de caducidad para excluir a un socio), SOC_105 (Suspensión provisoria de los derechos del socio a excluir)

#### D07 · Impugnación en la SRL

Para las resoluciones de la SRL (art. 159), ¿se aplica el art. 251 con su plazo de 3 meses? ¿Desde cuándo corre si la resolución se tomó por consulta simultánea o declaración escrita?

**Hitos afectados:** SOC_040 (Asamblea o reunión de socios), SOC_050 (Plazo de caducidad para impugnar la decisión)

### 5.3 Bloque C · Trámite hito por hito

Confirman cómo se modeló cada conflicto societario.

#### D06 · Intervención judicial

¿Se aplican en forma conjunta los arts. 113 a 117 LGS y las normas de intervención judicial del CPCCBA (arts. 222 a 227, a verificar)? La matriz abre la intervención solo con la demanda de remoción, porque el art. 114 exige la acción promovida. ¿Algún juzgado la admite antes de la demanda?

**Hitos afectados:** SOC_110 (Pedido de intervención judicial), SOC_120 (Designación del interventor y fijación de su misión), SOC_125 (Apelación de la resolución sobre la intervención), SOC_130 (Vencimiento del término de la intervención)

#### D08 · Pérdida del capital

El art. 59 de la Ley 27.541 (BO 23/12/2019) suspendió la causal de disolución del art. 94 inc. 5 hasta el fin del plazo de su art. 1. ¿Sigue suspendida al 13/11/2026? ¿Qué régimen tiene el art. 94 bis (reducción a uno del número de socios)?

**Hitos afectados:** SOC_600 (Disolución de la sociedad)

#### D09 · Liquidación sin juicio

La disolución y la liquidación muchas veces no pasan por un juzgado. ¿Se cargan en la app como expediente aunque no haya juicio, o solo cuando hay disolución judicial? El liquidador se cargó como DEMANDADA porque es un órgano de la sociedad: ¿es correcto?

**Hitos afectados:** SOC_600 a SOC_650

#### D10 · Derecho de información

¿Cuál es la vía en PBA para el socio a quien le niegan la información: diligencia preliminar de exhibición (art. 323 CPCCBA, inciso a verificar) o demanda sumaria? En la sociedad anónima con sindicatura, ¿el accionista con menos del 2% tiene alguna vía?

**Hitos afectados:** SOC_020 (Pedido de información o exhibición de libros)

#### D11 · Convocatoria administrativa o judicial

¿Qué plazo tiene la DPPJ para convocar? ¿La convocatoria judicial tramita como sumarísimo o como medida urgente sin mediación? Propuesta: SIN_PLAZO y aclaración en el checklist.

**Hitos afectados:** SOC_035 (Convocatoria a asamblea por la DPPJ o por el juez)

#### D12 · Inscripción en la DPPJ

¿Hay plazos para pedir la inscripción de la sentencia en la DPPJ? ¿Qué aranceles se pagan? Propuesta: SIN_PLAZO.

**Hitos afectados:** SOC_480 (Inscripción de la sentencia en la DPPJ)

#### D17 · Cobro de la condena

La condena dineraria no pagada termina en 'Sigue en la matriz de juicios ejecutivos', en el bloque de embargo y subasta (arts. 497 a 508 CPCCBA, a verificar). ¿Es correcto llevar la ejecución de sentencia al mismo bloque que la ejecución de la sentencia de remate?

**Hitos afectados:** SOC_460 (Liquidación de la condena), SOC_900 (Acuerdo, transacción o conciliación), SOC_985 (Sigue en la matriz de juicios ejecutivos (cumplimiento de la sentencia))

#### D18 · Hitos que se abren dos veces

La sentencia de disolución abre a la vez la liquidación (SOC_600) y los honorarios (SOC_960); la liquidación judicial vuelve a abrir los honorarios al final (SOC_650). ¿El motor admite abrir de nuevo un hito ya cerrado? Propuesta: sí, como nueva etapa regulatoria.

**Hitos afectados:** SOC_480 (Inscripción de la sentencia en la DPPJ), SOC_650 (Distribución y cancelación de la inscripción), SOC_960 (Regulación de honorarios y apelación)

### 5.4 Bloque D · Etapa contenciosa común (vale para ejecutivos y societarios)

Se responden una sola vez acá; la matriz de ejecutivos remite a este bloque.

#### D13 · Etapa contenciosa común: audiencia preliminar

La audiencia preliminar se cita como 'Programa de oralidad de la SCBA (a verificar)'. ¿Qué acordada la rige y en qué departamentos judiciales se aplica en el proceso sumario? ¿Qué norma del CPCCBA la prevé (art. 36 inc. 4, a verificar)? Vale para las matrices de ejecutivos y societarios.

**Hitos afectados:** SOC_340 (Audiencia preliminar)

#### D14 · Etapa contenciosa común: plazos del sumario

Confirmar los plazos del sumario: contestación 10 días (art. 484), ampliación de prueba por hechos nuevos 5 días, prueba en una audiencia (art. 487), sin alegatos (art. 493), sentencia en 30 días (art. 494, a verificar), agravios 5 días (art. 254) y caducidad de 3 meses (art. 310 inc. 2). El sumario procede hasta 4500 Jus (art. 320): ¿y el resto de las acciones de la LGS?

**Hitos afectados:** SOC_320 (Contestación de la demanda), SOC_350 (Ampliación de la prueba por hechos nuevos), SOC_400 (Sentencia de primera instancia), SOC_420 (Expresión de agravios), SOC_950 (Control de caducidad de instancia)

#### D15 · Etapa contenciosa común: pericia

El art. 473 CPCCBA prevé el traslado del dictamen pericial sin fijar plazo en el texto revisado. ¿Se usa el plazo general de 5 días (a verificar el artículo)? ¿Conviene un hito propio para la impugnación de la pericia? Propuesta: checklist en la audiencia de prueba.

**Hitos afectados:** SOC_365 (Audiencia de prueba)

#### D16 · Etapa contenciosa común: recursos

Confirmar el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278) y el depósito previo del 10%, con mínimo de 100 y máximo de 500 Jus (art. 280). La Cámara no tiene plazo cargado para sentenciar (SIN_PLAZO): ¿corresponde el del art. 34 inc. 3 c o el del art. 266?

**Hitos afectados:** SOC_430 (Sentencia de la Cámara de Apelación), SOC_440 (Recursos extraordinarios ante la SCBA)

### 5.5 Bloque E · Remisión

Recuerda dónde se responden las dudas transversales y de producto.

#### D19 · Dudas transversales y de producto

Las dudas que valen para las tres matrices comerciales (vigencia del CPCCBA y de las leyes de fondo, tasa de justicia, bono, aportes, honorarios, ferias, plazo de gracia, notificaciones electrónicas) y las de producto (roles, rol representado, cronogramas, incidentes, vinculación de expedientes, catálogos) se responden una sola vez en matriz_comercial_concursos_pba.xlsx. Las reglas del motor se validan en las dudas D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx y valen también acá. ¿Hay algo de esta matriz que se aparte de esas respuestas?

**Hitos afectados:** Todos

## 6. Citas marcadas "(a verificar)" en los hitos

Son las bases normativas y los puntos de checklist que no se pudieron confirmar en una fuente oficial. Ninguna se usa hasta que el abogado la confirme.

### 6.1 Concursos y quiebras (19)

| Hito | Nombre | Texto |
| :--- | :--- | :--- |
| CYQ_010 | Diagnóstico de la insolvencia y elección de la vía | Si el cliente es un acreedor: reunir el título y los hechos reveladores (art. 79) para pedir la quiebra, o verificar si el deudor ya está concursado |
| CYQ_100 | Presentación en concurso preventivo | Pagar el bono de la Ley 8480 y el anticipo previsional del art. 13 Ley 6716; verificar cuándo se paga la tasa de justicia (duda D15) |
| CYQ_125 | Apelación del rechazo de la apertura | Fundar en el plazo del memorial (art. 246 CPCCBA, supletorio; a verificar) |
| CYQ_155 | Informe sobre pasivos laborales y pronto pago | El acreedor laboral puede pedir el pronto pago sin verificar (duda D08) |
| CYQ_160 | Suspensión de juicios y fuero de atracción | Excluidos: expropiación, familia, ejecuciones de garantías reales, procesos de conocimiento en trámite y laborales (salvo opción por verificar), litisconsorcio pasivo necesario y extinción de dominio (art. 21 incs. 1 a 4) |
| CYQ_160 | Suspensión de juicios y fuero de atracción | Juicios llevados por el estudio contra el concursado: pedir la radicación o seguir en el tribunal de origen y verificar con la sentencia (duda D09) |
| CYQ_165 | Contratos con prestaciones recíprocas pendientes | Sin autorización comunicada en el plazo, el cocontratante puede resolver el contrato (art. 20, a verificar el cómputo) |
| CYQ_165 | Contratos con prestaciones recíprocas pendientes | Los servicios públicos no pueden suspenderse por deudas anteriores (art. 20, a verificar) |
| CYQ_240 | Incidente de revisión | La acción por dolo prescribe a los 90 días de la resolución (art. 38, a verificar el cómputo) |
| CYQ_300 | Propuesta de categorización de los acreedores | Controlar las categorías mínimas que exige el art. 41 (a verificar) |
| CYQ_520 | Período para obtener las conformidades en el salvataje | Art. 48 incs. 4 y siguientes y art. 48 bis LCQ (a verificar el disparador) |
| CYQ_600 | Pedido de homologación del acuerdo extrajudicial | Desde la orden de publicar edictos se suspenden las acciones de contenido patrimonial (art. 72, a verificar el alcance) |
| CYQ_700 | Pedido de quiebra por un acreedor | Pagar bono y anticipo previsional; verificar la tasa de justicia (duda D15) |
| CYQ_740 | Conversión de la quiebra en concurso preventivo | Acompañar los requisitos del art. 11 (a verificar el plazo del art. 93) |
| CYQ_805 | Subasta de bienes del fallido | Arts. 208, 211 y 212 LCQ (a verificar el reglamento de subastas electrónicas de la SCBA) |
| CYQ_830 | Clausura por distribución final | Los acreedores no presentados solo pueden verificar si denuncian bienes nuevos |
| CYQ_840 | Clausura por falta de activo | La clausura por falta de activo hace presumir el fraude y se comunica a la justicia penal (art. 233, a verificar) |
| CYQ_910 | Pago de aportes de la Ley 6716 | Art. 14 Ley 6716 (a verificar su aplicación a los honorarios concursales) |
| CYQ_990 | Archivo del expediente | Reglamento de archivo de la SCBA (a verificar) |

### 6.2 Juicios ejecutivos y cobro de pesos (18)

| Hito | Nombre | Texto |
| :--- | :--- | :--- |
| EJE_010 | Mora del deudor y elección de la vía | Factura de crédito electrónica: verificar en el registro de AFIP-ARCA que esté aceptada en forma expresa o tácita (art. 6 Ley 27.440; duda D05) |
| EJE_020 | Aviso del rechazo del cheque al librador y endosantes | Dar aviso del rechazo al librador y a los endosantes dentro de los 2 días hábiles bancarios (art. 39); verificar si la omisión hace perder la acción o solo genera responsabilidad (a verificar) |
| EJE_025 | Protesto del pagaré por falta de pago | Dar los avisos a los endosantes y avalistas en el plazo del art. 49 (a verificar el plazo) |
| EJE_025 | Protesto del pagaré por falta de pago | La falta de protesto hace perder las acciones de regreso contra los endosantes, no contra el suscriptor (art. 60, a verificar) |
| EJE_030 | Control de la prescripción de la acción | La mediación suspende la prescripción (art. 40 Ley 13.951; a verificar la remisión al CCyC) |
| EJE_040 | Intimación extrajudicial de pago | Art. 886 CCyC (mora automática; a verificar) |
| EJE_105 | Embargo preventivo previo: presentar la demanda | Verificar el inciso del art. 209 que habilita el embargo según el título (a verificar) |
| EJE_250 | Sentencia de remate | Sin excepciones, el juez dicta sentencia de remate sin más trámite (a verificar el artículo) |
| EJE_270 | Memorial de la apelación | Art. 246 CPCCBA (recurso en relación; a verificar) |
| EJE_340 | Audiencia preliminar | Programa de oralidad de la SCBA (a verificar); art. 36 inc. 4 CPCCBA (a verificar) |
| EJE_365 | Audiencia de prueba | Controlar el traslado del dictamen pericial e impugnarlo o pedir explicaciones (art. 473; plazo del traslado a verificar) |
| EJE_430 | Sentencia de la Cámara de Apelación | Arts. 34 inc. 3 c y 266 CPCCBA (a verificar) |
| EJE_440 | Recursos extraordinarios ante la SCBA | Verificar el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278, a verificar) |
| EJE_805 | Informes previos y constatación del bien | Arts. 558 inc. 2 y 4 y 568 a 570 CPCCBA; mandamiento de constatación (a verificar) |
| EJE_840 | Subasta electrónica | Art. 562 CPCCBA; reglamento de subastas electrónicas de la SCBA (a verificar) |
| EJE_990 | Archivo del expediente | Reglamento de archivo de la SCBA (a verificar) |
| EJE_995 | Sigue en la matriz de concursos y quiebras | Las ejecuciones de garantías reales no se suspenden, pero requieren verificar el crédito (art. 21 inc. 1) |
| EJE_995 | Sigue en la matriz de concursos y quiebras | Pedir el desglose del título original para verificar |

### 6.3 Conflictos societarios (14)

| Hito | Nombre | Texto |
| :--- | :--- | :--- |
| SOC_020 | Pedido de información o exhibición de libros | Arts. 55 y 294 inc. 6 LGS; art. 323 CPCCBA (a verificar el inciso) |
| SOC_035 | Convocatoria a asamblea por la DPPJ o por el juez | Art. 236 LGS; normativa de la DPPJ (a verificar) |
| SOC_035 | Convocatoria a asamblea por la DPPJ o por el juez | La convocatoria judicial no requiere mediación previa si se plantea como medida urgente (a verificar) |
| SOC_110 | Pedido de intervención judicial | Arts. 113, 114 y 116 LGS; arts. 222 a 227 CPCCBA (a verificar) |
| SOC_125 | Apelación de la resolución sobre la intervención | Fundar en el plazo del memorial (art. 246 CPCCBA, a verificar) |
| SOC_340 | Audiencia preliminar | Programa de oralidad de la SCBA (a verificar); art. 36 inc. 4 CPCCBA (a verificar) |
| SOC_365 | Audiencia de prueba | Controlar el traslado del dictamen pericial e impugnarlo o pedir explicaciones (art. 473; plazo del traslado a verificar) |
| SOC_430 | Sentencia de la Cámara de Apelación | Arts. 34 inc. 3 c y 266 CPCCBA (a verificar) |
| SOC_440 | Recursos extraordinarios ante la SCBA | Verificar el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278, a verificar) |
| SOC_600 | Disolución de la sociedad | Reducción a uno del número de socios: régimen del art. 94 bis (a verificar) |
| SOC_630 | Informe trimestral del liquidador | En las sociedades por acciones informa a la sindicatura (a verificar) |
| SOC_645 | Acción judicial de impugnación del balance final | Requiere mediación previa (a verificar) |
| SOC_990 | Archivo del expediente | Reglamento de archivo de la SCBA (a verificar) |
| SOC_985 | Sigue en la matriz de juicios ejecutivos (cumplimiento de la sentencia) | Arts. 497 a 508 CPCCBA (a verificar) |

## 7. Decisiones de modelado a confirmar

No son dudas de la planilla, pero cambian cómo se ve el flujo. Si el abogado no está de acuerdo con alguna, se abre como duda nueva.

1. **Concursos: la verificación y el informe general son los mismos hitos para el concurso preventivo y la quiebra** (`CYQ_200` a `CYQ_320`). La condición de salida dice por qué camino sigue. La alternativa es duplicar esos hitos para la quiebra.
2. **Concursos: la verificación tardía (`CYQ_250`) se abre con la presentación en concurso**, porque el plazo de 2 años del art. 56 corre desde ahí, aunque el acreedor recién la pida mucho después.
3. **Concursos: la quiebra indirecta entra a la sentencia de quiebra (`CYQ_720`) desde ocho hitos distintos** (sin conformidades, impugnación admitida, homologación rechazada, honorarios impagos, nulidad, incumplimiento, salvataje sin inscriptos o sin conformidades).
4. **Concursos no usa la etapa contenciosa común ni el bloque de subasta del CPCCBA:** tiene su propia liquidación (arts. 203 a 224 LCQ).
5. **Ejecutivos y societarios usan los plazos del juicio sumario** (los más cortos; art. 15 LGS para societarios). `datos/comun.py` también tiene los plazos del ordinario, por si el abogado indica que alguna acción tramita por esa vía (societarios D04).
6. **Societarios no repite el bloque de subasta:** si la condena no se paga, el expediente sigue en la matriz de ejecutivos (societarios D17).
7. **Las dudas de ejecutivos citan carátulas públicas de la SCBA con apellidos** ("Cuevas", "Asociación Mutual Asís c/ Cubilla"). Si se prefiere no usar nombres en la planilla, se pueden dejar solo los números de causa.

## 8. Después de validar

1. Pasar a `VALIDADO` o `CORREGIR` cada duda, hito y transición de las tres planillas.
2. Completar en la hoja `Flujo` de cada planilla quién validó y la fecha.
3. Regenerar solo los diagramas desde las planillas, con `diagrama.py` (ver [`README.md`](README.md)).
4. Llevar las respuestas de producto (bloque E de concursos) al equipo técnico.
