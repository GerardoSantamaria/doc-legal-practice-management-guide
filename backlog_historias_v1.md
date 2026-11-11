# Backlog de Historias de Usuario - Asistente Legal (V1)

**Estado:** borrador v0.1 · **Fecha:** 11/11/2026

Historias de la V1, derivadas de:
- el análisis;
- el modelo de datos;
- la UI;
- el documento de lógica de plazos;
- el contrato de API (`api/openapi_v1.yaml`, citado por `operationId`);
- el modelado de amenazas (citado por ID de amenaza).

Las historias están agrupadas por épica y ordenadas por dependencia: las primeras épicas habilitan a las siguientes. Las estimaciones y los sprints los define el equipo.

**Formato de los criterios:** *Dado* un contexto, *cuando* pasa algo, *entonces* el resultado esperado. Cada historia lista solo sus criterios propios; los transversales están en la Definición de terminado.

---

## Definición de listo (para empezar una historia)

- Tiene criterios de aceptación verificables, y cada uno se puede probar.
- Están identificados los endpoints del contrato de API y las tablas del modelo que toca.
- Si depende de una duda legal abierta (D01 a D36), está indicado cuál, y la historia tiene una postura por defecto para avanzar.
- Si toca datos personales, pagos, autenticación o el back-office, tiene revisadas sus amenazas en `modelado_de_amenazas_v1.md`.

## Definición de terminado (para cerrar una historia)

1. Todos los criterios de aceptación tienen una prueba automatizada que pasa.
2. **Aislamiento:** cada endpoint nuevo tiene una prueba con un usuario de otro estudio, que debe recibir 404 (ISO-09).
3. **Permisos:** cada endpoint con `x-roles` tiene una prueba con un rol no permitido, que debe recibir 403.
4. **Validación:** los cuerpos con campos desconocidos o fuera de rango responden 400, con el formato de problema y sin detalles internos.
5. Las acciones que modifican datos del estudio quedan en `audit_events` con su acción.
6. Los logs no contienen datos personales, tokens ni secretos (revisado en el pull request).
7. El pull request tiene revisión de código aprobada, y el análisis estático, el de dependencias y el escaneo de secretos están en verde, sin hallazgos críticos.
8. Las migraciones de Flyway corren desde cero y sobre la versión anterior.
9. La UI cumple lo de `definicion_de_ui_ux_asistente_legal.md` y funciona en un celular y en una computadora.

---

## Épica 1 · Base técnica

### HU-01 · Esqueleto del backend y del frontend
**Como** equipo **quiero** el proyecto base **para** construir sobre algo uniforme.
- *Dado* el repositorio del backend, *cuando* se compila con Maven, *entonces* genera una imagen con Java 21 y Spring Boot 3, organizada como monolito modular (expedientes, flujos, calendario, motor, suscripciones, facturación, auditoría).
- *Dado* el repositorio del frontend, *cuando* se compila, *entonces* genera una PWA en React, instalable.
- *Dado* un pull request, *cuando* corre la integración continua, *entonces* ejecuta las pruebas, el análisis estático, el de dependencias y el escaneo de secretos, y bloquea el merge si alguno falla.
- *Dado* un despliegue, *cuando* se aplica, *entonces* corre las migraciones de Flyway con un rol propio, y la app arranca con un rol sin permisos de DDL.

### HU-02 · Errores, logs y headers de seguridad
**Como** responsable de seguridad **quiero** un comportamiento uniforme ante errores **para** no filtrar información y poder diagnosticar.
- *Dado* cualquier error, *cuando* la API responde, *entonces* usa `application/problem+json` con un `correlationId`, y sin trazas, rutas internas ni versiones.
- *Dado* cualquier respuesta, *entonces* incluye CSP, HSTS, `X-Content-Type-Options`, `frame-ancestors 'none'`, `Referrer-Policy` y `Permissions-Policy`.
- *Dado* un log, *entonces* es JSON estructurado con los campos permitidos, y los tokens y credenciales salen enmascarados.
- *Dado* que se supera un límite de la sección 6 del modelado de amenazas, *entonces* la respuesta es 429 con `Retry-After`.

### HU-03 · Aislamiento entre estudios en la base
**Como** estudio **quiero** que nadie de otro estudio pueda ver mis datos **para** cuidar el secreto profesional.
- *Dado* una tabla con `organization_id`, *entonces* tiene Row-Level Security con `FORCE`, y la app no es dueña de la tabla.
- *Dado* una transacción de la API o de un job, *cuando* empieza, *entonces* fija el estudio en la variable de sesión. Sin esa variable, las consultas no devuelven filas.
- *Dado* un expediente, *cuando* se intenta asociarlo a un cliente de otro estudio, *entonces* la clave foránea compuesta lo rechaza.
- *Dado* el back-office, *entonces* usa un rol de base sin permisos sobre las tablas de los estudios (BO-02).

## Épica 2 · Acceso, estudio y documentos legales

### HU-04 · Ingresar con Google
**Como** abogado **quiero** entrar con mi cuenta de Google **para** no manejar otra contraseña.
- *Dado* un usuario nuevo, *cuando* completa el login (`iniciarLogin`), *entonces* se crea `users` y `user_identities` con el `sub` de Google, y se exige `email_verified`.
- *Dado* un usuario existente que cambió su email en Google, *cuando* entra, *entonces* se lo reconoce por `sub`, no por email (AUT-01).
- *Dado* un login exitoso, *entonces* se crea una sesión nueva con la cookie `__Host-SESSION` (`HttpOnly`, `Secure`, `SameSite=Lax`), y se registra `LOGIN`.
- *Dado* un login rechazado, *entonces* el mensaje es genérico y se registra `LOGIN_RECHAZADO`.
- *Dado* el parámetro de retorno después del login, *cuando* apunta a un sitio externo, *entonces* se ignora y se va al dashboard (AUT-05).

### HU-05 · Sesión, dispositivos y cierre de sesión
**Como** usuario **quiero** ver mis dispositivos y cerrar sesiones **para** controlar mi cuenta.
- *Dado* un usuario con 3 dispositivos activos, *cuando* entra desde un cuarto, *entonces* se cierra la sesión del más antiguo y se le avisa.
- *Dado* "Mis dispositivos" (`listarDispositivos`), *cuando* revoca uno (`revocarDispositivo`), *entonces* sus sesiones dejan de funcionar en la petición siguiente.
- *Dado* un usuario que es miembro de más de un estudio, *cuando* elige uno (`elegirEstudioActivo`), *entonces* toda la sesión opera sobre ese estudio, y el servidor verifica que la membresía siga activa en cada petición (ISO-02).
- *Dado* 8 horas de inactividad o 30 días de sesión, *entonces* la sesión vence.
- *Dado* "Cerrar sesión" (`cerrarSesion`), *entonces* la sesión se revoca en el servidor.
- *Dado* una petición `POST`, `PUT`, `PATCH` o `DELETE` sin el header `X-XSRF-TOKEN` válido, *entonces* responde 403 (AUT-04).

### HU-06 · Aceptar los documentos legales
**Como** prestador **quiero** registrar qué versión aceptó cada usuario **para** tener prueba de la aceptación.
- *Dado* un usuario nuevo, *cuando* termina el login, *entonces* no puede usar la app hasta aceptar los términos y la privacidad (`aceptarDocumentos`).
- *Dado* un titular, *cuando* crea el estudio, *entonces* acepta también el acuerdo de encargo, en nombre del estudio.
- *Dado* una versión nueva con `requires_reacceptance`, *cuando* el usuario entra después de su vigencia, *entonces* ve el resumen de cambios y tiene que aceptarla.
- *Dado* una aceptación, *entonces* queda en `legal_acceptances` (sin IP ni *user agent*) y en `audit_events` (`DOCUMENTO_LEGAL_ACEPTADO`).

### HU-07 · Crear el estudio (onboarding)
**Como** abogado **quiero** crear mi estudio **para** empezar la prueba gratuita.
- *Dado* un usuario sin estudio, *cuando* lo crea (`crearEstudio`) como `INDIVIDUAL` o `ESTUDIO`, *entonces* queda como `TITULAR` y la suscripción empieza en `PRUEBA` por 30 días, sin pedir medio de pago.
- *Dado* el onboarding, *entonces* se recomienda activar la verificación en dos pasos de Google.

### HU-08 · Invitar y gestionar miembros
**Como** titular **quiero** sumar abogados y asistentes **para** compartir la cartera.
- *Dado* un titular, *cuando* invita un email con un rol (`invitarMiembro`), *entonces* se envía un enlace con un token de un solo uso que vence a los 7 días; en la base se guarda solo su hash (AUT-06).
- *Dado* una invitación, *cuando* la acepta una cuenta de Google con otro email (`aceptarInvitacion`), *entonces* se rechaza.
- *Dado* el plan contratado, *cuando* la invitación superaría los usuarios del plan, *entonces* responde 409 `limite-usuarios`.
- *Dado* un miembro revocado (`revocarMiembro`), *entonces* sus sesiones en ese estudio se cierran en la misma transacción (AUT-10).
- *Dado* el único titular, *cuando* se intenta revocarlo o cambiarle el rol, *entonces* responde 409.

## Épica 3 · Catálogos, calendario y flujos (back-office)

### HU-09 · Back-office con MFA
**Como** admin **quiero** un back-office protegido **para** cargar catálogos sin exponer los datos de los estudios.
- *Dado* un usuario con `system_role = ADMIN`, *cuando* entra, *entonces* lo hace con una cuenta de Google Workspace con verificación en dos pasos forzada; si no la tiene, se rechaza.
- *Dado* una sesión de admin, *entonces* vence a la hora de inactividad, y cada login genera una alerta al responsable (BO-01).
- *Dado* un admin, *cuando* intenta leer datos de un estudio, *entonces* no puede: ni por la API ni por permisos de base.

### HU-10 · Cargar tribunales, regímenes y horarios
**Como** admin **quiero** mantener los catálogos **para** que el régimen y los límites horarios se resuelvan solos.
- *Dado* un tribunal (`crearTribunal`), *entonces* tiene departamento, tipo y régimen; su régimen no se puede cambiar si ya tiene expedientes judiciales.
- *Dado* un período de régimen por departamento (`crearRegimenDepartamento`), *cuando* se superpone con otro del mismo departamento, *entonces* responde 409.
- *Dado* un horario nuevo con fecha de vigencia (`crearHorario`), *entonces* exige la norma de referencia y recalcula los pasos pendientes afectados.

### HU-11 · Cargar y publicar el calendario
**Como** admin **quiero** cargar feriados, ferias y asuetos **para** que los vencimientos sean correctos.
- *Dado* un lote de cambios, *cuando* se simula (`simularCambioCalendario`), *entonces* informa cuántos pasos cambian, cuántos se adelantan y cuántos se atrasan.
- *Dado* un cambio que atrasa algún vencimiento, *cuando* se aplica sin `confirmDelays`, *entonces* responde 409 (MOT-02).
- *Dado* un cambio aplicado (`aplicarCambioCalendario`), *entonces*:
  - se incrementa `calendar_version`;
  - se recalculan los pasos pendientes afectados;
  - cada usuario afectado ve "tu vencimiento cambió", con el antes y el después;
  - se registra `CALENDARIO_MODIFICADO`.
- *Dado* un asueto o una feria, *entonces* exige la acordada de referencia.
- *Dado* la cobertura (`actualizarCobertura`), *cuando* se pasa a `OFICIAL`, *entonces* exige un validador distinto de quien hace el cambio.

### HU-12 · Importar y publicar la matriz
**Como** admin **quiero** importar la planilla validada por el abogado **para** publicar una versión del flujo.
- *Dado* un archivo de más de 5 MB, o que no sea un ZIP de Office por sus bytes iniciales, *cuando* se importa (`importarMatriz`), *entonces* se rechaza (BO-03).
- *Dado* una planilla, *entonces* se leen solo valores (sin evaluar fórmulas) y se aplican las validaciones de la sección 4 del documento de proyecto: IDs únicos, referencias existentes, un nodo inicial, plazos coherentes con su tipo, gracia solo en tipos que la admiten. Los errores salen con hoja y fila.
- *Dado* una importación sin errores, *cuando* se publica (`publicarVersionFlujo`) con quién la aprobó por el equipo legal, *entonces* se crea una versión `PUBLICADA` inmutable, con el SHA-256 de la planilla.
- *Dado* una versión nueva, *entonces* los expedientes existentes conservan la suya.

## Épica 4 · Motor de plazos

### HU-13 · Módulo del motor con los casos de prueba
**Como** equipo **quiero** el motor como función pura **para** probarlo de forma aislada antes que cualquier pantalla.
- *Dado* el módulo Java, *cuando* se corren sus pruebas, *entonces* pasan los casos 1 a 23 y los rechazos E1 y E2 de la sección 5 del documento de lógica, con los mismos resultados que `herramientas/motor_plazos_referencia.py`.
- *Dado* una entrada, *entonces* el motor no accede a la base: recibe el calendario, los inhábiles del estudio, las suspensiones y el horario como datos.
- *Dado* un valor por encima de `MAX_VALOR` del tipo, *entonces* lo rechaza (MOT-05).

### HU-14 · Todos los tipos de plazo
**Como** abogado **quiero** que la app calcule todos los tipos de plazo del fuero **para** no llevar ninguno por fuera.
- *Dado* cada uno de los 9 tipos, *entonces* el cálculo sigue la sección 2 del documento de lógica.
- *Dado* hábiles administrativos, *entonces* las ferias judiciales no suspenden (R6).
- *Dado* meses o años que vencen después del calendario cargado, *entonces* se calcula igual y se marca `calendar_incomplete` (R7).
- *Dado* horas, *entonces* corren desde el instante (R8).
- *Dado* una fecha fijada en un día inhábil, *entonces* se advierte `FECHA_EN_DIA_INHABIL`, sin bloquear.
- *Dado* una anticipación, *cuando* se reprograma la audiencia de referencia, *entonces* se recalcula (R9).
- *Dado* gracia en un tipo que no la admite, o prórroga en un tipo que no es en días, *entonces* responde 422.

### HU-15 · Vista previa y "por qué vence ese día"
**Como** abogado **quiero** ver cómo se calculó un vencimiento **para** confiar en él.
- *Dado* los datos de un plazo, *cuando* pido la vista previa (`calcularPlazo`), *entonces* recibo el vencimiento tipado (nominal, efectivo, límite ordinario y con gracia), sin que se guarde nada.
- *Dado* el resultado, *entonces* incluye cada día recorrido y el motivo de cada día salteado (feriado, feria, suspensión, inhábil del estudio).
- *Dado* un calendario provisorio, *entonces* el resultado dice "Cálculo aproximado: no considera feriados ni ferias".
- *Dado* un período sin calendario cargado (en tipos que lo exigen), *entonces* el estado es `CALENDARIO_NO_CARGADO` y la UI muestra una alerta bloqueante.

## Épica 5 · Clientes y expedientes

### HU-16 · Clientes
**Como** abogado **quiero** cargar y buscar clientes **para** asociarlos a sus expedientes.
- *Dado* un cliente nuevo (`crearCliente`), *entonces* el CUIT o DNI se valida por formato, y crear un cliente no consume el límite del plan.
- *Dado* la búsqueda (`listarClientes`), *entonces* busca por nombre o documento, paginada (máximo 100 por página).
- *Dado* un cliente con expedientes activos, *cuando* se intenta eliminarlo (`eliminarCliente`), *entonces* responde 409. Sin expedientes activos, se borra en forma lógica.

### HU-17 · Alta de un expediente nuevo
**Como** abogado **quiero** dar de alta un expediente **para** que la app me guíe desde el inicio.
- *Dado* el formulario, *cuando* elijo el tribunal, *entonces* la app muestra el régimen resuelto (`resolverRegimen`) antes de guardar.
- *Dado* un régimen que no se puede determinar, *cuando* guardo (`crearExpediente`), *entonces* responde 422 `regimen-sin-definir` y se pide el tribunal.
- *Dado* un régimen inconsistente entre tribunal y departamento, *entonces* se crea con el del tribunal, con un aviso, y se audita.
- *Dado* un régimen sin flujo publicado (Ley 15.057 en la V1), *entonces* se crea sin flujo y la ficha solo ofrece plazos sueltos.
- *Dado* que arranca en la etapa previa, *entonces* se asigna el flujo `PREJUDICIAL` y se abre su hito inicial; el tribunal puede quedar vacío.

### HU-18 · Límite de clientes del plan
**Como** prestador **quiero** aplicar el límite de clientes activos **para** sostener los tramos de precio.
- *Dado* un estudio en el límite de su tramo, *cuando* da de alta o reactiva un expediente de un cliente que no cuenta, *entonces* responde 409 `limite-clientes`, y la UI ofrece subir de plan sin perder lo cargado.
- *Dado* un cliente que ya cuenta como activo, *cuando* se le da de alta otro expediente, *entonces* no se aplica el límite.
- *Dado* dos altas simultáneas en el límite, *entonces* solo una pasa (`SELECT … FOR UPDATE`, PAG-04).
- *Dado* un estudio en el límite, *entonces* sus expedientes cargados siguen con plazos y alertas.
- *Dado* que se llega al 80 % del límite, *entonces* la app muestra un aviso.

### HU-19 · Alta de un expediente en curso
**Como** abogado **quiero** cargar mi cartera existente **para** empezar a usar la app con mis causas actuales.
- *Dado* "¿ya está en curso? Sí", *entonces* se pide la fecha de interposición y se eligen uno o más hitos actuales del mapa (`obtenerVersionFlujo`).
- *Dado* cada hito actual, *cuando* cargo el Día Cero, *entonces* se calcula. *Cuando* no lo conozco, puedo cargar el vencimiento a mano, con motivo, y queda `MANUAL`, con la leyenda "cargado a mano, no calculado".
- *Dado* un plazo cargado que ya venció, *entonces* la app pregunta en el momento si se cumplió.
- *Dado* el expediente creado, *entonces* los hitos anteriores se muestran como "anteriores a la carga", y se registra `EXPEDIENTE_EN_CURSO_CARGADO`.

### HU-20 · Editar, pausar, terminar y reactivar
**Como** abogado **quiero** mantener los datos del expediente **para** reflejar su estado real.
- *Dado* un expediente con flujo judicial, *cuando* se intenta cambiar el tribunal (`actualizarExpediente`), *entonces* responde 409.
- *Dado* "Terminar" (`terminarExpediente`), *entonces* exige el motivo y la fecha, y libera el lugar del cliente si era su último expediente activo.
- *Dado* "Reactivar" (`reactivarExpediente`), *entonces* aplica el límite de clientes.

### HU-21 · Interponer la demanda
**Como** abogado **quiero** pasar de la etapa previa al juicio **para** seguir con el flujo judicial que corresponde.
- *Dado* un expediente en la etapa previa, *cuando* cargo el tribunal y la fecha de interposición (`asignarFlujoJudicial`), *entonces* se resuelve el régimen, se asigna la versión vigente del flujo judicial y se abre su hito inicial.
- *Dado* un régimen sin flujo publicado, *entonces* el expediente queda con el régimen y solo admite plazos sueltos.

### HU-22 · Partes del expediente
**Como** abogado **quiero** cargar las contrapartes y terceros **para** tenerlos en la ficha.
- *Dado* las partes (`crearParte`, `actualizarParte`, `borrarParte`), *entonces* se cargan con su rol procesal.
- *Dado* más de un demandado, *entonces* la calculadora muestra el aviso de revisar desde qué notificación corre el plazo (D35).

## Épica 6 · Ficha del expediente y pasos

### HU-23 · Mapa del flujo con perspectiva
**Como** abogado **quiero** ver dónde está la causa y a quién le toca **para** saber qué hacer.
- *Dado* la ficha (`obtenerMapa`), *entonces* cada hito tiene su estado: futuro, actual, vencido, completado, salteado, no cumplido, anulado o anterior a la carga.
- *Dado* varios hitos actuales, *entonces* se muestra un panel de acción por cada uno.
- *Dado* un hito, *entonces* dice "Te toca a vos", "Le toca a la contraparte" o "Esperando al tribunal", según el responsable y el rol representado.

### HU-24 · Cargar y corregir el plazo de un paso
**Como** abogado **quiero** cargar el Día Cero y ajustar el plazo **para** obtener el vencimiento.
- *Dado* un paso recién abierto, *entonces* no tiene vencimiento hasta que se cargue el inicio del cómputo.
- *Dado* el inicio cargado (`actualizarPlazo`), *entonces* el backend calcula el vencimiento; un vencimiento enviado por el cliente se rechaza, salvo `MANUAL` en un paso cargado en curso (MOT-03).
- *Dado* un valor distinto del legal, *entonces* exige el motivo (por ejemplo, "Ampliación por distancia") y muestra el ícono de "modificado manualmente".
- *Dado* el botón "+1 día hábil", *entonces* suma a `extension_days` con motivo, solo en plazos en días.
- *Dado* cualquier cambio, *entonces* se registra `PLAZO_EDITADO` con los valores anteriores y nuevos.

### HU-25 · Avanzar de etapa
**Como** abogado **quiero** avanzar por el camino que corresponde **para** que se abran los próximos plazos.
- *Dado* un paso con varias transiciones, *cuando* avanzo (`avanzarEtapa`), *entonces* elijo una, y se abren todos sus destinos; si son varios, en paralelo.
- *Dado* un escrito presentado, *entonces* puedo registrar la fecha y hora del cargo (`filed_at`).
- *Dado* una transición que cierra el camino, *entonces* no se abre ningún paso.
- *Dado* un paso que no está pendiente, *cuando* intento avanzarlo, *entonces* responde 409 `paso-no-pendiente`.

### HU-26 · Saltear y retroceder
**Como** abogado **quiero** corregir el recorrido **para** reparar errores de carga.
- *Dado* "Saltear" (`saltearEtapa`), *entonces* exige el motivo y una confirmación, y registra `ETAPA_SALTEADA`.
- *Dado* "Retroceder" sobre un paso completado (`retrocederEtapa`), *entonces* los pasos que abrió pasan a `ANULADO` con motivo y él vuelve a `PENDIENTE` con su vencimiento original.
- *Dado* que los pasos a anular abrieron otros, *entonces* responde 409 `retroceso-con-dependientes`.
- *Dado* que los pasos a anular tienen actividad (checklist, cargo o edición), *cuando* no se confirmó, *entonces* responde 409 con el detalle de esa actividad.
- *Dado* un retroceso, *entonces* nada se borra, y se registra `ETAPA_RETROCEDIDA`.

### HU-27 · Plazos sueltos
**Como** abogado **quiero** cargar intimaciones del juzgado **para** que también me avisen.
- *Dado* "Agregar plazo suelto" (`crearPlazoSuelto`), *entonces* pide título, tipo, inicio, valor y gracia, y queda asociado al hito actual como contexto.
- *Dado* un plazo suelto, *entonces* entra en el dashboard, el semáforo y el email, igual que un hito.
- *Dado* un plazo suelto, *cuando* se completa (`marcarCumplido`) o se anula (`anularPlazoSuelto`), *entonces* no cambia la posición en el flujo.
- *Dado* el campo del título, *entonces* se muestra la ayuda "No incluyas datos de salud ni otros datos sensibles".

### HU-28 · Suspensiones de plazos
**Como** abogado **quiero** cargar una suspensión **para** que los plazos del expediente no corran.
- *Dado* una suspensión con desde, hasta y motivo (`crearSuspension`), *entonces* el motor la trata como días inhábiles de ese expediente y recalcula los pasos pendientes (`SUSPENSION_CARGADA`).
- *Dado* que se quita (`borrarSuspension`), *entonces* recalcula de nuevo.

### HU-29 · Checklist del paso
**Como** abogado **quiero** tildar las tareas y la documentación **para** no olvidarme de nada.
- *Dado* un paso de un hito, *entonces* muestra el checklist de la versión del flujo del expediente.
- *Dado* un ítem tildado (`actualizarItemChecklist`), *entonces* queda guardado por paso, con quién y cuándo.

### HU-30 · Historial del expediente
**Como** abogado **quiero** ver todo lo que pasó en el expediente **para** tener respaldo ante un reclamo.
- *Dado* el historial (`obtenerHistorial`), *entonces* lista los eventos de auditoría del expediente, paginados, con quién, cuándo, qué cambió y el motivo.
- *Dado* un evento, *entonces* muestra solo los campos de la lista permitida.

## Épica 7 · Alertas

### HU-31 · Dashboard con vencidos sin cumplir
**Como** abogado **quiero** ver primero lo que se me venció **para** actuar de inmediato.
- *Dado* un paso propio pendiente con el último límite pasado, *entonces* aparece arriba de todo en "Vencidos sin cumplir", con la acción, el expediente, el cliente y la fecha de vencimiento (`obtenerDashboard`).
- *Dado* un paso propio en su plazo de gracia, *entonces* la tarjeta dice "Último momento: hasta hoy a las 12:00".
- *Dado* una tarjeta de vencido, *entonces* no desaparece hasta elegir "Lo cumplí" (con el cargo), "No se cumplió" (con motivo y, si existe, la salida del hito; `registrarNoCumplido`) o "Corregir plazo".
- *Dado* un asistente, *entonces* puede usar "Lo cumplí" y "Corregir plazo", pero no "No se cumplió".

### HU-32 · Semáforo parametrizable
**Como** abogado **quiero** ver qué se viene **para** organizarme.
- *Dado* los umbrales (`obtenerParametrosAlertas`), *entonces* son los del estudio, o los globales si no tiene propios (por defecto, rojo hasta 2 días hábiles y amarillo hasta 5).
- *Dado* un titular, *cuando* los ajusta (`actualizarParametrosAlertas`), *entonces* el rojo tiene que ser menor que el amarillo, y se registra `ALERTAS_CONFIGURADAS`.
- *Dado* un vencimiento con cálculo aproximado, *entonces* la tarjeta lo indica.

### HU-33 · Oportunidades por plazos de la contraparte
**Como** abogado **quiero** saber cuándo venció un plazo de la otra parte **para** aprovecharlo.
- *Dado* un paso de la contraparte, *mientras* corre, *entonces* se ve en la ficha como seguimiento, sin alerta.
- *Dado* que vence, *entonces* aparece en "Oportunidades", con la acción sugerida.
- *Dado* un usuario que desactivó estos avisos, *entonces* no los ve en el dashboard ni en el email.

### HU-34 · Resumen diario por email
**Como** abogado **quiero** recibir mis vencimientos por email **para** enterarme aunque no abra la app.
- *Dado* la hora configurada (por defecto, 07:00), *entonces* cada usuario recibe sus vencidos sin cumplir, sus rojos, sus amarillos y sus oportunidades, de los estudios donde está activo (ISO-04).
- *Dado* las preferencias por defecto, *entonces* el email trae solo cantidades, números de expediente y el enlace; la carátula y el cliente, solo si el usuario lo activa (`actualizarPreferencias`).
- *Dado* un día sin novedades, *entonces* no se envía el email.
- *Dado* que el resumen no salió a las 07:30, *entonces* llega una alerta al responsable (JOB-06).
- *Dado* el dominio de envío, *entonces* tiene SPF, DKIM y DMARC (JOB-01).

### HU-35 · Inhábiles del estudio y aviso de recálculo
**Como** abogado **quiero** marcar un asueto local **para** que mis plazos se corran.
- *Dado* un día inhábil del estudio (`crearInhabilEstudio`), *entonces* recalcula los pasos pendientes del estudio, y el cambio es igual para todos sus miembros.
- *Dado* un recálculo por cualquier causa, *cuando* cambia un vencimiento, *entonces* el usuario ve "tu vencimiento cambió", con el antes y el después.

## Épica 8 · Suscripción y cobro

### HU-36 · Planes y tramos
**Como** abogado **quiero** ver los planes **para** elegir el que me conviene.
- *Dado* la lista de planes (`listarPlanes`), *entonces* muestra cada tramo con su límite de clientes activos, sus usuarios incluidos, sus dispositivos y su precio final con impuestos.
- *Dado* la pantalla 5, *entonces* muestra el plan actual y "X de N clientes activos".

### HU-37 · Contratar y pagar
**Como** titular **quiero** pagar mi plan **para** seguir usando la app al terminar la prueba.
- *Dado* un plan elegido (`iniciarCheckout`), *entonces* el backend crea el checkout con el precio de la base y devuelve la URL del proveedor; el cliente no envía importes (PAG-03).
- *Dado* un webhook (`recibirWebhookPagos`), *entonces* se procesa solo con firma válida y dentro de la ventana de tiempo, y el estado se confirma consultando la API del proveedor (PAG-01).
- *Dado* un evento repetido, *entonces* no se procesa dos veces (PAG-02).
- *Dado* un importe que no coincide con el plan, *entonces* no activa nada y genera una alerta.
- *Dado* que faltan los datos fiscales, *entonces* se piden antes del primer cobro.

### HU-38 · Cambiar de plan
**Como** titular **quiero** subir o bajar de tramo **para** ajustarme a mi cartera.
- *Dado* una subida, *cuando* la simulo (`simularCambioPlan`) y la confirmo (`cambiarPlan`), *entonces* tiene efecto inmediato, y la diferencia del período se informa antes.
- *Dado* una bajada, *entonces* se programa para el próximo período, y responde 409 `bajada-supera-limite` si los clientes activos no entran.
- *Dado* el cambio de período con una bajada programada, *cuando* los clientes activos ya no entran, *entonces* no se aplica y se avisa al titular.

### HU-39 · Falta de pago y solo lectura
**Como** prestador **quiero** un circuito claro ante la falta de pago **para** no cortar de golpe el acceso a plazos procesales.
- *Dado* un cobro fallido, *entonces* se avisa y se reintenta durante 7 días (`EN_MORA`).
- *Dado* que pasan los 7 días, o que termina la prueba sin elegir plan, *entonces* la suscripción pasa a `SOLO_LECTURA` por 30 días.
- *Dado* `SOLO_LECTURA`, *entonces*:
  - toda escritura responde 403 `suscripcion-solo-lectura`, verificado en el backend (PAG-05);
  - la exportación sigue disponible;
  - el resumen diario se sigue enviando;
  - la app muestra la franja con la fecha de borrado.
- *Dado* que el estudio paga durante la solo lectura, *entonces* recupera el uso completo.

### HU-40 · Dar de baja y arrepentimiento
**Como** titular **quiero** darme de baja o arrepentirme fácilmente **para** ejercer mis derechos como cliente.
- *Dado* el botón "Dar de baja", siempre visible (`darDeBaja`), *entonces* tiene efecto al final del período pagado, muestra un número de trámite y lo confirma por email (`BAJA_SOLICITADA`).
- *Dado* una baja pedida, *cuando* el titular la deja sin efecto antes del fin del período (`anularBaja`), *entonces* la suscripción sigue.
- *Dado* los 10 días corridos desde la contratación o el primer cobro, *entonces* se ve el botón "Arrepentimiento" (`arrepentirse`): devuelve lo cobrado, genera una nota de crédito y confirma con número de trámite (`ARREPENTIMIENTO_SOLICITADO`).
- *Dado* que el plazo de arrepentimiento venció, *entonces* el botón no se muestra, y la API responde 409.

### HU-41 · Purga de los datos del estudio
**Como** encargado del tratamiento **quiero** borrar los datos al terminar **para** cumplir el acuerdo de encargo.
- *Dado* el fin de la solo lectura, *entonces* los datos del estudio se eliminan dentro de los 30 días siguientes, con aviso al titular 7 días antes.
- *Dado* la purga, *cuando* corre, *entonces* vuelve a verificar en la misma transacción que el estudio no haya vuelto a contratar (JOB-05).
- *Dado* la purga, *entonces* conserva la fila del estudio, sus datos fiscales y sus facturas, y registra `DATOS_DEL_ESTUDIO_ELIMINADOS`.
- *Dado* el pedido del titular, *entonces* se entrega una constancia de la destrucción.

## Épica 9 · Facturación electrónica

### HU-42 · Datos fiscales
**Como** titular **quiero** cargar mis datos fiscales **para** recibir la factura correcta.
- *Dado* el formulario (`actualizarDatosFiscales`), *entonces* pide CUIT, razón social, condición frente al IVA, domicilio fiscal y email de facturación, y valida el dígito verificador del CUIT.
- *Dado* un cambio de datos, *entonces* las facturas ya emitidas no cambian (se guarda una copia en cada factura).

### HU-43 · Emitir la factura ante ARCA
**Como** prestador **quiero** facturar cada cobro **para** cumplir con ARCA.
- *Dado* un cobro confirmado, *entonces* se crea una factura `PENDIENTE` en la misma transacción.
- *Dado* el job de facturación, *entonces* se autentica en WSAA con el certificado del gestor de secretos, y pide el CAE con `FECAESolicitar`. El ticket de acceso nunca queda en los logs (FAC-04).
- *Dado* un reintento, *entonces* antes consulta `FECompUltimoAutorizado`: si el comprobante ya estaba autorizado, lo recupera y no pide otro número (FAC-02).
- *Dado* que ARCA no responde, *entonces* la factura queda pendiente y se reintenta, sin afectar el acceso del estudio.
- *Dado* una factura autorizada, *entonces* se genera el PDF con el código QR, se envía al email de facturación y se registra `FACTURA_EMITIDA`.
- *Dado* el tipo de comprobante, *entonces* sale de la condición frente al IVA del emisor y del receptor, según la regla validada por el contador.
- *Dado* el entorno de homologación, *entonces* toda la integración está probada ahí antes de producción, con certificados distintos.

### HU-44 · Notas de crédito y listado de facturas
**Como** titular **quiero** ver y descargar mis facturas **para** mi contabilidad.
- *Dado* un reembolso, *entonces* se emite una nota de crédito asociada a la factura original; la factura autorizada no se modifica (FAC-03).
- *Dado* el listado (`listarFacturas`), *entonces* muestra fecha, tipo, número, período, importe y estado, y permite descargar el PDF (`descargarFactura`) por un endpoint autenticado (ISO-06).

## Épica 10 · Privacidad y exportación

### HU-45 · Exportar los datos del estudio
**Como** titular **quiero** exportar todo **para** tener mis datos fuera de la app.
- *Dado* el pedido (`pedirExportacion`), *entonces* se prepara en segundo plano, en JSON o XLSX, con clientes, expedientes, pasos e historial.
- *Dado* una exportación lista (`obtenerExportacion`), *entonces* el enlace es firmado, de un solo uso y válido por 24 horas, y se registra `DATOS_EXPORTADOS` (JOB-03).
- *Dado* un valor que empieza con `=`, `+`, `-` o `@`, *entonces* se escapa en la planilla (JOB-04).
- *Dado* más de 3 pedidos en un día, *entonces* responde 429.

### HU-46 · Derechos de los titulares
**Como** responsable de privacidad **quiero** un procedimiento para los pedidos de acceso, rectificación y supresión **para** responder en plazo.
- *Dado* un pedido de un usuario sobre sus datos, *entonces* se responde en 10 días corridos (acceso) o 5 días hábiles (rectificación y supresión), con la identidad verificada.
- *Dado* un pedido de un cliente de un estudio, *entonces* se le hace llegar al estudio dentro de los 2 días hábiles, y no se responde por cuenta propia.
- *Dado* el perfil, *entonces* el usuario puede ver y corregir sus datos y retirar el consentimiento de los emails de novedades.

---

## Orden sugerido

1. **Base:** épicas 1 y 2, más la HU-13 del motor (se puede hacer en paralelo, guiada por los casos de prueba).
2. **Datos que habilitan el resto:** épica 3 (calendario provisorio y la matriz importada) y el resto de la épica 4.
3. **Núcleo del producto:** épicas 5, 6 y 7.
4. **Monetización:** épicas 8 y 9. La integración con ARCA en homologación conviene empezarla antes, porque depende de trámites (certificado y punto de venta).
5. **Cierre:** épica 10, prueba de penetración y revisión de las brechas del modelado de amenazas.

**Bloqueos externos:**
- las dudas legales de la reunión con el abogado (afectan a las HU-12, HU-14, HU-17 y HU-21);
- la elección del hosting (HU-01 y los backups);
- el proveedor de pagos (HU-37);
- la condición fiscal del emisor (HU-43).
