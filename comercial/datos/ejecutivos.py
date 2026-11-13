from comun import (CHECKLIST_COSTOS_INICIO, CON_GRACIA, CON_VALOR_CERO, DUDA_TRANSVERSAL, ESTADOS, PLAZO_TIPOS, ROLES,
                   bloque_ejecucion, etapa_contenciosa, flujo)
from comun import FASES as FASES_BASE
from comun import GRUPOS as GRUPOS_BASE
from comun import LEYENDA as LEYENDA_BASE

FASES = FASES_BASE[:1] + ["Preparación", "Intimación y excepciones"] + FASES_BASE[1:]

GRUPOS = GRUPOS_BASE[:1] + [
    ("Juicio ejecutivo: demanda y preparación de la vía", ["Preparación"]),
    ("Juicio ejecutivo: intimación, excepciones y sentencia de remate", ["Intimación y excepciones"]),
    ("Cobro de pesos: demanda y contestación", ["Postulación"]),
] + GRUPOS_BASE[2:]

ROL_TEXTO = {"ACTORA": "Acreedor ejecutante", "DEMANDADA": "Deudor ejecutado", "TRIBUNAL": "Juzgado",
             "AMBAS": "Ambas partes"}

EJEMPLO_PARALELO = "al presentar la demanda corre la caducidad de instancia mientras avanza la ejecución"

LEYENDA = {
    "roles": "celeste = acreedor ejecutante; naranja = deudor ejecutado (librador, suscriptor, avalistas o "
             "endosantes); gris = juzgado, oficial de justicia o martillero; violeta = cualquiera de las partes.",
    "paralelo": EJEMPLO_PARALELO,
    "adicionales": LEYENDA_BASE["adicionales"] + [
        "**Dos puertas al juicio:** el juicio ejecutivo (título que trae aparejada ejecución) y el cobro de pesos "
        "por juicio sumario (sin título ejecutivo o con la vía ejecutiva frustrada). Las dos terminan en la sentencia "
        "firme y comparten la ejecución, la subasta y el cierre.",
    ],
}

ROLES_DESCRIPCION = [
    ("ACTORA", "Debe actuar el acreedor ejecutante (portador del cheque o del pagaré, emisor de la factura, "
               "entidad emisora de la tarjeta)."),
    ("DEMANDADA", "Debe actuar el deudor ejecutado (librador, suscriptor, avalistas o endosantes)."),
    ("TRIBUNAL", "Depende del juzgado, del oficial de justicia o del martillero (la app muestra 'Esperando "
                 "resolución')."),
    ("AMBAS", "Puede o debe actuar cualquiera de las partes (recursos, audiencias, mediación, impugnaciones)."),
]

FLUJO = flujo(
    "Juicios ejecutivos y cobro de pesos - Provincia de Buenos Aires",
    "CPCCBA (Decreto-Ley 7425/68), arts. 518 a 593 (juicio ejecutivo) y 484 a 495 (sumario); Ley 24.452 (cheques); "
    "Decreto-Ley 5965/63 (pagaré); Ley 25.065 (tarjetas de crédito); Ley 27.440 (factura de crédito electrónica); "
    "Ley 13.951 (mediación)",
    "Cobro de cheques, echeqs y cheques de pago diferido, pagarés, saldos de tarjeta de crédito y facturas de "
    "crédito electrónicas por juicio ejecutivo, y de créditos sin título ejecutivo por cobro de pesos en juicio "
    "sumario. El cumplimiento de la sentencia (embargo, subasta y pago) es el bloque común de las matrices "
    "comerciales. Si el deudor se concursa o quiebra, el expediente sigue en la matriz de concursos. Las citas "
    "marcadas 'a verificar' no se usan hasta que el abogado las confirme.",
)

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
PROPIOS = [
    ("EJE_010", "Previa", "Mora del deudor y elección de la vía", "ACTORA",
     "Vencimiento impago del título o primera consulta del cliente", 0, "SIN_PLAZO", "NO",
     "Arts. 518 a 522 CPCCBA; arts. 1 y 36 Ley 24.240", "SI", "NO",
     ["Identificar el título: cheque, echeq o cheque de pago diferido; pagaré; resumen de tarjeta de crédito; "
      "factura de crédito electrónica; otro título del art. 521; o crédito sin título ejecutivo (cobro de pesos)",
      "Verificar si hay relación de consumo: el juez puede declarar de oficio la incompetencia por el domicilio "
      "real del consumidor (duda D02)",
      "Factura de crédito electrónica: verificar en el registro de AFIP-ARCA que esté aceptada en forma expresa o "
      "tácita (art. 6 Ley 27.440; duda D05)",
      "Definir el juzgado competente por domicilio y monto (Juzgado Civil y Comercial o Juzgado de Paz; duda D01)",
      "Consultar los registros de concursos y quiebras: si el deudor está concursado, no se inicia la ejecución"],
     ["Título original", "Constancias del registro de facturas (si es factura de crédito electrónica)"]),
    ("EJE_020", "Previa", "Aviso del rechazo del cheque al librador y endosantes", "ACTORA",
     "Rechazo del cheque o echeq por el banco girado", 2, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 38 y 39 Ley 24.452", "NO", "NO",
     ["La constancia de rechazo del banco produce los efectos del protesto y habilita la acción ejecutiva "
      "(art. 38)",
      "Dar aviso del rechazo al librador y a los endosantes dentro de los 2 días hábiles bancarios (art. 39); "
      "verificar si la omisión hace perder la acción o solo genera responsabilidad (a verificar)",
      "Echeq: pedir el certificado para acciones civiles (art. 61 Ley 24.452, texto Ley 27.444)",
      "Cheque de pago diferido rechazado por falta de registración: también habilita la vía ejecutiva (art. 57)"],
     ["Cheque con constancia de rechazo o certificado del echeq", "Constancia del aviso (carta documento)"]),
    ("EJE_025", "Previa", "Protesto del pagaré por falta de pago", "ACTORA",
     "Vencimiento del pagaré", 2, "HABILES_ADMINISTRATIVOS", "NO",
     "Arts. 48, 49, 50 y 103 Decreto-Ley 5965/63", "NO", "NO",
     ["Solo si el pagaré no tiene la cláusula 'sin protesto' (art. 50): con esa cláusula se cierra este camino",
      "Hacer el protesto ante escribano en uno de los 2 días hábiles siguientes al vencimiento (art. 48)",
      "Dar los avisos a los endosantes y avalistas en el plazo del art. 49 (a verificar el plazo)",
      "La falta de protesto hace perder las acciones de regreso contra los endosantes, no contra el suscriptor "
      "(art. 60, a verificar)"],
     ["Acta de protesto", "Constancia de los avisos"]),
    ("EJE_030", "Previa", "Control de la prescripción de la acción", "ACTORA",
     "Vencimiento del título (en el cheque, fin del plazo de presentación)", 1, "ANIOS", "NO",
     "Art. 61 Ley 24.452; art. 96 Decreto-Ley 5965/63; art. 47 Ley 25.065; art. 2560 CCyC", "NO", "NO",
     ["El plazo cargado es el más corto; ajustar el disparador y el plazo según el título (duda D04)",
      "Cheque: 1 año desde el fin del plazo de presentación (30 días desde la creación; 60 si es del exterior, "
      "art. 25); cheque de pago diferido: 1 año desde el rechazo (art. 61)",
      "Pagaré: 3 años contra el suscriptor desde el vencimiento; 1 año contra endosantes desde el protesto o el "
      "vencimiento si tiene cláusula 'sin protesto' (art. 96)",
      "Tarjeta de crédito: 1 año para la vía ejecutiva y 3 para la ordinaria (art. 47 Ley 25.065)",
      "Crédito sin título ejecutivo: plazo genérico de 5 años (art. 2560 CCyC), salvo plazo especial",
      "La mediación suspende la prescripción (art. 40 Ley 13.951; a verificar la remisión al CCyC)"],
     []),
    ("EJE_040", "Previa", "Intimación extrajudicial de pago", "ACTORA",
     "Decisión de reclamar", 0, "SIN_PLAZO", "NO", "Art. 886 CCyC (mora automática; a verificar)", "NO", "NO",
     ["Intimar por carta documento: no es requisito para la ejecución, pero ordena el reclamo",
      "Evaluar un embargo preventivo antes de demandar si hay riesgo de insolvencia (art. 209 CPCCBA)",
      "No incluir intereses ni gastos que no estén pactados o no surjan del título"],
     ["Carta documento"]),
    ("EJE_050", "Previa", "Mediación prejudicial", "AMBAS",
     "Última notificación de la audiencia de mediación al requerido", 30, "CORRIDOS", "NO",
     "Arts. 2, 4, 5, 12, 19 a 23 y 40 Ley 13.951", "NO", "NO",
     ["En el juicio ejecutivo es optativa para el reclamante (art. 5): el plazo es de 30 días corridos (art. 12)",
      "En el cobro de pesos es obligatoria y el plazo es de 60 días corridos, prorrogable 15 (art. 12): ajustar el "
      "plazo",
      "No hay mediación previa para las medidas cautelares ni para las diligencias preliminares (art. 4 incs. 6 "
      "y 7) ni ante los Juzgados de Paz Letrados (art. 4 inc. 12)",
      "Si hay acuerdo, se pide la homologación dentro de los 10 días (art. 19); el incumplimiento se ejecuta como "
      "sentencia (art. 23)",
      "Comparecencia personal o a distancia (arts. 15 y 15 bis); la inasistencia injustificada tiene multa "
      "(art. 14)"],
     ["Formulario de requerimiento", "Acta de cierre de la mediación"]),
    ("EJE_100", "Preparación", "Presentación de la demanda ejecutiva", "ACTORA",
     "Decisión de ejecutar (mediación cerrada, si se optó por ella)", 0, "SIN_PLAZO", "NO",
     "Arts. 518, 521, 522 y 529 CPCCBA", "NO", "NO",
     ["Acompañar el título original y reservarlo en secretaría",
      "Precisar el capital y pedir que el juez estime intereses y costas para el mandamiento (art. 529 inc. 1)",
      "Pagaré de consumo: acompañar el contrato o la documentación de la operación (duda D02)",
      *CHECKLIST_COSTOS_INICIO,
      "Pedir el mandamiento de intimación de pago y embargo; si no se conocen bienes, la inhibición general "
      "(art. 532)"],
     ["Demanda ejecutiva", "Título original", "Poder o patrocinio",
      "Comprobantes de tasa, contribución, bono y anticipo previsional"]),
    ("EJE_105", "Preparación", "Embargo preventivo previo: presentar la demanda", "ACTORA",
     "Traba del embargo preventivo", 10, "HABILES_JUDICIALES", "SI", "Arts. 207 y 209 CPCCBA", "NO", "NO",
     ["Si el embargo se trabó antes de la demanda, presentarla dentro de los 10 días de la traba (art. 207)",
      "Si no se presenta, el embargo caduca de pleno derecho y se cargan las costas y los daños al acreedor",
      "Verificar el inciso del art. 209 que habilita el embargo según el título (a verificar)"],
     ["Constancia de la traba"]),
    ("EJE_110", "Preparación", "Audiencia de reconocimiento de firma o de documentos", "DEMANDADA",
     "Fecha y hora fijadas por el juzgado para la citación", 0, "FECHA_FIJADA", "NO",
     "Arts. 523, 524 y 526 CPCCBA; art. 39 Ley 25.065", "NO", "NO",
     ["Cargar la fecha fijada para la audiencia",
      "El citado comparece en persona; si no comparece o no contesta categóricamente, se tiene por reconocido el "
      "documento (art. 524)",
      "Tarjeta de crédito: se pide el reconocimiento del contrato y del resumen de cuenta, con declaración jurada "
      "de que no hubo denuncia de extravío ni cuestionamiento del resumen (art. 39 Ley 25.065)",
      "Si desconoce la firma, el juez ordena la pericia; si la firma es auténtica, impone costas y multa del 30% "
      "de la deuda (art. 526)"],
     ["Cédula de citación", "Acta de la audiencia"]),
    ("EJE_120", "Preparación", "Promover la ejecución después de la preparación", "ACTORA",
     "Realización de la diligencia preparatoria (si el reconocimiento fue ficto, notificación de la providencia "
     "al ejecutante)", 15, "HABILES_JUDICIALES", "SI", "Art. 527 CPCCBA", "NO", "NO",
     ["Las medidas preparatorias caducan sin declaración judicial si no se deduce la demanda en 15 días",
      "Pedir el mandamiento de intimación de pago y embargo"],
     ["Escrito de promoción de la ejecución"]),
    ("EJE_200", "Intimación y excepciones", "Mandamiento de intimación de pago y embargo", "TRIBUNAL",
     "Providencia que ordena librar el mandamiento", 0, "SIN_PLAZO", "NO", "Arts. 529, 531, 532 y 540 CPCCBA",
     "NO", "NO",
     ["Confeccionar y diligenciar el mandamiento con el oficial de justicia",
      "Si no paga en el acto, el oficial embarga bienes suficientes; el dinero se deposita en el Banco de la "
      "Provincia el primer día hábil siguiente (art. 529 inc. 1)",
      "Si el deudor no estaba presente, se le hace saber dentro de los 3 días de la traba (art. 529 inc. 2)",
      "La intimación importa la citación para oponer excepciones y constituir domicilio (art. 540)",
      "La resolución que deniega la ejecución es apelable (art. 530)"],
     ["Mandamiento diligenciado"]),
    ("EJE_220", "Intimación y excepciones", "Oposición de excepciones", "DEMANDADA",
     "Diligenciamiento de la intimación de pago", 5, "HABILES_JUDICIALES", "SI", "Arts. 540, 542 y 543 CPCCBA",
     "NO", "NO",
     ["Oponer en un solo escrito, con el ofrecimiento de prueba (art. 540)",
      "Solo las del art. 542: incompetencia, falta de personería, litispendencia, falsedad o inhabilidad de título, "
      "prescripción, pago documentado, compensación de crédito líquido, quita, espera o remisión documentadas, "
      "y cosa juzgada",
      "La nulidad de la ejecución se opone por el art. 543",
      "Si se impuso la multa del art. 526, darla a embargo para que se admitan las excepciones",
      "Constituir domicilio en el mismo plazo"],
     ["Escrito de excepciones", "Prueba documental"]),
    ("EJE_230", "Intimación y excepciones", "Contestación del traslado de las excepciones", "ACTORA",
     "Notificación del traslado de las excepciones", 5, "HABILES_JUDICIALES", "SI", "Art. 545 CPCCBA", "NO", "NO",
     ["Contestar y ofrecer la prueba en el mismo escrito",
      "El juez rechaza sin sustanciación las excepciones no autorizadas y dicta sentencia de remate en el mismo "
      "acto (art. 545, primer párrafo)"],
     ["Contestación del traslado"]),
    ("EJE_240", "Intimación y excepciones", "Producción de la prueba de las excepciones", "AMBAS",
     "Fecha de vencimiento del plazo de prueba fijado por el juez", 0, "FECHA_FIJADA", "NO",
     "Arts. 547 y 548 CPCCBA", "NO", "NO",
     ["El juez fija un plazo común; no hay plazo extraordinario (art. 547)",
      "La carga de la prueba de las excepciones es del ejecutado",
      "Producida la prueba, el expediente queda 5 días en secretaría y el juez sentencia en 10 (art. 548)"],
     ["Escritos de prueba"]),
    ("EJE_250", "Intimación y excepciones", "Sentencia de remate", "TRIBUNAL",
     "Contestado el traslado de las excepciones, vencido el plazo para hacerlo o vencidos los 5 días en "
     "secretaría", 10, "HABILES_JUDICIALES", "NO", "Arts. 546, 548, 549 y 551 CPCCBA", "NO", "NO",
     ["Sin excepciones, el juez dicta sentencia de remate sin más trámite (a verificar el artículo)",
      "Ordena llevar adelante la ejecución, en todo o en parte, o la rechaza (art. 549)",
      "Puede imponer al ejecutado una multa del 3% al 10% de la deuda por inconducta (art. 549)",
      "Cualquiera sea la sentencia, después de cumplida se puede promover el juicio ordinario posterior "
      "(art. 551; duda D11)"],
     ["Sentencia de remate"]),
    ("EJE_260", "Recursos", "Apelación de la sentencia de remate", "AMBAS",
     "Notificación de la sentencia de remate", 5, "HABILES_JUDICIALES", "SI", "Arts. 244, 552, 553 y 555 CPCCBA",
     "NO", "NO",
     ["Solo es apelable en los casos del art. 552 (excepciones rechazadas in limine, de puro derecho o con prueba)",
      "Las demás apelaciones del ejecutivo se conceden en efecto diferido (art. 555)",
      "El ejecutante puede dar fianza para que el recurso se conceda en efecto devolutivo y seguir la ejecución; si "
      "no la presta en 5 días, el expediente se eleva (art. 553)"],
     ["Escrito de apelación", "Fianza (si se ofrece)"]),
    ("EJE_270", "Recursos", "Memorial de la apelación", "AMBAS",
     "Notificación de la providencia que concede el recurso", 5, "HABILES_JUDICIALES", "SI",
     "Art. 246 CPCCBA (recurso en relación; a verificar)", "NO", "NO",
     ["Fundar el recurso; el memorial se traslada a la otra parte por el mismo plazo",
      "Si no se funda, el recurso se declara desierto"],
     ["Memorial"]),
    ("EJE_995", "Cierre", "Sigue en la matriz de concursos y quiebras", "TRIBUNAL",
     "Publicación de los edictos del concurso o de la quiebra del deudor", 0, "SIN_PLAZO", "NO",
     "Arts. 21, 32, 56 y 132 LCQ", "NO", "SI",
     ["Puede pasar en cualquier momento del juicio: la ejecución se suspende y se verifica el crédito en el "
      "concurso",
      "Las ejecuciones de garantías reales no se suspenden, pero requieren verificar el crédito (art. 21 inc. 1)",
      "Abrir el expediente en la matriz de concursos desde el hito 'Pedidos de verificación' y vincularlo",
      "Pedir el desglose del título original para verificar"],
     ["Constancia de los edictos del concurso"]),
]

CONTENCIOSA_NODOS, CONTENCIOSA_TRANSICIONES = etapa_contenciosa("EJE", sumario=True, ajustes={
    "EJE_300": {"nombre": "Presentación de la demanda de cobro de pesos (juicio sumario)",
                "evento": "Mediación cerrada sin acuerdo, o vía ejecutiva frustrada"},
    "EJE_450": {"nombre": "Sentencia firme (de remate o del juicio sumario)"},
    "EJE_950": {"evento": "Último acto de impulso del proceso (en el ejecutivo, desde la demanda)"},
})
EJECUCION_NODOS, EJECUCION_TRANSICIONES = bloque_ejecucion("EJE")

NODOS = PROPIOS[:-1] + CONTENCIOSA_NODOS[:-1] + EJECUCION_NODOS + [CONTENCIOSA_NODOS[-1], PROPIOS[-1]]

TRANSICIONES = [
    ("EJE_010", "Cheque o echeq rechazado", "EJE_020"),
    ("EJE_010", "Pagaré sin cláusula 'sin protesto'", "EJE_025"),
    ("EJE_010", "Pagaré 'sin protesto', tarjeta, factura de crédito electrónica u otro título", "EJE_030"),
    ("EJE_010", "Crédito sin título ejecutivo (cobro de pesos)", "EJE_030"),
    ("EJE_010", "El deudor está concursado o en quiebra", "EJE_995"),
    ("EJE_020", "Aviso enviado", "EJE_030"),
    ("EJE_025", "Protesto hecho y avisos enviados", "EJE_030"),
    ("EJE_030", "Acción vigente", "EJE_040"),
    ("EJE_030", "Todas las acciones prescriptas: no se inicia el reclamo", ""),
    ("EJE_040", "Sin pago: juicio ejecutivo sin mediación (optativa, art. 5 Ley 13.951)", "EJE_100"),
    ("EJE_040", "Sin pago: se opta por la mediación o es cobro de pesos (obligatoria)", "EJE_050"),
    ("EJE_040", "Riesgo de insolvencia: embargo preventivo antes de demandar", "EJE_105"),
    ("EJE_040", "Pago total", ""),
    ("EJE_050", "Mediación cerrada sin acuerdo y hay título ejecutivo", "EJE_100"),
    ("EJE_050", "Mediación cerrada sin acuerdo en el cobro de pesos", "EJE_300"),
    ("EJE_050", "Acuerdo en la mediación", "EJE_900"),
    ("EJE_105", "Demanda ejecutiva presentada", "EJE_100"),
    ("EJE_105", "Demanda de cobro de pesos presentada", "EJE_300"),

    ("EJE_100", "Título que trae aparejada ejecución", "EJE_200"),
    ("EJE_100", "Título que trae aparejada ejecución", "EJE_950"),
    ("EJE_100", "Título que requiere preparación (firma, tarjeta de crédito)", "EJE_110"),
    ("EJE_100", "Título que requiere preparación (firma, tarjeta de crédito)", "EJE_950"),
    ("EJE_110", "Firma reconocida, tenida por reconocida o declarada auténtica", "EJE_120"),
    ("EJE_110", "Firma declarada no auténtica o vía no preparada: queda el cobro de pesos", "EJE_300"),
    ("EJE_120", "Ejecución promovida", "EJE_200"),
    ("EJE_120", "Caducaron las medidas preparatorias", "EJE_300"),
    ("EJE_200", "Intimación diligenciada sin pago", "EJE_220"),
    ("EJE_200", "Pago en el acto o dinero embargado", "EJE_870"),
    ("EJE_200", "Ejecución denegada y firme", "EJE_960"),
    ("EJE_220", "Excepciones opuestas", "EJE_230"),
    ("EJE_220", "No se oponen excepciones", "EJE_250"),
    ("EJE_220", "El deudor se concursa o quiebra", "EJE_995"),
    ("EJE_230", "Se ofreció prueba que no consiste en constancias del expediente", "EJE_240"),
    ("EJE_230", "Excepciones de puro derecho o sin prueba", "EJE_250"),
    ("EJE_240", "Prueba producida y vencidos los 5 días en secretaría", "EJE_250"),
    ("EJE_250", "Sentencia notificada y es apelable (art. 552)", "EJE_260"),
    ("EJE_250", "Sentencia notificada y no es apelable", "EJE_450"),
    ("EJE_260", "Se apela y el ejecutante da fianza (efecto devolutivo)", "EJE_270"),
    ("EJE_260", "Se apela y el ejecutante da fianza (efecto devolutivo)", "EJE_800"),
    ("EJE_260", "Se apela sin fianza", "EJE_270"),
    ("EJE_260", "No se apela", "EJE_450"),
    ("EJE_270", "Memorial presentado y contestado o vencido el plazo", "EJE_430"),
    ("EJE_270", "Recurso declarado desierto", "EJE_450"),

    *CONTENCIOSA_TRANSICIONES,
    ("EJE_450", "Sentencia de remate firme que manda llevar adelante la ejecución", "EJE_800"),
    ("EJE_450", "Condena dineraria firme en el juicio sumario", "EJE_460"),
    ("EJE_460", "Liquidación aprobada sin pago", "EJE_800"),
    ("EJE_460", "Liquidación aprobada y pagada", "EJE_960"),
    ("EJE_900", "Acuerdo incumplido: se ejecuta como sentencia", "EJE_800"),

    *EJECUCION_TRANSICIONES,
]

DUDAS = [
    ("D01", "Competencia por monto: Juzgados de Paz",
     "¿Hasta qué monto (en Jus) y en qué partidos los juicios ejecutivos y de cobro de pesos tramitan ante los "
     "Juzgados de Paz Letrados (art. 61 Ley 5827, a verificar el inciso y el monto vigente)? Allí no hay mediación "
     "previa (art. 4 inc. 12 Ley 13.951). ¿Cambia algún plazo de la matriz? Propuesta: el mismo flujo, con la "
     "aclaración en el checklist de EJE_010.", "EJE_010, EJE_050, EJE_100"),
    ("D02", "Pagaré de consumo",
     "La SCBA admitió declarar de oficio la incompetencia por el domicilio real del consumidor en ejecuciones de "
     "pagarés de consumo ('Cuevas', C. 109.305, resolución del 1/9/2010; el fallo también cita la C. 109.193: "
     "verificar cuál es el número correcto), y exigió integrar el pagaré con el contrato para cumplir el art. 36 de "
     "la Ley 24.240, acompañando la documentación en primera instancia ('Asociación Mutual Asís c/ Cubilla', "
     "C. 121.684, 14/8/2019). ¿Es la doctrina vigente al 13/11/2026? ¿Conviene un hito propio para la intimación "
     "a integrar el título, con plazo? Propuesta: checklist en EJE_010 y EJE_100.", "EJE_010, EJE_100"),
    ("D03", "Plazos bancarios",
     "El aviso del rechazo del cheque (2 días hábiles bancarios, art. 39 Ley 24.452) y el protesto del pagaré "
     "(2 días hábiles, art. 48 Decreto-Ley 5965/63) se cargaron como días hábiles administrativos, porque el motor "
     "no tiene días hábiles bancarios. ¿Es aceptable? Si no, hace falta un tipo de plazo nuevo (solo se registra).",
     "EJE_020, EJE_025"),
    ("D04", "Prescripción según el título",
     "EJE_030 usa el plazo más corto (1 año). Confirmar: cheque 1 año desde el fin del plazo de presentación y "
     "cheque de pago diferido desde el rechazo (art. 61 Ley 24.452, texto Ley 27.444); pagaré 3 años contra el "
     "suscriptor desde el vencimiento y 1 año contra endosantes (art. 96 Decreto-Ley 5965/63); pagaré a la vista "
     "con presentación dentro de 1 año (art. 36); tarjeta 1 año ejecutivo y 3 ordinario (art. 47 Ley 25.065); "
     "factura de crédito electrónica (a verificar si remite al régimen del pagaré); genérico 5 años (art. 2560 "
     "CCyC). ¿Conviene un hito por título o el abogado ajusta el plazo?", "EJE_030"),
    ("D05", "Factura de crédito electrónica: plazo de aceptación",
     "El art. 6 de la Ley 27.440 prevé la aceptación tácita a los 15 días corridos. Una resolución publicada en el "
     "BO el 29/10/2026 (argentina.gob.ar, norma 431777; número 424/2026 según la búsqueda, a verificar) llevó el "
     "plazo a 21 días corridos entre el 01/11/2026 y el 31/10/2027 para los arts. 4, 5, 6 y 8. ¿Se agrega un hito "
     "previo de espera de la aceptación? ¿Qué plazo se carga? Propuesta: checklist en EJE_010 con el plazo vigente a "
     "la fecha de emisión de la factura.", "EJE_010"),
    ("D06", "Factura conformada",
     "El art. 521 inc. 5 del CPCCBA sigue nombrando la factura conformada y remite al Código de Comercio, derogado "
     "por la Ley 26.994. ¿Sigue siendo título ejecutivo en PBA y bajo qué norma? Propuesta: no incluirla como "
     "variante hasta que se confirme.", "EJE_010"),
    ("D07", "Tarjeta de crédito",
     "Los arts. 39 a 47 de la Ley 25.065 (preparación de la vía ejecutiva y prescripción) no figuran entre los "
     "modificados por el DNU 70/2023 (a verificar). ¿La preparación sigue la audiencia de reconocimiento del art. "
     "523 CPCCBA? ¿El art. 42 (no cobro ejecutivo directo del resumen) obliga siempre a preparar la vía?",
     "EJE_100, EJE_110, EJE_030"),
    ("D08", "Mediación en ejecutivos y cobro de pesos",
     "En el juicio ejecutivo la mediación es optativa para el reclamante (art. 5 Ley 13.951) y el plazo es de "
     "30 días corridos (art. 12); en el cobro de pesos es obligatoria y el plazo es de 60. EJE_050 carga 30 (el "
     "más corto). ¿Se usa en la práctica la mediación optativa? ¿La exención por cautelar previa (art. 4 inc. 6) "
     "alcanza a la demanda posterior al embargo preventivo?", "EJE_050, EJE_105"),
    ("D09", "Prueba y sentencia en el ejecutivo",
     "El plazo de prueba lo fija el juez (art. 547): se cargó como fecha fijada. Después, el expediente queda 5 días "
     "en secretaría y el juez sentencia en 10 (art. 548). ¿Conviene un hito para los 5 días en secretaría (la "
     "práctica es presentar un alegato breve)? Sin excepciones, ¿qué artículo manda dictar sentencia de remate sin "
     "más trámite? No se encontró en el texto revisado.", "EJE_240, EJE_250"),
    ("D10", "Apelación de la sentencia de remate",
     "Se cargó apelación en 5 días (art. 244) y memorial en 5 días en relación (art. 246, a verificar que la "
     "sentencia de remate se concede en relación). ¿Es correcto? ¿Se admite recurso extraordinario contra la "
     "sentencia de remate, que en general no es definitiva? El camino EJE_430 → EJE_440 de la etapa común lo "
     "permite.", "EJE_260, EJE_270, EJE_430, EJE_440"),
    ("D11", "Juicio ordinario posterior",
     "El ordinario posterior (art. 551) lo promueve cualquiera de las partes después de cumplida la condena. No se "
     "modeló como camino: ¿se abre como expediente nuevo con el flujo de cobro de pesos y vinculado al ejecutivo? "
     "Propuesta: expediente nuevo (duda de producto de vinculación en la matriz de concursos).", "EJE_250"),
    ("D12", "Caducidad de instancia en el ejecutivo",
     "La caducidad es de 3 meses en el ejecutivo y el sumario (art. 310 inc. 2). ¿Corre durante la preparación de "
     "la vía? ¿Y en la ejecución de la sentencia de remate (el art. 313 inc. 1 la excluye en la ejecución de "
     "sentencia)? Propuesta: corre desde la demanda hasta la sentencia de remate.", "EJE_100, EJE_950"),
    ("D13", "Ejecución anticipada con fianza",
     "Si el ejecutante da fianza, el recurso se concede en efecto devolutivo y la ejecución sigue (art. 553): la "
     "matriz abre a la vez el memorial y el embargo ejecutorio. Cuando la sentencia queda firme, EJE_450 vuelve a "
     "abrir EJE_800. ¿El motor admite abrir de nuevo un hito que ya está abierto, o hay que evitarlo?",
     "EJE_260, EJE_450, EJE_800"),
    ("D14", "Intereses del título y tasa judicial",
     "En el cheque y el pagaré, ¿se liquidan los intereses pactados en el título o la tasa de la doctrina legal de "
     "la SCBA? ¿Se aplica de oficio la morigeración de tasas usurarias (art. 771 CCyC)? La tasa por defecto es "
     "la duda transversal de la matriz de concursos.", "EJE_460, EJE_870"),
    ("D15", "Subasta electrónica",
     "Confirmar el reglamento vigente de subastas electrónicas de la SCBA (número de acordada a verificar), la "
     "duración de la puja (art. 562: 10 días) y si los plazos del bloque de subasta son correctos en PBA.",
     "EJE_830, EJE_840, EJE_845, EJE_850"),
    ("D16", "Deudor concursado",
     "Si el deudor se concursa o quiebra durante el juicio, el expediente termina en 'Sigue en la matriz de "
     "concursos y quiebras'. Solo se dibujaron las entradas desde EJE_010 y EJE_220, pero puede pasar en cualquier "
     "hito. ¿Alcanza con eso o se agrega la salida en todos los hitos? Las ejecuciones con garantía real no se "
     "suspenden (art. 21 inc. 1 LCQ).", "EJE_010, EJE_220, EJE_995"),
    ("D17",) + DUDA_TRANSVERSAL,
    ("D18", "Etapa contenciosa común",
     "La demanda, la contestación, la prueba, la sentencia, los recursos, la caducidad y los honorarios del cobro de "
     "pesos son la etapa contenciosa común del CPCCBA. Sus dudas (audiencia preliminar, plazos del sumario, "
     "traslado de la pericia, recursos extraordinarios) se responden en matriz_comercial_societarios_pba.xlsx.",
     "EJE_300 a EJE_460"),
]
