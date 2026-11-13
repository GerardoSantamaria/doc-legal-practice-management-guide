"""Hábeas corpus (HCO) — CPP PBA arts. 405 a 420 (Ley 11.922)."""
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
    ROLES_DESCRIPCION_HABEAS,
    duda_federal,
    flujo,
    leyenda,
    numerar,
    ordenar,
    plazo_tipos,
)

P = "HCO"

FLUJO = flujo(
    "Hábeas corpus (PBA)",
    REGIMEN_CPP + "; arts. 405 a 420 CPP PBA; art. 20 inc. 1 Constitución de la Provincia de Buenos Aires; "
    "art. 43 Constitución Nacional; Ley 23.098 (hábeas corpus federal, solo como referencia); Ley 14.967; "
    "jurisprudencia Verbitsky (CSJN, 2005) y SCBA sobre hábeas colectivo (a verificar alcance)",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre reparador, preventivo, correctivo y colectivo. Puede abrirse "
    "desde la matriz de investigación ante detención, prisión preventiva o agravamiento de condiciones.",
)

FASES = [
    "Previa",
    "Interposición",
    "Trámite",
    "Audiencia y prueba",
    "Resolución",
    "Recursos",
    "Cierre",
]

GRUPOS = [
    ("Evaluación y tipo", ["Previa"]),
    ("Interposición", ["Interposición"]),
    ("Informe, orden y presentación", ["Trámite"]),
    ("Audiencia, prueba y plazos de resolución", ["Audiencia y prueba", "Resolución"]),
    ("Impugnación", ["Recursos"]),
    ("Cierre y derivaciones", ["Cierre"]),
]

ROL_TEXTO = {
    "ACTORA": "Quien interpone",
    "DEMANDADA": "Autoridad requerida",
    "TRIBUNAL": "Juez o tribunal",
    "AMBAS": "Cualquiera de los intervinientes",
}
ROLES_DESCRIPCION = ROLES_DESCRIPCION_HABEAS

LEYENDA = leyenda(
    "celeste = quien interpone el hábeas corpus: persona afectada o cualquiera a su favor (ACTORA); "
    "naranja = autoridad requerida: policía, servicio penitenciario u otro que restringe la libertad "
    "(DEMANDADA); gris = juez o tribunal penal que conoce, Cámara o Casación (TRIBUNAL); violeta = "
    "cualquiera de los intervinientes en la audiencia o el recurso (AMBAS).",
    "tras la radicación corren a la vez el informe de la autoridad (12 horas) y, si hay privación de "
    "libertad, la orden de presentar al detenido",
    adicionales=[
        ("**Tipos de hábeas corpus:** reparador (privación actual), preventivo (amenaza inminente), "
         "correctivo (agravamiento de condiciones de detención legal) y colectivo (afectación homogénea; "
         "Verbitsky, CSJN 2005, y SCBA). El tipo se elige en la evaluación y marca el checklist."),
        ("**Informalidad (arts. 406-407):** puede interponerse por cualquiera, sin formalidades, oralmente, "
         "por escrito o por teléfono, a cualquier hora, ante cualquier órgano jurisdiccional. Si se impugna "
         "una decisión judicial, hay que exponer agravios bajo sanción de inadmisibilidad."),
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "HORAS": (
        "informe de la autoridad 12 horas (art. 409); continuación de prueba hasta 24 horas (art. 413); "
        "resolución 24 horas sin audiencia o 48 horas desde el fin de la audiencia (art. 415)."
    ),
    "FECHA_FIJADA": "audiencia oral del art. 412 (fecha y hora que fija el órgano).",
    "SIN_PLAZO": (
        "evaluación del tipo, interposición, radicación, orden de presentar, cumplimiento, resultados "
        "(libertad, cese, corrección, rechazo), impugnación art. 417 (plazo a verificar), remisión de copias "
        "y cierres."
    ),
    "CORRIDOS": "impugnación de honorarios 5 días (art. 57 Ley 14.967).",
    "HABILES_JUDICIALES": "no se usa.",
    "HABILES_ADMINISTRATIVOS": "no se usa.",
    "MESES": "no se usa.",
    "ANIOS": "no se usa.",
    "ANTICIPACION_HABILES_JUDICIALES": "no se usa.",
})

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    (f"{P}_010", "Previa", "Evaluación del tipo de hábeas corpus", "ACTORA",
     "Consulta o decisión de interponer hábeas corpus", 0, "SIN_PLAZO", "NO",
     "Art. 405 CPP PBA; art. 20 inc. 1 Constitución PBA", "SI", "NO",
     ["Definir el tipo: reparador (privación actual ilegal o arbitraria), preventivo (amenaza inminente), "
      "correctivo (agravamiento de condiciones de detención legal) o colectivo (afectación homogénea de un grupo)",
      "Colectivo: mencionar Verbitsky (CSJN, 2005) y justificar homogeneidad del grupo y aptitud del remedio "
      "(SCBA; ver duda)",
      "Si deriva de IPP: detención sin puesta a disposición, denegatoria de excarcelación o prisión preventiva "
      "ilegal/arbitraria (art. 405 incs. y hasta el inicio del debate)",
      "Si se excedió el plazo máximo con detenido (art. 141), evaluar hábeas o pedido de cese ante el juez de la "
      "causa (a verificar)",
      "No registrar en la app el relato de los hechos ni datos de identidad de detenidos o víctimas"],
     []),
    (f"{P}_020", "Interposición", "Interposición del hábeas corpus", "ACTORA",
     "Decisión de interponer", 0, "SIN_PLAZO", "NO",
     "Arts. 406 y 407 CPP PBA", "NO", "NO",
     ["Puede interponerlo la persona afectada o cualquiera a su favor, con o sin mandato y con o sin abogado "
      "(art. 407)",
      "Sin formalidades: oral, escrito o telefónico; a cualquier hora; se labra acta si es oral (art. 407)",
      "Competencia: cualquier órgano jurisdiccional de la Provincia (art. 406; art. 20 Const. PBA). Si es contra "
      "prisión preventiva de juez o tribunal, interviene la Cámara de Garantías departamental (art. 406)",
      "Si se impugna una decisión judicial: exponer motivos de agravio bajo sanción de inadmisibilidad (art. 407)",
      "Proporcionar en lo posible: datos del peticionante y del beneficiario, autoridad o particular requerido y "
      "relación sucinta de las razones (sin copiar el relato en la app)"],
     ["Acta o escrito de interposición", "Copia de la resolución impugnada (si hay)"]),
    (f"{P}_100", "Trámite", "Radicación y apertura del trámite", "TRIBUNAL",
     "Interposición recibida por el órgano", 0, "SIN_PLAZO", "NO",
     "Arts. 406, 408 y 418 CPP PBA", "NO", "NO",
     ["No cabe recusación; si el magistrado se inhibe, se integra el tribunal (art. 408)",
      "Notificar al Ministerio Público Fiscal el inicio (art. 418); no es necesario citarlo en actos posteriores",
      "Abrir el informe (12 horas) y, si hay privación de libertad actual, también la orden de presentar al "
      "detenido",
      "Con detenido: plazos en horas pueden correr en días inhábiles (ver duda transversal)"],
     ["Constancia de radicación", "Notificación al MPF"]),
    (f"{P}_110", "Trámite", "Informe de la autoridad requerida (12 horas)", "DEMANDADA",
     "Requerimiento del informe por el órgano (fecha y hora)", 12, "HORAS", "NO",
     "Art. 409 CPP PBA", "NO", "NO",
     ["Plazo máximo de 12 horas desde el requerimiento (art. 409)",
      "El informe debe contener las razones de la medida o acto atacado y, en su caso, las actuaciones labradas",
      "Si hay detenido: incluir motivo, forma y condiciones de la detención; orden escrita si existe; y, si fue "
      "puesto a disposición de otra autoridad, a quién, por qué y cuándo (art. 410)",
      "Con detenido: corre en días inhábiles (a verificar)",
      "Incumplimiento: evaluar responsabilidad funcional (art. 420)"],
     ["Informe de la autoridad", "Actuaciones acompañadas"]),
    (f"{P}_120", "Trámite", "Orden de presentar al detenido", "TRIBUNAL",
     "Radicación con privación de libertad actual", 0, "SIN_PLAZO", "NO",
     "Arts. 410 y 411 CPP PBA", "NO", "NO",
     ["Si hay privación de libertad: ordenar la presentación inmediata del detenido junto con el informe "
      "(art. 410); corre en paralelo con el informe",
      "Si solo hay amenaza (preventivo): basta el informe; este camino no se abre",
      "Si se ignora la autoridad: librar la orden a superiores jerárquicos; el órgano puede constituirse en el lugar",
      "Desde el conocimiento de la orden, el restringido queda a disposición del órgano (art. 411)"],
     ["Orden de hábeas corpus"]),
    (f"{P}_130", "Trámite", "Cumplimiento de la orden y presentación", "DEMANDADA",
     "Notificación de la orden de hábeas corpus", 0, "SIN_PLAZO", "NO",
     "Art. 411 CPP PBA", "NO", "NO",
     ["Cumplir de inmediato o en el plazo que fije el órgano según las circunstancias",
      "Si hay impedimento físico: informe complementario y, si corresponde, visita de familiar o persona de confianza",
      "Controlar que el detenido quede a disposición del órgano para el procedimiento",
      "El trámite principal sigue por el informe, la audiencia y la resolución"],
     ["Constancia de presentación o informe complementario"]),
    (f"{P}_200", "Audiencia y prueba", "Audiencia oral (art. 412)", "AMBAS",
     "Fecha y hora fijadas por el órgano", 0, "FECHA_FIJADA", "NO",
     "Arts. 412 y 414 CPP PBA", "NO", "NO",
     ["El órgano designa audiencia oral citando a los interesados (art. 412; ver duda sobre obligatoriedad frente "
      "al art. 413)",
      "Requirente y requerido con asistencia letrada cuando corresponda",
      "Comienza con la lectura de la petición o acta y de los informes",
      "De la audiencia se labra acta (art. 414)",
      "Si no se celebra audiencia, el camino pasa a resolución en 24 horas (art. 415)"],
     ["Citación", "Acta de audiencia"]),
    (f"{P}_210", "Audiencia y prueba", "Continuación de la prueba (máx. 24 horas)", "TRIBUNAL",
     "Decisión de diferir la prueba que no pudo incorporarse en el mismo acto (fecha y hora)", 24, "HORAS", "NO",
     "Art. 413 CPP PBA", "NO", "NO",
     ["La prueba se incorpora en el mismo acto; si no es posible, continuar la audiencia en un plazo que no "
      "exceda las 24 horas (art. 413)",
      "Admisibilidad según utilidad o pertinencia; decisión exclusiva del órgano",
      "Con detenido: corre en días inhábiles (a verificar)",
      "Finalizada la prueba, oír a los intervinientes y pasar a resolución"],
     ["Acta de continuación", "Medidas probatorias"]),
    (f"{P}_220", "Resolución", "Resolución sin audiencia (24 horas)", "TRIBUNAL",
     "Decisión de resolver sin celebrar audiencia, o vencimiento del trámite sin audiencia (fecha y hora)", 24,
     "HORAS", "NO",
     "Art. 415 CPP PBA (primer párrafo)", "NO", "NO",
     ["Sin audiencia: el tribunal se integra con al menos dos jueces (incluido el que previno); en discrepancia, "
      "interviene el restante (art. 415)",
      "Resolver en 24 horas",
      "La resolución debe motivar rechazo o acogimiento, costas y sanciones (art. 415)",
      "Con detenido: corre en días inhábiles (a verificar)"],
     ["Resolución"]),
    (f"{P}_230", "Resolución", "Resolución tras audiencia (48 horas)", "TRIBUNAL",
     "Finalización de la audiencia del art. 412 (fecha y hora)", 48, "HORAS", "NO",
     "Art. 415 CPP PBA (segundo párrafo)", "NO", "NO",
     ["Con audiencia: intervienen todos los jueces del tribunal; resolver dentro de las 48 horas desde el fin "
      "de la audiencia (art. 415)",
      "Parte dispositiva: rechazo o acogimiento (libertad, cese de amenaza, corrección de condiciones, u otra "
      "medida que corresponda)",
      "Pronunciamiento sobre costas y sanciones",
      "Con detenido: corre en días inhábiles (a verificar)"],
     ["Resolución"]),
    (f"{P}_300", "Resolución", "Rechazo de la petición", "TRIBUNAL",
     "Notificación de la resolución que rechaza el hábeas corpus", 0, "SIN_PLAZO", "NO",
     "Art. 415 CPP PBA", "NO", "NO",
     ["Evaluar impugnación ante Cámara o Casación (art. 417)",
      "Si el rechazo es firme, cerrar el expediente de hábeas",
      "No copiar en la app los fundamentos fácticos sensibles"],
     ["Resolución de rechazo", "Cédula o notificación"]),
    (f"{P}_310", "Resolución", "Libertad inmediata (reparador)", "TRIBUNAL",
     "Notificación de la resolución que acoge y ordena la libertad", 0, "SIN_PLAZO", "NO",
     "Arts. 405 y 415 CPP PBA", "NO", "NO",
     ["Controlar el cumplimiento inmediato de la libertad",
      "Si hay indicios de delito de acción pública, abrir el camino de denuncia (art. 416)",
      "Evaluar impugnación de la autoridad o del MPF (art. 417)"],
     ["Resolución de libertad", "Constancia de egreso"]),
    (f"{P}_320", "Resolución", "Cese de la amenaza (preventivo)", "TRIBUNAL",
     "Notificación de la resolución que hace cesar la amenaza a la libertad", 0, "SIN_PLAZO", "NO",
     "Arts. 405 y 415 CPP PBA", "NO", "NO",
     ["Verificar que la autoridad cesó el acto amenazante",
      "Evaluar impugnación (art. 417)",
      "Si corresponde, dejar constancia sin detallar datos sensibles"],
     ["Resolución de cese"]),
    (f"{P}_330", "Resolución", "Corrección de condiciones de detención (correctivo)", "TRIBUNAL",
     "Notificación de la resolución que ordena corregir condiciones", 0, "SIN_PLAZO", "NO",
     "Arts. 405 y 415 CPP PBA; jurisprudencia correctiva/colectiva (Verbitsky 2005; a verificar)", "NO", "NO",
     ["Controlar el cumplimiento de las medidas correctivas (salud, hacinamiento, aislamiento, etc.)",
      "En colectivo: controlar homogeneidad y alcance del remedio (ver duda Verbitsky / SCBA)",
      "Evaluar impugnación (art. 417)",
      "No registrar en la app detalles clínicos ni ubicación sensible"],
     ["Resolución correctiva", "Informes de cumplimiento"]),
    (f"{P}_400", "Recursos", "Impugnación ante Cámara o Casación (art. 417)", "AMBAS",
     "Notificación de la resolución del hábeas corpus", 0, "SIN_PLAZO", "NO",
     "Art. 417 CPP PBA (plazo concreto a verificar)", "NO", "NO",
     ["Impugnable ante la Cámara de Apelación y Garantías; si la acción se originó en Cámara, ante el Tribunal "
      "de Casación (art. 417)",
      "Cargar el plazo concreto como plazo suelto hasta confirmar (ver duda)",
      "Fundar agravios; no usar el hábeas como mera reiteración de la apelación ordinaria"],
     ["Escrito de impugnación"]),
    (f"{P}_410", "Recursos", "Resolución del recurso", "TRIBUNAL",
     "Trámite del recurso ante Cámara o Casación", 0, "SIN_PLAZO", "NO",
     "Art. 417 CPP PBA", "NO", "NO",
     ["Controlar confirmación, revocación o modificación",
      "Si se ordena libertad, cese o corrección, abrir el hito de resultado correspondiente si aún no está",
      "Agotada la vía, cerrar o evaluar extraordinarios fuera de esta matriz"],
     ["Resolución de Cámara o Casación"]),
    (f"{P}_500", "Cierre", "Denuncia por delito o responsabilidad de la autoridad", "TRIBUNAL",
     "Conocimiento de probable delito de acción pública o incumplimiento funcional", 0, "SIN_PLAZO", "NO",
     "Arts. 416 y 420 CPP PBA", "NO", "NO",
     ["Art. 416: extraer copias y entregarlas al órgano que deba intervenir (denuncia / IPP)",
      "Art. 420: el juez o funcionario que incumpla las disposiciones incurre en falta grave; iniciar los "
      "trámites ante la autoridad competente",
      "La investigación del hecho es un expediente nuevo en la matriz de investigación; el hábeas sigue su trámite",
      "No copiar el relato en la app"],
     ["Oficio o remisión de copias"]),
    (f"{P}_900", "Cierre", "Costas y honorarios del hábeas corpus", "AMBAS",
     "Notificación de la resolución firme con costas o regulación de honorarios", 5, "CORRIDOS", "NO",
     "Art. 415 CPP PBA; art. 57 Ley 14.967 (días corridos o hábiles: ver duda transversal en IPP)", "NO", "NO",
     ["La resolución se pronuncia sobre costas y sanciones (art. 415)",
      "Si hay regulación, impugnar en 5 días fundando en el mismo escrito (art. 57 Ley 14.967)",
      "Si no hubo regulación ni costas, cerrar el hito",
      "Propuesta de la app: 5 CORRIDOS sin gracia"],
     ["Resolución con costas o regulación", "Escrito de impugnación (si corresponde)"]),
    (f"{P}_950", "Cierre", "Sigue en la matriz de investigación", "AMBAS",
     "Hábeas resuelto con la causa principal del beneficiario todavía en trámite", 0, "SIN_PLAZO", "NO",
     "Arts. 405 y 416 CPP PBA; vinculación con la matriz de investigación", "NO", "SI",
     ["Volver al expediente de investigación (IPP) o de juicio desde el que se abrió el hábeas",
      "Trasladar solo metadatos procesales, sin relatos ni datos sensibles"],
     ["Copia de la remisión o de la resolución"]),
    (f"{P}_990", "Cierre", "Cierre del hábeas corpus", "AMBAS",
     "Resolución firme, desistimiento o cumplimiento de lo ordenado", 0, "SIN_PLAZO", "NO",
     "Arts. 415 a 420 CPP PBA", "NO", "SI",
     ["Verificar que no queden recursos ni medidas pendientes de cumplimiento",
      "Devolver documentación al cliente",
      "No conservar relatos ni datos sensibles innecesarios"],
     []),
]

TRANSICIONES = [
    # Tipos e interposición
    (f"{P}_010", "Hábeas reparador (privación actual)", f"{P}_020"),
    (f"{P}_010", "Hábeas preventivo (amenaza inminente)", f"{P}_020"),
    (f"{P}_010", "Hábeas correctivo (condiciones de detención)", f"{P}_020"),
    (f"{P}_010", "Hábeas colectivo (afectación homogénea; Verbitsky)", f"{P}_020"),
    (f"{P}_010", "Deriva de IPP: detención, PP o denegatoria de excarcelación", f"{P}_020"),
    (f"{P}_020", "Interposición formulada", f"{P}_100"),
    # Trámite: informe y, con privación actual, orden de presentar en paralelo
    (f"{P}_100", "Privación de libertad actual (reparador, correctivo o colectivo)", f"{P}_110"),
    (f"{P}_100", "Privación de libertad actual (reparador, correctivo o colectivo)", f"{P}_120"),
    (f"{P}_100", "Amenaza a la libertad (preventivo)", f"{P}_110"),
    (f"{P}_110", "Informe presentado: se fija audiencia", f"{P}_200"),
    (f"{P}_110", "Informe presentado: se resuelve sin audiencia", f"{P}_220"),
    (f"{P}_110", "Vence sin informe: audiencia y responsabilidad de la autoridad", f"{P}_200"),
    (f"{P}_110", "Vence sin informe: audiencia y responsabilidad de la autoridad", f"{P}_500"),
    (f"{P}_120", "Orden librada: controlar presentación", f"{P}_130"),
    (f"{P}_130", "Detenido presentado y a disposición del órgano", CIERRA),
    (f"{P}_130", "Incumplimiento de la orden", f"{P}_500"),
    # Audiencia y prueba
    (f"{P}_200", "Audiencia celebrada sin prueba diferida", f"{P}_230"),
    (f"{P}_200", "Se difiere prueba (máx. 24 horas)", f"{P}_210"),
    (f"{P}_210", "Prueba incorporada: fin de la audiencia", f"{P}_230"),
    # Resultados
    (f"{P}_220", "Rechazo", f"{P}_300"),
    (f"{P}_220", "Se ordena libertad inmediata", f"{P}_310"),
    (f"{P}_220", "Se ordena el cese de la amenaza", f"{P}_320"),
    (f"{P}_220", "Se ordena corrección de condiciones", f"{P}_330"),
    (f"{P}_230", "Rechazo", f"{P}_300"),
    (f"{P}_230", "Se ordena libertad inmediata", f"{P}_310"),
    (f"{P}_230", "Se ordena el cese de la amenaza", f"{P}_320"),
    (f"{P}_230", "Se ordena corrección de condiciones", f"{P}_330"),
    # Después de la resolución
    (f"{P}_300", "Se impugna (art. 417)", f"{P}_400"),
    (f"{P}_300", "Rechazo firme", f"{P}_900"),
    (f"{P}_310", "Se impugna (art. 417)", f"{P}_400"),
    (f"{P}_310", "Libertad cumplida", f"{P}_900"),
    (f"{P}_310", "Libertad cumplida, con indicios de delito o falta grave", f"{P}_500"),
    (f"{P}_310", "Libertad cumplida, con indicios de delito o falta grave", f"{P}_900"),
    (f"{P}_320", "Se impugna (art. 417)", f"{P}_400"),
    (f"{P}_320", "Cese cumplido", f"{P}_900"),
    (f"{P}_330", "Se impugna (art. 417)", f"{P}_400"),
    (f"{P}_330", "Corrección cumplida", f"{P}_900"),
    (f"{P}_330", "Corrección cumplida, con indicios de delito o falta grave", f"{P}_500"),
    (f"{P}_330", "Corrección cumplida, con indicios de delito o falta grave", f"{P}_900"),
    # Recursos
    (f"{P}_400", "Recurso interpuesto", f"{P}_410"),
    (f"{P}_400", "Se desiste de la impugnación", f"{P}_900"),
    (f"{P}_410", "Confirma la resolución", f"{P}_900"),
    (f"{P}_410", "Revoca y ordena libertad", f"{P}_310"),
    (f"{P}_410", "Revoca y ordena cese de amenaza", f"{P}_320"),
    (f"{P}_410", "Revoca y ordena corrección", f"{P}_330"),
    (f"{P}_410", "Revoca y rechaza el hábeas", f"{P}_300"),
    # Remisión de copias (camino paralelo)
    (f"{P}_500", "Copias remitidas a la fiscalía (art. 416)", CIERRA),
    (f"{P}_500", "Trámite iniciado ante la autoridad competente (art. 420)", CIERRA),
    # Cierre
    (f"{P}_900", "Costas y honorarios resueltos o sin regulación", f"{P}_990"),
    (f"{P}_900", "Costas y honorarios resueltos; la causa principal sigue en la IPP", f"{P}_950"),
]

NODOS, TRANSICIONES = ordenar(NODOS, TRANSICIONES)

DUDAS_PROPIAS = [
    ("Plazo de impugnación (art. 417)",
     "El art. 417 CPP PBA no fija el plazo para impugnar la resolución de hábeas corpus ante Cámara o Casación. "
     "¿Rige el de apelación (5 días corridos, art. 441), el de 24 horas de la Ley 23.098 federal, u otro? "
     "Propuesta: hito SIN_PLAZO con carga manual hasta confirmar. " + FUENTE_CPP,
     f"{P}_400"),
    ("Audiencia obligatoria (arts. 412 y 413)",
     "El art. 412 (texto Ley 13.252) dice que el órgano 'deberá' designar audiencia oral; el art. 413 dice que "
     "la celebración de la audiencia y la prueba son decisión exclusiva del órgano, y el art. 415 contempla "
     "resolver sin audiencia en 24 horas. ¿La audiencia es obligatoria o discrecional al 13/11/2026? "
     "Propuesta: modelar ambos caminos. " + FUENTE_CPP,
     f"{P}_200, {P}_220"),
    ("Competencia: cualquier juez vs. juez penal",
     "El art. 20 Const. PBA permite hábeas ante cualquier juez. El Decreto 2749/04 observó en el art. 406 la "
     "frase 'con competencia penal'. ¿Confirmamos competencia amplia, con remisión a Cámara de Garantías solo "
     "contra prisión preventiva (art. 406 párr. 3)? Propuesta: sí; checklist en HCO_020. " + FUENTE_CPP,
     f"{P}_020, {P}_100"),
    ("Hábeas colectivo y Verbitsky (2005)",
     "¿Qué requisitos exige la práctica bonaerense para el hábeas colectivo (homogeneidad, legitimación, "
     "remedio) tras Verbitsky (CSJN, 2005) y la jurisprudencia SCBA (p. ej. P.133.682)? ¿Se modela solo con "
     "checklist o hace falta un subflujo? Propuesta: checklist en HCO_010/HCO_330 hasta validar. Norma y fallos "
     "a verificar.",
     f"{P}_010, {P}_330"),
    ("Hábeas contra prisión preventiva hasta el debate",
     "Art. 405: el hábeas contra el auto de PP procede hasta la iniciación de la audiencia de debate. ¿La app "
     "debe bloquear la apertura de HCO desde IPP/JOR después de iniciado el debate, o solo alertar? "
     "Propuesta: alertar en checklist; no bloquear en V1. " + FUENTE_CPP,
     f"{P}_010"),
    ("Cómputo del informe de 12 horas (art. 409)",
     "¿Las 12 horas del informe corren en días y horas inhábiles (con detenido) sin suspensión por feria? "
     "Propuesta: HORAS desde fecha/hora del requerimiento, sin interrupción (vencimiento más temprano). "
     + FUENTE_CPP,
     f"{P}_110"),
    ("Continuación de prueba en 24 horas (art. 413)",
     "Si la prueba no se incorpora en el mismo acto, ¿las 24 horas son corridas inclusive en inhábil? ¿Qué "
     "pasa si vence sin producirla? Propuesta: 24 HORAS; al vencer, pasar a resolución con la prueba "
     "incorporada. " + FUENTE_CPP,
     f"{P}_210"),
    ("Disparador de la resolución de 24/48 horas (art. 415)",
     "Sin audiencia: ¿las 24 horas corren desde la decisión de no celebrarla, desde el informe, o desde la "
     "interposición? Con audiencia: confirmar que las 48 horas corren desde el fin de la audiencia (incluida "
     "la continuación de prueba). Propuesta: disparadores como están en HCO_220 y HCO_230. " + FUENTE_CPP,
     f"{P}_220, {P}_230"),
    ("Costas y sanciones en la resolución",
     "Art. 415: la resolución se pronuncia sobre costas y sanciones. ¿Hay arancel o sanción típica? ¿Se "
     "regulan honorarios en el mismo acto (Ley 14.967)? Propuesta: hito HCO_900 de 5 CORRIDOS antes del "
     "cierre; si no hubo regulación, se cierra sin plazo. " + FUENTE_CPP,
     f"{P}_220, {P}_230, {P}_900"),
    ("Vinculación con la matriz de investigación",
     "Cuando el hábeas nace de una IPP (detención, PP, excarcelación) o remite denuncia (art. 416), ¿cómo se "
     "vinculan los expedientes sin copiar datos sensibles? Propuesta: la remisión de copias (HCO_500) es un "
     "camino paralelo que no cierra el hábeas; el hecho denunciado se investiga en un expediente nuevo; al "
     "terminar, HCO_950 vuelve a la causa principal. Ver duda de producto en la matriz de investigación.",
     f"{P}_500, {P}_950"),
    ("Notificación al MPF (art. 418)",
     "¿Basta la notificación oral con constancia del inicio, y después no se cita al fiscal en audiencia ni "
     "resolución? Propuesta: checklist en HCO_100; no modelar plazos adicionales. " + FUENTE_CPP,
     f"{P}_100"),
    ("Estado de sitio (art. 419)",
     "¿Hace falta un hito o solo una nota de que el hábeas procede y debe resolverse aún durante el estado de "
     "sitio? Propuesta: solo nota en instrucciones; no modelar hito. " + FUENTE_CPP,
     f"{P}_020"),
]

DUDAS_PROPIAS += [
    ("Consulta o elevación obligatoria de la resolución",
     "La Ley 23.098 (federal) no rige en PBA, y los arts. 405 a 420 CPP PBA no prevén una consulta o elevación "
     "obligatoria de la resolución que rechaza el hábeas. ¿Hay alguna acordada de la SCBA o práctica "
     "departamental que la imponga? Propuesta: no se modela; solo la impugnación del art. 417. " + FUENTE_CPP,
     f"{P}_300, {P}_400"),
    duda_federal(
        "el hábeas corpus",
        "Ley 23.098 (arts. 3 a 23, a verificar), con competencia del juez federal cuando la autoridad requerida "
        "es nacional.",
        f"{P}_010, {P}_020",
    ),
]

DUDAS = numerar(DUDAS_PROPIAS + [DUDA_REMITIR_TRANSVERSALES])
