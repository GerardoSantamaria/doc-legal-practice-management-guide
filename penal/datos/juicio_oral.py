"""Juicio oral y público (JOR) — CPP PBA, Ley 11.922.

Derivación típica desde la IPP tras el auto o decreto firme de elevación a juicio.
"""
from comun import (
    CIERRA,
    CON_GRACIA,
    CON_VALOR_CERO,
    DUDA_REMITIR_TRANSVERSALES,
    ESTADOS,
    FUENTE_CPP,
    INSTRUCCIONES_ADICIONALES,
    NOTA_FUENTES,
    NOTA_SENSIBLES,
    REGIMEN_CPP,
    ROLES,
    ROLES_DESCRIPCION_PENAL,
    duda_federal,
    flujo,
    leyenda,
    nodos_libertad,
    nodos_recursos,
    numerar,
    ordenar,
    plazo_tipos,
    trans_libertad,
    trans_recursos,
)

P = "JOR"

# Subconjunto de libertad útil en el juicio con imputado detenido (sin la cadena de aprehensión de la IPP).
_LIBERTAD = {f"{P}_230", f"{P}_240", f"{P}_270", f"{P}_280", f"{P}_290"}

FLUJO = flujo(
    "Juicio oral y público (PBA)",
    REGIMEN_CPP + "; juicio por jurados (arts. 22 bis, 338 bis a 338 quáter, 371 bis a 371 quáter y 375 bis, "
    "Ley 14.543); Ley 14.967 (honorarios); Código Penal",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Arranca con la radicación tras la elevación desde la IPP.",
)

FASES = [
    "Radicación",
    "Preparación",
    "Jurados",
    "Debate",
    "Libertad",
    "Sentencia",
    "Recursos",
    "Cierre",
]

GRUPOS = [
    ("Radicación y órgano de juicio", ["Radicación"]),
    ("Preparación del juicio", ["Preparación"]),
    ("Juicio por jurados", ["Jurados"]),
    ("Debate", ["Debate"]),
    ("Situación de libertad en el juicio", ["Libertad"]),
    ("Veredicto y sentencia", ["Sentencia"]),
    ("Recursos", ["Recursos"]),
    ("Firmeza, cómputo y derivaciones", ["Cierre"]),
]

ROL_TEXTO = {
    "ACTORA": "Fiscal / particular damnificado",
    "DEMANDADA": "Imputado / defensa",
    "TRIBUNAL": "Juzgado Correccional, Tribunal en lo Criminal, jurados u órgano",
    "AMBAS": "Cualquiera de las partes",
}
ROLES_DESCRIPCION = ROLES_DESCRIPCION_PENAL

LEYENDA = leyenda(
    "celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima constituida en parte "
    "(ACTORA); naranja = imputado y defensa (DEMANDADA); gris = Juzgado Correccional, Tribunal en lo Criminal, "
    "jurados, Cámara, Casación u otros órganos, aclarado en el nombre del hito (TRIBUNAL); violeta = cualquiera "
    "de las partes (AMBAS).",
    "desde la radicación corren a la vez la preparación del juicio y el plazo de 6 meses para hacer el debate; "
    "con imputado detenido, también la excarcelación y el control del plazo máximo con detenido",
    adicionales=[
        ("**Órgano de juicio (arts. 22 y 22 bis):** Juzgado Correccional o Tribunal en lo Criminal "
         "(unipersonal si la pena máxima en abstracto no supera 15 años; colegiado para funcionarios o por "
         "opción de la defensa en el plazo del art. 336). Jurados si la máxima supera 15 años, salvo renuncia "
         "ratificada en ese mismo plazo."),
        ("**Derivación desde la IPP:** el expediente vinculado nace en la radicación tras el auto o decreto "
         "firme de elevación; no se copian relatos ni datos sensibles."),
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "CORRIDOS": (
        "plazos del juicio (art. 139): citación a juicio 10 días (338), fundamentos del veredicto y la sentencia "
        "5 días (374), apelación de la sentencia correccional 20 días (441), casación 20 días (451), reposición 3 "
        "días, excarcelación 5 días (174), honorarios 5 días (Ley 14.967)."
    ),
    "HABILES_JUDICIALES": "recursos extraordinarios ante la SCBA: 10 días hábiles (art. 483).",
    "MESES": "plazo para realizar el debate: 6 meses desde la radicación, prorrogable una vez (art. 339).",
    "ANIOS": "duración máxima del proceso con detenido: 2 años (art. 141).",
    "FECHA_FIJADA": (
        "audiencia preliminar, fecha del debate, audiencia de selección del jurado y actos con día y hora fijados "
        "por el tribunal."
    ),
    "SIN_PLAZO": (
        "radicación, integración del órgano, nulidades, instrucción suplementaria, pasos del debate, deliberación, "
        "veredicto, cesura, absolución o condena, firmeza y cómputo."
    ),
    "HORAS": "no se usa por defecto (la declaración con detenido se controla en la IPP).",
    "HABILES_ADMINISTRATIVOS": "no se usa.",
    "ANTICIPACION_HABILES_JUDICIALES": (
        "no se modela acá; el tope de 30 días antes del debate para el abreviado (art. 397) se controla en la "
        "matriz de juicio abreviado."
    ),
})

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS_PROPIOS = [
    (f"{P}_010", "Radicación", "Radicación tras la elevación a juicio", "TRIBUNAL",
     "Auto o decreto firme de elevación a juicio (derivación desde la IPP)", 0, "SIN_PLAZO", "NO",
     "Arts. 337 y 338 CPP PBA", "SI", "NO",
     ["Crear el expediente vinculado desde la matriz de investigación (IPP_950)",
      "Controlar el órgano de destino: Juzgado Correccional o Tribunal en lo Criminal",
      "La prescripción de la acción sigue corriendo; la citación a juicio la interrumpe (art. 67 CP)",
      "Si hay imputado detenido, abrir en paralelo los hitos de libertad",
      "No copiar relatos ni datos sensibles de víctimas o detenidos"],
     ["Auto o decreto de elevación", "Constancia de radicación"]),
    (f"{P}_020", "Radicación", "Integración del órgano de juicio", "TRIBUNAL",
     "Radicación de la causa elevada", 0, "SIN_PLAZO", "NO",
     "Arts. 22, 22 bis y 338 CPP PBA", "NO", "NO",
     ["Tribunal unipersonal si la pena máxima en abstracto no supera 15 años (art. 22)",
      "Colegiado para funcionarios, o si la defensa optó en el plazo del art. 336 durante la IPP (art. 22)",
      "Jurados si la máxima supera 15 años y no hubo renuncia ratificada en el plazo del art. 336 (art. 22 bis)",
      "La integración se notifica a todas las partes (art. 338)"],
     ["Resolución de integración del tribunal"]),
    (f"{P}_040", "Radicación", "Juicio por jurados: sorteo del juez y lista de jurados", "TRIBUNAL",
     "Integración del órgano como tribunal de jurados", 0, "SIN_PLAZO", "NO",
     "Arts. 22 bis, 338 y 338 bis a 338 ter CPP PBA", "NO", "NO",
     ["Se sortea el juez que dirige el debate (art. 338)",
      "Firme la elevación, ya no se puede renunciar al jurado (art. 22 bis)",
      "Con varios imputados, si uno renunció en plazo, el juicio es ante tribunal técnico (art. 22 bis)",
      "El jurado se integra por mitades de hombres y mujeres, con suplentes (art. 338 bis)"],
     ["Constancia de sorteo del juez"]),
    (f"{P}_100", "Preparación", "Citación a juicio: recusaciones y ofrecimiento de prueba (10 días)", "AMBAS",
     "Notificación de la integración del tribunal y de la citación a juicio", 10, "CORRIDOS", "NO",
     "Arts. 78 y 338 CPP PBA", "NO", "NO",
     ["Plazo individual de 10 días para recusar y ofrecer la prueba del debate (art. 338)",
      "En el mismo acto, decir si se pide audiencia preliminar; con jurados es obligatoria (art. 338)",
      "El particular damnificado puede constituirse hasta 30 días antes de la fecha del debate (art. 78)",
      "Notificar a la víctima la fecha del debate y sus derechos (art. 83, texto Ley 15.232)",
      "Plazo continuo (art. 139); sin gracia"],
     ["Escrito de ofrecimiento de prueba", "Escrito de recusación (si corresponde)"]),
    (f"{P}_120", "Preparación", "Audiencia preliminar", "TRIBUNAL",
     "Fecha y hora fijadas para la audiencia preliminar", 0, "FECHA_FIJADA", "NO",
     "Art. 338 CPP PBA", "NO", "NO",
     ["Se fija una vez firme la integración del tribunal, en el plazo más breve posible (art. 338)",
      "Se tratan la prueba del debate, su duración probable, nulidades e instrucción suplementaria (art. 338)",
      "Hasta 30 días antes del debate se puede acordar el juicio abreviado (art. 397)",
      "Controlar la presencia de las partes y del imputado si está detenido"],
     ["Acta de audiencia preliminar"]),
    (f"{P}_130", "Preparación", "Planteo de nulidades", "AMBAS",
     "Audiencia preliminar o acto que habilita el planteo", 0, "SIN_PLAZO", "NO",
     "Arts. 201 y ss. y 338 CPP PBA", "NO", "NO",
     ["Plantear nulidades en la oportunidad legal",
      "Si se rechazan sin sustanciación, evaluar reposición",
      "No registrar en la app el contenido sensible de la actuación impugnada"],
     ["Escrito o acta de planteo de nulidad"]),
    (f"{P}_140", "Preparación", "Instrucción suplementaria", "TRIBUNAL",
     "Resolución que ordena instrucción suplementaria", 0, "SIN_PLAZO", "NO",
     "Arts. 338 y 339 CPP PBA", "NO", "NO",
     ["Controlar el objeto, el plazo que fije el tribunal y quién produce la medida",
      "Si impide hacer el debate en 6 meses, el plazo del art. 339 se puede prorrogar por única vez",
      "Al cumplirse, volver a fijar o confirmar la fecha del debate"],
     ["Resolución de instrucción suplementaria"]),
    (f"{P}_150", "Preparación", "Fecha del debate fijada", "TRIBUNAL",
     "Fecha y hora fijadas para el debate", 0, "FECHA_FIJADA", "NO",
     "Arts. 339 y 397 CPP PBA", "NO", "NO",
     ["La Secretaría de Gestión Administrativa fija día, hora y lugar del debate (art. 339)",
      "La notificación de testigos y peritos está a cargo de la parte que los propuso (art. 339)",
      "El acuerdo de abreviado se puede presentar hasta 30 días antes de esta fecha (art. 397)",
      "Si hay imputado detenido, controlar el traslado"],
     ["Notificación de la fecha del debate"]),
    (f"{P}_160", "Preparación", "Plazo para realizar el debate (6 meses)", "TRIBUNAL",
     "Radicación de la causa en el órgano de juicio", 6, "MESES", "NO",
     "Art. 339 CPP PBA", "NO", "NO",
     ["El debate debe hacerse dentro de los 6 meses de radicada la causa (art. 339)",
      "Se puede prorrogar por única vez si una instrucción suplementaria impide cumplirlo",
      "Si no se hace a tiempo, el órgano pierde la competencia y se comunica a la SCBA (art. 339)"],
     ["Cómputo del plazo del art. 339"]),
    (f"{P}_310", "Jurados", "Audiencia de selección del jurado", "TRIBUNAL",
     "Día fijado para comenzar el juicio", 0, "FECHA_FIJADA", "NO",
     "Art. 338 quáter CPP PBA", "NO", "NO",
     ["Se celebra el mismo día fijado para el juicio, con presencia obligatoria del juez y las partes",
      "Impedimentos, excusaciones y recusaciones de los ciudadanos convocados (art. 338 quáter)",
      "No registrar identidades de los jurados más allá de lo necesario para el acto"],
     ["Acta de selección del jurado"]),
    (f"{P}_320", "Jurados", "Audiencia de instrucciones al jurado", "TRIBUNAL",
     "Clausura del debate en el juicio por jurados", 0, "SIN_PLAZO", "NO",
     "Art. 371 bis CPP PBA", "NO", "NO",
     ["Sin el jurado en la sala, las partes proponen instrucciones y plantean objeciones (art. 371 bis)",
      "Las propuestas de instrucciones se anticipan por escrito antes del juicio",
      "Dejar constancia de las disidencias para impugnar la sentencia; sin registro, hay nulidad"],
     ["Propuesta de instrucciones", "Acta de la audiencia"]),
    (f"{P}_330", "Jurados", "Explicación de las instrucciones y deliberación del jurado", "TRIBUNAL",
     "Fin de la audiencia de instrucciones", 0, "SIN_PLAZO", "NO",
     "Art. 371 ter CPP PBA", "NO", "NO",
     ["El juez explica las instrucciones y las normas de la deliberación, que es secreta y continua",
      "No hay plazo perentorio para el veredicto",
      "Controlar las comunicaciones con el jurado y los pedidos de aclaración"],
     []),
    (f"{P}_340", "Jurados", "Veredicto del jurado", "TRIBUNAL",
     "Pronunciamiento del veredicto en la sala", 0, "SIN_PLAZO", "NO",
     "Art. 371 quáter CPP PBA", "NO", "NO",
     ["Culpabilidad: al menos 10 votos; unanimidad si el delito tiene pena perpetua",
      "El veredicto es irrecurrible; la absolución por no culpabilidad también (art. 371 quáter inc. 7)",
      "No culpabilidad: libertad inmediata y cese de las restricciones (art. 371 quáter inc. 3)",
      "Registrar solo el resultado, sin datos de los jurados"],
     ["Acta de veredicto"]),
    (f"{P}_345", "Jurados", "Jurado estancado", "TRIBUNAL",
     "Declaración de jurado estancado (más de 8 votos sin llegar al mínimo)", 0, "SIN_PLAZO", "NO",
     "Art. 371 quáter inc. 2 CPP PBA", "NO", "NO",
     ["El juez pregunta al fiscal si sigue con la acusación",
      "Si no sigue, se absuelve, salvo que el particular damnificado sostenga la acusación",
      "Si sigue, el jurado vuelve a deliberar; si persiste estancado, se disuelve y hay nuevo juicio con otro jurado",
      "Si el nuevo jurado también se estanca, el veredicto es de no culpabilidad"],
     ["Acta de la audiencia"]),
    (f"{P}_400", "Debate", "Apertura del debate y cuestiones preliminares", "TRIBUNAL",
     "Fecha y hora del debate", 0, "FECHA_FIJADA", "NO",
     "Arts. 342, 347, 354 y 356 CPP PBA", "NO", "NO",
     ["El debate es oral y público; puede hacerse a puertas cerradas para proteger a la víctima o a testigos (art. 342)",
      "La asistencia del fiscal y del defensor es obligatoria (art. 347)",
      "Cuestiones preliminares en un solo acto (art. 356)",
      "Durante el juicio solo procede reposición, que vale como protesta de recurrir (art. 429)"],
     ["Acta de apertura del debate"]),
    (f"{P}_410", "Debate", "Declaración del imputado en el debate", "DEMANDADA",
     "Apertura del debate u oportunidad de declarar", 0, "SIN_PLAZO", "NO",
     "Art. 358 CPP PBA", "NO", "NO",
     ["El imputado puede declarar todas las veces que quiera sobre su defensa (art. 358)",
      "Si declara, queda sometido al interrogatorio de su defensor y de las partes contrarias (art. 358)",
      "Asesorar sobre declarar o abstenerse; no registrar en la app el contenido de la declaración"],
     ["Acta de declaración en el debate"]),
    (f"{P}_420", "Debate", "Producción de prueba en el debate", "AMBAS",
     "Apertura del debate o admisión de prueba", 0, "SIN_PLAZO", "NO",
     "Arts. 365 y 366 CPP PBA", "NO", "NO",
     ["La prueba se produce oralmente (art. 365)",
      "Las actuaciones de la IPP no pueden fundar la condena, salvo las excepciones de lectura (art. 366)",
      "Víctimas y testigos vulnerables: medidas de protección (art. 83 CPP PBA)"],
     ["Actas de audiencia"]),
    (f"{P}_430", "Debate", "Ampliación del requerimiento fiscal", "ACTORA",
     "Hecho que integra el delito continuado o circunstancia agravante surgida en el debate", 0, "SIN_PLAZO",
     "NO",
     "Art. 359 CPP PBA", "NO", "NO",
     ["Controlar el hecho nuevo, la calificación y el derecho de defensa",
      "Pedir la suspensión o prueba adicional si hace falta",
      "Impugnar la ampliación inadmisible"],
     ["Acta o requerimiento de ampliación"]),
    (f"{P}_440", "Debate", "Discusión final (alegatos)", "AMBAS",
     "Cierre de la recepción de la prueba", 0, "SIN_PLAZO", "NO",
     "Art. 368 CPP PBA (texto Ley 15.232)", "NO", "NO",
     ["Orden: actor civil, fiscal, particular damnificado, civilmente demandado, asegurador y defensores (art. 368)",
      "No se pueden leer memoriales; réplica limitada a argumentos no discutidos",
      "En la réplica, la última palabra corresponde al defensor"],
     ["Notas de alegato"]),
    (f"{P}_450", "Debate", "Última palabra del imputado", "DEMANDADA",
     "Conclusión de los alegatos y réplicas", 0, "SIN_PLAZO", "NO",
     "Art. 368 CPP PBA", "NO", "NO",
     ["El presidente pregunta al imputado, bajo sanción de nulidad, si tiene algo que manifestar (art. 368)",
      "Después se cierra el debate",
      "No registrar el contenido en la app"],
     ["Acta de última palabra"]),
    (f"{P}_460", "Debate", "Clausura del debate", "TRIBUNAL",
     "Última palabra del imputado", 0, "SIN_PLAZO", "NO",
     "Arts. 368, 371 y 371 bis CPP PBA", "NO", "NO",
     ["Tribunal técnico: pasa a deliberar (art. 371)",
      "Jurados: sigue la audiencia de instrucciones (art. 371 bis)"],
     ["Acta de clausura"]),
    (f"{P}_500", "Sentencia", "Veredicto del tribunal y lectura de fundamentos (5 días)", "TRIBUNAL",
     "Audiencia de lectura del veredicto (art. 374)", 5, "CORRIDOS", "NO",
     "Arts. 371, 373 y 374 CPP PBA", "NO", "NO",
     ["El tribunal puede anticipar el carácter absolutorio o condenatorio del veredicto en audiencia (art. 374)",
      "La lectura de los fundamentos no puede exceder 5 días; 7 si hay acción civil (art. 374)",
      "La lectura vale como notificación para quienes intervinieron en el debate (art. 374)",
      "Si el hecho resulta distinto al de la acusación, se procede según el art. 359"],
     ["Veredicto y sentencia"]),
    (f"{P}_510", "Sentencia", "Cesura del juicio (determinación de la pena)", "TRIBUNAL",
     "Veredicto de culpabilidad o resolución que difiere la pena", 0, "SIN_PLAZO", "NO",
     "Arts. 372 y 375 bis CPP PBA", "NO", "NO",
     ["Tribunal técnico: puede diferir la pena hasta 1 mes desde la notificación (art. 372)",
      "Jurados: la cesura es obligatoria y la hace el juez que presidió; también en no culpabilidad por inimputabilidad",
      "Jurados: las partes pueden ofrecer prueba sobre la pena hasta 5 días después del veredicto (art. 372)",
      "El juez puede anular un veredicto de culpabilidad manifiestamente contrario a la prueba y ordenar nuevo juicio; es irrecurrible (art. 375 bis)"],
     ["Acta de cesura"]),
    (f"{P}_520", "Sentencia", "Absolución", "TRIBUNAL",
     "Sentencia absolutoria o veredicto de no culpabilidad", 0, "SIN_PLAZO", "NO",
     "Arts. 371 quáter, 441, 452 y 499 CPP PBA", "NO", "NO",
     ["Si hay detenido, libertad inmediata aunque se recurra (arts. 371 quáter inc. 3 y 499)",
      "Jurados: la absolución por no culpabilidad es irrecurrible",
      "Tribunal técnico: la acusación puede recurrir si pidió la condena (arts. 441 y 452)",
      "Costas: toda resolución que pone fin a la causa las resuelve (arts. 530 y 531)"],
     ["Sentencia absolutoria"]),
    (f"{P}_530", "Sentencia", "Condena", "TRIBUNAL",
     "Sentencia condenatoria", 0, "SIN_PLAZO", "NO",
     "Arts. 375, 375 bis y 530 CPP PBA", "NO", "NO",
     ["Controlar pena, accesorias, costas y cómputo provisorio",
      "Interrumpe la prescripción aunque no esté firme (art. 67 CP)",
      "Jurados: con pena de cumplimiento efectivo, el juez puede agravar la coerción aunque no esté firme (art. 375 bis)",
      "Recurso: casación en lo criminal y jurados, apelación en lo correccional (20 días en ambos casos)"],
     ["Sentencia condenatoria"]),
    (f"{P}_550", "Sentencia", "Regulación e impugnación de honorarios (Ley 14.967)", "AMBAS",
     "Notificación de la regulación de honorarios", 5, "CORRIDOS", "NO",
     "Arts. 9 y 57 Ley 14.967 (días corridos o hábiles: ver duda transversal en IPP)", "NO", "NO",
     ["Impugnar en 5 días fundando en el mismo escrito (art. 57)",
      "Verificar los mínimos arancelarios del fuero penal",
      "Si no hubo regulación, cerrar el hito",
      "Propuesta de la app: 5 CORRIDOS sin gracia"],
     ["Escrito de impugnación de honorarios"]),
    (f"{P}_600", "Recursos", "Decisión de recurrir la sentencia", "AMBAS",
     "Notificación de la sentencia definitiva", 0, "SIN_PLAZO", "NO",
     "Arts. 20, 21 inc. 4, 441 y 450 CPP PBA", "NO", "NO",
     ["Tribunal en lo Criminal y jurados (condena): casación ante el Tribunal de Casación Penal",
      "Juzgado Correccional: apelación ante la Cámara de Apelación y Garantías",
      "El plazo es de 20 días en ambos casos (arts. 441 y 451)",
      "Feria: se suspende el plazo de impugnación de la sentencia definitiva (art. 139), salvo flagrancia"],
     []),
    (f"{P}_900", "Cierre", "Firmeza de la sentencia", "AMBAS",
     "Vencimiento de los plazos de recurso o resolución que agota la vía", 0, "SIN_PLAZO", "NO",
     "Arts. 421 y ss. CPP PBA", "NO", "NO",
     ["Verificar que no queden recursos ordinarios ni extraordinarios pendientes",
      "En condena firme, abrir el cómputo y la derivación a ejecución",
      "En absolución o sobreseimiento firmes, cerrar"],
     ["Constancia de firmeza"]),
    (f"{P}_910", "Cierre", "Cómputo de la pena", "TRIBUNAL",
     "Condena firme", 0, "SIN_PLAZO", "NO",
     "Art. 500 CPP PBA (texto Ley 15.232)", "NO", "NO",
     ["El juez o tribunal que dictó la sentencia hace practicar el cómputo por Secretaría (art. 500)",
      "Controlar detención sufrida, unificación y accesorias",
      "No registrar datos sensibles del interno más allá del cómputo"],
     ["Cómputo de pena"]),
    (f"{P}_955", "Cierre", "Sigue en la matriz de juicio abreviado", "AMBAS",
     "Acuerdo de juicio abreviado presentado hasta 30 días antes del debate", 0, "SIN_PLAZO", "NO",
     "Arts. 395 a 397 CPP PBA", "NO", "SI",
     ["Crear el expediente vinculado con la matriz de juicio abreviado (JAB)",
      "Si el acuerdo se desestima, el expediente vuelve a esta matriz (JAB_320)"],
     ["Acuerdo de abreviado"]),
    (f"{P}_960", "Cierre", "Sigue en la matriz de hábeas corpus", "DEMANDADA",
     "Decisión de interponer hábeas corpus durante el juicio", 0, "SIN_PLAZO", "NO",
     "Arts. 164 y 405 a 420 CPP PBA", "NO", "SI",
     ["Crear el expediente vinculado con la matriz de hábeas corpus (HCO); el juicio sigue (ver duda de producto)",
      "Contra la prisión preventiva, el hábeas procede hasta el inicio del debate (art. 405)",
      "No copiar el relato de la detención en celdas de texto libre"],
     ["Copia de la resolución de coerción impugnada"]),
    (f"{P}_970", "Cierre", "Sigue en ejecución penal", "AMBAS",
     "Condena firme con cómputo practicado", 0, "SIN_PLAZO", "NO",
     "Ley 12.256 (ejecución penal; fuera de V1)", "NO", "SI",
     ["Crear el expediente vinculado de ejecución",
      "Trasladar solo metadatos de la condena y del cómputo, sin datos sensibles innecesarios"],
     ["Sentencia firme", "Cómputo"]),
    (f"{P}_980", "Cierre", "Absolución o sobreseimiento firme", "AMBAS",
     "Absolución firme, sobreseimiento en el juicio o extinción", 0, "SIN_PLAZO", "NO",
     "Arts. 341 y 499 CPP PBA; art. 59 Código Penal", "NO", "SI",
     ["Verificar que no queden honorarios ni recursos pendientes",
      "Devolver documentación original al cliente",
      "No conservar relatos ni datos sensibles innecesarios"],
     []),
]

TRANS_PROPIAS = [
    # Radicación
    (f"{P}_010", "Imputado en libertad", f"{P}_020"),
    (f"{P}_010", "Imputado en libertad", f"{P}_160"),
    (f"{P}_010", "Imputado detenido", f"{P}_020"),
    (f"{P}_010", "Imputado detenido", f"{P}_160"),
    (f"{P}_010", "Imputado detenido", f"{P}_230"),
    (f"{P}_010", "Imputado detenido", f"{P}_290"),
    (f"{P}_020", "Tribunal técnico (Correccional o Criminal)", f"{P}_100"),
    (f"{P}_020", "Tribunal de jurados", f"{P}_040"),
    (f"{P}_040", "Juez sorteado y tribunal notificado", f"{P}_100"),
    # Preparación
    (f"{P}_100", "Se pidió audiencia preliminar, o hay jurados", f"{P}_120"),
    (f"{P}_100", "Sin audiencia preliminar: se fija el debate", f"{P}_150"),
    (f"{P}_120", "Planteos de nulidad", f"{P}_130"),
    (f"{P}_120", "Se ordena instrucción suplementaria", f"{P}_140"),
    (f"{P}_120", "Se fija la fecha del debate", f"{P}_150"),
    (f"{P}_120", "Acuerdo de juicio abreviado", f"{P}_955"),
    (f"{P}_130", "Nulidad resuelta: se fija el debate", f"{P}_150"),
    (f"{P}_130", "Rechazo sin sustanciación: reposición", f"{P}_800"),
    (f"{P}_130", "Rechazo sin sustanciación: reposición", f"{P}_150"),
    (f"{P}_130", "Nulidad o excepción que termina el juicio (sobreseimiento, art. 341)", f"{P}_900"),
    (f"{P}_140", "Instrucción cumplida: nueva audiencia preliminar", f"{P}_120"),
    (f"{P}_140", "Instrucción cumplida: se fija el debate", f"{P}_150"),
    (f"{P}_150", "Tribunal técnico: llega la fecha del debate", f"{P}_400"),
    (f"{P}_150", "Jurados: llega la fecha del juicio", f"{P}_310"),
    (f"{P}_150", "Acuerdo de juicio abreviado hasta 30 días antes", f"{P}_955"),
    (f"{P}_160", "Debate iniciado dentro del plazo", CIERRA),
    (f"{P}_160", "Vence sin debate: pérdida de competencia y comunicación a la SCBA", CIERRA),
    # Jurados
    (f"{P}_310", "Jurado integrado: apertura del debate", f"{P}_400"),
    (f"{P}_320", "Instrucciones decididas", f"{P}_330"),
    (f"{P}_330", "El jurado llega a un veredicto", f"{P}_340"),
    (f"{P}_330", "El jurado se declara estancado", f"{P}_345"),
    (f"{P}_340", "No culpabilidad: absolución irrecurrible", f"{P}_520"),
    (f"{P}_340", "Culpabilidad o no culpabilidad por inimputabilidad: cesura obligatoria", f"{P}_510"),
    (f"{P}_345", "El fiscal desiste y no acusa el particular damnificado: absolución", f"{P}_520"),
    (f"{P}_345", "Sigue la acusación: nueva deliberación", f"{P}_330"),
    (f"{P}_345", "Persiste el estancamiento: nuevo juicio con otro jurado", f"{P}_310"),
    # Debate
    (f"{P}_400", "Cuestiones preliminares resueltas", f"{P}_410"),
    (f"{P}_410", "Declaración recibida o abstención", f"{P}_420"),
    (f"{P}_420", "Surge un hecho o agravante nuevo: ampliación", f"{P}_430"),
    (f"{P}_420", "Prueba concluida: discusión final", f"{P}_440"),
    (f"{P}_430", "Ampliación admitida o rechazada: sigue la prueba", f"{P}_420"),
    (f"{P}_440", "Alegatos y réplicas concluidos", f"{P}_450"),
    (f"{P}_450", "Última palabra ejercida o no", f"{P}_460"),
    (f"{P}_460", "Tribunal técnico: deliberación y veredicto", f"{P}_500"),
    (f"{P}_460", "Jurados: audiencia de instrucciones", f"{P}_320"),
    # Sentencia
    (f"{P}_500", "Veredicto absolutorio", f"{P}_520"),
    (f"{P}_500", "Veredicto condenatorio: sentencia", f"{P}_530"),
    (f"{P}_500", "Veredicto condenatorio: se difiere la pena (cesura)", f"{P}_510"),
    (f"{P}_510", "Pena o medida de seguridad determinada", f"{P}_530"),
    (f"{P}_510", "El juez anula el veredicto de culpabilidad: nuevo juicio con otro jurado", f"{P}_310"),
    (f"{P}_520", "Sentencia notificada", f"{P}_600"),
    (f"{P}_520", "Sentencia notificada", f"{P}_550"),
    (f"{P}_530", "Sentencia notificada", f"{P}_600"),
    (f"{P}_530", "Sentencia notificada", f"{P}_550"),
    (f"{P}_550", "Honorarios firmes, impugnación resuelta o sin regulación", CIERRA),
    # Recursos
    (f"{P}_600", "Tribunal en lo Criminal o jurados: casación", f"{P}_820"),
    (f"{P}_600", "Juzgado Correccional: apelación", f"{P}_810"),
    (f"{P}_600", "No se recurre o la sentencia es irrecurrible", f"{P}_900"),
    # Cierre
    (f"{P}_900", "Absolución o sobreseimiento firme", f"{P}_980"),
    (f"{P}_900", "Condena firme: cómputo", f"{P}_910"),
    (f"{P}_910", "Cómputo practicado", f"{P}_970"),
]

NODOS, TRANSICIONES = ordenar(
    NODOS_PROPIOS + [n for n in nodos_libertad(P) if n[0] in _LIBERTAD] + nodos_recursos(P),
    TRANS_PROPIAS + trans_libertad(P, _LIBERTAD) + trans_recursos(P, f"{P}_900", reenvio=f"{P}_150"),
)

DUDAS_PROPIAS = [
    ("Citación a juicio de 10 días (art. 338)",
     "Verificado: plazo individual de 10 días desde la notificación de la integración para recusar y ofrecer "
     "prueba; en el mismo acto se pide audiencia preliminar (obligatoria con jurados). ¿El plazo corre desde la "
     "notificación a cada parte por separado? Propuesta: 10 CORRIDOS desde la notificación a la parte que "
     "representa el abogado. " + FUENTE_CPP,
     f"{P}_100"),
    ("Plazo para realizar el debate (art. 339)",
     "El debate debe hacerse dentro de 6 meses de la radicación, prorrogable una vez por instrucción "
     "suplementaria; si no, el órgano pierde la competencia. ¿Qué pasa después con la causa (nuevo tribunal, "
     "nuevo plazo)? ¿La app debe alertar a la defensa como oportunidad? Propuesta: 6 MESES en JOR_160 como "
     "camino paralelo. " + FUENTE_CPP,
     f"{P}_160"),
    ("Instrucción suplementaria",
     "¿Hay plazo máximo para cumplir la instrucción suplementaria? ¿Quién la produce? Propuesta: hito sin plazo "
     "con carga manual; prorroga una vez el plazo de 6 meses (art. 339). Norma a verificar.",
     f"{P}_140"),
    ("Integración del órgano sin plazos propios en el juicio",
     "El borrador anterior tenía hitos de 15 días en el juicio para optar por tribunal colegiado y renunciar al "
     "jurado. Verificado en los arts. 22 y 22 bis: ambas cosas se hacen en el plazo del art. 336, durante la IPP, "
     "y firme la elevación ya no se puede renunciar al jurado. Se quitaron esos hitos. ¿Hay algún caso en que la "
     "opción se ejerza en el juicio (por ejemplo, cambio de calificación)? " + FUENTE_CPP,
     f"{P}_020, {P}_040"),
    ("Juicio por jurados: plazos de la selección y de las instrucciones",
     "La selección es el día fijado para el juicio (art. 338 quáter) y las instrucciones se discuten al cerrar el "
     "debate (art. 371 bis). Ninguna tiene plazo perentorio. ¿Hace falta un hito para la presentación "
     "anticipada y por escrito de las propuestas de instrucciones? Propuesta: checklist en JOR_320. "
     + FUENTE_CPP,
     f"{P}_310, {P}_320, {P}_330"),
    ("Fundamentos del veredicto en 5 días (art. 374)",
     "Verificado: hasta 5 días (7 con acción civil). ¿Los días se cuentan desde la audiencia de lectura del "
     "veredicto? ¿Se suspenden en feria? Propuesta: 5 CORRIDOS desde la lectura del veredicto; el abogado cambia "
     "a 7 si hay acción civil. " + FUENTE_CPP,
     f"{P}_500"),
    ("Cesura del juicio (art. 372)",
     "Verificado: sin jurados es facultativa y puede diferir la pena hasta 1 mes; con jurados es obligatoria y "
     "las partes ofrecen prueba hasta 5 días después del veredicto. ¿Conviene modelar esos plazos (1 MESES y "
     "5 CORRIDOS) como hitos propios? Propuesta: checklist en JOR_510 hasta validar. " + FUENTE_CPP,
     f"{P}_510"),
    ("Ampliación del requerimiento (art. 359)",
     "¿Qué límites y formalidades tiene la ampliación? ¿Obliga a suspender el debate o a reabrir la prueba? "
     "Propuesta: hito sin plazo con checklist de defensa. " + FUENTE_CPP,
     f"{P}_430"),
    ("Recurso contra la sentencia: casación o apelación (20 días)",
     "Verificado: en lo criminal y en jurados (condena) hay casación (arts. 20 y 450); en lo correccional, "
     "apelación ante la Cámara (art. 21 inc. 4). Ambos plazos son de 20 días (arts. 441 y 451). ¿Después de la "
     "Cámara, en correccional, se va directo a los recursos extraordinarios ante la SCBA? Propuesta: sí, como "
     "salida de JOR_810. " + FUENTE_CPP,
     f"{P}_600, {P}_810, {P}_820"),
    ("Manifestación de recurrir en casación (7 días)",
     "Art. 451: dentro de los primeros 7 días del plazo hay que manifestar la intención de recurrir; si no, la "
     "sentencia queda firme para quien omitió. ¿Hace falta un hito propio de 7 CORRIDOS con alerta? Propuesta: "
     "sí en una próxima versión; por ahora, checklist en JOR_820. " + FUENTE_CPP,
     f"{P}_820"),
    ("Feria y recursos contra la sentencia",
     "Art. 139: la feria suspende la impugnación de la sentencia definitiva (salvo flagrancia). ¿El motor puede "
     "marcar JOR_810 y JOR_820 como 'suspende en feria'? Propuesta: sí; registrar el requerimiento al motor. "
     + FUENTE_CPP,
     f"{P}_810, {P}_820"),
    ("Recursos extraordinarios SCBA y federal",
     "Verificado: los recursos ante la SCBA se interponen en 10 días hábiles (art. 483). ¿Se cuentan con el "
     "calendario judicial PBA? Para el recurso federal (art. 257 CPCCN, 10 días hábiles), ¿qué calendario usa "
     "la app? Propuesta: JOR_830 en HABILES_JUDICIALES; JOR_840 sin plazo con carga manual. " + FUENTE_CPP,
     f"{P}_830, {P}_840"),
    ("Libertad durante el juicio",
     "Con imputado detenido, ¿bastan los hitos de excarcelación, alternativas y control del plazo máximo con "
     "detenido, o hace falta reabrir la cadena de aprehensión de la IPP? Propuesta: JOR_230/240/270/280/290 y "
     "hábeas. " + FUENTE_CPP,
     f"{P}_230, {P}_240, {P}_270, {P}_280, {P}_290"),
    ("Cómputo de pena y derivación a ejecución",
     "Art. 500: el juez o tribunal que dictó la sentencia hace practicar el cómputo. ¿Hay plazo? ¿La app solo "
     "alerta y deriva a 'Sigue en ejecución penal'? Propuesta: hito sin plazo y final JOR_970. " + FUENTE_CPP,
     f"{P}_900, {P}_910, {P}_970"),
    ("Honorarios en el juicio oral",
     "¿Se regulan con la sentencia o al quedar firme? ¿El plazo de 5 días del art. 57 Ley 14.967 es corrido "
     "(CPP) o hábil (CPCCBA)? Propuesta: 5 CORRIDOS sin gracia (misma duda transversal de la IPP).",
     f"{P}_550"),
    ("Publicidad del debate y causa reservada",
     "Art. 342: el debate puede hacerse a puertas cerradas para proteger la intimidad de la víctima o testigos. "
     "¿Cómo se marca en la app sin filtrar datos sensibles? Propuesta: checklist en la apertura; sin registrar "
     "identidades protegidas. " + FUENTE_CPP,
     f"{P}_400"),
    ("Derivación al abreviado desde el juicio",
     "Art. 397: el acuerdo se puede presentar hasta 30 días antes del debate. La matriz deriva a JAB desde la "
     "audiencia preliminar y desde la fecha del debate. Si se desestima, ¿el juicio sigue con la misma fecha? "
     "Propuesta: volver a esta matriz desde JAB_320. " + FUENTE_CPP,
     f"{P}_120, {P}_150, {P}_955"),
    duda_federal(
        "el juicio oral",
        "En el CPPF hay control de la acusación en audiencia y juicio ante tribunal unipersonal o colegiado; en el "
        "CPPN el juicio es ante el Tribunal Oral Federal, con recurso ante la Cámara Federal de Casación Penal.",
        f"{P}_010, {P}_600",
    ),
]

DUDAS = numerar(DUDAS_PROPIAS + [DUDA_REMITIR_TRANSVERSALES])
