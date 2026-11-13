"""Contencioso administrativo (CAD) — Ley 12.008 y Decreto-Ley 7647/70, contra la Provincia, municipios y entes."""
from comun import (
    CHECKLIST_COSTOS_PBA,
    CHECKLIST_SIN_DATOS,
    CIERRA,
    CON_GRACIA,
    CON_VALOR_CERO,
    DUDAS_PRODUCTO,
    DUDAS_TRANSVERSALES,
    ESTADOS,
    FUENTE_7647,
    FUENTE_CCA,
    FUENTE_CF,
    INSTRUCCIONES_ADICIONALES,
    NOTA_FUENTES,
    NOTA_SENSIBLES,
    ROL_TEXTO,
    ROLES,
    ROLES_DESCRIPCION,
    bloque_cautelar,
    ejecucion_estado,
    flujo,
    honorarios,
    leyenda,
    numerar,
    ordenar,
    plazo_tipos,
    recursos_cca,
)

P = "CAD"
i = lambda n: f"{P}_{n:03d}"

FLUJO = flujo(
    "Contencioso administrativo (PBA)",
    "PBA",
    "Contencioso Administrativo",
    "Ley 12.008 (Código Contencioso Administrativo) con el CPCCBA supletorio (art. 77); vía administrativa: "
    "Decreto-Ley 7647/70 (Provincia) y Ordenanza General 267/80 (municipios)",
    NOTA_FUENTES + " " + NOTA_SENSIBLES + " Cubre la impugnación de actos, empleo público, tributario, licitaciones, "
    "responsabilidad del Estado, amparo por mora, el proceso sumario de ilegitimidad, cautelares, recursos y "
    "ejecución contra la Provincia, los municipios y los entes provinciales. El Estado nacional queda fuera: ver el "
    "cuadro de equivalencias en publico/README.md.",
)

FASES = [
    "Previa",
    "Vía administrativa",
    "Empleo público",
    "Tributario",
    "Licitaciones",
    "Amparo por mora",
    "Demanda",
    "Sumario de ilegitimidad",
    "Cautelares",
    "Prueba",
    "Sentencia",
    "Recursos",
    "Ejecución",
    "Cierre",
]

GRUPOS = [
    ("Etapa previa y encuadre", ["Previa"]),
    ("Vía administrativa (Decreto-Ley 7647/70 u Ordenanza General 267/80)", ["Vía administrativa"]),
    ("Variantes administrativas: empleo público, tributario y licitaciones",
     ["Empleo público", "Tributario", "Licitaciones"]),
    ("Amparo por mora (art. 76 Ley 12.008)", ["Amparo por mora"]),
    ("Demanda y contestación", ["Demanda"]),
    ("Proceso sumario de ilegitimidad", ["Sumario de ilegitimidad"]),
    ("Medidas cautelares contra el Estado provincial", ["Cautelares"]),
    ("Prueba y sentencia", ["Prueba", "Sentencia"]),
    ("Recursos", ["Recursos"]),
    ("Ejecución contra el Estado provincial o municipal", ["Ejecución"]),
    ("Acuerdo, honorarios y cierre", ["Cierre"]),
]

LEYENDA = leyenda(
    paralelo="la notificación del acto que agota la vía abre a la vez el control de la caducidad de 90 días y la "
             "preparación de la demanda",
    adicionales=[
        "**Calendario administrativo:** en la vía administrativa provincial rige el Decreto-Ley 7647/70 y en la "
        "municipal la Ordenanza General 267/80; el checklist de cada hito dice cuál aplica.",
        "**Estado nacional:** no tiene camino propio en esta matriz. La salida \"Estado nacional demandado: fuera "
        "de esta matriz\" remite al cuadro de equivalencias de publico/README.md.",
    ],
)
EJEMPLO_PARALELO = LEYENDA["paralelo"]

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": (
        "plazos de la Ley 12.008: caducidad de 90 días (art. 18), excepciones 15 días (art. 34), contestación 45 "
        "días (art. 38), alegatos 10 días (art. 48), sentencia 60 días (art. 49), apelación 10 días (art. 56), "
        "Cámara 30 días (art. 59), ejecución (arts. 63 y 65)."
    ),
    "HABILES_ADMINISTRATIVOS": (
        "revocatoria y jerárquico 10 días (arts. 89 y 92 Decreto-Ley 7647/70), plazos para resolver (art. 77), "
        "silencio 30 días tras el pronto despacho (art. 16 Ley 12.008), pedido de suspensión 5 días (art. 25), "
        "recursos del Código Fiscal (arts. 113 y 115)."
    ),
    "MESES": "caducidad de instancia de 6 meses, o 3 en los procesos especiales (art. 62 Ley 12.008).",
    "ANIOS": "prescripción de la acción de responsabilidad del Estado (3 años por analogía, a verificar).",
    "FECHA_FIJADA": "audiencia del art. 41 Ley 12.008 y cumplimiento de la cautelar.",
    "SIN_PLAZO": "decisiones del cliente, del juzgado o de la Administración sin plazo legal, y plazos que fija el juez.",
})

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    # --- Previa ---
    (i(10), "Previa", "Encuadre de la pretensión y del demandado", "ACTORA",
     "Consulta del cliente por un acto, una omisión o un hecho de la Administración provincial o municipal", 0,
     "SIN_PLAZO", "NO", "Arts. 1, 2, 12, 14 y 21 Ley 12.008", "SI", "NO",
     ["Identificar el demandado: Provincia, municipio o ente provincial; si es el Estado nacional, ver el cuadro de "
      "equivalencias",
      "Clasificar la pretensión: impugnación de acto, empleo público, tributaria, licitación, responsabilidad, vía "
      "de hecho u omisión",
      "Verificar si el acto agota la vía o si hay una excepción al agotamiento (art. 14 incs. a a d)",
      "Si ya hay un acto que agota la vía, calcular de inmediato el plazo de 90 días (art. 18)",
      "Juzgado en lo Contencioso Administrativo del departamento judicial que corresponda (competencia territorial "
      "a verificar)",
      CHECKLIST_SIN_DATOS],
     ["Acto administrativo y constancia de notificación", "Poder o patrocinio"]),
    (i(30), "Previa", "Vista de las actuaciones administrativas", "ACTORA",
     "Necesidad de conocer el expediente administrativo antes de recurrir o demandar", 0, "SIN_PLAZO", "NO",
     "Art. 11 Decreto-Ley 7647/70 (Ordenanza General 267/80 para municipios)", "NO", "NO",
     ["Pedir vista por escrito y copia de las actuaciones",
      "Verificar si el pedido de vista suspende el plazo para recurrir (a verificar)",
      "Calendario administrativo provincial o municipal según la repartición"],
     ["Pedido de vista con cargo de recepción"]),
    (i(40), "Previa", "Control de la prescripción de la acción de responsabilidad del Estado", "ACTORA",
     "Hecho o acto dañoso, o conocimiento del daño", 3, "ANIOS", "NO",
     "Sin ley provincial de responsabilidad del Estado ni adhesión a la Ley 26.944 (a verificar); por analogía, "
     "art. 7 Ley 26.944 y art. 2561 CCyC (3 años)", "NO", "NO",
     ["Plazo de 3 años por analogía hasta confirmar (ver duda)",
      "La pretensión resarcitoria puede acumularse a la impugnación del acto, con el mismo plazo de caducidad "
      "(art. 20 Ley 12.008), o plantearse en forma autónoma dentro de la prescripción",
      "Verificar si el reclamo administrativo suspende o interrumpe la prescripción (a verificar)"],
     ["Constancias del daño"]),
    # --- Vía administrativa ---
    (i(100), "Vía administrativa", "Reclamo o petición ante la Administración provincial o municipal", "ACTORA",
     "Omisión, hecho o pretensión sin acto previo", 0, "SIN_PLAZO", "NO",
     "Decreto-Ley 7647/70 (Ordenanza General 267/80 para municipios); art. 14 Ley 12.008", "NO", "NO",
     ["Presentar por escrito con constancia de recepción y número de expediente",
      "Precisar la pretensión, incluida la resarcitoria si la hay",
      "La fecha de presentación dispara el plazo para resolver"],
     ["Reclamo con cargo de recepción"]),
    (i(110), "Vía administrativa", "La Administración resuelve el reclamo o la petición", "DEMANDADA",
     "Presentación del reclamo o la petición", 30, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 77 Decreto-Ley 7647/70 (inciso aplicable a verificar)", "NO", "NO",
     ["Calendario administrativo provincial o municipal según la repartición",
      "Si vence sin resolver: pronto despacho (art. 79) o amparo por mora (art. 76 Ley 12.008)",
      "En repetición ante ARBA y en reclamos de empleo público, verificar si hay plazos especiales (a verificar)"],
     []),
    (i(120), "Vía administrativa", "Pedido de pronto despacho", "ACTORA",
     "Vencimiento del plazo para resolver sin respuesta", 0, "SIN_PLAZO", "NO",
     "Art. 79 Decreto-Ley 7647/70; art. 16 Ley 12.008", "NO", "NO",
     ["Presentar por escrito con cargo: su fecha dispara el plazo del silencio",
      "Evaluar el amparo por mora como alternativa"],
     ["Pronto despacho con cargo de recepción"]),
    (i(130), "Vía administrativa", "Silencio: la Administración no resuelve tras el pronto despacho", "DEMANDADA",
     "Presentación del pronto despacho", 30, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 16 Ley 12.008; art. 79 Decreto-Ley 7647/70", "NO", "NO",
     ["Vencidos 30 días hábiles administrativos sin resolución, se presume la denegatoria",
      "Verificar si con denegatoria presunta corre el plazo de caducidad del art. 18 (ver duda)",
      "Calendario administrativo provincial o municipal"],
     []),
    (i(150), "Vía administrativa", "Recurso de revocatoria", "ACTORA",
     "Notificación del acto administrativo", 10, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 74, 89 y 91 Decreto-Ley 7647/70 (Ordenanza General 267/80 para municipios)", "NO", "NO",
     ["Plazo perentorio (art. 74): fundar el recurso y ofrecer prueba",
      "Lleva implícito el jerárquico en subsidio (art. 91): mejora de fundamentos dentro de las 48 horas de "
      "notificada la elevación (cargar como plazo suelto; en municipios, a verificar)",
      "Calendario administrativo provincial o municipal",
      "Vencido el plazo queda la denuncia de ilegitimidad (art. 74), que no habilita la vía judicial (a verificar)"],
     ["Escrito de revocatoria"]),
    (i(160), "Vía administrativa", "La Administración resuelve la revocatoria", "DEMANDADA",
     "Presentación de la revocatoria", 5, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 77 inc. f Decreto-Ley 7647/70", "NO", "NO",
     ["Si se rechaza, se elevan las actuaciones para el jerárquico en subsidio",
      "Si vence sin resolver: pronto despacho o amparo por mora"],
     []),
    (i(170), "Vía administrativa", "Recurso jerárquico", "ACTORA",
     "Notificación del acto de un órgano inferior", 10, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 92 a 100 Decreto-Ley 7647/70", "NO", "NO",
     ["Plazo perentorio: fundar el recurso y ofrecer prueba",
      "Contra actos de entes autárquicos, verificar la apelación del art. 94",
      "Contra actos de alcance general, ver el art. 95 (30 días, a verificar alcance)"],
     ["Escrito de recurso jerárquico"]),
    (i(190), "Vía administrativa", "Resolución del jerárquico (ministro, Poder Ejecutivo o intendente)", "DEMANDADA",
     "Elevación del recurso con los dictámenes finales", 10, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 77 inc. g y art. 101 Decreto-Ley 7647/70", "NO", "NO",
     ["Antes de resolver intervienen la Asesoría General de Gobierno y, si corresponde, la Fiscalía de Estado "
      "(art. 101, alcance a verificar)",
      "Si vence sin resolver: pronto despacho o amparo por mora",
      "En municipios resuelve el intendente (Ordenanza General 267/80)"],
     []),
    (i(195), "Vía administrativa", "Notificación del acto que agota la vía administrativa", "DEMANDADA",
     "Acto definitivo de la autoridad superior o rechazo del último recurso", 0, "SIN_PLAZO", "NO",
     "Arts. 14 y 18 Ley 12.008", "NO", "NO",
     ["Guardar la constancia de notificación: dispara el plazo de 90 días para demandar",
      "Controlar que la notificación sea fehaciente y transcriba el acto (requisitos a verificar)",
      "Si el acto se ejecuta y hay urgencia, pedir la suspensión (art. 25) y la cautelar"],
     ["Acto que agota la vía y constancia de notificación"]),
    # --- Variantes administrativas ---
    (i(210), "Empleo público", "Reclamo del agente público ante la repartición (Ley 10.430 o Ley 14.656)", "ACTORA",
     "Pretensión del agente: diferencias salariales, licencias, reubicación u otra", 0, "SIN_PLAZO", "NO",
     "Ley 10.430 (agentes provinciales) y Ley 14.656 (municipales), a verificar; Decreto-Ley 7647/70", "NO", "NO",
     ["Identificar el régimen estatutario del agente (provincial, municipal o especial)",
      "Si el estatuto tiene recursos propios, verificar sus plazos (a verificar)",
      "En la cautelar solo se exige caución juratoria (art. 24 Ley 12.008)",
      CHECKLIST_SIN_DATOS],
     ["Recibos de haberes", "Acto de designación o constancia de situación de revista"]),
    (i(220), "Empleo público", "Demanda de impugnación de una sanción disciplinaria (arts. 71 a 73 Ley 12.008)",
     "ACTORA", "Notificación del acto sancionatorio que agota la vía", 60, "HABILES_JUDICIALES", "NO",
     "Arts. 71 a 73 Ley 12.008 (trámite especial; plazos a verificar)", "NO", "NO",
     ["Optar por el trámite especial o por el ordinario",
      "Plazo de 60 días (tipo de días y alcance a verificar)",
      "Caducidad de instancia de 3 meses en los procesos especiales (art. 62)",
      *CHECKLIST_COSTOS_PBA],
     ["Demanda", "Acto sancionatorio y constancia de notificación"]),
    (i(240), "Tributario", "Descargo ante la vista de la determinación (ARBA o municipio)", "ACTORA",
     "Notificación de la vista de la determinación de oficio", 15, "HABILES_ADMINISTRATIVOS", "NO",
     "Art. 113 Código Fiscal PBA; municipios: Ordenanza Fiscal (a verificar)", "NO", "NO",
     ["Presentar el descargo y ofrecer prueba",
      "Verificar la prescripción del tributo (a verificar)",
      "Tasas municipales: plazos de la Ordenanza Fiscal del municipio"],
     ["Descargo", "Prueba documental"]),
    (i(250), "Tributario", "Recurso de reconsideración ante ARBA o apelación ante el Tribunal Fiscal", "ACTORA",
     "Notificación de la resolución determinativa o sancionatoria de ARBA", 15, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 115 y 118 Código Fiscal PBA", "NO", "NO",
     ["Plazo excluyente de 15 días: elegir reconsideración ante ARBA o apelación ante el Tribunal Fiscal de "
      "Apelación",
      "La apelación al Tribunal Fiscal exige un monto mínimo (art. 115; valor vigente a verificar)",
      "El recurso suspende la intimación de pago pero no los intereses",
      "ARBA resuelve la reconsideración en 60 días (art. 118)"],
     ["Recurso"]),
    (i(270), "Tributario", "Sentencia del Tribunal Fiscal de Apelación", "TRIBUNAL",
     "Apelación concedida y elevada al Tribunal Fiscal (art. 121 Código Fiscal)", 0, "SIN_PLAZO", "NO",
     "Arts. 115 a 121 Código Fiscal PBA; art. 60 inc. 3 Ley 12.008", "NO", "NO",
     ["Controlar los plazos del trámite ante el Tribunal Fiscal (a verificar)",
      "Contra la sentencia: verificar si se demanda en el fuero contencioso o se recurre ante la Cámara, y en qué "
      "plazo (ver duda)",
      "Para demandar hay que pagar antes el tributo (art. 19 Ley 12.008)"],
     ["Sentencia del Tribunal Fiscal"]),
    (i(280), "Tributario", "Pago previo del tributo para demandar", "ACTORA",
     "Intimación judicial a pagar el tributo (art. 19)", 10, "HABILES_JUDICIALES", "SI",
     "Art. 19 Ley 12.008; art. 119 Código Fiscal PBA", "NO", "NO",
     ["Pagar o acreditar el pago dentro de los 10 días de la intimación",
      "El pago previo no alcanza a las multas",
      "Verificar las excepciones al pago previo (a verificar)"],
     ["Comprobante de pago"]),
    (i(285), "Tributario", "Reclamo de repetición de un tributo pagado indebidamente", "ACTORA",
     "Pago del tributo que se considera indebido", 0, "SIN_PLAZO", "NO",
     "Código Fiscal PBA (repetición, artículos a verificar); municipios: Ordenanza Fiscal", "NO", "NO",
     ["Verificar el plazo de prescripción de la repetición (a verificar)",
      "Acompañar los comprobantes de pago"],
     ["Reclamo de repetición", "Comprobantes de pago"]),
    (i(290), "Licitaciones", "Impugnación del dictamen de preadjudicación", "ACTORA",
     "Notificación o publicación del dictamen de preadjudicación", 0, "SIN_PLAZO", "NO",
     "Ley 13.981 y Decreto 59/19 (Provincia); Ley Orgánica de las Municipalidades (municipios); plazos a verificar",
     "NO", "NO",
     ["El plazo y la garantía de impugnación los fija la reglamentación o el pliego: cargar el plazo como plazo "
      "suelto",
      "Contra la adjudicación: recursos del Decreto-Ley 7647/70",
      "Si hay urgencia: cautelar anticipada (art. 23 Ley 12.008)"],
     ["Impugnación", "Garantía de impugnación"]),
    # --- Amparo por mora ---
    (i(300), "Amparo por mora", "Demanda de amparo por mora de la Administración", "ACTORA",
     "Vencimiento de los plazos para resolver sin respuesta", 0, "SIN_PLAZO", "NO", "Art. 76 Ley 12.008", "NO", "NO",
     ["Acreditar la petición y el vencimiento del plazo para resolver",
      "No reemplaza la demanda de fondo: si hay acto que agota la vía, seguir controlando la caducidad",
      *CHECKLIST_COSTOS_PBA],
     ["Demanda", "Constancia del reclamo pendiente"]),
    (i(310), "Amparo por mora", "Informe de la Administración sobre la demora", "DEMANDADA",
     "Notificación del pedido de informe", 5, "HABILES_JUDICIALES", "SI", "Art. 76 Ley 12.008", "NO", "NO",
     ["El juez fija el plazo, que no puede exceder de 5 días: si fija otro, cargarlo como plazo suelto"],
     ["Informe"]),
    (i(320), "Amparo por mora", "Orden judicial de pronto despacho", "TRIBUNAL",
     "Informe presentado o vencido el plazo", 0, "SIN_PLAZO", "NO", "Art. 76 Ley 12.008", "NO", "NO",
     ["La resolución es irrecurrible (alcance a verificar)",
      "Cargar como plazo suelto el plazo que fija el juez para que la Administración resuelva",
      "Si no cumple: astreintes y responsabilidad del funcionario"],
     ["Resolución"]),
    # --- Demanda ---
    (i(400), "Demanda", "Control del plazo de caducidad para demandar (90 días)", "ACTORA",
     "Notificación del acto que agota la vía o del rechazo del recurso, o conocimiento de la vía de hecho", 90,
     "HABILES_JUDICIALES", "NO", "Arts. 18 y 20 Ley 12.008", "NO", "NO",
     ["Plazo perentorio desde el día siguiente a la notificación",
      "Con denegatoria presunta por silencio, verificar si corre (ver duda)",
      "La pretensión resarcitoria puede acumularse en el mismo plazo (art. 20)",
      "Sin gracia hasta que se resuelva la duda transversal"],
     []),
    (i(410), "Demanda", "Demanda contencioso administrativa", "ACTORA",
     "Decisión de demandar con la vía agotada, con denegatoria presunta o en un caso exceptuado", 0, "SIN_PLAZO",
     "NO", "Arts. 12, 20, 27 y 28 Ley 12.008", "NO", "NO",
     ["Cumplir los requisitos del art. 27: pretensión, acto impugnado, hechos, derecho y prueba",
      "Acumular la pretensión resarcitoria si corresponde (art. 20)",
      "Acompañar el acto que agota la vía y la constancia de notificación",
      "Demanda tributaria: acreditar el pago previo (art. 19)",
      "Pedir la remisión del expediente administrativo (art. 30)",
      *CHECKLIST_COSTOS_PBA],
     ["Demanda", "Poder o patrocinio", "Acto impugnado y constancia de notificación", "Prueba documental",
      "Comprobantes de tasa, bono y anticipo previsional"]),
    (i(420), "Demanda", "Remisión del expediente administrativo por la demandada", "DEMANDADA",
     "Notificación del requerimiento de remisión", 15, "HABILES_JUDICIALES", "NO", "Art. 30 Ley 12.008", "NO", "NO",
     ["Si no lo remite, pedir la intimación y las consecuencias que prevé la ley (a verificar)"],
     ["Expediente administrativo"]),
    (i(430), "Demanda", "Control de admisibilidad de la demanda", "TRIBUNAL",
     "Recepción del expediente administrativo o vencimiento del plazo de remisión", 0, "SIN_PLAZO", "NO",
     "Art. 31 Ley 12.008", "NO", "NO",
     ["El juez controla agotamiento, plazo y requisitos antes del traslado",
      "Si hay defectos subsanables, intima a corregirlos en un plazo no menor de 5 días: cargarlo como plazo suelto",
      "La declaración de inadmisibilidad es apelable (art. 55)"],
     ["Providencia de admisibilidad"]),
    (i(440), "Demanda", "Traslado de la demanda y notificación a la Fiscalía de Estado o al municipio", "TRIBUNAL",
     "Demanda admitida", 0, "SIN_PLAZO", "NO",
     "Art. 33 Ley 12.008; Decreto-Ley 7543/69 (Fiscalía de Estado, a verificar)", "NO", "NO",
     ["Provincia: se notifica al Fiscal de Estado; municipio: al intendente (y al presidente del Concejo Deliberante "
      "si se impugna una ordenanza); ente: a su autoridad superior",
      "Controlar el domicilio y la fecha de notificación: disparan los plazos de excepciones y contestación"],
     ["Cédula u oficio de traslado"]),
    (i(450), "Demanda", "Excepciones previas", "DEMANDADA",
     "Notificación del traslado de la demanda", 15, "HABILES_JUDICIALES", "SI", "Art. 34 Ley 12.008", "NO", "NO",
     ["Se oponen dentro de los primeros 15 días del plazo para contestar y suspenden ese plazo",
      "La actora contesta el traslado de las excepciones en 5 días: cargar como plazo suelto"],
     ["Escrito de excepciones"]),
    (i(460), "Demanda", "Contestación de la demanda por la Provincia, el municipio o el ente", "DEMANDADA",
     "Notificación del traslado de la demanda", 45, "HABILES_JUDICIALES", "SI", "Arts. 37 a 39 Ley 12.008", "NO",
     "NO",
     ["Plazo común de 45 días; si se opusieron excepciones, se reanuda al resolverse (art. 34)",
      "Si reconviene, la actora contesta en 30 días (art. 39): cargar como plazo suelto",
      "Controlar si niega hechos o documentos"],
     ["Contestación"]),
    (i(470), "Demanda", "Contestación del traslado de la documental de la demandada", "ACTORA",
     "Notificación del traslado de los documentos acompañados con la contestación", 5, "HABILES_JUDICIALES", "SI",
     "Art. 40 Ley 12.008", "NO", "NO",
     ["Reconocer o desconocer cada documento",
      "Ofrecer prueba sobre hechos nuevos si corresponde"],
     ["Escrito de contestación del traslado"]),
    # --- Sumario de ilegitimidad ---
    (i(405), "Sumario de ilegitimidad", "Demanda por el proceso sumario de ilegitimidad", "ACTORA",
     "Notificación del acto que agota la vía (opción por el proceso sumario)", 60, "HABILES_JUDICIALES", "NO",
     "Arts. 67 a 70 Ley 12.008", "NO", "NO",
     ["Procede para la nulidad de actos con prueba documental (requisitos del art. 67 a verificar)",
      "Plazo de 60 días para demandar (a verificar si desplaza el de 90 días del art. 18)",
      "Sin audiencia; solo prueba documental",
      *CHECKLIST_COSTOS_PBA],
     ["Demanda", "Prueba documental"]),
    (i(407), "Sumario de ilegitimidad", "Contestación en el proceso sumario de ilegitimidad", "DEMANDADA",
     "Notificación del traslado de la demanda", 20, "HABILES_JUDICIALES", "SI", "Arts. 68 y 69 Ley 12.008", "NO", "NO",
     ["La demandada puede oponerse al trámite sumario dentro de 5 días (a verificar)",
      "Después de la contestación, alegato en 5 días (a verificar): cargar como plazo suelto"],
     ["Contestación"]),
    (i(409), "Sumario de ilegitimidad", "Sentencia en el proceso sumario de ilegitimidad", "TRIBUNAL",
     "Alegatos presentados o vencido el plazo", 30, "HABILES_JUDICIALES", "NO", "Art. 70 Ley 12.008", "NO", "NO",
     ["Controlar el plazo y pedir pronto despacho si se demora"],
     ["Sentencia"]),
    # --- Prueba y sentencia ---
    (i(480), "Prueba", "Audiencia del art. 41 (hechos, prueba o puro derecho)", "AMBAS",
     "Fecha y hora fijadas por el juez (dentro de los 15 días)", 0, "FECHA_FIJADA", "NO", "Art. 41 Ley 12.008", "NO",
     "NO",
     ["Se fijan los hechos controvertidos y la prueba, o se declara la cuestión de puro derecho",
      "Llevar propuesta si hay margen de conciliación: la demandada necesita autorización (art. 61)"],
     ["Acta de la audiencia"]),
    (i(490), "Prueba", "Producción de la prueba", "AMBAS",
     "Apertura a prueba en la audiencia del art. 41", 0, "SIN_PLAZO", "NO",
     "Arts. 42 a 47 Ley 12.008 (plazo máximo de 40 días; numeración a verificar)", "NO", "NO",
     ["El juez fija el plazo de prueba: cargar la fecha de clausura como plazo suelto",
      "Urgir informes y pericias para evitar la negligencia",
      "Controlar el traslado del dictamen pericial (plazo a verificar)"],
     ["Escritos de prueba"]),
    (i(500), "Prueba", "Alegatos", "AMBAS",
     "Notificación de la clausura del período de prueba", 10, "HABILES_JUDICIALES", "SI", "Art. 48 Ley 12.008",
     "NO", "NO",
     ["Plazo común de 10 días", "Alegar sobre el mérito de la prueba"],
     ["Alegato"]),
    (i(510), "Sentencia", "Sentencia de primera instancia", "TRIBUNAL",
     "Llamamiento de autos para sentencia firme", 60, "HABILES_JUDICIALES", "NO", "Art. 49 Ley 12.008", "NO", "NO",
     ["Si vence, pedir pronto despacho",
      "Aclaratoria en 5 días (art. 52); reposición de providencias simples en 3 días (art. 53)"],
     ["Sentencia"]),
    # --- Cierre ---
    (i(900), "Cierre", "Acuerdo, conciliación o transacción con el Estado", "AMBAS",
     "Propuesta de acuerdo", 0, "SIN_PLAZO", "NO", "Art. 61 Ley 12.008", "NO", "NO",
     ["La representación del Estado necesita autorización de la autoridad competente",
      "Pedir la homologación",
      "Prever forma de pago, costas y honorarios"],
     ["Acuerdo", "Acto que autoriza el acuerdo", "Resolución homologatoria"]),
    (i(910), "Cierre", "Control de caducidad de instancia", "ACTORA",
     "Último acto de impulso del proceso", 6, "MESES", "NO", "Art. 62 Ley 12.008", "NO", "NO",
     ["Seis meses en el proceso ordinario; tres en los procesos especiales del Título II y en el del art. 21",
      "Cada acto de impulso reinicia el plazo: actualizar el disparador",
      "Verificar si las ferias se descuentan (CPCCBA supletorio, a verificar)"],
     []),
    (i(980), "Cierre", "Sigue en la matriz de amparo", "ACTORA",
     "Urgencia o lesión manifiesta que hace del amparo la vía idónea", 0, "SIN_PLAZO", "NO",
     "Art. 20 inc. 2 Constitución PBA; Ley 13.928", "NO", "SI",
     ["Crear el expediente vinculado en la matriz de amparo",
      "Controlar el plazo de 30 días del amparo (art. 5 Ley 13.928)"],
     []),
    (i(985), "Cierre", "Estado nacional demandado: fuera de esta matriz", "ACTORA",
     "El acto, la omisión o el hecho es del Estado nacional o de un ente nacional", 0, "SIN_PLAZO", "NO",
     "Ley 19.549 reformada por la Ley 27.742; CPCCN; Ley 26.854", "NO", "SI",
     ["Ver el cuadro de equivalencias en publico/README.md",
      "Cargar desde ya los plazos de la Ley 19.549 como plazos sueltos (por ejemplo, 180 días hábiles judiciales "
      "del art. 25)"],
     []),
    (i(990), "Cierre", "Cierre y archivo del caso", "AMBAS",
     "Cumplimiento de la sentencia o del acuerdo, caducidad, desistimiento o resolución favorable en sede "
     "administrativa", 0, "SIN_PLAZO", "NO", "Reglamento de archivo de la SCBA (a verificar)", "NO", "SI",
     ["Verificar pagos, honorarios y aportes",
      "Devolver la documentación original al cliente"],
     ["Constancia de archivo"]),
]

CAUT_NODOS, CAUT_TRANS = bloque_cautelar(P, 600, pba="CCA", salidas={"demanda": i(410)})
REC_NODOS, REC_TRANS = recursos_cca(P, 700, i(750))
EJE_NODOS, EJE_TRANS = ejecucion_estado(P, 800, "PBA", i(950))
HON_NODOS, HON_TRANS = honorarios(P, 950, "PBA", i(990))
NODOS += CAUT_NODOS + REC_NODOS + EJE_NODOS + HON_NODOS

sin_resolver = [
    ("Vence sin resolver: pronto despacho", i(120)),
    ("Vence sin resolver: amparo por mora", i(300)),
]

TRANSICIONES = [
    # Encuadre
    (i(10), "Acto que no agota la vía: recurso de revocatoria", i(150)),
    (i(10), "Acto de un órgano inferior: recurso jerárquico", i(170)),
    (i(10), "No hay acto: reclamo o petición a la Administración", i(100)),
    (i(10), "Empleo público: reclamo del agente", i(210)),
    (i(10), "Empleo público: sanción disciplinaria que agota la vía", i(220)),
    (i(10), "Tributario: vista de una determinación de ARBA o de una tasa municipal", i(240)),
    (i(10), "Tributario: repetición de un pago indebido", i(285)),
    (i(10), "Licitación: impugnación de la preadjudicación", i(290)),
    (i(10), "Responsabilidad del Estado: reclamo y control de la prescripción", i(40)),
    (i(10), "Responsabilidad del Estado: reclamo y control de la prescripción", i(100)),
    (i(10), "El acto ya agota la vía, hay excepción al agotamiento (art. 14) o vía de hecho (art. 21)", i(400)),
    (i(10), "El acto ya agota la vía, hay excepción al agotamiento (art. 14) o vía de hecho (art. 21)", i(410)),
    (i(10), "El acto agota la vía y se opta por el proceso sumario de ilegitimidad", i(405)),
    (i(10), "Hace falta conocer las actuaciones: pedir vista", i(30)),
    (i(10), "Urgencia que hace del amparo la vía idónea", i(980)),
    (i(10), "El demandado es el Estado nacional", i(985)),
    (i(30), "Vista tomada: definir la vía", CIERRA),
    (i(40), "Reclamo o demanda presentados antes del vencimiento", CIERRA),
    (i(40), "Venció la prescripción sin reclamar", i(990)),
    # Vía administrativa
    (i(100), "Reclamo presentado", i(110)),
    (i(110), "Resuelve en contra con un acto que no agota la vía", i(150)),
    (i(110), "Resuelve en contra con un acto que agota la vía", i(195)),
    (i(110), "Resuelve a favor", i(990)),
    *[(i(110), c, d) for c, d in sin_resolver],
    (i(120), "Pronto despacho presentado", i(130)),
    (i(130), "Vence sin resolver: denegatoria presunta", i(400)),
    (i(130), "Vence sin resolver: denegatoria presunta", i(410)),
    (i(130), "Resuelve en contra con un acto que no agota la vía", i(150)),
    (i(130), "Resuelve en contra con un acto que agota la vía", i(195)),
    (i(130), "Resuelve a favor", i(990)),
    (i(150), "Revocatoria presentada", i(160)),
    (i(160), "Rechazada: se eleva el jerárquico en subsidio", i(190)),
    (i(160), "Rechazada por la autoridad superior: el acto agota la vía", i(195)),
    (i(160), "Revocatoria acogida", i(990)),
    *[(i(160), c, d) for c, d in sin_resolver],
    (i(170), "Jerárquico presentado", i(190)),
    (i(190), "Rechazado: acto que agota la vía", i(195)),
    (i(190), "Jerárquico acogido", i(990)),
    *[(i(190), c, d) for c, d in sin_resolver],
    (i(195), "Vía agotada: corre el plazo para demandar", i(400)),
    (i(195), "Vía agotada: corre el plazo para demandar", i(410)),
    (i(195), "Se opta por el proceso sumario de ilegitimidad", i(405)),
    (i(195), "Hay urgencia: se pide la cautelar antes de demandar", i(600)),
    # Variantes administrativas
    (i(210), "Reclamo presentado ante la repartición", i(110)),
    (i(220), "Demanda presentada", i(430)),
    (i(240), "ARBA dicta la determinación", i(250)),
    (i(240), "El municipio dicta la determinación: recursos de la Ordenanza General 267/80", i(150)),
    (i(250), "Apelación ante el Tribunal Fiscal de Apelación", i(270)),
    (i(250), "Reconsideración rechazada por ARBA: queda abierta la vía judicial", i(400)),
    (i(250), "Reconsideración rechazada por ARBA: queda abierta la vía judicial", i(410)),
    (i(250), "Recurso acogido", i(990)),
    (i(270), "Sentencia desfavorable: queda abierta la vía judicial", i(400)),
    (i(270), "Sentencia desfavorable: queda abierta la vía judicial", i(410)),
    (i(270), "Sentencia favorable firme", i(990)),
    (i(280), "Pago acreditado o excepción admitida", i(440)),
    (i(280), "Vencido sin pagar: se rechaza la demanda", i(950)),
    (i(285), "Reclamo de repetición presentado", i(110)),
    (i(290), "Adjudicación notificada: recurso administrativo", i(150)),
    (i(290), "Hay urgencia: cautelar anticipada", i(600)),
    # Amparo por mora
    (i(300), "Demanda presentada y pedido de informe", i(310)),
    (i(310), "Informe presentado o vencido el plazo", i(320)),
    (i(320), "Orden cumplida: acto en contra que no agota la vía", i(150)),
    (i(320), "Orden cumplida: acto en contra que agota la vía", i(195)),
    (i(320), "Orden cumplida: acto favorable", i(990)),
    (i(320), "Amparo por mora rechazado o la Administración no cumple: evaluar demanda de fondo", i(410)),
    # Demanda
    (i(400), "Demanda presentada en plazo", CIERRA),
    (i(400), "Venció el plazo sin demandar: caducidad", i(990)),
    (i(410), "Demanda presentada", i(420)),
    (i(410), "Demanda presentada", i(910)),
    (i(410), "Se pide una medida cautelar con la demanda", i(600)),
    (i(420), "Expediente remitido o vencido el plazo", i(430)),
    (i(430), "Demanda admitida", i(440)),
    (i(430), "Demanda tributaria sin pago previo acreditado: intimación", i(280)),
    (i(430), "Demanda declarada inadmisible: se apela", i(700)),
    (i(440), "Traslado notificado", i(450)),
    (i(440), "Traslado notificado", i(460)),
    (i(450), "Excepciones resueltas o no opuestas", CIERRA),
    (i(450), "Excepción admitida que termina el proceso: se apela", i(700)),
    (i(460), "Contestada con documental: traslado a la actora", i(470)),
    (i(460), "Contestada o vencido el plazo, sin documental nueva", i(480)),
    (i(460), "Allanamiento o propuesta de acuerdo", i(900)),
    (i(470), "Traslado contestado o vencido el plazo", i(480)),
    # Sumario de ilegitimidad
    (i(405), "Demanda admitida y traslado notificado", i(407)),
    (i(405), "Demanda admitida y traslado notificado", i(910)),
    (i(407), "Contestada o vencido el plazo, y alegatos", i(409)),
    (i(407), "Oposición admitida: sigue por el trámite ordinario", i(480)),
    (i(409), "Sentencia notificada", i(700)),
    # Prueba y sentencia
    (i(480), "Hay hechos controvertidos: apertura a prueba", i(490)),
    (i(480), "Cuestión de puro derecho", i(510)),
    (i(480), "Acuerdo en la audiencia", i(900)),
    (i(490), "Prueba producida o vencido el plazo", i(500)),
    (i(500), "Alegatos presentados o vencido el plazo", i(510)),
    (i(510), "Sentencia notificada", i(700)),
    # Sentencia firme
    (i(750), "Condena contra la Provincia, el municipio o el ente", i(800)),
    (i(750), "Rechazo o sentencia sin condena que ejecutar", i(950)),
    # Cierre
    (i(900), "Acuerdo homologado y cumplido", i(950)),
    (i(910), "Se dicta sentencia o termina el proceso", CIERRA),
    (i(910), "Caducidad de instancia declarada", i(950)),
] + CAUT_TRANS + REC_TRANS + EJE_TRANS + HON_TRANS

NODOS, TRANSICIONES = ordenar(NODOS, TRANSICIONES)

DUDAS_PROPIAS = [
    ("Caducidad del art. 18 y silencio",
     "Art. 18 Ley 12.008: 90 días perentorios desde la notificación del acto que agota la vía o del rechazo del "
     "recurso. ¿Son días hábiles judiciales? ¿Corre el plazo cuando se demanda por denegatoria presunta (art. 16), o "
     "con silencio se puede demandar en cualquier momento? Propuesta: 90 hábiles judiciales sin gracia, y abrir el "
     "control también con silencio (vencimiento más temprano). " + FUENTE_CCA,
     "CAD_130, CAD_400"),
    ("Agotamiento obligatorio y excepciones",
     "Art. 14 Ley 12.008: el agotamiento es obligatorio salvo los incisos a) a d). ¿Qué supuestos usa más la "
     "práctica (acto de la autoridad superior, ritualismo inútil, vía de hecho, actos de alcance general)? ¿Cómo "
     "juegan los actos de entes reguladores y tribunales administrativos (art. 15)? Propuesta: transición directa a la "
     "demanda solo con acto que agota la vía o excepción del art. 14. " + FUENTE_CCA,
     "CAD_010, CAD_195"),
    ("Plazos de la Administración para resolver",
     "Art. 77 Decreto-Ley 7647/70: revocatoria 5 días (inc. f), jerárquico 10 días y otras decisiones definitivas 30 "
     "días (inc. g). ¿Es correcto usar 30 días hábiles administrativos para reclamos y peticiones? ¿La Ordenanza "
     "General 267/80 tiene los mismos plazos para los municipios? Propuesta: sí, con checklist que pide verificar "
     "plazos especiales. " + FUENTE_7647,
     "CAD_110, CAD_160, CAD_190"),
    ("Mejora de fundamentos y denuncia de ilegitimidad",
     "Art. 91 Decreto-Ley 7647/70: el jerárquico en subsidio admite mejorar fundamentos dentro de las 48 horas de "
     "notificada la elevación; algunas ordenanzas municipales hablan de 2 días hábiles. ¿Se carga como plazo suelto "
     "en HORAS? ¿La denuncia de ilegitimidad (art. 74) habilita la vía judicial? Propuesta: plazo suelto de 48 horas "
     "y la denuncia no habilita la demanda. " + FUENTE_7647,
     "CAD_150"),
    ("Vista de las actuaciones",
     "Art. 11 Decreto-Ley 7647/70: ¿el pedido de vista suspende el plazo para recurrir, como en el orden nacional? "
     "Propuesta: no suspende hasta que se confirme (vencimiento más temprano). " + FUENTE_7647,
     "CAD_030"),
    ("Empleo público y sanciones",
     "¿Qué recursos propios tienen la Ley 10.430 (agentes provinciales) y la Ley 14.656 (municipales), y con qué "
     "plazos? ¿El trámite especial de impugnación de sanciones (arts. 71 a 73 Ley 12.008) se demanda en 60 días "
     "hábiles judiciales y es optativo frente al ordinario? Propuesta: 60 días hábiles judiciales sin gracia. Normas "
     "a verificar.",
     "CAD_210, CAD_220"),
    ("Tributario: Tribunal Fiscal y vía judicial",
     "Art. 115 Código Fiscal: 15 días para reconsideración ante ARBA o apelación ante el Tribunal Fiscal (monto "
     "mínimo según el texto consultado; valor vigente a verificar). ¿Son días hábiles administrativos? Contra la "
     "sentencia del Tribunal Fiscal, ¿se demanda ante el Juzgado Contencioso Administrativo dentro de los 90 días "
     "del art. 18 o se recurre ante la Cámara? ¿Cómo se repite (artículos y plazo de prescripción)? Propuesta: 15 "
     "hábiles administrativos y demanda con el plazo del art. 18. " + FUENTE_CF,
     "CAD_240, CAD_250, CAD_270, CAD_280, CAD_285"),
    ("Licitaciones",
     "Ley 13.981 y Decreto 59/19: ¿cuál es el plazo para impugnar la preadjudicación y qué garantía exige? ¿Y en los "
     "municipios (Ley Orgánica de las Municipalidades)? Propuesta: SIN_PLAZO con carga manual del plazo del pliego "
     "hasta confirmar. Normas a verificar.",
     "CAD_290"),
    ("Responsabilidad del Estado provincial",
     "Al 13/11/2026 la Provincia no tiene ley de responsabilidad del Estado ni adhirió a la Ley 26.944 (hay un "
     "proyecto de mayo de 2026 en el Senado bonaerense, a verificar su estado). La jurisprudencia aplica el CCyC por "
     "analogía. ¿El plazo de prescripción es de 3 años (art. 2561 CCyC o art. 7 Ley 26.944)? ¿El reclamo previo es "
     "obligatorio? Propuesta: 3 años desde el hecho y reclamo optativo.",
     "CAD_040, CAD_100"),
    ("Notificación a la Fiscalía de Estado y cómputo de la contestación",
     "Art. 33 Ley 12.008: se notifica al Fiscal de Estado (Provincia), al intendente (municipio) o a la autoridad "
     "superior del ente. ¿El plazo de 45 días de la contestación corre desde esa notificación? ¿El Decreto-Ley "
     "7543/69 agrega plazos o recaudos? Propuesta: sí, desde la notificación del traslado. " + FUENTE_CCA,
     "CAD_440, CAD_450, CAD_460"),
    ("Plazo de prueba y numeración",
     "La Ley 12.008 fija un plazo de prueba que fija el juez (máximo de 40 días según el texto consultado), pero la "
     "numeración de los arts. 42 y 43 no es clara en la fuente (uno figura vetado). ¿Cuál es el artículo y el "
     "máximo vigente? Propuesta: SIN_PLAZO con carga manual de la fecha de clausura. " + FUENTE_CCA,
     "CAD_490"),
    ("Proceso sumario de ilegitimidad",
     "Arts. 67 a 70 Ley 12.008: demanda en 60 días, oposición de la demandada en 5 días, contestación en 20 días, "
     "alegato en 5 días y sentencia en 30 días, solo con prueba documental. ¿Se confirman? ¿El plazo de 60 días "
     "reemplaza al de 90 días del art. 18? Propuesta: modelar como opción con su propio plazo. " + FUENTE_CCA,
     "CAD_405, CAD_407, CAD_409"),
    ("Ejecución contra la Provincia y los municipios",
     "Art. 63 Ley 12.008 y art. 163 Constitución PBA: plazo de 60 días para cumplir (¿hábiles judiciales?); "
     "art. 65: el Estado puede pedir la suspensión en 20 días. ¿Qué régimen de previsión presupuestaria, "
     "inembargabilidad y, si existe, consolidación rige al 13/11/2026 para la Provincia y los municipios? ¿Qué tasa "
     "de interés usa la SCBA? Propuesta: 60 hábiles judiciales y checklist de verificación. Normas a verificar.",
     "CAD_800, CAD_810, CAD_820, CAD_830, CAD_840"),
    ("Amparo por mora",
     "Art. 76 Ley 12.008: informe en el plazo que fija el juez (no más de 5 días) y orden de pronto despacho "
     "irrecurrible. ¿El amparo por mora suspende o interrumpe algún plazo de caducidad? ¿Qué pasa si la "
     "Administración no cumple la orden? Propuesta: no suspende nada; si no cumple, astreintes y demanda de fondo. "
     + FUENTE_CCA,
     "CAD_300, CAD_310, CAD_320"),
    ("Cautelares contra el Estado provincial",
     "Art. 23: la cautelar anticipada caduca si no se demanda en 30 días; ¿cómo se computa si la vía administrativa "
     "sigue abierta? Art. 25: para suspender un acto hay que pedirlo antes en sede administrativa (5 días hábiles, "
     "silencio = denegatoria). ¿Se confirma que el pedido administrativo es requisito y no solo optativo? Propuesta: "
     "requisito, como está en el diagrama. " + FUENTE_CCA,
     "CAD_600, CAD_605, CAD_610, CAD_630"),
    ("Competencia territorial de los juzgados en lo Contencioso Administrativo",
     "¿Qué juzgado corresponde según el domicilio del actor, el de la repartición o el lugar del acto, y qué Cámara "
     "de Apelación en lo Contencioso Administrativo es la alzada de cada departamento judicial? Propuesta: "
     "checklist en el encuadre hasta confirmar; afecta el calendario de asuetos departamentales.",
     "CAD_010, CAD_410"),
]

DUDAS = numerar(DUDAS_PROPIAS + DUDAS_TRANSVERSALES + DUDAS_PRODUCTO)
