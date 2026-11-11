# Definición de UI/UX - Asistente Legal (V1)

**Alcance:** Fuero Laboral (Provincia de Buenos Aires) | Roles: Actora y Demandada | Plataforma: Web/App Responsive.

**Identidad visual:** el nombre (Foja), la paleta, la tipografía, los íconos, los colores de cada estado y el tono de los textos están en [`identidad_y_diseno_v1.md`](identidad_y_diseno_v1.md). Los colores que menciona este documento (rojo, amarillo, verde, azul, gris) se aplican con los valores de esa paleta, y siempre con ícono y texto.

**Diseño de pantallas:** las maquetas de cada pantalla, con rutas, roles, estados y operaciones de la API, están en [`diseno_de_pantallas_v1.md`](diseno_de_pantallas_v1.md). Este documento define qué hace cada pantalla; aquel, cómo se ve y se comporta.

## 1. Mapa de Navegación (Sitemap)

La aplicación tendrá una estructura plana y rápida, priorizando que el abogado vea sus urgencias a primera vista.

1. **Dashboard (Inicio)**: Centro de alertas in-app y listado de expedientes.
2. **Alta de Expediente**: Formulario de creación paso a paso.
3. **Ficha del Expediente (Vista de Flujo)**: Pantalla principal de trabajo con el mapa interactivo del proceso.
4. **Configuración de Calendario**: Panel simple para ver días inhábiles globales.
5. **Cuenta, plan y facturación**: Plan y tramo, clientes activos, usuarios, datos fiscales, facturas, dispositivos y baja.

**Onboarding (primer ingreso):** después del login con Google, el usuario acepta los Términos y Condiciones y la Política de Privacidad, con un enlace a cada texto. Quien crea el estudio es su titular y acepta, además, el Acuerdo de Encargo del Tratamiento en nombre del estudio. Si se publica una versión que pide nueva aceptación, se muestra al ingresar, con un resumen de qué cambió.

---

## 2. Detalle de Pantallas (Wireframes Funcionales)

### Pantalla 1: Dashboard (Inicio)
Es la pantalla de aterrizaje del abogado. Su objetivo es responder a la pregunta: *"¿Qué se me vence hoy y en qué tengo que trabajar?"*.

* **Header:** Buscador global (por nombre de cliente, carátula o juzgado) y menú de usuario.
* **Sección 0: Vencidos sin cumplir** (siempre arriba; no se puede ocultar mientras tenga elementos)
    * Una tarjeta por plazo propio vencido: *"No se cumplió: Contestación de la demanda. Expediente: PEREZ C/ EMPRESA S/ DESPIDO (Nº 1234). Cliente: Juan Pérez. Venció el mar 18/06 a las 14:00."*
    * Si todavía corre el plazo de gracia, la tarjeta dice *"Último momento: hasta hoy a las 12:00 (plazo de gracia)"* en lugar de "No se cumplió".
    * *Acciones:* "Lo cumplí" (pide la fecha y hora del cargo), "No se cumplió" (pide el motivo y, si el hito tiene una salida para ese caso, por ejemplo "No contesta en término", ofrece avanzar por ella) y "Corregir plazo" (abre la calculadora). La tarjeta no desaparece hasta que se elige una acción.
* **Sección A: Centro de Alertas In-App (El Semáforo)**
    * *Tarjetas Rojas:* Vencimientos de HOY, plazos de gracia (primeras 4 horas de mañana) y vencimientos dentro de los días hábiles configurados para el rojo.
    * *Tarjetas Amarillas:* Vencimientos dentro de los días hábiles configurados para el amarillo.
    * *Umbrales:* son parámetros de la base (`alert_settings`; por defecto, rojo hasta 2 días hábiles y amarillo hasta 5), con valores globales y un posible ajuste por estudio.
    * *Oportunidades:* plazos de la contraparte que vencieron, con la acción sugerida. Ej: *"Venció el plazo de la demandada para contestar: podés pedir que se tenga por no contestada la demanda."*
    * *Acción:* Al hacer clic en una alerta, lleva directamente al nodo correspondiente en la Ficha del Expediente.
    * Las alertas incluyen los plazos sueltos.
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
    * **Rol a representar:** Dropdown (*Actora* / *Demandada*). El flujo es uno solo; el rol define qué hitos son "te toca a vos" y cuáles son de la contraparte.
* **Bloque 3: ¿El expediente ya está en curso?** (*No* / *Sí*)
    * *No:* el expediente arranca en el hito inicial (etapa previa o demanda).
    * *Sí:*
        * se pide la fecha de interposición de la demanda;
        * se eligen uno o más hitos actuales en el mapa del flujo (puede haber caminos en paralelo);
        * para cada hito actual se carga el Día Cero. Si el abogado no lo conoce, puede cargar el vencimiento a mano con un motivo, y la app lo marca como *"Vencimiento cargado a mano, no calculado"*;
        * si algún plazo cargado ya venció, la app pregunta en el momento si se cumplió;
        * los hitos anteriores se muestran como *"Anteriores a la carga"*, sin fechas.
* **Límite de clientes del plan:** si el cliente elegido todavía no cuenta como activo y el estudio ya llegó al límite de su tramo, el botón de guardar se reemplaza por el mensaje *"Llegaste al límite de 10 clientes activos de tu plan. Tus expedientes cargados siguen funcionando normalmente. Para sumar este cliente, pasá al plan de hasta 30 clientes."*, con el botón "Cambiar de plan". Los datos cargados en el formulario no se pierden.

### Pantalla 3: Ficha del Expediente (El Motor de la App)
Esta es la vista core del producto. 

* **Cabecera (Fija):**
    * Carátula, Cliente, Juzgado.
    * Menú de opciones: "Editar datos", "Eliminar caso".
* **Columna Izquierda / Superior: El Mapa de Flujo (Roadmap visual)**
    * Diagrama de línea de tiempo con los "Hitos" procesales.
    * *Estado visual:* Gris (Futuro), Verde (Completado), **Azul/Resaltado (Actual)**, Rojo (Vencido), Tachado (No cumplido o anulado, visible en el historial).
    * Puede haber **varios hitos actuales a la vez** (caminos en paralelo, por ejemplo la prescripción y el reclamo). Cada uno tiene su propio panel de acción.
    * Cada hito indica de quién es: *"Te toca a vos"*, *"Le toca a la contraparte"* (seguimiento, sin alerta) o *"Esperando al tribunal"*.
* **Columna Derecha / Inferior: Panel de Acción del Hito Actual**
    * **Título del Hito:** Ej. *"Contestación de Demanda"*.
    * **Checklist del Abogado:** Tareas y documentación.
    * **Calculadora de Plazos (El módulo más crítico):**
        * *Inputs según el tipo de plazo:* fecha de notificación (Día Cero) para los plazos en días; fecha del hecho para meses y años; fecha y hora para los plazos en horas y las audiencias; para una anticipación, la audiencia de referencia, que la app toma del hito de la audiencia si ya está cargada.
        * *Valor del plazo (Editable):* Muestra el plazo legal (ej. `10 días hábiles`, `48 horas`, `2 años`) y permite editar el número, con motivo (ej. *"Ampliación por distancia"*).
        * *Resultado Automático:* Texto destacado con el límite ordinario, por ejemplo *"Vence el DD/MM/AAAA a las 14:00hs"*. La hora sale del tipo de límite del hito y del horario de la jurisdicción (cierre del horario judicial o fin del día); ver la sección 1 del documento de lógica de plazos.
        * *Aviso de Gracia:* Texto *"Si no llegás, tenés hasta el DD/MM/AAAA a las 12:00hs (plazo de gracia)"*.
        * *Plazo corrido trasladado:* si el vencimiento nominal cae en un día inhábil, se muestra ese día como fecha de alerta y se aclara *"Se puede presentar hasta el DD/MM/AAAA (día hábil siguiente)"*.
        * *Calendario provisorio:* mientras el calendario no sea oficial, cada vencimiento lleva la leyenda *"Cálculo aproximado: no considera feriados ni ferias"*.
        * *Calendario incompleto:* en plazos de meses o años que vencen después del calendario cargado, *"Vencimiento a confirmar cuando se cargue el calendario de ese año"*.
        * *Fecha fijada en inhábil:* si la audiencia cae en un día inhábil, la app lo advierte, pero no bloquea la carga.
        * *Varios demandados:* si el expediente tiene más de un demandado, un aviso recuerda revisar desde qué notificación corre el plazo (duda D35).
        * *Botón de Emergencia:* **"+1 Día Hábil (Prorrogar por asueto/falla en sistema)"**.
    * **Botones de Navegación del Flujo:**
        * Botón Principal: **"Avanzar de Etapa"**. (Despliega selector si hay bifurcaciones).
        * Menú Secundario:
            * **"Saltear etapa manualmente"**.
            * **"Retroceder etapa"**: deshace el último avance de ese camino (corrección de carga). Pide un motivo y, si los pasos que se deshacen tienen actividad, muestra cuál y pide confirmación.
            * **"Agregar plazo suelto"**: un plazo que no está en el flujo, como una intimación del juzgado. Pide título, tipo, inicio, valor y si aplica gracia; queda asociado al hito actual como contexto y no cambia la posición en el flujo.
            * **"Cargar suspensión de plazos"**: período desde y hasta, con motivo (acuerdo de partes o resolución del tribunal). Recalcula los plazos del expediente.

### Pantalla 4: Configuración y Calendario Global
* **Vista de Calendario:** Mensual.
* **Feriados del Sistema:** Muestra en gris oscuro los feriados y ferias precargados.
* **Agregar Inhábil Manual:** Botón para marcar un día específico como inhábil para todo el estudio (lo ven y lo aplican todos sus miembros, para que el vencimiento de un expediente sea el mismo para todos).

### Pantalla 5: Cuenta, plan y facturación
La ven todos los miembros. Solo el titular puede cambiar el plan, los usuarios y los datos fiscales, y dar de baja.

* **Mi plan:**
    * Plan y tramo actual (ej. *"Individual · hasta 10 clientes · mensual"*), estado de la suscripción y fecha del próximo cobro.
    * **Indicador de clientes activos:** *"7 de 10 clientes activos"*, con una barra. Al llegar al 80 % aparece el aviso *"Estás cerca del límite de tu plan"*. Se aclara qué cuenta: clientes con al menos un expediente activo o pausado.
    * **"Cambiar de plan":** muestra los tramos con su precio final.
        * La subida es inmediata, y antes de confirmar se informa la diferencia a pagar por el período en curso.
        * La bajada se programa para el próximo período. Si los clientes activos superan el nuevo límite, no se permite y se explica por qué.
* **Usuarios (plan Estudio):** miembros, rol y estado, invitar y revocar. Se muestran los usuarios incluidos y el precio de cada adicional.
* **Datos fiscales:** CUIT, nombre o razón social, condición frente al IVA, domicilio fiscal y email de facturación. Se piden antes del primer cobro.
* **Facturas:** listado con fecha, tipo y número de comprobante, período, importe y estado, y descarga del PDF. Una factura pendiente de autorización se muestra como *"En proceso"*.
* **Mis dispositivos:** dispositivos con sesión activa, último uso y "Cerrar sesión" en cada uno.
* **"Dar de baja":** siempre visible, sin pasos intermedios innecesarios. Informa hasta cuándo sigue el acceso completo, el período de solo lectura y la fecha de borrado. Al confirmar, muestra y envía por email el número de trámite.
* **"Arrepentimiento":** visible durante los 10 días corridos posteriores a la contratación o al primer cobro. Al confirmar, informa el número de trámite y la devolución.
* **Solo lectura:** cuando la suscripción terminó, toda la app muestra la franja *"Tu plan terminó: podés consultar y exportar tus datos hasta el DD/MM. Después se eliminan."*, con los botones "Exportar datos" y "Volver a contratar".

---

## 3. Comportamientos Clave de la UI

1. **Flexibilidad de Edición:** Si el abogado sobrescribe los días de plazo, aparece un icono de "modificado manualmente".
2. **Prevención de Errores:** Confirmación (pop-up) antes de usar *"Saltear etapa manualmente"* y *"Retroceder etapa"*. Las dos acciones piden motivo y quedan en la auditoría.
3. **Vacíos de Tiempo:** Cuando una etapa depende del tribunal (valor 0 días), el cronómetro no corre; muestra estado de "Esperando resolución".
4. **Resumen diario por email:** a la hora configurada (por defecto, 07:00), cada usuario recibe sus vencidos sin cumplir, sus vencimientos en rojo y amarillo y las oportunidades por plazos de la contraparte. Por defecto el email trae solo cantidades, el número de expediente y el enlace a la app; la carátula y el cliente se incluyen solo si el usuario lo activa. Se puede desactivar desde el perfil.
5. **Datos sensibles en campos libres:** junto a los campos de texto libre (el motivo de un cambio, el título de un plazo suelto) se muestra la ayuda *"No incluyas datos de salud ni otros datos sensibles"*.
