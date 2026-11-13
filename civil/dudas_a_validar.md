# Dudas y puntos a validar · Fuero Civil y Comercial PBA

**Estado:** borrador para validar · **Fecha:** 13/11/2026 · **Versión de las matrices:** 1 (borrador)

Este documento reúne lo que el abogado tiene que validar en las cinco matrices de esta carpeta: las 113 dudas de las hojas `Dudas_a_validar`, por flujo, y las citas y datos que quedaron marcados "(a verificar)" en los hitos. El texto de cada duda es el mismo que el de la planilla. Se genera desde `datos/`; si cambia una duda en la planilla, la planilla manda.

---

## 1. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal` de la hoja `Dudas_a_validar`, con la norma o la acordada que la sostiene, y `Estado` pasa de `PENDIENTE` a `VALIDADO` o `CORREGIR`. Si la respuesta cambia un hito o un camino, se corrige también la fila en `Nodos` o en `Transiciones`.
- **Además de las dudas, cada fila se valida** con `Estado_Validacion` (hoy todas en `PENDIENTE`): sucesorio 60 hitos y 130 transiciones, daños y perjuicios 59 hitos y 135 transiciones, desalojo 50 hitos y 117 transiciones, prescripción adquisitiva 49 hitos y 113 transiciones, incumplimiento contractual 60 hitos y 139 transiciones. El control "filas pendientes" de la hoja `Flujo` las cuenta.
- **Cada duda se responde una sola vez:**
  - las de la **etapa contenciosa común** (demanda, prueba, sentencia, recursos, ejecución, honorarios, caducidad), en daños y perjuicios;
  - las del **producto** (roles, rol representado, régimen procesal, catálogos), en el sucesorio;
  - las **reglas del motor** (D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx`) no se repiten: el sucesorio y daños y perjuicios preguntan si valen sin cambios para el fuero civil.
- **Ante la duda, el vencimiento más temprano.** Hasta que el abogado confirme una cita "(a verificar)", la app no la usa para calcular.
- **No correr `generar.py` sobre una planilla que el abogado ya empezó a completar:** la pisa con lo que hay en `datos/` (ver [`README.md`](README.md)).

## 2. Por dónde empezar

Las cinco que atraviesan todos los flujos:

| Duda | Tema | Por qué primero |
| :--- | :--- | :--- |
| SUC D32 y D33 | Roles y rol representado | Si el cliente es el demandado, o un coheredero que impugna, los avisos de "te toca a vos" quedan invertidos. |
| SUC D35 y CTR D01 | Régimen procesal: voluntario, sumario y ordinario | Sin ese catálogo las matrices no se pueden importar, y define si hacen falta versiones sumarias. |
| SUC D40 y USU D01 | Tope de 10 años en la app | La usucapión larga exige 20 años. |
| SUC D41 y DYP D30 | Reglas del motor en el fuero civil | Feria, plazo de gracia y días corridos valen para todos los vencimientos. |
| DYP D22 y DYP D23 | Tasa de justicia, aportes y honorarios | Montos y alícuotas siguen "a verificar" y bloquean la sentencia, la inscripción y el archivo. |

Las tres de mayor impacto de cada flujo:

| Flujo | Dudas |
| :--- | :--- |
| Sucesorio | D05 (plazo de 15 días del ITGB), D16 (inventario en 3 meses), D24 (tracto abreviado) |
| Daños y perjuicios | D01 (sumario u ordinario), D02 (prescripción de 3 años, 2 en transporte), D04 (plazo de respuesta de la aseguradora) |
| Desalojo | D01 (régimen de locaciones tras el DNU 70/2023), D04 (desocupación inmediata), D08 (ocupantes vulnerables y Ley 14.449) |
| Prescripción adquisitiva | D01 (años máximos), D03 (plano y Geodesia), D05 y D06 (plazos del Defensor Oficial y del Fisco) |
| Contratos | D01 (tipo de proceso), D02 (prescripción de 5 o 3 años), D08 (texto vigente de los arts. 1201 y 1221) |

## 3. Sucesorio (`SUC`)

Planilla: [`matriz_civil_sucesorio_pba.xlsx`](matriz_civil_sucesorio_pba.xlsx) · diagrama: [`diagrama_civil_sucesorio_pba.md`](diagrama_civil_sucesorio_pba.md). 41 dudas. Incluye las dudas técnicas del producto (D32 a D40), que se responden solo acá, y la que remite a las reglas del motor (D41).

### SUC D01 · Edictos

El art. 2340 CCyC manda publicar 1 día en el diario de publicaciones oficiales; el art. 734 CPCCBA, 3 días en el Boletín Judicial y en otro diario (solo Boletín Judicial si el haber no supera 900 Jus). La Cámara Civil de Trenque Lauquen (24/9/2019) aceptó que la heredera se atuviera al art. 2340. ¿Qué ordenan hoy los juzgados de PBA? Propuesta: el checklist explica las dos opciones y manda seguir la providencia.

**Hitos afectados:** SUC_200, SUC_320

### SUC D02 · Cómputo de la citación

¿Los 30 días de la citación son corridos (así lo dice el art. 734) y corren desde la última publicación o desde el día siguiente (art. 147)? ¿Corren durante la feria? Propuesta: corridos, desde la última publicación y sin descontar la feria (vencimiento más temprano).

**Hitos afectados:** SUC_205, SUC_320

### SUC D03 · Juzgados de Paz

Fuera de los partidos del conurbano, los Juzgados de Paz Letrados tramitan sucesiones (art. 61 Ley 5827). ¿El flujo es el mismo? ¿Hay un límite de monto (a verificar)?

**Hitos afectados:** SUC_020, SUC_100

### SUC D04 · Gastos de inicio

¿El bono de la Ley 8480 y el anticipo de la Ley 6716 se pagan al promover el sucesorio, y la tasa de justicia recién al pedir la inscripción (Código Fiscal, a verificar el artículo del t.o. vigente)? ¿Qué exenciones hay (por ejemplo, vivienda única, a verificar)?

**Hitos afectados:** SUC_100, SUC_820

### SUC D05 · ITGB: plazo de 15 días

¿Los 15 días para pagar el ITGB desde la solicitud judicial de inscripción son corridos o hábiles administrativos? Propuesta: corridos (vencimiento más temprano). ¿El artículo es el 322 inc. b del Código Fiscal en el t.o. vigente?

**Hitos afectados:** SUC_016, SUC_810

### SUC D06 · ITGB: mínimos y declaración

Según ARBA (26/01/2026), los mínimos no imponibles de 2026 son $23.343.337 para padres, hijos y cónyuge y $5.606.568 para los demás (a verificar contra la Ley Impositiva 15.558). ¿Hay que presentar la declaración jurada aunque no se supere el mínimo?

**Hitos afectados:** SUC_016, SUC_810

### SUC D07 · Intimación a aceptar

El juez fija el plazo de la intimación entre 1 y 3 meses (art. 2289 CCyC); la matriz lo deja SIN_PLAZO para que el abogado lo cargue. ¿Conviene usar 1 mes (el mínimo) como valor por defecto?

**Hitos afectados:** SUC_430

### SUC D08 · Caducidad del derecho de aceptar

¿Los 10 años del art. 2288 se cuentan siempre desde el fallecimiento? ¿La app debe pedir la fecha de un llamado posterior (renuncia o exclusión de otro heredero)?

**Hitos afectados:** SUC_015

### SUC D09 · Testamento ológrafo

El art. 739 CPCCBA prevé el reconocimiento por dos testigos; el art. 2339 CCyC, la pericia caligráfica. ¿Qué se ordena en la práctica? ¿Hace falta un hito propio para la pericia?

**Hitos afectados:** SUC_300, SUC_305

### SUC D10 · Herederos instituidos

¿El plazo de citación del art. 742 es de 30 días corridos, como el del art. 734? ¿Corre desde la última publicación?

**Hitos afectados:** SUC_320

### SUC D11 · Registro de Juicios Universales

¿Qué acordada de la SCBA regula hoy el Registro de Juicios Universales y si hay un plazo para pedir la inscripción? Propuesta: SIN_PLAZO.

**Hitos afectados:** SUC_100, SUC_125

### SUC D12 · Registro de Testamentos

Si el causante vivió en otra provincia, ¿se piden también los informes de los registros de esa jurisdicción o del registro nacional? ¿Desde cuándo se espera la respuesta?

**Hitos afectados:** SUC_120

### SUC D13 · Rendición de cuentas

El art. 748 CPCCBA admite otro plazo si lo acuerda la mayoría; el art. 2355 CCyC, si lo fija el juez. ¿Los 3 meses corren desde la aceptación del cargo? ¿Rinde también el administrador provisional?

**Hitos afectados:** SUC_140, SUC_505

### SUC D14 · Observaciones a la rendición

¿Los 5 días (parcial) y 10 días (final) del art. 748 son hábiles judiciales y corren desde la notificación de la providencia que pone la cuenta en secretaría?

**Hitos afectados:** SUC_510

### SUC D15 · Inventario

¿Cuándo se exige hoy el inventario judicial y cuándo alcanza la denuncia de bienes (art. 751)? ¿ARBA suele pedir inventario judicial?

**Hitos afectados:** SUC_600, SUC_610, SUC_800

### SUC D16 · Inventario en 3 meses

¿Los 3 meses del art. 2321 CCyC corren desde la notificación de la intimación judicial? ¿Hace falta alertarlo si no representamos a quien fue intimado?

**Hitos afectados:** SUC_602

### SUC D17 · Traslado del inventario

¿Los 5 días del art. 759 son hábiles y corren desde la notificación por cédula?

**Hitos afectados:** SUC_620

### SUC D18 · Cuenta particionaria

¿Los 10 días del art. 766 son hábiles y desde la notificación por cédula? ¿Qué resoluciones de la partición son apelables?

**Hitos afectados:** SUC_715, SUC_725

### SUC D19 · Plazo del partidor

El juez fija el plazo del partidor (art. 763). ¿Hay un plazo habitual que convenga proponer?

**Hitos afectados:** SUC_710

### SUC D20 · Cónyuge supérstite

¿Se modela la liquidación de la comunidad de gananciales como un hito propio o alcanza con el checklist del inventario? ¿Y la indivisión poscomunitaria?

**Hitos afectados:** SUC_600

### SUC D21 · Unión convivencial

El conviviente no hereda, pero puede pedir el derecho real de habitación gratuito (art. 527 CCyC). ¿Se agrega un hito con su plazo?

**Hitos afectados:** SUC_010

### SUC D22 · Causante extranjero o bienes en el exterior

¿Basta con el checklist (arts. 2643 y 2644 CCyC, a verificar) o hace falta un flujo aparte para el exhorto internacional?

**Hitos afectados:** SUC_010, SUC_850

### SUC D23 · Bienes en otra provincia

¿Se inscribe por oficio de la Ley 22.172 o hace falta abrir sucesorio en la otra provincia? ¿Qué requisitos pide el registro de destino?

**Hitos afectados:** SUC_850

### SUC D24 · Tracto abreviado

Si los herederos venden sin inscribir (art. 16 Ley 17.801, a verificar), ¿el sucesorio termina ahí para la app o sigue con las demás inscripciones?

**Hitos afectados:** SUC_850, SUC_980

### SUC D25 · Sucesión extrajudicial

¿Qué alcance tiene hoy el art. 733 CPCCBA y cuándo se usa? ¿El expediente se cierra en la app al autorizarlo?

**Hitos afectados:** SUC_405, SUC_980

### SUC D26 · Requisitos registrales

¿El Registro de la Propiedad Inmueble de PBA exige libre deuda de ARBA o municipal, minuta o formulario para inscribir la declaratoria o las hijuelas? ¿Qué pide el DNRPA para los automotores?

**Hitos afectados:** SUC_850, SUC_855, SUC_860

### SUC D27 · Caducidad de instancia

¿Corre la caducidad en el sucesorio o solo en sus incidentes? Propuesta: alertar a los 6 meses (art. 310 inc. 1), que es la opción que no pierde un vencimiento.

**Hitos afectados:** SUC_925, SUC_930

### SUC D28 · Apelaciones

¿Todas las apelaciones del sucesorio se conceden en relación, con memorial de 5 días (art. 246)? ¿Desde cuándo corre el memorial?

**Hitos afectados:** SUC_900, SUC_905

### SUC D29 · Honorarios

¿En qué momento se regulan los honorarios del sucesorio, sobre qué base y por etapas (Ley 14.967, a verificar el artículo)? ¿Quién los paga?

**Hitos afectados:** SUC_915, SUC_920, SUC_980

### SUC D30 · Acreedores

Si representamos a un acreedor que promueve el sucesorio (art. 729), ¿se usa esta matriz u otra? Los roles quedarían invertidos.

**Hitos afectados:** SUC_010, SUC_100

### SUC D31 · Herencia vacante

¿Hace falta modelar el trámite con el curador y el remate (arts. 768 a 771) o basta con cerrar el flujo?

**Hitos afectados:** SUC_450

### SUC D32 · Producto: roles

Los roles de la app son ACTORA, DEMANDADA, TRIBUNAL y AMBAS. El civil tiene figuras que no encajan: interesados del sucesorio, organismos (registros, ARBA, escribano), la aseguradora citada en garantía. ¿Se agregan roles (por ejemplo INTERESADO, ORGANISMO, CITADO_EN_GARANTIA) o se explica el uso en cada matriz, como ahora? Solo se registra; no se modifican el contrato de API ni el modelo.

**Hitos afectados:** Todos

### SUC D33 · Producto: rol representado

legal_cases.represented_role solo admite ACTORA o DEMANDADA. El sucesorio no tiene demandado y en la usucapión el demandado puede ser indeterminado. Si representamos al coheredero que impugna, las alertas de 'te toca a vos' quedan invertidas. ¿Se agrega un valor o el rol se define por hito? Solo se registra.

**Hitos afectados:** SUC_310, SUC_415, SUC_625

### SUC D34 · Producto: hitos prejudiciales

La fase Previa se importa como flujo PREJUDICIAL (flows.flow_kind). En el civil, varios plazos de esa fase siguen corriendo durante el juicio (caducidad de 10 años, ITGB a 24 meses, prescripción). ¿Cómo se vinculan con el flujo judicial? Solo se registra.

**Hitos afectados:** SUC_015, SUC_016

### SUC D35 · Producto: régimen procesal

procedural_regimes solo tiene PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057. ¿Se agrega uno civil (por ejemplo PBA_CIV_DL_7425) o uno por proceso (ordinario, sumario, sucesorio, usucapión)? Hace falta también el fuero Civil y Comercial en legal_branches. Solo se registra.

**Hitos afectados:** Todos

### SUC D36 · Producto: juzgados

courts.court_type tiene TRIBUNAL_TRABAJO, JUZGADO_LABORAL y CAMARA_APELACION. Faltan el Juzgado Civil y Comercial y el Juzgado de Paz Letrado. Solo se registra.

**Hitos afectados:** Todos

### SUC D37 · Producto: límite FIN_DEL_DIA

Los plazos de fondo del CCyC vencen a las 24 horas (art. 6), pero la planilla no tiene la columna Limite_Horario y el importador usa CIERRE_HORARIO_JUDICIAL (ver D28 de la matriz laboral general). En el civil hay muchos: ¿se agrega la columna ya?

**Hitos afectados:** SUC_015, SUC_016, SUC_602, SUC_810

### SUC D38 · Producto: caminos que vuelven atrás

Algunos caminos vuelven a un hito anterior (rendición trimestral, declaratoria diferida, remoción del partidor). ¿El motor permite reabrir un hito ya cumplido?

**Hitos afectados:** SUC_405, SUC_510, SUC_710

### SUC D39 · Producto: plazos con rango legal

Hay plazos que fija el juez dentro de un rango legal (intimación a aceptar: 1 a 3 meses). ¿La app debería validar el rango al cargar el plazo suelto?

**Hitos afectados:** SUC_430

### SUC D40 · Producto: años máximos

MAX_VALOR admite hasta 10 años. Alcanza para el art. 2288, pero no para la usucapión larga de 20 años (ver la matriz de prescripción adquisitiva). Solo se registra.

**Hitos afectados:** SUC_015

### SUC D41 · Reglas del motor

Las reglas del motor de plazos (D26 a D34: gracia, hora límite, notificación electrónica, meses y años, horas, anticipación) se responden una sola vez en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para el fuero civil? Las diferencias propias del civil (ferias en la caducidad, plazos corridos de fondo) tienen sus propias dudas.

**Hitos afectados:** Todos

## 4. Daños y perjuicios (`DYP`)

Planilla: [`matriz_civil_danos_y_perjuicios_pba.xlsx`](matriz_civil_danos_y_perjuicios_pba.xlsx) · diagrama: [`diagrama_civil_danos_y_perjuicios_pba.md`](diagrama_civil_danos_y_perjuicios_pba.md). 30 dudas. Incluye las dudas de la etapa contenciosa común (D15 a D28), que se responden solo acá y valen para desalojo, prescripción adquisitiva y contratos.

### DYP D01 · Tipo de proceso

La matriz usa el juicio sumario: los daños por delitos y cuasidelitos tramitan así cualquiera sea el monto (art. 320 inc. 2 k CPCCBA). Los daños por incumplimiento contractual son sumario hasta 4.500 Jus (art. 320 inc. 1) y ordinario por encima. ¿La mala praxis de un establecimiento privado (responsabilidad contractual con el paciente) se trata como cuasidelito? ¿Hace falta una versión ordinaria de esta matriz para los contractuales de monto alto?

**Hitos afectados:** DYP_050, DYP_300, DYP_340

### DYP D02 · Prescripción

La matriz usa 3 años (art. 2561 CCyC) para todas las variantes, desde el hecho o desde que el daño se manifestó (art. 2554: desde que es exigible). ¿Es correcto para el incumplimiento contractual o rige el plazo general de 5 años (art. 2560)? En mala praxis, ¿desde cuándo se cuenta si el daño aparece después?

**Hitos afectados:** DYP_015

### DYP D03 · Suspensión por interpelación

La interpelación fehaciente suspende la prescripción una sola vez y hasta 6 meses (art. 2541). La matriz abre un hito de alerta de 6 meses, pero el vencimiento de DYP_015 no se corre solo: el abogado lo edita. ¿Alcanza o la app debería recalcularlo?

**Hitos afectados:** DYP_015, DYP_017

### DYP D04 · Reclamo a la aseguradora

El plazo de 30 días para que la aseguradora se pronuncie (art. 56 Ley 17.418) está previsto para el asegurado. ¿Hay un plazo para responder al tercero damnificado (normativa de la Superintendencia de Seguros, a verificar)? Si no lo hay, ¿el hito pasa a SIN_PLAZO?

**Hitos afectados:** DYP_024

### DYP D05 · Historia clínica

La copia se entrega dentro de las 48 horas de pedida (art. 14 Ley 26.529). El tipo HORAS cuenta horas corridas, incluidos fines de semana. ¿Es el criterio correcto?

**Hitos afectados:** DYP_042

### DYP D06 · Mediación

La mediación prejudicial es obligatoria para los reclamos de daños (Ley 13.951), salvo, entre otras, las acciones de menores con intervención del Ministerio Público (art. 4). ¿Se requiere también a la aseguradora? ¿Qué reglamentación vigente fija el pago inicial y el formulario (a verificar)?

**Hitos afectados:** DYP_080, DYP_082, DYP_084

### DYP D07 · Citación en garantía

El damnificado puede citar a la aseguradora hasta que la causa se abre a prueba (art. 118 Ley 17.418). La matriz lo deja en el checklist de la demanda y da a la aseguradora el mismo plazo que a la demandada (10 días en el sumario). ¿Es ese el plazo? ¿Conviene un hito con vencimiento en la apertura a prueba?

**Hitos afectados:** DYP_300, DYP_345, DYP_400

### DYP D08 · Causa penal

El juez civil no dicta sentencia mientras la causa penal sigue abierta, salvo las excepciones del art. 1775 CCyC; en los choques suele aplicarse la del factor objetivo (riesgo de la cosa). La matriz pone la suspensión como un hito antes de la sentencia. ¿Es el lugar correcto o se plantea antes?

**Hitos afectados:** DYP_030, DYP_495

### DYP D09 · Límite de cobertura y franquicia

La sentencia se ejecuta contra la aseguradora en la medida del seguro (art. 118 Ley 17.418). ¿Qué criterio sigue hoy la SCBA sobre la oponibilidad del límite de cobertura y la franquicia del transporte público al damnificado (a verificar)? ¿Hace falta un hito propio para el reclamo del saldo?

**Hitos afectados:** DYP_020, DYP_725

### DYP D10 · Acuerdos con incapaces

Si el damnificado es menor de edad o tiene capacidad restringida, el acuerdo extrajudicial o judicial necesita intervención del Ministerio Público y aprobación del juez (a verificar). ¿El convenio extrajudicial debe pasar por la homologación (DYP_800) en ese caso?

**Hitos afectados:** DYP_024, DYP_090, DYP_800

### DYP D11 · Estado como responsable

Si el responsable es el Estado provincial o un municipio (hospital público, calle en mal estado), el reclamo va al fuero contencioso administrativo. La matriz solo lo advierte en la consulta. ¿Hace falta otro flujo?

**Hitos afectados:** DYP_010

### DYP D12 · Relación de consumo

En los reclamos de consumo rige el proceso más abreviado de la jurisdicción (art. 53 Ley 24.240), que en PBA podría ser el sumarísimo (art. 496), y el beneficio de gratuidad. ¿Qué proceso se usa y cómo se carga la gratuidad frente a la tasa de justicia?

**Hitos afectados:** DYP_050, DYP_300

### DYP D13 · Prueba anticipada

La prueba anticipada (arts. 326 y 327 CPCCBA) no tiene plazo legal: el juzgado fija la producción. La matriz la deja SIN_PLAZO. ¿Es correcto? ¿Se usa también el habeas data del art. 20 Ley 26.529 para la historia clínica?

**Hitos afectados:** DYP_046

### DYP D14 · Daños a bienes

Cuando el daño sigue produciéndose (filtraciones, obras vecinas), se puede pedir la acción preventiva (art. 1711 CCyC) o una cautelar. La matriz no tiene un hito propio. ¿Hace falta?

**Hitos afectados:** DYP_060, DYP_320

### DYP D15 · Etapa común: tipo de proceso

Cada matriz usa un solo tipo de proceso (ordinario o sumario), que cambia plazos: contestación 15 o 10 días, agravios 10 o 5, caducidad 6 o 3 meses, y excepciones previas aparte o con la contestación. Si un caso del mismo tipo tramita por el otro proceso (por el monto, art. 320 inc. 1, o porque el juez lo decide), ¿se publica una segunda versión del flujo o el abogado edita los plazos? Propuesta: el abogado edita; se publica otra versión solo si el caso es frecuente.

**Hitos afectados:** DYP_340, DYP_610, DYP_615, DYP_900

### DYP D16 · Etapa común: audiencia preliminar

¿Qué juzgados civiles aplican el programa de oralidad (Res. SCBA 2761/16) con audiencia preliminar y audiencia de vista de causa? En el ordinario, ¿la prueba se ofrece antes de la audiencia preliminar (art. 365) o en ella? ¿Hay una norma del CPCCBA que la regule (art. 36, a verificar)?

**Hitos afectados:** DYP_400, DYP_410, DYP_415, DYP_440

### DYP D17 · Etapa común: informes

El plazo para contestar oficios es de 20 días hábiles para oficinas públicas y 10 para entidades privadas (art. 396). La app usa 10 por defecto porque de ese vencimiento depende el plazo de 5 días para pedir la reiteración (art. 400). ¿Es correcto o conviene separar el hito en dos?

**Hitos afectados:** DYP_430, DYP_435

### DYP D18 · Etapa común: dictamen pericial

En el ordinario, ¿los 30 días del perito (art. 459) son hábiles y corren desde la aceptación del cargo? En el sumario, el dictamen va 5 días antes de la audiencia (art. 492): ¿se modela bien como plazo hacia atrás (ANTICIPACION_HABILES_JUDICIALES)?

**Hitos afectados:** DYP_420

### DYP D19 · Etapa común: alegatos en el sumario

El art. 480 fija 6 días para alegar en el ordinario. ¿Hay alegatos en el juicio sumario (art. 495, normas supletorias)? Propuesta: dejar el hito con 6 días, porque es la opción que no pierde un vencimiento.

**Hitos afectados:** DYP_450

### DYP D20 · Etapa común: caducidad de instancia

El cómputo de la caducidad no cuenta las ferias (art. 311), pero el tipo MESES cuenta de fecha a fecha y la app alerta antes. ¿Es aceptable o hace falta un tipo de plazo que descuente las ferias? ¿Aplica el plazo de gracia al acto de impulso? Propuesta: sin gracia y sin descontar ferias (vencimiento más temprano).

**Hitos afectados:** DYP_900, DYP_905

### DYP D21 · Etapa común: rebeldía

Si la demandada no comparece, la actora pide la rebeldía (art. 59 CPCCBA), que se notifica por cédula o edictos, y el proceso sigue su curso (art. 60). La matriz no tiene un hito propio: 'No contesta en término' lleva a la apertura a prueba. ¿Alcanza o conviene un hito para el pedido y la notificación de la rebeldía?

**Hitos afectados:** DYP_340

### DYP D22 · Etapa común: tasa de justicia y aportes

Al iniciar se pagan la tasa de justicia, la contribución del 5 % (art. 12 inc. g Ley 6716), el bono de la Ley 8480 y el anticipo previsional de la Ley 6716. ¿Cuál es la alícuota vigente en 2026 (Ley Impositiva 15.558, a verificar), qué pasa si se demanda por monto indeterminado y cuándo se integra el saldo (por ejemplo, con la sentencia o el acuerdo)? ¿Conviene un hito propio para la intimación a integrar la tasa?

**Hitos afectados:** DYP_300, DYP_800, DYP_990

### DYP D23 · Etapa común: honorarios

El pago de honorarios firmes va en 10 días (art. 54 Ley 14.967) y su apelación en 5 días, fundada (art. 57). ¿Los 10 días son hábiles judiciales? ¿Cuándo se depositan los aportes de la Ley 6716 y qué porcentaje (a verificar)?

**Hitos afectados:** DYP_510, DYP_515, DYP_730

### DYP D24 · Etapa común: recursos extraordinarios

¿Cuál es el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278) y el valor del Jus a la fecha, para calcular el depósito previo (art. 280)? El memorial ante la SCBA va en 10 días desde la providencia de autos (art. 284): ¿se notifica por cédula o queda notificada por nota?

**Hitos afectados:** DYP_630, DYP_645

### DYP D25 · Etapa común: apelación de interlocutorias

Para apelar una excepción admitida, una cautelar o el beneficio, la matriz usa un solo hito con el memorial de 5 días desde la concesión (art. 246); los 5 días para apelar (art. 244) quedan en el checklist. ¿Conviene separarlos en dos hitos?

**Hitos afectados:** DYP_650

### DYP D26 · Etapa común: cautelar antes de la demanda

Si una medida cautelar se traba antes de demandar, la demanda debe presentarse dentro de los 10 días de la traba (art. 207; 5 días en la prohibición de contratar, art. 231) o la medida caduca de pleno derecho. Hoy queda en el checklist. ¿Se agrega un hito de 10 días hábiles en la etapa previa de cada flujo?

**Hitos afectados:** DYP_320

### DYP D27 · Etapa común: plazos corridos y feria

El civil usa muchos plazos corridos de fondo (CCyC art. 6: intimaciones, emplazamientos, mediación) que corren durante la feria, y algunos corridos procesales (por ejemplo, los 30 días de los edictos sucesorios) que podrían no correr. El tipo CORRIDOS es uno solo. ¿Hace falta distinguirlos? Propuesta: que corran siempre (vencimiento más temprano).

**Hitos afectados:** Todos los hitos CORRIDOS de las matrices civiles

### DYP D28 · Etapa común: rol en honorarios y costas

El pago de honorarios y la apelación de la regulación quedan como AMBAS, porque los paga quien fue condenado en costas. ¿Es correcto o la app debería decidir el rol según la sentencia?

**Hitos afectados:** DYP_510, DYP_515

### DYP D29 · Producto

Las dudas técnicas de producto del fuero civil (roles propios, rol representado, hitos prejudiciales, catálogos de regímenes y de juzgados, límite FIN_DEL_DIA y caminos que vuelven a un hito anterior) se registran en matriz_civil_sucesorio_pba.xlsx. ¿Alguna cambia la carga de esta matriz?

**Hitos afectados:** Todos

### DYP D30 · Reglas del motor

Las reglas del motor de plazos (D26 a D34: gracia, hora límite, notificación electrónica, meses y años, horas, anticipación) se responden una sola vez en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para el fuero civil? Las diferencias propias del civil (ferias en la caducidad, plazos corridos de fondo) tienen sus propias dudas.

**Hitos afectados:** Todos

## 5. Desalojo (`DES`)

Planilla: [`matriz_civil_desalojo_pba.xlsx`](matriz_civil_desalojo_pba.xlsx) · diagrama: [`diagrama_civil_desalojo_pba.md`](diagrama_civil_desalojo_pba.md). 13 dudas. Las dos últimas remiten al sucesorio (producto) y a daños y perjuicios (etapa común).

### DES D01 · Régimen de locaciones

La matriz cita los arts. 1198, 1199, 1221 y 1222 CCyC con el texto que surge de leyes-ar.com, que refleja el DNU 70/2023 (derogó la Ley 27.551). ¿Sigue vigente el DNU 70/2023 en materia de locaciones al 13/11/2026 y hay alguna norma posterior? ¿Los contratos firmados bajo la Ley 27.551 siguen regidos por ella (a verificar)?

**Hitos afectados:** DES_010, DES_020, DES_030

### DES D02 · Intimación del art. 1222

La intimación previa es obligatoria solo con destino habitacional y su plazo no puede ser menor a 10 días corridos desde la recepción. La matriz usa 10 días corridos. ¿Se usa también en los otros destinos por práctica? ¿Corren durante la feria judicial (son de fondo)?

**Hitos afectados:** DES_020

### DES D03 · Mediación optativa

En desalojo la mediación es optativa para el reclamante (art. 5 Ley 13.951) y dura hasta 30 días corridos (art. 12). La matriz no suma la reanudación de la prescripción porque el desalojo no se pierde por el paso del tiempo mientras la obligación de restituir sea exigible. ¿Es correcto?

**Hitos afectados:** DES_070, DES_074

### DES D04 · Desocupación inmediata

La entrega inmediata (art. 676 bis) y la desocupación inmediata (art. 676 ter) se piden después de trabada la litis y bajo caución real. La matriz las abre desde el traslado de la contestación y el juicio sigue en paralelo. ¿Se pueden pedir con la demanda? ¿Qué tipo de caución se acepta en la práctica?

**Hitos afectados:** DES_325, DES_360

### DES D05 · Plazo para desocupar

La sentencia fija el plazo para desocupar, no menor a 10 días (art. 1223 CCyC). La matriz usa 10 días corridos porque es una norma de fondo. ¿Los juzgados lo cuentan en días hábiles? ¿El CPCCBA tiene una norma propia?

**Hitos afectados:** DES_750

### DES D06 · Notificación en el inmueble

En el CPCCN el oficial notificador hace saber la demanda a sublocatarios y ocupantes (art. 684 CPCCN). No encontramos una norma igual en los arts. 676 a 678 bis CPCCBA. ¿Cómo se notifica a los ocupantes desconocidos en PBA y qué pasa si la sentencia no los alcanzó?

**Hitos afectados:** DES_330

### DES D07 · Lanzamiento

¿Qué norma del CPCCBA rige el mandamiento de lanzamiento (la matriz cita el art. 497, a verificar)? ¿Hace falta pedir en forma expresa el allanamiento y la fuerza pública? ¿Qué se hace con los muebles que quedan?

**Hitos afectados:** DES_760, DES_770, DES_780

### DES D08 · Ocupantes vulnerables

Antes de desalojar en una villa o asentamiento, el juez oficia al Ministerio de Infraestructura (art. 678 bis) y, si está registrado, no puede ordenarlo durante el plazo del art. 70 Ley 14.449. ¿Cuánto dura ese plazo? Con menores o personas con discapacidad fuera de ese supuesto, ¿qué intervención se exige (Ministerio Público, servicios sociales)?

**Hitos afectados:** DES_760, DES_765

### DES D09 · Intrusos y sede penal

Frente a un intruso, ¿se recomienda la denuncia por usurpación con pedido de restitución en sede penal (artículo del CPP PBA, a verificar), las acciones posesorias o directamente el desalojo? La matriz permite combinar denuncia y desalojo.

**Hitos afectados:** DES_050, DES_055

### DES D10 · Cobro de alquileres

El cobro de alquileres va en un juicio ejecutivo aparte (arts. 521 inc. 6 y 523 inc. 2 CPCCBA), que se cargaría como otro caso. ¿Conviene una matriz propia de ejecución de alquileres? ¿Se acumula el reclamo contra los fiadores?

**Hitos afectados:** DES_080

### DES D11 · Comodato y tenencia precaria

La restitución de la cosa dada en comodato tramita por sumario (art. 320 inc. 2 ll) y el desalojo alcanza al tenedor precario (art. 676). ¿Se usa siempre la vía del desalojo para el comodato de inmuebles?

**Hitos afectados:** DES_030, DES_300

### DES D12 · Producto

Las dudas técnicas de producto del fuero civil (roles propios, rol representado, hitos prejudiciales, catálogos de regímenes y de juzgados, límite FIN_DEL_DIA y caminos que vuelven a un hito anterior) se registran en matriz_civil_sucesorio_pba.xlsx. ¿Alguna cambia la carga de esta matriz?

**Hitos afectados:** Todos

### DES D13 · Etapa común

La etapa judicial común (demanda, prueba, sentencia, recursos, ejecución, acuerdo y caducidad) sale de civil/datos/comun.py. Sus dudas se responden una sola vez en matriz_civil_danos_y_perjuicios_pba.xlsx (temas que empiezan con 'Etapa común') y las reglas del motor (D26 a D34), en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para esta matriz?

**Hitos afectados:** Todos

## 6. Prescripción adquisitiva (`USU`)

Planilla: [`matriz_civil_prescripcion_adquisitiva_pba.xlsx`](matriz_civil_prescripcion_adquisitiva_pba.xlsx) · diagrama: [`diagrama_civil_prescripcion_adquisitiva_pba.md`](diagrama_civil_prescripcion_adquisitiva_pba.md). 15 dudas. Las dos últimas remiten al sucesorio (producto) y a daños y perjuicios (etapa común).

### USU D01 · Años máximos

La prescripción larga exige 20 años de posesión (art. 1899 CCyC) y la app admite hasta 10 años (ANIOS) o 120 meses. La matriz pide cargar como inicio la fecha en que se cumplen los primeros 10 años. ¿Se acepta ese recurso o hay que ampliar el máximo (ver la duda de producto en la matriz del sucesorio)?

**Hitos afectados:** USU_017

### USU D02 · Mediación

¿La demanda de usucapión exige mediación previa (Ley 13.951)? Si el titular es ignorado o el Fisco es parte, la mediación no parece posible (art. 4: causas en que el Estado es parte). La matriz no incluye hitos de mediación.

**Hitos afectados:** USU_300

### USU D03 · Plano y Geodesia

¿Qué organismo visa hoy el plano de mensura para usucapión (Dirección Provincial de Geodesia, a verificar), con qué antigüedad máxima y en qué plazo? ¿Hace falta un hito con plazo para la visación?

**Hitos afectados:** USU_030

### USU D04 · Edictos

Los edictos se publican por 10 días en el Boletín Judicial y en un diario de la zona (art. 681). ¿Qué plazo tienen los citados para comparecer después de la última publicación? La matriz usa 10 días hábiles (plazo de contestación del sumario).

**Hitos afectados:** USU_336, USU_338

### USU D05 · Defensor Oficial

¿En qué plazo contesta el Defensor Oficial de Ausentes y desde cuándo corre? ¿El rol DEMANDADA es correcto para él, aunque sea un funcionario?

**Hitos afectados:** USU_339

### USU D06 · Fisco de Estado

El Fisco de Estado y la Municipalidad son parte si hay intereses fiscales (art. 679 inc. 4). ¿El Fisco de Estado tiene un plazo especial para contestar (ley orgánica de Fiscalía de Estado, a verificar)? ¿Se los cita siempre o solo si el informe del art. 680 muestra intereses fiscales?

**Hitos afectados:** USU_342

### USU D07 · Anotación de litis

El art. 1905 CCyC obliga al juez a ordenar de oficio la anotación de litis al dar traslado. ¿Igual conviene pedirla en la demanda? ¿Quién diligencia el oficio?

**Hitos afectados:** USU_332

### USU D08 · Unión de posesiones

¿Cómo se acredita la unión de posesiones con la del antecesor (art. 1901 CCyC) y desde qué fecha se cuenta el plazo si hay cesiones de derechos posesorios?

**Hitos afectados:** USU_015

### USU D09 · Ley 24.374

¿Sigue vigente el régimen de regularización dominial de la Ley 24.374 en PBA al 13/11/2026, con qué plazo de ocupación exigido y qué organismo lo tramita? La matriz solo lo deja como alternativa.

**Hitos afectados:** USU_045

### USU D10 · Usucapión como defensa

Cuando el cliente es demandado por reivindicación o desalojo, la usucapión se opone como defensa (art. 1905 CCyC). La matriz la modela como un solo hito con el plazo de contestación y el juicio en contra sigue como otro caso. ¿Conviene reconvenir siempre?

**Hitos afectados:** USU_060

### USU D11 · Herederos del titular

Si el titular murió, ¿se demanda a los herederos declarados, a la sucesión, o se cita por edictos? ¿Hace falta abrir el sucesorio del titular?

**Hitos afectados:** USU_020, USU_330

### USU D12 · Tasa de justicia

¿La tasa de justicia de la usucapión se calcula sobre la valuación fiscal del inmueble y cuándo se paga (al iniciar o antes de inscribir, a verificar)?

**Hitos afectados:** USU_300, USU_750

### USU D13 · Inscripción

Si el Registro observa el testimonio, ¿qué plazo hay para subsanar antes de que caduque la inscripción provisional (Ley 17.801, a verificar)? ¿Hace falta un hito con plazo?

**Hitos afectados:** USU_760

### USU D14 · Producto

Las dudas técnicas de producto del fuero civil (roles propios, rol representado, hitos prejudiciales, catálogos de regímenes y de juzgados, límite FIN_DEL_DIA y caminos que vuelven a un hito anterior) se registran en matriz_civil_sucesorio_pba.xlsx. ¿Alguna cambia la carga de esta matriz?

**Hitos afectados:** Todos

### USU D15 · Etapa común

La etapa judicial común (demanda, prueba, sentencia, recursos, ejecución, acuerdo y caducidad) sale de civil/datos/comun.py. Sus dudas se responden una sola vez en matriz_civil_danos_y_perjuicios_pba.xlsx (temas que empiezan con 'Etapa común') y las reglas del motor (D26 a D34), en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para esta matriz?

**Hitos afectados:** Todos

## 7. Incumplimiento contractual (`CTR`)

Planilla: [`matriz_civil_contratos_pba.xlsx`](matriz_civil_contratos_pba.xlsx) · diagrama: [`diagrama_civil_contratos_pba.md`](diagrama_civil_contratos_pba.md). 14 dudas. Las dos últimas remiten al sucesorio (producto) y a daños y perjuicios (etapa común).

### CTR D01 · Tipo de proceso

La matriz usa el juicio ordinario, que corresponde a los contratos de más de 4.500 Jus (arts. 319 y 320 inc. 1 CPCCBA). La escrituración, la resolución de compraventa de inmuebles y la consignación son sumario (art. 320 inc. 2 a y f) y los reclamos de consumo van por el proceso más abreviado (art. 53 Ley 24.240). En esos casos el abogado edita los plazos. ¿Conviene publicar una versión sumaria de esta matriz?

**Hitos afectados:** CTR_300, CTR_340, CTR_350, CTR_410

### CTR D02 · Prescripción

La matriz usa 5 años (art. 2560 CCyC). ¿Los daños por incumplimiento contractual prescriben a los 3 años (art. 2561) o a los 5? ¿Desde cuándo corre la acción de escrituración del boleto?

**Hitos afectados:** CTR_015

### CTR D03 · Emplazamiento del art. 1088

El emplazamiento a cumplir tiene un plazo no menor a 15 días, salvo usos o índole de la prestación. La matriz usa 15 días corridos (norma de fondo). ¿Es correcto? ¿Corre durante la feria judicial?

**Hitos afectados:** CTR_025

### CTR D04 · Cláusula resolutoria expresa

Con cláusula resolutoria expresa la resolución opera desde la comunicación fehaciente (art. 1086). La matriz no abre un hito propio: va directo a la mediación. ¿Falta algún plazo (por ejemplo, para restituir)?

**Hitos afectados:** CTR_020

### CTR D05 · Mediación

La mediación es obligatoria en los reclamos contractuales (Ley 13.951), salvo exclusiones del art. 4. ¿Es obligatoria también para la consignación judicial y la escrituración?

**Hitos afectados:** CTR_080, CTR_300

### CTR D06 · Citación a escriturar

La matriz modela la citación a escriturar como una fecha fijada en la intimación (arts. 1018 y 1137 CCyC). ¿Qué anticipación mínima se suele dar, y la incomparecencia se documenta siempre con acta notarial?

**Hitos afectados:** CTR_032

### CTR D07 · Vicios ocultos

La denuncia del defecto va dentro de los 60 días de manifestado (art. 1054) y el reclamo prescribe al año (art. 2564 inc. a). ¿Desde cuándo corre el año: desde la manifestación, la denuncia o la recepción de la cosa?

**Hitos afectados:** CTR_050, CTR_052

### CTR D08 · Locación

Los arts. 1201, 1220 y 1221 CCyC se citan con el texto de leyes-ar.com; el del art. 1221 refleja el DNU 70/2023 y el del art. 1201 parece el de la Ley 27.551. ¿Qué texto rige al 13/11/2026?

**Hitos afectados:** CTR_060, CTR_062

### CTR D09 · Fideicomiso

El fiduciario debe rendir cuentas (art. 1676) pero el plazo depende del contrato. ¿Se usa el proceso de rendición de cuentas del CPCCBA (artículos, a verificar)? ¿La remoción del fiduciario (art. 1678) es ordinario o sumario?

**Hitos afectados:** CTR_070

### CTR D10 · Consignación extrajudicial

El acreedor tiene 5 días hábiles para responder a la consignación extrajudicial (art. 911 CCyC). La matriz los cuenta como días hábiles administrativos. ¿Es el criterio correcto?

**Hitos afectados:** CTR_090

### CTR D11 · Escrituración por el juez

La condena a escriturar se cumple en el plazo de la sentencia o la firma el juez (art. 510). La matriz agrega salidas propias desde la apelación, la Cámara, la queja y la SCBA. ¿Hay pasos que falten (certificados, tributos, inscripción)?

**Hitos afectados:** CTR_600, CTR_735, CTR_740

### CTR D12 · Consumo

En los contratos de consumo, ¿se aplica el beneficio de gratuidad (art. 53 Ley 24.240) a la tasa de justicia en PBA, y por qué proceso tramita (sumario o sumarísimo)?

**Hitos afectados:** CTR_010, CTR_300

### CTR D13 · Producto

Las dudas técnicas de producto del fuero civil (roles propios, rol representado, hitos prejudiciales, catálogos de regímenes y de juzgados, límite FIN_DEL_DIA y caminos que vuelven a un hito anterior) se registran en matriz_civil_sucesorio_pba.xlsx. ¿Alguna cambia la carga de esta matriz?

**Hitos afectados:** Todos

### CTR D14 · Etapa común

La etapa judicial común (demanda, prueba, sentencia, recursos, ejecución, acuerdo y caducidad) sale de civil/datos/comun.py. Sus dudas se responden una sola vez en matriz_civil_danos_y_perjuicios_pba.xlsx (temas que empiezan con 'Etapa común') y las reglas del motor (D26 a D34), en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para esta matriz?

**Hitos afectados:** Todos

## 8. Citas y datos marcados "(a verificar)"

Son las citas de `Base_Normativa`, los eventos de inicio y los ítems del checklist que no se pudieron confirmar en normas.gba.gob.ar ni en leyes-ar.com al 13/11/2026. El abogado confirma o corrige la cita y, si corresponde, el plazo del hito.

### En la etapa común (aparecen en más de una matriz)

- **Requerimiento de mediación prejudicial obligatoria** (checklist): Presentar el formulario de requerimiento y pagar lo que corresponda al inicio (reglamentación, a verificar). Hitos: `DYP_080`, `DES_070`, `CTR_080`.
- **Presentación de la demanda** (checklist): Pagar la tasa de justicia y la contribución del 5 % sobre la tasa (sobretasa, art. 12 inc. g Ley 6716) al iniciar, sobre el monto reclamado (alícuota de la Ley Impositiva vigente, a verificar). Hitos: `DYP_300`, `DES_300`, `USU_300`, `CTR_300`.
- **Presentación de la demanda** (checklist): Pagar el bono de derecho fijo de la Ley 8480 y el anticipo previsional de la Ley 6716 (monto, a verificar). Hitos: `DYP_300`, `DES_300`, `USU_300`, `CTR_300`.
- **Beneficio de litigar sin gastos** (checklist): Notificar a la contraria y al organismo fiscal según lo que ordene el juzgado (a verificar). Hitos: `DYP_310`, `DES_310`, `USU_310`, `CTR_310`.
- **Radicación, control de admisibilidad y traslado de la demanda** (checklist): Domicilio fuera del asiento del juzgado: el plazo se amplía 1 día cada 200 km (art. 158); fuera de la provincia, cédula por la Ley 22.172 (a verificar). Hitos: `DYP_330`, `DES_330`, `USU_330`, `CTR_330`.
- **Reposición u oposición contra la providencia de prueba** (checklist): Las resoluciones sobre prueba no son apelables salvo las excepciones del código (art. 377, a verificar). Hitos: `DYP_405`, `DES_405`, `USU_405`, `CTR_405`.
- **Audiencia preliminar** (base normativa): Res. SCBA 2761/16 (programa de oralidad civil); art. 36 CPCCBA (a verificar). Hitos: `DYP_415`, `DES_415`, `USU_415`, `CTR_415`.
- **Alegatos** (base normativa): Art. 480 CPCCBA; en el sumario, a verificar (art. 495). Hitos: `DYP_450`, `DES_450`, `USU_450`.
- **Recursos extraordinarios ante la SCBA** (checklist): Inaplicabilidad: valor mínimo del agravio (art. 278, a verificar el monto en Jus). Hitos: `DYP_630`, `DES_630`, `USU_630`, `CTR_630`.

### Sucesorio

- **`SUC_010` Consulta inicial por el fallecimiento del causante** (checklist): Detectar si el causante era extranjero, vivía en el exterior o tenía bienes fuera de PBA o del país (arts. 2643 y 2644 CCyC, a verificar).
- **`SUC_016` Vencimiento máximo del ITGB: 24 meses desde el fallecimiento** (base normativa): Código Fiscal PBA (Ley 10.397), art. 322 inc. b (a verificar el t.o. vigente); Ley 14.044.
- **`SUC_016` Vencimiento máximo del ITGB: 24 meses desde el fallecimiento** (checklist): Controlar los mínimos no imponibles de la Ley Impositiva del año (a verificar).
- **`SUC_100` Promoción del sucesorio** (checklist): Pedir la inscripción en el Registro de Juicios Universales (a verificar la acordada de la SCBA).
- **`SUC_100` Promoción del sucesorio** (checklist): Pagar bono de la Ley 8480 y anticipo de la Ley 6716 al iniciar (a verificar); la tasa de justicia se paga al pedir la inscripción.
- **`SUC_120` Informe del Registro de Testamentos** (checklist): Si el causante vivió en otra provincia, pedir también el informe de ese registro (a verificar).
- **`SUC_125` Inscripción en el Registro de Juicios Universales** (base normativa): Registro de Juicios Universales de la SCBA (a verificar la acordada vigente).
- **`SUC_210` Notificación a los herederos denunciados** (checklist): Domicilio fuera de la provincia: Ley 22.172 (a verificar).
- **`SUC_450` Herencia vacante** (base normativa): Arts. 768 a 771 CPCCBA; arts. 2441 a 2443 CCyC (a verificar).
- **`SUC_810` Declaración jurada y pago del ITGB** (base normativa): Código Fiscal PBA (Ley 10.397), art. 322 inc. b (a verificar); Ley 14.044.
- **`SUC_810` Declaración jurada y pago del ITGB** (checklist): Si son días hábiles administrativos (a verificar), editar el tipo de plazo.
- **`SUC_820` Tasa de justicia y contribución al pedir la inscripción** (base normativa): Código Fiscal PBA y Ley Impositiva vigente (a verificar); art. 12 inc. g Ley 6716.
- **`SUC_820` Tasa de justicia y contribución al pedir la inscripción** (checklist): En los sucesorios, la tasa se paga al pedir la inscripción, sobre el valor de los bienes (a verificar la base y la alícuota).
- **`SUC_820` Tasa de justicia y contribución al pedir la inscripción** (checklist): Revisar exenciones (a verificar).
- **`SUC_850` Pedido de inscripción y libramiento de testimonios y oficios** (checklist): Bienes en otra provincia: oficio por la Ley 22.172 (a verificar).
- **`SUC_850` Pedido de inscripción y libramiento de testimonios y oficios** (checklist): Si los herederos venden sin inscribir, se puede usar el tracto abreviado ante escribano (art. 16 Ley 17.801, a verificar).
- **`SUC_850` Pedido de inscripción y libramiento de testimonios y oficios** (checklist): Controlar si el registro exige libre deuda de ARBA o municipal (a verificar).
- **`SUC_860` Transferencia de automotores** (base normativa): Normas técnico-registrales del DNRPA (a verificar).
- **`SUC_860` Transferencia de automotores** (checklist): Usar el formulario que pida el registro seccional (a verificar).
- **`SUC_915` Apelación de la regulación de honorarios** (checklist): Controlar la base regulatoria (valor del haber) y las etapas cumplidas (a verificar).
- **`SUC_925` Control de la caducidad de instancia** (base normativa): Arts. 310 a 316 CPCCBA (a verificar si aplica al sucesorio o solo a sus incidentes).
- **`SUC_980` Conclusión del trámite judicial o continuación extrajudicial** (checklist): Si todos los herederos son capaces y están de acuerdo, el trámite puede seguir fuera del juzgado (art. 733, a verificar el alcance).

### Daños y perjuicios

- **`DYP_024` Respuesta de la aseguradora del responsable al reclamo** (base normativa): Art. 56 Ley 17.418 (plazo previsto para el asegurado; para el tercero damnificado, a verificar).
- **`DYP_024` Respuesta de la aseguradora del responsable al reclamo** (checklist): Si hay menores o personas con capacidad restringida, el acuerdo necesita aprobación judicial (a verificar).
- **`DYP_030` Seguimiento de la causa penal** (checklist): Evaluar presentarse como particular damnificado en la causa penal (a verificar en el CPP PBA).
- **`DYP_090` Convenio extrajudicial y cobro** (checklist): Si el damnificado es menor o tiene capacidad restringida, pedir la aprobación judicial (a verificar).
- **`DYP_345` Contestación de la citación en garantía por la aseguradora** (base normativa): Art. 118 Ley 17.418; arts. 94 y 484 CPCCBA (plazo igual al de la contestación, a verificar).
- **`DYP_725` Pago de la aseguradora citada: límite de cobertura y franquicia** (checklist): Si la aseguradora está en liquidación, verificar el crédito ante el liquidador (a verificar).
- **`DYP_800` Acuerdo, transacción o conciliación y homologación** (checklist): Si el damnificado es menor o tiene capacidad restringida, interviene el Ministerio Público y el acuerdo necesita aprobación judicial (a verificar).

### Desalojo

- **`DES_050` Constatación de la ocupación del inmueble** (checklist): Evaluar la denuncia penal por usurpación (art. 181 CP) y el pedido de restitución en sede penal (a verificar en el CPP PBA).
- **`DES_050` Constatación de la ocupación del inmueble** (checklist): Si la ocupación es reciente, evaluar las acciones posesorias o el interdicto (a verificar).
- **`DES_055` Denuncia penal por usurpación y restitución en sede penal** (base normativa): Art. 181 Código Penal; CPP PBA (restitución provisoria, a verificar).
- **`DES_330` Radicación, control de admisibilidad y traslado de la demanda** (checklist): Pedir que la cédula se diligencie en el inmueble y que se haga saber la demanda a todos los ocupantes (práctica y artículo aplicable, a verificar: ver duda D06).
- **`DES_760` Pedido y libramiento del mandamiento de lanzamiento** (checklist): Si hay menores o personas vulnerables, prever la intervención del Ministerio Público y de los servicios sociales (a verificar).
- **`DES_765` Consulta al Registro de Villas y Asentamientos y audiencia de relocalización** (checklist): Si el asentamiento está registrado, no se ordena el desalojo durante el plazo del art. 70 Ley 14.449 (duración, a verificar): cargarlo como plazo suelto.
- **`DES_770` Diligencia de lanzamiento** (base normativa): Art. 497 CPCCBA (a verificar).

### Prescripción adquisitiva

- **`USU_030` Plano de mensura para usucapión y visado de Geodesia** (checklist): Presentarlo para el visado de la Dirección Provincial de Geodesia (organismo y trámite, a verificar).
- **`USU_030` Plano de mensura para usucapión y visado de Geodesia** (checklist): Pedir la valuación fiscal y la partida inmobiliaria en ARBA (base de la tasa de justicia, a verificar).
- **`USU_045` Evaluación de la regularización dominial de la Ley 24.374** (base normativa): Ley 24.374 (requisitos y vigencia, a verificar).
- **`USU_045` Evaluación de la regularización dominial de la Ley 24.374** (checklist): Controlar los requisitos: vivienda única y permanente, ocupación pacífica, pública y continua con causa lícita durante el plazo legal (a verificar).
- **`USU_045` Evaluación de la regularización dominial de la Ley 24.374** (checklist): El trámite es administrativo, ante el organismo provincial y un escribano de registro (a verificar).
- **`USU_045` Evaluación de la regularización dominial de la Ley 24.374** (checklist): La inscripción se consolida como dominio después de 10 años (a verificar).
- **`USU_338` Plazo para comparecer de los citados por edictos** (base normativa): Arts. 147, 484 y 681 CPCCBA (plazo, a verificar).
- **`USU_339` Contestación del Defensor Oficial de Ausentes** (base normativa): Arts. 341 y 681 CPCCBA (plazo, a verificar).
- **`USU_342` Contestación del Fisco de Estado y de la Municipalidad** (base normativa): Arts. 679 inc. 4 y 681 CPCCBA (plazo especial del Fisco de Estado, a verificar).
- **`USU_750` Pedido de inscripción de la sentencia** (checklist): Pagar la tasa de justicia y los aportes pendientes antes de inscribir (a verificar).
- **`USU_760` Inscripción en el Registro de la Propiedad** (checklist): Si el Registro observa el documento, subsanar en el plazo de la inscripción provisional (a verificar).
- **`USU_770` Alta catastral y tributaria a nombre del cliente** (base normativa): Código Fiscal PBA (a verificar).

### Incumplimiento contractual

- **`CTR_052` Prescripción del reclamo por vicios redhibitorios** (evento de inicio): Denuncia del defecto oculto (inicio del cómputo, a verificar).
- **`CTR_060` Análisis del incumplimiento en la locación** (base normativa): Arts. 1201, 1220 y 1221 CCyC (texto según DNU 70/2023, a verificar).
