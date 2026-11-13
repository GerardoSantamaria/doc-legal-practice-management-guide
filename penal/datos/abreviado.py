"""Juicio abreviado (JAB) — CPP PBA, Ley 11.922, arts. 395 a 403."""
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
    nodos_recursos,
    numerar,
    ordenar,
    plazo_tipos,
    trans_recursos,
)

P = "JAB"

FLUJO = flujo(
    "Juicio abreviado (PBA)",
    REGIMEN_CPP + "; arts. 395 a 403 CPP PBA; Ley 13.811 (flagrancia, a verificar); Código Penal "
    "(suspensión del juicio a prueba, arts. 76 bis y 76 ter)",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre el acuerdo de juicio abreviado desde la IPP o hasta "
    "30 días antes del debate, la audiencia de conocimiento personal, la admisión o el rechazo, la "
    "sentencia, los recursos (casación criminal / apelación correccional), la relación con flagrancia "
    "y probation, honorarios y firmeza hacia ejecución.",
)

FASES = [
    "Oportunidad",
    "Acuerdo",
    "Audiencia",
    "Resolución",
    "Sentencia",
    "Flagrancia y probation",
    "Recursos",
    "Cierre",
]

GRUPOS = [
    ("Oportunidad del abreviado", ["Oportunidad"]),
    ("Acuerdo y víctimas", ["Acuerdo"]),
    ("Audiencia de conocimiento personal", ["Audiencia"]),
    ("Admisión, rechazo y sentencia", ["Resolución", "Sentencia"]),
    ("Flagrancia y relación con probation", ["Flagrancia y probation"]),
    ("Recursos", ["Recursos"]),
    ("Honorarios, firmeza y cierre", ["Cierre"]),
]

ROL_TEXTO = {
    "ACTORA": "Fiscal / particular damnificado / víctima",
    "DEMANDADA": "Imputado / defensa",
    "TRIBUNAL": "Juez o tribunal de juicio / Casación / Cámara",
    "AMBAS": "Cualquiera de las partes",
}
ROLES_DESCRIPCION = ROLES_DESCRIPCION_PENAL

LEYENDA = leyenda(
    "celeste = acusación: Ministerio Público Fiscal o particular damnificado / víctima (ACTORA); "
    "naranja = imputado y defensa (DEMANDADA); gris = juez o tribunal de juicio, Cámara o Casación "
    "(TRIBUNAL); violeta = cualquiera de las partes (AMBAS).",
    "tras la sentencia del abreviado corren a la vez el recurso (casación o apelación), la impugnación "
    "de honorarios y el control de firmeza hacia ejecución",
    adicionales=[
        ("**Tope de pena (art. 395):** la pena pedida por el fiscal no puede superar 15 años de prisión "
         "(o una pena no privativa de libertad, aún conjunta). Es pena concreta pedida, no máximo abstracto."),
        ("**Rechazo del acuerdo (art. 398):** si se desestima, el proceso sigue en juicio oral; las "
         "conformidades no valen como reconocimiento de culpabilidad. Resolución inimpugnable."),
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "CORRIDOS": (
        "sentencia en 5 días (art. 399); apelación de la sentencia correccional 20 días (441); casación 20 "
        "días (451); honorarios 5 días (Ley 14.967)."
    ),
    "FECHA_FIJADA": "audiencia de conocimiento personal del imputado (art. 398) y actos con fecha fijada.",
    "SIN_PLAZO": (
        "evaluación de oportunidad, negociación del acuerdo, presentación del pedido, notificación a "
        "víctima/particular damnificado, rechazo del acuerdo, flagrancia temprana, probation, acción "
        "civil, firmeza y derivaciones."
    ),
    "ANTICIPACION_HABILES_JUDICIALES": (
        "no se usa por defecto: el límite de 30 días antes del debate (art. 397) se controla con "
        "checklist en hito SIN_PLAZO (ver duda); si el equipo legal confirma anticipación corrida o "
        "hábil, se puede cambiar el tipo."
    ),
    "HORAS": "no se usa en este flujo.",
    "MESES": "no se usa.",
    "ANIOS": "no se usa (prescripción y plazo máximo con detenido se controlan en investigación y juicio oral).",
    "HABILES_JUDICIALES": "recursos extraordinarios ante la SCBA: 10 días hábiles (art. 483).",
    "HABILES_ADMINISTRATIVOS": "no se usa.",
})

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS_PROPIOS = [
    (f"{P}_010", "Oportunidad", "Evaluación de oportunidad del juicio abreviado", "AMBAS",
     "IPP en trámite, elevación a juicio o causa ya en etapa de juicio con debate fijado o por fijar",
     0, "SIN_PLAZO", "NO",
     "Arts. 395 a 397 CPP PBA", "SI", "NO",
     ["Definir si se representa a la defensa o al particular damnificado (el fiscal no es cliente)",
      "Verificar que la pena que el fiscal estimaría suficiente no supere 15 años (art. 395)",
      "El imputado y su defensor también pueden solicitar el trámite (art. 395)",
      "Si el debate ya tiene fecha, controlar el límite de 30 días antes (art. 397)",
      "Con imputado detenido, el plazo máximo de 2 años (art. 141) sigue corriendo en la matriz de origen",
      "La prescripción de la acción sigue corriendo hasta la sentencia (arts. 62 y 67 Código Penal)",
      "No registrar en la app el relato de los hechos ni datos de identidad de víctimas"],
     []),
    (f"{P}_020", "Oportunidad", "Control de oportunidad: hasta 30 días antes del debate", "AMBAS",
     "Fecha fijada para la audiencia del debate oral (si ya existe)", 0, "SIN_PLAZO", "NO",
     "Art. 397 CPP PBA", "NO", "NO",
     ["Las partes pueden acordar el abreviado hasta 30 días antes de la fecha fijada para el debate (art. 397)",
      "Si aún no hay fecha de debate (IPP o etapa intermedia), el límite no corre: cargar checklist al fijarse",
      "Propuesta de modelado: SIN_PLAZO + control manual; alternativa ANTICIPACION (ver duda)",
      "Si el plazo ya venció, no presentar el acuerdo; seguir en juicio oral"],
     ["Cédula o proveído que fija la fecha del debate"]),
    (f"{P}_100", "Acuerdo", "Propuesta de acuerdo (fiscal, imputado o defensa)", "AMBAS",
     "Decisión de impulsar el juicio abreviado", 0, "SIN_PLAZO", "NO",
     "Arts. 395 y 396 CPP PBA", "NO", "NO",
     ["El fiscal debe pedir pena concreta; la defensa e imputado prestan conformidad a pena y calificación",
      "No hay requisito legal general de confesión aparte de la conformidad (art. 396); no confundir con directísimo (403 bis)",
      "Evaluar pluralidad de imputados (art. 400): el régimen se aplica salvo desestimación judicial",
      "Si hay coimputados sin acuerdo, documentar la estrategia sin datos sensibles"],
     ["Borrador de acuerdo o minuta"]),
    (f"{P}_110", "Acuerdo", "Conformidad de hecho, calificación y pena (tope ≤ 15 años)", "DEMANDADA",
     "Propuesta de pena y calificación del fiscal", 0, "SIN_PLAZO", "NO",
     "Arts. 395 y 396 CPP PBA", "NO", "NO",
     ["Extender conformidad a la pena pedida y a la calificación (art. 396)",
      "Controlar que la pena pedida no supere 15 años de prisión (o sea no privativa de libertad, aún conjunta)",
      "Acordar modo de ejecución y reglas de conducta: la sentencia no puede empeorarlas (art. 399)",
      "Asesorar sobre renuncia al debate oral y consecuencias del acuerdo"],
     ["Conformidad escrita del imputado y del defensor"]),
    (f"{P}_120", "Acuerdo", "Notificación al particular damnificado y convocatoria a la víctima", "ACTORA",
     "Acuerdo de abreviado formalizado o en vías de presentación", 0, "SIN_PLAZO", "NO",
     "Arts. 396 y 402 CPP PBA (texto Ley 15.232)", "NO", "NO",
     ["El particular damnificado no puede oponerse a la elección del procedimiento (art. 402)",
      "Notificar el acuerdo al particular damnificado y a la víctima no constituida (art. 402)",
      "Convocar a la víctima a manifestar su opinión; el juez la considera (art. 396)",
      "Si la víctima no desea concurrir, notificarle la decisión que se adopte",
      "No copiar en la app el contenido de la opinión ni datos identificatorios de la víctima"],
     ["Constancia de notificación", "Convocatoria a la víctima"]),
    (f"{P}_130", "Acuerdo", "Presentación del acuerdo ante el órgano judicial", "ACTORA",
     "Acuerdo conjunto del fiscal, imputado y defensor listo para presentar", 0, "SIN_PLAZO", "NO",
     "Arts. 335 y 397 CPP PBA", "NO", "NO",
     ["El fiscal formula la solicitud según el art. 335, con la conformidad del art. 396",
      "Presentar ante el órgano que corresponda (IPP/Garantías o tribunal de juicio, según la etapa)",
      "Si el órgano es colegiado, actúa un solo juez para sustanciar y resolver (art. 398)",
      "Adjuntar constancias de notificación a víctima/particular damnificado"],
     ["Solicitud de juicio abreviado", "Acuerdo y conformidades"]),
    (f"{P}_200", "Audiencia", "Audiencia de conocimiento personal del imputado", "TRIBUNAL",
     "Fecha y hora fijadas para el contacto de visu con el imputado", 0, "FECHA_FIJADA", "NO",
     "Art. 398 CPP PBA", "NO", "NO",
     ["Previo a decidir, el juez o tribunal toma contacto de visu con el imputado (art. 398)",
      "Imponer al imputado de las consecuencias de la vía (renuncia al debate, techo de pena, recursos)",
      "Controlar consentimiento libre: sin coacción, con asistencia del defensor",
      "Si hay duda sobre vicio de voluntad, documentar para eventual rechazo del acuerdo"],
     ["Acta de audiencia o constancia de conocimiento personal"]),
    (f"{P}_300", "Resolución", "Resolución de admisión o rechazo del acuerdo", "TRIBUNAL",
     "Audiencia de conocimiento personal cumplida o formalización del acuerdo lista para resolver",
     0, "SIN_PLAZO", "NO",
     "Art. 398 CPP PBA", "NO", "NO",
     ["Admitir la conformidad y pasar a sentencia (art. 398 inc. 2), o desestimar (inc. 1)",
      "Rechazo solo por voluntad viciada o discrepancia insalvable con la calificación (congruencia)",
      "La desestimación es inimpugnable (art. 398); no abrir recurso ordinario contra ella",
      "Si se rechaza: las conformidades no valen como reconocimiento; el pedido de pena no vincula al fiscal del debate"],
     ["Resolución de admisión o desestimación"]),
    (f"{P}_310", "Sentencia", "Sentencia de juicio abreviado", "TRIBUNAL",
     "Admisión del acuerdo de juicio abreviado", 5, "CORRIDOS", "NO",
     "Art. 399 CPP PBA", "NO", "NO",
     ["Dictar sentencia en 5 días corridos (art. 399)",
      "Fundar en evidencias recibidas antes del acuerdo; no es mera homologación",
      "No imponer pena superior a la pedida ni empeorar modo de ejecución o reglas no convenidas",
      "Se puede absolver cuando corresponda",
      "Feria: el plazo de impugnación de la sentencia definitiva se suspende (art. 139), salvo flagrancia"],
     ["Sentencia"]),
    (f"{P}_320", "Cierre", "Sigue en la matriz de juicio oral", "AMBAS",
     "Desestimación del acuerdo de juicio abreviado (art. 398)", 0, "SIN_PLAZO", "NO",
     "Arts. 398 y 338 y ss. CPP PBA", "NO", "SI",
     ["Crear el expediente vinculado con la matriz de juicio oral (JOR)",
      "Ninguna conformidad o admisión del imputado vale como reconocimiento de culpabilidad",
      "El pedido de pena del acuerdo no vincula al Ministerio Público del debate",
      "Trasladar solo metadatos procesales, sin relatos ni datos sensibles"],
     ["Resolución de desestimación"]),
    (f"{P}_330", "Cierre", "Sigue en la matriz de investigación", "AMBAS",
     "Acuerdo frustrado o desestimado mientras la causa está en la IPP", 0, "SIN_PLAZO", "NO",
     "Arts. 398 y 284 quinquies CPP PBA", "NO", "SI",
     ["Volver al expediente de investigación (IPP) sin crear uno nuevo si ya existe",
      "Ninguna conformidad o admisión del imputado vale como reconocimiento de culpabilidad (art. 398)",
      "Trasladar solo metadatos procesales, sin relatos ni datos sensibles"],
     ["Resolución de desestimación o constancia de falta de acuerdo"]),
    (f"{P}_400", "Flagrancia y probation", "Abreviado en flagrancia o pedido temprano", "AMBAS",
     "Propuesta de abreviado en procedimiento de flagrancia (art. 284 quinquies) o vía temprana",
     0, "SIN_PLAZO", "NO",
     "Arts. 284 quinquies, 395 a 397 y 403 bis CPP PBA (Ley 13.811, a verificar)", "NO", "NO",
     ["En flagrancia puede pedirse abreviado de modo temprano (art. 284 quinquies)",
      "No confundir con juicio directísimo (art. 403 bis): aquel exige admisión de responsabilidad en la declaración",
      "Siguen las mismas reglas de acuerdo, audiencia, sentencia y recursos (arts. 395 a 403)",
      "La feria no suspende plazos en flagrancia (art. 139)"],
     ["Pedido temprano o acuerdo en flagrancia"]),
    (f"{P}_410", "Flagrancia y probation", "Relación con suspensión del juicio a prueba", "AMBAS",
     "Evaluación de probation en paralelo o como alternativa al abreviado", 0, "SIN_PLAZO", "NO",
     "Arts. 76 bis y 76 ter Código Penal; arts. 395 y ss. CPP PBA", "NO", "NO",
     ["Evaluar si conviene abreviado (condena acordada) o suspensión del juicio a prueba (sin condena si se cumple)",
      "No son excluyentes en abstracto: documentar la opción elegida y los requisitos de cada vía",
      "Si se opta por probation, el seguimiento queda en la matriz de investigación (IPP_530 e IPP_535)",
      "Si se revoca la suspensión, el proceso continúa según su estado (art. 76 ter Código Penal); no deriva a ejecución"],
     ["Pedido de probation o constancia de opción"]),
    (f"{P}_500", "Acuerdo", "Acción civil en el juicio abreviado", "AMBAS",
     "Existencia de pretensión civil acumulada o a acordar en el abreviado", 0, "SIN_PLAZO", "NO",
     "Art. 403 CPP PBA", "NO", "NO",
     ["La acción civil puede resolverse en el abreviado si hay conformidad de todas las partes civiles",
      "Sin conformidad civil: se deduce y resuelve en la sede civil competente",
      "Las partes civiles pueden acordar la solución; si fracasa la conciliación, el juez puede sentenciar con las constancias (art. 399)",
      "No registrar montos ni datos patrimoniales sensibles en texto libre de la app"],
     ["Acuerdo civil o constancia de remisión a sede civil"]),
    (f"{P}_600", "Recursos", "Recurso contra la sentencia del abreviado", "AMBAS",
     "Notificación de la sentencia de juicio abreviado", 0, "SIN_PLAZO", "NO",
     "Art. 401 CPP PBA", "NO", "NO",
     ["En lo criminal: recurso de casación (art. 401), 20 días (art. 451)",
      "En lo correccional: recurso de apelación (art. 401), 20 días contra la sentencia definitiva (art. 441)",
      "Legitimados: fiscal, imputado, defensor y particular damnificado",
      "Consentir el trámite no equivale a renunciar al doble conforme",
      "Feria: se suspende el plazo de impugnación de la sentencia definitiva (art. 139), salvo flagrancia"],
     ["Escrito de casación o de apelación"]),
    (f"{P}_700", "Cierre", "Firmeza de la sentencia del abreviado", "AMBAS",
     "Vencimiento de plazos de recurso sin interposición, o resolución firme del recurso",
     0, "SIN_PLAZO", "NO",
     "Arts. 399, 401 y 421 y ss. CPP PBA", "NO", "NO",
     ["Verificar que no queden recursos pendientes (casación, apelación, extraordinarios)",
      "Si hay condena de cumplimiento o reglas a ejecutar, derivar a ejecución penal",
      "Si hay absolución firme o pena de cumplimiento ya agotada en lo procesal, cerrar el expediente"],
     ["Constancia de firmeza"]),
    (f"{P}_900", "Cierre", "Regulación e impugnación de honorarios", "AMBAS",
     "Notificación de la regulación de honorarios", 5, "CORRIDOS", "NO",
     "Arts. 9 y 57 Ley 14.967 (días corridos o hábiles: ver duda transversal)", "NO", "NO",
     ["Impugnar en 5 días fundando en el mismo escrito (art. 57)",
      "Verificar mínimos arancelarios aplicables al fuero penal",
      "Propuesta de la app: 5 CORRIDOS sin gracia",
      "Si no hubo regulación, cerrar el hito"],
     ["Escrito de impugnación de honorarios"]),
    (f"{P}_970", "Cierre", "Sigue en ejecución penal", "AMBAS",
     "Condena firme de juicio abreviado con pena o reglas a ejecutar", 0, "SIN_PLAZO", "NO",
     "Ley 12.256 (ejecución penal; fuera de V1 detalle)", "NO", "SI",
     ["Crear el expediente vinculado de ejecución",
      "Trasladar solo metadatos de la condena (tipo de pena, vencimientos), sin relatos"],
     ["Sentencia firme"]),
    (f"{P}_990", "Cierre", "Archivo o absolución firme", "AMBAS",
     "Absolución firme, archivo o cierre sin ejecución pendiente", 0, "SIN_PLAZO", "NO",
     "Art. 399 CPP PBA; art. 59 Código Penal", "NO", "SI",
     ["Verificar que no queden recursos ni honorarios pendientes",
      "Devolver documentación original al cliente",
      "No conservar relatos ni datos sensibles innecesarios"],
     []),
]

TRANS_PROPIAS = [
    # Oportunidad
    (f"{P}_010", "Hay fecha de debate: controlar los 30 días", f"{P}_020"),
    (f"{P}_010", "Impulsar el acuerdo (IPP, elevación o juicio)", f"{P}_100"),
    (f"{P}_010", "Pedido temprano en flagrancia", f"{P}_400"),
    (f"{P}_010", "Evaluar probation como alternativa", f"{P}_410"),
    (f"{P}_020", "Dentro del plazo: negociar el acuerdo", f"{P}_100"),
    (f"{P}_020", "Plazo vencido: sigue el juicio oral", f"{P}_320"),
    # Acuerdo
    (f"{P}_100", "Propuesta de pena y calificación", f"{P}_110"),
    (f"{P}_100", "Propuesta de pena y calificación, con pretensión civil", f"{P}_110"),
    (f"{P}_100", "Propuesta de pena y calificación, con pretensión civil", f"{P}_500"),
    (f"{P}_110", "Conformidad prestada: notificar a la víctima y al particular damnificado", f"{P}_120"),
    (f"{P}_110", "Sin conformidad, causa en la IPP: sigue la investigación", f"{P}_330"),
    (f"{P}_110", "Sin conformidad, causa en juicio: sigue el juicio oral", f"{P}_320"),
    (f"{P}_120", "Notificaciones cumplidas: presentar el acuerdo", f"{P}_130"),
    (f"{P}_130", "Acuerdo presentado: audiencia de conocimiento personal", f"{P}_200"),
    (f"{P}_500", "Acción civil acordada, remitida a sede civil o desistida", CIERRA),
    # Audiencia y resolución
    (f"{P}_200", "Audiencia cumplida: resolver", f"{P}_300"),
    (f"{P}_300", "Admisión del acuerdo: sentencia", f"{P}_310"),
    (f"{P}_300", "Desestimación con la causa en la IPP: sigue la investigación", f"{P}_330"),
    (f"{P}_300", "Desestimación con la causa en juicio: sigue el juicio oral", f"{P}_320"),
    # Sentencia
    (f"{P}_310", "Sentencia notificada", f"{P}_600"),
    (f"{P}_310", "Sentencia notificada", f"{P}_900"),
    (f"{P}_900", "Honorarios firmes, impugnación resuelta o sin regulación", CIERRA),
    # Flagrancia y probation
    (f"{P}_400", "Acuerdo en flagrancia: conformidad", f"{P}_110"),
    (f"{P}_400", "Sin acuerdo temprano: sigue el procedimiento de flagrancia", f"{P}_330"),
    (f"{P}_410", "Se elige el abreviado", f"{P}_100"),
    (f"{P}_410", "Se elige la probation: sigue en la investigación", f"{P}_330"),
    (f"{P}_410", "Probation no viable: volver a evaluar la oportunidad", f"{P}_010"),
    # Recursos
    (f"{P}_600", "Abreviado en lo criminal: casación", f"{P}_820"),
    (f"{P}_600", "Abreviado en lo correccional: apelación", f"{P}_810"),
    (f"{P}_600", "No se recurre", f"{P}_700"),
    # Firmeza y cierre
    (f"{P}_700", "Condena firme con pena o reglas a ejecutar", f"{P}_970"),
    (f"{P}_700", "Absolución firme o cierre sin ejecución", f"{P}_990"),
]

_RECURSOS = ("810", "820", "830", "840")

NODOS, TRANSICIONES = ordenar(
    NODOS_PROPIOS + nodos_recursos(P, incluir=_RECURSOS),
    TRANS_PROPIAS + trans_recursos(P, f"{P}_700", incluir=_RECURSOS),
)

DUDAS_PROPIAS = [
    ("Modelado del límite de 30 días (art. 397)",
     "¿El plazo de 'hasta 30 días antes del debate' se modela como ANTICIPACION_HABILES_JUDICIALES (valor 30), "
     "como anticipación en CORRIDOS (hoy el motor no tiene ese tipo) o como SIN_PLAZO con checklist? "
     "Propuesta: SIN_PLAZO + checklist hasta confirmar; vencimiento más temprano. " + FUENTE_CPP,
     f"{P}_020"),
    ("Órgano competente según la etapa",
     "Si el acuerdo se presenta durante la IPP o la etapa intermedia, ¿resuelve el Juez de Garantías o debe "
     "esperarse la elevación al tribunal de juicio? ¿Cambia el cómputo del art. 399? Propuesta: checklist en "
     f"{P}_130; el abogado indica el órgano. " + FUENTE_CPP,
     f"{P}_130, {P}_300"),
    ("Inimpugnabilidad del rechazo (art. 398)",
     "La desestimación es inimpugnable. ¿Hay supuestos en que igual proceda casación/queja si el rechazo se "
     "aparta de las causales legales (voluntad viciada / calificación)? Propuesta: no abrir recurso ordinario; "
     "solo derivar a juicio oral. " + FUENTE_CPP,
     f"{P}_300, {P}_320"),
    ("Cómputo de los 5 días de sentencia (art. 399)",
     "¿Los 5 días corren desde la admisión formal, desde la audiencia de visu o desde otra actuación? "
     "¿Se suspenden en feria? Propuesta: 5 CORRIDOS desde la admisión; feria según art. 139 solo para la "
     "impugnación de la sentencia, no para dictarla. " + FUENTE_CPP,
     f"{P}_310"),
    ("Casación vs apelación (art. 401)",
     "Confirmar el criterio práctico para distinguir abreviado 'en lo criminal' (casación) y 'en lo correccional' "
     "(apelación): ¿competencia del órgano, escala penal o fuero del tribunal? Ambos recursos tienen 20 días "
     "contra la sentencia definitiva (arts. 441 y 451). Propuesta: hito JAB_600 con bifurcación manual. "
     + FUENTE_CPP,
     f"{P}_600, {P}_810, {P}_820"),
    ("Opinión de la víctima vs art. 402",
     "¿Qué peso tiene la opinión de la víctima (art. 396) si el particular damnificado no puede oponerse "
     "(art. 402)? ¿La omisión de convocatoria genera nulidad o solo agravio revisable? Propuesta: checklist "
     "obligatorio de convocatoria/notificación; no bloquear el acuerdo. " + FUENTE_CPP,
     f"{P}_120"),
    ("Pluralidad de imputados (art. 400)",
     "Si hay varios imputados y solo algunos acuerdan, ¿el abreviado puede prosperar respecto de los "
     "acordantes mientras los demás siguen a juicio oral? Propuesta: sí, salvo desestimación judicial; "
     "expedientes vinculados. " + FUENTE_CPP,
     f"{P}_100, {P}_400"),
    ("Abreviado vs probation",
     "¿Hay criterio del estudio o de la fiscalía local sobre cuándo preferir abreviado frente a suspensión "
     "del juicio a prueba? ¿Se documenta la opción rechazada? Propuesta: hito JAB_410 sin plazo. Norma: "
     "arts. 76 bis/ter CP y 395 CPP PBA.",
     f"{P}_410"),
    ("Acción civil y sede competente (art. 403)",
     "Si no hay conformidad de todas las partes civiles, ¿qué órgano civil de PBA recibe la remisión y "
     "con qué efecto sobre la sentencia penal? Propuesta: el penal sigue; civil fuera de esta matriz. "
     + FUENTE_CPP,
     f"{P}_500"),
    ("Directísimo (403 bis) fuera de esta matriz",
     "¿El juicio directísimo de flagrancia (art. 403 bis) debe tener matriz propia o alcanza con el hito "
     "JAB_400 y la remisión a investigación/flagrancia? Propuesta V1: solo el hito de relación; directísimo "
     "detalle fuera. " + FUENTE_CPP,
     f"{P}_400"),
]

DUDAS_PROPIAS.append(duda_federal(
    "el juicio abreviado",
    "En el CPPF hay acuerdos plenos, parciales y de colaboración (a verificar); en el CPPN, el juicio "
    "abreviado del art. 431 bis (a verificar).",
    f"{P}_100, {P}_300",
))

DUDAS = numerar(DUDAS_PROPIAS + [DUDA_REMITIR_TRANSVERSALES])
