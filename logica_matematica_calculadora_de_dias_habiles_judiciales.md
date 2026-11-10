# Lógica Matemática: Calculadora de Días Hábiles Judiciales (PBA)

Este documento define la lógica algorítmica que debe seguir el backend/frontend para calcular correctamente los vencimientos legales en la Provincia de Buenos Aires, evitando errores de mala praxis.

---

## 1. Conceptos Fundamentales

Para que el algoritmo funcione, los desarrolladores deben entender estas reglas del derecho procesal:

*   **Evento Disparador (Día Cero):** Es el día en que el abogado queda notificado (ej. recibe una cédula o es día de nota). **El plazo no comienza a correr ese día**.
*   **Inicio del Cómputo (Día Uno):** El plazo procesal comienza a correr a partir del **siguiente día hábil judicial** posterior al Día Cero.
*   **Día Hábil Judicial:** De Lunes a Viernes. Se excluyen sábados, domingos, feriados nacionales, provinciales inamovibles y ferias judiciales (Enero completo y dos semanas de Julio).
*   **Plazo de Gracia (Art. 124 CPCCBA):** El vencimiento final se extiende hasta las **primeras cuatro (4) horas hábiles del día hábil posterior** al vencimiento ordinario. En PBA, el horario judicial es de 08:00 a 14:00, por lo que el plazo de gracia finaliza a las **12:00 AM**.

---

## 2. Variables del Motor de Cálculo

### Inputs (Entradas de la función)
1.  `fecha_notificacion` (Date): Fecha ingresada por el usuario (Día Cero).
2.  `plazo_dias` (Integer): Cantidad de días de plazo (Ej: 10). *Este valor viene de la matriz procesal, pero puede ser sobrescrito por el usuario.*
3.  `dias_prorroga_manual` (Integer): Días extra sumados por asuetos imprevistos (Default: 0).
4.  `feriados_db` (Array of Dates): Lista consultada a la base de datos con todos los feriados y ferias del año.

### Outputs (Salidas de la función)
1.  `fecha_vencimiento_ordinario` (Date): Día en que se cumplen los `plazo_dias`.
2.  `fecha_plazo_gracia` (DateTime): Día hábil posterior a las 12:00 horas.

---

## 3. Lógica del Algoritmo (Pseudocódigo)

El algoritmo requiere un bucle (`while`) que avance día por día evaluando si el día calendario es válido para descontarlo del plazo.

```javascript
Función CalcularVencimiento(fecha_notificacion, plazo_dias + dias_prorroga_manual) {
    
    // 1. Inicializar variables
    dias_contados = 0
    fecha_actual = fecha_notificacion
    
    // 2. Bucle principal de conteo
    Mientras (dias_contados < plazo_dias) {
        
        // Sumar un día calendario
        fecha_actual = fecha_actual + 1 día
        
        // Verificar si es día hábil
        Si (fecha_actual NO ES Sábado) Y 
           (fecha_actual NO ES Domingo) Y 
           (fecha_actual NO ESTÁ EN feriados_db) {
               
               // Es un día hábil judicial válido, sumamos al contador
               dias_contados = dias_contados + 1
        }
    }
    
    fecha_vencimiento_ordinario = fecha_actual
    
    // 3. Calcular Plazo de Gracia (Buscar el Siguiente Día Hábil)
    fecha_gracia = fecha_vencimiento_ordinario + 1 día
    
    Mientras (fecha_gracia ES Sábado OR Domingo OR ESTÁ EN feriados_db) {
        fecha_gracia = fecha_gracia + 1 día
    }
    
    // Establecer hora de gracia a las 12:00 PM (hora local de Argentina)
    fecha_gracia = EstablecerHora(fecha_gracia, "12:00:00")
    
    Retornar { fecha_vencimiento_ordinario, fecha_gracia }
}
```

---

## 4. Ejemplos Prácticos de Validación (Test Cases)

Al momento de programar, los desarrolladores deben correr estas pruebas para asegurar que la lógica no falle.

### Ejemplo 1: Cálculo estándar sin feriados
*   **Regla:** Plazo de 10 días para contestar demanda.
*   **Día Cero:** Lunes 3 de Junio.
*   **Desarrollo:** Empieza a contar el Martes 4. Se cuentan los días (4, 5, 6, 7, 10, 11, 12, 13, 14, 18).
*   **Vencimiento Ordinario:** Martes 18 de Junio a las 23:59hs.
*   **Vencimiento con Gracia:** Miércoles 19 de Junio a las 12:00hs.

### Ejemplo 2: Cruzando un fin de semana largo o feriado
*   **Regla:** Plazo de 5 días para oponer excepciones.
*   **Día Cero:** Miércoles 20 de Marzo.
*   *Feriado:* Domingo 24 de Marzo (Día de la Memoria).
*   **Desarrollo:** Empieza a contar el Jueves 21 (Día 1), Viernes 22 (Día 2). Salta Sábado 23 y Domingo 24. Lunes 25 (Día 3), Martes 26 (Día 4), Miércoles 27 (Día 5).
*   **Vencimiento Ordinario:** Miércoles 27 de Marzo a las 23:59hs.
*   **Vencimiento con Gracia:** Jueves 28 de Marzo a las 12:00hs.

### Ejemplo 3: El limbo de la Feria Judicial (Feria de Invierno)
*   **Regla:** Plazo de 5 días.
*   **Día Cero:** Jueves 11 de Julio.
*   *Feria de Invierno:* Lunes 15 de Julio al Viernes 26 de Julio inclusive.
*   **Desarrollo:**
    *   Día 1: Viernes 12 de Julio.
    *   *Freno del reloj: Del Sábado 13 al Domingo 28 el reloj se congela.*
    *   Día 2: Lunes 29 de Julio.
    *   Día 3: Martes 30 de Julio.
    *   Día 4: Miércoles 31 de Julio.
    *   Día 5: Jueves 1 de Agosto.
*   **Vencimiento Ordinario:** Jueves 1 de Agosto.
*   **Vencimiento con Gracia:** Viernes 2 de Agosto a las 12:00hs.

---

## 5. Consideraciones Técnicas Críticas (Para Desarrolladores)

1.  **Zonas Horarias (Timezones):** Es vital que toda la aplicación, tanto en Base de Datos como en el servidor, esté forzada a trabajar en la zona horaria `America/Argentina/Buenos_Aires` (UTC-3). Si el servidor procesa esto en UTC(0), el plazo de gracia de las 12:00 AM se calculará erróneamente como las 09:00 AM en Argentina.
2.  **Estructura de la Tabla Feriados:** No utilizar una API de feriados genérica (porque no tienen las ferias judiciales ni los días del empleado judicial). Crear una tabla propia (`feriados_judiciales`) con columnas: `fecha` (Date) y `descripcion` (String). El equipo de operaciones debe poblarla a principio de cada año.
3.  **Botón de Prórroga (+1 día):** Si el abogado usa el botón de emergencia por asueto imprevisto, el sistema simplemente incrementa en 1 la variable `dias_prorroga_manual`, lo que prolonga el bucle `while` una iteración más, empujando todo el vencimiento limpiamente.