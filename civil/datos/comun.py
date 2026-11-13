import datos

ROLES = datos.ROLES
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS

_DESCRIPCION_TIPO = {
    "HABILES_JUDICIALES": "Días hábiles judiciales (calendario judicial PBA; las ferias no se cuentan). Admite gracia.",
    "CORRIDOS": "Días corridos, como los plazos de fondo del CCyC (art. 6). Si el último día es inhábil, se puede "
                "cumplir el hábil siguiente (regla R2). Admite gracia.",
    "HABILES_ADMINISTRATIVOS": "Días hábiles administrativos: lunes a viernes sin feriados; las ferias judiciales no "
                               "suspenden (regla R6). Sin gracia.",
    "MESES": "Meses, de fecha a fecha (regla R7). Admite gracia.",
    "ANIOS": "Años, de fecha a fecha, como la prescripción (regla R7). Admite gracia.",
    "HORAS": "Horas corridas desde la fecha y hora del disparador (regla R8). Sin gracia.",
    "FECHA_FIJADA": "Acto con fecha y hora fijadas, como una audiencia (valor 0). El abogado carga la fecha y la hora. "
                    "Sin gracia.",
    "ANTICIPACION_HABILES_JUDICIALES": "Días hábiles judiciales contados hacia atrás desde un acto fijado (regla R9). "
                                       "Sin gracia.",
    "SIN_PLAZO": "Sin plazo perentorio (valor 0). Depende del juzgado, de un organismo o de la parte; si el plazo lo "
                 "fija el juez, el abogado lo carga como plazo suelto. Sin gracia.",
}


def plazo_tipos(usos):
    """Tipos de plazo de la app (mismo orden que datos.py) con el uso propio del flujo. `usos` asigna a cada tipo un
    ejemplo del flujo; el tipo que no figura se marca como no usado."""
    desconocidos = set(usos) - set(_DESCRIPCION_TIPO)
    if desconocidos:
        raise ValueError(f"Tipos de plazo inexistentes: {desconocidos}")
    return [(t, f"{_DESCRIPCION_TIPO[t]} {usos.get(t, 'Este flujo no lo usa.')}") for t, _ in datos.PLAZO_TIPOS]


FASES_COMUNES = ["Previa", "Postulación", "Prueba", "Sentencia", "Recursos", "Ejecución", "Acuerdo", "Cierre"]

GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Prueba", ["Prueba"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Ejecución", ["Ejecución"]),
    ("Acuerdo", ["Acuerdo"]),
    ("Cierre", ["Cierre"]),
]

LEYENDA_ROLES = "celeste = Actora; naranja = Demandada; gris = Tribunal u organismo; violeta = Cualquiera de las partes."

DUDA_ETAPA_COMUN = (
    "Etapa común",
    "La etapa judicial común (demanda, prueba, sentencia, recursos, ejecución, acuerdo y caducidad) sale de "
    "civil/datos/comun.py. Sus dudas se responden una sola vez en matriz_civil_danos_y_perjuicios_pba.xlsx (temas que "
    "empiezan con 'Etapa común') y las reglas del motor (D26 a D34), en matriz_flujo_laboral_pba_ley_11653.xlsx. "
    "¿Valen sin cambios para esta matriz?",
    "Todos",
)

DUDA_MOTOR = (
    "Reglas del motor",
    "Las reglas del motor de plazos (D26 a D34: gracia, hora límite, notificación electrónica, meses y años, horas, "
    "anticipación) se responden una sola vez en matriz_flujo_laboral_pba_ley_11653.xlsx. ¿Valen sin cambios para el "
    "fuero civil? Las diferencias propias del civil (ferias en la caducidad, plazos corridos de fondo) tienen sus "
    "propias dudas.",
    "Todos",
)

DUDA_PRODUCTO = (
    "Producto",
    "Las dudas técnicas de producto del fuero civil (roles propios, rol representado, hitos prejudiciales, catálogos de "
    "regímenes y de juzgados, límite FIN_DEL_DIA y caminos que vuelven a un hito anterior) se registran en "
    "matriz_civil_sucesorio_pba.xlsx. ¿Alguna cambia la carga de esta matriz?",
    "Todos",
)

CAMPOS = {"nombre": 2, "rol": 3, "evento": 4, "valor": 5, "tipo": 6, "gracia": 7, "base": 8,
          "checklist": 11, "documentacion": 12}

_PROCESOS = {
    "ordinario": "juicio ordinario (art. 319 CPCCBA)",
    "sumario": "juicio sumario (art. 320 CPCCBA)",
}


def flujo(nombre, regimen, notas):
    return {
        "Flujo": nombre,
        "Jurisdicción": "PBA",
        "Fuero": "Civil y Comercial",
        "Régimen procesal": regimen,
        "Versión": "1 (borrador)",
        "Fecha del borrador": "13/11/2026",
        "Validado por (equipo legal)": "",
        "Fecha de validación": "",
        "Notas": notas,
    }


def _nodos_comunes(P, proceso):
    o = proceso == "ordinario"
    contestar = 15 if o else 10
    agravios = 10 if o else 5
    caducidad = 6 if o else 3
    art_traslado = "Arts. 337, 338 y 354 CPCCBA" if o else "Arts. 484 y 486 CPCCBA"
    oferta = ("Acompañar la documental; el resto de la prueba se ofrece dentro de los primeros 10 días del plazo de "
              "prueba (art. 365)") if o else "Ofrecer toda la prueba con la demanda (art. 484)"
    nodos = [
        (f"{P}_300", "Postulación", "Presentación de la demanda", "ACTORA",
         "Decisión de demandar: cierre de la etapa previa", 0, "SIN_PLAZO", "NO",
         "Arts. 330 y 332 CPCCBA; tasa de justicia (Código Fiscal PBA y Ley Impositiva vigente); Leyes 6716 y 8480",
         "NO", "NO",
         [f"Verificar el tipo de proceso: este flujo usa el {_PROCESOS[proceso]}",
          "Verificar la competencia: juzgado Civil y Comercial o Juzgado de Paz Letrado (art. 61 Ley 5827)",
          "Acompañar el acta de cierre de la mediación prejudicial cuando sea obligatoria (Ley 13.951)",
          "Pagar la tasa de justicia y la contribución del 5 % sobre la tasa (sobretasa, art. 12 inc. g Ley 6716) al "
          "iniciar, sobre el monto reclamado (alícuota de la Ley Impositiva vigente, a verificar)",
          "Pagar el bono de derecho fijo de la Ley 8480 y el anticipo previsional de la Ley 6716 (monto, a verificar)",
          "Si el cliente no puede afrontar los gastos, pedir el beneficio de litigar sin gastos (arts. 78 a 86)",
          oferta,
          "Pedir las medidas cautelares que hagan falta (arts. 195 y siguientes)",
          "Constituir domicilio electrónico"],
         ["Escrito de demanda", "Poder o acta poder", "Acta de cierre de la mediación (si corresponde)",
          "Comprobantes de tasa de justicia, contribución, bono Ley 8480 y anticipo Ley 6716", "Prueba documental"]),
        (f"{P}_310", "Postulación", "Beneficio de litigar sin gastos", "ACTORA",
         "Presentación del pedido de beneficio", 0, "SIN_PLAZO", "NO",
         "Arts. 78 a 86 CPCCBA", "NO", "NO",
         ["Ofrecer la prueba de la falta de recursos (testigos, informes) al pedirlo",
          "Mientras se tramita, el beneficio provisional cubre la tasa de justicia y los aportes iniciales (art. 83)",
          "Notificar a la contraria y al organismo fiscal según lo que ordene el juzgado (a verificar)",
          "El beneficio concedido también exime del depósito previo del recurso extraordinario (art. 280)"],
         ["Escrito de beneficio", "Declaración de testigos o información sumaria"]),
        (f"{P}_320", "Postulación", "Medidas cautelares", "ACTORA",
         "Presentación del pedido de medida cautelar", 0, "SIN_PLAZO", "NO",
         "Arts. 195, 207, 209, 212, 229, 230 y 231 CPCCBA", "NO", "NO",
         ["Elegir la medida: embargo preventivo, anotación de litis, prohibición de innovar o de contratar, inhibición",
          "Ofrecer la contracautela que fije el juez",
          "Diligenciar los oficios o el mandamiento de traba y controlar la inscripción en el registro",
          "Si la cautelar se trabó antes de la demanda, presentarla dentro de los 10 días de la traba o la medida "
          "caduca de pleno derecho (art. 207; prohibición de contratar: 5 días, art. 231)",
          "Embargos e inhibiciones caducan a los 5 años de su anotación: pedir la reinscripción antes (art. 207)"],
         ["Escrito de medida cautelar", "Contracautela", "Oficios o mandamiento"]),
        (f"{P}_330", "Postulación", "Radicación, control de admisibilidad y traslado de la demanda", "TRIBUNAL",
         "Presentación de la demanda", 0, "SIN_PLAZO", "NO",
         "Arts. 336, 337 y 338 CPCCBA" if o else "Arts. 336, 338 y 484 CPCCBA", "NO", "NO",
         ["Si el juzgado manda subsanar defectos, cargar como plazo suelto el que fije la providencia",
          "Confeccionar y diligenciar la cédula de traslado al domicilio real del demandado (art. 338)",
          "Domicilio fuera del asiento del juzgado: el plazo se amplía 1 día cada 200 km (art. 158); fuera de la "
          "provincia, cédula por la Ley 22.172 (a verificar)",
          "Demandado incierto o con domicilio ignorado: edictos por 2 días y defensor oficial (arts. 145 y 341)"],
         ["Cédula de traslado con copias de la demanda y la documental"]),
        (f"{P}_340", "Postulación", "Contestación de la demanda", "DEMANDADA",
         "Notificación de la cédula de traslado de la demanda", contestar, "HABILES_JUDICIALES", "SI",
         art_traslado, "NO", "NO",
         ["Reconocer o negar cada hecho y la autenticidad de cada documento (art. 354)",
          "Oponer la prescripción si corresponde",
          "Ofrecer la prueba" + ("" if o else ": en el sumario, toda con la contestación (art. 484)"),
          ("Las excepciones previas se oponen aparte, dentro de los primeros 10 días (art. 344)" if o else
           "Las excepciones previas se oponen junto con la contestación (art. 486)"),
          "Reconvenir, si corresponde, en el mismo escrito (art. 355" + (")" if o else " y 485)"),
          "Pedir la citación de terceros, si corresponde (art. 94)",
          "Si no comparece, la actora pide la rebeldía (art. 59): la sentencia se dicta según el mérito de la causa y, "
          "en caso de duda, se presumen ciertos los hechos lícitos afirmados (art. 60)"],
         ["Escrito de contestación", "Poder", "Prueba documental"]),
    ]
    if o:
        nodos.append(
            (f"{P}_350", "Postulación", "Excepciones de previo y especial pronunciamiento", "DEMANDADA",
             "Notificación de la cédula de traslado de la demanda", 10, "HABILES_JUDICIALES", "SI",
             "Arts. 344, 345 y 348 CPCCBA", "NO", "NO",
             ["Oponer todas en un solo escrito, con la prueba instrumental y el ofrecimiento de la restante (art. 348)",
              "Si se oponen excepciones, oponer también la prescripción (art. 344)",
              "La oposición no suspende el plazo para contestar la demanda (art. 344)"],
             ["Escrito de excepciones previas"]))
    nodos += [
        (f"{P}_355", "Postulación", "Traslado a la actora de las excepciones previas", "ACTORA",
         "Notificación del traslado de las excepciones", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 150 y 348 CPCCBA", "NO", "NO",
         ["Contestar, acompañar la prueba instrumental y ofrecer la restante (art. 348)",
          "Si se admite una excepción subsanable (por ejemplo, defecto legal), subsanar en el plazo que fije el juez"],
         ["Escrito de contestación de excepciones"]),
        (f"{P}_360", "Postulación", "Traslado a la actora de la documental de la contestación", "ACTORA",
         "Notificación del traslado de la documental acompañada con la contestación", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 150 y 356 CPCCBA" + ("" if o else "; art. 484"), "NO", "NO",
         ["Reconocer o desconocer los documentos atribuidos al cliente",
          "Ofrecer prueba sobre hechos nuevos alegados en la contestación"],
         ["Escrito de contestación del traslado"]),
        (f"{P}_370", "Postulación", "Contestación de la reconvención", "ACTORA",
         "Notificación del traslado de la reconvención", contestar, "HABILES_JUDICIALES", "SI",
         "Arts. 355 y 356 CPCCBA" if o else "Art. 485 CPCCBA", "NO", "NO",
         ["Contestar con las mismas cargas que la contestación de la demanda (art. 354)",
          "Ofrecer la prueba de la reconvención"],
         ["Escrito de contestación de la reconvención"]),
        (f"{P}_400", "Prueba", "Apertura a prueba, audiencia preliminar o declaración de puro derecho", "TRIBUNAL",
         "Cierre de la etapa de postulación", 0, "SIN_PLAZO", "NO",
         "Arts. 357, 358, 359 y 365 CPCCBA; Res. SCBA 2761/16 (programa de oralidad civil)", "NO", "NO",
         ["El plazo de prueba lo fija el juez (hasta 40 días, art. 365): cargarlo como plazo suelto",
          "En los juzgados del programa de oralidad, la prueba se ordena en la audiencia preliminar",
          "Si la causa se declara de puro derecho, se pasa a sentencia (art. 357)"],
         []),
        (f"{P}_405", "Prueba", "Reposición u oposición contra la providencia de prueba", "AMBAS",
         "Notificación de la providencia de prueba", 3, "HABILES_JUDICIALES", "SI",
         "Arts. 238, 239 y 359 CPCCBA", "NO", "NO",
         ["Reposición: 3 días (art. 239)", "Oposición a la apertura a prueba: 5 días (art. 359); editar si es el caso",
          "Las resoluciones sobre prueba no son apelables salvo las excepciones del código (art. 377, a verificar)"],
         ["Escrito de reposición u oposición"]),
    ]
    if o:
        nodos.append(
            (f"{P}_410", "Prueba", "Ofrecimiento de prueba", "AMBAS",
             "Notificación del auto de apertura a prueba", 10, "HABILES_JUDICIALES", "SI",
             "Art. 365 CPCCBA", "NO", "NO",
             ["Ofrecer pericial (con los puntos de pericia), testimonial, informativa y confesional",
              "Pedir la fijación de las audiencias dentro del plazo de prueba (art. 366)",
              "Prueba en el extranjero: plazo extraordinario (art. 367)"],
             ["Escrito de ofrecimiento de prueba", "Pliego de posiciones", "Lista de testigos"]))
    nodos += [
        (f"{P}_415", "Prueba", "Audiencia preliminar", "AMBAS",
         "Fecha y hora de la audiencia fijada por el juzgado", 0, "FECHA_FIJADA", "NO",
         "Res. SCBA 2761/16 (programa de oralidad civil); art. 36 CPCCBA (a verificar)", "NO", "NO",
         ["Concurrir con el cliente: el juez intenta la conciliación",
          "Fijar los hechos controvertidos y depurar la prueba innecesaria",
          "Llevar el plan de producción de la prueba; el juez fija la audiencia de vista de causa"],
         ["Propuesta de acuerdo, si la hay"]),
        (f"{P}_420", "Prueba", "Dictamen pericial", "TRIBUNAL",
         ("Aceptación del cargo por el perito" if o else "Fecha de la audiencia de prueba"),
         30 if o else 5, "HABILES_JUDICIALES" if o else "ANTICIPACION_HABILES_JUDICIALES", "NO",
         "Art. 459 CPCCBA" if o else "Art. 492 CPCCBA", "NO", "NO",
         (["Controlar la designación del perito, los puntos de pericia y el anticipo de gastos",
           "Si el juez no fijó plazo, el perito tiene 30 días (art. 459); editar si fijó otro",
           "Designar consultor técnico de parte, si conviene"] if o else
          ["En el sumario el juez designa perito único de oficio (art. 492)",
           "El dictamen debe presentarse 5 días antes de la audiencia de prueba (art. 492)",
           "Recusación del perito: hasta el día siguiente al de su nombramiento (art. 492)"]),
         ["Puntos de pericia", "Comprobante del anticipo de gastos"]),
        (f"{P}_425", "Prueba", "Traslado del dictamen pericial", "AMBAS",
         "Notificación por cédula del traslado del dictamen", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 150 y 473 CPCCBA", "NO", "NO",
         ["Observar o impugnar el dictamen, o pedir explicaciones (art. 473)",
          "Si el juez fija audiencia de explicaciones, cargarla como fecha fijada"],
         ["Escrito de observaciones o impugnación", "Informe del consultor técnico"]),
        (f"{P}_430", "Prueba", "Prueba informativa: contestación de los oficios", "TRIBUNAL",
         "Recepción del oficio por la oficina pública o la entidad privada", 10, "HABILES_JUDICIALES", "NO",
         "Art. 396 CPCCBA", "NO", "NO",
         ["Confeccionar y diligenciar los oficios ordenados",
          "Plazo para contestar: 20 días hábiles las oficinas públicas y 10 las entidades privadas (art. 396); "
          "por defecto se usa 10, editar si es una oficina pública"],
         ["Oficios con constancia de recepción"]),
        (f"{P}_435", "Prueba", "Pedido de reiteración del oficio no contestado", "AMBAS",
         "Vencimiento del plazo de contestación del informe", 5, "HABILES_JUDICIALES", "SI",
         "Art. 400 CPCCBA", "NO", "NO",
         ["Si no se pide la reiteración en 5 días, se tiene por desistida la prueba (art. 400)"],
         ["Escrito de reiteración"]),
        (f"{P}_440", "Prueba", "Audiencia de prueba o de vista de causa", "AMBAS",
         "Fecha y hora de la audiencia fijada por el juzgado", 0, "FECHA_FIJADA", "NO",
         "Arts. 366, 429 y 430 CPCCBA; Res. SCBA 2761/16", "NO", "NO",
         ["Citar a los testigos con la anticipación que fije el juzgado y evitar la caducidad de la prueba "
          "testimonial (art. 430)",
          "Absolución de posiciones: presentar el pliego antes de la audiencia",
          "Si la audiencia se reprograma, editar la fecha"],
         ["Pliego de posiciones", "Cédulas de citación a testigos"]),
        (f"{P}_450", "Prueba", "Alegatos", "AMBAS",
         "Notificación de la providencia que pone los autos para alegar", 6, "HABILES_JUDICIALES", "SI",
         "Art. 480 CPCCBA" + ("" if o else "; en el sumario, a verificar (art. 495)"), "NO", "NO",
         ["Alegar sobre el mérito de la prueba", "Vencido el plazo, se llama autos para sentencia (art. 481)"],
         ["Alegato"]),
        (f"{P}_500", "Sentencia", "Llamamiento de autos y sentencia definitiva", "TRIBUNAL",
         "Providencia de llamamiento de autos firme", 0, "SIN_PLAZO", "NO",
         "Arts. 481 y 482 CPCCBA; plazo del art. 34 inc. 3 c" if o else "Arts. 481, 482 y 494 CPCCBA (30 o 50 días)",
         "NO", "NO",
         ["Desde el llamamiento de autos no se presentan más escritos ni pruebas (art. 482)",
          "Si se demora la sentencia, evaluar el pedido de pronto despacho"],
         []),
        (f"{P}_505", "Sentencia", "Aclaratoria", "AMBAS",
         "Notificación de la sentencia", 3, "HABILES_JUDICIALES", "SI",
         "Art. 166 inc. 2 CPCCBA", "NO", "NO",
         ["Pedir que se corrija un error material o se supla una omisión", "No suspende el plazo de apelación"],
         ["Escrito de aclaratoria"]),
        (f"{P}_510", "Sentencia", "Apelación de la regulación de honorarios", "AMBAS",
         "Notificación de la regulación de honorarios (personal o por cédula, art. 54 Ley 14.967)", 5,
         "HABILES_JUDICIALES", "SI",
         "Arts. 54 y 57 Ley 14.967", "NO", "NO",
         ["La apelación se funda en el mismo escrito (art. 57)",
          "No hay recurso si reguló la Cámara, un tribunal de instancia única o la SCBA (art. 57)",
          "Controlar la base regulatoria y el valor del Jus a la fecha"],
         ["Escrito de apelación fundada"]),
        (f"{P}_515", "Sentencia", "Pago de los honorarios firmes", "AMBAS",
         "Notificación de la regulación firme", 10, "HABILES_JUDICIALES", "NO",
         "Art. 54 Ley 14.967; Ley 6716 (aportes)", "NO", "NO",
         ["Paga quien fue condenado en costas", "Depositar con los aportes de la Ley 6716 y el IVA si corresponde",
          "Si no se pagan, ejecutarlos (arts. 497 y siguientes CPCCBA)"],
         ["Comprobante de depósito judicial", "Boleta de aportes Ley 6716"]),
        (f"{P}_600", "Recursos", "Recurso de apelación contra la sentencia definitiva", "AMBAS",
         "Notificación de la sentencia definitiva", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 242 a 245 CPCCBA", "NO", "NO",
         ["Solo interponer el recurso, sin fundarlo (art. 245)",
          "Contra la sentencia definitiva se concede libremente y con efecto suspensivo (art. 243)"],
         ["Escrito de apelación"]),
        (f"{P}_610", "Recursos", "Expresión de agravios", "AMBAS",
         "Notificación de la providencia que pone el expediente en la oficina de la Cámara", agravios,
         "HABILES_JUDICIALES", "SI",
         "Arts. 254, 260 y 261 CPCCBA" + ("" if o else "; art. 269"), "NO", "NO",
         ["Criticar en forma concreta y razonada la sentencia (art. 260)",
          "Si no se expresan agravios en término, el recurso se declara desierto (art. 261)"],
         ["Escrito de expresión de agravios"]),
        (f"{P}_615", "Recursos", "Contestación de la expresión de agravios", "AMBAS",
         "Notificación del traslado de la expresión de agravios", agravios, "HABILES_JUDICIALES", "SI",
         "Art. 260 CPCCBA", "NO", "NO",
         ["Responder cada agravio"],
         ["Escrito de contestación de agravios"]),
        (f"{P}_620", "Recursos", "Sentencia o resolución de la Cámara", "TRIBUNAL",
         "Presentación de los escritos de agravios y memoriales, o vencimiento de sus plazos", 0, "SIN_PLAZO", "NO",
         "Arts. 254 a 269 CPCCBA", "NO", "NO",
         ["La Cámara confirma, revoca o modifica; también declara desierto el recurso (art. 261)",
          "La nueva regulación de honorarios de la Cámara no es apelable (art. 57 Ley 14.967)"],
         []),
        (f"{P}_630", "Recursos", "Recursos extraordinarios ante la SCBA", "AMBAS",
         "Notificación de la sentencia definitiva de la Cámara", 10, "HABILES_JUDICIALES", "SI",
         "Arts. 278 a 280, 296, 297, 299 y 300 CPCCBA", "NO", "NO",
         ["Elegir el recurso: inaplicabilidad de ley o doctrina legal, nulidad o inconstitucionalidad",
          "Inaplicabilidad: valor mínimo del agravio (art. 278, a verificar el monto en Jus)",
          "Depósito previo del 10 % del valor del litigio, con un mínimo de 100 Jus y un máximo de 500 Jus, salvo "
          "beneficio de litigar sin gastos (art. 280)",
          "Constituir domicilio en La Plata (art. 280)"],
         ["Escrito del recurso", "Comprobante del depósito previo"]),
        (f"{P}_640", "Recursos", "Queja ante la SCBA por recurso denegado", "AMBAS",
         "Notificación de la denegatoria del recurso extraordinario", 5, "HABILES_JUDICIALES", "SI",
         "Art. 292 CPCCBA", "NO", "NO",
         ["Acompañar las copias que exige el código"],
         ["Escrito de queja", "Copias de la sentencia, del recurso y de la denegatoria"]),
        (f"{P}_645", "Recursos", "Trámite y sentencia de la SCBA", "AMBAS",
         "Notificación de la providencia de autos de la SCBA", 10, "HABILES_JUDICIALES", "SI",
         "Art. 284 CPCCBA", "NO", "NO",
         ["Presentar memorial sobre el recurso propio o el de la contraria, si conviene (art. 284)",
          "No se ofrecen pruebas ni se alegan hechos nuevos (art. 284)"],
         ["Memorial"]),
        (f"{P}_650", "Recursos", "Memorial del recurso concedido en relación", "AMBAS",
         "Notificación de la concesión del recurso en relación", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 243 y 246 CPCCBA", "NO", "NO",
         ["Se usa para apelar resoluciones que no son la sentencia definitiva (por ejemplo, una excepción admitida, "
          "una cautelar o el beneficio de litigar sin gastos)",
          "Primero se apela en 5 días (art. 244); concedido el recurso, el memorial va en 5 días (art. 246)"],
         ["Memorial"]),
        (f"{P}_700", "Ejecución", "Liquidación", "ACTORA",
         "Notificación de la providencia que tiene por firme la sentencia o manda practicar liquidación", 10,
         "HABILES_JUDICIALES", "SI",
         "Art. 501 CPCCBA", "NO", "NO",
         ["Practicar la liquidación de capital, intereses y costas (art. 501)",
          "Si la vencedora no la presenta, puede hacerlo la vencida",
          "Aplicar la tasa de interés de la sentencia"],
         ["Planilla de liquidación"]),
        (f"{P}_705", "Ejecución", "Traslado de la liquidación", "DEMANDADA",
         "Notificación de la vista de la liquidación", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 501 y 502 CPCCBA", "NO", "NO",
         ["Conformidad o silencio: se ejecuta por la suma que resulte (art. 502)",
          "Impugnación: se tramita como incidente (art. 502)",
          "Aprobada la liquidación, la condenada paga en el plazo de la sentencia: cargarlo como plazo suelto"],
         ["Escrito de conformidad o impugnación"]),
        (f"{P}_710", "Ejecución", "Embargo y citación de venta", "ACTORA",
         "Vencimiento del plazo de pago sin depósito", 0, "SIN_PLAZO", "NO",
         "Arts. 497, 500 y 503 CPCCBA", "NO", "NO",
         ["Pedir el embargo de cuentas, sueldos, inmuebles o automotores",
          "Diligenciar oficios y mandamientos de embargo",
          "Trabado el embargo, citar al deudor de venta (art. 503)",
          "Si hay que subastar, seguir las reglas de la subasta (arts. 558 y siguientes)"],
         ["Mandamiento de embargo", "Oficios a bancos y registros", "Cédula de citación de venta"]),
        (f"{P}_720", "Ejecución", "Excepciones del ejecutado", "DEMANDADA",
         "Notificación de la citación de venta", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 503 a 505 y 507 CPCCBA", "NO", "NO",
         ["Solo se admiten falsedad o prescripción de la ejecutoria, pago, quita, espera o remisión (art. 504)",
          "Deben fundarse en hechos posteriores a la sentencia y probarse con documentos (art. 505)"],
         ["Escrito de excepciones"]),
        (f"{P}_730", "Ejecución", "Cobro y rendición al cliente", "ACTORA",
         "Existencia de fondos depositados en la cuenta judicial", 0, "SIN_PLAZO", "NO",
         "Ley 6716 (aportes)", "NO", "NO",
         ["Pedir el libramiento del giro o la transferencia",
          "Retener honorarios pactados y aportes según el convenio",
          "Rendir cuentas al cliente"],
         ["Orden de transferencia", "Recibo o rendición de cuentas al cliente"]),
        (f"{P}_800", "Acuerdo", "Acuerdo, transacción o conciliación y homologación", "AMBAS",
         "Firma del acuerdo entre las partes", 0, "SIN_PLAZO", "NO",
         "Arts. 308 y 309 CPCCBA; arts. 1641 y siguientes CCyC", "NO", "NO",
         ["Presentar el acuerdo para su homologación",
          "Si el acuerdo se firmó en la mediación prejudicial, su homologación sigue el art. 19 Ley 13.951",
          "Prever costas, honorarios, tasa de justicia sobre el monto del acuerdo y aportes de la Ley 6716"],
         ["Convenio firmado", "Escrito de homologación"]),
        (f"{P}_805", "Acuerdo", "Cumplimiento del acuerdo homologado", "DEMANDADA",
         "Notificación de la homologación", 0, "SIN_PLAZO", "NO",
         "Plazos pactados en el acuerdo", "NO", "NO",
         ["Cargar como plazos sueltos las cuotas o vencimientos pactados",
          "Si se incumple, se ejecuta como sentencia (arts. 497 y siguientes CPCCBA)"],
         []),
        (f"{P}_900", "Cierre", "Control de la caducidad de instancia", "ACTORA",
         "Último acto de impulso procesal útil", caducidad, "MESES", "NO",
         "Arts. 310, 311, 315 y 316 CPCCBA", "NO", "NO",
         [f"Caduca la instancia sin actos de impulso durante {caducidad} meses "
          f"({'primera instancia' if o else 'sumario, sumarísimo o segunda instancia'}, art. 310)",
          "Cada acto de impulso reinicia el cómputo: editar la fecha de inicio",
          "Las ferias no se cuentan (art. 311): la app cuenta meses de fecha a fecha, así que alerta antes"],
         []),
        (f"{P}_905", "Cierre", "Intimación a activar el proceso", "ACTORA",
         "Notificación de la intimación previa a la declaración de caducidad", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 315 y 316 CPCCBA", "NO", "NO",
         ["Manifestar la intención de continuar y producir actividad útil (art. 315)",
          "Si después de activar vuelve a pasar igual plazo sin actividad, se decreta la caducidad"],
         ["Escrito de impulso"]),
        (f"{P}_990", "Cierre", "Archivo del expediente", "AMBAS",
         "Finalización del proceso", 0, "SIN_PLAZO", "NO",
         "—", "NO", "SI",
         ["Controlar que no queden tasas, aportes ni honorarios pendientes", "Pedir el desglose de documentación"],
         []),
    ]
    return nodos


def _transiciones_comunes(P, proceso):
    o = proceso == "ordinario"
    t = [
        ("300", "Demanda presentada", "330"),
        ("300", "Demanda presentada", "900"),
        ("300", "Demanda presentada con pedido de beneficio de litigar sin gastos", "330"),
        ("300", "Demanda presentada con pedido de beneficio de litigar sin gastos", "310"),
        ("300", "Demanda presentada con pedido de beneficio de litigar sin gastos", "900"),
        ("300", "Demanda presentada con pedido de medida cautelar", "330"),
        ("300", "Demanda presentada con pedido de medida cautelar", "320"),
        ("300", "Demanda presentada con pedido de medida cautelar", "900"),
        ("310", "Beneficio concedido, o denegado sin recurso (se integran tasa y aportes)", ""),
        ("310", "Beneficio denegado: se apela", "650"),
        ("320", "Medida trabada o denegada sin recurso", ""),
        ("320", "Medida denegada o trabada: se apela", "650"),
        ("330", "Demanda rechazada in limine o no subsanada", "990"),
        ("330", "Se ordena el traslado de la demanda", "340"),
    ]
    if o:
        t.append(("330", "Se ordena el traslado de la demanda", "350"))
        t += [
            ("340", "Contesta la demanda", "360"),
            ("340", "Contesta y reconviene", "360"),
            ("340", "Contesta y reconviene", "370"),
            ("340", "No contesta en término", "400"),
            ("350", "Se oponen excepciones previas", "355"),
            ("350", "No se oponen excepciones previas", ""),
        ]
    else:
        t += [
            ("340", "Contesta la demanda", "360"),
            ("340", "Contesta y opone excepciones previas", "360"),
            ("340", "Contesta y opone excepciones previas", "355"),
            ("340", "Contesta y reconviene", "360"),
            ("340", "Contesta y reconviene", "370"),
            ("340", "No contesta en término", "400"),
        ]
    t += [
        ("355", "Excepciones rechazadas o diferidas para la sentencia", ""),
        ("355", "Excepción admitida que pone fin al proceso: se apela", "650"),
        ("355", "Excepción admitida y consentida", "990"),
        ("360", "Traslado contestado o plazo vencido", "400"),
        ("370", "Reconvención contestada o plazo vencido", ""),
    ]
    prueba = ["420", "430", "440"]
    if o:
        t += [("400", "Se abre a prueba", "405"), ("400", "Se abre a prueba", "410")]
        t += [("410", "Prueba ofrecida: se fija audiencia preliminar", "415")]
        t += [("410", "Prueba ofrecida y proveída sin audiencia preliminar", d) for d in prueba]
    else:
        t += [("400", "Se provee la prueba ofrecida", d) for d in ["405"] + prueba]
        t += [("400", "Se fija audiencia preliminar", "415")]
    t += [
        ("400", "Causa declarada de puro derecho", "500"),
        ("405", "Resuelta o plazo vencido", ""),
        ("415", "Acuerdo conciliatorio en la audiencia", "800"),
    ]
    t += [("415", "Se provee la prueba y se fija la audiencia de vista de causa", d) for d in ["405"] + prueba]
    t += [
        ("415", "Causa declarada de puro derecho", "500"),
        ("420", "Dictamen presentado", "425"),
        ("420", "Pericia no ofrecida o desistida", ""),
        ("425", "Observaciones presentadas o plazo vencido", ""),
        ("430", "Informes contestados o prueba desistida", ""),
        ("430", "Plazo vencido sin respuesta", "435"),
        ("435", "Reiteración pedida", "430"),
        ("435", "No se pide: prueba desistida", ""),
        ("440", "Audiencia realizada y prueba producida", "450"),
        ("440", "Acuerdo conciliatorio en la audiencia", "800"),
        ("450", "Alegatos presentados o plazo vencido", "500"),
        ("500", "Sentencia notificada", "505"),
        ("500", "Sentencia notificada", "510"),
        ("500", "Sentencia notificada", "600"),
        ("505", "Aclaratoria resuelta o plazo vencido", ""),
        ("510", "Regulación firme", "515"),
        ("515", "Honorarios pagados o en ejecución", ""),
        ("600", "No se recurre: queda firme y hace lugar a la demanda", "700"),
        ("600", "No se recurre: queda firme y rechaza la demanda", "990"),
        ("600", "Se interpone apelación", "610"),
        ("610", "Agravios presentados", "615"),
        ("610", "No expresa agravios: deserción", "620"),
        ("615", "Contestados o plazo vencido", "620"),
        ("620", "Sentencia de Cámara firme que hace lugar a la demanda", "700"),
        ("620", "Sentencia de Cámara firme que rechaza la demanda", "990"),
        ("620", "Cámara resuelve la apelación de una resolución interlocutoria: sigue el trámite", ""),
        ("620", "Se interponen recursos extraordinarios", "630"),
        ("630", "Recurso concedido", "645"),
        ("630", "Recurso denegado", "640"),
        ("640", "Queja admitida", "645"),
        ("640", "Queja rechazada: queda firme una sentencia que hace lugar a la demanda", "700"),
        ("640", "Queja rechazada: queda firme una sentencia que rechaza la demanda", "990"),
        ("645", "La SCBA resuelve: queda firme una sentencia que hace lugar a la demanda", "700"),
        ("645", "La SCBA resuelve: queda firme una sentencia que rechaza la demanda", "990"),
        ("645", "La SCBA anula y reenvía para nuevo pronunciamiento", "620"),
        ("650", "Memorial presentado o plazo vencido", "620"),
        ("700", "Liquidación presentada", "705"),
        ("705", "Liquidación aprobada y pagada en término", "730"),
        ("705", "Liquidación aprobada y no pagada", "710"),
        ("710", "Embargo trabado y citación de venta notificada", "720"),
        ("720", "Sin excepciones o excepciones rechazadas: fondos embargados o bienes subastados", "730"),
        ("720", "Excepción de pago admitida", "990"),
        ("730", "Cobro percibido y rendido al cliente", "990"),
        ("800", "Acuerdo homologado", "805"),
        ("800", "Acuerdo homologado", "510"),
        ("805", "Acuerdo cumplido", "990"),
        ("805", "Acuerdo incumplido: se ejecuta", "710"),
        ("900", "Proceso terminado antes del vencimiento", ""),
        ("900", "Plazo vencido: se intima a activar el proceso", "905"),
        ("905", "Proceso activado en término", ""),
        ("905", "No se activa: se decreta la caducidad", "990"),
    ]
    return [(f"{P}_{a}", c, f"{P}_{b}" if b else "") for a, c, b in t]


def etapa_judicial(prefijo, proceso, ajustes=None, agregar=None, quitar=(), redirigir=None, omitir=()):
    """Etapa judicial común del CPCCBA (demanda, prueba, sentencia, recursos, ejecución, acuerdo y caducidad).

    `proceso` es "ordinario" o "sumario" y cambia plazos e hitos. `ajustes` reemplaza campos por ID, por ejemplo
    {"DYP_300": {"nombre": "..."}}; `agregar` suma ítems al checklist de un hito ({"DYP_300": [...]}). `quitar` saca
    hitos que el flujo reemplaza por los propios; toda transición que llegaba a un hito quitado tiene que figurar en
    `redirigir` (ID quitado -> ID de destino, o "" para cerrar el camino). `omitir` saca salidas comunes, dadas como
    (hito de origen, condición), que el flujo reemplaza por las propias."""
    if proceso not in _PROCESOS:
        raise ValueError(f"Proceso desconocido: {proceso}")
    ajustes, agregar, quitar, redirigir = ajustes or {}, agregar or {}, set(quitar), redirigir or {}
    omitir = set(omitir)
    comunes = _transiciones_comunes(prefijo, proceso)
    faltantes = omitir - {(o, c) for o, c, _ in comunes}
    if faltantes:
        raise ValueError(f"Salidas a omitir inexistentes: {faltantes}")
    nodos = []
    for n in _nodos_comunes(prefijo, proceso):
        if n[0] in quitar:
            continue
        nodo = list(n)
        for campo, valor in ajustes.get(nodo[0], {}).items():
            nodo[CAMPOS[campo]] = valor
        nodo[CAMPOS["checklist"]] = nodo[CAMPOS["checklist"]] + agregar.get(nodo[0], [])
        nodos.append(tuple(nodo))
    ids = {n[0] for n in nodos}
    sobrantes = (set(ajustes) | set(agregar)) - ids
    if sobrantes:
        raise ValueError(f"Ajustes sobre hitos inexistentes: {sobrantes}")
    transiciones = []
    for o, c, d in comunes:
        if o in quitar or (o, c) in omitir:
            continue
        if d in quitar:
            if d not in redirigir:
                raise ValueError(f"La transición {o} -> {d} llega a un hito quitado sin destino nuevo")
            d = redirigir[d]
        if (o, c, d) not in transiciones:
            transiciones.append((o, c, d))
    return nodos, transiciones


def mediacion(prefijo, ids, demanda, acuerdo, optativa=False, reanudacion=True):
    """Mediación prejudicial de la Ley 13.951. `ids` son los cuatro IDs de los hitos (requerimiento, audiencia, plazo
    y reanudación de la prescripción); `demanda` y `acuerdo` son los hitos a los que lleva el cierre."""
    req, aud, plazo, rean = (f"{prefijo}_{i}" for i in ids)
    dias = 30 if optativa else 60
    nodos = [
        (req, "Previa", "Requerimiento de mediación prejudicial" + (" (optativa)" if optativa else " obligatoria"),
         "ACTORA", "Decisión de reclamar judicialmente", 0, "SIN_PLAZO", "NO",
         ("Arts. 2 y 5 Ley 13.951 (optativa para quien reclama en desalojos y ejecuciones)" if optativa else
          "Arts. 2 y 4 Ley 13.951"), "NO", "NO",
         ["Presentar el formulario de requerimiento y pagar lo que corresponda al inicio (reglamentación, a verificar)",
          "Se sortea el mediador",
          "La mediación suspende la prescripción (art. 2542 CCyC)"] +
         (["Es optativa para el reclamante, que puede demandar directamente; si la pide, el requerido está obligado "
           "a concurrir (art. 5)"] if optativa else
          ["Excluidas, entre otras: causas con el Estado, cautelares, diligencias preliminares y prueba anticipada, "
           "sucesiones, acciones de menores con intervención del Ministerio Público y causas ante Juzgados de Paz "
           "Letrados (art. 4 Ley 13.951)"]),
         ["Formulario de requerimiento", "DNI y poder", "Documentación del reclamo"]),
        (aud, "Previa", "Audiencia de mediación", "AMBAS",
         "Fecha y hora de la audiencia fijada por el mediador", 0, "FECHA_FIJADA", "NO",
         "Arts. 9, 10 y 13 Ley 13.951", "NO", "NO",
         ["El mediador fija la audiencia dentro de los 5 días de notificado, a no más de 45 días corridos de su "
          "designación (art. 9)",
          "Concurrir con el cliente (la asistencia es personal)", "Llevar una propuesta concreta y sus números",
          "Firmar el acta de cada audiencia"],
         ["Propuesta de acuerdo"]),
        (plazo, "Previa", "Plazo de la mediación", "TRIBUNAL",
         "Última notificación de la audiencia a la parte requerida", dias, "CORRIDOS", "NO",
         f"Art. 12 Ley 13.951 (hasta {dias} días corridos" + (" en desalojos y ejecuciones" if optativa else "") +
         ", prorrogables hasta 15)", "NO", "NO",
         ["El mediador conduce el trámite: el plazo es una alerta, no una carga de la parte",
          "Si las partes prorrogan de común acuerdo, editar el plazo (hasta 15 días más, art. 12)",
          "Vencido el plazo sin acuerdo se labra acta y queda expedita la vía judicial (art. 12)",
          "El acuerdo se homologa en el juzgado sorteado (arts. 19 y 20); si se incumple, se ejecuta y puede haber "
          "multa de hasta el 30 % de lo conciliado (art. 23)"],
         ["Acta de cierre"]),
    ]
    transiciones = [
        (req, "Mediador designado y audiencia fijada", aud),
        (req, "Mediador designado y audiencia fijada", plazo),
        (aud, "Audiencia realizada", ""),
        (plazo, "Acuerdo en la mediación", acuerdo),
        (plazo, "Cierre sin acuerdo o por incomparecencia", demanda),
    ]
    if reanudacion:
        nodos.append(
            (rean, "Previa", "Reanudación de la prescripción después de la mediación", "ACTORA",
             "Acta de cierre de la mediación a disposición de las partes", 20, "CORRIDOS", "NO",
             "Art. 2542 CCyC", "NO", "NO",
             ["La prescripción vuelve a correr 20 días después de que el acta de cierre está a disposición",
              "Recalcular el vencimiento de la prescripción sumando el tiempo que estuvo suspendida",
              "Demandar antes de ese vencimiento"],
             ["Acta de cierre"]))
        transiciones.append((plazo, "Cierre sin acuerdo o por incomparecencia", rean))
        transiciones.append((rean, "Demanda presentada", ""))
    return nodos, transiciones


def ordenar(nodos, transiciones):
    """Agrupa las transiciones por hito de origen, en el orden de NODOS, y deja juntas las filas de una misma
    condición (caminos en paralelo)."""
    posicion = {n[0]: i for i, n in enumerate(nodos)}
    primera = {}
    for i, (o, c, _) in enumerate(transiciones):
        primera.setdefault((o, c), i)
    vistas, salida = set(), []
    for i, t in sorted(enumerate(transiciones), key=lambda x: (posicion[x[1][0]], primera[x[1][0], x[1][1]], x[0])):
        if t not in vistas:
            vistas.add(t)
            salida.append(t)
    return salida


def dudas_etapa_comun(prefijo):
    """Dudas de la etapa judicial común. Van solo en la matriz de Daños y Perjuicios."""
    P = prefijo
    return [
        ("Etapa común: tipo de proceso",
         "Cada matriz usa un solo tipo de proceso (ordinario o sumario), que cambia plazos: contestación 15 o 10 días, "
         "agravios 10 o 5, caducidad 6 o 3 meses, y excepciones previas aparte o con la contestación. Si un caso del "
         "mismo tipo tramita por el otro proceso (por el monto, art. 320 inc. 1, o porque el juez lo decide), ¿se "
         "publica una segunda versión del flujo o el abogado edita los plazos? Propuesta: el abogado edita; se "
         "publica otra versión solo si el caso es frecuente.",
         f"{P}_340, {P}_610, {P}_615, {P}_900"),
        ("Etapa común: audiencia preliminar",
         "¿Qué juzgados civiles aplican el programa de oralidad (Res. SCBA 2761/16) con audiencia preliminar y "
         "audiencia de vista de causa? En el ordinario, ¿la prueba se ofrece antes de la audiencia preliminar "
         "(art. 365) o en ella? ¿Hay una norma del CPCCBA que la regule (art. 36, a verificar)?",
         f"{P}_400, {P}_410, {P}_415, {P}_440"),
        ("Etapa común: informes",
         "El plazo para contestar oficios es de 20 días hábiles para oficinas públicas y 10 para entidades privadas "
         "(art. 396). La app usa 10 por defecto porque de ese vencimiento depende el plazo de 5 días para pedir la "
         "reiteración (art. 400). ¿Es correcto o conviene separar el hito en dos?",
         f"{P}_430, {P}_435"),
        ("Etapa común: dictamen pericial",
         "En el ordinario, ¿los 30 días del perito (art. 459) son hábiles y corren desde la aceptación del cargo? "
         "En el sumario, el dictamen va 5 días antes de la audiencia (art. 492): ¿se modela bien como plazo hacia "
         "atrás (ANTICIPACION_HABILES_JUDICIALES)?",
         f"{P}_420"),
        ("Etapa común: alegatos en el sumario",
         "El art. 480 fija 6 días para alegar en el ordinario. ¿Hay alegatos en el juicio sumario (art. 495, normas "
         "supletorias)? Propuesta: dejar el hito con 6 días, porque es la opción que no pierde un vencimiento.",
         f"{P}_450"),
        ("Etapa común: caducidad de instancia",
         "El cómputo de la caducidad no cuenta las ferias (art. 311), pero el tipo MESES cuenta de fecha a fecha "
         "y la app alerta antes. ¿Es aceptable o hace falta un tipo de plazo que descuente las ferias? ¿Aplica el "
         "plazo de gracia al acto de impulso? Propuesta: sin gracia y sin descontar ferias (vencimiento más temprano).",
         f"{P}_900, {P}_905"),
        ("Etapa común: rebeldía",
         "Si la demandada no comparece, la actora pide la rebeldía (art. 59 CPCCBA), que se notifica por cédula o "
         "edictos, y el proceso sigue su curso (art. 60). La matriz no tiene un hito propio: 'No contesta en término' "
         "lleva a la apertura a prueba. ¿Alcanza o conviene un hito para el pedido y la notificación de la rebeldía?",
         f"{P}_340"),
        ("Etapa común: tasa de justicia y aportes",
         "Al iniciar se pagan la tasa de justicia, la contribución del 5 % (art. 12 inc. g Ley 6716), el bono de la "
         "Ley 8480 y el anticipo previsional de la Ley 6716. ¿Cuál es la alícuota vigente en 2026 (Ley Impositiva "
         "15.558, a verificar), qué pasa si se demanda por monto indeterminado y cuándo se integra el saldo (por "
         "ejemplo, con la sentencia o el acuerdo)? ¿Conviene un hito propio para la intimación a integrar la tasa?",
         f"{P}_300, {P}_800, {P}_990"),
        ("Etapa común: honorarios",
         "El pago de honorarios firmes va en 10 días (art. 54 Ley 14.967) y su apelación en 5 días, fundada "
         "(art. 57). ¿Los 10 días son hábiles judiciales? ¿Cuándo se depositan los aportes de la Ley 6716 y qué "
         "porcentaje (a verificar)?",
         f"{P}_510, {P}_515, {P}_730"),
        ("Etapa común: recursos extraordinarios",
         "¿Cuál es el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278) y el valor del "
         "Jus a la fecha, para calcular el depósito previo (art. 280)? El memorial ante la SCBA va en 10 días desde "
         "la providencia de autos (art. 284): ¿se notifica por cédula o queda notificada por nota?",
         f"{P}_630, {P}_645"),
        ("Etapa común: apelación de interlocutorias",
         "Para apelar una excepción admitida, una cautelar o el beneficio, la matriz usa un solo hito con el "
         "memorial de 5 días desde la concesión (art. 246); los 5 días para apelar (art. 244) quedan en el checklist. "
         "¿Conviene separarlos en dos hitos?",
         f"{P}_650"),
        ("Etapa común: cautelar antes de la demanda",
         "Si una medida cautelar se traba antes de demandar, la demanda debe presentarse dentro de los 10 días de la "
         "traba (art. 207; 5 días en la prohibición de contratar, art. 231) o la medida caduca de pleno derecho. "
         "Hoy queda en el checklist. ¿Se agrega un hito de 10 días hábiles en la etapa previa de cada flujo?",
         f"{P}_320"),
        ("Etapa común: plazos corridos y feria",
         "El civil usa muchos plazos corridos de fondo (CCyC art. 6: intimaciones, emplazamientos, mediación) que "
         "corren durante la feria, y algunos corridos procesales (por ejemplo, los 30 días de los edictos "
         "sucesorios) que podrían no correr. El tipo CORRIDOS es uno solo. ¿Hace falta distinguirlos? Propuesta: "
         "que corran siempre (vencimiento más temprano).",
         "Todos los hitos CORRIDOS de las matrices civiles"),
        ("Etapa común: rol en honorarios y costas",
         "El pago de honorarios y la apelación de la regulación quedan como AMBAS, porque los paga quien fue "
         "condenado en costas. ¿Es correcto o la app debería decidir el rol según la sentencia?",
         f"{P}_510, {P}_515"),
    ]
