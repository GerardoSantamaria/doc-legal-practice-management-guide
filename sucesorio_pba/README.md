# Proceso sucesorio en la Provincia de Buenos Aires

Matriz de flujo procesal del sucesorio (ab intestato y testamentario) ante los juzgados Civiles y Comerciales y los Juzgados de Paz Letrados de la Provincia de Buenos Aires, con su diagrama. Es el primer flujo del fuero Civil y Comercial. Tiene el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office la importa igual.

Es un **borrador para validar con el abogado**. Las citas se cotejaron con textos actualizados al 13/11/2026; las marcadas "(a verificar)" no se pudieron confirmar y tienen su duda en la hoja `Dudas_a_validar`.

| Archivo | Qué es |
| :--- | :--- |
| `matriz_flujo_sucesorio_pba.xlsx` | La planilla: 61 hitos (prefijo `SUC`), 139 transiciones y 45 dudas. |
| `diagrama_flujo_sucesorio_pba.md` | Diagramas Mermaid generados desde la planilla: la vista general por fases y un diagrama por grupo de fases. |
| `dudas_a_validar.md` | Lo que tiene que validar el abogado: las 45 dudas por bloque, las cinco de mayor impacto y las citas marcadas "(a verificar)" en los hitos. Tiene el mismo texto que la hoja `Dudas_a_validar`. |
| `datos/datos_sucesorio.py` | Hitos, transiciones, dudas, fases, grupos del diagrama y textos propios del sucesorio (roles, leyenda, ejemplo de caminos paralelos). Es la fuente del borrador. |
| `salida/tablas.md` | Las tablas en Markdown. La genera `generar.py`; no se edita a mano. |
| `salida/diagrama.md` | La vista general sola. La genera `diagrama.py`; no se edita a mano. |

## Uso de los roles

El sucesorio no tiene demandado, pero `Rol_Responsable` es un enum cerrado. Se usa así (está explicado en la hoja `Valores` y abierto como duda de producto D41):

| Rol | En el sucesorio |
| :--- | :--- |
| `ACTORA` | El heredero o interesado que promueve y al que representamos. |
| `DEMANDADA` | Otros interesados con intereses opuestos en una incidencia: coherederos que impugnan, acreedores, el cónyuge en la liquidación de los gananciales. |
| `TRIBUNAL` | El juzgado o la espera de un organismo (registros, ARBA); el nombre del hito aclara cuál. |
| `AMBAS` | Cualquiera de los interesados. |

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Los scripts son los mismos que los de la matriz laboral: cada uno recibe como último argumento el módulo de datos, y sin ese argumento siguen generando la matriz laboral.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
S=../../sucesorio_pba

$PY generar.py $S/matriz_flujo_sucesorio_pba.xlsx $S/salida/tablas.md $S/datos/datos_sucesorio.py
$PY verificar_excel.py $S/matriz_flujo_sucesorio_pba.xlsx $S/datos/datos_sucesorio.py
$PY diagrama.py $S/matriz_flujo_sucesorio_pba.xlsx $S/diagrama_flujo_sucesorio_pba.md $S/salida/diagrama.md $S/datos/datos_sucesorio.py
```

`verificar_excel.py` tiene que mostrar todos los controles en `OK`, `Nodo inicial: OK` y, con los errores inyectados, `El plazo debe ser 0 | Destino inexistente | Este tipo no lleva gracia`.

**`generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: el diagrama se regenera solo con `diagrama.py` (que lee la planilla) y `generar.py` no se vuelve a correr sobre ella. Los cambios que pida el abogado se cargan en la planilla y, si hace falta, también en `datos/datos_sucesorio.py` para no perderlos.
