# Matrices de Derecho Comercial por tipo de proceso

Tres matrices de Derecho Comercial del fuero Civil y Comercial de la Provincia de Buenos Aires, una por tipo de proceso, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado**. Las citas son orientativas: las marcadas "a verificar" no se usan hasta que el abogado las confirme.

| Tipo de proceso | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Concursos y quiebras | `matriz_comercial_concursos_pba.xlsx` | `diagrama_comercial_concursos_pba.md` | 69 | 131 | 31 |
| Juicios ejecutivos y cobro de pesos | `matriz_comercial_ejecutivos_pba.xlsx` | `diagrama_comercial_ejecutivos_pba.md` | 47 | 91 | 18 |
| Conflictos societarios | `matriz_comercial_societarios_pba.xlsx` | `diagrama_comercial_societarios_pba.md` | 44 | 91 | 19 |

## Qué cubre cada una

**Concursos y quiebras** (prefijo `CYQ`). Etapa previa con la elección de la vía. Concurso preventivo: presentación, ratificación, apertura, edictos, libros, síndico, pronto pago laboral, suspensión de juicios y fuero de atracción, contratos en curso, verificación (pedidos, observaciones, informe individual, resolución del art. 36, revisión y verificación tardía), categorización, informe general, exclusividad, propuesta, audiencia informativa, conformidades, impugnación, homologación, honorarios, cumplimiento, nulidad, incumplimiento y salvataje del art. 48. Acuerdo preventivo extrajudicial. Quiebra pedida, propia o indirecta: citación al deudor, sentencia, entrega de libros, edictos, reposición, conversión, incautación, inhabilitación, continuación y cooperativa, fecha de cesación de pagos, ineficacia, extensión, responsabilidad, realización, informe final, distribución, dividendo, clausura y conclusión (avenimiento, pago total o carta de pago). La verificación y el informe general son los mismos hitos para el concurso y la quiebra.

**Juicios ejecutivos y cobro de pesos** (prefijo `EJE`). Cheque, echeq y cheque de pago diferido (aviso del rechazo), pagaré (protesto), tarjeta de crédito (preparación de la vía, Ley 25.065), factura de crédito electrónica (Ley 27.440) y crédito sin título ejecutivo por cobro de pesos en juicio sumario. Prescripción, intimación, mediación optativa u obligatoria, embargo preventivo, reconocimiento de firma y caducidad de las preparatorias, mandamiento, excepciones, prueba, sentencia de remate, apelación con o sin fianza, y el bloque común de embargo, subasta, liquidación y pago. Si el deudor se concursa, sigue en la matriz de concursos.

**Conflictos societarios** (prefijo `SOC`). Derecho de información, convocatoria a asamblea (por la sociedad, la DPPJ o el juez), impugnación de decisiones con suspensión preventiva (arts. 251 y 252 LGS), exclusión de socios con suspensión provisoria (arts. 91 a 93), acción social e individual de responsabilidad, remoción de administradores con intervención judicial (arts. 113 a 117), inscripción de la sentencia en la DPPJ, y disolución y liquidación (arts. 94 a 112). Si la condena no se paga, sigue en la matriz de ejecutivos; si la sociedad se concursa, en la de concursos.

## Cómo se relacionan entre sí

- **Ejecutivos y societarios comparten la etapa contenciosa del CPCCBA** (demanda, contestación, prueba, sentencia, recursos, liquidación, acuerdo, caducidad, honorarios y archivo, hitos `_300` a `_990`), por el trámite sumario. La arma `datos/comun.py` cambiando el prefijo. Ejecutivos agrega el bloque común de embargo y subasta (`_800` a `_880`). Concursos tiene su propio trámite de la Ley 24.522 y no los usa.
- **Las dudas transversales y de producto se responden una sola vez**, en la matriz de concursos: vigencia, tasa de justicia, honorarios y aportes, ferias, plazo de gracia, notificaciones, tasa de interés, roles, rol representado, cronograma del juez, incidentes, vinculación de expedientes y catálogos. **Las dudas de la etapa contenciosa común** se responden en la matriz de societarios. Ejecutivos y societarios tienen una duda que lo recuerda.
- **Las reglas del motor** se validan en las dudas D26 a D34 de `matriz_flujo_laboral_pba_ley_11653.xlsx` y valen también acá.
- **Los hitos "Sigue en la matriz de ..."** son finales: el expediente continúa en otra matriz y hay que vincular los dos expedientes en la app.

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos; sin ese argumento siguen generando la matriz general.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=concursos   # o ejecutivos, o societarios

$PY generar.py ../../comercial/matriz_comercial_${CASO}_pba.xlsx ../../comercial/salida/tablas_${CASO}.md ../../comercial/datos/${CASO}.py
$PY verificar_excel.py ../../comercial/matriz_comercial_${CASO}_pba.xlsx ../../comercial/datos/${CASO}.py
$PY diagrama.py ../../comercial/matriz_comercial_${CASO}_pba.xlsx ../../comercial/diagrama_comercial_${CASO}_pba.md ../../comercial/salida/diagrama_${CASO}.md ../../comercial/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `datos/comun.py` | Lo que comparten las tres: valores permitidos, fases y grupos del diagrama, datos de la hoja `Flujo`, la etapa contenciosa del CPCCBA, el bloque de ejecución y subasta, y la duda que remite a las dudas transversales. |
| `datos/concursos.py`, `datos/ejecutivos.py`, `datos/societarios.py` | Hitos, transiciones y dudas de cada tipo de proceso. Son la fuente del borrador. |
| `dudas_a_validar.md` | Las dudas de las tres planillas ordenadas por bloque, las citas marcadas "(a verificar)" y las decisiones de modelado a confirmar, para trabajar con el abogado. |
| `salida/` | Tablas en Markdown y vista general de cada diagrama. Las generan los scripts; no se editan a mano. |

**Igual que con la matriz general, `generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py` y `generar.py` no se vuelve a correr sobre esa planilla.
