"""Partes comunes de las matrices del fuero Penal (CPP PBA, Ley 11.922).

No importa nada de civil/, laboral/ ni familia/: el proceso penal tiene plazos y roles propios.
Las dudas transversales y de producto se responden una sola vez en la matriz de investigación.
"""
import datos

ROLES = datos.ROLES
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS
CIERRA = ""

FUENTE_CPP = ("Fuente consultada el 13/11/2026: texto actualizado de la Ley 11.922 (CPP PBA) en normas.gba.gob.ar "
              "y leyes-ar.com (última actualización citada 16/10/2026).")

DESCRIPCION_PLAZOS = {
    "HABILES_JUDICIALES": (
        "Días hábiles judiciales (calendario judicial PBA). En el proceso penal el art. 139 CPP PBA dispone que los "
        "plazos son continuos y computan feriados; este tipo se usa solo si la norma habla de días hábiles, como los "
        "recursos extraordinarios ante la SCBA (art. 483: 10 días hábiles). El art. 124 CPCCBA (gracia) no rige: "
        "Aplica_Gracia = NO."
    ),
    "CORRIDOS": (
        "Días corridos (continuos): es el tipo por defecto del proceso penal (art. 139 CPP PBA). Si el último día es "
        "inhábil, se prorroga al hábil siguiente (art. 139). La feria suspende solo algunos plazos expresamente "
        "(oposición del art. 336, impugnación del auto de elevación y de la sentencia definitiva), salvo flagrancia. "
        "Sin gracia."
    ),
    "HABILES_ADMINISTRATIVOS": (
        "Días hábiles administrativos (lunes a viernes sin feriados; las ferias judiciales no suspenden). Este flujo "
        "penal no lo usa salvo que una norma especial lo fije. Sin gracia."
    ),
    "MESES": (
        "Meses, de fecha a fecha (regla R7 del motor). En penal: duración de la IPP (art. 282) y sus prórrogas, "
        "plazo del nuevo fiscal (art. 283) y plazo para realizar el debate (art. 339). Sin gracia."
    ),
    "ANIOS": (
        "Años, de fecha a fecha (regla R7), como la prescripción de la acción (Código Penal, arts. 62 y siguientes), "
        "la duración máxima del proceso con detenido (art. 141: 2 años) o el plazo de la suspensión del juicio a "
        "prueba. Sin gracia."
    ),
    "HORAS": (
        "Horas corridas desde la fecha y hora del disparador (regla R8), no desde el día hábil siguiente. Sin gracia. "
        "En penal hay plazos en horas con persona detenida (declaración del imputado, flagrancia, hábeas corpus, "
        "excarcelación tras prisión preventiva) que pueden correr en días inhábiles (a verificar con el motor)."
    ),
    "FECHA_FIJADA": (
        "Acto con fecha y hora fijadas (audiencias, debate, vencimiento que fija el juez). Valor 0: el abogado carga "
        "la fecha y la hora. Sin gracia."
    ),
    "ANTICIPACION_HABILES_JUDICIALES": (
        "Días hábiles judiciales contados hacia atrás desde un acto fijado (regla R9). En penal: el acuerdo de "
        "juicio abreviado hasta 30 días antes del debate (art. 397) se modela como anticipación o como control "
        "manual (ver dudas). Sin gracia."
    ),
    "SIN_PLAZO": (
        "Sin plazo perentorio (valor 0). Depende del fiscal, del juez o de la parte; si el plazo lo fija el órgano "
        "en cada caso, el abogado lo carga como plazo suelto. Sin gracia."
    ),
}
assert set(DESCRIPCION_PLAZOS) == {t for t, _ in datos.PLAZO_TIPOS}


def plazo_tipos(usos):
    return [(t, f"{DESCRIPCION_PLAZOS[t]} En este flujo: {usos.get(t, 'no se usa.')}") for t, _ in datos.PLAZO_TIPOS]


def flujo(nombre, regimen, notas):
    return {
        "Flujo": nombre,
        "Jurisdicción": "PBA",
        "Fuero": "Penal",
        "Régimen procesal": regimen,
        "Versión": "1 (borrador)",
        "Fecha del borrador": "13/11/2026",
        "Validado por (equipo legal)": "",
        "Fecha de validación": "",
        "Notas": notas,
    }


NOTA_FUENTES = (
    "Borrador para validar con el abogado. Las citas se cotejaron el 13/11/2026 con normas.gba.gob.ar, leyes-ar.com "
    "y el cronograma de implementación del CPPF (argentina.gob.ar / Boletín Oficial); las que no se pudieron "
    "confirmar dicen '(a verificar)' y tienen su duda. No contiene ni debe contener datos personales de nadie."
)

NOTA_SENSIBLES = (
    "Datos sensibles: la causa puede ser reservada; hay víctimas, detenidos, testigos y menores. No escribas nombres, "
    "DNI, domicilios, números de causa o IPP ni relatos de hechos en las celdas: nombrá los documentos, no su contenido."
)

REGIMEN_CPP = "CPP PBA (Ley 11.922 y modificatorias)"

FASES_COMUNES_BASE = [
    "Previa",
    "Investigación",
    "Libertad",
    "Prueba",
    "Salidas alternativas",
    "Etapa intermedia",
    "Flagrancia",
    "Juicio",
    "Jurados",
    "Debate",
    "Sentencia",
    "Recursos",
    "Abreviado",
    "Hábeas corpus",
    "Cierre",
]

LEYENDA = {
    "roles": (
        "celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima constituida en parte "
        "(ACTORA); naranja = imputado y defensa (DEMANDADA); gris = Juzgado de Garantías, juzgado o tribunal de "
        "juicio, Cámara, Casación, SCBA, policía, servicio penitenciario o peritos, aclarado en el nombre del hito "
        "(TRIBUNAL); violeta = cualquiera de las partes (AMBAS)."
    ),
    "paralelo": (
        "con imputado detenido, la excarcelación y el pedido de prisión preventiva corren en paralelo con la "
        "producción de prueba y el control del plazo de la IPP"
    ),
    "adicionales": [
        ("**Derivación a otra matriz:** caja con borde grueso (hito final) cuyo nombre empieza con "
         "\"Sigue en la matriz de ...\": el expediente continúa en ese otro flujo penal, en un expediente vinculado."),
        ("**Fase \"Previa\":** hitos anteriores a la intervención judicial formal (consulta, denuncia, designación "
         "de defensor, constitución como particular damnificado). La app los separa en el flujo prejudicial; en "
         "penal hay duda sobre si eso tiene sentido desde la denuncia."),
        ("**Plazos corridos (art. 139 CPP PBA):** la mayoría de los plazos procesales penales son días continuos "
         "(CORRIDOS), no hábiles judiciales. Aplica_Gracia = NO en todos los hitos."),
    ],
}


def leyenda(roles, paralelo, adicionales=None):
    return {
        "roles": roles,
        "paralelo": paralelo,
        "adicionales": LEYENDA["adicionales"] + (adicionales or []),
    }


ROLES_DESCRIPCION_PENAL = [
    ("ACTORA",
     "La acusación: el Ministerio Público Fiscal y el particular damnificado (o la víctima constituida en parte). "
     "El abogado puede representar al particular damnificado, nunca al fiscal; los actos del fiscal igual disparan "
     "plazos para las otras partes."),
    ("DEMANDADA",
     "El imputado y su defensa (particular u oficial). Es lo que el abogado representa con más frecuencia."),
    ("TRIBUNAL",
     "El Juzgado de Garantías, el juzgado o tribunal de juicio, la Cámara de Apelación y Garantías, el Tribunal de "
     "Casación Penal, la SCBA, y también la policía, el servicio penitenciario y los peritos de la Asesoría Pericial, "
     "aclarado en el nombre del hito."),
    ("AMBAS",
     "Cualquiera de las partes: recursos, pedidos de prueba, honorarios, audiencias."),
]

ROLES_DESCRIPCION_HABEAS = [
    ("ACTORA",
     "Quien interpone el hábeas corpus: la persona afectada o cualquiera a su favor (art. 407 CPP PBA), con o sin abogado."),
    ("DEMANDADA",
     "La autoridad requerida: policía, servicio penitenciario u otra autoridad o particular que restringe la libertad."),
    ("TRIBUNAL",
     "El juez o tribunal con competencia penal que conoce del hábeas corpus, la Cámara o Casación en la impugnación."),
    ("AMBAS",
     "Cualquiera de los intervinientes en la audiencia o en el recurso."),
]

INSTRUCCIONES_ADICIONALES = [
    ("Particularidades del fuero Penal", True),
    ("9. Plazos corridos (art. 139 CPP PBA): la mayoría de los plazos procesales son días continuos (CORRIDOS). Si el último día es inhábil, se prorroga al hábil siguiente. La feria suspende solo los plazos que la norma enumera (oposición del art. 336, impugnación del auto de elevación y de la sentencia definitiva), salvo en flagrancia.", False),
    ("10. Sin gracia del art. 124 CPCCBA: Aplica_Gracia = NO en todos los hitos. Si el CPP PBA tuviera un plazo de gracia propio, el equipo legal lo confirma en las dudas.", False),
    ("11. Plazos en HORAS (declaración del imputado, flagrancia, hábeas corpus, excarcelación tras prisión preventiva): corren desde la fecha y la hora exactas del Evento_Disparador (regla R8). Con detenido pueden correr en días inhábiles (a verificar).", False),
    ("12. Derivación a otra matriz: los hitos finales llamados 'Sigue en la matriz de ...' indican que el proceso continúa en otro flujo penal (investigación → juicio oral o abreviado; hábeas corpus; ejecución).", False),
    ("13. Datos sensibles: no escribas nombres, DNI, domicilios, números de causa o IPP ni relatos de hechos. Nombrá los documentos (acta de aprehensión, requerimiento), no su contenido. La causa puede ser reservada.", False),
    ("", False),
]


def ordenar(nodos, transiciones, por_numero=True):
    if por_numero:
        nodos = sorted(nodos, key=lambda n: int(n[0].split("_")[1]))
    posicion = {n[0]: i for i, n in enumerate(nodos)}
    return nodos, sorted(transiciones, key=lambda t: posicion[t[0]])


def numerar(dudas):
    return [(f"D{i:02d}", *d) for i, d in enumerate(dudas, start=1)]


# --- Bloques reutilizables de nodos (recursos y situación de libertad) -----------------

RECURSOS = ("800", "810", "820", "830", "840")


def nodos_recursos(p, incluir=RECURSOS, fase="Recursos"):
    """Recursos penales comunes. 810 es la apelación de la sentencia definitiva correccional (20 días).

    La reposición (800) siempre es un camino paralelo. Los demás están en la línea principal del flujo:
    sus salidas van al hito de firmeza que indique trans_recursos.
    """
    nodos = [
        (f"{p}_800", fase, "Recurso de reposición", "AMBAS",
         "Notificación de la resolución dictada sin sustanciación", 3, "CORRIDOS", "NO",
         "Arts. 436 a 438 CPP PBA", "NO", "NO",
         ["Interponer por escrito fundado dentro del tercer día (art. 437)",
          "Durante el juicio solo procede reposición, que vale como protesta de recurrir (art. 429)",
          "Puede deducirse junto con la apelación en subsidio (art. 438)"],
         ["Escrito de reposición"]),
        (f"{p}_810", fase, "Apelación de la sentencia correccional ante la Cámara (20 días)", "AMBAS",
         "Notificación de la sentencia definitiva del Juzgado Correccional", 20, "CORRIDOS", "NO",
         "Arts. 21 inc. 4, 439 y 441 CPP PBA", "NO", "NO",
         ["Contra sentencias definitivas el plazo es de 20 días; contra autos, de 5 (art. 441)",
          "Fiscal y particular damnificado: contra la absolución si pidieron condena, o contra la condena si la pena "
          "es inferior a la mitad de la pedida (art. 441)",
          "Indicar motivos y fundamentos bajo sanción de inadmisibilidad (art. 421)",
          "Feria: se suspende el plazo de impugnación de la sentencia definitiva (art. 139), salvo flagrancia",
          "Queja contra la denegatoria: 3 días (art. 433)"],
         ["Escrito de apelación"]),
        (f"{p}_820", fase, "Recurso de casación ante el Tribunal de Casación Penal (20 días)", "AMBAS",
         "Notificación de la sentencia definitiva (juicio oral, abreviado o directísimo en lo criminal)", 20,
         "CORRIDOS", "NO",
         "Arts. 20, 448 a 451 CPP PBA", "NO", "NO",
         ["Plazo de 20 días desde la notificación; escrito fundado con citas y solución pretendida (art. 451)",
          "Dentro de los primeros 7 días, manifestar la intención de recurrir ante el órgano que dictó la sentencia; "
          "si no, queda firme para quien omitió (art. 451)",
          "Jurados: solo la sentencia condenatoria; la absolución por veredicto de no culpabilidad es irrecurrible "
          "(arts. 371 quáter y 450)",
          "En lo correccional no hay casación: la sentencia se apela ante la Cámara (arts. 21 inc. 4 y 450)",
          "Feria: el plazo de impugnación de la sentencia definitiva se suspende (art. 139), salvo flagrancia",
          "Queja contra la denegatoria: 10 días (art. 433)"],
         ["Manifestación de recurrir", "Escrito de casación"]),
        (f"{p}_830", fase, "Recursos extraordinarios ante la SCBA (10 días hábiles)", "AMBAS",
         "Notificación de la sentencia definitiva de Casación o de la Cámara", 10, "HABILES_JUDICIALES", "NO",
         "Arts. 479 a 496 CPP PBA; art. 161 Constitución PBA", "NO", "NO",
         ["Inaplicabilidad de ley, nulidad e inconstitucionalidad (art. 479)",
          "Interponer ante el órgano que dictó la sentencia, dentro de los 10 días hábiles de notificada (art. 483)",
          "Sentencia definitiva a estos fines: la que termina la causa o hace imposible su continuación (art. 482)",
          "Si se rechaza, costas al recurrente (arts. 490 y 493)"],
         ["Escrito de recurso extraordinario provincial"]),
        (f"{p}_840", fase, "Recurso extraordinario federal", "AMBAS",
         "Notificación de la sentencia definitiva de la SCBA o del superior tribunal de la causa", 0, "SIN_PLAZO",
         "NO",
         "Art. 14 Ley 48; art. 257 CPCCN (plazo de 10 días hábiles, a verificar cómputo)", "NO", "NO",
         ["Evaluar cuestión federal suficiente",
          "Cargar el plazo como plazo suelto: 10 días hábiles con el calendario judicial federal, no el de PBA "
          "(a verificar)",
          "Efecto sobre la libertad del condenado: ver duda específica"],
         ["Escrito de recurso extraordinario federal"]),
    ]
    return [n for n in nodos if n[0].split("_")[1] in incluir]


def trans_recursos(p, firmeza, incluir=RECURSOS, reenvio=None):
    """Salidas de los recursos. `firmeza` es el hito que sigue cuando se agota o se abandona la vía."""
    extraordinarios = "830" in incluir
    t = [
        (f"{p}_800", "Reposición resuelta o plazo vencido", CIERRA),
        (f"{p}_810", "La Cámara resuelve y no se recurre más", firmeza),
        (f"{p}_810", "Apelación denegada: queja resuelta o no interpuesta", firmeza),
        (f"{p}_820", "Casación resuelta y no se recurre más", firmeza),
        (f"{p}_820", "Casación denegada o no manifestada en 7 días: queja resuelta o no interpuesta", firmeza),
        (f"{p}_830", "La SCBA resuelve o el recurso no se concede, sin cuestión federal", firmeza),
        (f"{p}_830", "Hay cuestión federal: recurso extraordinario federal", f"{p}_840"),
        (f"{p}_840", "Recurso federal resuelto, desistido o denegado", firmeza),
    ]
    if extraordinarios:
        t += [
            (f"{p}_810", "La Cámara resuelve: recursos extraordinarios ante la SCBA", f"{p}_830"),
            (f"{p}_820", "Casación resuelta: recursos extraordinarios ante la SCBA", f"{p}_830"),
        ]
    if reenvio:
        t.append((f"{p}_820", "Casación anula y reenvía a nuevo juicio (art. 473)", reenvio))
    return [x for x in t if x[0].split("_")[1] in incluir]


def nodos_libertad(p):
    """Situación de libertad del imputado: aprehensión, detención, PP, excarcelación y alternativas."""
    return [
        (f"{p}_200", "Libertad", "Aprehensión o detención del imputado", "TRIBUNAL",
         "Aprehensión policial o detención ordenada", 0, "SIN_PLAZO", "NO",
         "Arts. 151 a 156 CPP PBA", "NO", "NO",
         ["Con detenido: corre en días inhábiles (a verificar)",
          "Controlar el acta de aprehensión y la comunicación inmediata al fiscal y al juez de garantías",
          "Verificar que se informe el derecho a defensor y, si es extranjero, a asistencia consular (art. 308)",
          "No registrar en la app el relato de los hechos ni datos de identidad de víctimas"],
         ["Acta de aprehensión", "Constancia de comunicación al fiscal"]),
        (f"{p}_210", "Libertad", "Comunicación al Juez de Garantías y puesta a disposición", "TRIBUNAL",
         "Aprehensión o detención efectivizada", 0, "SIN_PLAZO", "NO",
         "Arts. 155, 161 y 284 ter CPP PBA (plazo concreto de puesta a disposición ante el juez, a verificar)",
         "NO", "NO",
         ["Con detenido: corre en días inhábiles (a verificar)",
          "La policía presenta de inmediato al aprehendido ante el fiscal (art. 155)",
          "Mientras el juez no ordene la detención, el fiscal puede liberarlo si no pedirá la prisión preventiva "
          "(art. 161)",
          "Flagrancia: el fiscal pide al Juez de Garantías convertir la aprehensión en detención (art. 284 ter)",
          "Si no hay puesta a disposición, evaluar hábeas corpus (art. 405)"],
         ["Oficio o constancia de puesta a disposición"]),
        (f"{p}_220", "Libertad", "Declaración del imputado (con detenido: 24 horas)", "ACTORA",
         "Momento en que se produjo la restricción de la libertad (fecha y hora)", 24, "HORAS", "NO",
         "Art. 308 CPP PBA", "NO", "NO",
         ["Con detenido: corre en días inhábiles (a verificar)",
          "El acto debe cumplirse de inmediato o a más tardar en 24 horas; prórroga por igual plazo si el fiscal no pudo recibirlo o el imputado pide proponer defensor (art. 308)",
          "Notificar al defensor bajo sanción de nulidad; asesorar sobre si conviene declarar",
          "Si el imputado lo pide motivadamente, puede declarar ante el Juez de Garantías (a verificar)",
          "No es 'indagatoria': en PBA es declaración del imputado (ver cuadro de equivalencias)"],
         ["Acta de declaración del imputado", "Designación de defensor"]),
        (f"{p}_230", "Libertad", "Pedido de excarcelación o eximición de prisión", "DEMANDADA",
         "Detención, citación con riesgo de coerción, o dictado de la prisión preventiva", 0, "SIN_PLAZO", "NO",
         "Arts. 169 a 191 CPP PBA", "NO", "NO",
         ["Tramita por incidente separado (art. 172)",
          "Evaluar excarcelación ordinaria, extraordinaria (art. 170) y peligros procesales (art. 171)",
          "Ofrecer caución juratoria, real o personal (art. 177)",
          "Si hay prisión preventiva, el juez debe resolver en 24 horas (art. 174)"],
         ["Escrito de excarcelación o eximición", "Ofrecimiento de caución"]),
        (f"{p}_240", "Libertad", "Resolución del pedido de excarcelación", "TRIBUNAL",
         "Presentación del pedido de excarcelación (o, si ya hay prisión preventiva, su presentación)", 5,
         "CORRIDOS", "NO",
         "Art. 174 CPP PBA", "NO", "NO",
         ["Plazo general: 5 días; si se pide después de la prisión preventiva: 24 horas (modelar el caso con plazo suelto o cambiar el tipo a HORAS)",
          "Con detenido: corre en días inhábiles (a verificar)",
          "Controlar la clase de caución y las obligaciones especiales (arts. 177 y 180)"],
         ["Auto de excarcelación o denegatoria"]),
        (f"{p}_250", "Libertad", "Pedido de prisión preventiva por el Fiscal", "ACTORA",
         "Efectivización de la detención", 15, "CORRIDOS", "NO",
         "Arts. 157 y 158 CPP PBA", "NO", "NO",
         ["El fiscal tiene 15 días prorrogables por otros 15 desde la detención para solicitar la PP (art. 158)",
          "Requisitos del art. 157: delito justificado, declaración del art. 308 o negativa, indicios de autoría y presupuestos del art. 171",
          "Flagrancia: el pedido se formula junto con la requisitoria de elevación (art. 284 sexies)",
          "Con detenido: corre en días inhábiles (a verificar)"],
         ["Requerimiento de prisión preventiva"]),
        (f"{p}_260", "Libertad", "Auto de prisión preventiva", "TRIBUNAL",
         "Solicitud fiscal de prisión preventiva", 5, "CORRIDOS", "NO",
         "Art. 158 CPP PBA", "NO", "NO",
         ["El juez dicta el auto dentro del quinto día de la solicitud (art. 158)",
          "Controlar la motivación y los elementos de cargo",
          "Apelación ante la Cámara de Garantías o hábeas corpus (art. 164)",
          "Con detenido: corre en días inhábiles (a verificar)"],
         ["Auto de prisión preventiva"]),
        (f"{p}_270", "Libertad", "Apelación de la coerción o de la denegatoria de excarcelación", "AMBAS",
         "Notificación del auto de detención, prisión preventiva o denegatoria de cese/excarcelación", 5,
         "CORRIDOS", "NO",
         "Arts. 164, 188 y 441 CPP PBA", "NO", "NO",
         ["Apelación ante la Cámara de Apelación y Garantías (art. 164)",
          "Eximición de prisión: impugnación en 48 horas (art. 188); cargar como HORAS si se confirma",
          "Evaluar en paralelo el hábeas corpus (art. 405)"],
         ["Escrito de apelación"]),
        (f"{p}_280", "Libertad", "Alternativas a la prisión preventiva y morigeración", "DEMANDADA",
         "Pedido de alternativa o morigeración, o revisión de la PP", 0, "SIN_PLAZO", "NO",
         "Arts. 147, 159, 160 y 163 CPP PBA", "NO", "NO",
         ["Alternativas (art. 159): mayores de 70 años, enfermedad terminal, embarazo o hijos menores de 5 años, si "
          "el peligro procesal se evita con una medida menos gravosa",
          "Modalidades: cuidado de persona o institución, presentaciones, prohibiciones, monitoreo (art. 160)",
          "Morigeración (art. 163): prisión domiciliaria, salidas laborales o ingreso a institución; es apelable y "
          "se hace efectiva cuando queda firme",
          "Cese de la medida si desaparecen sus condiciones (art. 147)"],
         ["Escrito de alternativa o morigeración"]),
        (f"{p}_290", "Libertad", "Control del plazo máximo con detenido (2 años)", "DEMANDADA",
         "Inicio de la privación de libertad (disparador a verificar)", 2, "ANIOS", "NO",
         "Art. 141 CPP PBA (términos fatales con detenido); art. 2 (plazo razonable); Ley 24.390 (a verificar "
         "aplicación en PBA)", "NO", "NO",
         ["Con detenido, los plazos de la IPP y de duración total del proceso son fatales: hasta 2 años (art. 141)",
          "En casos de suma complejidad rige el plazo razonable del art. 2, a criterio judicial",
          "Si vence, pedir la libertad, el cese o la morigeración de inmediato",
          "Con detenido: corre en días inhábiles y no se suspende en feria (a verificar)"],
         ["Cómputo de detención", "Pedido de cese"]),
    ]


def trans_libertad(p, ids=None):
    """Salidas del bloque de libertad. Todo el bloque son caminos paralelos: cierran con CIERRA o derivan a hábeas.

    `ids` limita las salidas a un subconjunto de hitos (el juicio oral no usa la cadena de aprehensión).
    """
    t = [
        (f"{p}_200", "Detenido a disposición", f"{p}_210"),
        (f"{p}_200", "Detenido a disposición", f"{p}_220"),
        (f"{p}_200", "Detenido a disposición", f"{p}_230"),
        (f"{p}_200", "Detenido a disposición", f"{p}_250"),
        (f"{p}_210", "Puesta a disposición cumplida", CIERRA),
        (f"{p}_210", "Sin puesta a disposición: hábeas corpus", f"{p}_960"),
        (f"{p}_220", "Declaración recibida o negativa a declarar", CIERRA),
        (f"{p}_220", "Vencido el plazo sin declaración: pedir la libertad o hábeas corpus", f"{p}_960"),
        (f"{p}_230", "Pedido presentado", f"{p}_240"),
        (f"{p}_240", "Excarcelación concedida", CIERRA),
        (f"{p}_240", "Excarcelación denegada: apelación", f"{p}_270"),
        (f"{p}_240", "Excarcelación denegada: alternativas o morigeración", f"{p}_280"),
        (f"{p}_240", "Excarcelación denegada: hábeas corpus", f"{p}_960"),
        (f"{p}_250", "El fiscal pide la prisión preventiva", f"{p}_260"),
        (f"{p}_250", "No se pide: libertad (art. 161) o el pedido va con la requisitoria en flagrancia", CIERRA),
        (f"{p}_260", "PP dictada", f"{p}_270"),
        (f"{p}_260", "PP dictada", f"{p}_280"),
        (f"{p}_260", "PP dictada", f"{p}_290"),
        (f"{p}_260", "PP dictada: hábeas corpus ante la Cámara (art. 405)", f"{p}_960"),
        (f"{p}_260", "PP rechazada: libertad", CIERRA),
        (f"{p}_270", "Apelación resuelta por la Cámara, desistida o no interpuesta", CIERRA),
        (f"{p}_270", "Se opta por el hábeas corpus (art. 164)", f"{p}_960"),
        (f"{p}_280", "Alternativa o morigeración resuelta", CIERRA),
        (f"{p}_290", "El proceso terminó o la detención cesó antes del vencimiento", CIERRA),
        (f"{p}_290", "Vence el plazo: pedir libertad, cese o morigeración", f"{p}_280"),
        (f"{p}_290", "Vence el plazo: hábeas corpus", f"{p}_960"),
    ]
    if ids is None:
        return t
    return [x for x in t if x[0] in ids]


# --- Dudas transversales y de producto (solo en investigación; las otras remiten) ------

DUDAS_TRANSVERSALES = [
    ("[TRANSVERSAL] Plazo de gracia en el proceso penal",
     "El art. 124 CPCCBA (día de gracia) no rige en el proceso penal. ¿El CPP PBA tiene un plazo de gracia propio? "
     "¿A qué escritos se aplica? Propuesta de la app: sin gracia en todos los hitos (vencimiento más temprano). "
     + FUENTE_CPP + " Art. 139: plazos continuos.",
     "Todos"),
    ("[TRANSVERSAL] Plazos con persona detenida",
     "¿Los plazos con persona detenida (declaración del art. 308, coerción, hábeas corpus, flagrancia) corren en "
     "días y horas inhábiles y no se suspenden en la feria? ¿Cómo debe tratarlos el motor (hoy asume día cero hábil "
     "siguiente salvo HORAS)? Propuesta: en HORAS desde la fecha/hora exacta; en CORRIDOS sin suspender por feria "
     "cuando hay detenido. " + FUENTE_CPP,
     "Todos los hitos con checklist 'Con detenido'"),
    ("[TRANSVERSAL] Cómputo de plazos en horas",
     "Regla R8 del motor: horas corridas desde el disparador. ¿En penal se interrumpen de noche o en días inhábiles? "
     "Propuesta: no se interrumpen (vencimiento más temprano), salvo que el equipo legal indique lo contrario. "
     "Fuente: logica_matematica_calculadora_de_dias_habiles_judiciales.md y art. 308/409/415 CPP PBA.",
     "Hitos en HORAS"),
    ("[TRANSVERSAL] Plazos corridos vs hábiles judiciales",
     "Art. 139 CPP PBA: los plazos son continuos y computan feriados; si vencen en inhábil, se prorrogan al hábil "
     "siguiente; la feria suspende solo oposición (336), impugnación del auto de elevación y de la sentencia "
     "definitiva, salvo flagrancia. ¿Confirmamos CORRIDOS como tipo por defecto y no HABILES_JUDICIALES? "
     "Propuesta: sí. " + FUENTE_CPP,
     "Todos"),
    ("[TRANSVERSAL] Duración de la IPP y prórrogas",
     "Art. 282: 4 meses desde la detención o la declaración del art. 308; prórroga fiscal hasta 2 meses; en casos "
     "excepcionales hasta 6 meses. Art. 283: vencido el plazo, el juez requiere al Fiscal General la sustitución y "
     "el nuevo fiscal tiene 2 meses. ¿El cómputo es de meses corridos (regla R7)? ¿Qué puede hacer la defensa al "
     "vencer? Propuesta: 4 MESES desde el disparador; alertar al vencer. " + FUENTE_CPP,
     "IPP_400, IPP_410, IPP_420"),
    ("[TRANSVERSAL] Plazo máximo con detenido (art. 141)",
     "Art. 141: si el imputado está privado de libertad, los términos de la IPP y de duración total del proceso "
     "son fatales y el proceso no puede durar más de 2 años; en casos de suma complejidad rige el plazo razonable "
     "del art. 2. ¿Desde qué acto se cuentan los 2 años (aprehensión, detención o prisión preventiva)? ¿Se aplica "
     "además la Ley 24.390 y sus cómputos? ¿Qué pide la defensa al vencer (libertad, cese, morigeración)? "
     "Propuesta: 2 ANIOS desde el inicio de la privación de libertad. " + FUENTE_CPP,
     "IPP_290, JOR_290"),
    ("[TRANSVERSAL] Derechos de la víctima y Ley 27.372",
     "En PBA los derechos de la víctima están en los arts. 83 a 88 CPP PBA (texto Ley 15.232): información, "
     "revisión del archivo y de la desestimación (art. 83 incs. 8 y 15), opinión en el abreviado (art. 396) y en "
     "la suspensión del juicio a prueba (art. 404), notificación del pedido de sobreseimiento si lo pidió (art. "
     "325). ¿La Ley 27.372 se aplica además como norma de fondo en PBA? ¿La app debe alertar esas notificaciones "
     "aunque el abogado solo represente a la defensa? Propuesta: hitos de ACTORA para el particular damnificado y "
     "checklist de derechos de la víctima. " + FUENTE_CPP,
     "Todos"),
    ("[TRANSVERSAL] Prescripción de la acción penal",
     "Código Penal arts. 62 y siguientes: ¿cómo se computa en la app (ANIOS desde el hecho o desde la última "
     "actuación que interrumpe, art. 67 CP: primer llamado a declarar, requerimiento de elevación, citación a "
     "juicio, sentencia condenatoria aunque no esté firme)? ¿Quién carga las interrupciones? Propuesta: hito de "
     "control con ANIOS según el máximo de la escala; el abogado edita las interrupciones como plazos sueltos.",
     "IPP_050, JOR_010, JAB_010"),
    ("[TRANSVERSAL] Honorarios Ley 14.967",
     "¿En qué momento se regulan los honorarios en materia penal y cuál es el plazo de impugnación (art. 57 Ley "
     "14.967: 5 días)? ¿Son días corridos del CPP o hábiles del CPCCBA? Propuesta: 5 CORRIDOS sin gracia.",
     "Hitos de honorarios"),
    ("[TRANSVERSAL] Fuero penal juvenil, acción privada y ejecución",
     "Fuera de la V1: fuero penal juvenil (Ley 13.634), delitos de acción privada (querella) y ejecución de la pena "
     "(Ley 12.256). ¿Se confirman fuera de estas matrices, con la ejecución solo como hito final 'Sigue en ejecución "
     "penal'? Propuesta: sí.",
     "Hitos finales de ejecución"),
    ("[PRODUCTO] Roles propios del fuero penal",
     "El enum de la app es ACTORA/DEMANDADA/TRIBUNAL/AMBAS. ¿Hacen falta roles propios (FISCAL, DEFENSA, "
     "PARTICULAR_DAMNIFICADO, AUTORIDAD_REQUERIDA)? Propuesta V1: mantener el enum y documentar el mapeo en Valores; "
     "no cambiar el contrato de API.",
     "Todos"),
    ("[PRODUCTO] represented_role del abogado",
     "Cuando el abogado representa a la defensa, ¿represented_role = DEMANDADA? ¿Y cuando representa al particular "
     "damnificado, ACTORA? El fiscal nunca es cliente. Propuesta: sí.",
     "Todos"),
    ("[PRODUCTO] Flujo prejudicial vs judicial en penal",
     "La app separa la fase Previa en flujo PREJUDICIAL. En penal, ¿tiene sentido desde la denuncia/consulta, o todo "
     "es judicial desde la denuncia en comisaría/fiscalía? Propuesta: Previa = consulta, denuncia y designación de "
     "defensor; desde la IPP formal, judicial.",
     "Hitos de fase Previa"),
    ("[PRODUCTO] Plazos con detenido y gracia en el motor",
     "Hoy el motor (D26–D34 de la matriz laboral) no distingue 'con detenido' ni gracia penal. ¿Qué hay que cambiar "
     "para soportar CORRIDOS sin gracia, HORAS en inhábiles y feria selectiva del art. 139? Registrar; no modificar "
     "el motor en este repo.",
     "Todos"),
    ("[PRODUCTO] Vinculación de expedientes entre matrices",
     "¿Cómo se vinculan investigación↔juicio oral, investigación↔abreviado, causa principal↔hábeas corpus y "
     "condena↔ejecución? Propuesta: hito final de derivación + expediente vinculado con el mismo número de causa "
     "interno, sin copiar datos sensibles.",
     "Hitos 'Sigue en la matriz...'"),
    ("[PRODUCTO] Causa reservada y datos de víctimas/detenidos",
     "¿Cómo se marca una causa reservada? ¿Quién ve en el estudio los datos de una víctima o de un detenido? ¿Los "
     "avisos pueden revelar datos de la causa en el dispositivo? Relacionar con modelado_de_amenazas_v1.md y "
     "legal/politica_de_privacidad.md. No modificar esos documentos; solo registrar la duda.",
     "Todos"),
    ("[PRODUCTO] Matrices federales aparte",
     "Al 13/11/2026 el CPPF (Ley 27.063 T.O. 2019) rige en distritos federales con asiento en PBA: Mar del Plata, "
     "Bahía Blanca, Rosario/San Nicolás y La Plata (desde 21/09/2026, Res. MJ 275/2026). San Martín aún sin fecha; "
     "CABA/Penal Económico previstos para 15/02/2027. Donde no rige el CPPF sigue el CPPN (Ley 23.984). ¿Hacen falta "
     "matrices federales aparte? Propuesta: sí, en una carpeta federal/ futura; estas matrices son solo provinciales. "
     "Fuente: argentina.gob.ar (cronograma) y Boletín Oficial.",
     "Todos"),
    ("[PRODUCTO] Catálogo de régimen procesal",
     "La app hoy tiene PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057 (más civiles/familia/comercial si ya están). ¿Agregar "
     "PBA_PEN_LEY_11922 (y variantes flagrancia/jurados)? No modificar el contrato de API ni el modelo de datos; "
     "solo registrar.",
     "Hoja Flujo"),
    ("[PRODUCTO] Hito final alcanzado desde un camino paralelo",
     "Las derivaciones a hábeas corpus ('Sigue en la matriz de hábeas corpus') salen de caminos paralelos de "
     "libertad mientras la causa principal sigue abierta. ¿La app cierra el expediente al llegar a un hito final "
     "desde un camino paralelo, o solo crea el expediente vinculado y deja abiertos los demás caminos? Propuesta: "
     "en las derivaciones, crear el vinculado y no cerrar los otros caminos; registrar el requerimiento, sin "
     "cambiar el contrato de API ni el modelo de datos.",
     "IPP_960, JOR_960"),
    ("[PRODUCTO] Hito que se vuelve a abrir a sí mismo",
     "En la IPP, el hito de pedidos de prueba (IPP_300) abre cada medida (allanamiento, pericia, testigos, "
     "intervenciones) y se vuelve a abrir a sí mismo con la misma condición, para que la investigación siga "
     "abierta. ¿El importador y el motor aceptan una transición cuyo destino es el mismo hito de origen? "
     "Propuesta: sí; si no, separar un hito 'IPP en trámite' sin plazo.",
     "IPP_300"),
]

DUDA_REMITIR_TRANSVERSALES = (
    "Dudas transversales y de producto",
    "Las dudas transversales del fuero penal (gracia, plazos con detenido, horas, plazos corridos, IPP, plazo "
    "máximo con detenido, víctima, prescripción, honorarios, V1) y las de producto (roles, represented_role, "
    "prejudicial, motor, vinculación, datos sensibles, matrices federales, catálogo de régimen, finales desde "
    "caminos paralelos, hitos que se reabren) se responden una sola vez en "
    "matriz_penal_investigacion_pba.xlsx. Las reglas del motor D26–D34 de la matriz laboral valen salvo donde el "
    "proceso penal se aparta. ¿Hay algo de esta matriz que se aparte de esas respuestas?",
    "Todos",
)


def duda_federal(flujo_pba, equivalente, hitos):
    """Duda de equivalencia federal propia de cada matriz (el resto está en la duda de producto)."""
    return (
        "Equivalencia en el fuero federal",
        f"En los distritos federales con asiento en PBA rige el CPPF (Mar del Plata, Bahía Blanca, Rosario/San "
        f"Nicolás y La Plata) o todavía el CPPN (San Martín). {equivalente} Esta matriz modela solo {flujo_pba} "
        f"del CPP PBA. ¿Alcanza con el cuadro de equivalencias del README, o hay que avisar en la app cuando el "
        f"expediente es federal? Propuesta: avisar y no aplicar esta matriz. Ver la duda de producto 'Matrices "
        f"federales aparte' en la matriz de investigación.",
        hitos,
    )


CUADRO_EQUIVALENCIAS_FEDERAL = """
| Instituto federal (CPPN Ley 23.984 / práctica mixta) | Equivalente en CPP PBA (Ley 11.922) | Notas |
| :--- | :--- | :--- |
| Indagatoria | Declaración del imputado (art. 308) | No usar "indagatoria" en las matrices PBA. |
| Procesamiento | No hay equivalente exacto | En PBA la coerción típica es la prisión preventiva (arts. 157/158); la elevación a juicio cierra la IPP. |
| Falta de mérito | Sobreseimiento / archivo / no elevación (arts. 321 y ss., 334) | El CPP PBA no usa "falta de mérito" como auto típico del juez de instrucción. |
| Juez de instrucción | Fiscal (dirección de la IPP) + Juez de Garantías (control) | Sistema acusatorio. |
| Requerimiento de elevación a juicio / auto de elevación | Requerimiento fiscal (art. 334) + oposición (336) + auto o decreto de elevación (337) | Etapa intermedia ante el Juez de Garantías. |
| Excarcelación | Excarcelación / eximición de prisión (arts. 169 y ss.) | Vocabulario coincidente en lo sustancial. |
| Juicio abreviado | Juicio abreviado (arts. 395 a 403) | Límite: pena pedida ≤ 15 años (art. 395). |
| Hábeas corpus (Ley 23.098) | Hábeas corpus (arts. 405 a 420 CPP PBA) | Ley 23.098 es referencia federal; en PBA rige el CPP. |
| Código vigente en federal con asiento en PBA (13/11/2026) | — | CPPF en MDP, Bahía Blanca, San Nicolás/Rosario y La Plata (desde 21/09/2026). San Martín: CPPN hasta implementación. |
"""
