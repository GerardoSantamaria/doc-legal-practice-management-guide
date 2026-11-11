# Lógica Matemática: Calculadora de Días Hábiles Judiciales (PBA)

Este documento define la lógica algorítmica que debe seguir el backend para calcular correctamente los vencimientos legales en la Provincia de Buenos Aires, evitando errores de mala praxis.

> **Fuente única de verdad:** el cálculo vive **solo en el backend** (Java + Spring Boot). El frontend nunca recalcula plazos por su cuenta; para mostrar una vista previa mientras el abogado edita, consulta al backend.

> **Principio rector:** ante una regla jurídica no confirmada, el motor elige la interpretación que produce **el vencimiento más temprano**. Un aviso anticipado es una molestia; uno tardío es mala praxis.

---

## 1. Conceptos Fundamentales

Para que el algoritmo funcione, los desarrolladores deben entender estas reglas del derecho procesal:

*   **Evento Disparador (Día Cero):** Es el día en que el abogado queda notificado (ej. recibe una cédula o es día de nota). **El plazo no comienza a correr ese día**.
*   **Inicio del Cómputo (Día Uno):** El plazo procesal comienza a correr a partir del **siguiente día hábil judicial** posterior al Día Cero.
*   **Día Hábil Judicial:** De Lunes a Viernes. Se excluyen sábados, domingos, feriados nacionales, provinciales inamovibles, ferias judiciales (Enero completo y dos semanas de Julio), asuetos declarados por la SCBA para el departamento judicial del expediente y los días inhábiles manuales que haya cargado el estudio dueño del expediente.
*   **Plazo de Gracia (Art. 124 CPCCBA):** El vencimiento final se extiende hasta las **primeras cuatro (4) horas hábiles del día hábil posterior** al vencimiento ordinario. En PBA, el horario judicial es de 08:00 a 14:00, por lo que el plazo de gracia finaliza a las **12:00 hs (mediodía)**. Solo se calcula si el hito tiene `Aplica_Gracia = SÍ`.

---

## 2. Variables del Motor de Cálculo

### Inputs (Entradas de la función)
1.  `fecha_notificacion` (Date, obligatorio): Fecha ingresada por el usuario (Día Cero).
2.  `plazo_valor` (Integer, `>= 0`): Cantidad de días de plazo (Ej: 10). *Este valor viene de la matriz procesal, pero puede ser sobrescrito por el usuario.*
3.  `plazo_tipo` (Enum): `HABILES_JUDICIALES`, `CORRIDOS` o `SIN_PLAZO`. `SIN_PLAZO` siempre devuelve `SIN_VENCIMIENTO`. Los tipos pendientes de la matriz (`HABILES_ADMINISTRATIVOS`, `ANIOS`, `FECHA_FIJADA`) no llegan al motor hasta que se defina su regla de cómputo; ver la sección 4 del análisis.
4.  `aplica_gracia` (Boolean): viene del hito de la matriz.
5.  `dias_prorroga_manual` (Integer, `>= 0`, default 0): Días extra sumados por asuetos imprevistos.
6.  `calendario` (Objeto): construido por el backend para el expediente, con:
    *   `inhabiles` (Set of Dates): unión de feriados, ferias, asuetos del departamento judicial del expediente e inhábiles manuales del estudio.
    *   `cubierto_hasta` (Date): último día para el cual el calendario oficial está cargado y validado.

El backend rechaza la entrada (error de validación) si falta `fecha_notificacion`, si algún entero es negativo o si `plazo_valor + dias_prorroga_manual` supera el máximo admitido (ver `MAX_DIAS_PLAZO`).

### Outputs (Salidas de la función)
1.  `estado` (Enum):
    *   `CALCULADO`: hay vencimiento.
    *   `SIN_VENCIMIENTO`: plazo 0. La UI muestra "Esperando resolución".
    *   `CALENDARIO_NO_CARGADO`: el cómputo llega a una fecha posterior a `cubierto_hasta`. **No se devuelve ninguna fecha**; la UI muestra una alerta bloqueante.
2.  `fecha_vencimiento_ordinario` (Date): Día en que se cumplen los días de plazo. La hora límite de ese día está pendiente de definición (ver regla R3).
3.  `fecha_hora_fin_gracia` (DateTime con zona horaria, nullable): Día hábil posterior a las 12:00 hs, hora de Argentina. Es `null` si `aplica_gracia = NO`.
4.  `dias_computados` (List of Dates): los días que se contaron, en orden. Permite que la UI explique "por qué vence ese día" y facilita la auditoría.

---

## 3. Lógica del Algoritmo (Pseudocódigo)

```text
CONSTANTES
    ZONA_HORARIA      = "America/Argentina/Buenos_Aires"
    HORA_FIN_GRACIA   = 12:00
    MAX_DIAS_PLAZO    = 365    // corte de validación de la entrada

Función EsInhabil(fecha, calendario) {
    Si (fecha > calendario.cubierto_hasta) {
        Lanzar CalendarioNoCargado(fecha)
    }
    Retornar (fecha ES Sábado) O (fecha ES Domingo) O (fecha ESTÁ EN calendario.inhabiles)
}

Función SiguienteHabil(fecha, calendario) {
    siguiente = fecha + 1 día
    Mientras (EsInhabil(siguiente, calendario)) {
        siguiente = siguiente + 1 día
    }
    Retornar siguiente
}

Función CalcularVencimiento(fecha_notificacion, plazo_valor, plazo_tipo,
                            aplica_gracia, dias_prorroga_manual, calendario) {

    // 1. Validar entradas (rechazar antes de calcular)
    Validar fecha_notificacion != null
    Validar plazo_valor >= 0 Y dias_prorroga_manual >= 0
    total_dias = plazo_valor + dias_prorroga_manual
    Validar total_dias <= MAX_DIAS_PLAZO

    // 2. Sin plazo: depende del tribunal, no hay vencimiento
    Si (plazo_tipo == SIN_PLAZO O total_dias == 0) {
        Retornar { estado: SIN_VENCIMIENTO }
    }

    Intentar {
        // 3. Cómputo del vencimiento ordinario
        dias_computados = []

        Si (plazo_tipo == HABILES_JUDICIALES) {
            // Regla R1 (a validar): si el Día Cero es inhábil, se cuenta igual
            // desde el siguiente hábil. Es la interpretación más temprana.
            fecha_actual = fecha_notificacion
            Mientras (largo(dias_computados) < total_dias) {
                fecha_actual = fecha_actual + 1 día
                Si (NO EsInhabil(fecha_actual, calendario)) {
                    Agregar fecha_actual a dias_computados
                }
            }
            fecha_vencimiento_ordinario = fecha_actual
        }

        Si (plazo_tipo == CORRIDOS) {
            // Se cuentan todos los días calendario desde el día siguiente al Día Cero.
            fecha_vencimiento_ordinario = fecha_notificacion + total_dias días
            // Regla R2 (a validar): si el último día es inhábil, el acto
            // se puede cumplir el siguiente día hábil.
            Si (EsInhabil(fecha_vencimiento_ordinario, calendario)) {
                fecha_vencimiento_ordinario = SiguienteHabil(fecha_vencimiento_ordinario, calendario)
            }
            dias_computados = días calendario entre (fecha_notificacion + 1) y fecha_vencimiento_ordinario
        }

        // 4. Plazo de gracia (solo si el hito lo admite)
        fecha_hora_fin_gracia = null
        Si (aplica_gracia) {
            dia_gracia = SiguienteHabil(fecha_vencimiento_ordinario, calendario)
            fecha_hora_fin_gracia = CrearFechaHora(dia_gracia, HORA_FIN_GRACIA, ZONA_HORARIA)
        }

        Retornar {
            estado: CALCULADO,
            fecha_vencimiento_ordinario,
            fecha_hora_fin_gracia,
            dias_computados
        }
    }
    Capturar (CalendarioNoCargado) {
        Retornar { estado: CALENDARIO_NO_CARGADO }
    }
}
```

**Por qué el bucle termina siempre:** `total_dias` está acotado por `MAX_DIAS_PLAZO` y cada iteración avanza un día calendario. Si el calendario no cubre el rango, `EsInhabil` corta con `CalendarioNoCargado` en lugar de seguir avanzando.

---

## 4. Reglas pendientes de validación jurídica

El motor ya implementa una interpretación por defecto (la más temprana). El equipo legal debe confirmar o corregir cada una antes del lanzamiento. Cada regla tiene su propio caso de prueba.

| Regla | Pregunta | Comportamiento por defecto del motor | Caso |
| ----- | ----- | ----- | ----- |
| R1 | Si la notificación ocurre en día inhábil (sábado, feriado, feria), ¿se tiene por notificado el siguiente día hábil? | Cuenta el Día Uno desde el siguiente hábil (no corre el Día Cero). | 10, 12 |
| R2 | En plazos corridos, si el último día es inhábil, ¿se traslada al siguiente hábil? | Sí, se traslada. | 11 |
| R3 | ¿Cuál es la hora límite del vencimiento ordinario: 14:00 (fin del horario judicial) o 23:59 (presentación electrónica)? ¿Cómo interactúa con el plazo de gracia según el reglamento de presentaciones electrónicas de la SCBA? | No se muestra hora; solo la fecha. | — |
| R4 | ¿Jueves Santo, el 24/12 y el 31/12 son inhábiles judiciales en PBA? (Dependen de lo que declare la SCBA cada año.) | Se cargan solo si hay acordada; el calendario es la fuente. | 3b |
| R5 | La forma de notificación (cédula, electrónica, ministerio de la ley los martes y viernes, art. 133 CPCCBA) cambia el Día Cero. ¿La app lo calcula o lo ingresa el abogado? | Lo ingresa el abogado (V1). | — |

---

## 5. Casos de Prueba (Test Cases)

Los tests **no dependen del calendario real**: cada caso declara su propio calendario de prueba (*fixture*). Así un test no falla porque alguien cargó o borró un feriado en la base. La validación del calendario real 2024–2026 es una tarea aparte, firmada por el equipo legal.

### 5.1 Calendarios de prueba

Salvo indicación, `cubierto_hasta = 31/12/2025`.

| Fixture | Días inhábiles (además de sábados y domingos) |
| ----- | ----- |
| `VACIO` | ninguno |
| `JUNIO_2024` | 17/06/2024, 20/06/2024, 21/06/2024 |
| `MARZO_2024` | 24/03/2024 |
| `SEMANA_SANTA_2024` | 24/03/2024, 28/03/2024, 29/03/2024, 02/04/2024 |
| `FERIA_INVIERNO_2024` | 15/07/2024 al 26/07/2024 |
| `FIN_DE_AÑO_2024` | 25/12/2024 y 01/01/2025 al 31/01/2025 |
| `FIN_DE_AÑO_2024_SIN_2025` | 25/12/2024, con `cubierto_hasta = 31/12/2024` |

### 5.2 Casos

Todos los resultados de gracia son a las 12:00 hs, hora de Argentina.

| # | Qué prueba | Día Cero | Plazo | Tipo | Gracia | Prórroga | Fixture | Vencimiento ordinario esperado | Fin de gracia esperado |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | Cómputo estándar sin feriados | Lun 03/06/2024 | 10 | Hábiles | Sí | 0 | `VACIO` | Lun 17/06/2024 | Mar 18/06/2024 |
| 2 | Feriado en día de semana dentro del plazo | Lun 03/06/2024 | 10 | Hábiles | Sí | 0 | `JUNIO_2024` | Mar 18/06/2024 | Mié 19/06/2024 |
| 3 | Fin de semana y feriado en domingo (sin efecto) | Mié 20/03/2024 | 5 | Hábiles | Sí | 0 | `MARZO_2024` | Mié 27/03/2024 | Jue 28/03/2024 |
| 3b | El día de gracia cae en inhábiles consecutivos | Mié 20/03/2024 | 5 | Hábiles | Sí | 0 | `SEMANA_SANTA_2024` | Mié 27/03/2024 | Lun 01/04/2024 |
| 4 | Feria judicial de invierno congela el reloj | Jue 11/07/2024 | 5 | Hábiles | Sí | 0 | `FERIA_INVIERNO_2024` | Jue 01/08/2024 | Vie 02/08/2024 |
| 5 | Cruce de año y feria de enero | Vie 20/12/2024 | 10 | Hábiles | Sí | 0 | `FIN_DE_AÑO_2024` | Jue 06/02/2025 | Vie 07/02/2025 |
| 6 | Calendario del año siguiente no cargado | Vie 20/12/2024 | 10 | Hábiles | Sí | 0 | `FIN_DE_AÑO_2024_SIN_2025` | Estado `CALENDARIO_NO_CARGADO`, sin fechas | — |
| 7 | Plazo 0 (depende del tribunal) | Lun 03/06/2024 | 0 | Hábiles | Sí | 0 | `JUNIO_2024` | Estado `SIN_VENCIMIENTO`, sin fechas | — |
| 8 | Hito sin plazo de gracia | Lun 03/06/2024 | 10 | Hábiles | No | 0 | `JUNIO_2024` | Mar 18/06/2024 | `null` |
| 9 | Prórroga manual +1 | Lun 03/06/2024 | 10 | Hábiles | Sí | 1 | `JUNIO_2024` | Mié 19/06/2024 | Lun 24/06/2024 |
| 10 | Notificación en sábado (regla R1) | Sáb 01/06/2024 | 3 | Hábiles | Sí | 0 | `VACIO` | Mié 05/06/2024 | Jue 06/06/2024 |
| 11 | Plazo corrido que termina en feriado (regla R2) | Mié 12/06/2024 | 5 | Corridos | Sí | 0 | `JUNIO_2024` | Mar 18/06/2024 | Mié 19/06/2024 |
| 12 | Notificación durante la feria (regla R1) | Mié 17/07/2024 | 3 | Hábiles | Sí | 0 | `FERIA_INVIERNO_2024` | Mié 31/07/2024 | Jue 01/08/2024 |

Casos de error de validación (deben rechazarse sin calcular): `fecha_notificacion` vacía, `plazo_valor = -1`, `dias_prorroga_manual = -1`, `plazo_valor = 366`.

### 5.3 Desarrollo de los casos clave

**Caso 1 vs. Caso 2.** Con el mismo Día Cero y plazo, la única diferencia es el feriado del lunes 17/06. Sin feriados se cuentan 4, 5, 6, 7, 10, 11, 12, 13, 14 y 17 de junio: vence el lunes 17. Con el 17 inhábil, el décimo día pasa al martes 18. *Este par reemplaza al ejemplo original, que se titulaba "sin feriados" pero salteaba el 17/06.*

**Caso 3b.** El vencimiento es el miércoles 27/03. El día hábil siguiente no es el jueves 28 (inhábil), ni el viernes 29 (inhábil), ni el fin de semana: es el lunes 01/04. El martes 02/04 también es inhábil, pero no influye porque la gracia ya cayó el lunes.

**Caso 4.** Día 1: viernes 12/07. Del sábado 13 al domingo 28 el reloj se congela. Días 2 a 5: lunes 29, martes 30, miércoles 31 de julio y jueves 1 de agosto.

**Caso 5.** Días 1 a 6: 23, 24, 26, 27, 30 y 31 de diciembre (el 25 es feriado). Enero completo es feria. Días 7 a 10: 3, 4, 5 y 6 de febrero de 2025. *Verifica que el motor use el calendario de más de un año.*

**Caso 9.** Con 11 días en total, el vencimiento pasa al miércoles 19/06. La gracia saltea el 20 y el 21 (inhábiles) y el fin de semana, y cae el lunes 24/06.

**Caso 11.** Corridos desde el jueves 13: 13, 14, 15, 16 y 17 de junio. El 17 es inhábil, así que el vencimiento se traslada al martes 18.

---

## 6. Consideraciones Técnicas Críticas (Para Desarrolladores)

1.  **Zonas Horarias (Timezones):** No depender de la zona horaria del servidor ni de la JVM. Los días se manejan como fechas sin hora (`LocalDate` en Java, columna `date` en PostgreSQL). La hora de fin de gracia se construye explícitamente en `America/Argentina/Buenos_Aires` (`ZonedDateTime.of(dia, LocalTime.NOON, ZoneId.of("America/Argentina/Buenos_Aires"))`) y se guarda como `timestamptz`. Si se construyera "12:00" en UTC, la app mostraría las 09:00 en Argentina.
2.  **Estructura de la Tabla Feriados:** No utilizar una API de feriados genérica (porque no tienen las ferias judiciales ni los días del empleado judicial). Se usa la tabla propia `holidays_calendar` (ver modelo de datos), con alcance (nacional, provincial, departamento judicial o estudio), tipo (feriado, feria, asueto, inhábil manual) y la acordada de referencia. El equipo de operaciones debe poblarla a principio de cada año, actualizar `cubierto_hasta` (columna `calendar_coverage.covered_until`) solo cuando el año está completo y validado, y cargar las acordadas extraordinarias apenas se publican.
3.  **Botón de Prórroga (+1 día):** Si el abogado usa el botón de emergencia por asueto imprevisto, el sistema incrementa en 1 `dias_prorroga_manual` y recalcula. Cada uso queda registrado en la auditoría del caso (quién, cuándo y motivo).
4.  **Recálculo:** si cambia el calendario (por ejemplo, la SCBA declara un asueto nuevo), el backend recalcula los vencimientos pendientes afectados y avisa al usuario de cada fecha que cambió.
5.  **Módulo aislado:** el motor es una función pura (sin acceso a base de datos ni reloj del sistema). El calendario se le pasa como parámetro. Esto permite testear todos los casos de la sección 5 sin infraestructura.
