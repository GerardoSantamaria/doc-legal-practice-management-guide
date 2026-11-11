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
*   **Vencimiento tipado:** un plazo no tiene una sola fecha, sino tres valores:
    *   **Vencimiento nominal:** el último día que sale del cómputo. Es la fecha contra la que alerta la app.
    *   **Límite ordinario:** el vencimiento efectivo a la hora límite que corresponde al hito. El vencimiento efectivo coincide con el nominal, salvo cuando un plazo corrido termina en un día inhábil (regla R2).
    *   **Límite con gracia:** el día hábil siguiente a la hora de fin de gracia, si el hito la admite.

    La UI muestra los dos límites: "Vence hoy a las 14:00. Si no llegás, tenés hasta mañana a las 12:00 (plazo de gracia)".
*   **Tipo de límite horario** (por hito):
    *   `CIERRE_HORARIO_JUDICIAL`: hasta el cierre del horario judicial. Es el valor por defecto para los plazos procesales.
    *   `FIN_DEL_DIA`: hasta las 24:00 del día. Aplica a plazos de derecho de fondo, como la prescripción.
    *   Los plazos en `HORAS` y los de `FECHA_FIJADA` (audiencias) no usan tipo de límite: su límite es un instante (la hora en que se cumplen las horas, o la hora del acto).
*   **Horario configurable:** la hora de cierre (14:00), la hora de fin de gracia (12:00) y la zona horaria son datos de la jurisdicción (tabla `jurisdiction_schedules` del modelo), no constantes del código. Si la SCBA cambia el horario, se publica una configuración nueva con fecha de vigencia.

---

## 2. Variables del Motor de Cálculo

### Tipos de plazo

| Tipo | Inicio (lo carga el abogado) | Cómputo | Gracia | Prórroga | Regla |
| ----- | ----- | ----- | ----- | ----- | ----- |
| `HABILES_JUDICIALES` | Fecha de notificación (Día Cero) | N días hábiles judiciales, desde el hábil siguiente al Día Cero | Si el hito la admite | Sí | R1 |
| `CORRIDOS` | Día Cero | N días calendario. Si el último es inhábil, el efectivo es el hábil siguiente | Si el hito la admite | Sí | R2 |
| `HABILES_ADMINISTRATIVOS` | Día Cero (ej. recepción del telegrama) | N días de lunes a viernes, sin feriados nacionales ni provinciales. Las ferias y los asuetos judiciales **no** son inhábiles para este tipo | No | Sí | R6 |
| `MESES` / `ANIOS` | Fecha del hecho (ej. la extinción del vínculo) | Fecha a fecha (CCyC art. 6): el mismo número de día; si ese mes no lo tiene, el último día del mes. Si cae en inhábil, el efectivo es el hábil judicial siguiente | Si el hito la admite | No | R7 |
| `HORAS` | Fecha **y hora** del disparador | N horas corridas desde ese instante | No | No | R8 |
| `FECHA_FIJADA` | Fecha y hora del acto (ej. la audiencia) | Sin cómputo: el límite es el instante del acto. Advierte si cae en un día inhábil | No | No | — |
| `ANTICIPACION_HABILES_JUDICIALES` | Fecha del acto de referencia (ej. la audiencia) | Hacia atrás: deja N días hábiles judiciales libres antes del acto; el límite es el hábil anterior a esos N días | No | No | R9 |
| `SIN_PLAZO` | — | Sin vencimiento ("Esperando resolución") | No | No | — |

**Por qué `MESES` y `ANIOS` no se bloquean sin calendario:** la prescripción de 2 años siempre cae más allá del calendario cargado. Si se bloqueara con `CALENDARIO_NO_CARGADO`, la app no mostraría el vencimiento más caro de perder. Como el nominal es pura aritmética de fechas y el efectivo nunca es anterior al nominal, el motor devuelve el nominal como efectivo y marca `calendario_incompleto = true`. Se recalcula cuando se carga el calendario de ese año.

### Inputs (Entradas de la función)
1.  `plazo_tipo` (Enum): uno de los de la tabla anterior.
2.  `inicio` (obligatorio salvo `SIN_PLAZO`): `Date` para todos los tipos, salvo `HORAS` y `FECHA_FIJADA`, que usan `DateTime` con zona horaria. Ver la tabla anterior.
3.  `plazo_valor` (Integer, `>= 0`): cantidad de días, horas, meses o años (Ej: 10). Es `0` para `SIN_PLAZO` y `FECHA_FIJADA`. *Este valor viene de la matriz procesal, pero puede ser sobrescrito por el usuario.*
4.  `aplica_gracia` (Boolean): viene del hito de la matriz. Solo se admite en los tipos marcados en la tabla.
5.  `dias_prorroga_manual` (Integer, `>= 0`, default 0): Días extra sumados por asuetos imprevistos. Solo para plazos en días.
6.  `tipo_limite_horario` (Enum): `CIERRE_HORARIO_JUDICIAL` (default) o `FIN_DEL_DIA`. Viene del hito de la matriz. No aplica a `HORAS` ni a `FECHA_FIJADA`, cuyo límite es un instante.
7.  `horario` (Objeto): configuración vigente de la jurisdicción del expediente, con `hora_cierre` (14:00), `hora_fin_gracia` (12:00) y `zona_horaria` (`America/Argentina/Buenos_Aires`).
8.  `calendario` (Objeto): construido por el backend para el expediente, con:
    *   `inhabiles` (Set of Dates): unión de feriados, ferias, asuetos del departamento judicial del expediente, inhábiles manuales del estudio y suspensiones del expediente.
    *   `inhabiles_administrativos` (Set of Dates): solo los feriados nacionales y provinciales (`holidays_calendar.type = FERIADO`). Se usa en `HABILES_ADMINISTRATIVOS`.
    *   `cubierto_hasta` (Date): último día para el cual el calendario está cargado.
    *   `estado` (Enum): `OFICIAL` (calendario completo y validado) o `PROVISORIO` (fase inicial: solo se excluyen sábados y domingos, más lo que se haya cargado). Ver la sección 6.

El backend rechaza la entrada (error de validación) si:

* falta `inicio`;
* algún entero es negativo, o `plazo_valor` supera el máximo de su tipo (`MAX_VALOR`);
* hay gracia en un tipo que no la admite, o prórroga en un plazo que no es en días.

### Outputs (Salidas de la función)
1.  `estado` (Enum):
    *   `CALCULADO`: hay vencimiento.
    *   `SIN_VENCIMIENTO`: plazo 0. La UI muestra "Esperando resolución".
    *   `CALENDARIO_NO_CARGADO`: el cómputo llega a una fecha posterior a `cubierto_hasta`. **No se devuelve ninguna fecha**; la UI muestra una alerta bloqueante.
2.  `vencimiento_nominal` (Date): último día del cómputo. La app alerta contra esta fecha.
3.  `vencimiento_efectivo` (Date): día en que todavía se puede cumplir el acto. Igual al nominal, salvo en plazos corridos, en meses o en años que terminan en inhábil (reglas R2 y R7).
4.  `limite_ordinario` (DateTime con zona horaria): `vencimiento_efectivo` a `hora_cierre`. Con `FIN_DEL_DIA` es las 00:00 del día siguiente, y un acto está en término si ocurre **antes** de ese instante.
5.  `limite_con_gracia` (DateTime con zona horaria, nullable): día hábil posterior al `vencimiento_efectivo`, a `hora_fin_gracia`. Es `null` si `aplica_gracia = NO`.
6.  `calendario_provisorio` (Boolean): `true` si se calculó con un calendario `PROVISORIO`. La UI muestra "Cálculo aproximado: no considera feriados ni ferias".
7.  `calendario_incompleto` (Boolean): `true` si un plazo en meses o años vence después de `cubierto_hasta`. La UI muestra "Vencimiento a confirmar cuando se cargue el calendario de ese año".
8.  `advertencias` (List of Enum): por ejemplo `FECHA_EN_DIA_INHABIL`, cuando una fecha fijada cae en un día inhábil. No bloquean el cálculo.
9.  `dias_computados` (List of Dates): los días que se contaron, en orden. Permite que la UI explique "por qué vence ese día" y facilita la auditoría.

---

## 3. Lógica del Algoritmo (Pseudocódigo)

```text
CONSTANTES
    MAX_VALOR = { días: 365, HORAS: 720, MESES: 120, ANIOS: 10 }   // corte de validación
    CON_GRACIA   = { HABILES_JUDICIALES, CORRIDOS, MESES, ANIOS }
    CON_PRORROGA = { HABILES_JUDICIALES, HABILES_ADMINISTRATIVOS, CORRIDOS }
    // Las horas y la zona horaria vienen en `horario` (configuración de la jurisdicción).

Función EsInhabil(fecha, inhabiles, calendario) {
    Si (fecha > calendario.cubierto_hasta) {
        Lanzar CalendarioNoCargado(fecha)
    }
    Retornar (fecha ES Sábado) O (fecha ES Domingo) O (fecha ESTÁ EN inhabiles)
}

Función SiguienteHabil(fecha, calendario) {
    siguiente = fecha + 1 día
    Mientras (EsInhabil(siguiente, calendario.inhabiles, calendario)) {
        siguiente = siguiente + 1 día
    }
    Retornar siguiente
}

Función AnteriorHabil(fecha, calendario) {
    anterior = fecha - 1 día
    Mientras (EsInhabil(anterior, calendario.inhabiles, calendario)) {
        anterior = anterior - 1 día
    }
    Retornar anterior
}

Función ContarHabiles(desde, total, inhabiles, calendario, dias_computados) {
    // Regla R1 (a validar): si el Día Cero es inhábil, se cuenta igual
    // desde el siguiente hábil. Es la interpretación más temprana.
    fecha = desde
    Mientras (largo(dias_computados) < total) {
        fecha = fecha + 1 día
        Si (NO EsInhabil(fecha, inhabiles, calendario)) {
            Agregar fecha a dias_computados
        }
    }
    Retornar fecha
}

Función SumarMeses(fecha, meses) {
    // CCyC art. 6: fecha a fecha; si el mes de destino no tiene ese día, el último del mes.
    destino = mes y año de (fecha + meses meses)
    Retornar día min(fecha.día, último_día(destino)) de destino
}

Función Limite(dia, tipo_limite_horario, horario) {
    Si (tipo_limite_horario == FIN_DEL_DIA) {
        Retornar CrearFechaHora(dia + 1 día, 00:00, horario.zona_horaria)   // exclusivo
    }
    Retornar CrearFechaHora(dia, horario.hora_cierre, horario.zona_horaria)
}

Función CalcularVencimiento(plazo_tipo, inicio, plazo_valor, aplica_gracia,
                            dias_prorroga_manual, tipo_limite_horario, horario, calendario) {

    // 1. Validar entradas (rechazar antes de calcular)
    Validar inicio != null (salvo SIN_PLAZO)
    Validar plazo_valor >= 0 Y dias_prorroga_manual >= 0
    Validar plazo_valor <= MAX_VALOR del tipo
    Validar NO aplica_gracia O plazo_tipo EN CON_GRACIA
    Validar dias_prorroga_manual == 0 O plazo_tipo EN CON_PRORROGA
    total = plazo_valor + dias_prorroga_manual

    // 2. Sin plazo: depende del tribunal, no hay vencimiento
    Si (plazo_tipo == SIN_PLAZO O (plazo_tipo != FECHA_FIJADA Y total == 0)) {
        Retornar { estado: SIN_VENCIMIENTO }
    }

    resultado = { estado: CALCULADO, limite_con_gracia: null, advertencias: [],
                  calendario_provisorio: (calendario.estado == PROVISORIO),
                  calendario_incompleto: false, dias_computados: [] }

    Intentar {
        // 3. Tipos cuyo límite es un instante
        Si (plazo_tipo == HORAS) {
            // Regla R8 (a validar): horas corridas desde el instante del disparador.
            instante = inicio + total horas
            Retornar resultado + { vencimiento_nominal: fecha(instante),
                                   vencimiento_efectivo: fecha(instante),
                                   limite_ordinario: instante }
        }
        Si (plazo_tipo == FECHA_FIJADA) {
            Si (EsInhabil(fecha(inicio), calendario.inhabiles, calendario)) {
                Agregar FECHA_EN_DIA_INHABIL a resultado.advertencias
            }
            Retornar resultado + { vencimiento_nominal: fecha(inicio),
                                   vencimiento_efectivo: fecha(inicio),
                                   limite_ordinario: inicio }
        }

        // 4. Plazo hacia atrás desde un acto fijado
        Si (plazo_tipo == ANTICIPACION_HABILES_JUDICIALES) {
            // Regla R9 (a validar): los N días hábiles anteriores al acto quedan
            // libres y el acto se cumple, a más tardar, el hábil anterior a ellos.
            libre = inicio
            Repetir total veces {
                libre = AnteriorHabil(libre, calendario)
                Agregar libre a resultado.dias_computados
            }
            dia = AnteriorHabil(libre, calendario)
            Retornar resultado + { vencimiento_nominal: dia, vencimiento_efectivo: dia,
                                   limite_ordinario: Limite(dia, tipo_limite_horario, horario) }
        }

        // 5. Cómputo hacia adelante
        Si (plazo_tipo == HABILES_JUDICIALES) {
            nominal = ContarHabiles(inicio, total, calendario.inhabiles, calendario,
                                    resultado.dias_computados)
            efectivo = nominal
        }
        Si (plazo_tipo == HABILES_ADMINISTRATIVOS) {
            // Regla R6 (a validar): solo feriados; las ferias judiciales no suspenden.
            nominal = ContarHabiles(inicio, total, calendario.inhabiles_administrativos,
                                    calendario, resultado.dias_computados)
            efectivo = nominal
        }
        Si (plazo_tipo == CORRIDOS) {
            // Se cuentan todos los días calendario desde el día siguiente al Día Cero.
            nominal = inicio + total días
            efectivo = nominal
            // Regla R2 (a validar): si el último día es inhábil, el acto se puede
            // cumplir el siguiente hábil. La alerta sigue siendo el nominal.
            Si (EsInhabil(nominal, calendario.inhabiles, calendario)) {
                efectivo = SiguienteHabil(nominal, calendario)
            }
            resultado.dias_computados = días calendario entre (inicio + 1) y nominal
        }
        Si (plazo_tipo EN { MESES, ANIOS }) {
            nominal = SumarMeses(inicio, total × (12 si ANIOS, 1 si MESES))
            Si (nominal > calendario.cubierto_hasta) {
                // No se bloquea: el nominal es la fecha más temprana posible.
                Retornar resultado + { vencimiento_nominal: nominal, vencimiento_efectivo: nominal,
                                       limite_ordinario: Limite(nominal, tipo_limite_horario, horario),
                                       calendario_incompleto: true }
            }
            efectivo = nominal
            // Regla R7 (a validar): igual que R2.
            Si (EsInhabil(nominal, calendario.inhabiles, calendario)) {
                efectivo = SiguienteHabil(nominal, calendario)
            }
        }

        // 6. Límites horarios
        resultado.vencimiento_nominal  = nominal
        resultado.vencimiento_efectivo = efectivo
        resultado.limite_ordinario     = Limite(efectivo, tipo_limite_horario, horario)

        // 7. Plazo de gracia (solo si el hito lo admite)
        Si (aplica_gracia) {
            dia_gracia = SiguienteHabil(efectivo, calendario)
            resultado.limite_con_gracia = CrearFechaHora(dia_gracia, horario.hora_fin_gracia,
                                                         horario.zona_horaria)
        }
        Retornar resultado
    }
    Capturar (CalendarioNoCargado) {
        Retornar { estado: CALENDARIO_NO_CARGADO }
    }
}
```

**Por qué los bucles terminan siempre:** `total` está acotado por `MAX_VALOR` y cada iteración avanza (o retrocede) un día calendario. Si el calendario no cubre el rango, `EsInhabil` corta con `CalendarioNoCargado` en lugar de seguir avanzando.

---

## 4. Reglas pendientes de validación jurídica

El motor ya implementa una interpretación por defecto (la más temprana). El equipo legal debe confirmar o corregir cada una antes del lanzamiento; están en la hoja `Dudas_a_validar` de la matriz como D26 a D34. Gracias al vencimiento tipado (sección 1), ninguna respuesta cambia la estructura del motor: a lo sumo cambia un parámetro o una rama del cómputo. Cada regla tiene su propio caso de prueba.

| Regla | Pregunta | Opciones | Comportamiento del motor (recomendado) | Duda | Caso |
| ----- | ----- | ----- | ----- | ----- | ----- |
| R1 | Si la notificación ocurre en día inhábil (sábado, feriado, feria), ¿desde cuándo corre el plazo? | (a) El Día Uno es el primer hábil posterior, sin mover la notificación. (b) Se tiene por notificado el siguiente hábil y el Día Uno es el hábil posterior a ese, un día más tarde. | (a), la más temprana. | D26 | 10, 12 |
| R2 | En plazos corridos, si el último día es inhábil, ¿se traslada al siguiente hábil? | (a) No se traslada. (b) Se traslada. | Se calculan las dos: el **nominal** es el día inhábil y la app alerta contra él; el **efectivo** es el hábil siguiente y define los límites. Si la respuesta es (a), el efectivo pasa a ser igual al nominal. | D27 | 11 |
| R3 | ¿Cuál es la hora límite del vencimiento ordinario? ¿Cómo interactúa con el plazo de gracia y con la presentación electrónica fuera de horario? | La hora es un parámetro de la jurisdicción y el tipo de límite es un dato del hito, así que cualquier respuesta se resuelve con configuración. | `CIERRE_HORARIO_JUDICIAL` a las 14:00, y gracia hasta las 12:00 del hábil siguiente. `FIN_DEL_DIA` para la prescripción. Lectura a validar: una presentación electrónica fuera de horario el día del vencimiento se tiene por hecha en el horario hábil siguiente, es decir, dentro de la gracia. | D28 | 13 |
| R4 | ¿Jueves Santo, el 24/12 y el 31/12 son inhábiles judiciales en PBA? (Dependen de lo que declare la SCBA cada año.) | (a) Se cargan siempre. (b) Se cargan solo si hay acordada. | (b). El motor no tiene ninguna fecha fija en el código: el calendario es la fuente, y lo carga el equipo. | D29 | 3b |
| R5 | La forma de notificación (cédula, electrónica, ministerio de la ley los martes y viernes, art. 133 CPCCBA) cambia el Día Cero. ¿La app lo calcula o lo ingresa el abogado? | (a) Lo ingresa el abogado. (b) La app lo calcula. (c) La app lo sugiere y el abogado confirma. | V1: (a). El abogado carga la fecha ya perfeccionada y la forma (`notification_type`). V1.x: (c) para la notificación electrónica. La fecha nunca se calcula sin confirmación del abogado. | D30 | — |
| R6 | En días hábiles administrativos (LCT, Dec. 146/01), ¿qué días son inhábiles? ¿Las ferias judiciales suspenden? ¿Los días no laborables cuentan? | (a) Solo sábados, domingos y feriados. (b) Además, los días no laborables. (c) Además, las ferias. | (a): es la que menos días excluye, así que da el vencimiento más temprano. | D31 (y D06) | 15, 16 |
| R7 | En meses o años (prescripción), si el último día es inhábil, ¿se puede cumplir el hábil siguiente? ¿Aplica el plazo de gracia? ¿Vence a las 24:00? | Igual que R2, más el tipo de límite y la gracia del hito. | Nominal fecha a fecha (CCyC art. 6, a validar) como fecha de alerta; efectivo el hábil siguiente; límite `FIN_DEL_DIA`; gracia según el hito (hoy `NO` en `LAB_015`). | D32 (y D04) | 17, 18, 19 |
| R8 | En plazos en horas, ¿se cuentan corridas? ¿Desde el instante exacto o desde la hora siguiente? ¿Qué pasa si terminan en un día inhábil? | (a) Corridas desde el instante. (b) Desde la hora siguiente. (c) Se trasladan al hábil siguiente. | (a), sin traslado: es la opción más temprana. Si el abogado no sabe la hora, la UI propone las 00:00 del día. | D33 | 20 |
| R9 | En plazos de anticipación (ej. citar testigos N días antes de la audiencia), ¿los N días tienen que quedar libres entre el acto y la audiencia, o el último día del cómputo ya sirve? | (a) N días libres: el límite es el hábil anterior a ellos. (b) El N-ésimo día hábil anterior es el límite. | (a), un día antes que (b). | D34 (y D13) | 22, 23 |

---

## 5. Casos de Prueba (Test Cases)

Los tests **no dependen del calendario real**: cada caso declara su propio calendario de prueba (*fixture*). Así un test no falla porque alguien cargó o borró un feriado en la base. La carga y validación del calendario real 2027–2028 es una tarea aparte, a cargo del equipo (ver la sección 6).

La implementación de referencia en `herramientas/motor_plazos_referencia.py` reproduce todos los casos y falla si alguno no da el resultado esperado.

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

Para `HABILES_ADMINISTRATIVOS` solo cuentan los feriados de cada fixture: los de `JUNIO_2024` sí; la feria de `FERIA_INVIERNO_2024` no.

### 5.2 Casos

Salvo indicación:

* el tipo de límite es `CIERRE_HORARIO_JUDICIAL` y el horario es el de PBA (cierre 14:00, fin de gracia 12:00, hora de Argentina);
* el calendario está en estado `OFICIAL`;
* el vencimiento nominal coincide con el efectivo, salvo en los casos 11 (nominal lun 17/06/2024) y 18 (ver la columna).

La columna "Vencimiento efectivo esperado" es el día del límite ordinario, a las 14:00.

| # | Qué prueba | Día Cero | Plazo | Tipo | Gracia | Prórroga | Fixture | Vencimiento efectivo esperado | Fin de gracia esperado |
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
| 13 | Límite `FIN_DEL_DIA` (regla R3) | Lun 03/06/2024 | 10 | Hábiles | No | 0 | `JUNIO_2024` | Mar 18/06/2024; límite ordinario: antes del mié 19/06/2024 00:00 | `null` |
| 14 | Calendario `PROVISORIO` | Lun 03/06/2024 | 10 | Hábiles | Sí | 0 | `VACIO` | Lun 17/06/2024, con `calendario_provisorio = true` | Mar 18/06/2024 |
| 15 | Hábiles administrativos: la feria no suspende (regla R6) | Jue 11/07/2024 | 2 | Hábiles adm. | No | 0 | `FERIA_INVIERNO_2024` | Lun 15/07/2024 (en hábiles judiciales sería el 29/07) | `null` |
| 16 | Hábiles administrativos con feriado (regla R6) | Vie 14/06/2024 | 2 | Hábiles adm. | No | 0 | `JUNIO_2024` (feriados) | Mié 19/06/2024 | `null` |
| 17 | Meses, fin de mes sin día equivalente (regla R7) | Vie 31/01/2025 | 1 | Meses | No | — | `VACIO` | Vie 28/02/2025 | `null` |
| 18 | Años desde un 29/02 y fin de semana (regla R7) | Jue 29/02/2024 | 2 | Años, `FIN_DEL_DIA` | No | — | `VACIO`, cubierto hasta 31/12/2026 | Nominal sáb 28/02/2026; efectivo lun 02/03/2026, límite antes del mar 03/03/2026 00:00 | `null` |
| 19 | Años sin calendario del año de vencimiento | Jue 29/02/2024 | 2 | Años, `FIN_DEL_DIA` | No | — | `VACIO` | Sáb 28/02/2026 (nominal = efectivo), con `calendario_incompleto = true` | `null` |
| 20 | Horas corridas que terminan en fin de semana (regla R8) | Vie 07/06/2024 10:30 | 48 | Horas | No | — | `VACIO` | Límite dom 09/06/2024 10:30 | `null` |
| 21 | Fecha fijada en un día inhábil | Lun 17/06/2024 09:00 | 0 | Fecha fijada | No | — | `JUNIO_2024` | Límite lun 17/06/2024 09:00, con la advertencia `FECHA_EN_DIA_INHABIL` | `null` |
| 22 | Anticipación de 3 días hábiles (regla R9) | Audiencia mié 12/06/2024 | 3 | Anticipación | No | — | `VACIO` | Jue 06/06/2024 | `null` |
| 23 | Anticipación con feriados en el medio (regla R9) | Audiencia lun 24/06/2024 | 3 | Anticipación | No | — | `JUNIO_2024` | Jue 13/06/2024 | `null` |

Casos de error de validación (deben rechazarse sin calcular): `inicio` vacío, `plazo_valor = -1`, `dias_prorroga_manual = -1`, `plazo_valor = 366` en días, gracia en un plazo en horas y prórroga en un plazo en meses.

### 5.3 Desarrollo de los casos clave

**Caso 1 vs. Caso 2.** Con el mismo Día Cero y plazo, la única diferencia es el feriado del lunes 17/06. Sin feriados se cuentan 4, 5, 6, 7, 10, 11, 12, 13, 14 y 17 de junio: vence el lunes 17. Con el 17 inhábil, el décimo día pasa al martes 18. *Este par reemplaza al ejemplo original, que se titulaba "sin feriados" pero salteaba el 17/06.*

**Caso 3b.** El vencimiento es el miércoles 27/03. El día hábil siguiente no es el jueves 28 (inhábil), ni el viernes 29 (inhábil), ni el fin de semana: es el lunes 01/04. El martes 02/04 también es inhábil, pero no influye porque la gracia ya cayó el lunes.

**Caso 4.** Día 1: viernes 12/07. Del sábado 13 al domingo 28 el reloj se congela. Días 2 a 5: lunes 29, martes 30, miércoles 31 de julio y jueves 1 de agosto.

**Caso 5.** Días 1 a 6: 23, 24, 26, 27, 30 y 31 de diciembre (el 25 es feriado). Enero completo es feria. Días 7 a 10: 3, 4, 5 y 6 de febrero de 2025. *Verifica que el motor use el calendario de más de un año.*

**Caso 9.** Con 11 días en total, el vencimiento pasa al miércoles 19/06. La gracia saltea el 20 y el 21 (inhábiles) y el fin de semana, y cae el lunes 24/06.

**Caso 15 vs. caso 4.** Los dos tienen la feria de invierno en el medio. En hábiles judiciales el reloj se congela; en hábiles administrativos no: los días 1 y 2 son el viernes 12 y el lunes 15 de julio.

**Caso 18.** Dos años desde el 29/02/2024 dan el 29/02/2026, que no existe: el plazo vence el último día de febrero, sábado 28. El efectivo es el lunes 02/03 y, con `FIN_DEL_DIA`, el acto está en término si se cumple antes de las 00:00 del martes 03/03. El caso 19 es el mismo plazo sin el calendario de 2026: no se bloquea, devuelve el sábado 28 y lo marca como incompleto.

**Caso 22.** Con la audiencia el miércoles 12, los tres días hábiles libres son el martes 11, el lunes 10 y el viernes 7. El acto se cumple, a más tardar, el jueves 6. En el caso 23, los feriados del 17, 20 y 21 corren los tres días libres al 19, 18 y 14, y el límite queda el jueves 13.

**Caso 11.** Corridos desde el jueves 13: 13, 14, 15, 16 y 17 de junio. El vencimiento nominal es el lunes 17, que es inhábil: la app alerta contra ese día. El efectivo se traslada al martes 18 (límite ordinario a las 14:00) y la gracia cae el miércoles 19 a las 12:00.

---

## 6. Consideraciones Técnicas Críticas (Para Desarrolladores)

1.  **Zonas Horarias (Timezones):** No depender de la zona horaria del servidor ni de la JVM. Los días se manejan como fechas sin hora (`LocalDate` en Java, columna `date` en PostgreSQL). Los límites (cierre, fin de gracia) se construyen explícitamente en la zona horaria de la jurisdicción (`ZonedDateTime.of(dia, horario.horaFinGracia(), horario.zonaHoraria())`) y se guardan como `timestamptz`. Si se construyera "12:00" en UTC, la app mostraría las 09:00 en Argentina.
2.  **Estructura de la Tabla Feriados:** No utilizar una API de feriados genérica (porque no tienen las ferias judiciales ni los días del empleado judicial). Se usa la tabla propia `holidays_calendar` (ver modelo de datos), con alcance (nacional, provincial, departamento judicial o estudio), tipo (feriado, feria, asueto, inhábil manual) y la acordada de referencia. El equipo debe poblarla a principio de cada año, pasar el calendario a `OFICIAL` (columna `calendar_coverage.status`) y actualizar `cubierto_hasta` (`calendar_coverage.covered_until`) solo cuando el año está completo y validado, y cargar las acordadas extraordinarias apenas se publican.
3.  **Calendario provisorio (fases iniciales):** mientras el equipo arma el calendario 2027–2028, se trabaja con `calendar_coverage.status = PROVISORIO`: solo se excluyen sábados y domingos, más lo que ya se haya cargado. El motor es el mismo, solo cambia el dato.
    *   **El error va hacia el lado seguro:** un feriado no cargado se cuenta como hábil, así que el vencimiento calculado queda **antes** que el real, nunca después.
    *   **Puede ser grande:** con la feria de enero, un plazo notificado a fines de diciembre da a principios de enero cuando el real es en febrero. Sirve para desarrollo y pruebas internas, no para usuarios reales.
    *   **Siempre visible:** con `PROVISORIO`, el motor devuelve `calendario_provisorio = true` y la UI muestra "Cálculo aproximado: no considera feriados ni ferias" en cada vencimiento.
    *   **Prioridad de carga:** primero los feriados nacionales y las dos ferias (poco trabajo y la mayor fuente de error), después los asuetos por departamento y los inhábiles variables (regla R4). Si se prueba con casos reales antes de 2027, hace falta cargar también diciembre de 2026, porque esos plazos cruzan la feria de enero.
    *   **Paso a producción:** con usuarios reales, el calendario de todo el rango usado tiene que estar en `OFICIAL`.
4.  **Botón de Prórroga (+1 día):** Si el abogado usa el botón de emergencia por asueto imprevisto, el sistema incrementa en 1 `dias_prorroga_manual` y recalcula. Cada uso queda registrado en la auditoría del caso (quién, cuándo y motivo).
5.  **Recálculo:** si cambia el calendario (por ejemplo, la SCBA declara un asueto nuevo, o el calendario pasa de `PROVISORIO` a `OFICIAL`), el backend recalcula los vencimientos pendientes afectados y avisa al usuario de cada fecha que cambió.
6.  **Módulo aislado:** el motor es una función pura (sin acceso a base de datos ni reloj del sistema). El calendario y el horario se le pasan como parámetros. Esto permite testear todos los casos de la sección 5 sin infraestructura.
