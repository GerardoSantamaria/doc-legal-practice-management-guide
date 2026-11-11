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

