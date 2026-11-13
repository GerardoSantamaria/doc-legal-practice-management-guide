# Matrices laborales por tipo de reclamo

Tres matrices del fuero laboral de la Provincia de Buenos Aires, una por tipo de reclamo, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado**. Las citas son orientativas: las marcadas "a verificar" o "verificar vigencia" no se usan hasta que el abogado las confirme.

| Tipo de reclamo | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Indemnización por despido | `matriz_laboral_despido_pba.xlsx` | `diagrama_laboral_despido_pba.md` | 43 | 94 | 11 |
| Accidentes de trabajo y enfermedades profesionales | `matriz_laboral_accidentes_pba.xlsx` | `diagrama_laboral_accidentes_pba.md` | 45 | 87 | 15 |
| Reclamos salariales | `matriz_laboral_reclamos_salariales_pba.xlsx` | `diagrama_laboral_reclamos_salariales_pba.md` | 38 | 78 | 10 |

## Qué cubre cada una

**Despido** (prefijo `DSP`). Despido sin causa y con causa (rechazo de la causa invocada), intimación a retomar tareas y abandono de trabajo, trabajo no registrado o mal registrado (intimación del art. 11 Ley 24.013 con la copia a ARCA), otras injurias con intimación del art. 57 LCT, despido indirecto, certificados del art. 80, liquidación final, intimación de pago de las indemnizaciones (art. 2 Ley 25.323) y conciliación previa.

**Accidentes** (prefijo `ACC`). Denuncia del siniestro, aceptación o rechazo de la ART, prestaciones e ILT, trámite ante la Comisión Médica Jurisdiccional (audiencia, plazo para expedirse, dictamen, homologación), recurso ante la Comisión Médica Central o acción ante el Tribunal de Trabajo, pago de la indemnización, empleador sin ART o trabajador no registrado, y la opción por la acción civil como salida del flujo. Agrega la fase `Comisión médica` entre la etapa previa y la demanda.

**Reclamos salariales** (prefijo `SAL`). Plazo de pago del sueldo (art. 128 LCT), diferencias por categoría o convenio, horas extra, comisiones, SAC y vacaciones, impugnación de sanciones disciplinarias (art. 67), aportes retenidos y no depositados (art. 132 bis), intimación del art. 57 y conciliación. Es el único que modela el **reclamo con el vínculo vigente**; si el trabajador se considera despedido, el flujo termina y el expediente sigue en la matriz de despido.

## Cómo se relacionan con la matriz general

- **La etapa judicial es la misma en las tres** (demanda, contestación, prueba, vista de causa, sentencia, recursos, ejecución y acuerdo, hitos `_050` a `_990`). Se copia de `herramientas/matriz/datos.py` cambiando el prefijo, y cada tipo ajusta solo el checklist y la documentación de algunos hitos (por ejemplo, la demanda o la pericia médica).
- **Las reglas del motor, el régimen procesal y las dudas de la etapa judicial se responden una sola vez**, en la matriz general. Cada matriz de esta carpeta tiene una última duda que lo recuerda y pregunta si va a reemplazar a la general para su tipo de reclamo o si van a convivir.
- **Accidentes de trabajo estaba fuera de la V1** (sección 4 de `analisis_y_definiciones_pendientes_v1.md`). Esta matriz sirve para validar el flujo; incluirlo en la V1 es una decisión aparte, que además depende de cómo se traten los datos de salud (duda D14 de esa matriz).

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos; sin ese argumento siguen generando la matriz general.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=despido   # o accidentes, o reclamos_salariales

$PY generar.py ../../laboral/matriz_laboral_${CASO}_pba.xlsx ../../laboral/salida/tablas_${CASO}.md ../../laboral/datos/${CASO}.py
$PY verificar_excel.py ../../laboral/matriz_laboral_${CASO}_pba.xlsx ../../laboral/datos/${CASO}.py
$PY diagrama.py ../../laboral/matriz_laboral_${CASO}_pba.xlsx ../../laboral/diagrama_laboral_${CASO}_pba.md ../../laboral/salida/diagrama_${CASO}.md ../../laboral/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `datos/comun.py` | Lo que comparten las tres: valores permitidos, grupos del diagrama, datos de la hoja `Flujo`, la etapa judicial tomada de la matriz general y la duda que remite a ella. |
| `datos/despido.py`, `datos/accidentes.py`, `datos/reclamos_salariales.py` | Hitos, transiciones y dudas de cada tipo de reclamo. Son la fuente del borrador. |
| `salida/` | Tablas en Markdown y vista general de cada diagrama. Las generan los scripts; no se editan a mano. |

**Igual que con la matriz general, `generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py` y `generar.py` no se vuelve a correr sobre esa planilla.
