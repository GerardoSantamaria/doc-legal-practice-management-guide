import re
from collections import OrderedDict

import datos

ROLES = datos.ROLES
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS
CIERRA = ""

DESCRIPCION_PLAZOS = {
    "HABILES_JUDICIALES": "Días hábiles judiciales (calendario judicial PBA: sin sábados, domingos, feriados, ferias ni asuetos). Es el tipo de casi todos los plazos procesales del CPCCBA. Admite gracia en los escritos de parte.",
    "CORRIDOS": "Días corridos, como los plazos del CCyC y de la Ley 14.528 (art. 6 CCyC). Si el último día es inhábil, se puede cumplir el hábil siguiente (regla R2). Admite gracia.",
    "HABILES_ADMINISTRATIVOS": "Días hábiles administrativos: lunes a viernes sin feriados; las ferias judiciales no suspenden (regla R6). Sin gracia.",
    "MESES": "Meses, de fecha a fecha (regla R7), como la caducidad de 6 meses de la compensación económica o el plazo máximo de la guarda. Admite gracia, pero en familia se carga sin gracia cuando el plazo no es para presentar un escrito.",
    "ANIOS": "Años, de fecha a fecha (regla R7). Admite gracia.",
    "HORAS": "Horas corridas desde la fecha y la hora exactas del disparador (regla R8), no desde el día hábil siguiente. Sin gracia. En familia hay plazos en horas para el juzgado y los organismos (24, 48 y 72 horas) que corren también en días inhábiles (ver la duda sobre plazos en horas).",
    "FECHA_FIJADA": "Acto con fecha y hora fijadas por el juzgado (audiencias, entrevistas, vencimiento de una medida que fija el juez). Valor 0: el abogado carga la fecha y la hora. Sin gracia.",
    "ANTICIPACION_HABILES_JUDICIALES": "Días hábiles judiciales contados hacia atrás desde un acto fijado (regla R9), como la prueba que tiene que estar agregada 10 días antes de la vista de causa. Sin gracia.",
    "SIN_PLAZO": "Sin plazo perentorio (valor 0). Depende del juzgado, de un organismo o de la parte, o el plazo lo fija el juez en cada caso: el abogado lo carga como plazo suelto. Sin gracia.",
}
assert set(DESCRIPCION_PLAZOS) == {t for t, _ in datos.PLAZO_TIPOS}


def plazo_tipos(usos):
    """Tipos de plazo de datos.py con la descripción del fuero y el uso propio de cada flujo."""
    return [(t, f"{DESCRIPCION_PLAZOS[t]} En este flujo: {usos.get(t, 'no se usa.')}") for t, _ in datos.PLAZO_TIPOS]


def flujo(nombre, regimen, notas):
    return {
        "Flujo": nombre,
        "Jurisdicción": "PBA",
        "Fuero": "Familia",
        "Régimen procesal": regimen,
        "Versión": "1 (borrador)",
        "Fecha del borrador": "13/11/2026",
        "Validado por (equipo legal)": "",
        "Fecha de validación": "",
        "Notas": notas,
    }


REGIMEN_FAMILIA = ("CPCCBA (Decreto-Ley 7425/68), Libro VIII: proceso ante los Juzgados de Familia (arts. 827 a 853, "
                   "texto de las Leyes 13.634 y 15.513)")

NOTA_FUENTES = ("Las citas se cotejaron el 13/11/2026 con textos actualizados (normas.gba.gob.ar, leyes-ar.com, "
                "digesto y acuerdos de la SCBA); las que no se pudieron confirmar dicen '(a verificar)' y tienen su duda. "
                "El expediente de familia tiene acceso limitado (art. 708 CCyC): la planilla no contiene ni debe contener "
                "datos personales de nadie.")

FASE_PREVIA = "Previa"
GRUPO_PREVIA = ("Etapa previa (antes de promover)", [FASE_PREVIA])
GRUPOS_ETAPA_COMUN = [
    ("Etapa previa ante el Consejero de Familia", ["Consejero de Familia"]),
    ("Demanda, contestación y audiencia preliminar", ["Postulación", "Audiencia preliminar"]),
    ("Prueba y vista de causa", ["Prueba", "Vista de causa"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Cumplimiento, acuerdo y cierre", ["Ejecución", "Acuerdo", "Cierre"]),
]
FASES_ETAPA_COMUN = [f for _, fases in GRUPOS_ETAPA_COMUN for f in fases]
FASES = [FASE_PREVIA] + FASES_ETAPA_COMUN
GRUPOS = [GRUPO_PREVIA] + GRUPOS_ETAPA_COMUN

ROL_TEXTO = {"ACTORA": "Actora", "DEMANDADA": "Demandada", "TRIBUNAL": "Juzgado u organismo",
             "AMBAS": "Cualquiera de las partes"}

LEYENDA = {
    "roles": ("celeste = la parte que promueve (ACTORA); naranja = la otra parte (DEMANDADA); gris = el juzgado o la "
              "espera de un organismo: Consejero de Familia, equipo técnico, Asesoría de Incapaces, Registro Provincial "
              "de las Personas, comisaría o Servicio Local, aclarado en el nombre del hito (TRIBUNAL); violeta = "
              "cualquiera de las partes (AMBAS)."),
    "paralelo": "al notificarse la sentencia corren a la vez la aclaratoria, la apelación y la apelación de los honorarios",
    "adicionales": [
        "**Derivación a otra matriz:** caja con borde grueso (es un hito final) cuyo nombre empieza con "
        "\"Sigue en la matriz de ...\": el expediente continúa en ese otro flujo de familia, en un expediente vinculado.",
        "**Fase \"Previa\":** hitos anteriores a la promoción (partidas, intimaciones, denuncia, inscripción en un "
        "registro). La app los separa en el flujo prejudicial.",
    ],
}


def leyenda(roles, paralelo):
    return {"roles": roles, "paralelo": paralelo, "adicionales": LEYENDA["adicionales"]}


INSTRUCCIONES_ADICIONALES = [
    ("Particularidades del fuero de Familia", True),
    ("9. Plazos en HORAS (por ejemplo, las 48 horas que tiene el juez para dictar medidas de protección): corren desde la fecha y la hora exactas del Evento_Disparador, no desde el día hábil siguiente (regla R8 del motor).", False),
    ("10. Plazos que fija el juez en cada caso (duración de una medida, término de la etapa previa, fecha de una audiencia o entrevista): el hito queda en SIN_PLAZO o FECHA_FIJADA y el checklist dice que el abogado carga el plazo como plazo suelto.", False),
    ("11. Derivación a otra matriz: los hitos finales llamados 'Sigue en la matriz de ...' indican que el proceso continúa en otro flujo de familia (por ejemplo, el divorcio que sigue en la matriz de alimentos y compensación económica).", False),
    ("12. Datos sensibles: estos expedientes tienen acceso limitado (art. 708 CCyC) e involucran a niños, niñas y adolescentes, víctimas de violencia y datos de salud. No escribas nombres, DNI, domicilios, diagnósticos ni relatos de hechos en las celdas ni en los comentarios: nombrá los documentos, no su contenido.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS_ETAPA = [
    ("FAM_100", "Consejero de Familia", "Solicitud de trámite de la etapa previa", "ACTORA",
     "Decisión de promover el reclamo ante el Juzgado de Familia", 0, "SIN_PLAZO", "NO",
     "Arts. 828, 829 y 830 CPCCBA (art. 828 texto Ley 15.513)", "NO", "NO",
     ["Verificar la competencia: centro de vida del niño (art. 716 CCyC), último domicilio conyugal (art. 717) o convivencial (art. 718)",
      "Presentar la solicitud de trámite ante la Receptoría General de Expedientes, con patrocinio letrado (sin patrocinio solo por urgencia, art. 829)",
      "Controlar el juzgado asignado: si hay peticiones anteriores de las mismas partes, la causa va al juzgado que previno (art. 830)",
      "Si el asunto no admite demora, pedir al juez la radicación directa sin etapa previa (art. 828, segundo párrafo)",
      "El Consejero informa en 24 horas si la etapa es conveniente, y contra la denegatoria cabe reposición (art. 831)",
      "No hace falta mediación previa: la Ley 13.951 excluye estas materias (art. 4 inc. 2, ver la duda de la etapa común)"],
     ["Formulario de solicitud de trámite", "DNI de la parte", "Partidas que acreditan el vínculo"]),
    ("FAM_110", "Consejero de Familia", "Audiencias ante el Consejero de Familia", "AMBAS",
     "Fecha y hora fijadas por el Consejero", 0, "FECHA_FIJADA", "NO",
     "Arts. 833, 834, 836 y 837 CPCCBA", "NO", "NO",
     ["Preparar al cliente y llevar una propuesta concreta",
      "El Consejero puede pedir informes al equipo técnico, convocar a otras personas y pedir al juez medidas cautelares (art. 834)",
      "Si hay violencia en el grupo familiar, pedir que no se haga una audiencia conjunta (la Ley 12.569 prohíbe la mediación y la conciliación en esos casos, art. 11)",
      "Cualquiera de las partes puede pedir que se dé por concluida la etapa (art. 836)",
      "Si el juez dispone continuarla, fija un término que no puede superar 15 días (art. 837): cargarlo como plazo suelto"],
     ["Constancia de la citación", "Propuesta de acuerdo"]),
    ("FAM_120", "Consejero de Familia", "Acta de cierre de la etapa previa", "TRIBUNAL",
     "Conciliación, fracaso o agotamiento de la intervención del Consejero", 0, "SIN_PLAZO", "NO",
     "Arts. 835 y 837 CPCCBA", "NO", "NO",
     ["Pedir copia del acta: deja constancia del resultado y de la conducta de las partes (art. 835)",
      "Si hubo acuerdo, pedir su homologación",
      "Si no hubo acuerdo, quedan expeditas las acciones (art. 837): preparar la demanda"],
     ["Acta de cierre de la etapa previa"]),
    ("FAM_200", "Postulación", "Interposición de la demanda", "ACTORA",
     "Cierre de la etapa previa, radicación directa por urgencia o decisión de demandar", 0, "SIN_PLAZO", "NO",
     "Arts. 330, 484 y 838 CPCCBA", "NO", "NO",
     ["Redactar objeto, hechos y derecho, y acompañar toda la documental y ofrecer toda la prueba con la demanda (art. 484)",
      "Acompañar el acta de cierre de la etapa previa o fundar el pedido de radicación directa",
      "Si hay niños, niñas o adolescentes o personas con capacidad restringida, pedir la intervención de la Asesoría de Incapaces (art. 103 CCyC)",
      "Pedir las medidas provisionales o cautelares que hagan falta (art. 232 CPCCBA)",
      "Tasa de justicia, bono Ley 8480 y aportes Ley 6716: verificar las exenciones (Código Fiscal, arts. 330 y 343)",
      "Constituir domicilio electrónico",
      "Incluir solo los datos de los niños que sean necesarios para resolver: el expediente tiene acceso limitado (art. 708 CCyC)"],
     ["Poder o patrocinio", "DNI de la parte", "Partidas que acreditan el vínculo", "Acta de cierre de la etapa previa",
      "Comprobantes de tasa de justicia, bono Ley 8480 y aportes Ley 6716, o constancia de exención o del beneficio de litigar sin gastos"]),
    ("FAM_210", "Postulación", "Beneficio de litigar sin gastos", "AMBAS",
     "Presentación del pedido (antes de la demanda o en cualquier estado del proceso)", 0, "SIN_PLAZO", "NO",
     "Arts. 78 a 86 CPCCBA", "NO", "NO",
     ["Ofrecer la prueba de la falta de recursos, con interrogatorio para al menos 3 testigos (art. 79)",
      "Mientras tramita, las presentaciones están exentas de impuestos y sellados (art. 83)",
      "Si se pide en el escrito de demanda, el trámite suspende el procedimiento (art. 83): evaluar si conviene pedirlo por separado",
      "Verificar antes si la materia ya está exenta de tasa"],
     ["Escrito de beneficio", "Interrogatorio para los testigos", "Constancias de ingresos"]),
    ("FAM_220", "Postulación", "Providencia inicial y traslado de la demanda", "TRIBUNAL",
     "Presentación de la demanda", 0, "SIN_PLAZO", "NO",
     "Arts. 484 y 838 CPCCBA; Reglamento de presentaciones y notificaciones electrónicas, Acuerdo SCBA 4013 (texto ordenado Ac. 4039), art. 11", "NO", "NO",
     ["Controlar el tipo de proceso: si el juez lo cambia, hay que adecuar las peticiones dentro de 10 días (art. 838): cargarlo como plazo suelto",
      "Controlar la vista a la Asesoría de Incapaces",
      "El traslado de la demanda no se notifica en forma automática: pedirlo expresamente o diligenciar la cédula en el domicilio real (art. 11 inc. c del reglamento)"],
     ["Cédula de traslado con copias de la demanda y la documental"]),
    ("FAM_230", "Postulación", "Citación por edictos al demandado con domicilio desconocido", "ACTORA",
     "Resultado negativo de las gestiones para conocer el domicilio", 0, "SIN_PLAZO", "NO",
     "Arts. 145, 146, 147 y 341 CPCCBA", "NO", "NO",
     ["Acreditar en forma sumaria las gestiones hechas para conocer el domicilio (art. 145): si la afirmación resulta falsa, se anula lo actuado y hay multa",
      "Publicar los edictos por 2 días en el Boletín Judicial y en un diario del último domicilio (arts. 146 y 341)",
      "La citación queda notificada al día siguiente de la última publicación (art. 147)",
      "Si el citado no comparece, se nombra al Defensor Oficial (art. 341)"],
     ["Oficios de averiguación de domicilio y sus respuestas", "Ejemplares de los edictos y recibos de pago"]),
    ("FAM_240", "Postulación", "Contestación de la demanda", "DEMANDADA",
     "Notificación del traslado de la demanda", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 484, 485, 486, 839 y 841 CPCCBA", "NO", "NO",
     ["Reconocer o negar cada hecho y la documental (art. 354)",
      "Oponer las excepciones previas junto con la contestación (art. 486)",
      "Reconvenir si corresponde (art. 485)",
      "Ofrecer toda la prueba (art. 484) y oponerse a los hechos no conducentes y a la prueba impertinente (art. 841)",
      "Verificar si corresponde la ampliación por distancia"],
     ["Poder o patrocinio", "DNI de la parte", "Documental", "Bono Ley 8480 y aportes Ley 6716"]),
    ("FAM_250", "Postulación", "Demanda no contestada", "ACTORA",
     "Vencimiento del plazo de contestación sin presentación", 0, "SIN_PLAZO", "NO",
     "Art. 840 CPCCBA", "NO", "NO",
     ["Pedir que se tenga por no contestada: importa el reconocimiento de los hechos lícitos pertinentes (art. 840)",
      "El juez puede dictar sentencia o disponer medidas de prueba de oficio (art. 36 inc. 2)",
      "Si el demandado fue citado por edictos, interviene el Defensor Oficial"],
     ["Escrito pidiendo que se tenga por no contestada la demanda"]),
    ("FAM_260", "Postulación", "Ampliación de la prueba del actor por hechos nuevos", "ACTORA",
     "Notificación de la providencia que tiene por contestada la demanda", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 484 (tercer párrafo) y 841 CPCCBA", "NO", "NO",
     ["Ampliar la prueba sobre los hechos nuevos invocados por el demandado",
      "Oponerse a los hechos no conducentes y a la prueba impertinente (art. 841)",
      "Revisar la documental agregada con la contestación y desconocerla si corresponde (art. 356, a verificar el plazo en el proceso de familia)"],
     ["Escrito de ampliación de prueba"]),
    ("FAM_270", "Postulación", "Contestación de la reconvención", "ACTORA",
     "Notificación del traslado de la reconvención", 10, "HABILES_JUDICIALES", "SI",
     "Art. 485 CPCCBA", "NO", "NO",
     ["Contestar la reconvención", "Ofrecer prueba"],
     ["Escrito de contestación de la reconvención"]),
    ("FAM_300", "Audiencia preliminar", "Audiencia preliminar", "AMBAS",
     "Fecha fijada por el juez una vez trabada la litis (dentro de 10 días)", 0, "FECHA_FIJADA", "NO",
     "Arts. 842 y 843 CPCCBA", "NO", "NO",
     ["Asistir con el cliente: si el actor no comparece sin justa causa se lo tiene por desistido con costas, y si no comparece el demandado se le aplica una multa de 10 a 20 Jus a depositar dentro del tercer día (art. 842)",
      "El juez puede diferirla por única vez por fuerza mayor acreditada",
      "Llevar una propuesta de acuerdo (art. 843 inc. 3)",
      "Pedir que se fijen los hechos controvertidos y se provea la prueba",
      "Las excepciones previas se resuelven en la audiencia (art. 843 inc. 6)"],
     ["Constancia de la notificación de la audiencia", "Propuesta de acuerdo"]),
    ("FAM_310", "Prueba", "Apertura a prueba y proveído de la prueba", "TRIBUNAL",
     "Cierre de la audiencia preliminar con hechos controvertidos", 0, "SIN_PLAZO", "NO",
     "Art. 843 (último párrafo) CPCCBA; art. 710 CCyC", "NO", "NO",
     ["Controlar qué prueba se admitió y cuál se denegó",
      "Registrar las cargas de impulso de cada medio de prueba",
      "Recordar que rigen la libertad, la amplitud y la flexibilidad de la prueba, y la carga probatoria dinámica (art. 710 CCyC)"],
     []),
    ("FAM_320", "Prueba", "Reposición contra la denegatoria de prueba", "AMBAS",
     "Notificación del proveído de la prueba", 3, "HABILES_JUDICIALES", "SI",
     "Arts. 238, 239 y 494 CPCCBA", "NO", "NO",
     ["Fundar la reposición contra la prueba denegada", "Hacer reserva de recurrir"],
     ["Escrito de reposición"]),
    ("FAM_330", "Prueba", "Equipo técnico: pericia psicológica o psiquiátrica", "TRIBUNAL",
     "Proveído de la prueba pericial", 0, "SIN_PLAZO", "NO",
     "Art. 844 CPCCBA; art. 12 Ley 13.634", "NO", "NO",
     ["La pericia la hace el equipo técnico del juzgado o, si no tiene la especialidad, la Asesoría Pericial (art. 844)",
      "El dictamen se presenta por escrito al menos 10 días antes de la vista de causa (art. 844)",
      "Designar consultor técnico y asegurar que el cliente concurra a las entrevistas",
      "Las explicaciones al perito se piden y se dan en la vista de causa (arts. 844 y 473)",
      "El dictamen tiene datos de salud: no copiar su contenido en los campos libres de la app"],
     ["Escrito designando consultor técnico"]),
    ("FAM_340", "Prueba", "Equipo técnico: informe socioambiental", "TRIBUNAL",
     "Proveído de la prueba o disposición de oficio del juez", 0, "SIN_PLAZO", "NO",
     "Art. 848 CPCCBA", "NO", "NO",
     ["El juez puede comisionar a trabajadores sociales: el informe se pone de manifiesto al menos 10 días antes de la vista de causa (art. 848)",
      "Preparar al cliente para la visita domiciliaria",
      "Revisar el informe y observarlo si corresponde"],
     []),
    ("FAM_350", "Prueba", "Prueba informativa (oficios)", "AMBAS",
     "Proveído de la prueba informativa", 0, "SIN_PLAZO", "NO",
     "Arts. 394 a 397 CPCCBA (art. 396 texto Ley 15.513)", "NO", "NO",
     ["Confeccionar y diligenciar los oficios (escuela, obra social, empleador, bancos, registros)",
      "Las oficinas públicas contestan en 20 días hábiles y las entidades privadas en 10, salvo otro plazo fijado (art. 396): cargar cada oficio como plazo suelto",
      "Reiterar los oficios no contestados",
      "Agregar las respuestas antes de los 10 días previos a la vista de causa (art. 846)"],
     ["Oficios diligenciados", "Constancias de recepción"]),
    ("FAM_360", "Prueba", "Escucha del niño, niña o adolescente por el juez", "TRIBUNAL",
     "Fecha y hora fijadas para la entrevista", 0, "FECHA_FIJADA", "NO",
     "Arts. 26 y 707 CCyC; art. 12 de la Convención sobre los Derechos del Niño; Ley 14.568", "NO", "NO",
     ["El juez escucha personalmente al niño y valora su opinión según su edad y grado de madurez (art. 707 CCyC)",
      "Informarle que tiene derecho a un abogado del niño (art. 1 Ley 14.568): si lo pide, pedir la designación",
      "No preparar ni condicionar al niño",
      "La entrevista es reservada: no registrar su contenido en la app"],
     []),
    ("FAM_370", "Prueba", "Incorporación de la prueba previa a la vista de causa", "AMBAS",
     "Fecha fijada para la audiencia de vista de causa", 10, "ANTICIPACION_HABILES_JUDICIALES", "NO",
     "Arts. 844, 846 y 848 CPCCBA", "NO", "NO",
     ["Verificar que pericias, informes y oficios estén agregados: la prueba que no se incorpore se pierde (art. 846)",
      "Si la demora es exclusivamente del organismo, pedir que se produzca antes de terminar la vista (art. 846)",
      "Citar a los testigos (art. 845): quienes viven a menos de 500 km están obligados a comparecer"],
     ["Cédulas de citación a testigos"]),
    ("FAM_400", "Vista de causa", "Fijación de la audiencia de vista de causa", "TRIBUNAL",
     "Apertura a prueba", 0, "SIN_PLAZO", "NO",
     "Arts. 846 a 849 CPCCBA", "NO", "NO",
     ["Instar la fijación de la audiencia", "Calcular la fecha límite para incorporar la prueba previa"],
     []),
    ("FAM_410", "Vista de causa", "Audiencia de vista de causa", "AMBAS",
     "Fecha y hora fijadas por el juez", 0, "FECHA_FIJADA", "NO",
     "Arts. 842 (último párrafo), 849, 850 y 851 CPCCBA", "NO", "NO",
     ["El juez intenta la conciliación (art. 849 inc. 1)",
      "Preparar el interrogatorio a la contraparte, a los testigos y a los peritos: los letrados interrogan en forma directa (art. 850 inc. 1)",
      "Los documentos y hechos nuevos se presentan hasta el inicio de la audiencia (art. 850 inc. 2)",
      "Preparar el alegato verbal (art. 850 inc. 3)",
      "La incomparecencia tiene las mismas consecuencias que en la audiencia preliminar (art. 842)",
      "Controlar el acta (art. 851)"],
     ["Interrogatorios", "Documentos nuevos, si los hay"]),
    ("FAM_490", "Sentencia", "Asesoría de Incapaces: vista previa a la sentencia", "TRIBUNAL",
     "Cierre de la prueba o declaración de puro derecho", 0, "SIN_PLAZO", "NO",
     "Art. 103 CCyC; art. 850 inc. 3 CPCCBA; Ley 14.442 (a verificar artículo)", "NO", "NO",
     ["Controlar que se haya dado vista a la Asesoría cuando hay niños o personas con capacidad restringida: su falta de intervención causa la nulidad relativa del acto (art. 103 CCyC)",
      "Revisar el dictamen y contestarlo si corresponde"],
     []),
    ("FAM_500", "Sentencia", "Sentencia", "TRIBUNAL",
     "Dictamen de la Asesoría o llamamiento de autos para sentencia", 0, "SIN_PLAZO", "NO",
     "Art. 494 CPCCBA (plazo del juez, a verificar en el proceso de familia)", "NO", "NO",
     ["Controlar la notificación de la sentencia",
      "Revisar lo resuelto, las costas y la regulación de honorarios",
      "Si la sentencia fija un plazo de cumplimiento, cargarlo como plazo suelto",
      "Informar al cliente"],
     []),
    ("FAM_510", "Sentencia", "Aclaratoria", "AMBAS",
     "Notificación de la sentencia", 3, "HABILES_JUDICIALES", "SI",
     "Art. 166 inc. 2 CPCCBA", "NO", "NO",
     ["Pedir la corrección de errores materiales, conceptos oscuros u omisiones"],
     ["Escrito de aclaratoria"]),
    ("FAM_520", "Sentencia", "Apelación de la regulación de honorarios", "AMBAS",
     "Notificación de la regulación de honorarios", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 9 y 57 Ley 14.967", "NO", "NO",
     ["Revisar la base y los mínimos en Jus del art. 9 Ley 14.967 para el proceso de familia de que se trate",
      "Fundar la apelación en el mismo acto de interponerla (art. 57)",
      "Controlar el pago de los aportes de la Ley 6716"],
     ["Escrito de apelación de honorarios"]),
    ("FAM_600", "Recursos", "Recurso de apelación", "AMBAS",
     "Notificación de la sentencia o de la resolución apelable", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 242, 243, 244, 494 y 852 CPCCBA", "NO", "NO",
     ["Verificar que la resolución sea apelable (arts. 242 y 494)",
      "El efecto es suspensivo salvo que la ley disponga otro (art. 243): en alimentos es devolutivo (art. 644 CPCCBA, art. 547 CCyC)",
      "Lo resuelve la Sala de Familia de la Cámara de Apelación en lo Civil y Comercial, si está creada (art. 852)",
      "Controlar si se concede libremente o en relación y en qué efecto: se puede pedir la rectificación dentro de 3 días (art. 246)"],
     ["Escrito de apelación"]),
    ("FAM_610", "Recursos", "Fundamentación de la apelación (expresión de agravios o memorial)", "AMBAS",
     "Notificación de la providencia que pone los autos en la oficina (libre) o de la que concede el recurso (en relación)", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 246 y 254 CPCCBA", "NO", "NO",
     ["Concedida libremente en el proceso sumario: expresar agravios en 5 días (art. 254)",
      "Concedida en relación: presentar el memorial en 5 días (art. 246)",
      "Si no se funda, se declara desierto el recurso",
      "Contestar el traslado de los agravios de la contraria (plazo a verificar)"],
     ["Escrito de expresión de agravios o memorial"]),
    ("FAM_620", "Recursos", "Sentencia de la Cámara (Sala de Familia)", "TRIBUNAL",
     "Fundamentación del recurso y contestación o vencimiento del traslado", 0, "SIN_PLAZO", "NO",
     "Art. 852 CPCCBA", "NO", "NO",
     ["Controlar la notificación", "Evaluar el recurso extraordinario"],
     []),
    ("FAM_630", "Recursos", "Recurso extraordinario ante la SCBA", "AMBAS",
     "Notificación de la sentencia definitiva de la Cámara", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 278, 279, 296 y 299 CPCCBA", "NO", "NO",
     ["Evaluar la procedencia (inaplicabilidad de ley o doctrina legal, nulidad, inconstitucionalidad) y el valor del agravio",
      "Fundarlo en el mismo escrito de interposición (art. 279)",
      "Verificar si corresponde el depósito previo y sus exenciones en familia (art. 280, a verificar)"],
     ["Escrito de interposición"]),
    ("FAM_640", "Recursos", "Queja ante la SCBA", "AMBAS",
     "Notificación de la denegatoria del recurso extraordinario", 5, "HABILES_JUDICIALES", "SI",
     "Art. 292 CPCCBA", "NO", "NO",
     ["Presentar la queja con las copias que exige el art. 292"],
     ["Escrito de queja", "Copias de las sentencias, del recurso y de la denegatoria"]),
    ("FAM_650", "Recursos", "Trámite y resolución ante la SCBA", "AMBAS",
     "Notificación de la providencia de autos", 10, "HABILES_JUDICIALES", "SI",
     "Art. 284 CPCCBA (a verificar)", "NO", "NO",
     ["Presentar memoria (optativa)", "Controlar la resolución de la SCBA"],
     ["Memoria"]),
    ("FAM_700", "Ejecución", "Cumplimiento de la sentencia firme", "DEMANDADA",
     "Sentencia firme o recurso concedido con efecto devolutivo", 0, "SIN_PLAZO", "NO",
     "Art. 497 CPCCBA", "NO", "NO",
     ["El plazo de cumplimiento lo fija la sentencia: cargarlo como plazo suelto",
      "Inscribir o comunicar lo que ordene la sentencia"],
     []),
    ("FAM_710", "Ejecución", "Ejecución de la sentencia", "ACTORA",
     "Vencimiento del plazo de cumplimiento sin cumplir", 0, "SIN_PLAZO", "NO",
     "Arts. 497 a 507 y 534 CPCCBA (art. 534 texto Ley 15.513)", "NO", "NO",
     ["Si la condena es ilíquida, presentar la liquidación dentro de 10 días, y la otra parte tiene vista por 5 días (art. 501)",
      "Pedir el embargo de bienes (art. 500)",
      "Las excepciones del ejecutado se oponen dentro del quinto día de la citación de venta (arts. 503 y 504)",
      "El juez puede convocar a una audiencia para definir la forma más rápida de cobro (art. 534)"],
     ["Liquidación", "Oficios de embargo"]),
    ("FAM_900", "Acuerdo", "Acuerdo y homologación", "AMBAS",
     "Firma del acuerdo (ante el Consejero, en una audiencia o fuera del expediente)", 0, "SIN_PLAZO", "NO",
     "Arts. 835 y 843 inc. 3 CPCCBA; arts. 308 y 309 CPCCBA (a verificar)", "NO", "NO",
     ["Redactar el acuerdo con plazos y modalidades verificables",
      "Si hay niños o personas con capacidad restringida, la Asesoría de Incapaces dictamina antes de la homologación",
      "Pedir la homologación",
      "Si se deniega, el proceso sigue: volver a la etapa que corresponda"],
     ["Acuerdo firmado", "Escrito pidiendo la homologación"]),
    ("FAM_910", "Acuerdo", "Cumplimiento del acuerdo homologado", "DEMANDADA",
     "Notificación de la homologación", 0, "SIN_PLAZO", "NO",
     "Arts. 498 inc. 1 y 500 CPCCBA", "NO", "NO",
     ["Cargar como plazos sueltos los vencimientos del acuerdo", "Controlar cada cumplimiento"],
     ["Constancias de cumplimiento"]),
    ("FAM_950", "Acuerdo", "Control de caducidad de instancia", "ACTORA",
     "Último acto de impulso del procedimiento", 3, "MESES", "NO",
     "Arts. 310, 311 y 313 CPCCBA", "NO", "NO",
     ["En el proceso sumario la instancia caduca a los 3 meses sin impulso (art. 310 inc. 3) y en el ordinario a los 6 meses: editar el plazo si el juez cambió el tipo de proceso",
      "El plazo corre en días inhábiles, salvo las ferias (art. 311)",
      "No hay caducidad en la ejecución de sentencia ni cuando la demora es del juzgado (art. 313)",
      "Cada acto de impulso vuelve a iniciar el cómputo: actualizar el Día Cero"],
     []),
    ("FAM_960", "Acuerdo", "Intimación previa a la caducidad de instancia", "ACTORA",
     "Notificación de la intimación del art. 315", 5, "HABILES_JUDICIALES", "SI",
     "Art. 315 CPCCBA", "NO", "NO",
     ["Manifestar la intención de continuar y producir actividad procesal útil dentro de 5 días (art. 315)",
      "Si después vuelve a pasar el mismo plazo sin actividad útil, la caducidad se decreta sin nueva intimación"],
     ["Escrito de impulso"]),
    ("FAM_990", "Cierre", "Archivo del expediente", "AMBAS",
     "Finalización del proceso", 0, "SIN_PLAZO", "NO",
     "—", "NO", "SI",
     ["Verificar que no queden honorarios ni aportes pendientes",
      "Devolver la documentación original al cliente"],
     []),
]

# origen, condicion, destino (CIERRA = cierra ese camino paralelo)
TRANSICIONES_ETAPA = [
    ("FAM_100", "Etapa previa admitida: el Consejero cita a las partes", "FAM_110"),
    ("FAM_100", "Asunto urgente o etapa improcedente: el juez dispone la radicación directa", "FAM_200"),
    ("FAM_110", "Conciliación, fracaso o intervención agotada: el Consejero labra el acta", "FAM_120"),
    ("FAM_110", "Una parte pide concluir la etapa y el juez la da por concluida", "FAM_120"),
    ("FAM_110", "El juez dispone continuar la etapa (hasta 15 días)", "FAM_110"),
    ("FAM_120", "Acuerdo", "FAM_900"),
    ("FAM_120", "Sin acuerdo: quedan expeditas las acciones", "FAM_200"),
    ("FAM_200", "Demanda presentada", "FAM_220"),
    ("FAM_200", "Demanda presentada con pedido de beneficio de litigar sin gastos", "FAM_210"),
    ("FAM_200", "Demanda presentada con pedido de beneficio de litigar sin gastos", "FAM_220"),
    ("FAM_210", "Beneficio resuelto", CIERRA),
    ("FAM_220", "Traslado ordenado al domicilio conocido del demandado", "FAM_240"),
    ("FAM_220", "Demandado con domicilio desconocido", "FAM_230"),
    ("FAM_230", "Edictos publicados: comparece el demandado o se nombra al Defensor Oficial", "FAM_240"),
    ("FAM_240", "Contesta la demanda", "FAM_260"),
    ("FAM_240", "Contesta la demanda", "FAM_300"),
    ("FAM_240", "Contesta y reconviene", "FAM_260"),
    ("FAM_240", "Contesta y reconviene", "FAM_270"),
    ("FAM_240", "Contesta y reconviene", "FAM_300"),
    ("FAM_240", "No contesta en término", "FAM_250"),
    ("FAM_250", "El juez dicta sentencia sin más trámite (art. 840)", "FAM_490"),
    ("FAM_250", "Se convoca a la audiencia preliminar", "FAM_300"),
    ("FAM_260", "Prueba ampliada o plazo vencido", CIERRA),
    ("FAM_270", "Reconvención contestada o plazo vencido", CIERRA),
    ("FAM_300", "Acuerdo en la audiencia", "FAM_900"),
    ("FAM_300", "Hechos controvertidos: se abre la causa a prueba", "FAM_310"),
    ("FAM_300", "Cuestión de puro derecho", "FAM_490"),
    ("FAM_300", "El actor no comparece sin justa causa: se lo tiene por desistido", "FAM_990"),
    ("FAM_300", "Audiencia diferida por fuerza mayor (única vez)", "FAM_300"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_330"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_340"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_350"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_360"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_400"),
    ("FAM_310", "Se provee la prueba ofrecida", "FAM_950"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_320"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_330"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_340"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_350"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_360"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_400"),
    ("FAM_310", "Se provee la prueba y se deniega una parte", "FAM_950"),
    ("FAM_320", "Reposición resuelta o plazo vencido", CIERRA),
    ("FAM_330", "Dictamen presentado, no ordenado o desistido", CIERRA),
    ("FAM_340", "Informe agregado, no ordenado o desistido", CIERRA),
    ("FAM_350", "Informes contestados o prueba desistida", CIERRA),
    ("FAM_360", "Entrevista realizada o no corresponde por la edad del niño", CIERRA),
    ("FAM_370", "Prueba incorporada o se prescinde de la pendiente", CIERRA),
    ("FAM_400", "Audiencia fijada", "FAM_370"),
    ("FAM_400", "Audiencia fijada", "FAM_410"),
    ("FAM_410", "Acuerdo en la audiencia", "FAM_900"),
    ("FAM_410", "Audiencia concluida: causa para sentencia", "FAM_490"),
    ("FAM_410", "Audiencia suspendida por fuerza mayor", "FAM_400"),
    ("FAM_490", "Dictamen emitido o no corresponde la intervención", "FAM_500"),
    ("FAM_500", "Sentencia notificada", "FAM_510"),
    ("FAM_500", "Sentencia notificada", "FAM_520"),
    ("FAM_500", "Sentencia notificada", "FAM_600"),
    ("FAM_510", "Aclaratoria resuelta o plazo vencido", CIERRA),
    ("FAM_520", "Regulación firme o apelación resuelta", CIERRA),
    ("FAM_600", "No se apela o se deniega la apelación: sentencia firme", "FAM_700"),
    ("FAM_600", "Apelación concedida", "FAM_610"),
    ("FAM_610", "Recurso fundado: resuelve la Cámara", "FAM_620"),
    ("FAM_610", "No se funda: recurso desierto y sentencia firme", "FAM_700"),
    ("FAM_620", "Sentencia de la Cámara notificada", "FAM_630"),
    ("FAM_630", "No se recurre: sentencia firme", "FAM_700"),
    ("FAM_630", "Recurso concedido", "FAM_650"),
    ("FAM_630", "Recurso denegado", "FAM_640"),
    ("FAM_640", "Queja admitida", "FAM_650"),
    ("FAM_640", "Queja rechazada o no interpuesta: sentencia firme", "FAM_700"),
    ("FAM_650", "La SCBA resuelve: sentencia firme", "FAM_700"),
    ("FAM_650", "La SCBA anula y reenvía para un nuevo pronunciamiento", "FAM_620"),
    ("FAM_700", "Sentencia cumplida", "FAM_990"),
    ("FAM_700", "Sentencia incumplida", "FAM_710"),
    ("FAM_710", "Sentencia cumplida o crédito cobrado", "FAM_990"),
    ("FAM_900", "Acuerdo homologado", "FAM_910"),
    ("FAM_900", "Homologación denegada antes de la demanda", "FAM_200"),
    ("FAM_900", "Homologación denegada con el juicio en trámite", "FAM_310"),
    ("FAM_910", "Acuerdo cumplido", "FAM_990"),
    ("FAM_910", "Acuerdo incumplido: se ejecuta", "FAM_710"),
    ("FAM_950", "Se impulsa el proceso: se actualiza el Día Cero al último acto", "FAM_950"),
    ("FAM_950", "Se dicta sentencia o termina el proceso", CIERRA),
    ("FAM_950", "La contraria pide la caducidad", "FAM_960"),
    ("FAM_960", "Actividad útil en término", "FAM_950"),
    ("FAM_960", "No hay actividad útil: se decreta la caducidad", "FAM_990"),
]

CAMPOS = {"fase": 1, "nombre": 2, "rol": 3, "evento": 4, "valor": 5, "tipo": 6, "gracia": 7, "base": 8,
          "checklist": 11, "documentacion": 12}


def etapa_judicial(prefijo, ajustes=None, quitar=(), salidas=None):
    """Etapa contenciosa común del proceso de familia (Libro VIII CPCCBA) con los IDs del flujo.

    `ajustes` reemplaza campos por ID ({"ALI_200": {"nombre": ...}}), `quitar` saca hitos y `salidas` reemplaza
    todas las transiciones de salida de un hito ({"ALI_600": [(condicion, destino), ...]}). Quitar un hito que es
    uno de varios destinos paralelos es seguro; si una condición se queda sin destinos, hay que darle otra salida
    a su origen con `salidas`."""
    ajustes, salidas, quitar = ajustes or {}, salidas or {}, set(quitar)

    def renombrar(nid):
        return nid.replace("FAM", prefijo, 1) if nid else nid

    nodos = []
    for n in NODOS_ETAPA:
        nodo = list(n)
        nodo[0] = renombrar(n[0])
        if nodo[0] in quitar:
            continue
        for campo, valor in ajustes.get(nodo[0], {}).items():
            nodo[CAMPOS[campo]] = valor
        nodos.append(tuple(nodo))
    propios = {n[0] for n in nodos}
    ajenos = (quitar - {renombrar(n[0]) for n in NODOS_ETAPA}) | ((set(ajustes) | set(salidas)) - propios)
    if ajenos:
        raise ValueError(f"IDs que no son de la etapa común o fueron quitados: {sorted(ajenos)}")

    por_condicion = OrderedDict()
    for o, c, d in TRANSICIONES_ETAPA:
        o, d = renombrar(o), renombrar(d)
        if o in quitar or o in salidas:
            continue
        por_condicion.setdefault((o, c), []).append(d)
    transiciones, sin_destino = [], []
    for (o, c), destinos in por_condicion.items():
        vivos = [d for d in destinos if d not in quitar]
        if not vivos:
            sin_destino.append(f"{o}: {c}")
        transiciones += [(o, c, d) for d in vivos]
    if sin_destino:
        raise ValueError(f"Condiciones que se quedan sin destino (usar `salidas`): {sin_destino}")
    for o, filas in salidas.items():
        transiciones += [(o, c, d) for c, d in filas]
    return nodos, transiciones


def ordenar(nodos, transiciones, por_numero=True):
    """Ordena los hitos (por número de ID, o en el orden recibido) y las transiciones según su origen, sin
    alterar el orden de las salidas de cada hito."""
    if por_numero:
        nodos = sorted(nodos, key=lambda n: int(n[0].split("_")[1]))
    posicion = {n[0]: i for i, n in enumerate(nodos)}
    return nodos, sorted(transiciones, key=lambda t: posicion[t[0]])


def numerar(dudas):
    return [(f"D{i:02d}", *d) for i, d in enumerate(dudas, start=1)]


def _solo_existentes(p, ids, nodos):
    citados = re.findall(rf"{p}_\d{{3}}", nodos)
    if not citados:
        return nodos
    vivos = [n for n in citados if n in ids]
    resto = re.sub(rf"{p}_\d{{3}}(, | y )?", "", nodos).strip()
    base = ", ".join(vivos) if vivos else "Los mismos hitos de las otras matrices de familia"
    return f"{base} {resto}".strip()


def dudas_etapa_comun(p, ids):
    """Dudas de la etapa contenciosa común, con los hitos que existen en la matriz `p`. Se responden una sola
    vez, en la matriz de alimentos."""
    return [(tema, pregunta, _solo_existentes(p, ids, nodos)) for tema, pregunta, nodos in _dudas_etapa_comun(p)]


def _dudas_etapa_comun(p):
    return [
        ("[ETAPA COMÚN] Etapa previa ante el Consejero",
         "El art. 835 CPCCBA dice que la etapa previa es 'previa e imprescindible' para las materias del art. 827, salvo urgencia, y la Ley 15.513 la hizo optativa solo en alimentos (art. 828, último párrafo). ¿En qué materias se exige hoy en la práctica de cada departamento (cuidado personal, régimen de comunicación, compensación económica, cuestiones del divorcio)? ¿Cuántas audiencias suele haber y cuánto dura? Propuesta de la app: la etapa previa es el camino por defecto y la radicación directa es una salida del primer hito. Fuente consultada: texto de los arts. 828 a 837 en leyes-ar.com (actualizado al 16/10/2026) y Ley 15.513 (B.O. 03/01/2025).",
         f"{p}_100, {p}_110, {p}_120"),
        ("[ETAPA COMÚN] Tipo de proceso y plazos",
         "El art. 838 remite al proceso plenario abreviado (sumario) y permite al juez cambiarlo. Confirmar los plazos que usa la matriz: contestación y reconvención 10 días (arts. 484 y 485), ampliación de prueba 5 días (art. 484), audiencia preliminar dentro de 10 días (art. 842), todos en días hábiles judiciales. ¿Qué materias tramitan como sumarísimo (art. 496: contestación en 5 días)? Propuesta de la app: los plazos del sumario, editables por expediente.",
         f"{p}_220, {p}_240, {p}_260, {p}_270, {p}_300"),
        ("[ETAPA COMÚN] Mediación previa",
         "La Ley 13.951 (art. 4 inc. 2) excluye de la mediación obligatoria el divorcio, la nulidad de matrimonio, la filiación y la patria potestad, los alimentos, las guardas y las adopciones. ¿El régimen de comunicación, la compensación económica, la atribución de la vivienda y la liquidación de la comunidad también quedan fuera? Propuesta de la app: en familia no hay mediación previa; la etapa previa es la del Consejero. Fuente consultada: texto de la Ley 13.951 en normas.gba.gob.ar.",
         f"{p}_100, {p}_200"),
        ("[ETAPA COMÚN] Juzgados de Paz",
         "El art. 828 permite optar por los Juzgados de Paz y remite a sus procedimientos. ¿En qué materias de familia son competentes los Juzgados de Paz Letrados (art. 61 Ley 5827, a verificar: alimentos, régimen de comunicación, violencia, divorcio por presentación conjunta) y sus plazos son los mismos? Propuesta de la app: la misma matriz sirve para el Juzgado de Paz, sin la etapa previa ante el Consejero.",
         f"{p}_100, {p}_200"),
        ("[ETAPA COMÚN] Prueba previa a la vista de causa",
         "Los arts. 844, 846 y 848 exigen que pericias, informes y prueba previa estén agregados 10 días antes de la vista de causa. ¿Son días hábiles judiciales contados hacia atrás? ¿Tienen que quedar 10 días libres (regla R9 de la matriz general, D34)? Propuesta de la app: 10 días hábiles judiciales libres antes de la audiencia (es lo más temprano).",
         f"{p}_330, {p}_340, {p}_370"),
        ("[ETAPA COMÚN] Plazo para dictar sentencia",
         "¿Qué plazo tiene el juez de familia para dictar sentencia después de la vista de causa (art. 494: 30 días, u otro del Libro VIII)? Sirve solo para alertar demoras. Propuesta de la app: sin plazo; el abogado puede cargar uno suelto.",
         f"{p}_500"),
        ("[ETAPA COMÚN] Apelación y su efecto",
         "Confirmar: apelación en 5 días (art. 244), fundamentación en 5 días (expresión de agravios en el sumario, art. 254, o memorial en relación, art. 246) y contestación de agravios (¿plazo?). ¿La Sala de Familia del art. 852 existe en todos los departamentos? ¿Qué efecto tiene la apelación en cuidado personal y régimen de comunicación (la regla del art. 243 es suspensiva)? Propuesta de la app: 5 + 5 días hábiles judiciales con gracia; el efecto se anota en el checklist.",
         f"{p}_600, {p}_610"),
        ("[ETAPA COMÚN] Queja por apelación denegada",
         "La matriz no tiene un hito para la queja ante la Cámara cuando se deniega la apelación (art. 275 CPCCBA, a verificar). ¿Qué plazo tiene? ¿Conviene agregar el hito? Propuesta de la app: plazo suelto de 5 días hábiles judiciales desde la denegatoria (a confirmar).",
         f"{p}_600"),
        ("[ETAPA COMÚN] Caducidad de instancia",
         "¿Rige la caducidad de instancia (arts. 310 a 316) en los procesos de familia: alimentos, cuidado personal, cuestiones del divorcio, compensación económica? ¿El plazo es de 3 meses por ser sumario (art. 310 inc. 3)? La intimación previa del art. 315 es de 5 días. Propuesta de la app: control de 3 meses desde el último acto de impulso, que el abogado reinicia con cada acto.",
         f"{p}_950, {p}_960"),
        ("[ETAPA COMÚN] Asesoría de Incapaces",
         "¿En qué momentos hay que dar vista a la Asesoría de Incapaces (demanda, acuerdos, prueba, antes de la sentencia) y qué artículo de la Ley 14.442 fija su intervención en familia? La falta de intervención causa la nulidad relativa (art. 103 CCyC). Propuesta de la app: vista antes de la sentencia y de cada homologación, como hitos del juzgado.",
         f"{p}_200, {p}_490, {p}_900"),
        ("[ETAPA COMÚN] Abogado del niño",
         "Ley 14.568: ¿desde qué edad se informa al niño su derecho a un abogado del niño? ¿Cómo se pide la designación en cada departamento (Registro Provincial del Colegio de Abogados)? ¿Es obligatorio en cuidado personal, como lo hizo la Ley 15.610 en adopción (art. 6 Ley 14.528)? Fuente consultada: texto de la Ley 14.568 en normas.gba.gob.ar.",
         f"{p}_360"),
        ("[ETAPA COMÚN] Feria judicial",
         "¿Qué plazos de familia se suspenden durante las ferias de enero y de invierno, y cuáles corren porque el juez habilitó días y horas (art. 153 CPCCBA; art. 4 Ley 14.528 en adopción; art. 637 en alimentos)? La SCBA fija juzgados de familia de turno para lo urgente (Acuerdos 4213 y 4214 de 2025 para 2026). Propuesta de la app: la feria suspende todos los plazos en días hábiles judiciales, salvo que el expediente tenga cargada una habilitación (ver la duda de producto sobre habilitación). Fuente consultada: Acuerdo SCBA 4214/25.",
         "Todos los de días hábiles judiciales"),
        ("[ETAPA COMÚN] Plazos en horas",
         "Los plazos de 24, 48 y 72 horas de familia (Consejero, art. 831; medidas de protección, art. 7 Ley 12.569; control de legalidad, art. 35 bis Ley 13.298; comunicaciones de la Ley 14.528) ¿corren en días inhábiles, feriados y feria? La regla R8 de la matriz general (D33) propone horas corridas desde el instante, sin traslado. Propuesta de la app: la misma regla, que es la más temprana; en familia tiene sentido porque son plazos para el juzgado o un organismo en situaciones urgentes.",
         "Todos los de horas"),
        ("[ETAPA COMÚN] Plazo de gracia",
         "¿Qué plazos de familia admiten el plazo de gracia del art. 124 CPCCBA (hasta las 12:00 del hábil siguiente)? Propuesta de la app: solo los escritos de parte en días hábiles judiciales; sin gracia en los plazos del juzgado y de organismos, en los pagos (multas, depósitos), en las caducidades y en los plazos en horas.",
         "Todos"),
        ("[ETAPA COMÚN] Notificaciones electrónicas",
         "Reglamento del Acuerdo SCBA 4013 (texto ordenado Ac. 4039): la notificación se perfecciona el martes o viernes posterior a quedar disponible, o en el momento en que queda disponible si el juez la declara urgente (art. 13). ¿Qué resoluciones de familia suelen notificarse como urgentes? El traslado de la demanda queda diferido hasta que se pida (art. 11 inc. c). Propuesta de la app: el abogado carga la fecha ya perfeccionada (como en la D30 de la matriz general). Fuente consultada: digesto de la SCBA.",
         f"{p}_220, {p}_240 y todos los que empiezan con una notificación"),
        ("[ETAPA COMÚN] Tasa de justicia, bono y aportes",
         "Código Fiscal: exentos el actor en alimentos (art. 330 inc. 7), las actuaciones de familia sin carácter patrimonial, la adopción y la tenencia (art. 343 inc. 5) y los alimentos con cuotas bajas (art. 343 inc. 10). El divorcio tiene una tasa propia en la Ley Impositiva del año, mayor si se liquida la comunidad (a verificar con la Ley Impositiva vigente). ¿El bono Ley 8480 y los aportes Ley 6716 se pagan en alimentos, violencia y adopción? Propuesta de la app: solo un ítem del checklist, sin montos. Fuente consultada: arts. 330 y 343 del Código Fiscal en leyes-ar.com.",
         f"{p}_200"),
        ("[ETAPA COMÚN] Honorarios",
         "Ley 14.967: mínimos por proceso de familia en el art. 9 (divorcio 40 Jus, violencia 20, cuidado personal y régimen de comunicación 45, adopción 40, entre otros), base de dos años en alimentos (art. 39) y apelación en 5 días (art. 57). ¿La etapa previa se regula como una etapa del proceso? ¿Qué plazo tiene la Cámara para resolver (art. 57: 10 días)? Propuesta de la app: un hito de apelación de honorarios de 5 días hábiles judiciales con gracia. Fuente consultada: texto de la Ley 14.967 en normas.gba.gob.ar.",
         f"{p}_520"),
        ("[ETAPA COMÚN] Vigencia del régimen procesal",
         "Al 13/11/2026 sigue vigente el Decreto-Ley 7425/68 con reformas parciales: no hay un código procesal de familia nuevo (hubo un proyecto de reforma integral en 2025, sin sanción conocida). ¿Hay reformas posteriores a la Ley 15.513 (2025) y a la Ley 15.610 (2026) que cambien estos plazos? Propuesta de la app: la matriz se versiona; una reforma genera una versión nueva. Fuente consultada: normas.gba.gob.ar y legislativa.senado-ba.gov.ar.",
         "Todos"),
    ]


def dudas_producto(p):
    """Dudas técnicas para el equipo de producto. Se responden una sola vez, en la matriz de alimentos."""
    return [
        ("[PRODUCTO] Roles del fuero",
         "[PRODUCTO] El rol responsable es un enum cerrado (ACTORA, DEMANDADA, TRIBUNAL, AMBAS). En familia actúan además el niño (con o sin abogado del niño), el Ministerio Público (Asesoría de Incapaces) y organismos (Servicio Local o Zonal, equipo técnico, Registro de aspirantes, comisaría). Hoy se nombran en el hito y quedan como TRIBUNAL. ¿Hacen falta roles propios (por ejemplo NNA, MINISTERIO_PUBLICO u ORGANISMO), o alcanza con el nombre del hito? Propuesta: no ampliar el enum en la V1.",
         "Todos"),
        ("[PRODUCTO] Rol representado",
         "[PRODUCTO] legal_cases.represented_role admite ACTORA o DEMANDADA. En violencia el abogado puede representar a la persona denunciada (DEMANDADA) y en adopción a los progenitores de origen (DEMANDADA, aunque consientan la adopción). En la petición conjunta de divorcio representa a los dos cónyuges (AMBAS). ¿Cómo se carga el rol representado en esos casos y cómo cambia la vista 'paso propio, de la contraparte o del juzgado'?",
         "Todos"),
        ("[PRODUCTO] Flujo prejudicial y judicial",
         "[PRODUCTO] Las matrices marcan con la fase 'Previa' lo que pasa antes de promover (partidas, intimación, denuncia policial, inscripción en el registro de aspirantes). La etapa ante el Consejero de Familia ya está radicada en un juzgado, así que se propone dejarla en el flujo judicial. Las medidas de abrigo del Servicio Local son administrativas pero con control judicial inmediato: se propone dejarlas en el judicial. ¿Es correcto? ¿Qué régimen procesal tiene un expediente que empieza en la comisaría (violencia)?",
         "Hitos de la fase Previa; ADO_100 a ADO_130; VIO_030 a VIO_050"),
        ("[PRODUCTO] Derivación entre matrices",
         "[PRODUCTO] Cuando un flujo sigue en otro (divorcio hacia compensación económica o alimentos, violencia hacia alimentos o cuidado personal, cuidado personal hacia alimentos), la matriz termina en un hito final 'Sigue en la matriz de ...'. ¿Cómo se crea y se vincula el expediente nuevo (mismo cliente, misma carátula de origen, plazos ya corriendo como la caducidad de la compensación)? ¿Un hito final en un camino paralelo cierra todo el expediente o solo ese camino? Propuesta: la app ofrece crear el expediente vinculado y el hito final cierra solo su camino si quedan otros abiertos.",
         "Hitos 'Sigue en la matriz de ...'"),
        ("[PRODUCTO] Expediente reservado",
         "[PRODUCTO] El expediente de familia tiene acceso limitado a las partes y sus letrados (art. 708 CCyC) y en adopción es reservado (art. 617 inc. e CCyC). ¿Cómo se marca un expediente reservado en la app? ¿Qué cambia: quién lo ve dentro del estudio, si aparece la carátula en el dashboard, en el resumen diario y en las exportaciones? Propuesta: todo expediente del fuero de familia es reservado por defecto. Relacionarlo con el activo A1 y la amenaza JOB-02 de modelado_de_amenazas_v1.md.",
         "Todos"),
        ("[PRODUCTO] Datos de niños y víctimas",
         "[PRODUCTO] ¿Qué datos de niños, niñas y adolescentes y de víctimas se guardan (por ejemplo, la fecha de nacimiento del hijo para el control de los 21 años en alimentos, la fecha y hora de la denuncia en violencia) y quién los ve dentro del estudio? Propuesta: solo las fechas que el motor necesita, sin nombres ni relato de hechos, y visibles solo para los miembros asignados al expediente. La política de privacidad hoy no menciona datos de terceros de esta sensibilidad.",
         f"{p}_760 y todos los de violencia y adopción"),
        ("[PRODUCTO] Datos de salud",
         "[PRODUCTO] Pericias psicológicas y psiquiátricas, informes del equipo interdisciplinario, historia clínica y certificados médicos son datos sensibles (Ley 25.326). La V1 no guarda adjuntos ni notas, pero el abogado puede escribirlos en campos libres (motivos, plazos sueltos). ¿Alcanza con el aviso que ya prevé el análisis (sección de datos sensibles) o hace falta algo más para el fuero de familia? Es la misma pregunta que la D14 de la matriz de accidentes de trabajo.",
         "CUI_330, CUI_340, VIO_130, ADO_240 y todos los informes de equipos técnicos"),
        ("[PRODUCTO] Avisos y dispositivos compartidos",
         "[PRODUCTO] Un recordatorio por email o push no puede revelar datos de una víctima ni llegar a un dispositivo o cuenta que comparte con la persona denunciada. Hoy el resumen diario trae solo cantidades y números de expediente salvo que el usuario active la carátula (JOB-02). ¿Hace falta un modo discreto por expediente (sin carátula, sin nombre del hito, sin fuero) y bloquear la activación de la carátula en expedientes de violencia? Registrarlo como amenaza nueva en modelado_de_amenazas_v1.md y revisar la política de privacidad; no se modificaron esos documentos.",
         "Todos; en especial violencia"),
        ("[PRODUCTO] Régimen procesal en el catálogo",
         "[PRODUCTO] procedural_regimes tiene hoy PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057 (y el sucesorio pidió uno civil). Para familia haría falta al menos uno (por ejemplo, el Libro VIII del CPCCBA), y quizá aparte la Ley 12.569 para violencia y la Ley 14.528 para adopción, que tienen procedimiento propio. courts.court_type tampoco tiene Juzgado de Familia ni Juzgado de Paz. ¿Uno para los cinco flujos o uno por régimen? No se modificaron el contrato de API ni el modelo de datos.",
         "Todos"),
        ("[PRODUCTO] Expediente que empieza en un hito intermedio",
         "[PRODUCTO] Si el abogado representa al denunciado en violencia, el expediente empieza en la notificación de las medidas; si representa a postulantes convocados para una guarda, empieza en la selección. ¿La app permite crear el expediente en un hito que no es el inicial? Propuesta: sí, eligiendo el hito actual al crear el expediente.",
         "VIO_070, ADO_300, ADO_400"),
        ("[PRODUCTO] Plazos que se reinician y plazos mínimos",
         "[PRODUCTO] La caducidad de instancia vuelve a correr con cada acto de impulso (se modeló como una transición del hito a sí mismo) y algunos plazos son mínimos, no máximos (la manifestación de los progenitores en adopción solo vale después de 45 días del nacimiento). En violencia, además, la apelación se abre con cada resolución apelable y puede volver a abrirse mientras sigue abierta. El motor calcula vencimientos. ¿Se aceptan estas soluciones (hito que vuelve sobre sí, un ítem del checklist para los mínimos y un plazo suelto para el segundo plazo del mismo hito)?",
         "CUI_950, DIV_950, ADO_200, VIO_200"),
        ("[PRODUCTO] Habilitación de días y horas por expediente",
         "[PRODUCTO] En adopción el juez puede habilitar días y horas inhábiles (art. 4 Ley 14.528) y en violencia y alimentos es habitual. Con habilitación, los días inhábiles cuentan para ese expediente. Hoy el motor solo permite agregar inhábiles (suspensiones), no quitarlos. ¿Hace falta una marca de 'habilitación' por expediente o por plazo?",
         "Todos los de violencia y adopción"),
    ]


DUDA_ETAPA_COMUN = (
    "Etapa común y producto",
    "Las dudas marcadas [ETAPA COMÚN] (etapa contenciosa común del proceso de familia) y [PRODUCTO] (dudas técnicas para el equipo de producto) se responden una sola vez, en matriz_familia_alimentos_pba.xlsx, y valen para esta matriz. Las reglas del motor que ya están en la matriz laboral general (D26 a D34 de matriz_flujo_laboral_pba_ley_11653.xlsx) también valen para familia: en esta matriz solo se abrieron dudas donde el fuero de familia se aparta.",
    "Todos")
