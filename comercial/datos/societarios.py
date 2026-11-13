from comun import CON_GRACIA, CON_VALOR_CERO, DUDA_TRANSVERSAL, ESTADOS, PLAZO_TIPOS, ROLES, etapa_contenciosa, flujo
from comun import FASES as FASES_BASE
from comun import GRUPOS as GRUPOS_BASE
from comun import LEYENDA as LEYENDA_BASE

FASES = FASES_BASE[:1] + ["Cautelares"] + FASES_BASE[1:-1] + ["Liquidación"] + FASES_BASE[-1:]

GRUPOS = GRUPOS_BASE[:1] + [("Medidas cautelares e intervención judicial", ["Cautelares"])] + GRUPOS_BASE[1:4] + [
    ("Liquidación de la condena", ["Ejecución"]),
    ("Disolución y liquidación de la sociedad", ["Liquidación"]),
] + GRUPOS_BASE[5:]

ROL_TEXTO = {"ACTORA": "Socio o accionista que promueve", "DEMANDADA": "Sociedad o administradores",
             "TRIBUNAL": "Juzgado, interventor o DPPJ", "AMBAS": "Cualquiera de las partes"}

EJEMPLO_PARALELO = ("al clausurarse la asamblea corre la caducidad de 3 meses de la impugnación mientras se pide la "
                    "suspensión de la decisión y se hace la mediación")

LEYENDA = {
    "roles": "celeste = socio, accionista o director que promueve (o la sociedad, en la acción social y en la "
             "exclusión); naranja = sociedad, administradores, liquidadores o socio excluido; gris = juzgado, "
             "veedor, interventor o Dirección Provincial de Personas Jurídicas (DPPJ); violeta = cualquiera de las "
             "partes.",
    "paralelo": EJEMPLO_PARALELO,
    "adicionales": LEYENDA_BASE["adicionales"] + [
        "**Cobro de la condena:** si la sentencia condena a pagar y no se paga, el expediente sigue en la matriz de "
        "juicios ejecutivos, en el bloque de embargo y subasta.",
    ],
}

ROLES_DESCRIPCION = [
    ("ACTORA", "Debe actuar el socio, accionista o director que promueve la acción (o la sociedad, en la acción "
               "social de responsabilidad y en la exclusión de un socio)."),
    ("DEMANDADA", "Debe actuar la sociedad, sus administradores o liquidadores, o el socio excluido."),
    ("TRIBUNAL", "Depende del juzgado, del veedor o interventor, o de la DPPJ (la app muestra 'Esperando "
                 "resolución')."),
    ("AMBAS", "Puede o debe actuar cualquiera de las partes (asambleas, mediación, recursos, impugnaciones)."),
]

FLUJO = flujo(
    "Conflictos societarios - Provincia de Buenos Aires",
    "Ley General de Sociedades 19.550 (t.o. 1984, con las reformas de las Leyes 26.994 y 27.077); CPCCBA "
    "(Decreto-Ley 7425/68), juicio sumario (art. 15 LGS); Ley 13.951 (mediación)",
    "Impugnación de decisiones de asamblea o de reunión de socios (con suspensión preventiva), intervención "
    "judicial, remoción de administradores y acción de responsabilidad, exclusión de socios, convocatoria judicial "
    "o administrativa a asamblea, derecho de información, y disolución y liquidación. El juicio sigue la etapa "
    "contenciosa común del CPCCBA por el trámite sumario. Las citas marcadas 'a verificar' no se usan hasta que el "
    "abogado las confirme.",
)

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
PREVIA = [
    ("SOC_010", "Previa", "Diagnóstico del conflicto societario", "ACTORA",
     "Primera consulta del socio, accionista, director o de la sociedad", 0, "SIN_PLAZO", "NO",
     "Arts. 15, 55, 91, 94, 113, 236, 251 y 276 a 279 LGS", "SI", "NO",
     ["Identificar el tipo social y pedir el estatuto o contrato y sus reformas inscriptas en la DPPJ",
      "Revisar si el estatuto tiene cláusula arbitral o un procedimiento interno previo",
      "Acreditar la calidad de socio o accionista y su porcentaje (libro de registro de acciones o contrato)",
      "Pedir copia del legajo de la sociedad en la DPPJ",
      "Identificar la vía: información, convocatoria, impugnación, exclusión, remoción y responsabilidad, "
      "intervención o disolución",
      "Si la sociedad está en cesación de pagos, evaluar la vía concursal"],
     ["Estatuto o contrato social y reformas", "Constancia de la calidad de socio o accionista",
      "Legajo de la DPPJ"]),
    ("SOC_020", "Previa", "Pedido de información o exhibición de libros", "ACTORA",
     "Decisión de pedir información a la sociedad", 0, "SIN_PLAZO", "NO",
     "Arts. 55 y 294 inc. 6 LGS; art. 323 CPCCBA (a verificar el inciso)", "NO", "NO",
     ["Socio de sociedad de personas o de SRL sin consejo de vigilancia: examinar libros y papeles (art. 55)",
      "Accionista de sociedad por acciones con sindicatura: pedir la información al síndico, si tiene al menos el "
      "2% del capital (art. 294 inc. 6)",
      "Pedir por carta documento, indicando los libros y documentos",
      "Si se niega, evaluar la diligencia preliminar de exhibición, que no requiere mediación (art. 4 inc. 7 Ley "
      "13.951)"],
     ["Carta documento con el pedido"]),
    ("SOC_030", "Previa", "Plazo para celebrar la asamblea pedida por accionistas", "DEMANDADA",
     "Recepción del pedido de convocatoria por el directorio o el síndico", 40, "CORRIDOS", "NO",
     "Art. 236 LGS", "NO", "NO",
     ["Lo pueden pedir accionistas con al menos el 5% del capital, salvo que el estatuto fije menos",
      "El pedido indica los temas a tratar",
      "El directorio o el síndico convoca para que la asamblea se celebre dentro de los 40 días de recibido",
      "SRL: revisar el régimen del art. 159 y del contrato"],
     ["Pedido de convocatoria con constancia de recepción"]),
    ("SOC_035", "Previa", "Convocatoria a asamblea por la DPPJ o por el juez", "ACTORA",
     "Omisión del directorio o del síndico de convocar", 0, "SIN_PLAZO", "NO",
     "Art. 236 LGS; normativa de la DPPJ (a verificar)", "NO", "NO",
     ["Elegir entre la vía administrativa ante la DPPJ y la judicial",
      "Acreditar el pedido y la omisión",
      "La convocatoria judicial no requiere mediación previa si se plantea como medida urgente (a verificar)"],
     ["Pedido de convocatoria", "Constancia del pedido a la sociedad"]),
    ("SOC_040", "Previa", "Asamblea o reunión de socios", "AMBAS",
     "Fecha y hora fijadas en la convocatoria", 0, "FECHA_FIJADA", "NO", "Arts. 237, 238 y 159 LGS", "NO", "NO",
     ["Cargar la fecha fijada en la convocatoria",
      "Controlar las publicaciones: 5 días, con 10 a 30 días de anticipación (art. 237)",
      "Depositar las acciones o comunicar la asistencia con 3 días hábiles de anticipación (art. 238)",
      "Votar en contra o dejar constancia en el acta para conservar la legitimación para impugnar (art. 251)",
      "Pedir copia del acta"],
     ["Edictos de convocatoria", "Comprobante de asistencia", "Acta de la asamblea"]),
    ("SOC_050", "Previa", "Plazo de caducidad para impugnar la decisión", "ACTORA",
     "Clausura de la asamblea", 3, "MESES", "NO", "Arts. 251, 253 y 254 LGS", "NO", "NO",
     ["Pueden impugnar los accionistas que no votaron a favor, los ausentes y los que votaron con vicio de la "
      "voluntad; también los directores, síndicos y la autoridad de contralor (art. 251)",
      "La demanda es contra la sociedad, ante el juez de su domicilio (art. 251)",
      "El juicio no avanza hasta vencidos los 3 meses; todas las impugnaciones se acumulan (art. 253)",
      "Si una asamblea posterior revoca la decisión, la acción se extingue (art. 254)",
      "La mediación no suspende esta caducidad (duda D02): presentar la demanda antes del vencimiento"],
     []),
    ("SOC_055", "Previa", "Plazo de caducidad para excluir a un socio", "ACTORA",
     "Conocimiento del hecho que justifica la exclusión", 90, "CORRIDOS", "NO", "Arts. 91 a 93 LGS", "NO", "NO",
     ["Requiere justa causa, como el grave incumplimiento de las obligaciones del socio (art. 91)",
      "La acción la ejerce la sociedad por su representante, o los socios en forma individual citando a los demás",
      "Se puede pedir la suspensión provisoria de los derechos del socio (art. 91)",
      "Sociedad de dos socios: régimen del art. 93",
      "Verificar en qué tipos sociales procede (duda D05)"],
     []),
    ("SOC_060", "Previa", "Plazo para que el accionista promueva la acción social", "ACTORA",
     "Fecha de la asamblea que resolvió promover la acción de responsabilidad", 3, "MESES", "NO",
     "Arts. 276, 277 y 279 LGS", "NO", "NO",
     ["La resolución de la asamblea implica la remoción del director afectado (art. 276)",
      "Si la sociedad no la promueve dentro de los 3 meses, puede hacerlo cualquier accionista (art. 277)",
      "La acción individual del accionista dañado en su patrimonio corre por separado (art. 279)",
      "Si la sociedad quiebra, la acción la ejerce el síndico (art. 278)"],
     ["Acta de la asamblea"]),
    ("SOC_070", "Previa", "Mediación prejudicial obligatoria", "AMBAS",
     "Última notificación de la audiencia de mediación al requerido", 60, "CORRIDOS", "NO",
     "Arts. 2, 4, 12, 19 a 23 y 40 Ley 13.951", "NO", "NO",
     ["Plazo de 60 días corridos, prorrogable 15 por acuerdo (art. 12)",
      "No requieren mediación previa las medidas cautelares ni las diligencias preliminares (art. 4 incs. 6 y 7)",
      "Si hay acuerdo, pedir la homologación dentro de los 10 días (art. 19)",
      "Controlar que la mediación no haga vencer la caducidad de la impugnación o de la exclusión"],
     ["Formulario de requerimiento", "Acta de cierre de la mediación"]),
]

CAUTELARES = [
    ("SOC_100", "Cautelares", "Suspensión preventiva de la decisión impugnada", "ACTORA",
     "Decisión de impugnar con pedido de suspensión", 0, "SIN_PLAZO", "NO",
     "Art. 252 LGS; arts. 195 y 199 CPCCBA", "NO", "NO",
     ["Acreditar motivos graves y que la suspensión no perjudica a terceros",
      "Ofrecer la garantía suficiente que fije el juez",
      "Pedirla con la demanda o antes; si se traba antes, presentar la demanda dentro de los 10 días (art. 207 "
      "CPCCBA)"],
     ["Escrito de suspensión", "Contracautela"]),
    ("SOC_105", "Cautelares", "Suspensión provisoria de los derechos del socio a excluir", "ACTORA",
     "Decisión de excluir con pedido de suspensión", 0, "SIN_PLAZO", "NO", "Art. 91 LGS; art. 195 CPCCBA",
     "NO", "NO",
     ["Acreditar la justa causa con verosimilitud",
      "Si se traba antes de la demanda, presentarla dentro de los 10 días (art. 207 CPCCBA)"],
     ["Escrito de suspensión"]),
    ("SOC_110", "Cautelares", "Pedido de intervención judicial", "ACTORA",
     "Demanda de remoción del administrador presentada", 0, "SIN_PLAZO", "NO",
     "Arts. 113, 114 y 116 LGS; arts. 222 a 227 CPCCBA (a verificar)", "NO", "NO",
     ["Acreditar la calidad de socio, el peligro grave y que se agotaron los recursos del contrato (art. 114)",
      "Acreditar que se promovió la acción de remoción",
      "El criterio de los jueces es restrictivo: elegir la medida menos gravosa",
      "Ofrecer la contracautela que fije el juez (art. 116)"],
     ["Escrito de intervención", "Prueba del peligro grave", "Contracautela"]),
    ("SOC_120", "Cautelares", "Designación del interventor y fijación de su misión", "TRIBUNAL",
     "Resolución que decreta la intervención", 0, "SIN_PLAZO", "NO", "Art. 115 LGS", "NO", "NO",
     ["El juez elige entre veedor, coadministrador o administrador",
      "Fija la misión, las atribuciones y el término de la intervención, y los honorarios",
      "Controlar la aceptación del cargo y los informes del interventor"],
     ["Resolución de designación", "Acta de aceptación del cargo"]),
    ("SOC_125", "Cautelares", "Apelación de la resolución sobre la intervención", "AMBAS",
     "Notificación de la resolución que decreta o rechaza la intervención", 5, "HABILES_JUDICIALES", "SI",
     "Art. 117 LGS; art. 244 CPCCBA", "NO", "NO",
     ["La resolución que decreta la intervención es apelable al solo efecto devolutivo (art. 117)",
      "Fundar en el plazo del memorial (art. 246 CPCCBA, a verificar)"],
     ["Escrito de apelación"]),
    ("SOC_130", "Cautelares", "Vencimiento del término de la intervención", "AMBAS",
     "Fecha de vencimiento fijada por el juez", 0, "FECHA_FIJADA", "NO", "Art. 115 LGS", "NO", "NO",
     ["Cargar la fecha que fijó el juez",
      "La prórroga se pide por información sumaria antes del vencimiento",
      "Pedir el informe final del interventor"],
     ["Pedido de prórroga", "Informe del interventor"]),
]

PROPIOS_CIERRE = [
    ("SOC_480", "Sentencia", "Inscripción de la sentencia en la DPPJ", "ACTORA",
     "Sentencia firme que anula la decisión, excluye al socio, remueve al administrador o declara la disolución",
     0, "SIN_PLAZO", "NO", "Arts. 60, 92 inc. 5 y 98 LGS", "NO", "NO",
     ["Librar el oficio a la DPPJ con testimonio de la sentencia firme",
      "La designación o cesación de administradores se inscribe (art. 60)",
      "El socio excluido responde frente a terceros hasta la inscripción (art. 92 inc. 5)",
      "La disolución se inscribe (art. 98)"],
     ["Oficio a la DPPJ", "Constancia de inscripción"]),
    ("SOC_600", "Liquidación", "Disolución de la sociedad", "ACTORA",
     "Ocurrencia de la causal de disolución", 0, "SIN_PLAZO", "NO", "Arts. 94, 94 bis, 97, 98, 99 y 100 LGS",
     "NO", "NO",
     ["Identificar la causal del art. 94",
      "Pérdida del capital (art. 94 inc. 5): suspendida por el art. 59 de la Ley 27.541 (duda D08)",
      "Reducción a uno del número de socios: régimen del art. 94 bis (a verificar)",
      "Los administradores solo atienden asuntos urgentes desde la causal y responden por los actos posteriores "
      "(art. 99)",
      "Las causales pueden removerse con decisión del órgano de gobierno si es viable (art. 100)"],
     ["Acta que constata la causal", "Estados contables"]),
    ("SOC_610", "Liquidación", "Designación e inscripción del liquidador", "DEMANDADA",
     "Disolución de la sociedad", 30, "CORRIDOS", "NO", "Art. 102 LGS", "NO", "NO",
     ["La liquidación está a cargo del órgano de administración, salvo pacto en contrario",
      "Si no, los socios nombran liquidador por mayoría dentro de los 30 días",
      "Si no lo designan, cualquier socio puede pedir al juez el nombramiento",
      "Inscribir el nombramiento; el liquidador puede ser removido por justa causa"],
     ["Acta de designación", "Constancia de inscripción"]),
    ("SOC_620", "Liquidación", "Inventario y balance inicial de liquidación", "DEMANDADA",
     "Asunción del cargo por el liquidador", 30, "CORRIDOS", "NO", "Art. 103 LGS", "NO", "NO",
     ["El liquidador los presenta dentro de los 30 días de asumir; los socios pueden extender el plazo hasta "
      "120 días",
      "Pedir copia y revisar los criterios de valuación"],
     ["Inventario", "Balance de liquidación"]),
    ("SOC_630", "Liquidación", "Informe trimestral del liquidador", "DEMANDADA",
     "Presentación del inventario o del último informe", 3, "MESES", "NO", "Art. 104 LGS", "NO", "NO",
     ["El liquidador informa a los socios sobre el estado de la liquidación al menos cada 3 meses",
      "En las sociedades por acciones informa a la sindicatura (a verificar)",
      "Al recibir cada informe, actualizar el disparador"],
     ["Informe trimestral"]),
    ("SOC_635", "Liquidación", "Balance final y proyecto de distribución", "DEMANDADA",
     "Extinción del pasivo social", 0, "SIN_PLAZO", "NO", "Arts. 107 y 109 LGS", "NO", "NO",
     ["Reembolso de las partes de capital y distribución del excedente según la participación en las ganancias "
      "(art. 109)",
      "Puede haber distribuciones parciales con garantía (art. 107)"],
     ["Balance final", "Proyecto de distribución"]),
    ("SOC_640", "Liquidación", "Impugnación del balance final", "ACTORA",
     "Comunicación del balance final y del proyecto de distribución", 15, "CORRIDOS", "NO", "Art. 110 LGS",
     "NO", "NO",
     ["Impugnar dentro de los 15 días de la comunicación",
      "En las SRL del art. 299 inc. 2 y en las sociedades por acciones, el balance se somete a la asamblea "
      "(art. 110)"],
     ["Escrito de impugnación"]),
    ("SOC_645", "Liquidación", "Acción judicial de impugnación del balance final", "ACTORA",
     "Vencimiento del plazo de impugnación del balance", 60, "CORRIDOS", "NO", "Art. 110 LGS", "NO", "NO",
     ["Promover la acción dentro de los 60 días siguientes; se acumulan todas en una causa",
      "Requiere mediación previa (a verificar)"],
     ["Demanda de impugnación"]),
    ("SOC_650", "Liquidación", "Distribución y cancelación de la inscripción", "DEMANDADA",
     "Balance final y proyecto aprobados", 0, "SIN_PLAZO", "NO", "Arts. 111 y 112 LGS", "NO", "NO",
     ["Agregar el balance y el proyecto aprobados al legajo y ejecutar la distribución (art. 111)",
      "Lo no reclamado en 90 días se deposita en un banco oficial; a los 3 años pasa a la autoridad escolar",
      "Pedir la cancelación de la inscripción y designar quién conserva los libros (art. 112)"],
     ["Constancia de cancelación de la inscripción"]),
]

DERIVACIONES = [
    ("SOC_980", "Cierre", "Sigue en la matriz de concursos y quiebras", "TRIBUNAL",
     "Presentación en concurso o declaración de quiebra de la sociedad", 0, "SIN_PLAZO", "NO",
     "Arts. 5, 21, 77 y 278 LCQ; art. 94 inc. 6 LGS", "NO", "SI",
     ["Los juicios de contenido patrimonial contra la sociedad se suspenden (art. 21 LCQ)",
      "La quiebra disuelve la sociedad (art. 94 inc. 6 LGS)",
      "La acción social de responsabilidad la ejerce el síndico (art. 278 LGS)",
      "Abrir el expediente en la matriz de concursos y vincularlo"],
     ["Constancia de los edictos del concurso o de la quiebra"]),
    ("SOC_985", "Cierre", "Sigue en la matriz de juicios ejecutivos (cumplimiento de la sentencia)", "ACTORA",
     "Liquidación aprobada o acuerdo homologado incumplido", 0, "SIN_PLAZO", "NO",
     "Arts. 497 a 508 CPCCBA (a verificar)", "NO", "SI",
     ["Pedir el embargo ejecutorio y seguir con el bloque de ejecución y subasta",
      "Abrir el expediente en la matriz de juicios ejecutivos desde el hito 'Embargo ejecutorio y anotación' y "
      "vincularlo"],
     ["Liquidación aprobada o acuerdo homologado"]),
]

CONTENCIOSA_NODOS, CONTENCIOSA_TRANSICIONES = etapa_contenciosa("SOC", sumario=True, ajustes={
    "SOC_300": {"nombre": "Presentación de la demanda societaria (juicio sumario)",
                "evento": "Mediación cerrada sin acuerdo o exenta, y dentro del plazo de caducidad"},
})

NODOS = (PREVIA + CAUTELARES + CONTENCIOSA_NODOS[:-1] + PROPIOS_CIERRE + [CONTENCIOSA_NODOS[-1]] + DERIVACIONES)

TRANSICIONES = [
    ("SOC_010", "El socio no tiene información sobre la gestión", "SOC_020"),
    ("SOC_010", "Hay que pedir una asamblea (temas a tratar, remoción o acción social)", "SOC_030"),
    ("SOC_010", "Hay una asamblea convocada o ya celebrada", "SOC_040"),
    ("SOC_010", "Exclusión de un socio por justa causa", "SOC_055"),
    ("SOC_010", "Remoción judicial del administrador o acción individual de responsabilidad", "SOC_070"),
    ("SOC_010", "Causal de disolución", "SOC_600"),
    ("SOC_010", "Sociedad en cesación de pagos", "SOC_980"),
    ("SOC_020", "Información obtenida sin irregularidades", ""),
    ("SOC_020", "Información obtenida: se pide una asamblea", "SOC_030"),
    ("SOC_020", "Información obtenida: acción contra los administradores", "SOC_070"),
    ("SOC_020", "Información negada: diligencia preliminar o demanda de exhibición (sin mediación)", "SOC_300"),
    ("SOC_030", "Asamblea convocada", "SOC_040"),
    ("SOC_030", "El directorio o el síndico no convocan en término", "SOC_035"),
    ("SOC_035", "Asamblea convocada por la DPPJ o por el juez", "SOC_040"),
    ("SOC_040", "Decisión impugnable, con pedido de suspensión", "SOC_050"),
    ("SOC_040", "Decisión impugnable, con pedido de suspensión", "SOC_100"),
    ("SOC_040", "Decisión impugnable, con pedido de suspensión", "SOC_070"),
    ("SOC_040", "Decisión impugnable, sin pedido de suspensión", "SOC_050"),
    ("SOC_040", "Decisión impugnable, sin pedido de suspensión", "SOC_070"),
    ("SOC_040", "La asamblea resolvió promover la acción de responsabilidad", "SOC_060"),
    ("SOC_040", "La asamblea resolvió la disolución", "SOC_600"),
    ("SOC_040", "Sin decisiones para impugnar", ""),
    ("SOC_050", "Demanda presentada en término o decisión revocada", ""),
    ("SOC_050", "Plazo vencido sin demanda: caducó la acción", ""),
    ("SOC_055", "Decisión de excluir, con pedido de suspensión", "SOC_105"),
    ("SOC_055", "Decisión de excluir, con pedido de suspensión", "SOC_070"),
    ("SOC_055", "Decisión de excluir, sin pedido de suspensión", "SOC_070"),
    ("SOC_055", "Plazo vencido sin demanda: caducó el derecho", ""),
    ("SOC_060", "Acción promovida por la sociedad o por el accionista", "SOC_070"),
    ("SOC_060", "Plazo vencido sin acción del accionista", ""),
    ("SOC_070", "Mediación cerrada sin acuerdo", "SOC_300"),
    ("SOC_070", "Acuerdo en la mediación", "SOC_900"),

    ("SOC_100", "Suspensión resuelta", ""),
    ("SOC_105", "Suspensión resuelta", ""),
    ("SOC_300", "Demanda de remoción proveída con pedido de intervención", "SOC_320"),
    ("SOC_300", "Demanda de remoción proveída con pedido de intervención", "SOC_950"),
    ("SOC_300", "Demanda de remoción proveída con pedido de intervención", "SOC_110"),
    ("SOC_110", "Intervención decretada", "SOC_120"),
    ("SOC_110", "Intervención decretada", "SOC_125"),
    ("SOC_110", "Intervención rechazada", "SOC_125"),
    ("SOC_120", "Interventor en funciones", "SOC_130"),
    ("SOC_125", "Apelación resuelta o no interpuesta", ""),
    ("SOC_130", "Prórroga concedida: el juez fija nuevo término", "SOC_120"),
    ("SOC_130", "Intervención cesada o levantada", ""),

    *CONTENCIOSA_TRANSICIONES,
    ("SOC_450", "Sentencia que anula la decisión, excluye al socio, remueve al administrador o disuelve la sociedad",
     "SOC_480"),
    ("SOC_450", "Condena dineraria firme (responsabilidad o parte del socio excluido)", "SOC_460"),
    ("SOC_460", "Liquidación aprobada y pagada", "SOC_960"),
    ("SOC_460", "Liquidación aprobada sin pago", "SOC_985"),
    ("SOC_900", "Acuerdo incumplido", "SOC_985"),
    ("SOC_480", "Sentencia inscripta", "SOC_960"),
    ("SOC_480", "Sentencia inscripta y declaró la disolución", "SOC_600"),
    ("SOC_480", "Sentencia inscripta y declaró la disolución", "SOC_960"),

    ("SOC_600", "Causal removida por los socios", ""),
    ("SOC_600", "Disolución resuelta e inscripta", "SOC_610"),
    ("SOC_600", "Los socios no reconocen la causal: disolución judicial", "SOC_070"),
    ("SOC_600", "Disolución por quiebra", "SOC_980"),
    ("SOC_610", "Liquidador designado por los socios o por el juez", "SOC_620"),
    ("SOC_620", "Inventario y balance presentados", "SOC_630"),
    ("SOC_620", "Inventario y balance presentados", "SOC_635"),
    ("SOC_630", "Informe presentado (se repite hasta el balance final)", ""),
    ("SOC_635", "Balance final comunicado a los socios", "SOC_640"),
    ("SOC_640", "Balance impugnado sin acuerdo", "SOC_645"),
    ("SOC_640", "Balance aprobado o sin impugnaciones", "SOC_650"),
    ("SOC_645", "Acción resuelta o plazo vencido", "SOC_650"),
    ("SOC_650", "Inscripción cancelada en una disolución judicial", "SOC_960"),
    ("SOC_650", "Inscripción cancelada en una liquidación sin juicio", "SOC_990"),
]

DUDAS = [
    ("D01", "Régimen y vigencia",
     "¿Sigue vigente al 13/11/2026 la Ley 19.550 con las reformas encontradas (Leyes 26.994 y 27.077, Decreto "
     "70/2023 y Resolución MJ 10/2024, que fijó en ARS 2.000.000.000 el capital del art. 299 inc. 2)? ¿Qué normas "
     "de la DPPJ rigen la convocatoria administrativa y las inscripciones (Decreto-Ley 8671/76 y disposiciones, a "
     "verificar)? ¿Se incluyen las SAS (Ley 27.349), donde la LGS es supletoria? Fuentes: InfoLEG (Ley 19.550, "
     "texto actualizado).", "Todos"),
    ("D02", "Mediación y caducidad de 3 meses",
     "La impugnación caduca a los 3 meses de clausurada la asamblea (art. 251) y la mediación obligatoria dura "
     "hasta 60 días corridos. El art. 40 de la Ley 13.951 habla de la prescripción; la caducidad, en principio, no "
     "se suspende (art. 2567 CCyC, a verificar). ¿La mediación suspende el plazo del art. 251? ¿Está la "
     "impugnación excluida de la mediación? Propuesta (lo más seguro): iniciar la mediación de inmediato y "
     "presentar la demanda antes de los 3 meses aunque la mediación no haya terminado. Vale también para los 90 "
     "días de la exclusión.", "SOC_050, SOC_055, SOC_070"),
    ("D03", "Cómputo de los plazos de la LGS",
     "Los plazos en días de la LGS (40 del art. 236, 90 del art. 91, 30 del art. 102 y del art. 103, 15 y 60 del "
     "art. 110) se cargaron como días corridos (art. 6 CCyC) y los de meses, por calendario. ¿Es correcto? ¿El "
     "plazo de 3 días hábiles del art. 238 es de días hábiles administrativos?", "SOC_030, SOC_055, SOC_610, "
     "SOC_620, SOC_640, SOC_645"),
    ("D04", "Tipo de proceso",
     "El art. 15 LGS manda el procedimiento sumario y la matriz usa la etapa contenciosa sumaria del CPCCBA. ¿Hay "
     "acciones societarias que tramitan por ordinario en PBA (por ejemplo, la de responsabilidad por su "
     "complejidad) o por sumarísimo? Propuesta: sumario, que tiene los plazos más cortos.", "SOC_300 a SOC_460"),
    ("D05", "Exclusión de socios",
     "¿En qué tipos sociales procede la exclusión del art. 91 (sociedades de personas, SRL; no en las sociedades "
     "por acciones, a verificar)? El plazo de 90 días corre desde que se conoció el hecho: ¿se carga como fecha "
     "del disparador ese conocimiento?", "SOC_055, SOC_105"),
    ("D06", "Intervención judicial",
     "¿Se aplican en forma conjunta los arts. 113 a 117 LGS y las normas de intervención judicial del CPCCBA "
     "(arts. 222 a 227, a verificar)? La matriz abre la intervención solo con la demanda de remoción, porque el "
     "art. 114 exige la acción promovida. ¿Algún juzgado la admite antes de la demanda?", "SOC_110, SOC_120, "
     "SOC_125, SOC_130"),
    ("D07", "Impugnación en la SRL",
     "Para las resoluciones de la SRL (art. 159), ¿se aplica el art. 251 con su plazo de 3 meses? ¿Desde cuándo "
     "corre si la resolución se tomó por consulta simultánea o declaración escrita?", "SOC_040, SOC_050"),
    ("D08", "Pérdida del capital",
     "El art. 59 de la Ley 27.541 (BO 23/12/2019) suspendió la causal de disolución del art. 94 inc. 5 hasta el fin "
     "del plazo de su art. 1. ¿Sigue suspendida al 13/11/2026? ¿Qué régimen tiene el art. 94 bis (reducción a uno "
     "del número de socios)?", "SOC_600"),
    ("D09", "Liquidación sin juicio",
     "La disolución y la liquidación muchas veces no pasan por un juzgado. ¿Se cargan en la app como expediente "
     "aunque no haya juicio, o solo cuando hay disolución judicial? El liquidador se cargó como DEMANDADA porque es "
     "un órgano de la sociedad: ¿es correcto?", "SOC_600 a SOC_650"),
    ("D10", "Derecho de información",
     "¿Cuál es la vía en PBA para el socio a quien le niegan la información: diligencia preliminar de exhibición "
     "(art. 323 CPCCBA, inciso a verificar) o demanda sumaria? En la sociedad anónima con sindicatura, ¿el "
     "accionista con menos del 2% tiene alguna vía?", "SOC_020"),
    ("D11", "Convocatoria administrativa o judicial",
     "¿Qué plazo tiene la DPPJ para convocar? ¿La convocatoria judicial tramita como sumarísimo o como medida "
     "urgente sin mediación? Propuesta: SIN_PLAZO y aclaración en el checklist.", "SOC_035"),
    ("D12", "Inscripción en la DPPJ",
     "¿Hay plazos para pedir la inscripción de la sentencia en la DPPJ? ¿Qué aranceles se pagan? Propuesta: "
     "SIN_PLAZO.", "SOC_480"),
    ("D13", "Etapa contenciosa común: audiencia preliminar",
     "La audiencia preliminar se cita como 'Programa de oralidad de la SCBA (a verificar)'. ¿Qué acordada la rige y "
     "en qué departamentos judiciales se aplica en el proceso sumario? ¿Qué norma del CPCCBA la prevé (art. 36 "
     "inc. 4, a verificar)? Vale para las matrices de ejecutivos y societarios.", "SOC_340"),
    ("D14", "Etapa contenciosa común: plazos del sumario",
     "Confirmar los plazos del sumario: contestación 10 días (art. 484), ampliación de prueba por hechos nuevos "
     "5 días, prueba en una audiencia (art. 487), sin alegatos (art. 493), sentencia en 30 días (art. 494, a "
     "verificar), agravios 5 días (art. 254) y caducidad de 3 meses (art. 310 inc. 2). El sumario procede hasta "
     "4500 Jus (art. 320): ¿y el resto de las acciones de la LGS?", "SOC_320, SOC_350, SOC_400, SOC_420, SOC_950"),
    ("D15", "Etapa contenciosa común: pericia",
     "El art. 473 CPCCBA prevé el traslado del dictamen pericial sin fijar plazo en el texto revisado. ¿Se usa el "
     "plazo general de 5 días (a verificar el artículo)? ¿Conviene un hito propio para la impugnación de la "
     "pericia? Propuesta: checklist en la audiencia de prueba.", "SOC_365"),
    ("D16", "Etapa contenciosa común: recursos",
     "Confirmar el valor mínimo del agravio para el recurso de inaplicabilidad de ley (art. 278) y el depósito "
     "previo del 10%, con mínimo de 100 y máximo de 500 Jus (art. 280). La Cámara no tiene plazo cargado para "
     "sentenciar (SIN_PLAZO): ¿corresponde el del art. 34 inc. 3 c o el del art. 266?", "SOC_430, SOC_440"),
    ("D17", "Cobro de la condena",
     "La condena dineraria no pagada termina en 'Sigue en la matriz de juicios ejecutivos', en el bloque de embargo "
     "y subasta (arts. 497 a 508 CPCCBA, a verificar). ¿Es correcto llevar la ejecución de sentencia al mismo "
     "bloque que la ejecución de la sentencia de remate?", "SOC_460, SOC_900, SOC_985"),
    ("D18", "Hitos que se abren dos veces",
     "La sentencia de disolución abre a la vez la liquidación (SOC_600) y los honorarios (SOC_960); la liquidación "
     "judicial vuelve a abrir los honorarios al final (SOC_650). ¿El motor admite abrir de nuevo un hito ya "
     "cerrado? Propuesta: sí, como nueva etapa regulatoria.", "SOC_480, SOC_650, SOC_960"),
    ("D19",) + DUDA_TRANSVERSAL,
]
