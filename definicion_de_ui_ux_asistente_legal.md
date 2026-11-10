# Definición de UI/UX - Asistente Legal (V1)

**Alcance:** Fuero Laboral (Provincia de Buenos Aires) | Roles: Actora y Demandada | Plataforma: Web/App Responsive.

## 1. Mapa de Navegación (Sitemap)

La aplicación tendrá una estructura plana y rápida, priorizando que el abogado vea sus urgencias a primera vista.

1. **Dashboard (Inicio)**: Centro de alertas in-app y listado de expedientes.
2. **Alta de Expediente**: Formulario de creación paso a paso.
3. **Ficha del Expediente (Vista de Flujo)**: Pantalla principal de trabajo con el mapa interactivo del proceso.
4. **Configuración de Calendario**: Panel simple para ver días inhábiles globales.

---

## 2. Detalle de Pantallas (Wireframes Funcionales)

### Pantalla 1: Dashboard (Inicio)
Es la pantalla de aterrizaje del abogado. Su objetivo es responder a la pregunta: *"¿Qué se me vence hoy y en qué tengo que trabajar?"*.

* **Header:** Buscador global (por nombre de cliente, carátula o juzgado) y menú de usuario.
* **Sección A: Centro de Alertas In-App (El Semáforo)**
    * *Tarjetas Rojas:* Vencimientos de HOY y plazos de gracia (primeras 4 horas de mañana).
    * *Tarjetas Amarillas:* Vencimientos en los próximos 2 a 3 días hábiles.
    * *Acción:* Al hacer clic en una alerta, lleva directamente al nodo correspondiente en la Ficha del Expediente.
* **Sección B: Mis Expedientes Activos**
    * Tabla o lista de tarjetas ordenadas por fecha de última actividad o vencimiento más próximo.
    * *Columnas/Datos:* Carátula, Cliente, Rol, Estado Actual, Próximo Vencimiento.

### Pantalla 2: Alta de Expediente
Un formulario dividido en dos bloques rápidos.

* **Bloque 1: Datos del Cliente**
    * Nombre/Razón Social, DNI/CUIT, Teléfono, Email.
* **Bloque 2: Datos del Proceso**
    * Carátula (Ej: *PEREZ C/ EMPRESA S.A. S/ DESPIDO*).
    * **Jurisdicción:** Dropdown (Opciones: *PBA* / *CABA [Próximamente]* / *Federal [Próximamente]*). Para la V1, PBA viene seleccionada por defecto.
    * **Departamento Judicial (Solo PBA):** Selector (Ej: *San Isidro, Morón, La Plata, Lomas de Zamora*).
    * **Juzgado/Tribunal:** Selector dependiente del Departamento Judicial (Ej: *Tribunal de Trabajo N° 1*).
    * **Rol a representar:** Dropdown (*Actora* / *Demandada*). Define qué diagrama de flujo se carga.

### Pantalla 3: Ficha del Expediente (El Motor de la App)
Esta es la vista core del producto. 

* **Cabecera (Fija):**
    * Carátula, Cliente, Juzgado.
    * Menú de opciones: "Editar datos", "Eliminar caso".
* **Columna Izquierda / Superior: El Mapa de Flujo (Roadmap visual)**
    * Diagrama de línea de tiempo con los "Hitos" procesales.
    * *Estado visual:* Gris (Futuro), Verde (Completado), **Azul/Resaltado (Actual)**.
* **Columna Derecha / Inferior: Panel de Acción del Hito Actual**
    * **Título del Hito:** Ej. *"Contestación de Demanda"*.
    * **Checklist del Abogado:** Tareas y documentación.
    * **Calculadora de Plazos (El módulo más crítico):**
        * *Input Fecha Notificación:* Calendario para elegir el "evento disparador".
        * *Días Hábiles (Editable):* Muestra el plazo legal (ej. `10 días`), permite editar el número.
        * *Resultado Automático:* Texto destacado *"Vence el DD/MM/AAAA a las 23:59hs"*.
        * *Aviso de Gracia:* Texto *"Plazo de gracia hasta el DD/MM/AAAA a las 12:00hs"*.
        * *Botón de Emergencia:* **"+1 Día Hábil (Prorrogar por asueto/falla en sistema)"**.
    * **Botones de Navegación del Flujo:**
        * Botón Principal: **"Avanzar de Etapa"**. (Despliega selector si hay bifurcaciones).
        * Menú Secundario: **"Saltear etapa manualmente"**.

### Pantalla 4: Configuración y Calendario Global
* **Vista de Calendario:** Mensual.
* **Feriados del Sistema:** Muestra en gris oscuro los feriados y ferias precargados.
* **Agregar Inhábil Manual:** Botón para marcar un día específico como inhábil a nivel global de la cuenta del abogado.

---

## 3. Comportamientos Clave de la UI

1. **Flexibilidad de Edición:** Si el abogado sobrescribe los días de plazo, aparece un icono de "modificado manualmente".
2. **Prevención de Errores:** Confirmación (pop-up) antes de usar *"Saltear etapa manualmente"*.
3. **Vacíos de Tiempo:** Cuando una etapa depende del tribunal (valor 0 días), el cronómetro no corre; muestra estado de "Esperando resolución".