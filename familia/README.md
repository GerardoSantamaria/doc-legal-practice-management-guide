# Matrices del fuero de Familia por tipo de proceso

Cinco matrices del fuero de Familia de la Provincia de Buenos Aires, una por tipo de proceso, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado** (versión 1, 13/11/2026, sin validar). Las citas se cotejaron con textos actualizados (normas.gba.gob.ar y leyes-ar.com), pero son orientativas: las marcadas "a verificar" no se usan hasta que el abogado las confirme, y cada una tiene su duda.

| Tipo de proceso | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Alimentos | `matriz_familia_alimentos_pba.xlsx` | `diagrama_familia_alimentos_pba.md` | 47 | 109 | 50 |
| Divorcio | `matriz_familia_divorcio_pba.xlsx` | `diagrama_familia_divorcio_pba.md` | 48 | 105 | 18 |
| Cuidado personal y régimen de comunicación | `matriz_familia_cuidado_personal_pba.xlsx` | `diagrama_familia_cuidado_personal_pba.md` | 46 | 107 | 17 |
| Violencia familiar: medidas de protección | `matriz_familia_violencia_pba.xlsx` | `diagrama_familia_violencia_pba.md` | 29 | 63 | 20 |
| Adopción | `matriz_familia_adopcion_pba.xlsx` | `diagrama_familia_adopcion_pba.md` | 38 | 76 | 20 |

La matriz de alimentos tiene 20 dudas propias, 18 de la etapa común y 12 de producto. Las otras cuatro tienen solo sus dudas propias y una última duda que remite a alimentos.

## Qué cubre cada una

**Alimentos** (prefijo `ALI`). Es la matriz de referencia. Cubre la interpelación al alimentante y el plazo para demandar con efecto retroactivo, la etapa previa ante el Consejero de Familia, los alimentos provisorios, la audiencia y la sentencia del juicio de alimentos, la intimación y la ejecución de las cuotas atrasadas, el empleador que no retiene o no deposita la cuota, los incidentes de aumento, reducción, cese o coparticipación, el control de los 21 años del hijo, y la compensación económica entre ex cónyuges o ex convivientes con su caducidad, que tramita por la etapa común. Es la única que tiene las dudas de la etapa común y de producto.

**Divorcio** (prefijo `DIV`). Cubre la petición unilateral o conjunta con propuesta de convenio regulador (art. 438 CCyC), la contrapropuesta, la audiencia y la sentencia, las medidas provisionales previas, el matrimonio celebrado en el extranjero, la inscripción, la caducidad de la compensación económica y las cuestiones pendientes (vivienda y liquidación de la comunidad). Las cuestiones pendientes usan la etapa común. Alimentos y cuidado de los hijos se derivan a sus matrices.

**Cuidado personal y régimen de comunicación** (prefijo `CUI`). Cubre el plan de parentalidad, las medidas provisorias, la etapa común con la escucha del niño y el abogado del niño, el incumplimiento del régimen y las medidas del juez, la modificación del régimen, la autorización para salir del país o cambiar la residencia, la restitución internacional y la delegación del ejercicio o la guarda a un pariente.

**Violencia familiar** (prefijo `VIO`). Tiene trámite propio (Ley 12.569), sin la etapa común. Cubre la denuncia y su remisión al juzgado, las medidas de protección en 48 horas, el dispositivo de alerta y las comunicaciones, las audiencias y el informe interdisciplinario en 48 horas, el control de eficacia, el incumplimiento y las sanciones, la apelación en 3 días hábiles, la modificación y el cese de las medidas, la intervención del Servicio Local cuando hay niños y los honorarios. Modela también el expediente de la persona denunciada.

**Adopción** (prefijo `ADO`). Tiene trámite propio (Ley 14.528, texto Ley 15.610, y art. 35 bis Ley 13.298). Cubre la inscripción en el Registro Central de Aspirantes, la entrega directa o guarda de hecho, la medida de abrigo con su control de legalidad y su plazo máximo, la búsqueda de la familia de origen, la declaración de la situación de adoptabilidad (por manifestación de los progenitores, vencimiento de la medida o búsqueda agotada), la guarda con fines de adopción (selección, vinculación, otorgamiento, seguimiento y revocación), el juicio de adopción y las acciones posteriores (conversión, revocación, nulidad y acceso a los orígenes).

## Cómo se relacionan entre sí

- **La etapa contenciosa común del Libro VIII del CPCCBA** (etapa previa ante el Consejero, demanda, contestación, audiencia preliminar, prueba, vista de causa, sentencia, recursos y ejecución) está en `datos/comun.py`. Alimentos, divorcio y cuidado personal la usan cambiando el prefijo y ajustando algunos hitos. Violencia y adopción tienen trámite propio y no la usan.
- **Las dudas de la etapa común y las de producto se responden una sola vez**, en la matriz de alimentos (marcadas `[ETAPA COMÚN]` y `[PRODUCTO]`). Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx`) también valen para familia y no se repiten.
- **Las derivaciones son hitos finales "Sigue en la matriz de ..."**. Divorcio deriva a alimentos y a cuidado personal, cuidado personal deriva a alimentos, y violencia deriva a alimentos y a cuidado personal. La forma de vincular los dos expedientes es una duda de producto.
- **La V1 se define sobre el fuero laboral** y deja fuera otros procesos (sección 4, punto 9, de `analisis_y_definiciones_pendientes_v1.md`). Estas matrices sirven para validar los flujos de familia. Incluirlo en la V1 es una decisión aparte, que depende de las dudas de producto sobre roles, expediente reservado y datos sensibles. Ninguna de estas matrices modifica el contrato de API ni el modelo de datos: lo que haría falta cambiar quedó registrado como duda.

## Datos sensibles

Los expedientes de familia tienen acceso limitado (art. 708 CCyC) y el de adopción es reservado (art. 617 inc. e CCyC). Involucran niños, víctimas de violencia y datos de salud. Por eso:

- **Ni las planillas ni los diagramas tienen datos personales** reales ni de ejemplo. Los checklists nombran los documentos ("partida de nacimiento del hijo"), no su contenido.
- **Al cargar un expediente no se copian en la app** nombres de niños, domicilios de víctimas, perímetros de exclusión, datos del dispositivo de alerta, contenido de informes de equipos técnicos ni datos de la familia de origen.
- **Los avisos de violencia** no pueden revelar datos de la víctima ni llegar a un dispositivo que comparte con la persona denunciada.

Las dudas de producto de la matriz de alimentos piden registrar estos riesgos en `modelado_de_amenazas_v1.md` y revisar la política de privacidad. Esos documentos no se modificaron.

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=alimentos   # o divorcio, cuidado_personal, violencia, adopcion

$PY generar.py ../../familia/matriz_familia_${CASO}_pba.xlsx ../../familia/salida/tablas_${CASO}.md ../../familia/datos/${CASO}.py
$PY verificar_excel.py ../../familia/matriz_familia_${CASO}_pba.xlsx ../../familia/datos/${CASO}.py
$PY diagrama.py ../../familia/matriz_familia_${CASO}_pba.xlsx ../../familia/diagrama_familia_${CASO}_pba.md ../../familia/salida/diagrama_${CASO}.md ../../familia/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `dudas_a_validar.md` | Las dudas de las cinco planillas, las citas marcadas "(a verificar)" y las decisiones de modelado a confirmar, para la reunión con el abogado. |
| `datos/comun.py` | Lo que comparten las cinco: valores permitidos, datos de la hoja `Flujo`, régimen procesal, la etapa contenciosa común, las dudas de la etapa común y de producto, y la duda que remite a alimentos. |
| `datos/alimentos.py`, `datos/divorcio.py`, `datos/cuidado_personal.py`, `datos/violencia.py`, `datos/adopcion.py` | Hitos, transiciones y dudas de cada tipo de proceso. Son la fuente del borrador. |
| `salida/` | Tablas en Markdown y vista general de cada diagrama. Las generan los scripts; no se editan a mano. |

**Igual que con la matriz general, `generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py` y `generar.py` no se vuelve a correr sobre esa planilla.
