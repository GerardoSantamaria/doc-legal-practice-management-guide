"""Amparo (AMP) — Ley 13.928 y art. 20 inc. 2 Constitución PBA; variante federal: art. 43 CN y Ley 16.986."""
from comun import (
    CHECKLIST_SIN_DATOS,
    CON_GRACIA,
    CON_VALOR_CERO,
    DUDA_REMITIR_TRANSVERSALES,
    ESTADOS,
    FUENTE_26854,
    FUENTE_AMPARO,
    INSTRUCCIONES_ADICIONALES,
    NOTA_FUENTES,
    NOTA_SENSIBLES,
    ROL_TEXTO,
    ROLES,
    ROLES_DESCRIPCION,
    ajustar,
    bloque_amparo,
    bloque_cautelar,
    ejecucion_estado,
    extraordinarios,
    flujo,
    honorarios,
    leyenda,
    numerar,
    ordenar,
    plazo_tipos,
)

P = "AMP"
i = lambda n: f"{P}_{n:03d}"

FLUJO = flujo(
    "Amparo (PBA, con variante federal)",
    "PBA",
    "Juzgado de primera instancia del lugar del acto (fuero según el demandado); variante federal",
    "Ley 13.928 (texto Leyes 14.192 y 15.016) con el CPCCBA supletorio (art. 25); variante federal: art. 43 "
    "Constitución Nacional, Ley 16.986 y CPCCN; cautelares contra el Estado nacional: Ley 26.854",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre el amparo de salud (reclamo previo, negativa o silencio, "
    "autosatisfactiva, cautelar con caución juratoria), el amparo contra actos u omisiones del Estado y de "
    "particulares, el amparo colectivo, la apelación, los recursos extraordinarios y el cumplimiento con astreintes. "
    "La competencia depende del demandado: IOMA, cajas y hospitales provinciales o municipales van a la justicia "
    "provincial; obras sociales nacionales, el Estado nacional y, según el caso, las prepagas, a la federal.",
)

FASES = [
    "Previa",
    "Vía administrativa",
    "Demanda",
    "Cautelares",
    "Prueba",
    "Sentencia",
    "Recursos",
    "Cumplimiento",
    "Ejecución",
    "Cierre",
]

GRUPOS = [
    ("Etapa previa: encuadre, competencia y amparo colectivo", ["Previa"]),
    ("Reclamo previo: vía administrativa o intimación al agente de salud", ["Vía administrativa"]),
    ("Demanda: amparo provincial (Ley 13.928) y federal (Ley 16.986)", ["Demanda"]),
    ("Medidas cautelares y autosatisfactiva", ["Cautelares"]),
    ("Prueba y sentencia", ["Prueba", "Sentencia"]),
    ("Recursos", ["Recursos"]),
    ("Cumplimiento, astreintes y ejecución contra el Estado", ["Cumplimiento", "Ejecución"]),
    ("Honorarios, derivación y cierre", ["Cierre"]),
]

LEYENDA = leyenda(
    paralelo="la cautelar otorgada abre a la vez el control de su cumplimiento y, contra el Estado nacional, el "
             "de su vigencia",
    adicionales=[
        "**Competencia según el demandado:** los caminos provincial (hitos AMP_200 a AMP_280) y federal (hitos "
        "AMP_400 a AMP_480) comparten fases; el nombre del hito dice cuál es.",
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": (
        "Ley 13.928: demanda en 30 días (art. 5), contestación en 5 (art. 10), prueba en 5 (art. 11), sentencia en "
        "5 (art. 13), apelación en 3 (art. 17), queja en 1 y alzada en 3; Ley 16.986: demanda en 15 días (art. 2 "
        "inc. e); informe previo de la Ley 26.854 en 3 días; recursos extraordinarios en 10 días."
    ),
    "HORAS": "sentencia sin prueba y apelación en 48 horas, recurso directo en 24 horas (arts. 8 y 15 Ley 16.986).",
    "MESES": "vigencia de la cautelar contra el Estado nacional en el amparo (3 meses, art. 5 Ley 26.854).",
    "FECHA_FIJADA": "audiencia simplificadora, informe y audiencia del amparo federal, y cumplimiento de órdenes.",
    "SIN_PLAZO": "decisiones del cliente, respuestas del agente de salud sin plazo legal, resoluciones del juzgado "
                 "sin plazo y plazos que fija el juez.",
})

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    # --- Previa ---
    (i(10), "Previa", "Encuadre del amparo, del demandado y del juzgado competente", "ACTORA",
     "Consulta del cliente por un acto u omisión lesiva", 0, "SIN_PLAZO", "NO",
     "Art. 20 inc. 2 Constitución PBA; arts. 1 a 3 Ley 13.928; art. 43 Constitución Nacional; Ley 16.986", "SI",
     "NO",
     ["Anotar la fecha en que el cliente conoció el acto u omisión: desde ahí corre el plazo para demandar",
      "Identificar al demandado: IOMA, caja, hospital o repartición provincial o municipal (justicia provincial); "
      "obra social nacional, Estado nacional o ente nacional (justicia federal); prepaga (ver duda de competencia)",
      "Evaluar si hay otra vía idónea sin daño grave o irreparable (art. 2 Ley 13.928; art. 2 inc. a Ley 16.986)",
      "No procede contra actos jurisdiccionales ni para la sola declaración de inconstitucionalidad de normas "
      "generales (art. 2 Ley 13.928)",
      CHECKLIST_SIN_DATOS],
     ["Constancia del acto u omisión", "Poder o patrocinio"]),
    (i(60), "Previa", "Consulta del registro de amparos y procesos colectivos antes de demandar", "ACTORA",
     "Decisión de promover un amparo por derechos de incidencia colectiva", 0, "SIN_PLAZO", "NO",
     "Arts. 4, 7, 8 y 21 Ley 13.928; registro federal: Acordadas CSJN 32/2014 y 12/2016 (a verificar)", "NO", "NO",
     ["Consultar el Registro Público de Amparos de Incidencia Colectiva de la SCBA (art. 21, consulta libre y "
      "gratuita) y, si es federal, el registro de la CSJN",
      "Si ya hay un proceso con el mismo objeto o colectivo, evaluar presentarse en él: la causa nueva se remite al "
      "juzgado que previno (art. 8)",
      "Definir el colectivo, los efectos comunes y la representación adecuada (art. 7)",
      "Prever la publicidad del proceso"],
     ["Constancia de consulta del registro"]),
    # --- Vía administrativa / reclamo previo ---
    (i(20), "Vía administrativa", "Pedido de cobertura o prestación al agente de salud", "ACTORA",
     "Indicación médica de una prestación, medicamento o tratamiento", 0, "SIN_PLAZO", "NO",
     "PMO (Resolución 201/2002 MS y modificatorias, a verificar); Ley 24.901 (discapacidad); Ley 26.682 "
     "(medicina prepaga); Leyes 23.660 y 23.661 (obras sociales); IOMA: Ley 6982 (a verificar)", "NO", "NO",
     ["Presentar el pedido por escrito y guardar la constancia de recepción",
      "Acompañar prescripción médica del profesional tratante, resumen de historia clínica y, si corresponde, el "
      "certificado único de discapacidad",
      "Si el agente es estatal provincial (IOMA, caja), es una presentación administrativa: no interrumpe el plazo "
      "del amparo (art. 5 Ley 13.928)",
      "Con prepagas u obras sociales es un reclamo extrajudicial",
      CHECKLIST_SIN_DATOS],
     ["Pedido de cobertura con constancia de recepción", "Prescripción médica", "Resumen de historia clínica",
      "Certificado único de discapacidad (si corresponde)", "Credencial de afiliación"]),
    (i(30), "Vía administrativa", "Intimación por carta documento al agente de salud", "ACTORA",
     "Silencio o demora en responder el pedido de cobertura", 0, "SIN_PLAZO", "NO",
     "Práctica previa al amparo de salud; Ley 26.682 y Leyes 23.660 y 23.661 (a verificar)", "NO", "NO",
     ["Intimar a cubrir en un plazo acorde con la urgencia y cargarlo como plazo suelto",
      "Mencionar la prestación por su nombre genérico, sin detallar el diagnóstico",
      "La intimación no interrumpe el plazo para demandar (art. 5 Ley 13.928)",
      "Opcional: reclamo ante la Superintendencia de Servicios de Salud (ver duda)"],
     ["Carta documento con aviso de entrega"]),
    (i(40), "Vía administrativa", "Respuesta, negativa o silencio del agente de salud", "DEMANDADA",
     "Pedido de cobertura o intimación recibidos por el agente de salud", 0, "SIN_PLAZO", "NO",
     "Sin plazo legal uniforme (ver duda); IOMA: Decreto-Ley 7647/70 (a verificar)", "NO", "NO",
     ["Si la intimación fijó un plazo, cargarlo como plazo suelto",
      "Guardar la negativa escrita o la constancia del silencio: es la prueba central del amparo",
      "Calcular el plazo para demandar desde la negativa o el silencio (ver duda sobre el plazo del amparo)"],
     ["Negativa escrita o constancia del silencio"]),
    # --- Cautelares: autosatisfactiva ---
    (i(330), "Cautelares", "Medida autosatisfactiva en salud (provincial): pedido, resolución y cumplimiento",
     "ACTORA", "Negativa o silencio del agente de salud con riesgo para la vida o la salud", 0, "SIN_PLAZO", "NO",
     "Creación jurisprudencial; art. 232 CPCCBA (medida genérica, a verificar)", "NO", "NO",
     ["Pedirla solo si la urgencia es extrema y el derecho es evidente: se agota con su cumplimiento",
      "Ofrecer caución juratoria",
      "Pedir que se ordene cumplir en horas y cargar ese vencimiento como plazo suelto",
      "Pedir habilitación de días y horas inhábiles o de feria",
      "Si se rechaza, promover el amparo dentro del plazo",
      CHECKLIST_SIN_DATOS],
     ["Escrito de autosatisfactiva", "Prescripción médica", "Negativa o constancia del silencio"]),
    # --- Cumplimiento ---
    (i(500), "Cumplimiento", "Cumplimiento de la sentencia de amparo en el plazo fijado", "DEMANDADA",
     "Notificación de la sentencia favorable firme (o de la que se cumple con efecto devolutivo)", 0, "FECHA_FIJADA",
     "NO", "Art. 14 inc. 3 Ley 13.928; art. 12 Ley 16.986", "NO", "NO",
     ["Cargar el plazo de cumplimiento que fijó la sentencia",
      "En la provincia la apelación tiene efecto devolutivo: la sentencia se cumple aunque esté apelada (art. 17)",
      "Pedir constancia de cumplimiento al cliente sin detallar la prestación"],
     ["Constancia de cumplimiento"]),
    (i(510), "Cumplimiento", "Astreintes e intimación por incumplimiento de la orden judicial", "ACTORA",
     "Vencimiento del plazo de cumplimiento de la sentencia o de la cautelar sin cumplir", 0, "SIN_PLAZO", "NO",
     "Art. 804 CCyC; art. 24 Ley 13.928; art. 239 Código Penal", "NO", "NO",
     ["Pedir astreintes; contra autoridades públicas el art. 804 CCyC remite al derecho administrativo (ver duda)",
      "Pedir la intimación personal al funcionario o directivo responsable",
      "Si la obstrucción es maliciosa, pedir que se remitan las actuaciones a la justicia penal (art. 24 Ley "
      "13.928; desobediencia, art. 239 Código Penal)"],
     ["Escrito de intimación y astreintes"]),
    (i(520), "Sentencia", "Sentencia de amparo firme tras los recursos extraordinarios", "TRIBUNAL",
     "Notificación de la decisión de la SCBA o de la CSJN, o denegatoria firme", 0, "SIN_PLAZO", "NO",
     "Art. 15 Ley 13.928; art. 13 Ley 16.986", "NO", "NO",
     ["La sentencia firme deja subsistentes otras acciones que correspondan (art. 15 Ley 13.928)",
      "Si es favorable, controlar el cumplimiento; si no, pasar a honorarios"],
     ["Constancia de firmeza"]),
    # --- Cierre ---
    (i(980), "Cierre", "Sigue en la matriz de contencioso administrativo", "ACTORA",
     "Hay otra vía idónea, venció el plazo del amparo o el caso requiere mayor debate y prueba", 0, "SIN_PLAZO",
     "NO", "Art. 2 inc. 1 Ley 13.928; Ley 12.008", "NO", "SI",
     ["Crear el expediente vinculado en la matriz de contencioso administrativo (o en la civil, si el demandado es "
      "un particular)",
      "Controlar el plazo de caducidad del art. 18 Ley 12.008 y el agotamiento de la vía"],
     []),
    (i(990), "Cierre", "Cierre y archivo del caso", "AMBAS",
     "Cumplimiento de la sentencia, cobertura otorgada, desistimiento o rechazo firme con honorarios regulados", 0,
     "SIN_PLAZO", "NO", "Reglamento de archivo del juzgado (a verificar)", "NO", "SI",
     ["Verificar pagos, honorarios y aportes",
      "Devolver la documentación original al cliente y no conservar copias de la historia clínica más allá de lo "
      "necesario"],
     ["Constancia de archivo"]),
]

AMP_PBA_NODOS, AMP_PBA_TRANS = bloque_amparo(
    P, 200, "PBA", {"cumplimiento": i(500), "cierre": i(950), "extraordinarios": i(600)},
    ajustes={i(200): {
        "nombre": "Demanda de amparo provincial (Ley 13.928) dentro de los 30 días",
        "evento": "Conocimiento del acto u omisión lesiva (si la lesión es periódica, cada una)",
        "valor": 30, "tipo": "HABILES_JUDICIALES", "gracia": "NO",
    }},
)
AMP_FED_NODOS, AMP_FED_TRANS = bloque_amparo(
    P, 400, "FED", {"cumplimiento": i(500), "cierre": i(955), "extraordinarios": i(610)},
    ajustes={i(400): {
        "nombre": "Demanda de amparo federal (Ley 16.986) dentro de los 15 días hábiles",
        "evento": "Fecha en que el acto se ejecutó o debió producirse",
        "valor": 15, "tipo": "HABILES_JUDICIALES", "gracia": "NO",
    }},
)
CAUT_NODOS, CAUT_TRANS = bloque_cautelar(P, 300, pba="AMPARO", fed="AMPARO", salidas={"incumplimiento": i(510)})
EXT_NODOS, EXT_TRANS = extraordinarios(P, 600, True, {"firme": i(520)})
EJE_NODOS, EJE_TRANS = ejecucion_estado(P, 800, "PBA", i(950), incluir=("liquidacion", "forzada", "pago"))
HON_NODOS, HON_TRANS = honorarios(P, 950, "AMBOS", i(990))
HON_NODOS = ajustar(HON_NODOS, {i(950): {"checklist": [
    "Pedir la regulación al terminar cada instancia",
    "Primera instancia: hasta 20 Jus (art. 20 bis Ley 13.928, Ley 15.016)",
    "Costas al vencido; sin costas si el acto cesó antes de vencer el plazo de contestación (art. 19 Ley 13.928)",
    "Apelar fundadamente dentro de los 5 días si la regulación es baja o alta (art. 57 Ley 14.967, a verificar)",
    "Pagar los aportes de la Ley 6716 sobre los honorarios y acreditarlos (plazo a verificar)",
]}})
NODOS += AMP_PBA_NODOS + AMP_FED_NODOS + CAUT_NODOS + EXT_NODOS + EJE_NODOS + HON_NODOS

TRANSICIONES = [
    # Encuadre
    (i(10), "Salud: falta de cobertura o de una prestación", i(20)),
    (i(10), "Acto u omisión de la Provincia, un municipio, un ente provincial o un particular: amparo provincial",
     i(200)),
    (i(10), "Acto u omisión del Estado nacional o de un ente nacional: amparo federal", i(400)),
    (i(10), "Derechos de incidencia colectiva", i(60)),
    (i(10), "Hay otra vía idónea o la cuestión requiere mayor debate", i(980)),
    (i(60), "No hay otro proceso colectivo con el mismo objeto: amparo colectivo provincial", i(200)),
    (i(60), "No hay otro proceso colectivo con el mismo objeto: amparo colectivo federal", i(400)),
    # Reclamo previo de salud
    (i(20), "Pedido presentado", i(40)),
    (i(30), "Carta documento entregada", i(40)),
    (i(40), "Cobertura otorgada", i(990)),
    (i(40), "Silencio o demora: intimar por carta documento", i(30)),
    (i(40), "Negativa o silencio de IOMA, una caja o un hospital provincial o municipal: amparo provincial", i(200)),
    (i(40), "Negativa o silencio de una obra social nacional, una prepaga o el Estado nacional: amparo federal",
     i(400)),
    (i(40), "Riesgo para la vida o la salud: medida autosatisfactiva", i(330)),
    (i(330), "Despachada y cumplida", i(950)),
    (i(330), "Despachada e incumplida", i(510)),
    (i(330), "Rechazada: se promueve el amparo", i(200)),
    # Demanda: plazo vencido y cautelar
    (i(200), "Venció el plazo sin demandar: evaluar otra vía", i(980)),
    (i(200), "Se pide una medida cautelar con la demanda", i(300)),
    (i(400), "Venció el plazo sin demandar: evaluar otra vía", i(980)),
    (i(400), "Se pide una medida cautelar con la demanda", i(300)),
    # Cumplimiento
    (i(500), "Cumplida: proceso provincial", i(950)),
    (i(500), "Cumplida: proceso federal", i(955)),
    (i(500), "Vencido el plazo sin cumplir", i(510)),
    (i(500), "La sentencia ordena pagar o reintegrar dinero a cargo del Estado provincial", i(830)),
    (i(510), "Cumplimiento obtenido: proceso provincial", i(950)),
    (i(510), "Cumplimiento obtenido: proceso federal", i(955)),
    (i(510), "El Estado provincial persiste en el incumplimiento", i(850)),
    (i(520), "Sentencia favorable firme", i(500)),
    (i(520), "Rechazo firme: proceso provincial", i(950)),
    (i(520), "Rechazo firme: proceso federal", i(955)),
] + AMP_PBA_TRANS + AMP_FED_TRANS + CAUT_TRANS + EXT_TRANS + EJE_TRANS + HON_TRANS

NODOS, TRANSICIONES = ordenar(NODOS, TRANSICIONES)

DUDAS_PROPIAS = [
    ("Competencia según el demandado",
     "Ley 13.928 art. 3: cualquier juez letrado de primera instancia del lugar donde el acto tiene efectos. IOMA, "
     "cajas y hospitales provinciales o municipales van a la justicia provincial (¿Contencioso Administrativo o "
     "Civil y Comercial?). Obras sociales nacionales: justicia federal (art. 38 Ley 23.661, a verificar). Prepagas: "
     "¿federal cuando actúan como agentes del seguro o provincial? La jurisprudencia está dividida (a verificar). "
     "Propuesta: checklist en el encuadre que pida definirlo en cada caso. " + FUENTE_AMPARO,
     "AMP_010, AMP_040, AMP_200, AMP_400"),
    ("Tipo de días del plazo de 30 días para el amparo provincial",
     "Art. 5 Ley 13.928: 30 días desde el conocimiento del acto; no lo interrumpen intimaciones ni presentaciones "
     "administrativas; los términos son perentorios (art. 18). Con el CPCCBA supletorio (art. 25) serían días "
     "hábiles judiciales. ¿Lo confirman, o algún juzgado los computa corridos? Propuesta: 30 días hábiles "
     "judiciales sin gracia y, mientras no se confirme, que el abogado controle también el vencimiento en días "
     "corridos (el más temprano). " + FUENTE_AMPARO,
     "AMP_200"),
    ("Plazo de 15 días hábiles del amparo federal",
     "Art. 2 inc. e Ley 16.986: 15 días hábiles desde que el acto se ejecutó o debió producirse. Parte de la "
     "jurisprudencia lo considera incompatible con el art. 43 CN o no lo aplica a omisiones continuadas. ¿Se "
     "mantiene como plazo de control? Propuesta: sí, sin gracia (vencimiento más temprano). " + FUENTE_AMPARO,
     "AMP_400"),
    ("Proceso aplicable contra prepagas y particulares en la justicia federal",
     "La Ley 16.986 regula el amparo contra autoridades públicas; contra particulares rige el sumarísimo del "
     "CPCCN (arts. 321 y 498, a verificar). ¿Qué plazos de contestación y de apelación usan los juzgados federales "
     "con prepagas y obras sociales? Propuesta: usar los plazos de la Ley 16.986 (más breves) hasta confirmar.",
     "AMP_400, AMP_420, AMP_460"),
    ("Cautelares contra el Estado nacional en salud",
     "Ley 26.854: informe previo en 3 días en el amparo (art. 4) y vigencia de 3 meses (art. 5), salvo los "
     "supuestos del art. 2 inc. 2 (vida digna, salud, alimentario, sectores vulnerables). ¿La mayoría de los "
     "amparos de salud quedan en la excepción? ¿Se cierra el camino del informe previo en esos casos? Propuesta: "
     "checklist que pida invocar la excepción y cerrar esos hitos. " + FUENTE_26854,
     "AMP_300, AMP_315, AMP_350"),
    ("Medida autosatisfactiva",
     "No está regulada en el CPCCBA ni en la Ley 13.928: es de creación jurisprudencial. ¿Se usa en la práctica "
     "bonaerense para salud, o se prefiere la cautelar dentro del amparo? ¿Qué contracautela se exige? Propuesta: "
     "dejarla como camino excepcional con caución juratoria y plazo de cumplimiento cargado como plazo suelto.",
     "AMP_330"),
    ("Amparo colectivo: registros",
     "Arts. 8 y 21 Ley 13.928: Registro Público de Amparos de Incidencia Colectiva de la SCBA, que informa en 2 días. "
     "¿Cuál es la acordada vigente que lo reglamenta? En lo federal, ¿siguen vigentes las Acordadas CSJN 32/2014 y "
     "12/2016? ¿Hace falta un hito para el informe del registro? Propuesta: checklist en la admisibilidad. "
     + FUENTE_AMPARO,
     "AMP_060, AMP_210"),
    ("Efecto de la apelación",
     "Provincia: efecto devolutivo, excepcionalmente suspensivo (art. 17 Ley 13.928). Nación: la Ley 16.986 "
     "(art. 15) concede la apelación en ambos efectos, pero contra la medida de no innovar el efecto es devolutivo "
     "(a verificar). ¿Cómo debe tratar la app el cumplimiento mientras la apelación está pendiente? Propuesta: el "
     "plazo de cumplimiento se abre con la sentencia provincial aunque se apele, y con la firme en lo federal. "
     + FUENTE_AMPARO,
     "AMP_260, AMP_460, AMP_345, AMP_500"),
    ("Plazo de respuesta del agente de salud y Superintendencia",
     "No hay un plazo legal uniforme para que una obra social o una prepaga responda un pedido de cobertura. ¿Hay "
     "plazos en resoluciones de la Superintendencia de Servicios de Salud o del IOMA (a verificar)? ¿El reclamo ante "
     "la Superintendencia es un paso que conviene modelar o es optativo? Propuesta: SIN_PLAZO con plazo suelto de "
     "la intimación, y Superintendencia optativa.",
     "AMP_020, AMP_030, AMP_040"),
    ("Documentación médica y datos de salud",
     "¿Qué exige la práctica para el amparo de salud (prescripción del médico tratante, resumen de historia clínica, "
     "certificado único de discapacidad para la Ley 24.901)? Los checklists nombran los documentos sin su contenido. "
     "¿Hay que pedir el consentimiento del cliente para cargar la historia clínica en la app? Relacionado con la "
     "duda de producto sobre datos sensibles.",
     "AMP_020, AMP_330"),
    ("Astreintes contra el Estado",
     "El art. 804 CCyC dice que la observancia de los mandatos judiciales a las autoridades públicas se rige por el "
     "derecho administrativo. ¿Qué norma provincial habilita las astreintes contra la Provincia o sus funcionarios "
     "en el amparo (arts. 63 y 64 Ley 12.008 por remisión, a verificar)? Propuesta: checklist que pida las "
     "astreintes con esa fundamentación.",
     "AMP_325, AMP_510, AMP_850"),
    ("Ejecución contra el Estado de una condena de amparo",
     "Si la sentencia de amparo ordena pagar o reintegrar dinero (por ejemplo, gastos de una prestación), ¿rige el "
     "plazo de 60 días del art. 163 Constitución PBA o solo el que fija la sentencia? ¿Hace falta previsión "
     "presupuestaria? Propuesta: el plazo de la sentencia, y liquidación y pago como en contencioso.",
     "AMP_500, AMP_830, AMP_850"),
    ("Caducidad de instancia en el amparo",
     "La Ley 13.928 no la regula; el CPCCBA supletorio prevé plazos más breves para los procesos sumarísimos (a "
     "verificar). ¿Se modela un control de caducidad de instancia? Propuesta: no en V1, por la brevedad de los "
     "plazos del amparo.",
     "AMP_220, AMP_420"),
    ("Honorarios en el amparo",
     "Provincia: hasta 20 Jus en primera instancia (art. 20 bis Ley 13.928, Ley 15.016) y costas al vencido "
     "(art. 19). Nación: Ley 27.423 (¿hay mínimo o escala propia para el amparo?, a verificar). ¿El tope de 20 Jus "
     "rige también para la alzada? " + FUENTE_AMPARO,
     "AMP_950, AMP_955"),
    ("Amparo contra particulares en la Provincia",
     "El art. 20 inc. 2 Constitución PBA y la Ley 13.928 (art. 14) admiten el amparo contra particulares. ¿Qué "
     "fuero lo recibe (Civil y Comercial) y cuál es la alzada, si no rige el art. 17 bis? Propuesta: Civil y "
     "Comercial con su Cámara.",
     "AMP_010, AMP_260"),
    DUDA_REMITIR_TRANSVERSALES,
]

DUDAS = numerar(DUDAS_PROPIAS)
