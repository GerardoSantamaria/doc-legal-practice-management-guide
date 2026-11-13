from comun import (CON_GRACIA, CON_VALOR_CERO, DUDA_MATRIZ_GENERAL, ESTADOS, FASES, GRUPOS, PLAZO_TIPOS, ROLES,
                   etapa_judicial, flujo)

FLUJO = flujo(
    "Reclamos salariales - Provincia de Buenos Aires",
    "Sueldos impagos, diferencias por categoría o convenio, horas extra, comisiones, SAC y vacaciones, con el vínculo "
    "vigente o ya extinguido. Si el trabajador se considera despedido, el expediente sigue en la matriz de despido. "
    "Las citas son orientativas y deben validarse artículo por artículo.",
)

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
PREVIA = [
    ("SAL_010", "Previa", "Crédito salarial impago o pagado de menos", "ACTORA",
     "Detección del crédito (falta de pago, recibo con diferencias o rubro no liquidado)", 0, "SIN_PLAZO", "NO",
     "Arts. 74, 103, 128 y 260 LCT", "SI", "NO",
     ["Identificar cada rubro y período: sueldo, diferencias por categoría o convenio colectivo, horas extra (art. 201 LCT), comisiones (arts. 108 a 111), SAC (arts. 121 y 122), vacaciones (art. 155) y adicionales del convenio",
      "Revisar los recibos (arts. 138 a 146 LCT), el convenio aplicable y sus escalas",
      "Recordar que el pago insuficiente es entrega a cuenta aunque se firme sin reservas (art. 260 LCT)",
      "Registrar si el vínculo sigue vigente",
      "Si hay una rebaja salarial unilateral, evaluar el art. 66 LCT (fuera de este flujo)"],
     ["Recibos de sueldo", "Convenio colectivo y escalas salariales", "Registros de horario o constancias de horas extra",
      "Constancias de comisiones"]),
    ("SAL_012", "Previa", "Pago de la remuneración del período", "DEMANDADA",
     "Vencimiento del período de pago (mes, quincena o semana)", 4, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 128 LCT", "NO", "NO",
     ["Mensual: 4 días hábiles; quincenal o semanal: 3 días hábiles (editar el plazo)",
      "Controlar el recibo del período"],
     ["Recibo del período"]),
    ("SAL_013", "Previa", "Impugnación de la sanción disciplinaria", "ACTORA",
     "Notificación de la sanción", 30, "CORRIDOS", "NO",
     "Arts. 67 y 218 a 224 LCT", "NO", "NO",
     ["Cuestionar por TCL la procedencia, el tipo o la extensión de la sanción",
      "Controlar el tope de 30 días de suspensión por año (art. 220 LCT)",
      "Si es una suspensión, reclamar los salarios de los días suspendidos (art. 223 LCT)"],
     ["Comunicación de la sanción", "TCL de impugnación", "Aviso de entrega del correo"]),
    ("SAL_015", "Previa", "Control de prescripción del crédito más antiguo", "ACTORA",
     "Exigibilidad del crédito más antiguo reclamado", 2, "ANIOS", "NO",
     "Arts. 256 y 257 LCT", "NO", "NO",
     ["Cada período prescribe por separado desde que es exigible: cargar un plazo suelto de prescripción para los períodos próximos a vencer",
      "Considerar la suspensión por reclamo ante la autoridad administrativa (máximo 6 meses, art. 257 LCT)",
      "Interponer el reclamo antes de que prescriban los períodos más antiguos"],
     ["Recibos o constancias de cada período"]),
    ("SAL_017", "Previa", "Acreditación del depósito de aportes retenidos", "DEMANDADA",
     "Recepción por el empleador de la intimación", 30, "CORRIDOS", "NO",
     "Art. 132 bis LCT; art. 1 Dec. 146/01 (verificar vigencia tras la Ley 27.742)", "NO", "NO",
     ["Intimar por TCL que el empleador acredite el ingreso de los aportes retenidos",
      "Controlar los 30 días",
      "Pedir el historial de aportes en ARCA"],
     ["TCL de intimación", "Historial de aportes (ARCA)"]),
    ("SAL_020", "Previa", "Intimación de pago de las diferencias", "DEMANDADA",
     "Recepción por el empleador del telegrama del trabajador", 2, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 57 LCT; Ley 23.789", "NO", "NO",
     ["Detallar en el TCL los rubros, los períodos y los montos reclamados",
      "Intimar bajo apercibimiento: el silencio del empleador es presunción en su contra (art. 57 LCT)",
      "Fijar un plazo no inferior a 2 días hábiles (editar el plazo si se fija uno mayor)"],
     ["TCL (Ley 23.789)", "Aviso de entrega del correo"]),
    ("SAL_040", "Previa", "Instancia de conciliación laboral previa", "ACTORA",
     "Presentación del reclamo ante el organismo de conciliación", 0, "SIN_PLAZO", "NO",
     "A validar: obligatoriedad, organismo y norma según el régimen del departamento", "NO", "NO",
     ["Verificar si la instancia es obligatoria en el departamento judicial",
      "Con el vínculo vigente, hablar con el cliente sobre el riesgo de represalias y documentar cualquier cambio de condiciones",
      "Presentar el reclamo y asistir a las audiencias",
      "Obtener el acta de cierre (acuerdo o fracaso)"],
     ["Formulario de reclamo", "DNI del trabajador", "Poder", "Acta de cierre"]),
]

FINAL_DESPIDO = [
    ("SAL_995", "Cierre", "Despido indirecto: continúa en la matriz de despido", "ACTORA",
     "Comunicación del despido indirecto", 0, "SIN_PLAZO", "NO",
     "Arts. 242 y 246 LCT", "NO", "SI",
     ["Cargar el expediente con el flujo de indemnización por despido, con la comunicación del despido indirecto como hito actual",
      "Reclamar los créditos salariales junto con las indemnizaciones"],
     []),
]

JUDICIAL, TRANSICIONES_JUDICIALES = etapa_judicial("SAL", {
    "SAL_050": {"checklist": [
        "Redactar objeto, hechos, derecho y liquidación por período y rubro, con intereses desde cada vencimiento",
        "Pedir la exhibición del libro del art. 52 LCT, los recibos y los registros de horario, bajo apercibimiento de la presunción del art. 55 LCT",
        "Ofrecer pericia contable sobre los libros del empleador",
        "Ofrecer toda la prueba con la demanda (documental, informativa, testimonial, confesional)",
        "Constituir domicilio electrónico",
        "Presentar ante la Receptoría General de Expedientes del departamento"]},
})

NODOS = PREVIA + JUDICIAL + FINAL_DESPIDO

# origen, condicion, destino ("" = cierra ese camino paralelo)
TRANSICIONES = [
    ("SAL_010", "Sueldo del período todavía no vencido", "SAL_012"),
    ("SAL_010", "Diferencias o rubros adeudados ya exigibles", "SAL_015"),
    ("SAL_010", "Diferencias o rubros adeudados ya exigibles", "SAL_020"),
    ("SAL_010", "Sanción disciplinaria con descuento o suspensión", "SAL_013"),
    ("SAL_010", "Aportes retenidos y no depositados", "SAL_015"),
    ("SAL_010", "Aportes retenidos y no depositados", "SAL_017"),
    ("SAL_010", "Aportes retenidos y no depositados", "SAL_020"),
    ("SAL_012", "Pagado íntegramente", "SAL_990"),
    ("SAL_012", "No pagado o pagado de menos", "SAL_015"),
    ("SAL_012", "No pagado o pagado de menos", "SAL_020"),
    ("SAL_013", "Sanción impugnada en término", "SAL_015"),
    ("SAL_013", "Sanción impugnada en término", "SAL_020"),
    ("SAL_013", "Sanción consentida", "SAL_990"),
    ("SAL_015", "Reclamo interpuesto en término", ""),
    ("SAL_017", "Acredita el depósito", ""),
    ("SAL_017", "No lo acredita: la sanción se reclama en la demanda", ""),
    ("SAL_020", "El empleador paga lo reclamado", "SAL_990"),
    ("SAL_020", "Rechazo o silencio: se reclama con el vínculo vigente o ya extinguido", "SAL_040"),
    ("SAL_020", "Rechazo o silencio: el trabajador se considera despedido", "SAL_995"),
    ("SAL_040", "Acuerdo alcanzado", "SAL_900"),
    ("SAL_040", "Fracaso de la conciliación o instancia no exigida", "SAL_050"),
] + TRANSICIONES_JUDICIALES

# id, tema, pregunta, nodos
DUDAS = [
    ("D01", "Prescripción por período", "Cada período salarial prescribe a los 2 años desde que es exigible (art. 256 LCT). Propuesta de la app: un control por el crédito más antiguo y plazos sueltos para los demás. ¿Es suficiente o conviene un hito por período? Es la misma pregunta que la D04 de la matriz general.", "SAL_015"),
    ("D02", "Exigibilidad del sueldo", "¿Los 4 días (mensual) y 3 días (quincenal o semanal) del art. 128 LCT son hábiles administrativos? ¿Cómo se cuentan el SAC (30/6 y 18/12, art. 122 LCT) y las vacaciones?", "SAL_012, SAL_015"),
    ("D03", "Aportes retenidos", "¿Sigue vigente la sanción del art. 132 bis LCT y el plazo de 30 días del art. 1 Dec. 146/01 tras la Ley 27.742? Si no, SAL_017 se elimina.", "SAL_017"),
    ("D04", "Sanciones disciplinarias", "Confirmar el plazo de 30 días corridos para impugnar (art. 67 LCT) y que el silencio implica consentimiento.", "SAL_013"),
    ("D05", "Reclamo con el vínculo vigente", "¿La conciliación previa es exigible igual con el vínculo vigente? ¿Hay medidas que convenga pedir para proteger al trabajador mientras dura el juicio?", "SAL_040, SAL_050"),
    ("D06", "Horas extra", "¿Qué prueba suele exigirse en PBA para las horas extra? ¿Los límites del Dec. 484/00 afectan la liquidación?", "SAL_010, SAL_050"),
    ("D07", "Pago insuficiente", "Confirmar que el recibo firmado sin reservas no impide reclamar la diferencia (art. 260 LCT).", "SAL_010"),
    ("D08", "Ejecución autónoma", "¿Se modela la ejecución de un acta de acuerdo homologado fuera del juicio, o de un certificado de deuda? Hoy queda fuera de la V1.", "SAL_900, SAL_910"),
    ("D09", "Rebaja salarial", "¿La acción de restablecimiento de condiciones del art. 66 LCT (vía sumarísima) debería tener su propio camino? Hoy queda fuera de este flujo.", "SAL_010"),
    ("D10", *DUDA_MATRIZ_GENERAL),
]
