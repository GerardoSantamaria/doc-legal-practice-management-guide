"""Hábeas data (HDA) — art. 20 inc. 3 Constitución PBA y Ley 14.214; variante federal: art. 43 CN y Ley 25.326."""
from comun import (
    CHECKLIST_COSTOS_FED,
    CHECKLIST_COSTOS_PBA,
    CHECKLIST_SIN_DATOS,
    CIERRA,
    CON_GRACIA,
    CON_VALOR_CERO,
    DUDA_REMITIR_TRANSVERSALES,
    ESTADOS,
    FUENTE_HD,
    INSTRUCCIONES_ADICIONALES,
    NOTA_FUENTES,
    NOTA_SENSIBLES,
    ROL_TEXTO,
    ROLES,
    ROLES_DESCRIPCION,
    bloque_amparo,
    flujo,
    honorarios,
    leyenda,
    numerar,
    ordenar,
    plazo_tipos,
)

P = "HDA"
i = lambda n: f"{P}_{n:03d}"

FLUJO = flujo(
    "Hábeas data (PBA, con variante federal)",
    "PBA",
    "Civil y Comercial o Paz Letrado (bancos privados) y Contencioso Administrativo (bancos públicos provinciales); "
    "federal para bancos nacionales o interconectados",
    "Ley 14.214 con el CPCCBA supletorio (sumarísimo, art. 8); variante federal: Ley 25.326 (arts. 33 a 44), con "
    "el procedimiento del amparo común y el sumarísimo del CPCCN supletorios (art. 37)",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre el acceso, la rectificación, la actualización, la confidencialidad "
    "y la supresión de datos personales: reclamo previo obligatorio, denuncia ante la AAIP, datos crediticios "
    "(art. 26 Ley 25.326 y Central de Deudores del BCRA), demanda, anotación de litigiosidad o bloqueo, informe, "
    "prueba, sentencia, apelación y cumplimiento. El fuero depende del banco de datos.",
)

FASES = [
    "Previa",
    "Vía administrativa",
    "Organismo de control",
    "Demanda",
    "Cautelares",
    "Prueba",
    "Sentencia",
    "Recursos",
    "Cumplimiento",
    "Cierre",
]

GRUPOS = [
    ("Etapa previa: encuadre, datos crediticios y Central de Deudores", ["Previa"]),
    ("Reclamo previo ante el responsable del banco de datos (arts. 14 y 16 Ley 25.326; art. 5 Ley 14.214)",
     ["Vía administrativa"]),
    ("Denuncia ante la AAIP", ["Organismo de control"]),
    ("Demanda: hábeas data provincial (Ley 14.214) y federal (Ley 25.326)", ["Demanda"]),
    ("Anotación de litigiosidad y bloqueo provisional", ["Cautelares"]),
    ("Prueba y sentencia", ["Prueba", "Sentencia"]),
    ("Recursos", ["Recursos"]),
    ("Cumplimiento, honorarios y cierre", ["Cumplimiento", "Cierre"]),
]

LEYENDA = leyenda(
    paralelo="la negativa o el silencio del responsable abren a la vez la demanda y la denuncia ante la AAIP",
    adicionales=[
        "**Fuero según el banco de datos:** bancos privados provinciales, juzgado Civil y Comercial o de Paz; "
        "públicos provinciales, Contencioso Administrativo (art. 4 Ley 14.214); públicos nacionales o "
        "interconectados, justicia federal (art. 36 Ley 25.326).",
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "CORRIDOS": "respuesta al pedido de acceso en 10 días corridos (art. 14 Ley 25.326).",
    "HABILES_ADMINISTRATIVOS": "respuesta al reclamo de rectificación, actualización o supresión en 5 días hábiles "
                               "(art. 16 Ley 25.326).",
    "HABILES_JUDICIALES": (
        "Ley 14.214: demanda en 60 días (art. 7), admisión en 2 (art. 13), informe en 5 o 10 (art. 13), sentencia "
        "en 10 (art. 15), apelación en 2 o 5 (art. 16); Ley 25.326: informe en hasta 5 días (art. 39) y ampliación "
        "en 3 (art. 42)."
    ),
    "HORAS": "sentencia, apelación y recurso directo del amparo común federal (Ley 16.986, supletoria).",
    "ANIOS": "plazo de conservación de datos crediticios: 2 años desde la cancelación (art. 26 inc. 4 Ley 25.326).",
    "FECHA_FIJADA": "audiencia de prueba federal y cumplimiento de la sentencia.",
    "SIN_PLAZO": "decisiones del cliente, plazo de prueba que fija el juez y actos sin plazo legal.",
})

FED = "Calendario y gracia federales: se carga sin gracia (ver duda de producto sobre jurisdicción federal)"

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    # --- Previa ---
    (i(10), "Previa", "Encuadre del hábeas data, del banco de datos y del fuero", "ACTORA",
     "Consulta del cliente por datos personales registrados", 0, "SIN_PLAZO", "NO",
     "Art. 20 inc. 3 Constitución PBA; arts. 1 a 4 Ley 14.214; art. 43 Constitución Nacional; arts. 33 a 36 Ley "
     "25.326", "SI", "NO",
     ["Definir el objeto: acceso, rectificación, actualización, confidencialidad o supresión (art. 33 Ley 25.326)",
      "Definir el banco: público o privado destinado a dar informes; provincial, nacional o interconectado",
      "Fuero: Civil y Comercial o Paz (privado), Contencioso Administrativo (público provincial), federal (público "
      "nacional o interconectado); juez del domicilio del actor, del demandado o del lugar del efecto",
      CHECKLIST_SIN_DATOS],
     ["Poder o patrocinio", "Informe o constancia del dato cuestionado"]),
    (i(60), "Previa", "Control del plazo de conservación del dato crediticio", "ACTORA",
     "Cancelación o extinción de la obligación informada", 2, "ANIOS", "NO", "Art. 26 inc. 4 Ley 25.326", "NO",
     "NO",
     ["Solo se pueden informar datos significativos de los últimos 5 años; 2 años si la deuda se canceló",
      "Pedir al acreedor la constancia de cancelación (libre deuda) y que informe la cancelación",
      "Si la deuda no se canceló, ajustar el plazo a 5 años desde la fecha que corresponda (ver duda)"],
     ["Constancia de deuda cancelada"]),
    (i(70), "Previa", "Central de Deudores del BCRA: identificación de la entidad informante", "ACTORA",
     "El dato cuestionado figura en la Central de Deudores del Sistema Financiero", 0, "SIN_PLAZO", "NO",
     "Normas del BCRA sobre la Central de Deudores (comunicación vigente a verificar); art. 26 Ley 25.326", "NO",
     "NO",
     ["Consultar la Central de Deudores e identificar la entidad que informó el dato y el período",
      "El reclamo de rectificación se dirige a la entidad informante (ver duda sobre el rol del BCRA)",
      "Reunir la constancia de cancelación o de la inexactitud"],
     ["Consulta de la Central de Deudores", "Constancia de deuda cancelada"]),
    # --- Vía administrativa / reclamo previo ---
    (i(20), "Vía administrativa", "Solicitud fehaciente de acceso a los datos", "ACTORA",
     "Decisión de conocer los datos registrados", 0, "SIN_PLAZO", "NO",
     "Arts. 14 y 15 Ley 25.326; art. 5 Ley 14.214", "NO", "NO",
     ["Intimar por medio fehaciente acreditando la identidad",
      "Gratuito cada 6 meses salvo interés legítimo (art. 14 inc. 3)",
      "Si es un banco público, es una presentación administrativa: indicar la dependencia"],
     ["Solicitud de acceso con constancia de recepción"]),
    (i(30), "Vía administrativa", "Respuesta del responsable al pedido de acceso", "DEMANDADA",
     "Recepción de la intimación de acceso", 10, "CORRIDOS", "NO", "Art. 14 inc. 2 Ley 25.326; art. 6 Ley 14.214",
     "NO", "NO",
     ["Ley 25.326: 10 días corridos",
      "Si rige la Ley 14.214, hay silencio a los 5 días hábiles (privados) o 15 (públicos): cargar el que venza "
      "antes como plazo suelto (ver duda)",
      "La información debe ser clara, completa y sin datos de terceros (art. 15)"],
     ["Respuesta del responsable"]),
    (i(40), "Vía administrativa", "Reclamo de rectificación, actualización, supresión o confidencialidad", "ACTORA",
     "Conocimiento de un dato falso, inexacto, desactualizado o de registro prohibido", 0, "SIN_PLAZO", "NO",
     "Art. 16 Ley 25.326; art. 5 Ley 14.214", "NO", "NO",
     ["Intimar por medio fehaciente indicando el dato y lo que se pide",
      "Acompañar la prueba (por ejemplo, constancia de deuda cancelada)",
      "No es exigible si el reclamo previo causa un perjuicio de imposible reparación (art. 5 Ley 14.214)",
      CHECKLIST_SIN_DATOS],
     ["Reclamo con constancia de recepción", "Prueba documental"]),
    (i(50), "Vía administrativa", "Respuesta del responsable al reclamo de rectificación o supresión", "DEMANDADA",
     "Recepción del reclamo", 5, "HABILES_ADMINISTRATIVOS", "NO", "Art. 16 incs. 2 y 3 Ley 25.326; art. 6 Ley 14.214",
     "NO", "NO",
     ["Plazo máximo de 5 días hábiles; si no cumple, queda habilitado el hábeas data (art. 16 inc. 3)",
      "Banco público provincial: el art. 6 Ley 14.214 da 15 días hábiles para que haya silencio (ver duda)",
      "Calendario administrativo provincial o nacional según el banco (ver duda de producto)",
      "Durante el reclamo, el dato puede bloquearse (art. 16, a verificar)"],
     ["Respuesta del responsable"]),
    # --- Organismo de control ---
    (i(80), "Organismo de control", "Denuncia ante la Agencia de Acceso a la Información Pública (AAIP)", "ACTORA",
     "Negativa o silencio del responsable del banco de datos", 0, "SIN_PLAZO", "NO",
     "Arts. 29 y 31 Ley 25.326; Ley 27.275 (AAIP como órgano de control, a verificar)", "NO", "NO",
     ["La AAIP puede sancionar al responsable, pero la denuncia no reemplaza al hábeas data ni suspende sus plazos "
      "(a verificar)",
      "Acompañar el reclamo previo y la respuesta o la constancia del silencio",
      CHECKLIST_SIN_DATOS],
     ["Denuncia", "Reclamo previo y respuesta"]),
    # --- Demanda provincial ---
    (i(200), "Demanda", "Demanda de hábeas data provincial (Ley 14.214) dentro de los 60 días hábiles", "ACTORA",
     "Notificación de la negativa del responsable (o configuración del silencio, ver duda)", 60,
     "HABILES_JUDICIALES", "NO", "Arts. 7, 9 y 19 Ley 14.214", "NO", "NO",
     ["Si vence el plazo, caduca el procedimiento y hay que reiterar la intimación previa (art. 7)",
      "Requisitos del art. 9: identificar el banco, el dato, el motivo y acreditar el reclamo previo",
      "No se pueden acumular pretensiones económicas (art. 13 inc. 2)",
      "Exenta del pago previo de tasas e impuestos (art. 19); bono de la Ley 8480 y anticipo del art. 13 Ley 6716",
      CHECKLIST_COSTOS_PBA[2],
      CHECKLIST_SIN_DATOS],
     ["Demanda", "Poder o patrocinio", "Reclamo previo y respuesta"]),
    (i(210), "Demanda", "Admisión formal de la demanda de hábeas data provincial", "TRIBUNAL",
     "Presentación de la demanda", 2, "HABILES_JUDICIALES", "NO", "Art. 13 Ley 14.214", "NO", "NO",
     ["El juez se pronuncia sobre la admisión en 2 días",
      "Si se demora, pedir pronto despacho"],
     ["Providencia de admisión"]),
    (i(230), "Demanda", "Informe del banco de datos (Ley 14.214)", "DEMANDADA",
     "Notificación del emplazamiento a producir el informe", 5, "HABILES_JUDICIALES", "SI",
     "Art. 13 incs. 1, 3 y 4 Ley 14.214", "NO", "NO",
     ["5 días hábiles para bancos privados y 10 para públicos: si es público, cambiar el plazo a 10",
      "Si el juez lo amplía, cargarlo como plazo suelto",
      "Solo se admiten las excepciones del art. 13 inc. 3",
      "El informe debe explicar por qué se incluyó el dato y para qué se usó (art. 13 inc. 4)"],
     ["Informe del banco de datos"]),
    # --- Cautelares ---
    (i(220), "Cautelares", "Anotación de litigiosidad o bloqueo provisional del dato", "ACTORA",
     "Presentación de la demanda (o en cualquier estado del proceso)", 0, "SIN_PLAZO", "NO",
     "Art. 10 Ley 14.214; art. 38 incs. 3 y 4 Ley 25.326", "NO", "NO",
     ["Pedir que el banco asiente que el dato está sometido a proceso judicial",
      "Pedir el bloqueo provisional si el carácter falso, inexacto o discriminatorio es manifiesto",
      "En la provincia solo puede pedirse después de presentada la demanda (art. 10)"],
     ["Escrito de cautelar"]),
    (i(225), "Cautelares", "Apelación de la resolución cautelar (provincial)", "AMBAS",
     "Notificación de la resolución cautelar", 2, "HABILES_JUDICIALES", "SI", "Art. 16 Ley 14.214", "NO", "NO",
     ["Interponer y fundar dentro de los 2 días hábiles",
      "Efecto devolutivo salvo gravamen irreparable"],
     ["Escrito de apelación"]),
    # --- Prueba y sentencia provincial ---
    (i(240), "Prueba", "Prueba en el hábeas data provincial", "AMBAS",
     "Apertura a prueba por hechos controvertidos", 0, "SIN_PLAZO", "NO", "Art. 14 Ley 14.214", "NO", "NO",
     ["El juez fija el plazo de prueba: cargarlo como plazo suelto",
      "Pedir informes al banco y a la fuente del dato",
      CHECKLIST_SIN_DATOS],
     ["Constancias de prueba"]),
    (i(250), "Sentencia", "Sentencia de hábeas data provincial", "TRIBUNAL",
     "Informe presentado o vencido, y prueba producida", 10, "HABILES_JUDICIALES", "NO", "Arts. 15 y 18 Ley 14.214",
     "NO", "NO",
     ["No hay alegatos (art. 15)",
      "Controlar que diga si el dato se suprime, rectifica, actualiza o declara confidencial, y el plazo para "
      "cumplir",
      "Costas al vencido (art. 18) y regulación de honorarios"],
     ["Sentencia"]),
    (i(260), "Recursos", "Apelación de la sentencia de hábeas data provincial", "AMBAS",
     "Notificación de la sentencia o del rechazo de la demanda", 5, "HABILES_JUDICIALES", "SI",
     "Art. 16 Ley 14.214", "NO", "NO",
     ["Interponer y fundar dentro de los 5 días hábiles",
      "Se concede o rechaza dentro de las 24 horas; efecto devolutivo salvo gravamen irreparable",
      "Traslado por 5 días y elevación inmediata"],
     ["Escrito de apelación fundado"]),
    (i(270), "Recursos", "Sentencia de la alzada en el hábeas data provincial", "TRIBUNAL",
     "Elevación del expediente", 0, "SIN_PLAZO", "NO",
     "Art. 16 Ley 14.214; CPCCBA (sumarísimo, supletorio)", "NO", "NO",
     ["Cámara Civil y Comercial o Contencioso Administrativa según el banco",
      "Controlar el plazo y pedir pronto despacho si se demora",
      "Evaluar recursos extraordinarios ante la SCBA (art. 161 Constitución PBA)"],
     ["Sentencia de la alzada"]),
    # --- Federal: ampliación ---
    (i(425), "Demanda", "Ampliación de la demanda tras el informe (federal)", "ACTORA",
     "Notificación del informe del banco de datos", 3, "HABILES_JUDICIALES", "NO", "Art. 42 Ley 25.326", "NO", "NO",
     ["Ampliar el objeto (supresión, rectificación, confidencialidad o actualización) dentro de 3 días",
      "Ofrecer la prueba en el mismo escrito; se corre traslado al banco por 3 días",
      FED],
     ["Escrito de ampliación"]),
    # --- Cumplimiento ---
    (i(500), "Cumplimiento", "Cumplimiento de la sentencia por el banco de datos", "DEMANDADA",
     "Notificación de la sentencia favorable firme (o de la que se cumple con efecto devolutivo)", 0, "FECHA_FIJADA",
     "NO", "Art. 15 Ley 14.214; art. 43 incs. 2 y 4 Ley 25.326", "NO", "NO",
     ["Cargar el plazo de cumplimiento que fija la sentencia",
      "Pedir constancia de la supresión, rectificación o actualización y de su comunicación a los cesionarios",
      "En lo federal, controlar que la sentencia se comunique a la AAIP (art. 43 inc. 4)"],
     ["Constancia de cumplimiento"]),
    (i(510), "Cumplimiento", "Incumplimiento: astreintes y comunicación a la AAIP", "ACTORA",
     "Vencimiento del plazo de cumplimiento sin cumplir", 0, "SIN_PLAZO", "NO",
     "Art. 804 CCyC; arts. 31 y 43 inc. 4 Ley 25.326", "NO", "NO",
     ["Pedir astreintes e intimación bajo apercibimiento",
      "Informar el incumplimiento a la AAIP para que evalúe sanciones (art. 31)"],
     ["Escrito de intimación y astreintes"]),
    # --- Cierre ---
    (i(990), "Cierre", "Cierre y archivo del caso", "AMBAS",
     "Cumplimiento de la sentencia, rectificación voluntaria, desistimiento o rechazo firme con honorarios regulados",
     0, "SIN_PLAZO", "NO", "Reglamento de archivo del juzgado (a verificar)", "NO", "SI",
     ["Verificar honorarios y aportes",
      "Devolver la documentación al cliente y no conservar informes crediticios más allá de lo necesario"],
     ["Constancia de archivo"]),
]

HDA_FED_NODOS, HDA_FED_TRANS = bloque_amparo(
    P, 400, "FED", {"cumplimiento": i(500), "cierre": i(955)},
    ajustes={
        i(400): {
            "nombre": "Demanda de hábeas data federal (Ley 25.326)",
            "evento": "Negativa, silencio o respuesta insuficiente del responsable de un banco nacional o "
                      "interconectado",
            "base": "Art. 43 Constitución Nacional; arts. 33 a 38 Ley 25.326; Ley 16.986 y CPCCN (sumarísimo) "
                    "supletorios (art. 37)",
            "checklist": [
                "Competencia federal: banco público nacional o interconectado en redes interjurisdiccionales "
                "(arts. 36 y 44 Ley 25.326)",
                "Acreditar el reclamo previo y la negativa o el silencio (arts. 14, 16 y 38 inc. 2)",
                "Identificar el banco, su responsable y, si es público, el organismo del que depende (art. 38 inc. 1)",
                "Plazo para demandar: la Ley 25.326 no lo fija; controlar los 15 días del art. 2 inc. e Ley 16.986 "
                "como plazo suelto (ver duda)",
                "Pedir en el mismo escrito la anotación de litigiosidad o el bloqueo (art. 38 incs. 3 y 4)",
                *CHECKLIST_COSTOS_FED,
                CHECKLIST_SIN_DATOS,
            ],
        },
        i(410): {"nombre": "Admisión del hábeas data federal y rechazo in limine",
                 "base": "Arts. 38 inc. 5 y 39 Ley 25.326; art. 3 Ley 16.986"},
        i(420): {"nombre": "Informe del banco de datos (Ley 25.326)",
                 "evento": "Notificación del requerimiento de informe", "valor": 5, "tipo": "HABILES_JUDICIALES",
                 "gracia": "NO", "base": "Arts. 39 a 41 Ley 25.326",
                 "checklist": ["Plazo de hasta 5 días hábiles, ampliable por el juez: si fija otro, cargarlo",
                               "Los bancos privados no pueden alegar confidencialidad salvo fuentes periodísticas "
                               "(art. 40)",
                               "El informe explica por qué se incluyó el dato y por qué no se atendió el reclamo "
                               "(art. 41)",
                               FED]},
        i(450): {"nombre": "Sentencia de hábeas data federal",
                 "base": "Art. 43 Ley 25.326; arts. 8 y 11 Ley 16.986 (supletorios)",
                 "checklist": ["La Ley 25.326 no fija plazo; se carga el del amparo común (ver duda)",
                               "Controlar que diga si el dato se suprime, rectifica, actualiza o declara "
                               "confidencial, y el plazo para cumplir (art. 43 inc. 2)",
                               "Debe comunicarse a la AAIP (art. 43 inc. 4)"]},
    },
)
HON_NODOS, HON_TRANS = honorarios(P, 950, "AMBOS", i(990))
NODOS += HDA_FED_NODOS + HON_NODOS

TRANSICIONES = [
    # Encuadre
    (i(10), "Acceso a los datos", i(20)),
    (i(10), "Rectificación, actualización, supresión o confidencialidad", i(40)),
    (i(10), "Dato crediticio de una deuda cancelada o antigua", i(60)),
    (i(10), "Dato informado en la Central de Deudores del BCRA", i(70)),
    (i(10), "Perjuicio de imposible reparación: demanda sin reclamo previo en la provincia (art. 5 Ley 14.214)",
     i(200)),
    (i(10), "Perjuicio de imposible reparación: demanda sin reclamo previo contra un banco nacional o "
     "interconectado", i(400)),
    (i(20), "Solicitud entregada", i(30)),
    (i(30), "Información suficiente y correcta", i(990)),
    (i(30), "La información muestra datos falsos, inexactos o desactualizados", i(40)),
    (i(30), "Silencio o respuesta insuficiente: banco provincial", i(200)),
    (i(30), "Silencio o respuesta insuficiente: banco nacional o interconectado", i(400)),
    (i(40), "Reclamo entregado", i(50)),
    (i(50), "Dato rectificado, actualizado, suprimido o declarado confidencial", i(990)),
    (i(50), "Negativa o silencio: banco provincial", i(200)),
    (i(50), "Negativa o silencio: banco provincial", i(80)),
    (i(50), "Negativa o silencio: banco nacional o interconectado", i(400)),
    (i(50), "Negativa o silencio: banco nacional o interconectado", i(80)),
    (i(60), "Venció el plazo y el dato sigue informado: reclamar la supresión", i(40)),
    (i(60), "El dato dejó de informarse", i(990)),
    (i(70), "Entidad informante identificada y constancia reunida", i(40)),
    (i(80), "Denuncia presentada", CIERRA),
    # Demanda provincial
    (i(200), "Demanda presentada", i(210)),
    (i(200), "Se pide anotación de litigiosidad o bloqueo provisional", i(220)),
    (i(200), "Venció el plazo: reiterar el reclamo o la intimación previa (art. 7)", i(40)),
    (i(210), "Demanda admitida: se emplaza a informar", i(230)),
    (i(210), "Demanda rechazada in limine: se apela", i(260)),
    (i(220), "Medida resuelta por el juzgado provincial y se apela", i(225)),
    (i(220), "Medida resuelta por el juzgado federal y se apela", i(460)),
    (i(220), "Medida resuelta y no se apela", CIERRA),
    (i(225), "Apelación resuelta", CIERRA),
    (i(230), "Informe presentado o vencido: hay hechos controvertidos", i(240)),
    (i(230), "Informe presentado o vencido: no hay hechos controvertidos", i(250)),
    (i(240), "Prueba producida o vencido su plazo", i(250)),
    (i(250), "Sentencia notificada y se apela", i(260)),
    (i(250), "Sentencia favorable no apelada", i(500)),
    (i(250), "Rechazo no apelado", i(950)),
    (i(260), "Apelación concedida", i(270)),
    (i(260), "Apelación denegada: queda firme una decisión favorable", i(500)),
    (i(260), "Apelación denegada: queda firme el rechazo", i(950)),
    (i(270), "Sentencia favorable firme", i(500)),
    (i(270), "Rechazo firme", i(950)),
    # Federal: cautelar y ampliación
    (i(400), "Se pide anotación de litigiosidad o bloqueo provisional", i(220)),
    (i(420), "Informe contestado: se amplía la demanda (art. 42)", i(425)),
    (i(425), "Ampliación contestada o vencido el traslado: hay prueba que producir", i(430)),
    (i(425), "Ampliación contestada o vencido el traslado: sin prueba pendiente", i(450)),
    # Cumplimiento
    (i(500), "Cumplida: proceso provincial", i(950)),
    (i(500), "Cumplida: proceso federal", i(955)),
    (i(500), "Vencido el plazo sin cumplir", i(510)),
    (i(510), "Cumplimiento obtenido: proceso provincial", i(950)),
    (i(510), "Cumplimiento obtenido: proceso federal", i(955)),
] + HDA_FED_TRANS + HON_TRANS

NODOS, TRANSICIONES = ordenar(NODOS, TRANSICIONES)

DUDAS_PROPIAS = [
    ("Competencia: provincial o federal",
     "Art. 4 Ley 14.214: Civil y Comercial o Paz Letrado para bancos privados y Contencioso Administrativo para "
     "públicos provinciales. Art. 36 Ley 25.326: federal si el banco es público nacional o está interconectado en "
     "redes interjurisdiccionales. Las empresas de informes crediticios suelen estar interconectadas: ¿los juzgados "
     "provinciales aceptan esos casos o se declaran incompetentes? Propuesta: checklist en el encuadre que pida "
     "definirlo en cada caso. " + FUENTE_HD,
     "HDA_010, HDA_200, HDA_400"),
    ("Plazo de respuesta al pedido de acceso",
     "Ley 25.326 art. 14: 10 días corridos. Ley 14.214 art. 6: silencio a los 5 días hábiles (privados) o 15 "
     "(públicos). ¿Cuál rige para un banco provincial? Propuesta: cargar 10 días corridos y, si rige la Ley 14.214, "
     "el que venza antes como plazo suelto. " + FUENTE_HD,
     "HDA_030"),
    ("Plazo de respuesta al reclamo de rectificación",
     "Ley 25.326 art. 16: 5 días hábiles. ¿Son hábiles administrativos aunque el banco sea privado? ¿Para un banco "
     "público provincial rigen los 15 días del art. 6 Ley 14.214? Propuesta: 5 días hábiles administrativos (el más "
     "temprano). " + FUENTE_HD,
     "HDA_050"),
    ("Plazo de 60 días para la demanda provincial",
     "Art. 7 Ley 14.214: 60 días hábiles judiciales desde la notificación de la negativa; si vence, hay que reiterar "
     "la intimación. ¿Corre también desde el silencio (art. 6)? Propuesta: computarlo desde el silencio, que da el "
     "vencimiento más temprano. " + FUENTE_HD,
     "HDA_200"),
    ("Plazo para demandar en lo federal",
     "La Ley 25.326 no fija un plazo; el art. 37 remite al amparo común. ¿Se aplica el plazo de 15 días hábiles del "
     "art. 2 inc. e Ley 16.986? Propuesta: controlar los 15 días como plazo suelto hasta confirmar. " + FUENTE_HD,
     "HDA_400"),
    ("Trámite federal: informe, sentencia y recursos",
     "Art. 39: informe en hasta 5 días hábiles. La Ley 25.326 no fija plazos para la sentencia ni la apelación: ¿se "
     "usan los del amparo común (48 horas, art. 15 Ley 16.986) o los del sumarísimo del CPCCN? Propuesta: amparo "
     "común (los más breves). " + FUENTE_HD,
     "HDA_420, HDA_450, HDA_460, HDA_470"),
    ("Datos crediticios: cómputo del art. 26 inc. 4",
     "Solo se informan datos de los últimos 5 años, o 2 años desde la cancelación. ¿Desde cuándo se cuentan los 5 "
     "años (mora, último dato, vencimiento)? ¿Qué pasa con deudas prescriptas no canceladas? Propuesta: 2 años "
     "desde la cancelación como plazo del hito y 5 años como plazo suelto. " + FUENTE_HD,
     "HDA_060"),
    ("Central de Deudores del BCRA",
     "¿El reclamo se dirige solo a la entidad informante o también al BCRA? ¿Qué comunicación del BCRA regula hoy la "
     "rectificación y el plazo para que la entidad corrija? ¿Contra quién se demanda (legitimación pasiva)? "
     "Propuesta: reclamo y demanda contra la entidad informante; BCRA solo si no publica la corrección.",
     "HDA_070, HDA_040"),
    ("Denuncia ante la AAIP",
     "¿La AAIP interviene respecto de bancos públicos provinciales o solo nacionales y privados? ¿La denuncia "
     "suspende algún plazo? ¿Conviene presentarla siempre en paralelo? Propuesta: en paralelo y sin efecto sobre "
     "los plazos.",
     "HDA_080, HDA_510"),
    ("Anotación de litigiosidad y bloqueo provisional",
     "Ley 14.214 art. 10: solo después de presentada la demanda; apelación en 2 días (art. 16). En lo federal "
     "(art. 38 incs. 3 y 4 Ley 25.326), ¿la apelación de la cautelar sigue la Ley 16.986 (48 horas)? Propuesta: sí, "
     "con el plazo más breve. " + FUENTE_HD,
     "HDA_220, HDA_225, HDA_460"),
    ("Informe del banco público provincial",
     "Art. 13 Ley 14.214: 5 días hábiles para privados y 10 para públicos. El hito tiene 5 y el checklist pide "
     "cambiarlo a 10 si el banco es público. ¿Conviene separar dos hitos? Propuesta: un hito con 5 (vencimiento más "
     "temprano). " + FUENTE_HD,
     "HDA_230"),
    ("Comunicación de la sentencia a la AAIP",
     "Art. 43 inc. 4 Ley 25.326: la sentencia se comunica al órgano de control. ¿Lo hace el juzgado de oficio o la "
     "parte? ¿Rige para la sentencia provincial? Propuesta: checklist de control en el cumplimiento.",
     "HDA_500, HDA_510"),
    DUDA_REMITIR_TRANSVERSALES,
]

DUDAS = numerar(DUDAS_PROPIAS)
