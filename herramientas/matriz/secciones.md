## 4. Matriz de Flujos Procesales (Entregable del Abogado)

El equipo legal completa una planilla por régimen procesal. Para el fuero laboral de PBA bajo la Ley 11.653, el archivo es `matriz_flujo_laboral_pba_ley_11653.xlsx`. El back-office la importa, la valida y la publica como una **versión del flujo**: una vez publicada no se modifica, y cada expediente queda atado a la versión con la que se creó (ver el dominio Motor de Flujos en el modelo de datos).

### Hojas de la planilla

| Hoja | Contenido | Se importa a |
| ----- | ----- | ----- |
| `Instrucciones` | Reglas de carga | No se importa |
| `Flujo` | Régimen, versión, quién validó y cuándo | `flows`, `flow_versions` |
| `Nodos` | Un hito por fila | `flow_nodes`, `flow_node_checklist_items` |
| `Transiciones` | Un camino posible por fila | `flow_transitions` |
| `Dudas_a_validar` | Preguntas abiertas para el equipo legal | No se importa |
| `Valores` | Listas de valores permitidos (desplegables) | No se importa |

### Hoja `Nodos`

#### Bloque 1: Identificación y Estado

* **`ID_Paso`**: Código único alfanumérico (ej: `LAB_050`). Usar saltos de 10 en 10, para poder intercalar hitos sin renumerar (ej: `LAB_015`).
* **`Fase_Proceso`**: Etapa macro. Valores: `Previa`, `Postulación`, `Prueba`, `Vista de causa`, `Sentencia`, `Recursos`, `Ejecución`, `Acuerdo`, `Cierre`.
* **`Nombre_Hito`**: Título corto de la acción o estado actual.
* **`Rol_Responsable`**: Quién debe actuar.
  * `ACTORA`: la parte actora.
  * `DEMANDADA`: la parte demandada.
  * `TRIBUNAL`: depende del tribunal; la app muestra "Esperando resolución".
  * `AMBAS`: puede o debe actuar cualquiera de las partes (recursos, impugnaciones, audiencias).
* **`Es_Inicial`** / **`Es_Final`**: `SI` / `NO`. Hay un solo nodo inicial. Los nodos finales no tienen transiciones de salida.

#### Bloque 2: Reglas de Cómputo del Plazo

* **`Evento_Disparador`**: Hecho exacto que inicia el reloj (el Día Cero).
* **`Plazo_Valor_Default`**: Número entero predeterminado por ley, en la unidad del tipo (días, horas, meses o años). Es el valor que la app sugiere y que el abogado puede editar en cada expediente.
* **`Plazo_Tipo`** (el cómputo de cada uno está en la sección 2 del documento de lógica de plazos):

  | Valor | Significado | Gracia |
  | ----- | ----- | ----- |
  | `HABILES_JUDICIALES` | Días hábiles según el calendario judicial PBA | Admite |
  | `CORRIDOS` | Días corridos | Admite |
  | `HABILES_ADMINISTRATIVOS` | Días hábiles de la LCT y la etapa prejudicial: lunes a viernes sin feriados; las ferias judiciales no suspenden | No |
  | `MESES` | Meses, de fecha a fecha | Admite |
  | `ANIOS` | Años, de fecha a fecha (prescripción) | Admite |
  | `HORAS` | Horas corridas desde la fecha y hora del disparador (intimaciones en horas) | No |
  | `FECHA_FIJADA` | Acto con fecha y hora fijadas, como una audiencia (valor `0`); el abogado carga la fecha y la hora | No |
  | `ANTICIPACION_HABILES_JUDICIALES` | Días hábiles contados hacia atrás desde un acto fijado (ej. citar testigos antes de la audiencia) | No |
  | `SIN_PLAZO` | Sin plazo perentorio (valor `0`); depende del tribunal o de la parte | No |

* **`Aplica_Gracia`**: `SI` / `NO`. Habilita las 4 primeras horas del día hábil posterior (art. 124 CPCCBA). Solo puede ser `SI` en los tipos que la admiten.
* **`Base_Normativa`**: Ley y artículo.

#### Bloque 4: Asistente / Guía

* **`Checklist_Abogado`**: Tareas que el profesional debe realizar en este hito. Cada ítem va separado por punto y coma (`;`) y se convierte en una tarea tildable en el expediente.
* **`Documentacion_Requerida`**: Escritos, bonos, tasas o adjuntos obligatorios, con el mismo separador.

#### Columnas de trabajo (no se importan)

* **`Estado_Validacion`**: `PENDIENTE`, `VALIDADO` o `CORREGIR`.
* **`Comentarios_Equipo_Legal`**: observaciones libres.
* **`Control`**: fórmula que marca en rojo los errores de carga (ID duplicado, hito sin salidas o sin entradas, plazo incoherente con su tipo).

### Hoja `Transiciones` (Bloque 3: Flujo y Lógica de Bifurcación)

* **`ID_Paso_Origen`**: hito desde el que se sale.
* **`Condicion_Salida`**: qué evento define el camino a seguir. La app lo muestra como opción al presionar "Avanzar de etapa".
* **`ID_Paso_Destino`**: el hito al que se salta, o `CIERRA_CAMINO` (ver abajo). Nunca queda vacío.
* **`Orden`**: orden en que se muestran las opciones.

Reglas:

1. **Bifurcación:** si un hito tiene 3 salidas posibles, ocupa 3 filas con el mismo origen y distinta condición. Reemplaza a la regla anterior de repetir el hito con sufijos (`LAB_050-A`, `-B`, `-C`).
2. **Caminos en paralelo:** si la misma condición aparece en varias filas con distinto destino, al elegirla se abren **todos** esos hitos a la vez. Así se representan los plazos simultáneos; por ejemplo, la prescripción corre mientras avanza el reclamo.
3. **`CIERRA_CAMINO`:** la fila termina ese camino paralelo sin abrir otro hito (en la base de datos, `target_node_id` queda vacío).

**Relación con el rol representado (decidido, E13 del análisis):** hay un único flujo para ambos roles. `Rol_Responsable` indica quién debe actuar en cada hito, y la app lo cruza con el rol que el abogado representa en el expediente:

* **Te toca a vos:** el hito es de tu parte, o de `AMBAS`. Tiene alerta y semáforo.
* **Le toca a la contraparte:** se muestra para seguimiento, sin alerta. Cuando vence, la app avisa la oportunidad; por ejemplo, pedir que se tenga por no contestada la demanda.
* **Espera al tribunal:** se muestra como "Esperando resolución".

### Validaciones del importador

El back-office rechaza la planilla si no se cumple alguna de estas reglas:

* `ID_Paso` único y un solo nodo con `Es_Inicial = SI`.
* Todo origen y todo destino de `Transiciones` existe en `Nodos`, y ningún destino está vacío.
* Todo nodo no final tiene al menos una salida; ningún nodo final tiene salidas.
* Todos los nodos son alcanzables desde el nodo inicial.
* `SIN_PLAZO` y `FECHA_FIJADA` llevan plazo `0`; los demás tipos llevan un plazo mayor que `0`.
* `Aplica_Gracia = SI` solo en `HABILES_JUDICIALES`, `CORRIDOS`, `MESES` y `ANIOS`.
* Todos los valores están dentro de las listas permitidas.

Además, **no se publica** una versión que tenga filas en `PENDIENTE` o `CORREGIR`, o sin el campo "Validado por" de la hoja `Flujo`.

## 5. Ejemplo de Carga: Proceso Laboral Ordinario PBA (Ley 11.653)

Este ejemplo recorre un juicio laboral bonaerense ante un Tribunal de Trabajo de instancia única, completo, en 38 hitos y 76 transiciones:

* intercambio telegráfico, con la prescripción y la entrega de certificados en paralelo;
* conciliación previa;
* demanda, contestación y reconvención;
* prueba pericial e informativa;
* audiencia de vista de causa;
* veredicto y sentencia;
* recursos ante la SCBA;
* liquidación, ejecución y cobro;
* acuerdo conciliatorio, al que se puede llegar desde varias etapas.

> **Estado: borrador para validar.** Todas las filas están en `PENDIENTE`. Las citas normativas son orientativas y deben validarse artículo por artículo. Las 36 preguntas abiertas están en la sección 5.4 y en la hoja `Dudas_a_validar`; las D26 a D34 son las reglas R1 a R9 del motor de plazos. Si en algún departamento rige la Ley 15.057, se arma una matriz separada para ese régimen. El contenido es idéntico al de la planilla, que es la fuente de trabajo.

### 5.1 Mapa del flujo

Vista general por fases. El diagrama hito por hito, con colores por responsable, caminos en paralelo y condiciones en cada flecha, está en [`diagrama_flujo_laboral_pba_ley_11653.md`](diagrama_flujo_laboral_pba_ley_11653.md). Ambos se generan desde la planilla con `herramientas/matriz/diagrama.py`.

{{DIAGRAMA}}

### 5.2 Hitos (hoja `Nodos`)

{{NODOS}}

### 5.3 Transiciones (hoja `Transiciones`)

{{TRANSICIONES}}

### 5.4 Dudas a validar con el equipo legal

{{DUDAS}}

## 6. Instrucciones para el Equipo Legal

1. **Bifurcaciones:** cada salida posible de un hito es una fila en `Transiciones`, con el mismo origen y distinta condición (ver `LAB_070`, con tres salidas).
2. **Plazos en paralelo:** repetir la misma condición en varias filas para abrir varios hitos a la vez (ver `LAB_010` y `LAB_100`). Cerrar cada camino paralelo con `CIERRA_CAMINO`.
3. **Día Cero:** el sistema calcula que los plazos comienzan a correr a partir del día hábil siguiente al `Evento_Disparador` (según normativa procesal bonaerense).
4. **Casos sin plazo:** usar `SIN_PLAZO` con valor `0` y gracia `NO` para etapas que dependen de los tiempos del juzgado (ej. dictado de un proveído simple).
5. **Audiencias:** usar `FECHA_FIJADA` con valor `0`; el abogado carga la fecha y hora en cada expediente. Lo que haya que hacer antes de la audiencia (ej. citar testigos) va en un hito con `ANTICIPACION_HABILES_JUDICIALES`.
6. **Checklist y documentación:** separar cada ítem con punto y coma (`;`).
7. **Validación:** revisar cada fila y marcar `Estado_Validacion`. Responder las preguntas de `Dudas_a_validar`. Al terminar, completar "Validado por" y la fecha en la hoja `Flujo`.
8. **Controles:** antes de entregar la planilla, corregir toda celda en rojo de las columnas `Control`.
9. **Un archivo por régimen:** no mezclar hitos de la Ley 11.653 y de la Ley 15.057 en la misma planilla.
