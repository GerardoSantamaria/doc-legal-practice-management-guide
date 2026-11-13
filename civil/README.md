# Matrices del fuero Civil y Comercial por tipo de proceso

Cinco matrices del fuero Civil y Comercial de la Provincia de Buenos Aires, una por tipo de proceso, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado**. Las citas se cotejaron al 13/11/2026 con normas.gba.gob.ar y leyes-ar.com; las marcadas "a verificar" no se usan hasta que el abogado las confirme y cada una tiene su duda. Todas las dudas y las citas a verificar están reunidas en [`dudas_a_validar.md`](dudas_a_validar.md).

| Tipo de proceso | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Sucesorio | `matriz_civil_sucesorio_pba.xlsx` | `diagrama_civil_sucesorio_pba.md` | 60 | 130 | 41 |
| Daños y perjuicios | `matriz_civil_danos_y_perjuicios_pba.xlsx` | `diagrama_civil_danos_y_perjuicios_pba.md` | 59 | 135 | 30 |
| Desalojo | `matriz_civil_desalojo_pba.xlsx` | `diagrama_civil_desalojo_pba.md` | 50 | 117 | 13 |
| Prescripción adquisitiva (usucapión) | `matriz_civil_prescripcion_adquisitiva_pba.xlsx` | `diagrama_civil_prescripcion_adquisitiva_pba.md` | 49 | 113 | 15 |
| Incumplimiento contractual | `matriz_civil_contratos_pba.xlsx` | `diagrama_civil_contratos_pba.md` | 60 | 139 | 14 |

## Qué cubre cada una

**Sucesorio** (prefijo `SUC`). Proceso voluntario: ab intestato y testamentario (protocolización del ológrafo o cerrado, testamento por acto público), apertura, Registro de Testamentos y de Juicios Universales, edictos y citación de herederos y acreedores, intervención del Ministerio Público, declaratoria de herederos y su ampliación o impugnación, intimación a aceptar o renunciar, herencia vacante, aprobación del testamento, administración y rendición de cuentas, inventario y avalúo, partición privada o judicial, colación y reducción, inscripción de inmuebles, automotores y otros bienes, tracto abreviado, ITGB, tasa de justicia y sobretasa, bono Ley 8480, aportes Ley 6716 y honorarios Ley 14.967. No tiene mediación ni la etapa contenciosa común. Es la matriz que reúne las **dudas técnicas del producto** (roles, rol representado, etapa prejudicial y judicial, catálogo de régimen procesal).

**Daños y perjuicios** (prefijo `DYP`). Juicio sumario. Accidentes de tránsito, responsabilidad contractual y daños a bienes; reclamo previo a la aseguradora, historia clínica y prueba anticipada, carta documento y convenio extrajudicial, prescripción de 3 años y su suspensión, mediación obligatoria, citación en garantía de la aseguradora, suspensión de la sentencia por causa penal en trámite y pago de la aseguradora hasta el límite de cobertura o la franquicia. Es la matriz que reúne las **dudas de la etapa contenciosa común**.

**Desalojo** (prefijo `DES`). Juicio sumario. Intimación de pago previa (art. 1222 CCyC), intimación a restituir, restitución voluntaria, constatación de la ocupación, denuncia penal por usurpación, mediación optativa, desocupación inmediata bajo caución (arts. 676 bis y ter CPCCBA), plazo para desocupar, mandamiento y diligencia de lanzamiento, consulta al Registro de Villas y Asentamientos (art. 678 bis, Ley 14.449) y toma de posesión. El cobro de alquileres va en juicio aparte. Reemplaza la ejecución dineraria común por la fase `Lanzamiento`.

**Prescripción adquisitiva** (prefijo `USU`). Juicio sumario. Cómputo de la posesión (20 años, o 10 con justo título y buena fe), informe de dominio, plano de mensura visado por Geodesia, regularización por Ley 24.374, la usucapión opuesta como defensa, anotación de litis, citación del titular con domicilio conocido o por edictos, Defensor Oficial de Ausentes, citación del Fisco y de la Municipalidad, inscripción de la sentencia en el Registro de la Propiedad y alta en ARBA. Agrega las fases `Citaciones` e `Inscripción`.

**Incumplimiento contractual** (prefijo `CTR`). Juicio ordinario (la escrituración, la resolución de compraventa de inmuebles y la consignación son sumario: ver duda D01). Opción entre cumplimiento y resolución con daños, cláusula resolutoria expresa (art. 1086 CCyC), emplazamiento del art. 1088 (no menor a 15 días), compraventa (boleto, citación a escriturar, entrega, precio, vicios redhibitorios), locación sin desalojo (reparaciones del art. 1201, resolución por el locatario), fideicomiso (rendición de cuentas y remoción del fiduciario, art. 1678), consignación extrajudicial y judicial, excepción de incumplimiento (art. 1031), contratos de consumo (art. 53 Ley 24.240) y la condena a escriturar con firma del juez (art. 510 CPCCBA).

## Cómo se relacionan entre sí y con la matriz general

- **La etapa contenciosa es la misma en las cuatro con demanda** (demanda, beneficio de litigar sin gastos, cautelares, contestación y excepciones, prueba, sentencia, recursos, ejecución, honorarios, acuerdo y caducidad, hitos `_300` a `_990`). Se define una sola vez en `datos/comun.py`, en su versión de juicio sumario u ordinario, y cada tipo agrega checklist, quita hitos que no usa o redirige salidas.
- **Las dudas de la etapa común se responden una sola vez**, en la matriz de daños y perjuicios. Desalojo, prescripción adquisitiva y contratos tienen una última duda que lo recuerda.
- **Las dudas del producto se responden en la matriz del sucesorio.** Las otras cuatro tienen una duda que remite a ella. Se registran, pero no cambian el contrato de API ni el modelo de datos.
- **Las reglas del motor (dudas D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx`) no se duplican.** El sucesorio y daños y perjuicios preguntan si valen sin cambios para el fuero civil.
- `sucesorio_pba/` es un borrador anterior del sucesorio hecho por separado. Hay que decidir cuál de los dos queda.

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos; sin ese argumento siguen generando la matriz general.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=sucesorio   # o danos_y_perjuicios, desalojo, prescripcion_adquisitiva, contratos

$PY generar.py ../../civil/matriz_civil_${CASO}_pba.xlsx ../../civil/salida/tablas_${CASO}.md ../../civil/datos/${CASO}.py
$PY verificar_excel.py ../../civil/matriz_civil_${CASO}_pba.xlsx ../../civil/datos/${CASO}.py
$PY diagrama.py ../../civil/matriz_civil_${CASO}_pba.xlsx ../../civil/diagrama_civil_${CASO}_pba.md ../../civil/salida/diagrama_${CASO}.md ../../civil/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `datos/comun.py` | Lo que comparten las cinco: valores permitidos, grupos del diagrama, datos de la hoja `Flujo`, la mediación (Ley 13.951), la etapa contenciosa común (sumario y ordinario), sus dudas y las dudas que remiten al producto, a la etapa común y al motor. |
| `datos/sucesorio.py`, `datos/danos_y_perjuicios.py`, `datos/desalojo.py`, `datos/prescripcion_adquisitiva.py`, `datos/contratos.py` | Hitos, transiciones y dudas de cada tipo de proceso. Son la fuente del borrador. |
| `salida/` | Tablas en Markdown y vista general de cada diagrama. Las generan los scripts; no se editan a mano. |

**Igual que con la matriz general, `generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py` y `generar.py` no se vuelve a correr sobre esa planilla.
