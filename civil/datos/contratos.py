from comun import (CON_GRACIA, CON_VALOR_CERO, DUDA_ETAPA_COMUN, DUDA_PRODUCTO, ESTADOS, FASES_COMUNES, GRUPOS,
                   ROLES, etapa_judicial, flujo, mediacion, ordenar, plazo_tipos)

FLUJO = flujo(
    "Incumplimiento contractual (compraventa, locación sin desalojo y fideicomiso) - Provincia de Buenos Aires",
    "CPCCBA (Decreto-Ley 7425/68), juicio ordinario (art. 319); CCyC arts. 1031, 1077 a 1090, 1137 a 1171, 1201, "
    "1666 a 1678; Ley 13.951 (mediación); Ley 24.240",
    "Borrador para validar con el equipo legal. Citas cotejadas al 13/11/2026 con normas.gba.gob.ar y leyes-ar.com; "
    "lo que no se pudo confirmar dice '(a verificar)' y tiene su duda. La etapa judicial sale de civil/datos/comun.py "
    "en su versión de juicio ordinario; la escrituración, la resolución de compraventa de inmuebles y la "
    "consignación tramitan por sumario (art. 320 inc. 2 a y f): ver duda D01. Las dudas de la etapa común se "
    "responden en matriz_civil_danos_y_perjuicios_pba.xlsx y las de producto en matriz_civil_sucesorio_pba.xlsx.",
)

FASES = FASES_COMUNES

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": "En este flujo: toda la etapa judicial del juicio ordinario (contestación, excepciones "
                          "previas, ofrecimiento de prueba, recursos, liquidación y honorarios).",
    "CORRIDOS": "En este flujo: emplazamiento del art. 1088 CCyC (no menor a 15 días), denuncia del vicio oculto "
                "(60 días, art. 1054), intimación al locador a reparar (10 días, art. 1201), mediación y "
                "reanudación de la prescripción.",
    "HABILES_ADMINISTRATIVOS": "En este flujo: respuesta del acreedor a la consignación extrajudicial (5 días "
                               "hábiles, art. 911 CCyC; tipo de días hábiles, a verificar).",
    "MESES": "En este flujo: suspensión de la prescripción por interpelación (6 meses) y caducidad de instancia "
             "(6 meses en el ordinario).",
    "ANIOS": "En este flujo: prescripción de la acción (5 años, art. 2560 CCyC) y de los vicios redhibitorios "
             "(1 año, art. 2564).",
    "FECHA_FIJADA": "En este flujo: citación a escriturar, audiencias de mediación, preliminar y de vista de causa.",
    "SIN_PLAZO": "En este flujo: análisis del caso, rendición de cuentas del fiduciario, actos del juzgado y plazos "
                 "que fija el juez o la intimación.",
})

ROL_TEXTO = {"ACTORA": "Contratante que representamos", "DEMANDADA": "Contraparte incumplidora",
             "TRIBUNAL": "Juzgado u organismo", "AMBAS": "Cualquiera de las partes"}
LEYENDA_ROLES = ("celeste = el contratante que reclama y al que representamos: comprador, vendedor, locatario, "
                 "fiduciante, beneficiario o deudor que consigna (ACTORA); naranja = la contraparte incumplidora o el "
                 "acreedor que no recibe el pago (DEMANDADA); gris = el juzgado, el mediador, el escribano o un "
                 "registro (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).")
EJEMPLO_PARALELO = ("la prescripción queda suspendida por la interpelación mientras corre el emplazamiento para "
                    "cumplir")
ROLES_DESCRIPCION = [
    ("ACTORA", "El contratante que reclama y al que representamos: comprador o vendedor, locatario, fiduciante o "
               "beneficiario, o el deudor que consigna el pago."),
    ("DEMANDADA", "La contraparte incumplidora: vendedor que no escritura o no entrega, comprador que no paga, "
                  "locador que no repara, fiduciario que no rinde cuentas, o el acreedor que no recibe el pago."),
    ("TRIBUNAL", "El juzgado, la Cámara, la SCBA, el mediador, el escribano o un registro. El nombre del hito dice "
                 "cuál. La app muestra 'Esperando resolución'."),
    ("AMBAS", "Cualquiera de las partes: citación a escriturar, audiencias, prueba, recursos, honorarios y acuerdos."),
]
INSTRUCCIONES_ADICIONALES = [
    ("Particularidades de contratos", True),
    ("La consulta inicial abre una variante: compraventa, locación sin desalojo, fideicomiso, consignación del pago "
     "u otro contrato (también de consumo). El desalojo y el cobro de alquileres tienen su propia matriz.", False),
    ("La etapa judicial es la común del fuero civil para el juicio ordinario, con un camino propio para la condena "
     "a escriturar (art. 510 CPCCBA).", False),
    ("Plazos que fija la intimación, el contrato o el juez: el hito es SIN_PLAZO y el checklist indica que el "
     "abogado lo carga como plazo suelto.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
_PREVIA = [
    ("CTR_010", "Previa", "Consulta inicial por el incumplimiento del contrato", "ACTORA",
     "Fecha de la consulta", 0, "SIN_PLAZO", "NO",
     "Arts. 957, 959 y 1084 CCyC", "SI", "NO",
     ["Identificar el contrato, las partes, las prestaciones y la fecha de exigibilidad de cada una",
      "Identificar el incumplimiento y si es esencial (art. 1084)",
      "Controlar si el cliente cumplió su parte: si no, la contraria puede suspender u oponerse (arts. 1031 y "
      "1078 inc. c)",
      "Si es una relación de consumo, rige la Ley 24.240: proceso más abreviado y beneficio de gratuidad (art. 53)",
      "El desalojo y el cobro de alquileres tienen su propia matriz",
      "Pactar honorarios y firmar el poder"],
     ["Contrato", "Comprobantes de pago", "Comunicaciones entre las partes", "Poder"]),
    ("CTR_015", "Previa", "Control de prescripción de la acción", "ACTORA",
     "Exigibilidad de la prestación incumplida", 5, "ANIOS", "NO",
     "Arts. 2554, 2560, 2561, 2562 y 2564 CCyC", "NO", "NO",
     ["Plazo genérico: 5 años desde que la prestación es exigible (arts. 2554 y 2560)",
      "Plazos especiales: daños, 3 años (art. 2561); prestaciones periódicas como los alquileres, 2 años (art. 2562 "
      "inc. c); vicios redhibitorios, 1 año (art. 2564): editar si es el caso (ver duda D02)",
      "Se suspende por la interpelación fehaciente (art. 2541) y la mediación (art. 2542); se interrumpe con la "
      "demanda (art. 2546)"],
     ["Contrato", "Constancia de la fecha de exigibilidad"]),
    ("CTR_017", "Previa", "Suspensión de la prescripción por la interpelación fehaciente", "ACTORA",
     "Recepción de la intimación por la contraparte", 6, "MESES", "NO",
     "Art. 2541 CCyC", "NO", "NO",
     ["La suspensión opera una sola vez y dura 6 meses (art. 2541)",
      "Sumar el período de suspensión al vencimiento de la prescripción (hito CTR_015)"],
     ["Intimación con aviso de recibo"]),
    ("CTR_020", "Previa", "Elección entre exigir el cumplimiento o resolver el contrato", "ACTORA",
     "Fecha del incumplimiento", 0, "SIN_PLAZO", "NO",
     "Arts. 1078, 1081, 1083, 1086, 1087 y 1088 CCyC", "NO", "NO",
     ["Optar entre exigir el cumplimiento o resolver, y reclamar los daños en ambos casos",
      "La resolución total y la parcial se excluyen: elegida una, no se puede pasar a la otra (art. 1083)",
      "Pedir el cumplimiento no impide pedir después la resolución; demandar la resolución impide pedir después el "
      "cumplimiento (art. 1078 inc. e y g)",
      "Si hay cláusula resolutoria expresa, la resolución opera desde la comunicación fehaciente (art. 1086)",
      "Si no la hay, emplazar a cumplir bajo apercibimiento de resolver (art. 1088)",
      "No hace falta emplazar si venció un plazo esencial, si la contraria dijo que no cumplirá o si el "
      "cumplimiento es imposible (art. 1088)",
      "Evaluar medidas cautelares: anotación de litis, embargo, prohibición de innovar"],
     ["Contrato", "Borrador de la intimación"]),
    ("CTR_025", "Previa", "Emplazamiento a cumplir bajo apercibimiento de resolución", "DEMANDADA",
     "Recepción del emplazamiento por la contraparte", 15, "CORRIDOS", "NO",
     "Art. 1088 CCyC", "NO", "NO",
     ["El plazo no puede ser menor a 15 días, salvo que los usos o la índole de la prestación permitan uno menor: "
      "editar si se dio otro",
      "El emplazamiento debe tener el apercibimiento expreso de resolución total o parcial",
      "La resolución se produce de pleno derecho al vencer el plazo (art. 1088)",
      "El emplazamiento recibido es interpelación fehaciente: suspende la prescripción (art. 2541)"],
     ["Carta documento con aviso de recibo"]),
    ("CTR_030", "Previa", "Análisis de la compraventa: boleto, entrega, precio y escritura", "ACTORA",
     "Fecha del incumplimiento", 0, "SIN_PLAZO", "NO",
     "Arts. 1137, 1139, 1141, 1146, 1170 y 1171 CCyC", "NO", "NO",
     ["Revisar el boleto: fecha cierta, precio pagado, posesión entregada y escribano designado",
      "El comprador de buena fe tiene prioridad sobre embargantes posteriores si pagó al menos el 25 % del precio, "
      "el boleto tiene fecha cierta y hay publicidad registral o posesoria (art. 1170)",
      "Pedir informe de dominio e inhibiciones del vendedor",
      "El vendedor debe transferir la propiedad y entregar los documentos y la cosa; el inmueble, inmediatamente "
      "después de la escritura salvo pacto en contrario (arts. 1137, 1139 y 1146)",
      "El comprador debe pagar el precio en el lugar y tiempo convenidos (de contado si nada se pactó) y recibir la "
      "cosa (art. 1141)",
      "Si el vendedor está en concurso o quiebra, ver el art. 1171"],
     ["Boleto", "Recibos de pago", "Informe de dominio e inhibiciones"]),
    ("CTR_032", "Previa", "Citación a escriturar ante el escribano", "AMBAS",
     "Fecha y hora fijadas en la intimación a escriturar", 0, "FECHA_FIJADA", "NO",
     "Arts. 1018 y 1137 CCyC", "NO", "NO",
     ["Intimar a la contraparte a escriturar con día, hora y escribanía",
      "El otorgamiento de la escritura es una obligación de hacer: si la parte condenada es remisa, la otorga el "
      "juez, siempre que las contraprestaciones estén cumplidas o aseguradas (art. 1018)",
      "Tener lista la documentación: certificados registrales, catastrales, de deudas e impuestos",
      "Si la contraparte no comparece, labrar acta notarial de la incomparecencia"],
     ["Intimación a escriturar", "Acta notarial"]),
    ("CTR_050", "Previa", "Denuncia del defecto oculto al vendedor", "ACTORA",
     "Manifestación del defecto (si es gradual, desde que se pudo advertir)", 60, "CORRIDOS", "NO",
     "Arts. 1051, 1053, 1054, 1055, 1056 y 1057 CCyC", "NO", "NO",
     ["Denunciar expresamente el defecto al vendedor dentro de los 60 días de manifestado: si no, se pierde la "
      "garantía, salvo que el vendedor lo conociera (art. 1054)",
      "La garantía caduca a los 3 años de recibido el inmueble o a los 6 meses de recibida la cosa mueble "
      "(art. 1055)",
      "Si es un vicio redhibitorio, se puede resolver el contrato (art. 1056), salvo que el defecto sea subsanable y "
      "el vendedor ofrezca subsanarlo (art. 1057)"],
     ["Constancia del defecto", "Denuncia con aviso de recibo"]),
    ("CTR_052", "Previa", "Prescripción del reclamo por vicios redhibitorios", "ACTORA",
     "Denuncia del defecto oculto (inicio del cómputo, a verificar)", 1, "ANIOS", "NO",
     "Art. 2564 inc. a CCyC", "NO", "NO",
     ["El reclamo por vicios redhibitorios prescribe al año (art. 2564 inc. a)",
      "Demandar antes del vencimiento"],
     []),
    ("CTR_060", "Previa", "Análisis del incumplimiento en la locación", "ACTORA",
     "Fecha del incumplimiento", 0, "SIN_PLAZO", "NO",
     "Arts. 1201, 1220 y 1221 CCyC (texto según DNU 70/2023, a verificar)", "NO", "NO",
     ["El locador debe conservar la cosa apta para el uso convenido y hacer las reparaciones (art. 1201)",
      "Reparación urgente: el locatario puede hacerla a cargo del locador después de 24 horas del reclamo "
      "(art. 1201)",
      "El locatario puede resolver si el locador no conserva la cosa o por evicción o vicios (art. 1220)",
      "Resolución anticipada por el locatario: pagar el 10 % del canon futuro (art. 1221)",
      "Reclamar la devolución del depósito en garantía al terminar la locación"],
     ["Contrato de locación", "Reclamos enviados", "Presupuestos"]),
    ("CTR_062", "Previa", "Plazo del locador para hacer las reparaciones", "DEMANDADA",
     "Recepción de la intimación a reparar", 10, "CORRIDOS", "NO",
     "Art. 1201 CCyC", "NO", "NO",
     ["La intimación para reparaciones no urgentes da un plazo no menor a 10 días corridos (art. 1201): editar si se "
      "dio otro",
      "Vencido el plazo, el locatario puede hacerlas a cargo del locador (art. 1201)"],
     ["Intimación con aviso de recibo", "Presupuestos"]),
    ("CTR_070", "Previa", "Rendición de cuentas del fiduciario", "DEMANDADA",
     "Recepción de la intimación a rendir cuentas", 0, "SIN_PLAZO", "NO",
     "Arts. 1666, 1674, 1676 y 1678 CCyC", "NO", "NO",
     ["El fiduciario no puede ser dispensado de rendir cuentas (art. 1676): intimarlo y cargar el plazo dado como "
      "plazo suelto",
      "Debe actuar con la diligencia de un buen hombre de negocios (art. 1674)",
      "Ante incumplimiento grave, pedir la remoción judicial (art. 1678 inc. a): la pide el fiduciante, o el "
      "beneficiario o fideicomisario con citación del fiduciante",
      "En el fideicomiso inmobiliario, revisar si la relación es de consumo"],
     ["Contrato de fideicomiso", "Intimación", "Rendiciones recibidas"]),
    ("CTR_090", "Previa", "Respuesta del acreedor a la consignación extrajudicial", "DEMANDADA",
     "Notificación del depósito por el escribano", 5, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 904, 910, 911 y 912 CCyC", "NO", "NO",
     ["Procede si el acreedor está en mora, si hay incertidumbre sobre quién es o si no se puede pagar en forma "
      "segura (art. 904)",
      "Notificar antes al acreedor el día, la hora y el lugar del depósito ante escribano (art. 910 inc. a)",
      "Depositar capital e intereses; el escribano notifica el depósito dentro de las 48 horas hábiles (art. 910 "
      "inc. b)",
      "El acreedor tiene 5 días hábiles para aceptar, retirar con reserva o rechazar (art. 911)",
      "Si rechaza o no se expide, consignar judicialmente (juicio sumario, art. 320 inc. 2 a CPCCBA)"],
     ["Notificación previa", "Acta de depósito notarial"]),
]

_MED_NODOS, _MED_TRANSICIONES = mediacion("CTR", ("080", "082", "084", "086"), demanda="CTR_300",
                                          acuerdo="CTR_800")

_ETAPA_NODOS, _ETAPA_TRANSICIONES = etapa_judicial(
    "CTR", "ordinario",
    agregar={
        "CTR_300": [
            "Pedir el cumplimiento o la resolución, con los daños, y las restituciones recíprocas si se resuelve "
            "(arts. 1081 y 1083 CCyC)",
            "La demanda de resolución puede iniciarse sin el emplazamiento previo (art. 1078 inc. b)",
            "Escrituración, resolución de compraventa de inmuebles y consignación tramitan por sumario (art. 320 "
            "inc. 2 a y f CPCCBA); los reclamos de consumo, por el proceso más abreviado y con justicia gratuita "
            "(art. 53 Ley 24.240): ver duda D01",
            "Cautelares típicas: anotación de litis sobre el inmueble, embargo, prohibición de innovar",
            "Remoción del fiduciario: demandar con citación del fiduciante si la pide el beneficiario (art. 1678)"],
        "CTR_340": [
            "Defensas típicas: excepción de incumplimiento (art. 1031 CCyC) y tutela preventiva (art. 1032)",
            "Oposición a la resolución si quien la declara no cumplió su parte (art. 1078 inc. c)",
            "Si se demandó la resolución sin el emplazamiento previo, el demandado puede cumplir hasta que venza el "
            "plazo de emplazamiento (art. 1078 inc. f)"],
        "CTR_500": [
            "La condena a escriturar lleva el apercibimiento de que el juez firme por el obligado (art. 510 CPCCBA)"],
    },
)

_PROPIOS = [
    ("CTR_735", "Ejecución", "Plazo para escriturar fijado en la sentencia", "DEMANDADA",
     "Notificación de la sentencia firme que condena a escriturar", 0, "SIN_PLAZO", "NO",
     "Art. 510 CPCCBA", "NO", "NO",
     ["El plazo lo fija la sentencia: cargarlo como plazo suelto",
      "Proponer el escribano si el contrato no lo designó (art. 510)",
      "Si el comprador debe saldo de precio, depositarlo según la sentencia"],
     ["Sentencia firme"]),
    ("CTR_740", "Ejecución", "Escrituración por el juez a costa del obligado", "TRIBUNAL",
     "Vencimiento del plazo para escriturar sin otorgamiento", 0, "SIN_PLAZO", "NO",
     "Art. 510 CPCCBA", "NO", "NO",
     ["Pedir que el juez suscriba la escritura por el obligado y a su costa (art. 510)",
      "El juez ordena las medidas complementarias: certificados, levantamiento de medidas, tributos (art. 510)",
      "Controlar la inscripción de la escritura en el Registro de la Propiedad"],
     ["Escritura", "Constancia de inscripción"]),
]

NODOS = sorted(_PREVIA + _MED_NODOS + _ETAPA_NODOS + _PROPIOS, key=lambda n: n[0])

_RESOLVER = "Se emplaza a cumplir bajo apercibimiento de resolución"
_CUMPLIMIENTO = "Se pide la mediación para exigir el cumplimiento o los daños"
_ESCRITURAR = "Queda firme la condena a escriturar"

TRANSICIONES = ordenar(NODOS, [
    ("CTR_010", "Compraventa", "CTR_015"),
    ("CTR_010", "Compraventa", "CTR_030"),
    ("CTR_010", "Locación sin desalojo", "CTR_015"),
    ("CTR_010", "Locación sin desalojo", "CTR_060"),
    ("CTR_010", "Fideicomiso", "CTR_015"),
    ("CTR_010", "Fideicomiso", "CTR_070"),
    ("CTR_010", "Otro contrato o relación de consumo", "CTR_015"),
    ("CTR_010", "Otro contrato o relación de consumo", "CTR_020"),
    ("CTR_010", "El cliente quiere pagar y el acreedor no recibe: consignación extrajudicial", "CTR_090"),
    ("CTR_010", "El cliente quiere pagar y el acreedor no recibe: consignación judicial", "CTR_300"),
    ("CTR_015", "Demanda presentada antes del vencimiento, o reclamo abandonado", ""),
    ("CTR_017", "Suspensión agotada o demanda presentada", ""),
    ("CTR_020", _RESOLVER, "CTR_017"),
    ("CTR_020", _RESOLVER, "CTR_025"),
    ("CTR_020", "Hay cláusula resolutoria expresa: se comunica la resolución", "CTR_080"),
    ("CTR_020", _CUMPLIMIENTO, "CTR_080"),
    ("CTR_025", "Cumple en el plazo", "CTR_990"),
    ("CTR_025", "No cumple: el contrato queda resuelto", "CTR_080"),
    ("CTR_030", "Falta la escritura: se cita a escriturar", "CTR_032"),
    ("CTR_030", "Falta la entrega de la cosa o el pago del precio", "CTR_020"),
    ("CTR_030", "La cosa tiene defectos ocultos", "CTR_050"),
    ("CTR_032", "Se otorga la escritura", "CTR_990"),
    ("CTR_032", "La contraparte no comparece o se niega", "CTR_080"),
    ("CTR_050", "Defecto denunciado en término", "CTR_020"),
    ("CTR_050", "Defecto denunciado en término", "CTR_052"),
    ("CTR_050", "Vencido sin denuncia: se evalúa si el vendedor conocía el defecto", ""),
    ("CTR_052", "Demanda presentada o reclamo resuelto", ""),
    ("CTR_060", "Reparación no urgente: se intima al locador", "CTR_062"),
    ("CTR_060", "Otro incumplimiento: se elige cumplimiento o resolución", "CTR_020"),
    ("CTR_062", "El locador repara", "CTR_990"),
    ("CTR_062", "No repara: el locatario repara a su cargo o resuelve", "CTR_020"),
    ("CTR_070", "Rinde cuentas en forma satisfactoria", "CTR_990"),
    ("CTR_070", "No rinde o hay incumplimiento grave: se reclama o se pide la remoción", "CTR_080"),
    ("CTR_090", "Acepta o retira el depósito", "CTR_990"),
    ("CTR_090", "Rechaza o no se expide: se consigna judicialmente", "CTR_300"),
    *_MED_TRANSICIONES,
    *_ETAPA_TRANSICIONES,
    ("CTR_600", "No se recurre: " + _ESCRITURAR[:1].lower() + _ESCRITURAR[1:], "CTR_735"),
    ("CTR_620", "Cámara: " + _ESCRITURAR[:1].lower() + _ESCRITURAR[1:], "CTR_735"),
    ("CTR_640", "Queja rechazada: " + _ESCRITURAR[:1].lower() + _ESCRITURAR[1:], "CTR_735"),
    ("CTR_645", "La SCBA resuelve: " + _ESCRITURAR[:1].lower() + _ESCRITURAR[1:], "CTR_735"),
    ("CTR_735", "El obligado escritura", "CTR_990"),
    ("CTR_735", "No escritura en el plazo: firma el juez", "CTR_740"),
    ("CTR_740", "Escritura otorgada e inscripta", "CTR_990"),
])

_PROPIAS = [
    ("Tipo de proceso",
     "La matriz usa el juicio ordinario, que corresponde a los contratos de más de 4.500 Jus (arts. 319 y 320 "
     "inc. 1 CPCCBA). La escrituración, la resolución de compraventa de inmuebles y la consignación son sumario "
     "(art. 320 inc. 2 a y f) y los reclamos de consumo van por el proceso más abreviado (art. 53 Ley 24.240). En "
     "esos casos el abogado edita los plazos. ¿Conviene publicar una versión sumaria de esta matriz?",
     "CTR_300, CTR_340, CTR_350, CTR_410"),
    ("Prescripción",
     "La matriz usa 5 años (art. 2560 CCyC). ¿Los daños por incumplimiento contractual prescriben a los 3 años "
     "(art. 2561) o a los 5? ¿Desde cuándo corre la acción de escrituración del boleto?",
     "CTR_015"),
    ("Emplazamiento del art. 1088",
     "El emplazamiento a cumplir tiene un plazo no menor a 15 días, salvo usos o índole de la prestación. La matriz "
     "usa 15 días corridos (norma de fondo). ¿Es correcto? ¿Corre durante la feria judicial?",
     "CTR_025"),
    ("Cláusula resolutoria expresa",
     "Con cláusula resolutoria expresa la resolución opera desde la comunicación fehaciente (art. 1086). La matriz no "
     "abre un hito propio: va directo a la mediación. ¿Falta algún plazo (por ejemplo, para restituir)?",
     "CTR_020"),
    ("Mediación",
     "La mediación es obligatoria en los reclamos contractuales (Ley 13.951), salvo exclusiones del art. 4. ¿Es "
     "obligatoria también para la consignación judicial y la escrituración?",
     "CTR_080, CTR_300"),
    ("Citación a escriturar",
     "La matriz modela la citación a escriturar como una fecha fijada en la intimación (arts. 1018 y 1137 CCyC). "
     "¿Qué anticipación mínima se suele dar, y la incomparecencia se documenta siempre con acta notarial?",
     "CTR_032"),
    ("Vicios ocultos",
     "La denuncia del defecto va dentro de los 60 días de manifestado (art. 1054) y el reclamo prescribe al año "
     "(art. 2564 inc. a). ¿Desde cuándo corre el año: desde la manifestación, la denuncia o la recepción de la cosa?",
     "CTR_050, CTR_052"),
    ("Locación",
     "Los arts. 1201, 1220 y 1221 CCyC se citan con el texto de leyes-ar.com; el del art. 1221 refleja el DNU "
     "70/2023 y el del art. 1201 parece el de la Ley 27.551. ¿Qué texto rige al 13/11/2026?",
     "CTR_060, CTR_062"),
    ("Fideicomiso",
     "El fiduciario debe rendir cuentas (art. 1676) pero el plazo depende del contrato. ¿Se usa el proceso de "
     "rendición de cuentas del CPCCBA (artículos, a verificar)? ¿La remoción del fiduciario (art. 1678) es ordinario "
     "o sumario?",
     "CTR_070"),
    ("Consignación extrajudicial",
     "El acreedor tiene 5 días hábiles para responder a la consignación extrajudicial (art. 911 CCyC). La matriz los "
     "cuenta como días hábiles administrativos. ¿Es el criterio correcto?",
     "CTR_090"),
    ("Escrituración por el juez",
     "La condena a escriturar se cumple en el plazo de la sentencia o la firma el juez (art. 510). La matriz agrega "
     "salidas propias desde la apelación, la Cámara, la queja y la SCBA. ¿Hay pasos que falten (certificados, "
     "tributos, inscripción)?",
     "CTR_600, CTR_735, CTR_740"),
    ("Consumo",
     "En los contratos de consumo, ¿se aplica el beneficio de gratuidad (art. 53 Ley 24.240) a la tasa de justicia "
     "en PBA, y por qué proceso tramita (sumario o sumarísimo)?",
     "CTR_010, CTR_300"),
]

DUDAS = [(f"D{i:02d}", *d)
         for i, d in enumerate(_PROPIAS + [DUDA_PRODUCTO, DUDA_ETAPA_COMUN], start=1)]
