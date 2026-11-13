# Matrices del fuero Penal (Provincia de Buenos Aires)

Cuatro matrices del proceso penal provincial, una por tipo de flujo, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado**. Las citas se cotejaron el 13/11/2026 con normas.gba.gob.ar, leyes-ar.com y el cronograma de implementación del CPPF; las marcadas "(a verificar)" no se usan hasta que el abogado las confirme.

**Alcance:** solo fuero penal provincial (CPP PBA, Ley 11.922). No modelan el fuero federal ni el penal económico.

| Flujo | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Investigación Penal Preparatoria | `matriz_penal_investigacion_pba.xlsx` | `diagrama_penal_investigacion_pba.md` | 53 | 139 | 34 |
| Juicio oral y público | `matriz_penal_juicio_oral_pba.xlsx` | `diagrama_penal_juicio_oral_pba.md` | 43 | 82 | 19 |
| Juicio abreviado | `matriz_penal_abreviado_pba.xlsx` | `diagrama_penal_abreviado_pba.md` | 23 | 41 | 12 |
| Hábeas corpus | `matriz_penal_habeas_corpus_pba.xlsx` | `diagrama_penal_habeas_corpus_pba.md` | 20 | 50 | 15 |

Las 80 dudas y las citas que quedaron "(a verificar)" están reunidas en [`dudas_a_validar.md`](dudas_a_validar.md), con un orden sugerido para empezar.

## Qué cubre cada una

**Investigación (`IPP`)**. Denuncia y actuación de oficio, particular damnificado, designación de defensor, aprehensión/detención, declaración del imputado (art. 308), excarcelación, prisión preventiva y plazo máximo con detenido (art. 141), prueba (allanamientos, pericias, testimoniales, intervenciones; cada medida se abre en paralelo y la investigación sigue), revisión de diligencias denegadas (art. 334), plazo de la IPP (art. 282) y prórrogas, archivo, criterios especiales (art. 56 bis), mediación, probation, conciliación y prescripción, etapa intermedia (requerimiento, sobreseimiento con particular damnificado del art. 334 bis, oposición del art. 336, elevación y apelación), flagrancia (arts. 284 bis a 284 sexies) y derivaciones a juicio oral, abreviado, hábeas corpus o ejecución. Reúne las **dudas transversales y de producto** del fuero.

**Juicio oral (`JOR`)**. Radicación ante Juzgado Correccional o Tribunal en lo Criminal (art. 22) o jurados (art. 22 bis), citación a juicio con 10 días para recusar y ofrecer prueba (art. 338), audiencia preliminar, plazo de 6 meses para el debate (art. 339), selección del jurado, debate, instrucciones y veredicto del jurado (incluido el jurado estancado), veredicto del tribunal técnico, cesura (art. 372), sentencia, recursos (casación o apelación de 20 días, extraordinarios, reenvío a nuevo juicio), cómputo de pena y derivación a ejecución.

**Juicio abreviado (`JAB`)**. Oportunidad del acuerdo (hasta 30 días antes del debate, art. 397), requisitos (arts. 395-396), audiencia de conocimiento personal, admisión o rechazo (el proceso continúa en la IPP o en el juicio oral, según la etapa), sentencia en 5 días (art. 399), recursos y relación con flagrancia/probation.

**Hábeas corpus (`HCO`)**. Reparador, preventivo, correctivo y colectivo; interposición informal (arts. 406-407); informe en 12 horas; presentación del detenido; audiencia y resolución en horas (art. 415); impugnación (art. 417); remisión de copias por delito o falta grave (arts. 416 y 420) en paralelo; costas y honorarios.

## Alcance provincial y equivalencias con el proceso federal

Estas matrices **no** cubren narcotráfico, trata, contrabando ni evasión: tramitan en la justicia federal.

| Distrito federal con asiento en / sobre PBA (al 13/11/2026) | Código que rige |
| :--- | :--- |
| Mar del Plata | CPPF (Ley 27.063 T.O. 2019) |
| Bahía Blanca | CPPF |
| Rosario / San Nicolás de los Arroyos | CPPF |
| La Plata | CPPF desde el 21/09/2026 (Res. MJ 275/2026) |
| San Martín | CPPN (Ley 23.984) hasta que se fije fecha de implementación del CPPF |
| CABA / Penal Económico (referencia) | CPPF previsto para el 15/02/2027 |

**Propuesta:** sí hacen falta matrices federales aparte (carpeta futura `federal/` o similar), porque el vocabulario y los plazos no coinciden con el CPP PBA. Ver duda de producto en la matriz de investigación.

### Cuadro de equivalencias federal ↔ PBA

| Instituto federal (CPPN / práctica mixta) | Equivalente en CPP PBA | Notas |
| :--- | :--- | :--- |
| Indagatoria | Declaración del imputado (art. 308) | No usar "indagatoria" en las matrices PBA. |
| Procesamiento | No hay equivalente exacto | En PBA la coerción típica es la prisión preventiva (arts. 157/158); la elevación cierra la IPP. |
| Falta de mérito | Sobreseimiento / archivo / no elevación | El CPP PBA no usa "falta de mérito" como auto típico del juez de instrucción. |
| Juez de instrucción | Fiscal (IPP) + Juez de Garantías (control) | Sistema acusatorio. |
| Elevación a juicio | Requerimiento (334) + oposición (336) + auto/decreto (337) | Etapa intermedia ante el Juez de Garantías. |
| Excarcelación | Excarcelación / eximición de prisión (arts. 169 y ss.) | Vocabulario coincidente en lo sustancial. |
| Juicio abreviado | Arts. 395 a 403 | Límite: pena pedida ≤ 15 años (art. 395). |
| Hábeas corpus (Ley 23.098) | Arts. 405 a 420 CPP PBA | Ley 23.098 es referencia federal. |

## Cómo se relacionan

- **Partes comunes** en `datos/comun.py`: valores de la app, `flujo()`, recursos penales, bloque de libertad, fases/grupos base, leyenda, dudas transversales y de producto.
- **Dudas transversales y de producto** se responden una sola vez en la matriz de investigación. Las otras tres tienen una última duda que lo recuerda.
- **Derivaciones:** IPP → juicio oral / abreviado / hábeas / ejecución; juicio oral → abreviado / hábeas / ejecución; abreviado rechazado → IPP o juicio oral, según la etapa; hábeas resuelto → vuelve a la causa principal; condena firme → ejecución penal (fuera de V1: Ley 12.256).
- **Caminos paralelos:** la situación de libertad, el plazo de la IPP, el plazo para el debate, los honorarios y la remisión de copias del hábeas corren en paralelo con el camino principal y terminan en "Fin de este camino". Las derivaciones a hábeas corpus salen de esos caminos paralelos sin cerrar la causa principal (duda de producto IPP D33).
- **Fuera de la V1:** fuero penal juvenil (Ley 13.634), delitos de acción privada y ejecución de la pena.

## Datos sensibles

Las causas penales tienen datos especialmente sensibles (detención, víctimas, testigos, menores, reserva de la investigación). **No escribas nombres, DNI, domicilios, números de causa o IPP ni relatos de hechos** en las planillas. Las dudas de producto sobre causa reservada, visibilidad en el estudio y avisos están en la matriz de investigación; no se modificaron `modelado_de_amenazas_v1.md` ni `legal/politica_de_privacidad.md`.

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=investigacion   # o juicio_oral, abreviado, habeas_corpus

$PY generar.py ../../penal/matriz_penal_${CASO}_pba.xlsx ../../penal/salida/tablas_${CASO}.md ../../penal/datos/${CASO}.py
$PY verificar_excel.py ../../penal/matriz_penal_${CASO}_pba.xlsx ../../penal/datos/${CASO}.py
$PY diagrama.py ../../penal/matriz_penal_${CASO}_pba.xlsx ../../penal/diagrama_penal_${CASO}_pba.md ../../penal/salida/diagrama_${CASO}.md ../../penal/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `datos/comun.py` | Valores permitidos, `flujo()`, recursos, libertad, leyenda, dudas transversales/producto. |
| `datos/investigacion.py`, `juicio_oral.py`, `abreviado.py`, `habeas_corpus.py` | Fuente de cada borrador. |
| `salida/` | Tablas Markdown y vista general; las generan los scripts. |
| `dudas_a_validar.md` | Las dudas de las cuatro planillas y las citas "(a verificar)", para trabajar con el abogado. |

**`generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py`.
