# Matrices de Derecho Público y Constitucional

Cuatro matrices de Derecho Público y Constitucional para abogados de la Provincia de Buenos Aires, una por tipo de proceso, cada una con su diagrama. Tienen el mismo formato que `matriz_flujo_laboral_pba_ley_11653.xlsx` (hojas `Instrucciones`, `Flujo`, `Nodos`, `Transiciones`, `Dudas_a_validar` y `Valores`), así que el back-office las importa igual.

Son **borradores para validar con el abogado** (versión 1, 13/11/2026). Las citas se cotejaron con normas.gba.gob.ar, argentina.gob.ar, hcdn.gob.ar y leyes-ar.com; las marcadas "a verificar" no se usan hasta que el abogado las confirme, y cada una tiene su duda.

| Tipo de proceso | Planilla | Diagrama | Hitos | Transiciones | Dudas |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Contencioso administrativo | `matriz_publico_contencioso_pba.xlsx` | `diagrama_publico_contencioso_pba.md` | 64 | 137 | 34 |
| Seguridad social | `matriz_publico_seguridad_social_pba.xlsx` | `diagrama_publico_seguridad_social_pba.md` | 42 | 76 | 14 |
| Amparo | `matriz_publico_amparo_pba.xlsx` | `diagrama_publico_amparo_pba.md` | 42 | 90 | 16 |
| Hábeas data | `matriz_publico_habeas_data_pba.xlsx` | `diagrama_publico_habeas_data_pba.md` | 31 | 69 | 13 |

Las 34 dudas de contencioso incluyen las 10 transversales y las 8 de producto de toda la carpeta. Las otras matrices tienen solo sus dudas propias más una última que remite a contencioso.

## Qué cubre cada una

**Contencioso administrativo** (prefijo `CAD`). Proceso contra la Provincia, los municipios y los entes provinciales (Ley 12.008, con el CPCCBA supletorio). Cubre:

- **Vía administrativa** del Decreto-Ley 7647/70 (municipios: Ordenanza General 267/80): obligatoriedad y excepciones del art. 14, reclamo, revocatoria, jerárquico, pronto despacho, silencio y vista de las actuaciones.
- **Variantes:** empleo público (reclamo y sanciones), tributario (determinación de ARBA o tasa municipal, Tribunal Fiscal de Apelación, pago previo y repetición), licitaciones y responsabilidad del Estado.
- **Proceso:** amparo por mora (art. 76), caducidad de 90 días (art. 18), proceso sumario de ilegitimidad, demanda con notificación a la Fiscalía de Estado, excepciones, contestación, prueba, alegatos y sentencia.
- **Cautelares** contra el Estado, con el pedido previo de suspensión del art. 25.
- **Recursos y cierre:** apelación ante la Cámara en lo Contencioso Administrativo, SCBA y recurso extraordinario federal, ejecución contra el Estado (arts. 63 a 66), acuerdo, caducidad de instancia y honorarios.

El Estado nacional no tiene camino propio: su salida remite al cuadro de equivalencias de más abajo.

**Seguridad social** (prefijo `SSO`). Camino principal en la Nación (ANSES y justicia federal). Cubre:

- **Previa:** reajuste del haber inicial y de la movilidad, reconocimiento de servicios, denegatoria de beneficios y retenciones; documentación, prescripción de las mensualidades y acuerdo de Reparación Histórica (Ley 27.260).
- **Vía ANSES:** reclamo, plazo para resolver, pronto despacho, silencio y amparo por mora (art. 28 Ley 19.549).
- **Proceso:** caducidad para demandar, demanda de conocimiento pleno (art. 15 Ley 24.463, sin recurso administrativo previo), contestación, pericia contable e impugnación, alegatos y sentencia.
- **Recursos:** apelación ante la Cámara Federal del distrito o la de la Seguridad Social (fallo "Pedraza") y recurso extraordinario federal.
- **Cautelares y ejecución:** cautelares contra ANSES y ejecución en 120 días hábiles (art. 22).
- **Variante provincial:** el reclamo ante el IPS o una caja profesional, que sigue en contencioso administrativo.

**Amparo** (prefijo `AMP`). Camino principal en la Provincia (Ley 13.928, art. 20 inc. 2 Constitución PBA), con variante federal (art. 43 Constitución Nacional, Ley 16.986). Cubre:

- **Amparo de salud:** pedido de cobertura con prescripción médica, historia clínica y certificado de discapacidad; carta documento; negativa o silencio; medida autosatisfactiva; cautelar con caución juratoria.
- **Otros amparos** contra el Estado y contra particulares, y el amparo colectivo (Registro Público de Amparos de Incidencia Colectiva de la SCBA).
- **Proceso:** competencia según el demandado, admisibilidad y rechazo in limine, contestación o informe, audiencia, prueba y sentencia.
- **Recursos y cumplimiento:** apelación con su efecto, queja o recurso directo, recursos extraordinarios, y cumplimiento con astreintes (art. 804 CCyC) y ejecución contra el Estado provincial.

**Hábeas data** (prefijo `HDA`). Proceso provincial (Ley 14.214, art. 20 inc. 3 Constitución PBA) y federal (Ley 25.326). Cubre:

- **Objeto:** acceso, rectificación, actualización, confidencialidad y supresión.
- **Reclamo previo obligatorio** (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214) y denuncia ante la AAIP.
- **Datos crediticios:** plazo del art. 26 inc. 4 con la constancia de deuda cancelada y la Central de Deudores del BCRA.
- **Proceso:** demanda, admisión, anotación de litigiosidad o bloqueo provisional, informe, ampliación (federal), prueba, sentencia y apelación.
- **Cumplimiento** con astreintes y comunicación a la AAIP.

## Jurisdicciones

| Flujo | Camino principal | Variantes | Fuero |
| :--- | :--- | :--- | :--- |
| Contencioso administrativo | Provincia, municipios y entes provinciales (Ley 12.008; Decreto-Ley 7647/70) | Estado nacional: solo cuadro de equivalencias y duda | Contencioso Administrativo de PBA |
| Seguridad social | Nación: ANSES y justicia federal (Ley 24.463; CPCCN) | IPS (Decreto-Ley 9650/80) y cajas profesionales: derivan a contencioso | Juzgado federal con asiento en PBA o de la Seguridad Social de CABA |
| Amparo | Provincia (Ley 13.928; art. 20 inc. 2 Constitución PBA) | Nación: Ley 16.986; contra particulares, CPCCN | Según el demandado: provincial (IOMA, cajas, Provincia, municipios) o federal (obras sociales nacionales, Estado nacional; prepagas según el caso) |
| Hábeas data | Provincia (Ley 14.214; art. 20 inc. 3 Constitución PBA) | Nación: Ley 25.326 (bancos públicos nacionales o interconectados) | Civil y Comercial o Paz (privados), Contencioso Administrativo (públicos provinciales) o federal |

Los caminos federales se cargan con `Aplica_Gracia = NO` y con el calendario del expediente. El motor todavía no tiene calendario federal: ver la duda de producto prioritaria sobre la jurisdicción federal, en la matriz de contencioso.

## Contencioso contra el Estado nacional: equivalencias

La matriz de contencioso no modela el proceso contra el Estado nacional. Si el demandado es nacional, el caso sale por el hito `CAD_985` y estas equivalencias sirven de guía hasta que se decida si hace falta una matriz federal (duda de producto "Estado nacional en el contencioso").

| Instituto | Provincia de Buenos Aires (esta matriz) | Estado nacional (fuera de esta matriz) |
| :--- | :--- | :--- |
| Procedimiento administrativo | Decreto-Ley 7647/70 (municipios: Ordenanza General 267/80) | Ley 19.549 reformada por la Ley 27.742 y su reglamentación |
| Agotamiento de la vía | Obligatorio con excepciones (art. 14 Ley 12.008) | Obligatorio con excepciones (arts. 23, 24, 30 y 32 Ley 19.549) |
| Silencio | Pronto despacho y 30 días hábiles administrativos (art. 16 Ley 12.008; art. 79 Decreto-Ley 7647/70) | 60 días si no hay plazo especial (art. 10 Ley 19.549) |
| Recursos | Revocatoria 10 días, jerárquico 10 días (arts. 89 y 92 Decreto-Ley 7647/70) | Plazo no menor de 30 días (art. 23 Ley 19.549 reformada; reglamento a verificar) |
| Plazo para demandar | 90 días (art. 18 Ley 12.008) | 180 días hábiles judiciales (art. 25 Ley 19.549); recurso directo 30 días (art. 25 bis) |
| Reclamo previo | Según el caso (art. 14 Ley 12.008) | Obligatorio salvo excepciones; 90 días para resolver (arts. 30 y 31 Ley 19.549) |
| Amparo por mora | Art. 76 Ley 12.008 | Art. 28 Ley 19.549 (informe en el plazo que fije el juez) |
| Código procesal | Ley 12.008 y CPCCBA supletorio | CPCCN |
| Cautelares contra el Estado | Arts. 22 a 25 Ley 12.008 | Ley 26.854 (informe previo 5 días; vigencia hasta 6 meses) |
| Tribunal | Juzgado y Cámara en lo Contencioso Administrativo; SCBA | Juzgados federales; Cámara Contencioso Administrativo Federal; CSJN |
| Responsabilidad del Estado | Sin ley provincial ni adhesión a la Ley 26.944 (a verificar) | Ley 26.944 (prescripción de 3 años, art. 7) |

El cuadro también está en `datos/comun.py` (`CUADRO_EQUIVALENCIAS_NACION`); si se corrige, corregir los dos.

## Cómo se relacionan entre sí y con las demás matrices

- **Derivaciones:** un hito final cuyo nombre empieza con "Sigue en la matriz de ..." indica que el caso continúa en otra matriz de esta carpeta, en un expediente vinculado. Hay tres:
  - el amparo que no es la vía idónea o venció su plazo sigue en contencioso (`AMP_980`);
  - el contencioso con urgencia sigue en amparo (`CAD_980`);
  - el reclamo ante el IPS o una caja sigue en contencioso (`SSO_620`).
- **Bloques compartidos** en `datos/comun.py`:
  - el amparo provincial y el federal, que reutiliza hábeas data;
  - las cautelares contra el Estado (Ley 12.008, Ley 13.928, Ley 26.854);
  - los recursos (Cámara CA, SCBA, recurso extraordinario federal);
  - la ejecución contra el Estado provincial y contra ANSES;
  - los honorarios (Ley 14.967 y Ley 27.423).
- **Dudas transversales y de producto:** se responden una sola vez, en la matriz de contencioso. Son:
  - gracia por jurisdicción, calendario administrativo, horas del amparo federal, feria, tasas, honorarios y numeración de la Ley 12.008;
  - de producto: jurisdicción federal, PREJUDICIAL o judicial, roles y abogado del Estado, vinculación de expedientes, datos sensibles y catálogo de régimen.
- **Reglas del motor:** las reglas D26 a D34 de la matriz laboral valen acá. Cada apartamiento tiene su propia duda transversal: días hábiles administrativos con calendarios distintos, horas del amparo federal, gracia federal y feria habilitada.
- **Sin dependencias con otras carpetas:** no se importa nada de `civil/`, `laboral/`, `familia/`, `comercial/` ni `penal/`, y no se modificaron los scripts de `herramientas/matriz`.

## Datos sensibles

Estos expedientes pueden contener datos de salud (historia clínica, prescripción médica, certificado de discapacidad), datos previsionales (recibos de haberes, números de beneficio) y datos crediticios. **No escribas nombres, DNI, CUIL, números de beneficio, diagnósticos ni montos de un caso** en checklists, documentación, ejemplos ni dudas. Nombrá los documentos ("historia clínica", "recibo de haberes"), no su contenido. La duda de producto sobre datos sensibles relaciona esto con `modelado_de_amenazas_v1.md` y `legal/politica_de_privacidad.md`, que no se modificaron.

## Regenerar

Desde `herramientas/matriz`, con el entorno de `herramientas/README.md`. Cada script recibe como último argumento el módulo de datos.

```bash
cd herramientas/matriz
PY=../.venv/bin/python
CASO=contencioso   # o seguridad_social, amparo, habeas_data

$PY generar.py ../../publico/matriz_publico_${CASO}_pba.xlsx ../../publico/salida/tablas_${CASO}.md ../../publico/datos/${CASO}.py
$PY verificar_excel.py ../../publico/matriz_publico_${CASO}_pba.xlsx ../../publico/datos/${CASO}.py
$PY diagrama.py ../../publico/matriz_publico_${CASO}_pba.xlsx ../../publico/diagrama_publico_${CASO}_pba.md ../../publico/salida/diagrama_${CASO}.md ../../publico/datos/${CASO}.py
```

| Archivo | Para qué sirve |
| :--- | :--- |
| `datos/comun.py` | Lo que comparten las cuatro: valores permitidos, datos de la hoja `Flujo`, leyenda, bloques de amparo, cautelares, recursos, ejecución y honorarios, dudas transversales y de producto, y el cuadro de equivalencias. |
| `datos/contencioso.py`, `datos/seguridad_social.py`, `datos/amparo.py`, `datos/habeas_data.py` | Hitos, transiciones y dudas de cada tipo de proceso. Son la fuente del borrador. |
| `salida/` | Tablas en Markdown y vista general de cada diagrama. Las generan los scripts; no se editan a mano. |

**`generar.py` pisa la planilla.** Cuando el abogado empiece a completarla, la planilla pasa a ser la fuente: los diagramas se regeneran solo con `diagrama.py` y `generar.py` no se vuelve a correr sobre esa planilla.
