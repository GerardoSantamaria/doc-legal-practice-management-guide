"""Seguridad social (SSO) — ANSES y justicia federal (Ley 24.463, CPCCN); variante provincial: IPS y cajas (deriva a CAD)."""
from comun import (
    CHECKLIST_COSTOS_FED,
    CHECKLIST_SIN_DATOS,
    CIERRA,
    CON_GRACIA,
    CON_VALOR_CERO,
    DUDA_REMITIR_TRANSVERSALES,
    ESTADOS,
    FUENTE_7647,
    FUENTE_24463,
    FUENTE_LPA,
    INSTRUCCIONES_ADICIONALES,
    NOTA_FUENTES,
    NOTA_SENSIBLES,
    ROL_TEXTO,
    ROLES,
    ROLES_DESCRIPCION,
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

P = "SSO"
i = lambda n: f"{P}_{n:03d}"

FLUJO = flujo(
    "Seguridad social (ANSES y justicia federal, con variante provincial)",
    "Nación (juzgado federal con asiento en PBA o de la Seguridad Social de CABA); variante PBA",
    "Federal de la Seguridad Social",
    "Ley 24.463 (art. 15 según Ley 24.655) y CPCCN; vía administrativa: Ley 19.549 reformada por la Ley 27.742; "
    "variante provincial: Decreto-Ley 9650/80 (IPS) y leyes de las cajas profesionales, que siguen en contencioso "
    "administrativo",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre el reajuste del haber (haber inicial y movilidad), el reconocimiento "
    "de servicios, la denegatoria de beneficios y las retenciones, desde el reclamo ante ANSES hasta la ejecución "
    "de la sentencia (art. 22 Ley 24.463). Los plazos federales se cargan sin gracia y con el calendario provincial "
    "hasta que se resuelva la duda de producto sobre la jurisdicción federal.",
)

FASES = [
    "Previa",
    "Vía administrativa",
    "Amparo por mora",
    "Demanda",
    "Cautelares",
    "Prueba",
    "Sentencia",
    "Recursos",
    "Ejecución",
    "Vía administrativa provincial",
    "Cierre",
]

GRUPOS = [
    ("Etapa previa: encuadre, documentación y prescripción", ["Previa"]),
    ("Vía administrativa ante ANSES (Ley 19.549, calendario administrativo nacional)", ["Vía administrativa"]),
    ("Amparo por mora contra ANSES (art. 28 Ley 19.549)", ["Amparo por mora"]),
    ("Demanda de conocimiento pleno y contestación", ["Demanda"]),
    ("Medidas cautelares contra ANSES", ["Cautelares"]),
    ("Prueba y sentencia", ["Prueba", "Sentencia"]),
    ("Recursos", ["Recursos"]),
    ("Ejecución contra ANSES (art. 22 Ley 24.463)", ["Ejecución"]),
    ("Variante provincial: IPS y cajas profesionales", ["Vía administrativa provincial"]),
    ("Honorarios y cierre", ["Cierre"]),
]

LEYENDA = leyenda(
    paralelo="la resolución denegatoria de ANSES abre a la vez el control de la caducidad para demandar y la "
             "preparación de la demanda",
    adicionales=[
        "**Calendario administrativo:** la vía ante ANSES usa el calendario administrativo nacional (Ley 19.549) y "
        "la del IPS o las cajas, el provincial (Decreto-Ley 7647/70); el checklist de cada hito lo dice.",
        "**Alzada:** desde el fallo 'Pedraza' (CSJN, 2014) las sentencias de los juzgados federales con asiento en "
        "PBA se apelan ante la Cámara Federal de Apelaciones del distrito; las de los juzgados de la Seguridad "
        "Social de CABA, ante la Cámara Federal de la Seguridad Social.",
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": (
        "caducidad para demandar (art. 15 Ley 24.463 y art. 25 inc. a Ley 19.549), contestación, alegatos, "
        "apelación y agravios del CPCCN, informe previo de la Ley 26.854 y recurso extraordinario; todos sin gracia "
        "por ser federales."
    ),
    "HABILES_ADMINISTRATIVOS": (
        "plazos para que ANSES resuelva (art. 10 Ley 19.549), cumplimiento de la sentencia en 120 días hábiles "
        "(art. 22 Ley 24.463, tipo de días a verificar) y recursos ante el IPS o las cajas (Decreto-Ley 7647/70)."
    ),
    "MESES": "vigencia de la cautelar contra ANSES (6 meses, art. 5 Ley 26.854).",
    "ANIOS": "prescripción de las mensualidades no reclamadas (a verificar si es 1 o 2 años).",
    "FECHA_FIJADA": "informe del amparo por mora y cumplimiento de la cautelar.",
    "SIN_PLAZO": "decisiones del cliente, actos del juzgado sin plazo legal, plazo de prueba que fija el juez y "
                 "trámites de ANSES sin plazo.",
})

FED = "Calendario y gracia federales: se carga sin gracia (ver duda de producto sobre jurisdicción federal)"

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    # --- Previa ---
    (i(10), "Previa", "Encuadre del reclamo previsional y del organismo", "ACTORA",
     "Consulta del cliente por su haber, un beneficio o servicios no reconocidos", 0, "SIN_PLAZO", "NO",
     "Ley 24.241; Ley 24.463; Ley 19.549", "SI", "NO",
     ["Definir la pretensión: reajuste del haber inicial, movilidad, reconocimiento de servicios, denegatoria de "
      "un beneficio o retenciones indebidas",
      "Definir el organismo: ANSES (régimen nacional) o IPS o caja profesional (régimen provincial)",
      "Juzgado: federal con asiento en la provincia o de la Seguridad Social de CABA (ver duda de competencia)",
      CHECKLIST_SIN_DATOS],
     ["Poder o patrocinio"]),
    (i(20), "Previa", "Documentación previsional del cliente", "ACTORA",
     "Encuadre del reclamo", 0, "SIN_PLAZO", "NO", "Ley 24.241 (prueba de servicios, art. 24 a verificar)", "NO",
     "NO",
     ["Pedir recibos de haberes, resolución de otorgamiento, historia laboral y certificaciones de servicios",
      "Para reconocer servicios, reunir prueba documental: la testimonial sola no alcanza (a verificar)",
      "Nombrar los documentos en la app, sin copiar números de beneficio ni de CUIL",
      CHECKLIST_SIN_DATOS],
     ["Recibos de haberes", "Resolución de otorgamiento", "Historia laboral", "Certificación de servicios"]),
    (i(30), "Previa", "Control de la prescripción de las mensualidades", "ACTORA",
     "Cada haber mensual devengado y no reclamado", 1, "ANIOS", "NO",
     "Art. 82 Ley 18.037 (a verificar) y art. 2562 inc. c CCyC (a verificar)", "NO", "NO",
     ["El reclamo administrativo interrumpe la prescripción: presentarlo cuanto antes",
      "Se carga 1 año (el plazo más corto) hasta confirmar si es 1 o 2 años",
      "El derecho al beneficio no prescribe; prescriben las diferencias mensuales"],
     []),
    (i(40), "Previa", "Control de un acuerdo de Reparación Histórica (Ley 27.260)", "ACTORA",
     "El cliente firmó o recibió una propuesta de acuerdo de Reparación Histórica", 0, "SIN_PLAZO", "NO",
     "Ley 27.260 (Programa Nacional de Reparación Histórica; vigencia del programa a verificar)", "NO", "NO",
     ["Verificar si el acuerdo fue homologado: puede impedir reclamar lo que cubrió",
      "Comparar el haber del acuerdo con el que resultaría del reajuste judicial",
      "Verificar si el programa sigue abierto al 13/11/2026 (a verificar)"],
     ["Acuerdo y resolución homologatoria"]),
    # --- Vía administrativa ANSES ---
    (i(100), "Vía administrativa", "Reclamo administrativo ante ANSES", "ACTORA",
     "Decisión de reclamar el reajuste, el beneficio o la devolución de retenciones", 0, "SIN_PLAZO", "NO",
     "Art. 15 Ley 24.463 (no exige recurso administrativo); Ley 19.549", "NO", "NO",
     ["Presentar el reclamo con turno o por los canales de ANSES y guardar el número de expediente",
      "Pedir expresamente el reajuste y las diferencias retroactivas no prescriptas",
      "Calendario administrativo nacional (ver duda de producto)",
      CHECKLIST_SIN_DATOS],
     ["Reclamo con constancia de presentación", "Recibos de haberes"]),
    (i(105), "Vía administrativa", "Reconocimiento de servicios: prueba en sede administrativa", "ACTORA",
     "Reclamo de reconocimiento de servicios no registrados o no computados", 0, "SIN_PLAZO", "NO",
     "Ley 24.241 (art. 24, a verificar); Ley 19.549", "NO", "NO",
     ["Ofrecer prueba documental y, como complemento, testigos",
      "Pedir informes a empleadores y organismos",
      "Controlar las vistas y requerimientos de ANSES y cargarlos como plazos sueltos"],
     ["Certificaciones de servicios", "Constancias de aportes"]),
    (i(110), "Vía administrativa", "ANSES resuelve el reclamo", "DEMANDADA",
     "Presentación del reclamo o de la prueba de servicios", 60, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 10 Ley 19.549 (texto reformado por la Ley 27.742 a verificar)", "NO", "NO",
     ["Calendario administrativo nacional (ver duda de producto)",
      "Si ANSES fija vistas o requerimientos, cargarlos como plazos sueltos",
      "Vencido el plazo: pronto despacho o amparo por mora"],
     ["Resolución de ANSES"]),
    (i(120), "Vía administrativa", "ANSES resuelve tras el pronto despacho", "DEMANDADA",
     "Presentación del pronto despacho", 30, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 10 Ley 19.549 (texto reformado a verificar)", "NO", "NO",
     ["Vencido el plazo sin resolución, hay silencio con sentido negativo y se puede demandar",
      "Calendario administrativo nacional"],
     ["Pronto despacho con constancia de presentación"]),
    # --- Amparo por mora ---
    (i(130), "Amparo por mora", "Amparo por mora contra ANSES", "ACTORA",
     "Vencimiento de los plazos para resolver sin pronunciamiento de ANSES", 0, "SIN_PLAZO", "NO",
     "Art. 28 Ley 19.549", "NO", "NO",
     ["Presentarlo ante el juzgado federal competente",
      "Acreditar el reclamo y el tiempo transcurrido sin resolución",
      *CHECKLIST_COSTOS_FED],
     ["Escrito de amparo por mora", "Constancia del reclamo administrativo"]),
    (i(140), "Amparo por mora", "Informe de ANSES sobre la demora", "DEMANDADA",
     "Notificación del requerimiento de informe", 0, "FECHA_FIJADA", "NO", "Art. 28 Ley 19.549", "NO", "NO",
     ["El juez fija el plazo del informe: cargar la fecha de vencimiento",
      FED],
     ["Informe de ANSES"]),
    (i(150), "Amparo por mora", "Orden judicial de resolver y su cumplimiento por ANSES", "TRIBUNAL",
     "Informe presentado o vencido su plazo", 0, "SIN_PLAZO", "NO", "Art. 28 Ley 19.549", "NO", "NO",
     ["El juez fija un plazo prudencial para que ANSES resuelva: cargarlo como plazo suelto",
      "Si ANSES no cumple, pedir astreintes (art. 804 CCyC; ver duda de astreintes contra el Estado en amparo)"],
     ["Resolución del amparo por mora"]),
    # --- Demanda ---
    (i(200), "Demanda", "Control del plazo de caducidad para demandar a ANSES", "ACTORA",
     "Notificación de la resolución denegatoria de ANSES o configuración del silencio", 180, "HABILES_JUDICIALES",
     "NO", "Art. 15 Ley 24.463; art. 25 inc. a Ley 19.549 (texto Ley 27.742, a verificar)", "NO", "NO",
     ["Se carga el plazo del art. 25 inc. a Ley 19.549 al que remite el art. 15 (ver duda)",
      "Con silencio, verificar si corre el plazo (ver duda)",
      FED],
     []),
    (i(210), "Demanda", "Demanda de conocimiento pleno contra ANSES", "ACTORA",
     "Resolución denegatoria, silencio o decisión de demandar", 0, "SIN_PLAZO", "NO",
     "Art. 15 Ley 24.463; CPCCN (trámite aplicable a verificar)", "NO", "NO",
     ["No hace falta recurso administrativo previo (art. 15)",
      "ANSES es la demandada; juzgado según el domicilio y la opción del actor (ver duda de competencia)",
      "Ofrecer pericia contable para cuantificar las diferencias",
      "Plantear la inconstitucionalidad de los topes o de la movilidad aplicada si corresponde",
      *CHECKLIST_COSTOS_FED,
      CHECKLIST_SIN_DATOS],
     ["Demanda", "Poder o patrocinio", "Resolución de ANSES", "Recibos de haberes"]),
    (i(230), "Demanda", "Contestación de la demanda por ANSES", "DEMANDADA",
     "Notificación del traslado de la demanda", 15, "HABILES_JUDICIALES", "NO",
     "Art. 338 CPCCN (a verificar si rige el plazo de 60 días para el Estado nacional)", "NO", "NO",
     ["Se carga 15 días (el plazo más corto) hasta confirmar si ANSES tiene 60 días",
      "ANSES remite el expediente administrativo",
      FED],
     ["Contestación de demanda", "Expediente administrativo"]),
    # --- Prueba ---
    (i(240), "Prueba", "Prueba: pericia contable y demás medios", "AMBAS",
     "Apertura a prueba", 0, "SIN_PLAZO", "NO", "Arts. 360, 367 y 457 y siguientes CPCCN (a verificar)", "NO",
     "NO",
     ["El juez fija el plazo de prueba: cargarlo como plazo suelto",
      "Proponer puntos de pericia: haber inicial, movilidad, topes y retroactivo",
      "Controlar la designación del perito contador y su aceptación"],
     ["Puntos de pericia", "Constancias de prueba"]),
    (i(245), "Prueba", "Observaciones o impugnación de la pericia contable", "AMBAS",
     "Notificación del traslado de la pericia", 5, "HABILES_JUDICIALES", "NO", "Art. 473 CPCCN (a verificar)", "NO",
     "NO",
     ["Revisar los cálculos con el consultor técnico",
      "Pedir explicaciones o impugnar fundadamente",
      FED],
     ["Escrito de observaciones"]),
    (i(250), "Prueba", "Alegatos", "AMBAS",
     "Notificación de la puesta de autos para alegar", 6, "HABILES_JUDICIALES", "NO",
     "Art. 482 CPCCN (a verificar)", "NO", "NO",
     ["Retirar el expediente o consultarlo digitalmente y alegar sobre la prueba",
      FED],
     ["Alegato"]),
    # --- Sentencia ---
    (i(260), "Sentencia", "Sentencia de primera instancia", "TRIBUNAL",
     "Llamamiento de autos para sentencia", 40, "HABILES_JUDICIALES", "NO",
     "Art. 34 inc. 3 ap. c CPCCN (a verificar)", "NO", "NO",
     ["Controlar que fije el haber reajustado, las pautas de movilidad, los intereses y el retroactivo",
      "Costas por su orden (art. 21 Ley 24.463)",
      "Si vence el plazo, pedir pronto despacho"],
     ["Sentencia"]),
    # --- Recursos ---
    (i(270), "Recursos", "Apelación de la sentencia previsional", "AMBAS",
     "Notificación de la sentencia de primera instancia", 5, "HABILES_JUDICIALES", "NO",
     "Art. 244 CPCCN; art. 18 Ley 24.463 y CSJN 'Pedraza' (alzada)", "NO", "NO",
     ["Apelación sin fundar en 5 días (a verificar el trámite aplicable)",
      "Alzada: Cámara Federal de Apelaciones del distrito si el juzgado está en PBA; Cámara Federal de la Seguridad "
      "Social si está en CABA",
      FED],
     ["Escrito de apelación"]),
    (i(280), "Recursos", "Expresión de agravios", "AMBAS",
     "Notificación del auto que pone el expediente en la oficina", 10, "HABILES_JUDICIALES", "NO",
     "Art. 259 CPCCN (a verificar)", "NO", "NO",
     ["Crítica concreta y razonada de la sentencia; si no se presenta, el recurso queda desierto",
      FED],
     ["Expresión de agravios"]),
    (i(285), "Recursos", "Contestación de los agravios", "AMBAS",
     "Notificación del traslado de los agravios", 10, "HABILES_JUDICIALES", "NO",
     "Art. 265 CPCCN (a verificar)", "NO", "NO",
     ["Contestar cada agravio", FED],
     ["Contestación de agravios"]),
    (i(290), "Recursos", "Sentencia de la Cámara Federal de Apelaciones o de la Seguridad Social", "TRIBUNAL",
     "Expediente en estado de resolver en la Cámara", 0, "SIN_PLAZO", "NO",
     "Art. 18 Ley 24.463; CSJN 'Pedraza'; CPCCN", "NO", "NO",
     ["Controlar el plazo y pedir pronto despacho si se demora",
      "El recurso ordinario ante la CSJN fue derogado (art. 19 derogado por la Ley 26.025): solo queda el "
      "extraordinario federal"],
     ["Sentencia de Cámara"]),
    (i(320), "Sentencia", "Sentencia previsional firme", "TRIBUNAL",
     "Vencimiento del plazo para recurrir o notificación de la última sentencia", 0, "SIN_PLAZO", "NO",
     "CPCCN", "NO", "NO",
     ["Verificar que no queden recursos pendientes",
      "Si hay condena contra ANSES, pasar a la ejecución; si no, a honorarios"],
     ["Constancia de firmeza"]),
    # --- Vía administrativa provincial ---
    (i(600), "Vía administrativa provincial", "Reclamo ante el IPS o la caja profesional", "ACTORA",
     "Decisión de reclamar un beneficio del régimen provincial", 0, "SIN_PLAZO", "NO",
     "Decreto-Ley 9650/80 (IPS) o ley de la caja profesional; Decreto-Ley 7647/70 supletorio (a verificar)", "NO",
     "NO",
     ["Presentar el reclamo con la documentación de servicios y aportes",
      "Calendario administrativo provincial (ver duda de producto)",
      CHECKLIST_SIN_DATOS],
     ["Reclamo con constancia de presentación", "Certificación de servicios"]),
    (i(605), "Vía administrativa provincial", "El IPS o la caja resuelve el reclamo", "DEMANDADA",
     "Presentación del reclamo", 30, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 77 inc. g Decreto-Ley 7647/70 (a verificar para el IPS y para cada caja)", "NO", "NO",
     ["Calendario administrativo provincial",
      "Vencido el plazo: pronto despacho o amparo por mora en la matriz de contencioso administrativo"],
     ["Resolución del IPS o de la caja"]),
    (i(610), "Vía administrativa provincial", "Recurso de revocatoria ante el IPS o la caja", "ACTORA",
     "Notificación de la resolución denegatoria", 10, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 89 Decreto-Ley 7647/70 (a verificar el régimen de recursos del IPS y de cada caja)", "NO", "NO",
     ["Calendario administrativo provincial",
      "Verificar si la resolución del directorio agota la vía o hace falta otro recurso"],
     ["Recurso de revocatoria"]),
    (i(620), "Vía administrativa provincial", "Sigue en la matriz de contencioso administrativo", "ACTORA",
     "Resolución que agota la vía, silencio o mora del IPS o de la caja", 0, "SIN_PLAZO", "NO",
     "Ley 12.008 (art. 2; cajas profesionales: art. 75, a verificar)", "NO", "SI",
     ["Crear el expediente vinculado en la matriz de contencioso administrativo",
      "Controlar el plazo de 90 días del art. 18 Ley 12.008"],
     []),
    # --- Cierre ---
    (i(990), "Cierre", "Cierre y archivo del caso", "AMBAS",
     "Pago de la sentencia, resolución favorable, desistimiento o rechazo firme con honorarios regulados", 0,
     "SIN_PLAZO", "NO", "Reglamento de archivo del juzgado (a verificar)", "NO", "SI",
     ["Verificar el alta del haber reajustado, el retroactivo y los honorarios",
      "Devolver la documentación original al cliente"],
     ["Constancia de archivo"]),
]

EXT_NODOS, EXT_TRANS = extraordinarios(P, 300, False, {"firme": i(320)})
CAUT_NODOS, CAUT_TRANS = bloque_cautelar(P, 400, fed="ORDINARIO", salidas={"incumplimiento": i(550)})
EJE_NODOS, EJE_TRANS = ejecucion_estado(P, 500, "NACION", i(950))
HON_NODOS, HON_TRANS = honorarios(P, 945, "FED", i(990))
NODOS += EXT_NODOS + CAUT_NODOS + EJE_NODOS + HON_NODOS

denegatoria = [i(200), i(210)]

TRANSICIONES = [
    # Encuadre
    (i(10), "Reajuste del haber inicial o de la movilidad", i(20)),
    (i(10), "Reajuste del haber inicial o de la movilidad", i(30)),
    (i(10), "Denegatoria de un beneficio, reconocimiento de servicios o retenciones", i(20)),
    (i(10), "El cliente firmó o recibió un acuerdo de Reparación Histórica", i(40)),
    (i(10), "Beneficio del IPS o de una caja profesional provincial", i(600)),
    (i(10), "Trámite ya iniciado y sin resolver: pronto despacho", i(120)),
    (i(10), "Trámite ya iniciado y sin resolver: amparo por mora", i(130)),
    (i(20), "Documentación reunida", i(100)),
    (i(20), "Documentación reunida: hay servicios que reconocer", i(105)),
    (i(30), "Reclamo administrativo presentado: se interrumpe la prescripción", CIERRA),
    (i(40), "Sin acuerdo, o acuerdo que no cubre lo que se reclama", i(20)),
    (i(40), "Acuerdo homologado que cubre el reclamo", i(990)),
    # Vía administrativa ANSES
    (i(100), "Reclamo presentado", i(110)),
    (i(105), "Prueba de servicios presentada", i(110)),
    (i(110), "Resolución favorable", i(990)),
    *[(i(110), "Resolución denegatoria o parcial", d) for d in denegatoria],
    (i(110), "Vence sin resolver: pronto despacho", i(120)),
    (i(110), "Vence sin resolver: amparo por mora", i(130)),
    (i(120), "Resolución favorable", i(990)),
    *[(i(120), "Resolución denegatoria o silencio", d) for d in denegatoria],
    # Amparo por mora
    (i(130), "Amparo por mora presentado", i(140)),
    (i(140), "Informe presentado o vencido el plazo", i(150)),
    (i(150), "ANSES resuelve a favor", i(990)),
    *[(i(150), "ANSES resuelve en contra, no cumple la orden o se rechaza el amparo por mora", d)
      for d in denegatoria],
    # Demanda
    (i(200), "Demanda presentada en plazo", CIERRA),
    (i(200), "Venció el plazo sin demandar: nuevo reclamo administrativo (ver duda)", i(100)),
    (i(210), "Demanda presentada y traslado notificado", i(230)),
    (i(210), "Se pide una medida cautelar", i(400)),
    (i(230), "Contestada o vencido el plazo: hay hechos que probar", i(240)),
    (i(230), "Cuestión de puro derecho", i(260)),
    # Prueba y sentencia
    (i(240), "Pericia contable presentada", i(245)),
    (i(240), "Prueba producida sin pericia pendiente", i(250)),
    (i(245), "Observaciones presentadas o vencido el plazo", i(250)),
    (i(250), "Alegatos presentados o vencido el plazo", i(260)),
    (i(260), "Sentencia notificada y se apela", i(270)),
    (i(260), "Sentencia notificada y no se apela", i(320)),
    (i(270), "Apelación concedida", i(280)),
    (i(270), "Apelación denegada o desierta", i(320)),
    (i(280), "Agravios presentados: traslado", i(285)),
    (i(280), "No se expresan agravios: recurso desierto", i(320)),
    (i(285), "Contestados o vencido el plazo", i(290)),
    (i(290), "Sentencia de Cámara notificada y se interpone recurso extraordinario", i(310)),
    (i(290), "Sentencia de Cámara notificada y no se recurre", i(320)),
    (i(320), "Condena contra ANSES", i(500)),
    (i(320), "Rechazo de la demanda", i(950)),
    # Vía administrativa provincial
    (i(600), "Reclamo presentado", i(605)),
    (i(605), "Resolución favorable", i(990)),
    (i(605), "Resolución denegatoria", i(610)),
    (i(605), "Vence sin resolver", i(620)),
    (i(610), "Revocatoria rechazada o vencido el plazo para resolver", i(620)),
    (i(610), "Revocatoria acogida", i(990)),
] + EXT_TRANS + CAUT_TRANS + EJE_TRANS + HON_TRANS

NODOS, TRANSICIONES = ordenar(NODOS, TRANSICIONES)

DUDAS_PROPIAS = [
    ("Competencia y alzada en PBA",
     "Art. 15 Ley 24.463: Juzgados Federales de Primera Instancia de la Seguridad Social de CABA y juzgados "
     "federales con asiento en las provincias. ¿Un beneficiario domiciliado en PBA puede optar por CABA? Desde "
     "'Pedraza' (CSJN, 06/05/2014) la alzada de los juzgados del interior es la Cámara Federal de Apelaciones del "
     "distrito (La Plata, San Martín, Mar del Plata, Bahía Blanca). ¿Hay cambios posteriores? Propuesta: checklist "
     "en el encuadre y en la apelación. " + FUENTE_24463,
     "SSO_010, SSO_210, SSO_270, SSO_290"),
    ("Trámite aplicable a la demanda de conocimiento pleno",
     "El art. 15 remite al proceso sumario del CPCCN, que la Ley 25.488 suprimió. ¿Los juzgados aplican hoy el "
     "ordinario? De eso dependen los plazos de contestación (15 días, o 60 para el Estado nacional, art. 338), "
     "apelación (art. 244), agravios (art. 259) y alegatos (art. 482). Propuesta: plazos del ordinario, con el más "
     "corto donde hay duda. " + FUENTE_24463,
     "SSO_230, SSO_250, SSO_270, SSO_280, SSO_285"),
    ("Plazo de caducidad para demandar a ANSES",
     "El art. 15 remite al art. 25 inc. a Ley 19.549, reformado por la Ley 27.742. ¿Cuál es el plazo vigente (se "
     "cargó 180 días hábiles judiciales) y se aplica en materia previsional, donde la jurisprudencia suele "
     "flexibilizarlo? ¿Corre con el silencio? Si vence, ¿se puede iniciar un nuevo reclamo? Propuesta: cargar el "
     "plazo sin gracia y permitir un nuevo reclamo. " + FUENTE_24463 + " " + FUENTE_LPA,
     "SSO_200"),
    ("Plazos de ANSES para resolver y silencio",
     "Art. 10 Ley 19.549: ¿el texto reformado por la Ley 27.742 mantiene 60 días para resolver, pronto despacho y "
     "30 días más? ¿Hay plazos especiales en materia previsional? ¿Son días hábiles administrativos del calendario "
     "nacional? Propuesta: 60 y 30 días hábiles administrativos. " + FUENTE_LPA,
     "SSO_110, SSO_120"),
    ("Prescripción de las diferencias",
     "¿Las mensualidades prescriben al año (art. 82 Ley 18.037) o a los 2 años (art. 2562 inc. c CCyC)? ¿Desde "
     "cuándo y qué actos la interrumpen? Propuesta: 1 año (el más temprano), interrumpido por el reclamo "
     "administrativo.",
     "SSO_030"),
    ("Movilidad: Badaro, Elliff y la ley vigente",
     "Los reajustes suelen fundarse en 'Badaro' (CSJN, 2006 y 2007) para la movilidad y en 'Elliff' (CSJN, 2009) "
     "para el haber inicial. ¿Qué fórmula de movilidad rige al 13/11/2026 y qué índices pide la pericia? Solo afecta "
     "el contenido del checklist, no los plazos.",
     "SSO_010, SSO_210, SSO_240"),
    ("Retenciones de Ganancias sobre haberes",
     "'García' (CSJN, 2019) declaró inconstitucional la retención de Ganancias a una jubilada vulnerable. ¿Qué "
     "régimen rige hoy y el reclamo se dirige a ANSES, a ARCA o a ambos? ¿Es la misma vía del art. 15? Propuesta: "
     "variante dentro de este flujo, a confirmar.",
     "SSO_010, SSO_100"),
    ("Reparación Histórica",
     "Ley 27.260: ¿el programa sigue abierto? ¿El acuerdo homologado impide demandar por los mismos rubros? "
     "Propuesta: hito de control previo, sin plazo.",
     "SSO_040"),
    ("Contestación de ANSES y expediente administrativo",
     "¿ANSES tiene 15 o 60 días para contestar (art. 338 CPCCN)? ¿Debe remitir el expediente administrativo con la "
     "contestación? Propuesta: 15 días (el más temprano para controlar la rebeldía).",
     "SSO_230"),
    ("Costas por su orden",
     "Art. 21 Ley 24.463: en todos los casos las costas son por su orden (texto vigente). ¿Hay jurisprudencia que lo "
     "inaplique a favor del jubilado? ¿Cómo se regulan entonces los honorarios (Ley 27.423)? " + FUENTE_24463,
     "SSO_260, SSO_950"),
    ("Cumplimiento de la sentencia (art. 22 Ley 24.463)",
     "120 días hábiles desde la recepción efectiva del expediente administrativo. ¿Son hábiles administrativos o "
     "judiciales? ¿Qué tasa de interés aplica la Cámara para el retroactivo? ¿Rige el orden de prelación de pago de "
     "las leyes de presupuesto? Propuesta: 120 hábiles administrativos del calendario nacional. " + FUENTE_24463,
     "SSO_500, SSO_510, SSO_530, SSO_540"),
    ("Régimen provincial: IPS y cajas profesionales",
     "¿Qué recursos prevé el Decreto-Ley 9650/80 para el IPS y con qué plazos? ¿Las cajas profesionales (abogados, "
     "médicos, ingenieros) tienen recursos propios antes del contencioso (art. 75 Ley 12.008, a verificar)? "
     "Propuesta: revocatoria del Decreto-Ley 7647/70 y derivación a contencioso administrativo. " + FUENTE_7647,
     "SSO_600, SSO_605, SSO_610, SSO_620"),
    ("Cautelares contra ANSES",
     "¿Se otorgan cautelares en reajustes (por ejemplo, por edad avanzada o enfermedad) y entran en la excepción del "
     "art. 2 inc. 2 Ley 26.854 (carácter alimentario)? Propuesta: checklist que pida invocar la excepción.",
     "SSO_400, SSO_415, SSO_450"),
    DUDA_REMITIR_TRANSVERSALES,
]

DUDAS = numerar(DUDAS_PROPIAS)
