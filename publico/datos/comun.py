"""Partes comunes de las matrices de Derecho Público y Constitucional (PBA, con variantes federales).

No importa nada de civil/, laboral/, familia/, comercial/ ni penal/: el contencioso administrativo, el amparo, la
seguridad social y el hábeas data tienen plazos, roles y vía administrativa propios.
Las dudas transversales y de producto se responden una sola vez en la matriz de contencioso administrativo.
"""
import datos

ROLES = datos.ROLES
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS
CIERRA = ""

FUENTE_CCA = ("Fuente consultada el 13/11/2026: Ley 12.008 (texto con Leyes 12.310, 13.101, 13.325 y 14.437) en "
              "normas.gba.gob.ar y leyes-ar.com (actualización 16/10/2026); se cita la numeración oficial.")
FUENTE_7647 = ("Fuente consultada el 13/11/2026: Decreto-Ley 7647/70 en normas.gba.gob.ar; la Ordenanza General "
               "267/80 (municipios) reproduce la numeración.")
FUENTE_LPA = ("Fuente consultada el 13/11/2026: Ley 19.549 con la reforma de la Ley 27.742 (B.O. 08/07/2024) en "
              "argentina.gob.ar.")
FUENTE_24463 = ("Fuente consultada el 13/11/2026: Ley 24.463 (art. 15 según Ley 24.655; art. 19 derogado por la Ley "
                "26.025; arts. 16, 17, 20 y 23 derogados por la Ley 26.153) en argentina.gob.ar y leyes-ar.com; "
                "CSJN 'Pedraza' (06/05/2014) sobre el art. 18.")
FUENTE_AMPARO = ("Fuentes consultadas el 13/11/2026: Ley 13.928 (texto con Leyes 14.192 y 15.016) en "
                 "normas.gba.gob.ar; Ley 16.986 en argentina.gob.ar y texto actualizado de hcdn.gob.ar.")
FUENTE_26854 = ("Fuente consultada el 13/11/2026: Ley 26.854 en biblioteca.arca.gob.ar e InfoLEG; leyes-ar.com la "
                "informa vigente (actualización 22/04/2026).")
FUENTE_HD = ("Fuentes consultadas el 13/11/2026: Ley 14.214 en normas.gba.gob.ar y Ley 25.326 en argentina.gob.ar "
             "(proyectos de reforma 1751-D-2026 y 3397-D-2026 sin dictamen al 26/09/2026).")
FUENTE_CF = ("Fuente consultada el 13/11/2026: Código Fiscal PBA (Ley 10.397, t.o. 2011) en leyes-ar.com y guía de "
             "trámites de ARBA.")

DESCRIPCION_PLAZOS = {
    "HABILES_JUDICIALES": (
        "Días hábiles judiciales del calendario del expediente. En el fuero provincial (Ley 12.008, Ley 13.928, "
        "Ley 14.214) rige el CPCCBA como supletorio y la gracia del art. 124 se marca en los escritos de parte. En "
        "los caminos federales (CPCCN) se marca Aplica_Gracia = NO hasta que el motor soporte el calendario y la "
        "gracia federales (ver dudas de producto)."
    ),
    "CORRIDOS": (
        "Días corridos. En estas matrices solo se usa donde la ley lo dice (acceso a datos personales: 10 días "
        "corridos, art. 14 Ley 25.326)."
    ),
    "HABILES_ADMINISTRATIVOS": (
        "Días hábiles administrativos (regla R6 del motor: lunes a viernes sin feriados; las ferias judiciales no "
        "suspenden). Se usa en la vía administrativa: recursos, reclamos y plazos para que la Administración "
        "resuelva. El checklist de cada hito dice qué calendario administrativo aplica (provincial, municipal o "
        "nacional). Sin gracia."
    ),
    "MESES": (
        "Meses, de fecha a fecha (regla R7). Caducidad de instancia (art. 62 Ley 12.008) y vigencia de cautelares "
        "contra el Estado nacional (art. 5 Ley 26.854). Sin gracia en estas matrices."
    ),
    "ANIOS": (
        "Años, de fecha a fecha (regla R7). Prescripción de acciones y plazos de conservación de datos. Sin gracia."
    ),
    "HORAS": (
        "Horas corridas desde la fecha y hora del disparador (regla R8). Plazos del amparo federal (Ley 16.986: 48 y "
        "24 horas) y mejora de fundamentos del jerárquico en subsidio (48 horas, art. 91 Decreto-Ley 7647/70). "
        "Sin gracia. Ver duda transversal sobre el cómputo."
    ),
    "FECHA_FIJADA": (
        "Acto o vencimiento con fecha y hora fijadas por el juzgado (audiencias, informe del amparo federal, "
        "cumplimiento de una orden). Valor 0: el abogado carga la fecha y la hora."
    ),
    "ANTICIPACION_HABILES_JUDICIALES": (
        "Días hábiles judiciales contados hacia atrás desde un acto fijado (regla R9). No se usa en estas matrices."
    ),
    "SIN_PLAZO": (
        "Sin plazo perentorio (valor 0): depende del juzgado, de la Administración o de la decisión del cliente. Si "
        "el juez fija el plazo en cada caso, el checklist pide cargarlo como plazo suelto."
    ),
}
assert set(DESCRIPCION_PLAZOS) == {t for t, _ in datos.PLAZO_TIPOS}


def plazo_tipos(usos):
    return [(t, f"{DESCRIPCION_PLAZOS[t]} En este flujo: {usos.get(t, 'no se usa.')}") for t, _ in datos.PLAZO_TIPOS]


def flujo(nombre, jurisdiccion, fuero, regimen, notas):
    return {
        "Flujo": nombre,
        "Jurisdicción": jurisdiccion,
        "Fuero": fuero,
        "Régimen procesal": regimen,
        "Versión": "1 (borrador)",
        "Fecha del borrador": "13/11/2026",
        "Validado por (equipo legal)": "",
        "Fecha de validación": "",
        "Notas": notas,
    }


NOTA_FUENTES = (
    "Borrador para validar con el abogado. Las citas se cotejaron el 13/11/2026 con normas.gba.gob.ar, "
    "argentina.gob.ar, hcdn.gob.ar y leyes-ar.com; las que no se pudieron confirmar dicen '(a verificar)' y tienen "
    "su duda. No contiene ni debe contener datos personales de nadie."
)

NOTA_SENSIBLES = (
    "Datos sensibles: estos expedientes pueden incluir datos de salud, previsionales y crediticios. No escribas "
    "nombres, DNI, CUIL, números de beneficio, diagnósticos ni montos de un caso en las celdas: nombrá los documentos "
    "(historia clínica, recibo de haberes), no su contenido."
)

CHECKLIST_COSTOS_PBA = [
    "Tasa de justicia y contribución del art. 12 inc. g Ley 6716: verificar si el proceso está exento (ver duda "
    "transversal de tasas)",
    "Bono de la Ley 8480 y anticipo previsional del art. 13 Ley 6716 por cada letrado",
    "Si el cliente no puede afrontar los gastos, iniciar el beneficio de litigar sin gastos (arts. 78 a 86 CPCCBA) "
    "en paralelo con la demanda",
]

CHECKLIST_COSTOS_FED = [
    "Tasa de justicia federal (Ley 23.898): verificar la exención que corresponda (ver duda transversal de tasas)",
    "Aportes y bono del letrado en causas federales con asiento en PBA: verificar qué exige la Caja de Abogados "
    "(a verificar)",
    "Si el cliente no puede afrontar los gastos, iniciar el beneficio de litigar sin gastos (arts. 78 a 86 CPCCN)",
]

CHECKLIST_SIN_DATOS = ("No cargar en la app nombres, documentos de identidad, números de beneficio ni diagnósticos: "
                       "nombrar los documentos, no su contenido")

ROLES_DESCRIPCION = [
    ("ACTORA",
     "El particular: la persona o empresa que reclama contra el Estado, el organismo, el agente de salud o el "
     "responsable de la base de datos. Es a quien representa el abogado en estas matrices."),
    ("DEMANDADA",
     "El Estado o el organismo demandado (Provincia, municipio, ente, ARBA, ANSES, IPS, caja profesional, obra "
     "social, prepaga o banco de datos), también mientras resuelve en la vía administrativa: el nombre del hito "
     "dice quién (por ejemplo, 'ANSES resuelve el reclamo')."),
    ("TRIBUNAL",
     "Juzgados y tribunales (Juzgado y Cámara en lo Contencioso Administrativo, SCBA, juzgados federales, Cámara "
     "Federal de la Seguridad Social, CSJN) y organismos de control que no son parte (AAIP, Tribunal Fiscal de "
     "Apelación), aclarado en el nombre del hito."),
    ("AMBAS",
     "Cualquiera de las partes: recursos, audiencias, alegatos, honorarios."),
]

ROL_TEXTO = {
    "ACTORA": "Particular",
    "DEMANDADA": "Estado u organismo",
    "TRIBUNAL": "Juzgado u organismo de control",
    "AMBAS": "Cualquiera de las partes",
}

LEYENDA = {
    "roles": (
        "celeste = el particular que reclama (ACTORA); naranja = el Estado o el organismo demandado, también cuando "
        "resuelve en la vía administrativa (DEMANDADA); gris = juzgado, tribunal u organismo de control que no es "
        "parte, como la AAIP o el Tribunal Fiscal de Apelación (TRIBUNAL); violeta = cualquiera de las partes "
        "(AMBAS)."
    ),
    "paralelo": "con la demanda se abren a la vez el pedido de la medida cautelar y el control de la caducidad",
    "adicionales": [
        "**Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con \"Sigue en la "
        "matriz de ...\": el caso continúa en otra matriz de Derecho Público, en un expediente vinculado.",
        "**Provincial o federal:** cuando un flujo tiene las dos variantes, el nombre del hito lo dice "
        "(\"provincial\" o \"federal\") o nombra la ley que lo rige (por ejemplo, \"Ley 13.928\" o \"Ley 16.986\").",
        "**Vía administrativa:** sus hitos están en un diagrama aparte de los judiciales. La Administración que "
        "resuelve aparece en naranja, como parte demandada, y sus plazos son días hábiles administrativos.",
    ],
}


def leyenda(roles=None, paralelo=None, adicionales=None):
    return {
        "roles": roles or LEYENDA["roles"],
        "paralelo": paralelo or LEYENDA["paralelo"],
        "adicionales": LEYENDA["adicionales"] + (adicionales or []),
    }


INSTRUCCIONES_ADICIONALES = [
    ("Particularidades de Derecho Público", True),
    ("9. Vía administrativa: los recursos, reclamos y plazos para que la Administración resuelva usan "
     "HABILES_ADMINISTRATIVOS (sin gracia). El checklist de cada hito dice qué calendario administrativo aplica "
     "(provincial, municipal o nacional).", False),
    ("10. Gracia según la jurisdicción: Aplica_Gracia = SI solo en escritos de parte ante la justicia provincial, "
     "donde el CPCCBA es supletorio. En los caminos federales es NO hasta que se resuelva la duda sobre la gracia del "
     "CPCCN y el calendario federal. Los plazos para demandar (caducidad) van sin gracia.", False),
    ("11. Provincial o federal: si el flujo tiene las dos variantes, el nombre del hito dice cuál es o nombra la ley "
     "que lo rige.", False),
    ("12. Plazo fijado por el juez: el hito usa SIN_PLAZO o FECHA_FIJADA y el checklist pide cargar el vencimiento "
     "como plazo suelto en cada expediente.", False),
    ("13. Derivación a otra matriz: los hitos finales 'Sigue en la matriz de ...' indican que el caso continúa en "
     "otro flujo de Derecho Público (por ejemplo, el reclamo ante el IPS sigue en contencioso administrativo).",
     False),
    ("14. Rol DEMANDADA en la vía administrativa: la Administración que resuelve un reclamo o recurso es la parte "
     "demandada; el nombre del hito dice quién resuelve.", False),
    ("15. Datos sensibles: no escribas nombres, DNI, CUIL, números de beneficio, diagnósticos ni montos de un caso. "
     "Nombrá los documentos (historia clínica, recibo de haberes), no su contenido.", False),
    ("", False),
]

CAMPOS = {"nombre": 2, "rol": 3, "evento": 4, "valor": 5, "tipo": 6, "gracia": 7, "base": 8,
          "checklist": 11, "documentacion": 12}


def ajustar(nodos, ajustes):
    resultado = []
    for n in nodos:
        nodo = list(n)
        for campo, valor in (ajustes or {}).get(nodo[0], {}).items():
            nodo[CAMPOS[campo]] = valor
        resultado.append(tuple(nodo))
    return resultado


def filtrar(nodos, transiciones, omitir):
    omitir = set(omitir or ())
    nodos = [n for n in nodos if n[0] not in omitir]
    transiciones = [t for t in transiciones if t[0] not in omitir and t[2] not in omitir]
    return nodos, transiciones


def ordenar(nodos, transiciones):
    nodos = sorted(nodos, key=lambda n: int(n[0].split("_")[1]))
    posicion = {n[0]: i for i, n in enumerate(nodos)}
    return nodos, sorted(transiciones, key=lambda t: posicion[t[0]])


def numerar(dudas):
    return [(f"D{i:02d}", *d) for i, d in enumerate(dudas, start=1)]


# --- Amparo: procedimiento común con variante provincial (Ley 13.928) y federal (Ley 16.986) ---------------------

def bloque_amparo(p, base, variante, salidas, omitir=(), ajustes=None):
    """Demanda, admisibilidad, informe, audiencia y prueba, sentencia, apelación, queja y alzada.
    `variante` es "PBA" (Ley 13.928) o "FED" (Ley 16.986). `salidas` tiene "cumplimiento" (sentencia favorable
    firme), "cierre" (rechazo firme o desistimiento) y, opcional, "extraordinarios"."""
    i = lambda n: f"{p}_{base + n}"
    pba = variante == "PBA"
    if pba:
        nodos = [
            (i(0), "Demanda", "Demanda de amparo provincial (Ley 13.928)", "ACTORA",
             "Decisión de demandar ante la negativa, el silencio o el acto lesivo", 0, "SIN_PLAZO", "NO",
             "Art. 20 inc. 2 Constitución PBA; arts. 1 a 6 Ley 13.928 (texto Ley 14.192)", "NO", "NO",
             ["Presentar dentro de los 30 días del conocimiento del acto u omisión (art. 5): las intimaciones y las "
              "presentaciones administrativas no interrumpen el plazo; si la lesión es periódica, corre por cada una",
              "Acreditar la arbitrariedad o ilegalidad manifiesta y que los remedios ordinarios causarían un daño "
              "grave o irreparable (art. 2 inc. 1)",
              "Juez letrado de primera instancia del lugar donde el acto tiene efectos (art. 3); fuero según el "
              "demandado (ver duda de competencia)",
              "Requisitos del art. 6; en amparos colectivos, los efectos comunes y la representación adecuada (art. 7)",
              "Acompañar la prueba documental y ofrecer el resto con la demanda (art. 6 inc. 5)",
              "Pedir la medida cautelar en el mismo escrito si hay urgencia (art. 9)",
              "Exento de tasa de justicia, sellado y todo otro tributo (art. 20); bono de la Ley 8480 y anticipo "
              "previsional del art. 13 Ley 6716 por cada letrado",
              CHECKLIST_COSTOS_PBA[2],
              CHECKLIST_SIN_DATOS],
             ["Demanda", "Poder o patrocinio", "Prueba documental", "Constancia de la negativa o del silencio"]),
            (i(10), "Demanda", "Admisibilidad del amparo provincial y otra vía idónea", "TRIBUNAL",
             "Presentación de la demanda", 0, "SIN_PLAZO", "NO",
             "Arts. 2, 8 y 9 Ley 13.928", "NO", "NO",
             ["El juez se expide inmediatamente; si la acción es manifiestamente inadmisible la rechaza sin "
              "sustanciación (art. 8)",
              "El rechazo in limine es apelable en 3 días (arts. 16 inc. 1 y 17)",
              "La cautelar pedida con la demanda se resuelve junto con la admisibilidad (art. 9)",
              "Amparo colectivo: el juez ordena inscribirlo en el Registro Público de Amparos de Incidencia "
              "Colectiva de la SCBA, que informa en 2 días si hay otros juicios; si los hay, la causa va al juzgado "
              "que previno (arts. 8 y 21)",
              "Si el juzgado se declara incompetente, controlar la remisión y que la cautelar no se pierda"],
             ["Providencia de admisión o rechazo"]),
            (i(20), "Demanda", "Contestación de la demanda de amparo (Ley 13.928)", "DEMANDADA",
             "Notificación del traslado de la demanda (por cédula o personalmente, art. 18)", 5,
             "HABILES_JUDICIALES", "SI", "Arts. 10, 18 y 22 Ley 13.928", "NO", "NO",
             ["Plazo de 5 días, que el juez puede adecuar a la naturaleza del caso: si fija otro, cargarlo como "
              "plazo suelto",
              "No se admiten cuestiones previas, reconvención ni incidentes (art. 22)",
              "Si el acto u omisión cesa antes de vencer este plazo, no hay condena en costas (art. 19)",
              "Si niega los hechos, habrá audiencia y prueba"],
             ["Contestación de la demanda"]),
            (i(30), "Prueba", "Audiencia simplificadora (Ley 13.928)", "AMBAS",
             "Fecha y hora fijadas por el juez con el traslado (dentro de los 10 días)", 0, "FECHA_FIJADA", "NO",
             "Art. 11 Ley 13.928", "NO", "NO",
             ["Asistir siempre: si la actora no comparece por sí o por apoderado, se la tiene por desistida con "
              "costas (art. 11 inc. 1)",
              "El juez invita a conciliar, revisa las cautelares y provee la prueba",
              "Llevar una propuesta de cumplimiento si hay margen de acuerdo"],
             ["Acta de la audiencia"]),
            (i(40), "Prueba", "Producción de la prueba (Ley 13.928)", "AMBAS",
             "Audiencia simplificadora que provee la prueba", 5, "HABILES_JUDICIALES", "NO",
             "Arts. 11 inc. 3, 12 y 18 Ley 13.928", "NO", "NO",
             ["La prueba se produce dentro de 5 días; los términos son perentorios (art. 18)",
              "Urgir informes y pericias; el juez puede ordenar medidas para mejor proveer (art. 12)",
              CHECKLIST_SIN_DATOS],
             ["Constancias de prueba"]),
            (i(50), "Sentencia", "Sentencia de amparo (Ley 13.928)", "TRIBUNAL",
             "Prueba producida o vencido su plazo, o contestación sin prueba que producir", 5, "HABILES_JUDICIALES",
             "NO", "Arts. 13 y 14 Ley 13.928", "NO", "NO",
             ["Controlar que nombre al obligado, la conducta a cumplir y el plazo de cumplimiento (art. 14)",
              "Costas al vencido (art. 19); honorarios de primera instancia hasta 20 Jus (art. 20 bis)"],
             ["Sentencia"]),
            (i(60), "Recursos", "Apelación en el amparo provincial (3 días)", "AMBAS",
             "Notificación de la sentencia, del rechazo in limine o de la resolución cautelar apelable", 3,
             "HABILES_JUDICIALES", "SI", "Arts. 16, 17 y 17 bis Ley 13.928", "NO", "NO",
             ["Interponer y fundar en el mismo escrito dentro de los 3 días, ante el juez que dictó la decisión",
              "Efecto devolutivo; excepcionalmente y con fundamento, suspensivo (art. 17)",
              "Traslado a la contraria por 3 días; el juez eleva en igual plazo",
              "Si se cuestiona la función administrativa de la Provincia, un municipio o un ente, la alzada es la "
              "Cámara en lo Contencioso Administrativo (art. 17 bis)"],
             ["Escrito de apelación fundado"]),
            (i(70), "Recursos", "Queja por apelación denegada en el amparo provincial (1 día)", "AMBAS",
             "Notificación de la denegatoria de la apelación", 1, "HABILES_JUDICIALES", "SI",
             "Art. 17 Ley 13.928", "NO", "NO",
             ["Plazo de 1 día: preparar la queja apenas llega la notificación",
              "Acompañar copia de la resolución recurrida, del recurso y de la denegatoria"],
             ["Escrito de queja"]),
            (i(80), "Recursos", "Sentencia de la alzada en el amparo provincial", "TRIBUNAL",
             "Recepción del expediente en la alzada", 3, "HABILES_JUDICIALES", "NO",
             "Arts. 17 y 17 bis Ley 13.928", "NO", "NO",
             ["La alzada resuelve dentro de 3 días de recibido el expediente; 3 días también tras la queja",
              "Si se demora, pedir pronto despacho",
              "Evaluar recursos extraordinarios ante la SCBA"],
             ["Sentencia de la alzada"]),
        ]
    else:
        nodos = [
            (i(0), "Demanda", "Demanda de amparo federal (Ley 16.986 o art. 43 CN)", "ACTORA",
             "Decisión de demandar ante la negativa, el silencio o el acto lesivo", 0, "SIN_PLAZO", "NO",
             "Art. 43 Constitución Nacional; arts. 1, 2, 4, 6 y 7 Ley 16.986; contra particulares, arts. 321 y 498 "
             "CPCCN (a verificar)", "NO", "NO",
             ["Presentar dentro de los 15 días hábiles desde que el acto se ejecutó o debió producirse (art. 2 "
              "inc. e Ley 16.986): ver duda sobre su vigencia tras el art. 43 CN",
              "Juez del lugar donde el acto se exterioriza o tiene efecto (art. 4 Ley 16.986); fuero según el "
              "demandado (ver duda de competencia)",
              "Contra prepagas u obras sociales: verificar si el juzgado aplica la Ley 16.986 por analogía o el "
              "proceso sumarísimo del CPCCN",
              "Acompañar la prueba instrumental; hasta 5 testigos; no se admite absolución de posiciones (art. 7)",
              *CHECKLIST_COSTOS_FED,
              CHECKLIST_SIN_DATOS],
             ["Demanda", "Poder o patrocinio", "Prueba documental", "Constancia de la negativa o del silencio"]),
            (i(10), "Demanda", "Admisibilidad del amparo federal y rechazo in limine", "TRIBUNAL",
             "Presentación de la demanda", 0, "SIN_PLAZO", "NO", "Art. 3 Ley 16.986", "NO", "NO",
             ["Si es manifiestamente inadmisible, el juez la rechaza sin sustanciación (art. 3)",
              "Esa resolución es apelable en 48 horas (art. 15)"],
             ["Providencia de admisión o rechazo"]),
            (i(20), "Demanda", "Informe circunstanciado del demandado (Ley 16.986)", "DEMANDADA",
             "Notificación del requerimiento de informe", 0, "FECHA_FIJADA", "NO", "Art. 8 Ley 16.986", "NO", "NO",
             ["El juez fija un plazo prudencial: cargar la fecha y hora de vencimiento",
              "La omisión del pedido de informe es causa de nulidad del proceso",
              "El requerido ofrece su prueba con el informe",
              "Si se demanda al Estado nacional, el informe previo de la cautelar es otro plazo (art. 4 Ley 26.854)"],
             ["Informe circunstanciado"]),
            (i(30), "Prueba", "Audiencia de prueba en el amparo federal", "AMBAS",
             "Fecha y hora fijadas por el juez (dentro del tercer día)", 0, "FECHA_FIJADA", "NO",
             "Arts. 9 y 10 Ley 16.986", "NO", "NO",
             ["Asistir siempre: si la actora no comparece, se la tiene por desistida con costas (art. 10)",
              "Hacer comparecer a los testigos propios"],
             ["Acta de la audiencia"]),
            (i(50), "Sentencia", "Sentencia de amparo federal", "TRIBUNAL",
             "Informe presentado o vencido sin prueba pendiente (48 horas); o audiencia de prueba realizada (3 días)",
             48, "HORAS", "NO", "Arts. 8, 11 y 12 Ley 16.986", "NO", "NO",
             ["Sin prueba pendiente: 48 horas desde el informe o su vencimiento (art. 8)",
              "Con audiencia de prueba: 3 días (art. 11); cargar ese plazo como plazo suelto",
              "Controlar que fije la conducta y el plazo de cumplimiento (art. 12)"],
             ["Sentencia"]),
            (i(60), "Recursos", "Apelación en el amparo federal (48 horas)", "AMBAS",
             "Notificación de la sentencia, del rechazo in limine o de la medida de no innovar o suspensión", 48,
             "HORAS", "NO", "Art. 15 Ley 16.986", "NO", "NO",
             ["Interponer y fundar dentro de las 48 horas de notificada la resolución",
              "Se concede en ambos efectos dentro de las 48 horas y se eleva en 24 horas",
              "Ver la duda sobre el cómputo de las horas y la gracia del CPCCN"],
             ["Escrito de apelación fundado"]),
            (i(70), "Recursos", "Recurso directo por apelación denegada en el amparo federal (24 horas)", "AMBAS",
             "Notificación de la denegatoria de la apelación", 24, "HORAS", "NO", "Art. 15 Ley 16.986", "NO", "NO",
             ["Articularlo ante la Cámara dentro de las 24 horas",
              "La Cámara debe resolver dentro del tercer día"],
             ["Escrito de recurso directo"]),
            (i(80), "Recursos", "Sentencia de la Cámara Federal en el amparo", "TRIBUNAL",
             "Elevación del expediente con el recurso concedido", 0, "SIN_PLAZO", "NO",
             "Art. 15 Ley 16.986; CPCCN supletorio (a verificar)", "NO", "NO",
             ["Controlar el plazo y pedir pronto despacho si se demora",
              "Evaluar el recurso extraordinario federal"],
             ["Sentencia de Cámara"]),
        ]
    transiciones = [
        (i(0), "Demanda presentada", i(10)),
        (i(10), "Demanda admitida: se requiere el informe", i(20)),
        (i(10), "Rechazo in limine (otra vía idónea, plazo vencido o inadmisibilidad manifiesta)", i(60)),
        (i(20), "Contestación o informe presentados, o vencido el plazo: hay hechos que probar", i(30)),
        (i(20), "Contestación o informe presentados, o vencido el plazo: no hay prueba pendiente", i(50)),
        (i(30), "Audiencia celebrada: se abre a prueba", i(40)) if pba else
        (i(30), "Audiencia de prueba realizada", i(50)),
    ]
    if pba:
        transiciones.append((i(30), "Audiencia celebrada sin prueba que producir", i(50)))
    transiciones += [
        (i(30), "La actora no comparece: se la tiene por desistida", salidas["cierre"]),
    ]
    if pba:
        transiciones.append((i(40), "Prueba producida o vencido el plazo", i(50)))
    transiciones += [
        (i(50), "Sentencia notificada y se apela", i(60)),
        (i(50), "Sentencia favorable notificada y no apelada", salidas["cumplimiento"]),
        (i(50), "Sentencia de rechazo notificada y no apelada", salidas["cierre"]),
        (i(60), "Apelación concedida", i(80)),
        (i(60), "Apelación denegada", i(70)),
        (i(70), "Queja o recurso directo admitido", i(80)),
        (i(70), "Rechazado o no deducido: queda firme una decisión favorable", salidas["cumplimiento"]),
        (i(70), "Rechazado o no deducido: queda firme el rechazo", salidas["cierre"]),
        (i(80), "Sentencia favorable firme", salidas["cumplimiento"]),
        (i(80), "Rechazo firme", salidas["cierre"]),
    ]
    if salidas.get("extraordinarios"):
        transiciones.append((i(80), "Se interpone recurso extraordinario", salidas["extraordinarios"]))
    nodos, transiciones = filtrar(nodos, transiciones, omitir)
    return ajustar(nodos, ajustes), transiciones


# --- Cautelares contra el Estado (Ley 12.008 / Ley 13.928 / Ley 26.854) -----------------------------------------

def bloque_cautelar(p, base, pba=None, fed=None, salidas=None, ajustes=None):
    """Pedido, informe previo, resolución, cumplimiento, apelación y vigencia de la medida cautelar.
    `pba`: "CCA" (Ley 12.008) o "AMPARO" (Ley 13.928); `fed`: "ORDINARIO" o "AMPARO" (Ley 26.854 y CPCCN).
    `salidas` puede tener "demanda" (demanda tras la cautelar anticipada) e "incumplimiento"."""
    i = lambda n: f"{p}_{base + n}"
    salidas = salidas or {}
    bases = []
    checklist = []
    if pba == "CCA":
        bases.append("arts. 22 a 25 Ley 12.008")
        checklist += [
            "Acreditar verosimilitud del derecho, peligro en la demora y que no afecta gravemente el interés "
            "público (art. 22); se admiten medidas positivas",
            "Puede pedirse antes de la demanda (art. 23): si se otorga, demandar dentro de los 30 días",
            "Contracautela: en empleo público, materia previsional o con beneficio de litigar sin gastos, solo "
            "caución juratoria; el Estado no presta contracautela (art. 24)",
            "Para suspender un acto administrativo, antes hay que pedirlo en sede administrativa (art. 25)",
        ]
    if pba == "AMPARO":
        bases.append("arts. 9 y 23 Ley 13.928; capítulo IV Ley 12.008 y arts. 195 a 232 CPCCBA en lo pertinente")
        checklist += [
            "Se resuelve con la admisibilidad o, si se pide después, en 1 día (art. 9); la medida de no innovar, en "
            "el día (art. 23)",
            "En salud: pedir medida innovativa con caución juratoria; acompañar prescripción médica y constancia de "
            "la negativa",
            "Pedir habilitación de días y horas inhábiles o de feria si la prestación es urgente",
        ]
    if fed:
        bases.append("Ley 26.854 (si se demanda al Estado nacional o a sus entes) y arts. 195 a 233 CPCCN")
        checklist += [
            "Ley 26.854: la cautelar no puede coincidir con el objeto de la demanda (art. 3); hay excepciones para "
            "sectores vulnerables, vida digna, salud o derechos alimentarios (art. 2 inc. 2)",
            "Contra prepagas u obras sociales no estatales la Ley 26.854 no rige: aplica el CPCCN (a verificar)",
        ]
    checklist.append(CHECKLIST_SIN_DATOS)
    base_normativa = "; ".join(bases)
    base_normativa = base_normativa[0].upper() + base_normativa[1:]
    nodos = [
        (i(0), "Cautelares", "Pedido de medida cautelar", "ACTORA",
         "Riesgo de daño durante el proceso (con la demanda, antes o después)", 0, "SIN_PLAZO", "NO",
         base_normativa, "NO", "NO", checklist,
         ["Escrito de cautelar", "Prueba de la urgencia"]),
        (i(20), "Cautelares", "Resolución de la medida cautelar", "TRIBUNAL",
         "Pedido de la cautelar, o informe previo presentado o vencido", 0, "SIN_PLAZO", "NO",
         base_normativa, "NO", "NO",
         ["Con riesgo para la salud o la vida, pedir que se resuelva en el día",
          "Controlar la contracautela fijada",
          "Controlar el plazo de cumplimiento que fija la orden"],
         ["Resolución cautelar"]),
        (i(25), "Cautelares", "Cumplimiento de la medida cautelar por el demandado", "DEMANDADA",
         "Notificación de la orden cautelar", 0, "FECHA_FIJADA", "NO",
         "Orden judicial; art. 804 CCyC (astreintes)", "NO", "NO",
         ["Cargar la fecha y hora de vencimiento que fija la orden (en salud suele fijarse en horas)",
          "Si no cumple: pedir astreintes (art. 804 CCyC) y la intimación bajo apercibimiento de denuncia por "
          "desobediencia (art. 239 Código Penal)"],
         ["Constancia de notificación de la orden", "Constancia de cumplimiento"]),
    ]
    transiciones = []
    if pba == "CCA":
        nodos += [
            (i(5), "Cautelares", "La Administración resuelve el pedido de suspensión del acto", "DEMANDADA",
             "Presentación del pedido de suspensión ante la Administración", 5, "HABILES_ADMINISTRATIVOS", "NO",
             "Art. 25 Ley 12.008", "NO", "NO",
             ["Presentar el pedido en sede administrativa antes de la cautelar judicial",
              "Si no resuelve en 5 días hábiles, se considera denegado",
              "Calendario administrativo provincial o municipal según quién dictó el acto (ver duda de producto)"],
             ["Pedido de suspensión con cargo de recepción"]),
            (i(10), "Cautelares", "Informe previo de la Provincia, el municipio o el ente (optativo)", "DEMANDADA",
             "Notificación del pedido de informe previo", 5, "HABILES_JUDICIALES", "SI",
             "Art. 23 Ley 12.008", "NO", "NO",
             ["El juez puede pedirlo; plazo máximo de 5 días",
              "Si el juez fija uno menor, cargarlo como plazo suelto"],
             ["Informe previo"]),
            (i(30), "Cautelares", "Demanda dentro de los 30 días de la cautelar anticipada", "ACTORA",
             "Notificación de la cautelar otorgada antes de la demanda", 30, "HABILES_JUDICIALES", "NO",
             "Art. 23 Ley 12.008", "NO", "NO",
             ["Si no se demanda en 30 días, la medida caduca",
              "Si la vía administrativa sigue abierta, verificar cómo se computa (a verificar)"],
             []),
        ]
        transiciones += [
            (i(0), "Se pide suspender un acto administrativo", i(5)),
            (i(0), "El juez pide informe previo", i(10)),
            (i(5), "Suspensión denegada o vencido el plazo: sigue el pedido judicial", i(20)),
            (i(5), "La Administración suspende el acto", CIERRA),
            (i(10), "Informe presentado o vencido el plazo", i(20)),
        ]
    if fed:
        informe = 3 if fed == "AMPARO" else 5
        nodos += [
            (i(15), "Cautelares", "Informe previo del Estado nacional (Ley 26.854)", "DEMANDADA",
             "Notificación del requerimiento del informe previo", informe, "HABILES_JUDICIALES", "NO",
             "Art. 4 Ley 26.854", "NO", "NO",
             ["Plazo de 5 días; 3 días en el amparo y el sumarísimo (art. 4 inc. 2)",
              "No se exige en los supuestos del art. 2 inc. 2 (salud, vida digna, alimentario, sectores "
              "vulnerables): pedir que se resuelva sin informe",
              "El juez puede dictar una medida interina hasta el informe",
              "Calendario judicial federal y gracia del CPCCN: ver duda de producto"],
             ["Informe previo"]),
            (i(50), "Cautelares", "Vencimiento de la cautelar contra el Estado nacional", "ACTORA",
             "Notificación de la cautelar otorgada", 3 if fed == "AMPARO" else 6, "MESES", "NO",
             "Art. 5 Ley 26.854", "NO", "NO",
             ["El juez fija un límite de vigencia: hasta 6 meses, 3 en el amparo y el sumarísimo; si fija otro, "
              "ajustar el plazo",
              "Pedir la prórroga antes del vencimiento (hasta 6 meses más)",
              "No rige en los supuestos del art. 2 inc. 2 (salud, alimentario): cerrar este camino",
              "Si se dictó con la vía administrativa pendiente, dura hasta la notificación del acto que la agota"],
             ["Pedido de prórroga"]),
        ]
        transiciones += [
            (i(0), "Se demanda al Estado nacional y no es un supuesto del art. 2 inc. 2 Ley 26.854", i(15)),
            (i(15), "Informe presentado o vencido el plazo", i(20)),
        ]
    transiciones.append((i(0), "Se resuelve sin informe previo", i(20)))
    otorgada = [i(25)] + ([i(50)] if fed else [])
    transiciones += [(i(20), "Cautelar otorgada", d) for d in otorgada]
    if pba == "CCA":
        transiciones += [(i(20), "Cautelar otorgada antes de la demanda", d) for d in otorgada + [i(30)]]
    if pba:
        apelacion_pba = 5 if pba == "CCA" else 3
        nodos.append(
            (i(40), "Cautelares", "Apelación de la resolución cautelar (provincial)", "AMBAS",
             "Notificación de la resolución cautelar", apelacion_pba, "HABILES_JUDICIALES", "SI",
             "Arts. 55, 56 y 59 Ley 12.008" if pba == "CCA" else "Arts. 16 inc. 2 y 17 Ley 13.928", "NO", "NO",
             (["Apelación fundada en 5 días; la Cámara resuelve en 5 días (art. 59)"] if pba == "CCA" else
              ["Interponer y fundar en 3 días (arts. 16 inc. 2 y 17)",
               "Efecto devolutivo; excepcionalmente suspensivo (art. 17)"])
             + ["La apelación puede venir de cualquiera de las partes"],
             ["Escrito de apelación"]))
        transiciones += [
            (i(20), "Se apela la resolución cautelar (juzgado provincial)", i(40)),
            (i(40), "Apelación resuelta", CIERRA),
        ]
    if fed:
        amparo = fed == "AMPARO"
        nodos.append(
            (i(45), "Cautelares", "Apelación de la resolución cautelar (federal)", "AMBAS",
             "Notificación de la resolución cautelar", 48 if amparo else 5, "HORAS" if amparo else
             "HABILES_JUDICIALES", "NO",
             "Art. 15 Ley 16.986 (medidas de no innovar o suspensión)" if amparo else
             "Art. 244 CPCCN y art. 13 Ley 26.854 (a verificar)", "NO", "NO",
             (["Interponer y fundar dentro de las 48 horas"] if amparo else
              ["Plazo de 5 días (a verificar)",
               "Si se suspende un acto estatal, la apelación del Estado puede tener efecto suspensivo (art. 13 "
               "Ley 26.854, a verificar)"])
             + ["Calendario y gracia federales: ver duda de producto"],
             ["Escrito de apelación"]))
        transiciones += [
            (i(20), "Se apela la resolución cautelar (juzgado federal)", i(45)),
            (i(45), "Apelación resuelta", CIERRA),
        ]
    transiciones += [
        (i(20), "Cautelar denegada y no se apela", CIERRA),
        (i(25), "Medida cumplida", CIERRA),
        (i(25), "Medida incumplida", salidas.get("incumplimiento", CIERRA)),
    ]
    if pba == "CCA":
        transiciones += [
            (i(30), "Demanda presentada en plazo", salidas.get("demanda", CIERRA)),
            (i(30), "Venció el plazo sin demandar: la cautelar caduca", CIERRA),
        ]
    if fed:
        transiciones.append((i(50), "Prórroga pedida y resuelta, o terminó el proceso", CIERRA))
    nodos, transiciones = ordenar(nodos, transiciones)
    return ajustar(nodos, ajustes), transiciones


# --- Recursos: apelación ante la Cámara CA, extraordinarios ante la SCBA y REF ante la CSJN ------------------------

def extraordinarios(p, base, scba, salidas):
    """Recursos extraordinarios provinciales (si `scba`) y recurso extraordinario federal.
    `salidas`: "firme" (un solo destino) o "favorable" y "rechazo"."""
    i = lambda n: f"{p}_{base + n}"
    nodos = []
    if scba:
        nodos.append(
            (i(0), "Recursos", "Recursos extraordinarios ante la SCBA", "AMBAS",
             "Notificación de la sentencia definitiva de la Cámara o de la alzada", 10, "HABILES_JUDICIALES", "SI",
             "Art. 161 inc. 3 Constitución PBA; art. 60 Ley 12.008; arts. 278 a 280 CPCCBA", "NO", "NO",
             ["Evaluar inaplicabilidad de ley, nulidad e inconstitucionalidad",
              "Controlar el valor mínimo del agravio y el depósito previo (art. 280 CPCCBA) o su exención; en causas "
              "que vienen del Tribunal Fiscal de Apelación ver art. 60 inc. 3 Ley 12.008",
              "Verificar si el Estado está exento del depósito (a verificar)"],
             ["Escrito de recurso", "Comprobante del depósito previo o fundamento de la exención"]))
    nodos.append(
        (i(10), "Recursos", "Recurso extraordinario federal ante la CSJN", "AMBAS",
         "Notificación de la sentencia definitiva del superior tribunal de la causa", 10, "HABILES_JUDICIALES", "NO",
         "Art. 14 Ley 48; arts. 256 y 257 CPCCN; Acordada CSJN 4/2007 (a verificar texto vigente)", "NO", "NO",
         ["Plazo de 10 días hábiles desde la notificación (art. 257 CPCCN, a verificar)",
          "Cumplir el reglamento de la Acordada 4/2007 (carátula, extensión, requisitos)",
          "Si se deniega: queja ante la CSJN en 5 días (art. 285 CPCCN, a verificar) y depósito o su exención",
          "Calendario y gracia federales: ver duda de producto"],
         ["Escrito de recurso extraordinario", "Carátula de la Acordada 4/2007"]))

    def a(origen, texto):
        if "firme" in salidas:
            return [(origen, texto, salidas["firme"])]
        return [(origen, texto + ": favorable", salidas["favorable"]), (origen, texto + ": rechazo", salidas["rechazo"])]

    transiciones = []
    if scba:
        transiciones.append((i(0), "Sentencia de la SCBA notificada y hay cuestión federal", i(10)))
        transiciones += a(i(0), "Resuelto por la SCBA sin cuestión federal, denegado o desistido")
    transiciones += a(i(10), "Recurso federal resuelto, denegado (queja incluida) o desistido")
    return nodos, transiciones


def recursos_cca(p, base, firme):
    """Apelación ante la Cámara CA (arts. 55 a 59 Ley 12.008), extraordinarios y sentencia firme ({p}_{base+50})."""
    i = lambda n: f"{p}_{base + n}"
    nodos = [
        (i(0), "Recursos", "Apelación de la sentencia ante la Cámara en lo Contencioso Administrativo", "AMBAS",
         "Notificación de la sentencia definitiva", 10, "HABILES_JUDICIALES", "SI", "Arts. 55 y 56 Ley 12.008", "NO",
         "NO",
         ["Interponer y fundar en el mismo escrito dentro de los 10 días (5 para las demás resoluciones apelables)",
          "Hacer una crítica concreta y razonada del fallo",
          "Pedir prueba o invocar hechos nuevos en la alzada solo en los casos del art. 57"],
         ["Escrito de apelación fundado"]),
        (i(10), "Recursos", "Contestación del traslado de la apelación", "AMBAS",
         "Notificación del traslado del recurso", 10, "HABILES_JUDICIALES", "SI", "Art. 58 Ley 12.008", "NO", "NO",
         ["El plazo es igual al de interposición (10 días contra la sentencia definitiva)",
          "Contestar cada agravio y mantener las defensas no tratadas"],
         ["Contestación de agravios"]),
        (i(20), "Recursos", "Sentencia de la Cámara en lo Contencioso Administrativo", "TRIBUNAL",
         "Expediente en estado de resolver en la Cámara", 30, "HABILES_JUDICIALES", "NO", "Art. 59 Ley 12.008", "NO",
         "NO",
         ["Plazo de 30 días; 5 si se apeló una cautelar",
          "Si vence, pedir pronto despacho",
          "Pedir aclaratoria en 5 días si hay error material u omisión (art. 52)"],
         ["Sentencia de Cámara"]),
        (i(50), "Sentencia", "Sentencia firme", "TRIBUNAL",
         "Vencimiento del plazo para recurrir o notificación de la última sentencia", 0, "SIN_PLAZO", "NO",
         "Art. 163 CPCCBA (supletorio, art. 77 Ley 12.008)", "NO", "NO",
         ["Verificar que no queden recursos pendientes",
          "Si hay condena contra el Estado, pasar a la ejecución; si no, a honorarios"],
         ["Constancia de firmeza"]),
    ]
    ext_nodos, ext_trans = extraordinarios(p, base + 30, True, {"firme": i(50)})
    transiciones = [
        (i(0), "Apelación concedida y traslado notificado", i(10)),
        (i(0), "Apelación denegada o desierta: queda firme la sentencia", i(50)),
        (i(10), "Contestado el traslado o vencido el plazo", i(20)),
        (i(20), "Sentencia de Cámara notificada y se recurre", i(30)),
        (i(20), "Sentencia de Cámara notificada y no se recurre", i(50)),
        *ext_trans,
    ]
    return nodos + ext_nodos, transiciones


# --- Ejecución de sentencias contra el Estado (provincial y nacional) ----------------------------------------------

def ejecucion_estado(p, base, variante, salida, incluir=None, ajustes=None):
    """Notificación, plazo de cumplimiento, suspensión (solo PBA), liquidación, previsión presupuestaria, cumplimiento
    forzado y pago. `variante`: "PBA" (arts. 63 a 66 Ley 12.008) o "NACION" (ANSES, art. 22 Ley 24.463).
    `incluir`: claves de los hitos que se usan (por defecto, todos). Termina en `salida` (honorarios)."""
    i = lambda n: f"{p}_{base + n}"
    if variante == "PBA":
        nodos = {
            "intimacion": (i(0), "Ejecución", "Notificación de la sentencia firme a la autoridad obligada (provincial)",
                           "TRIBUNAL", "Sentencia firme de condena contra la Provincia, el municipio o el ente", 5,
                           "HABILES_JUDICIALES", "NO", "Art. 63 Ley 12.008", "NO", "NO",
                           ["El juzgado notifica dentro de 5 días a la autoridad que debe cumplir",
                            "Controlar que la intime a cumplir en el plazo de la sentencia"],
                           ["Oficio o cédula a la autoridad obligada"]),
            "plazo": (i(10), "Ejecución", "Cumplimiento voluntario por la Provincia, el municipio o el ente",
                      "DEMANDADA", "Notificación de la sentencia firme a la autoridad obligada", 60,
                      "HABILES_JUDICIALES", "NO",
                      "Art. 63 Ley 12.008; art. 163 Constitución PBA (60 días; tipo de días a verificar)", "NO", "NO",
                      ["Si la sentencia fija otro plazo, cargarlo como plazo suelto",
                       "Vencido el plazo, la vencedora puede pedir el cumplimiento directo (art. 63)",
                       "Condenas dinerarias: liquidación y previsión presupuestaria (ver duda)"],
                      []),
            "suspension": (i(20), "Ejecución", "Pedido del Estado provincial de suspender o no ejecutar la sentencia",
                           "DEMANDADA", "Notificación de la sentencia firme a la autoridad obligada", 20,
                           "HABILES_JUDICIALES", "SI", "Art. 65 Ley 12.008", "NO", "NO",
                           ["Puede alegar causas graves de interés público dentro de 20 días",
                            "Contestar el traslado en 5 días; prueba en 10 días; el juez resuelve en 10 días",
                            "Si se admite, el juez fija la indemnización sustitutiva"],
                           ["Contestación del traslado"]),
            "liquidacion": (i(30), "Ejecución", "Liquidación de la condena (provincial)", "ACTORA",
                            "Sentencia firme de condena dineraria", 10, "HABILES_JUDICIALES", "SI",
                            "Art. 77 Ley 12.008; arts. 501 y 502 CPCCBA", "NO", "NO",
                            ["Presentar la liquidación; si no, puede hacerlo la vencida (art. 501 CPCCBA)",
                             "Tasa de interés según la sentencia o la doctrina legal de la SCBA (ver duda)",
                             "La impugnación de la otra parte se contesta en 5 días (art. 502 CPCCBA)"],
                            ["Liquidación"]),
            "presupuesto": (i(40), "Ejecución", "Previsión presupuestaria y pago de la sentencia (provincial o "
                            "municipal)", "DEMANDADA", "Liquidación aprobada", 0, "SIN_PLAZO", "NO",
                            "Régimen provincial y municipal de pago de sentencias e inembargabilidad (normas vigentes "
                            "a verificar)", "NO", "NO",
                            ["Pedir que el crédito se incluya en el presupuesto si no hay partida",
                             "Verificar si rige algún régimen de consolidación de deudas (a verificar)",
                             "Municipios: Ley Orgánica de las Municipalidades (embargos y pago de sentencias, a "
                             "verificar)"],
                            ["Oficio a la autoridad presupuestaria"]),
            "forzada": (i(50), "Ejecución", "Cumplimiento forzado contra el Estado provincial: astreintes, embargo o "
                        "ejecución directa", "ACTORA", "Vencimiento del plazo de cumplimiento sin cumplir", 0,
                        "SIN_PLAZO", "NO", "Arts. 63 y 64 Ley 12.008; art. 804 CCyC", "NO", "NO",
                        ["Pedir el cumplimiento directo y la intimación al funcionario responsable",
                         "Astreintes al ente o al funcionario (art. 804 CCyC)",
                         "Los actos dictados durante la ejecución se impugnan en el mismo proceso (art. 64)",
                         "Embargo solo sobre fondos no afectados (verificar inembargabilidad)"],
                        ["Escrito de intimación o embargo"]),
            "pago": (i(60), "Ejecución", "Pago por el Estado y percepción", "DEMANDADA",
                     "Depósito judicial o cumplimiento de la obligación", 0, "SIN_PLAZO", "NO",
                     "Arts. 63 a 66 Ley 12.008", "NO", "NO",
                     ["Pedir el giro o la transferencia", "Controlar el pago de costas"],
                     ["Orden de transferencia"]),
        }
    else:
        nodos = {
            "intimacion": (i(0), "Ejecución", "Sentencia firme notificada y expediente administrativo remitido a ANSES",
                           "TRIBUNAL", "Sentencia firme de condena contra ANSES", 0, "SIN_PLAZO", "NO",
                           "Art. 22 Ley 24.463", "NO", "NO",
                           ["Controlar que el juzgado remita el expediente administrativo y comunique la sentencia",
                            "Guardar la constancia de recepción: es el disparador del plazo de cumplimiento"],
                           ["Constancia de recepción del expediente por ANSES"]),
            "plazo": (i(10), "Ejecución", "ANSES liquida y cumple la sentencia (120 días hábiles)", "DEMANDADA",
                      "Recepción del expediente administrativo por ANSES", 120, "HABILES_ADMINISTRATIVOS", "NO",
                      "Art. 22 Ley 24.463 (tipo de días a verificar)", "NO", "NO",
                      ["Calendario administrativo nacional (ver duda de producto)",
                       "Controlar el alta del haber reajustado y la liquidación del retroactivo"],
                      []),
            "liquidacion": (i(30), "Ejecución", "Liquidación de la sentencia previsional e impugnación", "AMBAS",
                            "Presentación de la liquidación de ANSES o de la actora", 5, "HABILES_JUDICIALES", "NO",
                            "Arts. 503 y 504 CPCCN (a verificar)", "NO", "NO",
                            ["Revisar haber inicial, movilidad aplicada e intereses según la sentencia",
                             "Tasa de interés: la que fije la sentencia o la jurisprudencia de la Cámara (a verificar)",
                             "Impugnar dentro del plazo del traslado (a verificar)"],
                            ["Liquidación", "Impugnación"]),
            "presupuesto": (i(40), "Ejecución", "Previsión presupuestaria del crédito (Estado nacional)", "DEMANDADA",
                            "Liquidación aprobada", 0, "SIN_PLAZO", "NO",
                            "Ley 11.672 (Complementaria Permanente de Presupuesto) y Ley 24.624 (inembargabilidad); "
                            "artículos a verificar", "NO", "NO",
                            ["Verificar el orden de prelación de pago de sentencias previsionales (a verificar)",
                             "Si no se paga en el ejercicio, pedir cumplimiento forzado"],
                            []),
            "forzada": (i(50), "Ejecución", "Cumplimiento forzado contra ANSES: intimación, astreintes o embargo",
                        "ACTORA", "Vencimiento del plazo de cumplimiento sin cumplir", 0, "SIN_PLAZO", "NO",
                        "Art. 22 Ley 24.463; art. 804 CCyC; CPCCN (a verificar)", "NO", "NO",
                        ["Intimar el cumplimiento bajo apercibimiento de astreintes",
                         "Embargo solo sobre fondos no afectados (verificar inembargabilidad)"],
                        ["Escrito de intimación"]),
            "pago": (i(60), "Ejecución", "ANSES paga el retroactivo y liquida el nuevo haber", "DEMANDADA",
                     "Liquidación aprobada o cumplimiento", 0, "SIN_PLAZO", "NO", "Art. 22 Ley 24.463", "NO", "NO",
                     ["Controlar el pago del retroactivo y el haber mensual reajustado",
                      "Controlar las retenciones (ver duda sobre Ganancias)"],
                     ["Constancia de pago", "Recibo de haberes posterior"]),
        }
    claves = [k for k in nodos if incluir is None or k in incluir]
    presentes = {k: nodos[k][0] for k in claves}
    t = []

    def ir(o, cond, d):
        destinos = {**presentes, "salida": salida, CIERRA: CIERRA}
        if o in presentes and d in destinos:
            t.append((presentes[o], cond, destinos[d]))

    if variante == "PBA":
        ir("intimacion", "Sentencia notificada a la autoridad", "plazo")
        ir("intimacion", "Sentencia notificada a la autoridad", "suspension")
    else:
        ir("intimacion", "Expediente recibido por ANSES", "plazo")
    ir("plazo", "Cumplida en plazo", "pago")
    ir("plazo", "Condena dineraria: hay que liquidar", "liquidacion")
    ir("plazo", "Vencido el plazo sin cumplir", "forzada")
    ir("suspension", "Pedido rechazado, no presentado o resuelto con indemnización", CIERRA)
    ir("liquidacion", "Liquidación aprobada", "presupuesto" if "presupuesto" in presentes else "pago")
    ir("presupuesto", "Crédito previsto y pagado", "pago")
    ir("presupuesto", "Sin previsión o sin pago en el ejercicio", "forzada")
    ir("forzada", "Cumplimiento o pago obtenido", "pago")
    ir("pago", "Pago percibido y obligación cumplida", "salida")
    return ajustar([nodos[k] for k in claves], ajustes), t


# --- Honorarios ----------------------------------------------------------------------------------------------------

def honorarios(p, base, fuero, salida):
    """Regulación y apelación de honorarios: "PBA" (Ley 14.967), "FED" (Ley 27.423) o "AMBOS" (dos hitos)."""
    i = lambda n: f"{p}_{base + n}"
    nodos, transiciones = [], []
    if fuero in ("PBA", "AMBOS"):
        nodos.append(
            (i(0), "Cierre", "Regulación de honorarios y apelación (provincial, Ley 14.967)", "AMBAS",
             "Notificación de la regulación de honorarios", 5, "HABILES_JUDICIALES", "SI",
             "Art. 57 Ley 14.967 (a verificar texto vigente)", "NO", "NO",
             ["Pedir la regulación al terminar cada etapa o el proceso",
              "Apelar fundadamente dentro de los 5 días si la regulación es baja o alta",
              "Costas: verificar la regla del art. 51 Ley 12.008 o la del proceso (a verificar)",
              "Pagar los aportes de la Ley 6716 sobre los honorarios y acreditarlos (plazo a verificar)"],
             ["Escrito de regulación o de apelación", "Boleta de aportes"]))
        transiciones.append((i(0), "Regulación firme y aportes acreditados", salida))
    if fuero in ("FED", "AMBOS"):
        nodos.append(
            (i(5), "Cierre", "Regulación de honorarios y apelación (federal, Ley 27.423)", "AMBAS",
             "Notificación de la regulación de honorarios", 5, "HABILES_JUDICIALES", "NO",
             "Ley 27.423 (plazo y forma de la apelación a verificar)", "NO", "NO",
             ["Pedir la regulación al terminar cada etapa o el proceso",
              "Apelar dentro del plazo (a verificar si son 5 días y si debe fundarse en el mismo escrito)",
              "En seguridad social las costas son por su orden (art. 21 Ley 24.463; ver duda sobre su aplicación)",
              "Aportes a la Caja de Abogados de PBA en causas federales: ver duda transversal"],
             ["Escrito de regulación o de apelación"]))
        transiciones.append((i(5), "Regulación firme y aportes acreditados", salida))
    return nodos, transiciones


# --- Dudas transversales y de producto (solo en contencioso; las otras matrices remiten) ---------------------------

DUDAS_TRANSVERSALES = [
    ("[TRANSVERSAL] Plazo de gracia según la jurisdicción",
     "Se marcó Aplica_Gracia = SI solo en escritos de parte ante la justicia provincial, porque el CPCCBA es "
     "supletorio en la Ley 12.008 (art. 77), en la Ley 13.928 (art. 25, Ley 14.192) y en la Ley 14.214 (art. 8, "
     "sumarísimo). En los caminos federales (CPCCN) la gracia sería la de las primeras horas del despacho del "
     "art. 124 CPCCN (a verificar) y se marcó NO. ¿Confirman que la gracia no contraría la operatividad del amparo "
     "(art. 25 Ley 13.928) y cuál es la gracia federal? Propuesta: dejar NO en federal hasta que el motor tenga "
     "calendario federal (vencimiento más temprano). " + FUENTE_CCA + " " + FUENTE_AMPARO,
     "Todos los hitos con Plazo_Tipo HABILES_JUDICIALES"),
    ("[TRANSVERSAL] Gracia en los plazos para demandar",
     "¿El art. 124 CPCCBA se aplica a la demanda presentada el último día del plazo de caducidad (90 días del "
     "art. 18 Ley 12.008, 30 días del art. 23, 30 días del art. 5 Ley 13.928, 60 días del art. 7 Ley 14.214)? "
     "Propuesta: Aplica_Gracia = NO en todos los plazos para demandar, porque da el vencimiento más temprano.",
     "CAD_400, CAD_405, CAD_630, AMP_200, AMP_400, HDA_200"),
    ("[TRANSVERSAL] Calendario de los días hábiles administrativos",
     "La regla R6 del motor excluye solo feriados nacionales y provinciales y no suspende en feria. En la "
     "Administración provincial y municipal hay asuetos administrativos del Poder Ejecutivo o del intendente, y en la "
     "nacional, días no laborables. ¿Qué días son inhábiles para cada calendario administrativo (Decreto-Ley "
     "7647/70 art. 68; Ordenanza General 267/80; Ley 19.549 art. 1)? ¿Quién los carga? Propuesta: usar R6 y "
     "cargar los asuetos como inhábiles manuales del estudio hasta que haya calendario administrativo. "
     + FUENTE_7647 + " " + FUENTE_LPA,
     "Todos los hitos HABILES_ADMINISTRATIVOS"),
    ("[TRANSVERSAL] Plazos en horas del amparo federal",
     "La Ley 16.986 fija 48 horas para la sentencia sin prueba y para apelar, y 24 horas para el recurso directo. "
     "La regla R8 del motor cuenta horas corridas desde el disparador. ¿Corren de corrido aunque haya días "
     "inhábiles, o la jurisprudencia las computa como días hábiles (2 y 1)? ¿Se aplica la gracia del CPCCN? Esto "
     "aparta al amparo federal de las reglas D26 a D34 de la matriz laboral. Propuesta: horas corridas (vencimiento "
     "más temprano) y alerta en el checklist. " + FUENTE_AMPARO,
     "AMP_450, AMP_460, AMP_470, AMP_345, HDA_450, HDA_460, HDA_470"),
    ("[TRANSVERSAL] Feria judicial en amparos y cautelares urgentes",
     "En amparos de salud y cautelares urgentes se pide habilitación de feria. ¿La app debe dejar de suspender los "
     "plazos en feria cuando el juzgado la habilita (provincial y federal)? ¿Y los plazos de la vía administrativa, "
     "que no se suspenden en feria (R6)? Propuesta: el abogado marca el expediente como 'feria habilitada' y los "
     "vencimientos se recalculan sin excluir la feria. Registrar; no modificar el motor.",
     "Hitos de amparo y cautelares"),
    ("[TRANSVERSAL] Tasa de justicia, contribuciones y exenciones",
     "¿Qué procesos están exentos de tasa de justicia y contribuciones? Confirmado: el amparo provincial está exento "
     "de tasa, sellado y todo otro tributo (art. 20 Ley 13.928) y el hábeas data provincial, del pago previo de "
     "tasas (art. 19 Ley 14.214). A verificar: si la exención del amparo alcanza la contribución del art. 12 inc. g "
     "Ley 6716 y el bono de la Ley 8480; reclamos de empleo público y previsionales en PBA; Ley 23.898 en el fuero "
     "federal (seguridad social, amparo, hábeas data); y la gratuidad del art. 53 Ley 24.240 frente a prepagas. "
     "Propuesta: checklist que pide verificar en cada demanda hasta que se confirme. " + FUENTE_HD + " "
     + FUENTE_AMPARO,
     "Hitos de demanda de las cuatro matrices"),
    ("[TRANSVERSAL] Honorarios y aportes por jurisdicción",
     "Provincial: Ley 14.967 (apelación en 5 días, art. 57, a verificar). En el amparo provincial los honorarios "
     "de primera instancia tienen un tope de 20 Jus y en el amparo por mora son 5 Jus (art. 20 bis Ley 13.928, "
     "Ley 15.016): ¿ese tope de 5 Jus alcanza al amparo por mora del art. 76 Ley 12.008? Federal: Ley 27.423 (plazo "
     "de apelación a verificar). Seguridad social: costas por su orden (art. 21 Ley 24.463, texto vigente; verificar "
     "cómo lo aplica la jurisprudencia). ¿La Caja de Abogados de PBA exige aportes y bono en causas federales con asiento en PBA? ¿Y en causas contra el Estado, "
     "rigen reglas especiales de costas? Propuesta: 5 días hábiles judiciales en ambos fueros, con gracia solo en "
     "el provincial.",
     "CAD_300, CAD_950, AMP_950, AMP_955, SSO_950, HDA_950, HDA_955"),
    ("[TRANSVERSAL] Beneficio de litigar sin gastos y gratuidad",
     "¿Se modela el beneficio de litigar sin gastos como incidente aparte o solo como checklist de la demanda? ¿La "
     "gratuidad del consumidor (art. 53 Ley 24.240) alcanza los amparos de salud contra prepagas? Propuesta V1: "
     "checklist en cada demanda; incidente fuera de estas matrices.",
     "Hitos de demanda"),
    ("[TRANSVERSAL] Numeración de la Ley 12.008 y vigencia de las normas",
     "En leyes-ar.com las páginas de la Ley 12.008 desde el art. 18 aparecen corridas un número (el texto del "
     "art. 18 está en la página del 17, con notas de 'renumerado'). Las remisiones internas (art. 16 en el amparo "
     "por mora, art. 18 en el sumario de ilegitimidad) confirman la numeración oficial, que es la que se cita. "
     "¿Pueden cotejar con el texto oficial de normas.gba.gob.ar? También verificar vigencia al 13/11/2026 de la "
     "Ley 19.549 reformada por la Ley 27.742, la Ley 26.854 y la Ley 25.326. " + FUENTE_CCA + " " + FUENTE_LPA,
     "Todos"),
    ("[TRANSVERSAL] Reglas del motor D26 a D34",
     "Las reglas del motor validadas en las dudas D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx valen acá, "
     "salvo donde estos procesos se apartan: días hábiles administrativos con calendarios distintos (provincial, "
     "municipal, nacional), plazos en horas del amparo federal, gracia federal y feria habilitada. Cada apartamiento "
     "tiene su propia duda. ¿Hay alguna otra diferencia?",
     "Todos"),
]

DUDAS_PRODUCTO = [
    ("[PRODUCTO] PRIORITARIA: jurisdicción federal en una app PBA",
     "Seguridad social (ANSES), amparo contra obras sociales nacionales y prepagas, y hábeas data contra bases "
     "nacionales o interconectadas tramitan en la justicia federal: otro código (CPCCN), otra gracia y el calendario "
     "de la CSJN (ferias y acordadas propias). Se revisó logica_matematica_calculadora_de_dias_habiles_judiciales.md "
     "sin modificarlo: el motor ya recibe 'horario' y 'calendario' por expediente desde la jurisdicción "
     "(jurisdiction_schedules con hora de cierre y fin de gracia; holidays_calendar con alcance NACIONAL, PROVINCIAL, "
     "DEPARTAMENTO u ORGANIZACION; calendar_coverage único por jurisdicción). Haría falta: (1) una jurisdicción "
     "federal con su horario, su fin de gracia y sus ferias; (2) dependencias federales en lugar de departamentos "
     "judiciales; (3) que un expediente pueda pasar de un calendario a otro (vía administrativa nacional o "
     "provincial y luego juicio federal), porque hoy legal_cases tiene una sola jurisdiction_id; (4) una decisión "
     "sobre los plazos en horas. Propuesta V1: dejar los caminos federales en las matrices con Aplica_Gracia = NO y "
     "un aviso de 'cálculo con calendario provincial'. Solo se registra.",
     "Todos los hitos de caminos federales"),
    ("[PRODUCTO] Calendario administrativo y HABILES_ADMINISTRATIVOS",
     "El motor tiene un solo tipo HABILES_ADMINISTRATIVOS (R6) sobre los feriados de la jurisdicción del "
     "expediente. No hay calendario administrativo municipal ni nacional, ni asuetos administrativos. ¿Hace falta "
     "un alcance nuevo en holidays_calendar (por ejemplo, ADMINISTRACION_PROVINCIAL, MUNICIPIO, ADMINISTRACION_"
     "NACIONAL) o se resuelve con inhábiles manuales? Propuesta V1: inhábiles manuales. Solo se registra.",
     "Todos los hitos HABILES_ADMINISTRATIVOS"),
    ("[PRODUCTO] La vía administrativa: ¿flujo PREJUDICIAL o parte del judicial?",
     "flows.flow_kind distingue PREJUDICIAL (sin régimen procesal) y JUDICIAL (desde la demanda). La vía "
     "administrativa tiene su propio régimen (Decreto-Ley 7647/70, Ordenanza General 267/80, Ley 19.549) y "
     "hitos que se cruzan con el juicio (amparo por mora, pedido de suspensión del art. 25 Ley 12.008, cautelar "
     "anticipada). ¿Se publica 'Previa' más 'Vía administrativa' como flujo PREJUDICIAL y el resto como JUDICIAL? "
     "¿O hace falta un régimen administrativo para el flujo prejudicial? Propuesta: PREJUDICIAL con las fases Previa "
     "y Vía administrativa (y las variantes administrativas: empleo público, tributario, licitaciones); JUDICIAL "
     "desde la demanda. Solo se registra.",
     "Hitos de las fases Previa, Vía administrativa, Empleo público, Tributario y Licitaciones"),
    ("[PRODUCTO] Roles propios y abogado del Estado",
     "El enum es ACTORA, DEMANDADA, TRIBUNAL, AMBAS. Se modeló a la Administración que resuelve como DEMANDADA y a "
     "los organismos de control que no son parte (AAIP, Tribunal Fiscal de Apelación) como TRIBUNAL, nombrados en el "
     "hito. ¿Hacen falta roles ADMINISTRACION y ORGANISMO_DE_CONTROL? Y si el estudio representa al Estado (un "
     "municipio, un ente, una caja), ¿represented_role = DEMANDADA y los plazos de la Administración pasan a ser "
     "propios? Propuesta V1: mantener el enum y documentar el mapeo en Valores. No se modifica el contrato de API.",
     "Todos"),
    ("[PRODUCTO] Vinculación de expedientes",
     "Hay casos que viven en dos expedientes: el expediente administrativo y el judicial; el amparo por mora y el "
     "juicio de fondo; la cautelar anticipada y la demanda; el reclamo ante el IPS que sigue en contencioso; la "
     "denuncia ante la AAIP y el hábeas data; el amparo que deriva a contencioso. ¿Cómo se vinculan? Propuesta: hito "
     "final 'Sigue en la matriz de ...' y expediente vinculado, sin copiar datos sensibles. Solo se registra.",
     "Hitos 'Sigue en la matriz de ...'"),
    ("[PRODUCTO] Datos sensibles: salud, previsión y crédito",
     "Los amparos de salud usan historia clínica, prescripción médica y certificado de discapacidad; la seguridad "
     "social, recibos de haberes y números de beneficio; el hábeas data, informes crediticios. ¿Qué datos de salud "
     "guarda la app y quién del estudio los ve? ¿Los avisos y notificaciones pueden mostrar el nombre del hito sin "
     "revelar un diagnóstico (por ejemplo, 'Cumplimiento de la cautelar' y no la prestación)? Relacionar con "
     "modelado_de_amenazas_v1.md (activo A1, datos del estudio, confidencial) y legal/politica_de_privacidad.md (el "
     "estudio es responsable y Foja encargado; la AAIP es el órgano de control de la Ley 25.326). No se modifican "
     "esos documentos; solo se registra la duda.",
     "Todos"),
    ("[PRODUCTO] Catálogo de régimen procesal y tipos de tribunal",
     "procedural_regimes tiene hoy PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057 (y las otras matrices pidieron los suyos). "
     "Para Derecho Público harían falta, por ejemplo, PBA_CA_LEY_12008, PBA_AMP_LEY_13928 y PBA_HD_LEY_14214; y, si "
     "se aceptan los caminos federales, NAC_SS_LEY_24463_CPCCN, NAC_AMP_LEY_16986 y NAC_HD_LEY_25326. "
     "courts.court_type no tiene Juzgado ni Cámara en lo Contencioso Administrativo, juzgados federales ni la "
     "Cámara Federal de la Seguridad Social. No se modifican el contrato de API ni el modelo de datos; solo se "
     "registra.",
     "Hoja Flujo"),
    ("[PRODUCTO] Estado nacional en el contencioso",
     "La matriz de contencioso solo cubre a la Provincia, los municipios y los entes provinciales. El contencioso "
     "contra el Estado nacional (Ley 19.549 reformada, CPCCN, Ley 26.854) figura solo como cuadro de equivalencias "
     "en publico/README.md y como salida 'Demandado nacional'. ¿Se arma una matriz federal aparte cuando se resuelva "
     "la duda de jurisdicción federal? Propuesta: sí. " + FUENTE_LPA,
     "CAD_985"),
]

DUDA_REMITIR_TRANSVERSALES = (
    "Dudas transversales y de producto",
    "Las dudas transversales de Derecho Público (gracia por jurisdicción, gracia en los plazos para demandar, "
    "calendario administrativo, horas del amparo federal, feria, tasas, honorarios, beneficio de litigar sin "
    "gastos, numeración de la Ley 12.008, reglas del motor) y las de producto (jurisdicción federal, calendario "
    "administrativo, prejudicial o judicial, roles y abogado del Estado, vinculación de expedientes, datos "
    "sensibles, catálogo de régimen, Estado nacional) se responden una sola vez en "
    "matriz_publico_contencioso_pba.xlsx. Las reglas del motor D26 a D34 de la matriz laboral valen salvo donde "
    "estos procesos se apartan. ¿Hay algo de esta matriz que se aparte de esas respuestas?",
    "Todos",
)

CUADRO_EQUIVALENCIAS_NACION = """
| Instituto | Provincia de Buenos Aires (esta matriz) | Estado nacional (fuera de esta matriz) |
| :--- | :--- | :--- |
| Procedimiento administrativo | Decreto-Ley 7647/70 (municipios: Ordenanza General 267/80) | Ley 19.549 reformada por la Ley 27.742 y su reglamentación |
| Agotamiento de la vía | Obligatorio con excepciones (art. 14 Ley 12.008) | Obligatorio con excepciones (arts. 23, 24, 30 y 32 Ley 19.549) |
| Silencio | Pronto despacho y 30 días hábiles administrativos (art. 16 Ley 12.008; art. 79 Decreto-Ley 7647/70) | 60 días si no hay plazo especial (art. 10 Ley 19.549) |
| Recursos | Revocatoria 10 días, jerárquico 10 días (arts. 89 y 92 Decreto-Ley 7647/70) | Plazo no menor de 30 días (art. 23 Ley 19.549 reformada; reglamento a verificar) |
| Plazo para demandar | 90 días (art. 18 Ley 12.008) | 180 días hábiles judiciales (art. 25 Ley 19.549); recurso directo 30 días (art. 25 bis) |
| Reclamo previo | Según el caso (art. 14 Ley 12.008) | Obligatorio salvo excepciones; 90 días para resolver (arts. 30 y 31 Ley 19.549) |
| Amparo por mora | Art. 76 Ley 12.008 | Art. 28 Ley 19.549 (informe en el plazo que fije el juez) |
| Código procesal | Ley 12.008 y CPCCBA supletorio | CPCCN |
| Cautelares contra el Estado | Arts. 22 a 25 Ley 12.008 | Ley 26.854 (informe previo 5 días; vigencia hasta 6 meses) |
| Tribunal | Juzgado y Cámara en lo Contencioso Administrativo; SCBA | Juzgados federales; Cámara Contencioso Administrativo Federal; CSJN |
| Responsabilidad del Estado | Sin ley provincial ni adhesión a la Ley 26.944 (a verificar) | Ley 26.944 (prescripción de 3 años, art. 7) |
"""
