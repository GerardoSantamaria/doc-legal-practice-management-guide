# Dudas y puntos a validar · Fuero Penal PBA

**Estado:** borrador para validar · **Fecha:** 13/11/2026 · **Versión de las matrices:** 1 (borrador)

Este documento reúne lo que el abogado tiene que validar en las cuatro matrices de esta carpeta: las 80 dudas de las hojas `Dudas_a_validar`, por flujo, y las citas y datos que quedaron marcados "(a verificar)" en los hitos. El texto de cada duda es el mismo que el de la planilla. Se genera desde `datos/`; si cambia una duda en la planilla, la planilla manda.

---

## 1. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal` de la hoja `Dudas_a_validar`, con la norma, el fallo o la acordada que la sostiene, y `Estado` pasa de `PENDIENTE` a `VALIDADO` o `CORREGIR`. Si la respuesta cambia un hito o un camino, se corrige también la fila en `Nodos` o en `Transiciones`.
- **Además de las dudas, cada fila se valida** con `Estado_Validacion` (hoy todas en `PENDIENTE`): investigación 53 hitos y 139 transiciones, juicio oral y público 43 hitos y 82 transiciones, juicio abreviado 23 hitos y 41 transiciones, hábeas corpus 20 hitos y 50 transiciones. El control "filas pendientes" de la hoja `Flujo` las cuenta.
- **Cada duda se responde una sola vez:**
  - las **transversales** del fuero (gracia, plazos con detenido, horas, días corridos, duración de la IPP, plazo máximo con detenido, víctima, prescripción, honorarios y alcance de la V1), en investigación;
  - las de **producto** (roles, rol representado, fase previa, motor, vinculación de expedientes, datos sensibles, matrices federales, catálogo de régimen, finales desde caminos paralelos e hitos que se reabren), también en investigación;
  - las **reglas del motor** (D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx`) no se repiten: la última duda de cada matriz pregunta si algo se aparta de esas respuestas.
- **Ante la duda, el vencimiento más temprano.** Todos los hitos tienen `Aplica_Gracia = NO`. Hasta que el abogado confirme una cita "(a verificar)", la app no la usa para calcular.
- **Sin datos de causas reales.** Al responder, citar normas y fallos; no escribir nombres, DNI, domicilios, números de causa o IPP ni relatos de hechos.
- **No correr `generar.py` sobre una planilla que el abogado ya empezó a completar:** la pisa con lo que hay en `datos/` (ver [`README.md`](README.md)).

## 2. Por dónde empezar

Las que atraviesan todos los flujos (todas en investigación):

| Duda | Tema | Por qué primero |
| :--- | :--- | :--- |
| IPP D15, D18 y D28 | Gracia, días corridos y feria selectiva del art. 139 | Definen el cálculo de casi todos los vencimientos; el motor hoy no distingue la feria penal. |
| IPP D16, D17 y D20 | Plazos con detenido, horas y plazo máximo de 2 años (art. 141) | Son los vencimientos más urgentes y los que corren en días inhábiles. |
| IPP D33 y D34 | Hito final desde un camino paralelo e hito que se reabre a sí mismo | Si el importador o el motor no los aceptan, hay que cambiar la forma de las matrices antes de importarlas. |
| IPP D30 | Causa reservada y datos de víctimas y detenidos | Condiciona qué se puede mostrar en avisos y quién ve cada expediente (relacionada con el modelado de amenazas y la política de privacidad). |
| IPP D31, D14, JOR D18, JAB D11 y HCO D14 | Fuero federal | Define si la app tiene que avisar cuando el expediente es federal y no aplicar estas matrices. |

Las tres de mayor impacto de cada flujo:

| Flujo | Dudas |
| :--- | :--- |
| Investigación | D01 (plazos de flagrancia y revisión de la defensa), D05 (sobreseimiento con particular damnificado, art. 334 bis), D08 (desde cuándo corren los 4 meses del art. 282) |
| Juicio oral | D02 (debate dentro de 6 meses, art. 339), D09 (casación o apelación, 20 días), D10 (manifestación de recurrir en 7 días, art. 451) |
| Juicio abreviado | D01 (límite de 30 días antes del debate), D02 (órgano competente según la etapa), D05 (casación o apelación, art. 401) |
| Hábeas corpus | D01 (plazo de impugnación del art. 417), D02 (audiencia obligatoria o discrecional), D08 (desde cuándo corren las 24 y 48 horas del art. 415) |

## 3. Investigación Penal Preparatoria (`IPP`)

Planilla: [`matriz_penal_investigacion_pba.xlsx`](matriz_penal_investigacion_pba.xlsx) · diagrama: [`diagrama_penal_investigacion_pba.md`](diagrama_penal_investigacion_pba.md). 34 dudas. Incluye las dudas transversales del fuero (D15 a D24) y las de producto (D25 a D34), que se responden solo acá.

### IPP D01 · Flagrancia: plazos y revisión de la defensa

Arts. 284 bis a 284 sexies: el fiscal declara el caso en 48 horas desde que conoce la aprehensión; la defensa puede discrepar y el Juez de Garantías revisa dentro de las 48 horas de la notificación; investigación en 20 + 20 días desde la aprehensión; requisitoria en 5 días. ¿Hace falta un hito propio para la revisión de la defensa (48 HORAS) o alcanza con el checklist? ¿La Ley 13.811 (audiencias orales) cambia estos plazos en algún departamento judicial? Propuesta: checklist en IPP_700. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_700, IPP_710, IPP_720, IPP_730

### IPP D02 · Mediación penal Ley 13.433

¿En qué delitos de competencia provincial procede la mediación penal en PBA y qué control judicial exige? ¿Está vedada en violencia de género y delitos contra la integridad sexual? Propuesta: hito sin plazo y checklist de exclusiones hasta validar. Norma a verificar.

**Hitos afectados:** IPP_520

### IPP D03 · Ley del Ministerio Público (14.442)

El borrador anterior citaba la Ley 12.061. El CPP cita la Ley 14.442 (por ejemplo, en el art. 92). ¿La Ley 14.442 es hoy la Ley Orgánica del Ministerio Público de PBA y fija plazos de revisión del archivo, la desestimación o los criterios de oportunidad? Propuesta: citar la 14.442 con '(a verificar)'.

**Hitos afectados:** IPP_100, IPP_500, IPP_510

### IPP D04 · Órgano que revisa el archivo

El art. 56 bis dice que la revisión del archivo es ante el Fiscal General; el art. 83 inc. 8 dice 'Fiscal de Cámara Departamental'. ¿Son hoy el mismo órgano? ¿Hay plazo para pedir la revisión? Propuesta: hito sin plazo; el abogado carga el plazo si lo hay. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_500, IPP_510

### IPP D05 · Sobreseimiento con particular damnificado (art. 334 bis)

Circuito verificado: vista al Fiscal de Cámara; si no sostiene el sobreseimiento, otro fiscal requiere la elevación; si lo mantiene, vista de 15 días al particular damnificado para requerir la elevación a su costa. ¿Hay plazo para que se expida el Fiscal de Cámara? ¿La feria suspende los 15 días (el art. 139 no los menciona)? Propuesta: Fiscal de Cámara sin plazo; 15 CORRIDOS sin suspensión por feria. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_610, IPP_612, IPP_614

### IPP D06 · Oposición del art. 336 y feria

Art. 139: la feria suspende el plazo de oposición del art. 336, salvo flagrancia. ¿El motor puede marcar ese hito como 'suspende en feria'? Propuesta: sí; registrar el requerimiento al motor. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_630

### IPP D07 · Revisión de diligencias denegadas (art. 334)

Verificado: si el fiscal denegó diligencias, notifica el cierre; las partes tienen 5 días para pedir al Fiscal General la revisión y este resuelve en 48 horas. ¿Qué pasa si no resuelve en 48 horas? ¿Hace falta un hito de 48 HORAS para el Fiscal General? Propuesta: checklist en IPP_605. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_605

### IPP D08 · Disparo del plazo de 4 meses (art. 282)

Si no hay detención ni declaración del art. 308 (imputado no individualizado), el plazo no corre. La matriz abre IPP_400 recién con la detención o la declaración. ¿Es correcto? Si el imputado declara y después es detenido, ¿el plazo sigue desde la declaración? Propuesta: sí; la salida de IPP_300 distingue los dos casos. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_120, IPP_300, IPP_400

### IPP D09 · Renuncia al jurado y opción de tribunal

Verificado: la renuncia al jurado y la opción por tribunal colegiado se ejercen en el plazo del art. 336; la renuncia exige ratificación personal ante el juez y no procede firme la elevación (art. 22 bis). ¿Hace falta un hito para la audiencia de ratificación? Propuesta: checklist en IPP_630. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_630

### IPP D10 · Apelación y casación en la etapa intermedia

Contra lo que resuelve la Cámara sobre el sobreseimiento puede proceder casación (art. 450, segundo párrafo). La matriz no la modela como hito: queda como plazo suelto. Si la Cámara revoca el sobreseimiento, ¿la causa vuelve al fiscal para un nuevo requerimiento o se eleva directamente? Propuesta: volver a IPP_600 hasta confirmar. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_650, IPP_655

### IPP D11 · Abreviado durante la IPP

¿El acuerdo de abreviado puede presentarse antes del auto de elevación (además del art. 284 quinquies en flagrancia) y cuándo deriva a la matriz JAB? Propuesta: salida desde IPP_620 e IPP_630. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_620, IPP_630, IPP_955

### IPP D12 · Intervención de comunicaciones

El art. 229 autoriza la intervención por orden judicial. ¿Qué plazo máximo y qué prórrogas rigen al 13/11/2026 (por ley especial o acordada)? Propuesta: hito sin plazo hasta confirmar. Norma a verificar.

**Hitos afectados:** IPP_340

### IPP D13 · Suspensión del juicio a prueba: duración y revocación

El plazo de suspensión lo fija el tribunal entre 1 y 3 años (art. 76 ter CP) y el Juez de Ejecución controla las reglas (art. 404). Si se revoca, el proceso continúa. ¿La app debe pedir el valor al abogado al conceder la suspensión? ¿El control queda en esta matriz o en ejecución penal? Propuesta: IPP_535 en ANIOS, editable; sin derivación a ejecución.

**Hitos afectados:** IPP_530, IPP_535

### IPP D14 · Equivalencia en el fuero federal

En los distritos federales con asiento en PBA rige el CPPF (Mar del Plata, Bahía Blanca, Rosario/San Nicolás y La Plata) o todavía el CPPN (San Martín). En el CPPF la investigación la dirige el fiscal con control del juez de garantías y hay formalización; en el CPPN hay juez de instrucción, indagatoria y procesamiento. Esta matriz modela solo la IPP del CPP PBA. ¿Alcanza con el cuadro de equivalencias del README, o hay que avisar en la app cuando el expediente es federal? Propuesta: avisar y no aplicar esta matriz. Ver la duda de producto 'Matrices federales aparte' en la matriz de investigación.

**Hitos afectados:** IPP_010, IPP_100

### IPP D15 · [TRANSVERSAL] Plazo de gracia en el proceso penal

El art. 124 CPCCBA (día de gracia) no rige en el proceso penal. ¿El CPP PBA tiene un plazo de gracia propio? ¿A qué escritos se aplica? Propuesta de la app: sin gracia en todos los hitos (vencimiento más temprano). Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026). Art. 139: plazos continuos.

**Hitos afectados:** Todos

### IPP D16 · [TRANSVERSAL] Plazos con persona detenida

¿Los plazos con persona detenida (declaración del art. 308, coerción, hábeas corpus, flagrancia) corren en días y horas inhábiles y no se suspenden en la feria? ¿Cómo debe tratarlos el motor (hoy asume día cero hábil siguiente salvo HORAS)? Propuesta: en HORAS desde la fecha/hora exacta; en CORRIDOS sin suspender por feria cuando hay detenido. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** Todos los hitos con checklist 'Con detenido'

### IPP D17 · [TRANSVERSAL] Cómputo de plazos en horas

Regla R8 del motor: horas corridas desde el disparador. ¿En penal se interrumpen de noche o en días inhábiles? Propuesta: no se interrumpen (vencimiento más temprano), salvo que el equipo legal indique lo contrario. Fuente: logica_matematica_calculadora_de_dias_habiles_judiciales.md y art. 308/409/415 CPP PBA.

**Hitos afectados:** Hitos en HORAS

### IPP D18 · [TRANSVERSAL] Plazos corridos vs hábiles judiciales

Art. 139 CPP PBA: los plazos son continuos y computan feriados; si vencen en inhábil, se prorrogan al hábil siguiente; la feria suspende solo oposición (336), impugnación del auto de elevación y de la sentencia definitiva, salvo flagrancia. ¿Confirmamos CORRIDOS como tipo por defecto y no HABILES_JUDICIALES? Propuesta: sí. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** Todos

### IPP D19 · [TRANSVERSAL] Duración de la IPP y prórrogas

Art. 282: 4 meses desde la detención o la declaración del art. 308; prórroga fiscal hasta 2 meses; en casos excepcionales hasta 6 meses. Art. 283: vencido el plazo, el juez requiere al Fiscal General la sustitución y el nuevo fiscal tiene 2 meses. ¿El cómputo es de meses corridos (regla R7)? ¿Qué puede hacer la defensa al vencer? Propuesta: 4 MESES desde el disparador; alertar al vencer. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_400, IPP_410, IPP_420

### IPP D20 · [TRANSVERSAL] Plazo máximo con detenido (art. 141)

Art. 141: si el imputado está privado de libertad, los términos de la IPP y de duración total del proceso son fatales y el proceso no puede durar más de 2 años; en casos de suma complejidad rige el plazo razonable del art. 2. ¿Desde qué acto se cuentan los 2 años (aprehensión, detención o prisión preventiva)? ¿Se aplica además la Ley 24.390 y sus cómputos? ¿Qué pide la defensa al vencer (libertad, cese, morigeración)? Propuesta: 2 ANIOS desde el inicio de la privación de libertad. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** IPP_290, JOR_290

### IPP D21 · [TRANSVERSAL] Derechos de la víctima y Ley 27.372

En PBA los derechos de la víctima están en los arts. 83 a 88 CPP PBA (texto Ley 15.232): información, revisión del archivo y de la desestimación (art. 83 incs. 8 y 15), opinión en el abreviado (art. 396) y en la suspensión del juicio a prueba (art. 404), notificación del pedido de sobreseimiento si lo pidió (art. 325). ¿La Ley 27.372 se aplica además como norma de fondo en PBA? ¿La app debe alertar esas notificaciones aunque el abogado solo represente a la defensa? Propuesta: hitos de ACTORA para el particular damnificado y checklist de derechos de la víctima. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** Todos

### IPP D22 · [TRANSVERSAL] Prescripción de la acción penal

Código Penal arts. 62 y siguientes: ¿cómo se computa en la app (ANIOS desde el hecho o desde la última actuación que interrumpe, art. 67 CP: primer llamado a declarar, requerimiento de elevación, citación a juicio, sentencia condenatoria aunque no esté firme)? ¿Quién carga las interrupciones? Propuesta: hito de control con ANIOS según el máximo de la escala; el abogado edita las interrupciones como plazos sueltos.

**Hitos afectados:** IPP_050, JOR_010, JAB_010

### IPP D23 · [TRANSVERSAL] Honorarios Ley 14.967

¿En qué momento se regulan los honorarios en materia penal y cuál es el plazo de impugnación (art. 57 Ley 14.967: 5 días)? ¿Son días corridos del CPP o hábiles del CPCCBA? Propuesta: 5 CORRIDOS sin gracia.

**Hitos afectados:** Hitos de honorarios

### IPP D24 · [TRANSVERSAL] Fuero penal juvenil, acción privada y ejecución

Fuera de la V1: fuero penal juvenil (Ley 13.634), delitos de acción privada (querella) y ejecución de la pena (Ley 12.256). ¿Se confirman fuera de estas matrices, con la ejecución solo como hito final 'Sigue en ejecución penal'? Propuesta: sí.

**Hitos afectados:** Hitos finales de ejecución

### IPP D25 · [PRODUCTO] Roles propios del fuero penal

El enum de la app es ACTORA/DEMANDADA/TRIBUNAL/AMBAS. ¿Hacen falta roles propios (FISCAL, DEFENSA, PARTICULAR_DAMNIFICADO, AUTORIDAD_REQUERIDA)? Propuesta V1: mantener el enum y documentar el mapeo en Valores; no cambiar el contrato de API.

**Hitos afectados:** Todos

### IPP D26 · [PRODUCTO] represented_role del abogado

Cuando el abogado representa a la defensa, ¿represented_role = DEMANDADA? ¿Y cuando representa al particular damnificado, ACTORA? El fiscal nunca es cliente. Propuesta: sí.

**Hitos afectados:** Todos

### IPP D27 · [PRODUCTO] Flujo prejudicial vs judicial en penal

La app separa la fase Previa en flujo PREJUDICIAL. En penal, ¿tiene sentido desde la denuncia/consulta, o todo es judicial desde la denuncia en comisaría/fiscalía? Propuesta: Previa = consulta, denuncia y designación de defensor; desde la IPP formal, judicial.

**Hitos afectados:** Hitos de fase Previa

### IPP D28 · [PRODUCTO] Plazos con detenido y gracia en el motor

Hoy el motor (D26–D34 de la matriz laboral) no distingue 'con detenido' ni gracia penal. ¿Qué hay que cambiar para soportar CORRIDOS sin gracia, HORAS en inhábiles y feria selectiva del art. 139? Registrar; no modificar el motor en este repo.

**Hitos afectados:** Todos

### IPP D29 · [PRODUCTO] Vinculación de expedientes entre matrices

¿Cómo se vinculan investigación↔juicio oral, investigación↔abreviado, causa principal↔hábeas corpus y condena↔ejecución? Propuesta: hito final de derivación + expediente vinculado con el mismo número de causa interno, sin copiar datos sensibles.

**Hitos afectados:** Hitos 'Sigue en la matriz...'

### IPP D30 · [PRODUCTO] Causa reservada y datos de víctimas/detenidos

¿Cómo se marca una causa reservada? ¿Quién ve en el estudio los datos de una víctima o de un detenido? ¿Los avisos pueden revelar datos de la causa en el dispositivo? Relacionar con modelado_de_amenazas_v1.md y legal/politica_de_privacidad.md. No modificar esos documentos; solo registrar la duda.

**Hitos afectados:** Todos

### IPP D31 · [PRODUCTO] Matrices federales aparte

Al 13/11/2026 el CPPF (Ley 27.063 T.O. 2019) rige en distritos federales con asiento en PBA: Mar del Plata, Bahía Blanca, Rosario/San Nicolás y La Plata (desde 21/09/2026, Res. MJ 275/2026). San Martín aún sin fecha; CABA/Penal Económico previstos para 15/02/2027. Donde no rige el CPPF sigue el CPPN (Ley 23.984). ¿Hacen falta matrices federales aparte? Propuesta: sí, en una carpeta federal/ futura; estas matrices son solo provinciales. Fuente: argentina.gob.ar (cronograma) y Boletín Oficial.

**Hitos afectados:** Todos

### IPP D32 · [PRODUCTO] Catálogo de régimen procesal

La app hoy tiene PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057 (más civiles/familia/comercial si ya están). ¿Agregar PBA_PEN_LEY_11922 (y variantes flagrancia/jurados)? No modificar el contrato de API ni el modelo de datos; solo registrar.

**Hitos afectados:** Hoja Flujo

### IPP D33 · [PRODUCTO] Hito final alcanzado desde un camino paralelo

Las derivaciones a hábeas corpus ('Sigue en la matriz de hábeas corpus') salen de caminos paralelos de libertad mientras la causa principal sigue abierta. ¿La app cierra el expediente al llegar a un hito final desde un camino paralelo, o solo crea el expediente vinculado y deja abiertos los demás caminos? Propuesta: en las derivaciones, crear el vinculado y no cerrar los otros caminos; registrar el requerimiento, sin cambiar el contrato de API ni el modelo de datos.

**Hitos afectados:** IPP_960, JOR_960

### IPP D34 · [PRODUCTO] Hito que se vuelve a abrir a sí mismo

En la IPP, el hito de pedidos de prueba (IPP_300) abre cada medida (allanamiento, pericia, testigos, intervenciones) y se vuelve a abrir a sí mismo con la misma condición, para que la investigación siga abierta. ¿El importador y el motor aceptan una transición cuyo destino es el mismo hito de origen? Propuesta: sí; si no, separar un hito 'IPP en trámite' sin plazo.

**Hitos afectados:** IPP_300

## 4. Juicio oral y público (`JOR`)

Planilla: [`matriz_penal_juicio_oral_pba.xlsx`](matriz_penal_juicio_oral_pba.xlsx) · diagrama: [`diagrama_penal_juicio_oral_pba.md`](diagrama_penal_juicio_oral_pba.md). 19 dudas. La última remite a las transversales y de producto de investigación.

### JOR D01 · Citación a juicio de 10 días (art. 338)

Verificado: plazo individual de 10 días desde la notificación de la integración para recusar y ofrecer prueba; en el mismo acto se pide audiencia preliminar (obligatoria con jurados). ¿El plazo corre desde la notificación a cada parte por separado? Propuesta: 10 CORRIDOS desde la notificación a la parte que representa el abogado. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_100

### JOR D02 · Plazo para realizar el debate (art. 339)

El debate debe hacerse dentro de 6 meses de la radicación, prorrogable una vez por instrucción suplementaria; si no, el órgano pierde la competencia. ¿Qué pasa después con la causa (nuevo tribunal, nuevo plazo)? ¿La app debe alertar a la defensa como oportunidad? Propuesta: 6 MESES en JOR_160 como camino paralelo. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_160

### JOR D03 · Instrucción suplementaria

¿Hay plazo máximo para cumplir la instrucción suplementaria? ¿Quién la produce? Propuesta: hito sin plazo con carga manual; prorroga una vez el plazo de 6 meses (art. 339). Norma a verificar.

**Hitos afectados:** JOR_140

### JOR D04 · Integración del órgano sin plazos propios en el juicio

El borrador anterior tenía hitos de 15 días en el juicio para optar por tribunal colegiado y renunciar al jurado. Verificado en los arts. 22 y 22 bis: ambas cosas se hacen en el plazo del art. 336, durante la IPP, y firme la elevación ya no se puede renunciar al jurado. Se quitaron esos hitos. ¿Hay algún caso en que la opción se ejerza en el juicio (por ejemplo, cambio de calificación)? Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_020, JOR_040

### JOR D05 · Juicio por jurados: plazos de la selección y de las instrucciones

La selección es el día fijado para el juicio (art. 338 quáter) y las instrucciones se discuten al cerrar el debate (art. 371 bis). Ninguna tiene plazo perentorio. ¿Hace falta un hito para la presentación anticipada y por escrito de las propuestas de instrucciones? Propuesta: checklist en JOR_320. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_310, JOR_320, JOR_330

### JOR D06 · Fundamentos del veredicto en 5 días (art. 374)

Verificado: hasta 5 días (7 con acción civil). ¿Los días se cuentan desde la audiencia de lectura del veredicto? ¿Se suspenden en feria? Propuesta: 5 CORRIDOS desde la lectura del veredicto; el abogado cambia a 7 si hay acción civil. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_500

### JOR D07 · Cesura del juicio (art. 372)

Verificado: sin jurados es facultativa y puede diferir la pena hasta 1 mes; con jurados es obligatoria y las partes ofrecen prueba hasta 5 días después del veredicto. ¿Conviene modelar esos plazos (1 MESES y 5 CORRIDOS) como hitos propios? Propuesta: checklist en JOR_510 hasta validar. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_510

### JOR D08 · Ampliación del requerimiento (art. 359)

¿Qué límites y formalidades tiene la ampliación? ¿Obliga a suspender el debate o a reabrir la prueba? Propuesta: hito sin plazo con checklist de defensa. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_430

### JOR D09 · Recurso contra la sentencia: casación o apelación (20 días)

Verificado: en lo criminal y en jurados (condena) hay casación (arts. 20 y 450); en lo correccional, apelación ante la Cámara (art. 21 inc. 4). Ambos plazos son de 20 días (arts. 441 y 451). ¿Después de la Cámara, en correccional, se va directo a los recursos extraordinarios ante la SCBA? Propuesta: sí, como salida de JOR_810. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_600, JOR_810, JOR_820

### JOR D10 · Manifestación de recurrir en casación (7 días)

Art. 451: dentro de los primeros 7 días del plazo hay que manifestar la intención de recurrir; si no, la sentencia queda firme para quien omitió. ¿Hace falta un hito propio de 7 CORRIDOS con alerta? Propuesta: sí en una próxima versión; por ahora, checklist en JOR_820. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_820

### JOR D11 · Feria y recursos contra la sentencia

Art. 139: la feria suspende la impugnación de la sentencia definitiva (salvo flagrancia). ¿El motor puede marcar JOR_810 y JOR_820 como 'suspende en feria'? Propuesta: sí; registrar el requerimiento al motor. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_810, JOR_820

### JOR D12 · Recursos extraordinarios SCBA y federal

Verificado: los recursos ante la SCBA se interponen en 10 días hábiles (art. 483). ¿Se cuentan con el calendario judicial PBA? Para el recurso federal (art. 257 CPCCN, 10 días hábiles), ¿qué calendario usa la app? Propuesta: JOR_830 en HABILES_JUDICIALES; JOR_840 sin plazo con carga manual. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_830, JOR_840

### JOR D13 · Libertad durante el juicio

Con imputado detenido, ¿bastan los hitos de excarcelación, alternativas y control del plazo máximo con detenido, o hace falta reabrir la cadena de aprehensión de la IPP? Propuesta: JOR_230/240/270/280/290 y hábeas. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_230, JOR_240, JOR_270, JOR_280, JOR_290

### JOR D14 · Cómputo de pena y derivación a ejecución

Art. 500: el juez o tribunal que dictó la sentencia hace practicar el cómputo. ¿Hay plazo? ¿La app solo alerta y deriva a 'Sigue en ejecución penal'? Propuesta: hito sin plazo y final JOR_970. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_900, JOR_910, JOR_970

### JOR D15 · Honorarios en el juicio oral

¿Se regulan con la sentencia o al quedar firme? ¿El plazo de 5 días del art. 57 Ley 14.967 es corrido (CPP) o hábil (CPCCBA)? Propuesta: 5 CORRIDOS sin gracia (misma duda transversal de la IPP).

**Hitos afectados:** JOR_550

### JOR D16 · Publicidad del debate y causa reservada

Art. 342: el debate puede hacerse a puertas cerradas para proteger la intimidad de la víctima o testigos. ¿Cómo se marca en la app sin filtrar datos sensibles? Propuesta: checklist en la apertura; sin registrar identidades protegidas. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_400

### JOR D17 · Derivación al abreviado desde el juicio

Art. 397: el acuerdo se puede presentar hasta 30 días antes del debate. La matriz deriva a JAB desde la audiencia preliminar y desde la fecha del debate. Si se desestima, ¿el juicio sigue con la misma fecha? Propuesta: volver a esta matriz desde JAB_320. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JOR_120, JOR_150, JOR_955

### JOR D18 · Equivalencia en el fuero federal

En los distritos federales con asiento en PBA rige el CPPF (Mar del Plata, Bahía Blanca, Rosario/San Nicolás y La Plata) o todavía el CPPN (San Martín). En el CPPF hay control de la acusación en audiencia y juicio ante tribunal unipersonal o colegiado; en el CPPN el juicio es ante el Tribunal Oral Federal, con recurso ante la Cámara Federal de Casación Penal. Esta matriz modela solo el juicio oral del CPP PBA. ¿Alcanza con el cuadro de equivalencias del README, o hay que avisar en la app cuando el expediente es federal? Propuesta: avisar y no aplicar esta matriz. Ver la duda de producto 'Matrices federales aparte' en la matriz de investigación.

**Hitos afectados:** JOR_010, JOR_600

### JOR D19 · Dudas transversales y de producto

Las dudas transversales del fuero penal (gracia, plazos con detenido, horas, plazos corridos, IPP, plazo máximo con detenido, víctima, prescripción, honorarios, V1) y las de producto (roles, represented_role, prejudicial, motor, vinculación, datos sensibles, matrices federales, catálogo de régimen, finales desde caminos paralelos, hitos que se reabren) se responden una sola vez en matriz_penal_investigacion_pba.xlsx. Las reglas del motor D26–D34 de la matriz laboral valen salvo donde el proceso penal se aparta. ¿Hay algo de esta matriz que se aparte de esas respuestas?

**Hitos afectados:** Todos

## 5. Juicio abreviado (`JAB`)

Planilla: [`matriz_penal_abreviado_pba.xlsx`](matriz_penal_abreviado_pba.xlsx) · diagrama: [`diagrama_penal_abreviado_pba.md`](diagrama_penal_abreviado_pba.md). 12 dudas. La última remite a las transversales y de producto de investigación.

### JAB D01 · Modelado del límite de 30 días (art. 397)

¿El plazo de 'hasta 30 días antes del debate' se modela como ANTICIPACION_HABILES_JUDICIALES (valor 30), como anticipación en CORRIDOS (hoy el motor no tiene ese tipo) o como SIN_PLAZO con checklist? Propuesta: SIN_PLAZO + checklist hasta confirmar; vencimiento más temprano. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_020

### JAB D02 · Órgano competente según la etapa

Si el acuerdo se presenta durante la IPP o la etapa intermedia, ¿resuelve el Juez de Garantías o debe esperarse la elevación al tribunal de juicio? ¿Cambia el cómputo del art. 399? Propuesta: checklist en JAB_130; el abogado indica el órgano. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_130, JAB_300

### JAB D03 · Inimpugnabilidad del rechazo (art. 398)

La desestimación es inimpugnable. ¿Hay supuestos en que igual proceda casación/queja si el rechazo se aparta de las causales legales (voluntad viciada / calificación)? Propuesta: no abrir recurso ordinario; solo derivar a juicio oral. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_300, JAB_320

### JAB D04 · Cómputo de los 5 días de sentencia (art. 399)

¿Los 5 días corren desde la admisión formal, desde la audiencia de visu o desde otra actuación? ¿Se suspenden en feria? Propuesta: 5 CORRIDOS desde la admisión; feria según art. 139 solo para la impugnación de la sentencia, no para dictarla. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_310

### JAB D05 · Casación vs apelación (art. 401)

Confirmar el criterio práctico para distinguir abreviado 'en lo criminal' (casación) y 'en lo correccional' (apelación): ¿competencia del órgano, escala penal o fuero del tribunal? Ambos recursos tienen 20 días contra la sentencia definitiva (arts. 441 y 451). Propuesta: hito JAB_600 con bifurcación manual. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_600, JAB_810, JAB_820

### JAB D06 · Opinión de la víctima vs art. 402

¿Qué peso tiene la opinión de la víctima (art. 396) si el particular damnificado no puede oponerse (art. 402)? ¿La omisión de convocatoria genera nulidad o solo agravio revisable? Propuesta: checklist obligatorio de convocatoria/notificación; no bloquear el acuerdo. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_120

### JAB D07 · Pluralidad de imputados (art. 400)

Si hay varios imputados y solo algunos acuerdan, ¿el abreviado puede prosperar respecto de los acordantes mientras los demás siguen a juicio oral? Propuesta: sí, salvo desestimación judicial; expedientes vinculados. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_100, JAB_400

### JAB D08 · Abreviado vs probation

¿Hay criterio del estudio o de la fiscalía local sobre cuándo preferir abreviado frente a suspensión del juicio a prueba? ¿Se documenta la opción rechazada? Propuesta: hito JAB_410 sin plazo. Norma: arts. 76 bis/ter CP y 395 CPP PBA.

**Hitos afectados:** JAB_410

### JAB D09 · Acción civil y sede competente (art. 403)

Si no hay conformidad de todas las partes civiles, ¿qué órgano civil de PBA recibe la remisión y con qué efecto sobre la sentencia penal? Propuesta: el penal sigue; civil fuera de esta matriz. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_500

### JAB D10 · Directísimo (403 bis) fuera de esta matriz

¿El juicio directísimo de flagrancia (art. 403 bis) debe tener matriz propia o alcanza con el hito JAB_400 y la remisión a investigación/flagrancia? Propuesta V1: solo el hito de relación; directísimo detalle fuera. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** JAB_400

### JAB D11 · Equivalencia en el fuero federal

En los distritos federales con asiento en PBA rige el CPPF (Mar del Plata, Bahía Blanca, Rosario/San Nicolás y La Plata) o todavía el CPPN (San Martín). En el CPPF hay acuerdos plenos, parciales y de colaboración (a verificar); en el CPPN, el juicio abreviado del art. 431 bis (a verificar). Esta matriz modela solo el juicio abreviado del CPP PBA. ¿Alcanza con el cuadro de equivalencias del README, o hay que avisar en la app cuando el expediente es federal? Propuesta: avisar y no aplicar esta matriz. Ver la duda de producto 'Matrices federales aparte' en la matriz de investigación.

**Hitos afectados:** JAB_100, JAB_300

### JAB D12 · Dudas transversales y de producto

Las dudas transversales del fuero penal (gracia, plazos con detenido, horas, plazos corridos, IPP, plazo máximo con detenido, víctima, prescripción, honorarios, V1) y las de producto (roles, represented_role, prejudicial, motor, vinculación, datos sensibles, matrices federales, catálogo de régimen, finales desde caminos paralelos, hitos que se reabren) se responden una sola vez en matriz_penal_investigacion_pba.xlsx. Las reglas del motor D26–D34 de la matriz laboral valen salvo donde el proceso penal se aparta. ¿Hay algo de esta matriz que se aparte de esas respuestas?

**Hitos afectados:** Todos

## 6. Hábeas corpus (`HCO`)

Planilla: [`matriz_penal_habeas_corpus_pba.xlsx`](matriz_penal_habeas_corpus_pba.xlsx) · diagrama: [`diagrama_penal_habeas_corpus_pba.md`](diagrama_penal_habeas_corpus_pba.md). 15 dudas. La última remite a las transversales y de producto de investigación.

### HCO D01 · Plazo de impugnación (art. 417)

El art. 417 CPP PBA no fija el plazo para impugnar la resolución de hábeas corpus ante Cámara o Casación. ¿Rige el de apelación (5 días corridos, art. 441), el de 24 horas de la Ley 23.098 federal, u otro? Propuesta: hito SIN_PLAZO con carga manual hasta confirmar. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_400

### HCO D02 · Audiencia obligatoria (arts. 412 y 413)

El art. 412 (texto Ley 13.252) dice que el órgano 'deberá' designar audiencia oral; el art. 413 dice que la celebración de la audiencia y la prueba son decisión exclusiva del órgano, y el art. 415 contempla resolver sin audiencia en 24 horas. ¿La audiencia es obligatoria o discrecional al 13/11/2026? Propuesta: modelar ambos caminos. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_200, HCO_220

### HCO D03 · Competencia: cualquier juez vs. juez penal

El art. 20 Const. PBA permite hábeas ante cualquier juez. El Decreto 2749/04 observó en el art. 406 la frase 'con competencia penal'. ¿Confirmamos competencia amplia, con remisión a Cámara de Garantías solo contra prisión preventiva (art. 406 párr. 3)? Propuesta: sí; checklist en HCO_020. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_020, HCO_100

### HCO D04 · Hábeas colectivo y Verbitsky (2005)

¿Qué requisitos exige la práctica bonaerense para el hábeas colectivo (homogeneidad, legitimación, remedio) tras Verbitsky (CSJN, 2005) y la jurisprudencia SCBA (p. ej. P.133.682)? ¿Se modela solo con checklist o hace falta un subflujo? Propuesta: checklist en HCO_010/HCO_330 hasta validar. Norma y fallos a verificar.

**Hitos afectados:** HCO_010, HCO_330

### HCO D05 · Hábeas contra prisión preventiva hasta el debate

Art. 405: el hábeas contra el auto de PP procede hasta la iniciación de la audiencia de debate. ¿La app debe bloquear la apertura de HCO desde IPP/JOR después de iniciado el debate, o solo alertar? Propuesta: alertar en checklist; no bloquear en V1. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_010

### HCO D06 · Cómputo del informe de 12 horas (art. 409)

¿Las 12 horas del informe corren en días y horas inhábiles (con detenido) sin suspensión por feria? Propuesta: HORAS desde fecha/hora del requerimiento, sin interrupción (vencimiento más temprano). Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_110

### HCO D07 · Continuación de prueba en 24 horas (art. 413)

Si la prueba no se incorpora en el mismo acto, ¿las 24 horas son corridas inclusive en inhábil? ¿Qué pasa si vence sin producirla? Propuesta: 24 HORAS; al vencer, pasar a resolución con la prueba incorporada. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_210

### HCO D08 · Disparador de la resolución de 24/48 horas (art. 415)

Sin audiencia: ¿las 24 horas corren desde la decisión de no celebrarla, desde el informe, o desde la interposición? Con audiencia: confirmar que las 48 horas corren desde el fin de la audiencia (incluida la continuación de prueba). Propuesta: disparadores como están en HCO_220 y HCO_230. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_220, HCO_230

### HCO D09 · Costas y sanciones en la resolución

Art. 415: la resolución se pronuncia sobre costas y sanciones. ¿Hay arancel o sanción típica? ¿Se regulan honorarios en el mismo acto (Ley 14.967)? Propuesta: hito HCO_900 de 5 CORRIDOS antes del cierre; si no hubo regulación, se cierra sin plazo. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_220, HCO_230, HCO_900

### HCO D10 · Vinculación con la matriz de investigación

Cuando el hábeas nace de una IPP (detención, PP, excarcelación) o remite denuncia (art. 416), ¿cómo se vinculan los expedientes sin copiar datos sensibles? Propuesta: la remisión de copias (HCO_500) es un camino paralelo que no cierra el hábeas; el hecho denunciado se investiga en un expediente nuevo; al terminar, HCO_950 vuelve a la causa principal. Ver duda de producto en la matriz de investigación.

**Hitos afectados:** HCO_500, HCO_950

### HCO D11 · Notificación al MPF (art. 418)

¿Basta la notificación oral con constancia del inicio, y después no se cita al fiscal en audiencia ni resolución? Propuesta: checklist en HCO_100; no modelar plazos adicionales. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_100

### HCO D12 · Estado de sitio (art. 419)

¿Hace falta un hito o solo una nota de que el hábeas procede y debe resolverse aún durante el estado de sitio? Propuesta: solo nota en instrucciones; no modelar hito. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_020

### HCO D13 · Consulta o elevación obligatoria de la resolución

La Ley 23.098 (federal) no rige en PBA, y los arts. 405 a 420 CPP PBA no prevén una consulta o elevación obligatoria de la resolución que rechaza el hábeas. ¿Hay alguna acordada de la SCBA o práctica departamental que la imponga? Propuesta: no se modela; solo la impugnación del art. 417. Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar y leyes-ar.com (última actualización citada 16/10/2026).

**Hitos afectados:** HCO_300, HCO_400

### HCO D14 · Equivalencia en el fuero federal

En los distritos federales con asiento en PBA rige el CPPF (Mar del Plata, Bahía Blanca, Rosario/San Nicolás y La Plata) o todavía el CPPN (San Martín). Ley 23.098 (arts. 3 a 23, a verificar), con competencia del juez federal cuando la autoridad requerida es nacional. Esta matriz modela solo el hábeas corpus del CPP PBA. ¿Alcanza con el cuadro de equivalencias del README, o hay que avisar en la app cuando el expediente es federal? Propuesta: avisar y no aplicar esta matriz. Ver la duda de producto 'Matrices federales aparte' en la matriz de investigación.

**Hitos afectados:** HCO_010, HCO_020

### HCO D15 · Dudas transversales y de producto

Las dudas transversales del fuero penal (gracia, plazos con detenido, horas, plazos corridos, IPP, plazo máximo con detenido, víctima, prescripción, honorarios, V1) y las de producto (roles, represented_role, prejudicial, motor, vinculación, datos sensibles, matrices federales, catálogo de régimen, finales desde caminos paralelos, hitos que se reabren) se responden una sola vez en matriz_penal_investigacion_pba.xlsx. Las reglas del motor D26–D34 de la matriz laboral valen salvo donde el proceso penal se aparta. ¿Hay algo de esta matriz que se aparte de esas respuestas?

**Hitos afectados:** Todos

## 7. Citas y datos marcados "(a verificar)"

Son las citas de `Base_Normativa`, los eventos de inicio y los ítems del checklist que no se pudieron confirmar en normas.gba.gob.ar ni en leyes-ar.com al 13/11/2026. El abogado confirma o corrige la cita y, si corresponde, el plazo del hito.

### En las partes comunes (aparecen en más de una matriz)

- **Plazos con detenido** (checklist): "Con detenido: corre en días inhábiles (a verificar)". Es la misma pregunta que la duda IPP D16. Hitos: `IPP_200`, `IPP_210`, `IPP_220`, `IPP_240`, `IPP_250`, `IPP_260`, `IPP_700`, `IPP_710`, `JOR_240`, `HCO_110`, `HCO_210`, `HCO_220`, `HCO_230`.
- **Control del plazo máximo con detenido (2 años)** (evento de inicio): Inicio de la privación de libertad (disparador a verificar). Hitos: `IPP_290`, `JOR_290`.
- **Control del plazo máximo con detenido (2 años)** (base normativa): Art. 141 CPP PBA (términos fatales con detenido); art. 2 (plazo razonable); Ley 24.390 (a verificar aplicación en PBA). Hitos: `IPP_290`, `JOR_290`.
- **Control del plazo máximo con detenido (2 años)** (checklist): Con detenido: corre en días inhábiles y no se suspende en feria (a verificar). Hitos: `IPP_290`, `JOR_290`.
- **Recurso extraordinario federal** (base normativa): Art. 14 Ley 48; art. 257 CPCCN (plazo de 10 días hábiles, a verificar cómputo). Hitos: `JOR_840`, `JAB_840`.
- **Recurso extraordinario federal** (checklist): Cargar el plazo como plazo suelto: 10 días hábiles con el calendario judicial federal, no el de PBA (a verificar). Hitos: `JOR_840`, `JAB_840`.

### Investigación Penal Preparatoria

- **`IPP_100` Apertura o radicación de la IPP ante el Fiscal** (base normativa): Arts. 266 a 270 CPP PBA; Ley 14.442 del Ministerio Público (a verificar).
- **`IPP_120` Citación y declaración del imputado no detenido** (checklist): Si hay riesgo de detención, evaluar la eximición de prisión (arts. 185 y ss., a verificar).
- **`IPP_210` Comunicación al Juez de Garantías y puesta a disposición** (base normativa): Arts. 155, 161 y 284 ter CPP PBA (plazo concreto de puesta a disposición ante el juez, a verificar).
- **`IPP_220` Declaración del imputado (con detenido: 24 horas)** (checklist): Si el imputado lo pide motivadamente, puede declarar ante el Juez de Garantías (a verificar).
- **`IPP_330` Testimoniales, reconocimientos e informes** (checklist): Víctimas y testigos vulnerables: medidas de protección (art. 83 CPP PBA; Ley 27.372, a verificar).
- **`IPP_340` Intervención de comunicaciones y otras medidas restrictivas** (base normativa): Art. 229 CPP PBA (plazos máximos y prórrogas, a verificar).
- **`IPP_520` Mediación penal** (base normativa): Ley 13.433 (mediación penal; a verificar vigencia y alcance).
- **`IPP_540` Conciliación o reparación integral** (base normativa): Art. 59 inc. 6 Código Penal; arts. 86 y 87 CPP PBA (a verificar aplicación procesal).

### Juicio abreviado

- **`JAB_400` Abreviado en flagrancia o pedido temprano** (base normativa): Arts. 284 quinquies, 395 a 397 y 403 bis CPP PBA (Ley 13.811, a verificar).

### Hábeas corpus

- **`HCO_010` Evaluación del tipo de hábeas corpus** (checklist): Si se excedió el plazo máximo con detenido (art. 141), evaluar hábeas o pedido de cese ante el juez de la causa (a verificar).
- **`HCO_330` Corrección de condiciones de detención (correctivo)** (base normativa): Arts. 405 y 415 CPP PBA; jurisprudencia correctiva/colectiva (Verbitsky 2005; a verificar).
- **`HCO_400` Impugnación ante Cámara o Casación (art. 417)** (base normativa): Art. 417 CPP PBA (plazo concreto a verificar).
