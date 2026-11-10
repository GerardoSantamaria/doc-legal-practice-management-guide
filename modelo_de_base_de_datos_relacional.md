# Modelo de Base de Datos Relacional - Asistente Legal (V1)

Este documento define la estructura de tablas para el motor de base de datos relacional (recomendado: PostgreSQL). El modelo se divide en tres dominios principales: **Catálogos del Sistema**, **Motor de Flujos** y **Datos del Usuario**.

## 1. Dominio: Catálogos del Sistema (Datos estáticos)

Estas tablas son administradas por los dueños de la app. Los usuarios solo las leen.

### Tabla: `jurisdictions` (jurisdicciones)

*Para la V1 solo tendrá un registro activo, pero prepara el sistema para escalar.*

* `id` (PK, UUID)

* `name` (nombre) (String) -> Ej: "Provincia de Buenos Aires", "CABA".

* `is_active` (activa) (Boolean) -> Ej: true/false.

### Tabla: `judicial_departments` (departamentos judiciales)

* `id` (PK, UUID)

* `jurisdiction_id` (jurisdicción_id) (FK -> jurisdictions.id)

* `name` (nombre) (String) -> Ej: "San Isidro", "Lomas de Zamora".

### Tabla: `courts` (tribunales)

* `id` (PK, UUID)

* `department_id` (departamento_id) (FK -> judicial_departments.id)

* `name` (nombre) (String) -> Ej: "Tribunal de Trabajo N° 1".

### Tabla: `holidays_calendar` (calendario de feriados)

* `id` (PK, UUID)

* `date` (fecha) (Date) -> Ej: "2024-07-15" (sin hora).

* `description` (descripción) (String) -> Ej: "Feria de Invierno", "Día del Empleado Judicial".

* `jurisdiction_id` (jurisdicción_id) (FK -> jurisdictions.id) -> Permite feriados específicos por provincia.

## 2. Dominio: Motor de Flujos (La "Receta" Procesal)

Estas tablas digitalizan la matriz de hoja de cálculo que armará tu abogado.

### Tabla: `flow_nodes` (nodos de flujo)

*Representa cada etapa individual del proceso legal.*

* `id` (PK, UUID)

* `step_code` (código de paso) (String) -> Ej: "LAB_050".

* `legal_branch` (fuero) (String) -> Ej: "Laboral".

* `responsible_role` (rol responsable) (Enum) -> "Actora", "Demandada", "Tribunal".

* `phase` (fase) (String) -> Ej: "Postulación".

* `name` (nombre) (String) -> Ej: "Contestación de Demanda".

* `trigger_event` (evento disparador) (String) -> Ej: "Recepción de cédula".

* `default_term_days` (plazo de días por defecto) (Integer) -> Ej: 10.

* `applies_grace_period` (aplica gracia) (Boolean) -> true/false.

* `checklist_json` (JSON) -> Arreglo de tareas a realizar y documentación.

### Tabla: `flow_transitions` (transiciones de flujo / bifurcaciones)

*Conecta un nodo con los posibles siguientes pasos según qué haya pasado.*

* `id` (PK, UUID)

* `source_node_id` (nodo_origen_id) (FK -> flow_nodes.id)

* `exit_condition` (condición de salida) (String) -> Ej: "Demandado contesta", "Demandado no contesta".

* `target_node_id` (nodo_destino_id) (FK -> flow_nodes.id)

## 3. Dominio: Datos del Usuario (Transaccional)

Aquí se guarda la información privada de cada abogado, sus clientes y expedientes.

### Tabla: `users` (usuarios / abogados)

* `id` (PK, UUID)

* `email` (String, Unique)

* `password_hash` (String)

* `full_name` (nombre completo) (String)

* `created_at` (fecha de creación) (Timestamp)

### Tabla: `clients` (clientes)

* `id` (PK, UUID)

* `user_id` (usuario_id) (FK -> users.id) -> Asegura que un abogado solo vea a SUS clientes.

* `full_name_or_company` (nombre o razón social) (String)

* `tax_id` (cuit_dni) (String)

* `phone` (teléfono) (String)

* `email` (String)

### Tabla: `legal_cases` (expedientes)

* `id` (PK, UUID)

* `user_id` (usuario_id) (FK -> users.id)

* `client_id` (cliente_id) (FK -> clients.id)

* `case_title` (carátula) (String) -> Ej: "PEREZ C/ EMPRESA S/ DESPIDO"

* `jurisdiction_id` (jurisdicción_id) (FK -> jurisdictions.id)

* `court_id` (tribunal_id) (FK -> courts.id)

* `represented_role` (rol representado) (Enum) -> "Actora", "Demandada"

* `current_status` (estado actual) (Enum) -> "Activo", "Pausado", "Terminado"

* `created_at` (fecha de creación) (Timestamp)

### Tabla: `case_steps` (pasos del expediente / línea de tiempo)

*Es la tabla más importante. Registra el progreso de un expediente específico sobre el flujo ideal.*

* `id` (PK, UUID)

* `case_id` (expediente_id) (FK -> legal_cases.id)

* `node_id` (nodo_id) (FK -> flow_nodes.id) -> Qué hito procesal es.

* `status` (estado) (Enum) -> "Pendiente", "Completado", "Salteado".

* `start_notification_date` (fecha notificación inicio) (Date, Nullable) -> El Día Cero que carga el abogado.

* `edited_term_days` (plazo días editado) (Integer) -> Copia el valor del nodo por defecto, pero el usuario puede editarlo (Ej: cambiar de 10 a 12).

* `extension_days` (días de prórroga) (Integer, Default: 0) -> Suma días si hay asuetos imprevistos (+1).

* `calculated_due_date` (fecha de vencimiento calculada) (DateTime, Nullable) -> Resultado del algoritmo.

* `calculated_grace_date` (fecha de gracia calculada) (DateTime, Nullable) -> Resultado del algoritmo.

* `completed_at` (fecha completado) (Timestamp, Nullable) -> Cuándo el abogado marcó este paso como terminado.

* `chosen_transition_id` (transición elegida_id) (FK -> flow_transitions.id, Nullable) -> Por qué camino avanzó.

## 4. Resumen de Relaciones Clave

1. **Multitenancy Básico:** Todo `Client` y todo `Legal_Case` tiene un `user_id`. Esto garantiza la seguridad y privacidad: en la base de datos conviven todos los juicios de todos los abogados, pero el código filtra siempre por el ID del usuario logueado.

2. **Separación Plantilla vs. Instancia:** Separamos la definición del proceso (`flow_nodes`) de la realidad del caso (`case_steps`). Si el año que viene cambia la ley y un plazo pasa de 10 a 15 días, editás `flow_nodes`, pero los juicios ya iniciados en el pasado (`case_steps`) no se rompen porque mantienen su registro histórico.