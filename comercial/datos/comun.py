import datos

ROLES = datos.ROLES
PLAZO_TIPOS = datos.PLAZO_TIPOS
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS

FASES = ["Previa", "Postulación", "Prueba", "Sentencia", "Recursos", "Ejecución", "Acuerdo", "Cierre"]

GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Prueba", ["Prueba"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Ejecución y subasta", ["Ejecución"]),
    ("Acuerdo, honorarios y cierre", ["Acuerdo", "Cierre"]),
]

LEYENDA = {
    "adicionales": [
        "**Hitos \"Sigue en la matriz de ...\":** son finales. El expediente continúa con el flujo de otra matriz "
        "comercial y hay que vincular los dos expedientes en la app (ver las dudas de producto de la matriz de concursos).",
    ],
}

DUDA_TRANSVERSAL = (
    "Dudas transversales y de producto",
    "Las dudas que valen para las tres matrices comerciales (vigencia del CPCCBA y de las leyes de fondo, tasa de "
    "justicia, bono, aportes, honorarios, ferias, plazo de gracia, notificaciones electrónicas) y las de producto "
    "(roles, rol representado, cronogramas, incidentes, vinculación de expedientes, catálogos) se responden una sola "
    "vez en matriz_comercial_concursos_pba.xlsx. Las reglas del motor se validan en las dudas D26 a D34 de "
    "matriz_flujo_laboral_pba_ley_11653.xlsx y valen también acá. ¿Hay algo de esta matriz que se aparte de esas "
    "respuestas?",
    "Todos",
)

CAMPOS = {"nombre": 2, "rol": 3, "evento": 4, "valor": 5, "tipo": 6, "gracia": 7, "base": 8,
          "checklist": 11, "documentacion": 12}

CHECKLIST_COSTOS_INICIO = [
    "Pagar la tasa de justicia y la contribución del art. 12 inc. g Ley 6716 sobre la tasa (Código Fiscal y Ley "
    "Impositiva vigente; ver dudas transversales)",
    "Pagar el bono de la Ley 8480 y el anticipo previsional del art. 13 Ley 6716 por cada letrado",
    "Estimar el monto en Jus para definir el juzgado y el tipo de proceso",
]


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


def ajustar(nodos, ajustes):
    resultado = []
    for n in nodos:
        nodo = list(n)
        for campo, valor in (ajustes or {}).get(nodo[0], {}).items():
            nodo[CAMPOS[campo]] = valor
        resultado.append(tuple(nodo))
    return resultado


def etapa_contenciosa(p, sumario, ajustes=None):
    """Proceso de conocimiento del CPCCBA (Decreto-Ley 7425/68): demanda, contestación, prueba, sentencia, recursos,
    liquidación, acuerdo, caducidad, honorarios y archivo. `sumario` elige los plazos del juicio sumario (arts. 484 a
    495) o del ordinario. Cada flujo agrega las salidas de {p}_450 (sentencia firme), {p}_460 (liquidación) y
    {p}_900 (acuerdo incumplido), y las entradas a {p}_300."""
    i = lambda n: f"{p}_{n}"
    contestacion = 10 if sumario else 15
    agravios = 5 if sumario else 10
    caducidad = 3 if sumario else 6
    proceso = "sumario (arts. 484 a 495 CPCCBA)" if sumario else "ordinario"

    nodos = [
        (i(300), "Postulación", "Presentación de la demanda", "ACTORA",
         "Decisión de demandar (mediación cerrada sin acuerdo, si corresponde)", 0, "SIN_PLAZO", "NO",
         "Arts. 330 y 332 CPCCBA" + ("; art. 484 (sumario)" if sumario else ""), "NO", "NO",
         ["Redactar la demanda con los requisitos del art. 330 y precisar el monto",
          "Acompañar toda la prueba documental (art. 332)"
          + (" y ofrecer el resto de la prueba en el mismo escrito (art. 484)" if sumario else ""),
          "Acompañar el acta de cierre de la mediación o justificar la exención",
          *CHECKLIST_COSTOS_INICIO,
          "Evaluar medidas cautelares (embargo preventivo, inhibición, anotación de litis, prohibición de innovar: "
          "arts. 209 a 232) y la contracautela (art. 199)",
          "Si la cautelar se trabó antes de la demanda, presentarla dentro de los 10 días de la traba (art. 207)"],
         ["Demanda", "Poder o patrocinio", "Prueba documental", "Acta de cierre de mediación",
          "Comprobantes de tasa, contribución, bono y anticipo previsional"]),
        (i(320), "Postulación", "Contestación de la demanda", "DEMANDADA",
         "Notificación del traslado de la demanda por cédula", contestacion, "HABILES_JUDICIALES", "SI",
         ("Art. 484 CPCCBA (10 días en el sumario; 15 en el ordinario, art. 337)" if sumario
          else "Arts. 337 y 354 CPCCBA"), "NO", "NO",
         ["Reconocer o negar cada hecho y cada documento (art. 354 inc. 1): el silencio puede tomarse como reconocimiento",
          "Oponer las excepciones previas del art. 345 "
          + ("con la contestación (art. 486)" if sumario else "dentro de los primeros 10 días (art. 344)"),
          "Oponer la prescripción junto con las excepciones, si corresponde (art. 344)",
          "Reconvenir en el mismo escrito, si corresponde (art. 355); el actor la contesta en "
          f"{contestacion} días",
          "Acompañar la documental y ofrecer la prueba" + (" (art. 484)" if sumario else ""),
          "Pagar bono y anticipo previsional del letrado del demandado"],
         ["Contestación", "Poder o patrocinio", "Prueba documental"]),
        (i(340), "Prueba", "Audiencia preliminar", "AMBAS",
         "Fecha y hora fijadas por el juzgado al proveer la contestación", 0, "FECHA_FIJADA", "NO",
         "Programa de oralidad de la SCBA (a verificar); art. 36 inc. 4 CPCCBA (a verificar)", "NO", "NO",
         ["Asistir con el cliente o con poder para conciliar",
          "Llevar una propuesta de acuerdo",
          "Controlar qué hechos se fijan como controvertidos y qué prueba se admite",
          "Si el juzgado no aplica el programa de oralidad, la audiencia no existe: cerrar este camino"],
         ["Acta de la audiencia"]),
        (i(350), "Prueba",
         "Ampliación de la prueba por hechos nuevos" if sumario else "Ofrecimiento de prueba",
         "ACTORA" if sumario else "AMBAS",
         "Notificación de la providencia que tiene por contestada la demanda" if sumario
         else "Notificación de la apertura a prueba",
         5 if sumario else 10, "HABILES_JUDICIALES", "SI",
         "Art. 484, tercer párrafo, CPCCBA" if sumario else "Arts. 358 y 365 CPCCBA", "NO", "NO",
         (["Solo para la prueba sobre los hechos nuevos que invocó el demandado",
           "Controlar la providencia que fija el plazo de prueba y la audiencia (art. 487)"] if sumario else
          ["Ofrecer toda la prueba dentro de los primeros 10 días del plazo",
           "Alegar hechos nuevos hasta 5 días después de la apertura (art. 363)",
           "El plazo de prueba lo fija el juez y no excede 40 días (art. 365): cargar la fecha de clausura"]),
         ["Escrito de prueba"]),
        (i(365), "Prueba", "Audiencia de prueba", "AMBAS",
         "Fecha y hora fijadas por el juzgado", 0, "FECHA_FIJADA", "NO",
         "Art. 487 CPCCBA" if sumario else "Arts. 404 a 456 CPCCBA (a verificar)", "NO", "NO",
         ["Citar a los testigos propios (art. 431)",
          "Preparar el pliego de posiciones",
          "Controlar el traslado del dictamen pericial e impugnarlo o pedir explicaciones (art. 473; plazo del "
          "traslado a verificar)",
          "Urgir la prueba de informes para evitar la negligencia"],
         ["Pliego de posiciones", "Lista de testigos"]),
        (i(400), "Sentencia", "Sentencia de primera instancia", "TRIBUNAL",
         "Llamamiento de autos para sentencia firme", 30 if sumario else 40, "HABILES_JUDICIALES", "NO",
         "Art. 494 CPCCBA" if sumario else "Arts. 34 inc. 3 c y 482 CPCCBA", "NO", "NO",
         ["Controlar el llamamiento de autos (art. 481)",
          "Si vence el plazo, evaluar el pedido de pronto despacho",
          "Pedir aclaratoria dentro de 3 días si hay error material u omisión (art. 166 inc. 2)"],
         ["Sentencia"]),
        (i(410), "Recursos", "Apelación de la sentencia", "AMBAS",
         "Notificación de la sentencia", 5, "HABILES_JUDICIALES", "SI", "Art. 244 CPCCBA", "NO", "NO",
         ["Apelar dentro de los 5 días",
          "Las interlocutorias se recurren con reposición en 3 días (art. 239) o apelación en 5 (art. 244)"
          + ("; en el sumario solo son apelables las del art. 494" if sumario else ""),
          "Controlar la concesión y el efecto"],
         ["Escrito de apelación"]),
        (i(420), "Recursos", "Expresión de agravios", "AMBAS",
         "Notificación de la providencia que pone el expediente en la oficina de la Cámara", agravios,
         "HABILES_JUDICIALES", "SI", "Arts. 254 y 260 CPCCBA", "NO", "NO",
         ["Hacer una crítica concreta y razonada del fallo (art. 260)",
          "Fundar en 5 días las apelaciones diferidas y pedir la prueba denegada (art. 255)",
          "Si no se expresan agravios, el recurso se declara desierto"],
         ["Expresión de agravios"]),
        (i(425), "Recursos", "Contestación de agravios", "AMBAS",
         "Notificación del traslado de la expresión de agravios", agravios, "HABILES_JUDICIALES", "SI",
         "Art. 260 CPCCBA", "NO", "NO",
         ["Contestar cada agravio", "Mantener las defensas no tratadas en la sentencia"],
         ["Contestación de agravios"]),
        (i(430), "Recursos", "Sentencia de la Cámara de Apelación", "TRIBUNAL",
         "Llamamiento de autos en la Cámara", 0, "SIN_PLAZO", "NO",
         "Arts. 34 inc. 3 c y 266 CPCCBA (a verificar)", "NO", "NO",
         ["Controlar el sorteo del orden de votación y el plazo para dictar sentencia"],
         ["Sentencia de Cámara"]),
        (i(440), "Recursos", "Recursos extraordinarios ante la SCBA", "AMBAS",
         "Notificación de la sentencia de la Cámara", 10, "HABILES_JUDICIALES", "SI",
         "Arts. 278 a 280 CPCCBA (inaplicabilidad de ley)", "NO", "NO",
         ["Verificar el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278, a verificar)",
          "Depositar el 10% del valor del litigio, entre 100 y 500 Jus (art. 280), salvo exención",
          "Evaluar también los recursos de nulidad e inconstitucionalidad"],
         ["Recurso", "Comprobante del depósito previo"]),
        (i(450), "Sentencia", "Sentencia firme", "TRIBUNAL",
         "Vencimiento del plazo para recurrir o notificación de la sentencia que pone fin al proceso", 0,
         "SIN_PLAZO", "NO", "Arts. 163 y 497 CPCCBA", "NO", "NO",
         ["Verificar que no queden recursos pendientes",
          "Controlar el plazo de cumplimiento que fije la sentencia"],
         ["Constancia de firmeza"]),
        (i(460), "Ejecución", "Liquidación de la condena", "ACTORA",
         "Sentencia ejecutable (firme y vencido el plazo de cumplimiento)", 10, "HABILES_JUDICIALES", "SI",
         "Arts. 500 a 502 CPCCBA", "NO", "NO",
         ["Practicar la liquidación con las bases de la sentencia; si el vencedor no la presenta en 10 días, "
          "puede hacerlo el vencido (art. 501)",
          "Aplicar la tasa de interés de la sentencia o, en su defecto, la de la doctrina legal de la SCBA "
          "(ver dudas transversales)",
          "La otra parte contesta la vista en 5 días; si la impugna, se tramita como incidente (art. 502)"],
         ["Liquidación"]),
        (i(900), "Acuerdo", "Acuerdo, transacción o conciliación", "AMBAS",
         "Acuerdo entre las partes", 0, "SIN_PLAZO", "NO", "Arts. 308 y 309 CPCCBA; arts. 1641 a 1648 CCyC",
         "NO", "NO",
         ["Redactar el acuerdo con monto, forma de pago, costas y honorarios",
          "Pedir la homologación: el acuerdo homologado tiene autoridad de cosa juzgada (art. 309)",
          "Pagar la tasa de justicia sobre el monto del acuerdo, si corresponde",
          "Prever la cláusula de incumplimiento y la ejecución por el trámite de ejecución de sentencia"],
         ["Acuerdo firmado", "Resolución homologatoria"]),
        (i(950), "Cierre", "Control de caducidad de instancia", "ACTORA",
         "Último acto de impulso del proceso", caducidad, "MESES", "NO",
         f"Arts. 310 a 316 CPCCBA ({caducidad} meses en el proceso {'sumario y en el ejecutivo' if sumario else 'ordinario'})",
         "NO", "NO",
         ["Cada acto de impulso reinicia el plazo: actualizar la fecha del disparador",
          "Las ferias no se cuentan (art. 311): el aviso queda antes del vencimiento real",
          "Antes de declararla, el juzgado intima por 5 días a continuar (art. 315)",
          "No corre en la ejecución de sentencia (art. 313 inc. 1)"],
         []),
        (i(960), "Cierre", "Regulación de honorarios y apelación", "AMBAS",
         "Notificación de la regulación de honorarios", 5, "HABILES_JUDICIALES", "SI",
         "Ley 14.967 (art. 57: apelación en 5 días, fundada en el mismo acto)", "NO", "NO",
         ["Pedir la regulación al terminar cada etapa o el proceso",
          "Controlar la base regulatoria y la escala de la Ley 14.967",
          "Apelar fundadamente dentro de los 5 días si la regulación es baja o alta"],
         ["Escrito de regulación o de apelación"]),
        (i(970), "Cierre", "Pago de aportes de la Ley 6716", "ACTORA",
         "Regulación de honorarios firme", 60, "CORRIDOS", "NO", "Art. 14 Ley 6716", "NO", "NO",
         ["Liquidar y pagar los aportes a la Caja de Abogados sobre los honorarios regulados",
          "Acreditar el pago en el expediente antes de pedir el archivo"],
         ["Boleta de aportes pagada"]),
        (i(990), "Cierre", "Archivo del expediente", "TRIBUNAL",
         "Cumplimiento de la sentencia o del acuerdo y pago de honorarios y aportes", 0, "SIN_PLAZO", "NO",
         "Reglamento de archivo de la SCBA (a verificar)", "NO", "SI",
         ["Verificar el pago total, el levantamiento de las cautelares y la devolución de la documentación original"],
         ["Constancia de archivo"]),
    ]
    transiciones = [
        (i(300), "Demanda proveída y traslado notificado", i(320)),
        (i(300), "Demanda proveída y traslado notificado", i(950)),
        (i(320), "Contestada la demanda (o vencido el plazo) y el juzgado fija audiencia preliminar", i(340)),
        (i(320), "Contestada la demanda (o vencido el plazo) y hay hechos controvertidos", i(350)),
        (i(320), "Cuestión de puro derecho (art. " + ("487" if sumario else "357") + ")", i(400)),
        (i(320), "Las partes llegan a un acuerdo", i(900)),
        (i(340), "Audiencia celebrada sin acuerdo", i(350)),
        (i(340), "Acuerdo en la audiencia", i(900)),
        (i(350), "Prueba ofrecida y proveída", i(365)),
        (i(400), "Sentencia notificada", i(410)),
        (i(410), "Se apela", i(420)),
        (i(410), "No se apela: queda firme", i(450)),
        (i(420), "Agravios expresados y traslado notificado", i(425)),
        (i(420), "Recurso declarado desierto", i(450)),
        (i(425), "Contestados los agravios o vencido el plazo", i(430)),
        (i(430), "Sentencia de Cámara notificada y se recurre", i(440)),
        (i(430), "Sentencia de Cámara notificada y no se recurre", i(450)),
        (i(440), "Recurso resuelto, denegado o desistido", i(450)),
        (i(450), "Sentencia de rechazo o sin condena dineraria", i(960)),
        (i(900), "Acuerdo homologado y cumplido", i(960)),
        (i(950), "Se dicta sentencia o termina el proceso", ""),
        (i(950), "Caducidad declarada", i(960)),
        (i(960), "Regulación firme", i(970)),
        (i(970), "Aportes pagados y acreditados", i(990)),
    ]
    if sumario:
        transiciones.append((i(365), "Prueba producida (en el sumario no hay alegatos, art. 493)", i(400)))
    else:
        nodos.insert(1, (
            i(325), "Postulación", "Excepciones previas", "DEMANDADA",
            "Notificación del traslado de la demanda por cédula", 10, "HABILES_JUDICIALES", "SI",
            "Arts. 344 y 345 CPCCBA", "NO", "NO",
            ["Oponerlas en un solo escrito dentro de los primeros 10 días del plazo para contestar",
             "Acompañar los recaudos del art. 347 (testimonios, documentos)",
             "Oponer en el mismo escrito la prescripción, si corresponde"],
            ["Escrito de excepciones"]))
        nodos.insert(6, (
            i(380), "Prueba", "Alegatos", "AMBAS",
            "Entrega del expediente para alegar o puesta a disposición de las constancias", 6, "HABILES_JUDICIALES",
            "SI", "Art. 480 CPCCBA", "NO", "NO",
            ["Alegar sobre el mérito de la prueba", "El plazo es común"], ["Alegato"]))
        transiciones += [
            (i(300), "Demanda proveída y traslado notificado", i(325)),
            (i(325), "Excepciones resueltas o no opuestas", ""),
            (i(365), "Prueba producida", i(380)),
            (i(380), "Alegatos presentados o vencido el plazo", i(400)),
        ]
    return ajustar(nodos, ajustes), transiciones


def bloque_ejecucion(p, ajustes=None):
    """Embargo, subasta y pago (arts. 500, 529 a 592 CPCCBA). Entra por {p}_800 y termina en {p}_960 (honorarios)."""
    i = lambda n: f"{p}_{n}"
    nodos = [
        (i(800), "Ejecución", "Embargo ejecutorio y anotación", "ACTORA",
         "Sentencia firme o liquidación aprobada", 0, "SIN_PLAZO", "NO", "Arts. 500, 529, 532 y 536 CPCCBA",
         "NO", "NO",
         ["Pedir el embargo sobre bienes suficientes; si no se conocen bienes, la inhibición general (art. 532)",
          "Los oficios a los registros se libran dentro de las 48 horas de la providencia (art. 536)",
          "Controlar el orden de la traba y los bienes inembargables (art. 533)",
          "Si lo embargado es dinero, pasar directo a la liquidación y el pago (art. 557)"],
         ["Oficios de embargo", "Informes de dominio"]),
        (i(805), "Ejecución", "Informes previos y constatación del bien", "TRIBUNAL",
         "Orden de venta del bien embargado", 0, "SIN_PLAZO", "NO",
         "Arts. 558 inc. 2 y 4 y 568 a 570 CPCCBA; mandamiento de constatación (a verificar)", "NO", "NO",
         ["Pedir informes de dominio, gravámenes, impuestos, tasas y expensas (art. 568)",
          "Citar a los acreedores hipotecarios y comunicar a los jueces embargantes; tienen 3 días (art. 569)",
          "Intimar al ejecutado a presentar el título dentro de 3 días (art. 570)",
          "Librar el mandamiento de constatación del estado de ocupación"],
         ["Informes registrales", "Acta de constatación"]),
        (i(815), "Ejecución", "Designación y aceptación del martillero", "TRIBUNAL",
         "Resolución que ordena la subasta", 0, "SIN_PLAZO", "NO", "Arts. 558 inc. 1 y 565 CPCCBA", "NO", "NO",
         ["El martillero se designa de oficio salvo acuerdo de partes (art. 558 inc. 1)",
          "En inmuebles no puede recusarse; el juez puede dejar sin efecto la designación dentro de 5 días (art. 565)",
          "Controlar la aceptación del cargo"],
         ["Acta de aceptación del cargo"]),
        (i(820), "Ejecución", "Base de la subasta: vista de la tasación", "AMBAS",
         "Notificación de la tasación o de la valuación fiscal", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 566 y 567 CPCCBA", "NO", "NO",
         ["La base de un inmueble es dos tercios de la valuación fiscal; sin valuación, de la tasación (art. 566)",
          "Manifestar conformidad u oposición fundada dentro de los 5 días comunes (art. 567)",
          "Los muebles se venden sin base (art. 558 inc. 1): cerrar este camino"],
         ["Escrito de conformidad u oposición"]),
        (i(830), "Ejecución", "Publicación de edictos de subasta", "ACTORA",
         "Resolución que fija las condiciones de la subasta", 0, "SIN_PLAZO", "NO",
         "Arts. 559, 574 y 575 CPCCBA", "NO", "NO",
         ["Muebles: 2 días en el Boletín Judicial y otro diario (art. 559)",
          "Inmuebles: 3 días en el Boletín Judicial y otro diario; 1 día si es de escaso valor (art. 574)",
          "Controlar el contenido del edicto (art. 575) y la propaganda adicional"],
         ["Edictos publicados"]),
        (i(840), "Ejecución", "Subasta electrónica", "TRIBUNAL",
         "Fecha y hora de inicio y cierre fijadas en el edicto", 0, "FECHA_FIJADA", "NO",
         "Art. 562 CPCCBA; reglamento de subastas electrónicas de la SCBA (a verificar)", "NO", "NO",
         ["La puja dura 10 días y cierra en el día y hora fijados (art. 562)",
          "En registrables el depósito previo en garantía es obligatorio",
          "Controlar la rendición de cuentas del martillero dentro de 3 días (art. 579)"],
         ["Acta de subasta", "Rendición de cuentas del martillero"]),
        (i(845), "Ejecución", "Pedido de nulidad de la subasta", "AMBAS",
         "Realización de la subasta", 5, "HABILES_JUDICIALES", "SI", "Art. 587 CPCCBA", "NO", "NO",
         ["Plantearla hasta 5 días después de realizada; se da traslado por igual plazo",
          "Si fracasa por falta de postores, nueva subasta con la base reducida 25% y luego sin base (art. 577)"],
         ["Escrito de nulidad"]),
        (i(850), "Ejecución", "Aprobación del remate y pago del saldo de precio", "TRIBUNAL",
         "Notificación del auto que aprueba el remate", 5, "HABILES_JUDICIALES", "NO",
         "Arts. 581, 582 y 585 CPCCBA", "NO", "NO",
         ["El comprador deposita el saldo dentro de 5 días de aprobado el remate (art. 581)",
          "Compra en comisión: ratificación en el mismo plazo (art. 582)",
          "Postor remiso: nuevo remate o invitación al segundo mejor postor (art. 585)"],
         ["Comprobante de depósito del saldo"]),
        (i(860), "Ejecución", "Posesión, escrituración y levantamiento de medidas", "TRIBUNAL",
         "Pago total del precio", 0, "SIN_PLAZO", "NO", "Arts. 583, 584, 586 y 588 CPCCBA", "NO", "NO",
         ["Ordenar la tradición: la venta se perfecciona con el pago y la tradición (art. 586)",
          "Escrituración sin comparecencia del ejecutado (art. 583)",
          "Levantar embargos e inhibiciones, que pasan al precio (art. 584)",
          "La desocupación se tramita por incidente (art. 588)"],
         ["Mandamiento de posesión", "Testimonio para inscripción"]),
        (i(870), "Ejecución", "Liquidación final", "ACTORA",
         "Pago del precio o aprobación del remate; o dinero embargado", 5, "HABILES_JUDICIALES", "SI",
         "Arts. 557 y 589 CPCCBA", "NO", "NO",
         ["Presentar la liquidación de capital, intereses y costas dentro de 5 días; si no, puede hacerlo el "
          "ejecutado (art. 589)",
          "Usar la tasa de la sentencia o de la doctrina legal de la SCBA (ver dudas transversales)",
          "Si el ejecutado lo pide, prestar fianza para percibir (art. 589)"],
         ["Liquidación"]),
        (i(880), "Ejecución", "Pago y distribución del producido", "TRIBUNAL",
         "Liquidación aprobada", 0, "SIN_PLAZO", "NO", "Arts. 589 y 590 CPCCBA", "NO", "NO",
         ["Pedir el libramiento de giro o transferencia",
          "Respetar preferencias: costas de la ejecución y acreedores privilegiados (art. 590)",
          "Si el producido no alcanza, ampliar el embargo sobre otros bienes"],
         ["Orden de transferencia"]),
    ]
    transiciones = [
        (i(800), "Embargo sobre bienes que hay que vender", i(805)),
        (i(800), "Dinero embargado o pago en el acto", i(870)),
        (i(805), "Informes y constatación agregados", i(815)),
        (i(815), "Martillero aceptó el cargo (inmueble)", i(820)),
        (i(815), "Martillero aceptó el cargo (mueble, sin base)", i(830)),
        (i(820), "Base fijada", i(830)),
        (i(830), "Edictos publicados", i(840)),
        (i(840), "Subasta con postor ganador", i(845)),
        (i(840), "Subasta fracasada por falta de postores", i(830)),
        (i(845), "Sin nulidad o nulidad rechazada", i(850)),
        (i(845), "Nulidad admitida: nueva subasta", i(830)),
        (i(850), "Saldo pagado", i(860)),
        (i(850), "Saldo pagado", i(870)),
        (i(850), "Postor remiso: nuevo remate", i(830)),
        (i(860), "Posesión y escrituración cumplidas", ""),
        (i(870), "Liquidación aprobada", i(880)),
        (i(880), "Crédito cancelado", i(960)),
        (i(880), "Producido insuficiente: nuevos bienes", i(800)),
    ]
    return ajustar(nodos, ajustes), transiciones
