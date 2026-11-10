# Documentación de Proyecto: Asistente Legal y Gestor de Procesos (V1)

## 1. Visión General

Aplicación diseñada para abogados en Argentina que funciona como un asistente inteligente. Su objetivo dual es:

1. **Gestión de Cartera:** Mostrar el estado actual de cada cliente y su proceso legal activo.

2. **Motor de Guía y Plazos:** Basado en diagramas de flujo pre-cargados por fuero, guía al abogado paso a paso, calculando los vencimientos legales y recordando las tareas críticas (con foco en el plazo de gracia).

## 2. Alcance de la Versión 1 (MVP)

Para garantizar el lanzamiento ágil y controlar costos, la V1 tendrá el siguiente alcance definido:

* **Fueros y Jurisdicciones:** Únicamente **Fuero Laboral de la Provincia de Buenos Aires (PBA)**. (CABA y otros fueros quedan para V2+).

* **Ingreso de Datos:** 100% manual por parte del abogado/asistente.

* **Integraciones Externas:** **EXCLUIDAS**. No habrá conexión automática con la MEV (Mesa de Entradas Virtual) ni con el portal de Notificaciones Electrónicas de la SCBA en esta fase.

* **Notificaciones:** El sistema generará alertas exclusivamente dentro de la aplicación.

* **Motor de Calendario:** Debe incluir lógica de días hábiles judiciales PBA, ferias judiciales (enero/julio) y feriados nacionales precargados.

## 3. Definiciones Funcionales Acordadas (V1)

El desarrollo del MVP se guiará por las siguientes definiciones de producto:

### A. Perspectiva y Roles
* **Múltiples Roles:** La app permitirá elegir al inicio del proceso si el abogado representa a la **Parte Actora** o a la **Parte Demandada**. El sistema adaptará quién tiene la responsabilidad del plazo perentorio en cada hito según el rol seleccionado.

### B. Mecánica de Cálculo y Sobrescritura
* **Cálculo Automático Híbrido:** El abogado ingresa la fecha del evento disparador (ej. día de notificación) y el sistema suma automáticamente los días hábiles judiciales correspondientes.
* **Sobrescritura Manual (Override):** Aunque el sistema sugiera el plazo legal por defecto (ej. 10 días), **el campo de cantidad de días será editable**. Si el tribunal fijó un plazo atípico (ej. 12 días hábiles), el abogado podrá modificar este valor antes de iniciar la cuenta regresiva.

### C. Calendario Judicial y Contingencias
* **Base Centralizada:** El backend de la app contendrá los feriados y ferias inamovibles.
* **Botón de Prórroga por Asueto:** Ante un asueto imprevisto de la SCBA, paro judicial local o caída del portal, el usuario tendrá un botón dentro del caso procesal para **"Prorrogar plazo (+1 día hábil)"**. Esto recalculará inmediatamente la fecha fatal sin necesidad de que el sistema central se entere del asueto local.

### D. Flexibilidad del Flujo (Roadmap)
* **Navegación Flexible:** La app guiará paso a paso proponiendo el camino lógico siguiente según la matriz, pero siempre existirá la opción de **"Cambiar de etapa manualmente"** (saltar pasos o retroceder). El flujo sugerido no será una camisa de fuerza.

### E. Sistema de Alertas (V1)
* **In-App Exclusivo:** En esta primera versión, todas las alertas (vencimientos del día, plazo de gracia, próximos a vencer) se visualizarán **únicamente dentro de la aplicación** (mediante un panel de control o *dashboard* y listados con indicadores visuales). El envío de correos electrónicos consolidados queda relegado para la V2.

## 4. Matriz de Flujos Procesales (Entregable del Abogado)

El abogado responsable del área legal debe completar una hoja de cálculo con la siguiente estructura exacta. Cada fila representa un "nodo" o un camino posible en el juicio.

### Bloque 1: Identificación y Estado

* **`ID_Paso`**: Código único alfanumérico (ej: `LAB_010`). Usar saltos de 10 en 10.

* **`Fase_Proceso`**: Etapa macro (Previa, Postulación, Prueba, etc.).

* **`Nombre_Hito`**: Título corto de la acción o estado actual.

* **`Rol_Responsable`**: Quién debe actuar (Actora, Demandada, Tribunal).

### Bloque 2: Reglas de Cómputo del Plazo

* **`Evento_Disparador`**: Hecho exacto que inicia el reloj judicial.

* **`Plazo_Valor_Default`**: Número entero de días predeterminado por ley (0 si no tiene plazo perentorio). Este es el valor que la app sugerirá pero que el abogado podrá editar.

* **`Plazo_Tipo`**: Hábiles judiciales o Corridos.

* **`Aplica_Gracia`**: SÍ/NO (Habilita las 4 primeras horas del día posterior - Art. 124 CPCCBA).

* **`Base_Normativa`**: Ley y artículo.

### Bloque 3: Flujo y Lógica de Bifurcación

* **`Condicion_Salida`**: Qué evento define el camino a seguir.

* **`Paso_Siguiente_ID`**: El ID al que salta el sistema según la condición. *(Nota: Si un hito tiene 3 salidas posibles, debe ocupar 3 filas en la planilla con el mismo ID pero distinto Paso Siguiente).*

### Bloque 4: Asistente / Guía

* **`Checklist_Abogado`**: Qué tareas debe realizar el profesional en este hito.

* **`Documentacion_Requerida`**: Escritos, bonos, tasas o adjuntos obligatorios.

## 5. Ejemplo de Carga: Fuero Laboral PBA (Ley 11.653 / 15.057)

| ID_Paso | Fase_Proceso | Nombre_Hito | Rol_Responsable | Evento_Disparador | Plazo_Valor_Default | Plazo_Tipo | Aplica_Gracia | Base_Normativa | Condicion_Salida | Paso_Siguiente_ID | Checklist_Abogado | Documentacion_Requerida | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| **LAB_010** | Previa | Intercambio Telegráfico | Actora | Despido o injuria | 0 | N/A | LCT | Intimación rechazada | **LAB_020** | Enviar TCL intimando aclaración o pago. | Copia de TCL y avisos de entrega. |  | 
| **LAB_030** | Postulación | Inicio de Demanda | Actora | Fracaso de conciliación | 0 | N/A | Art. 256 LCT | Demanda interpuesta | **LAB_040** | Redactar objeto, hechos, liquidación, prueba. | Bono Ley 8480, Ius previsional, documental PDF. |  | 
| **LAB_050-A** | Postulación | Contestación Demanda | Demandada | Recepción de cédula | 10 | Hábiles judic. | SÍ | Art. 29 L.11653 | Contesta y niega | **LAB_060** | Contestar, oponer defensas, ofrecer prueba. | Poder, Ius, Bono, documental. | 
| **LAB_050-B** | Postulación | Contestación Demanda | Demandada | Recepción de cédula | 10 | Hábiles judic. | SÍ | Art. 29 L.11653 | No contesta | **LAB_070** | Pedir acusación de rebeldía. | Escrito pidiendo rebeldía. | 
| **LAB_050-C** | Postulación | Contestación Demanda | Demandada | Recepción de cédula | 10 | Hábiles judic. | SÍ | Art. 31 L.11653 | Opone excepciones previas | **LAB_080** | Contestar traslado de excepciones. | Escrito contestando excepciones. | 

## 6. Instrucciones para el Equipo Legal

1. **Bifurcaciones:** Respetar la regla de multiplicar las filas si un paso tiene más de un resultado posible (ver ejemplo `LAB_050-A, B y C`).

2. **Día Cero:** Considerar que el sistema calculará que los plazos comienzan a correr a partir del día hábil siguiente a la notificación (según normativa procesal bonaerense).

3. **Casos sin plazo:** Usar `0` para etapas que dependen de los tiempos del juzgado (ej. dictado de un proveído simple).