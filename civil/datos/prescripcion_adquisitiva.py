from comun import (CON_GRACIA, CON_VALOR_CERO, DUDA_ETAPA_COMUN, DUDA_PRODUCTO, ESTADOS, ROLES, etapa_judicial,
                   flujo, ordenar, plazo_tipos)

FLUJO = flujo(
    "Prescripción adquisitiva de inmuebles (usucapión) - Provincia de Buenos Aires",
    "CPCCBA (Decreto-Ley 7425/68), juicio sumario con las reglas de los arts. 679 a 682; CCyC arts. 1897 a 1905; "
    "Ley 14.159 (art. 24)",
    "Borrador para validar con el equipo legal. Citas cotejadas al 13/11/2026 con normas.gba.gob.ar, leyes-ar.com y "
    "argentina.gob.ar; lo que no se pudo confirmar dice '(a verificar)' y tiene su duda. La etapa judicial sale de "
    "civil/datos/comun.py, con las citaciones propias de la usucapión y sin la ejecución dineraria, que se reemplaza "
    "por la inscripción. Las dudas de la etapa común se responden en matriz_civil_danos_y_perjuicios_pba.xlsx y las "
    "de producto en matriz_civil_sucesorio_pba.xlsx.",
)

FASES = ["Previa", "Postulación", "Citaciones", "Prueba", "Sentencia", "Recursos", "Inscripción", "Acuerdo", "Cierre"]

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": "En este flujo: contestación del titular, de los citados por edictos, del Defensor "
                          "Oficial, del Fisco de Estado y de la Municipalidad, y el resto de la etapa judicial.",
    "MESES": "En este flujo: caducidad de instancia (3 meses en el sumario).",
    "ANIOS": "En este flujo: cumplimiento del plazo de posesión (10 años; los 20 de la prescripción larga superan "
             "el máximo de la app, ver duda D01).",
    "FECHA_FIJADA": "En este flujo: audiencias preliminar y de vista de causa, y el reconocimiento judicial del "
                    "inmueble.",
    "ANTICIPACION_HABILES_JUDICIALES": "En este flujo: dictamen pericial 5 días antes de la audiencia de prueba "
                                       "(art. 492 CPCCBA).",
    "SIN_PLAZO": "En este flujo: informes de registros y organismos, plano de mensura, edictos, inscripción y "
                 "plazos que fija el juez.",
})

GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Citaciones, edictos y anotación de litis", ["Citaciones"]),
    ("Prueba", ["Prueba"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Inscripción", ["Inscripción"]),
    ("Acuerdo", ["Acuerdo"]),
    ("Cierre", ["Cierre"]),
]

ROL_TEXTO = {"ACTORA": "Poseedor que representamos", "DEMANDADA": "Titular registral o citado",
             "TRIBUNAL": "Juzgado u organismo", "AMBAS": "Cualquiera de las partes"}
LEYENDA_ROLES = ("celeste = el poseedor que pide la usucapión y al que representamos (ACTORA); naranja = el titular "
                 "registral, sus herederos, los citados por edictos, el Defensor Oficial de Ausentes, el Fisco de "
                 "Estado o la Municipalidad (DEMANDADA); gris = el juzgado o un organismo: Registro de la Propiedad, "
                 "Geodesia, ARBA (TRIBUNAL); violeta = cualquiera de las partes (AMBAS).")
EJEMPLO_PARALELO = ("los edictos al titular y a quienes se consideren con derecho corren mientras se cita al Fisco "
                    "de Estado y a la Municipalidad")
ROLES_DESCRIPCION = [
    ("ACTORA", "El poseedor que pide que se declare adquirido el dominio y al que representamos. También cuando "
               "opone la usucapión como defensa en un juicio en su contra."),
    ("DEMANDADA", "Quien figura como titular en el Registro de la Propiedad o sus herederos, los citados por edictos "
                  "(titular ignorado y quienes se consideren con derecho), el Defensor Oficial de Ausentes que los "
                  "representa, y el Fisco de Estado o la Municipalidad cuando son parte (arts. 679 inc. 4 y 681 "
                  "CPCCBA)."),
    ("TRIBUNAL", "El juzgado, la Cámara, la SCBA o un organismo: Registro de la Propiedad, Dirección de Geodesia, "
                 "ARBA, secretaría electoral, policía o correo. El nombre del hito dice cuál. La app muestra "
                 "'Esperando resolución'."),
    ("AMBAS", "Cualquiera de las partes: audiencias, prueba, recursos, honorarios y acuerdos."),
]
INSTRUCCIONES_ADICIONALES = [
    ("Particularidades de la prescripción adquisitiva", True),
    ("La consulta inicial abre tres caminos: preparar la demanda de usucapión, evaluar la regularización por la "
     "Ley 24.374 u oponer la usucapión como defensa en un juicio en contra del cliente.", False),
    ("La etapa judicial es la común del fuero civil para el juicio sumario, con las citaciones de los arts. 679 a "
     "681 CPCCBA en paralelo, y termina con la inscripción de la sentencia en lugar de la ejecución.", False),
    ("La prescripción larga exige 20 años de posesión y la app admite hasta 10 años: ver la duda D01.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
_PREVIA = [
    ("USU_010", "Previa", "Consulta inicial por la posesión del inmueble", "ACTORA",
     "Fecha de la consulta", 0, "SIN_PLAZO", "NO",
     "Arts. 1897, 1900 y 1909 CCyC", "SI", "NO",
     ["Relevar desde cuándo y cómo posee el cliente: actos posesorios, mejoras, pago de impuestos y servicios",
      "La posesión debe ser ostensible y continua (art. 1900) y el cliente debe comportarse como dueño (art. 1909)",
      "Con justo título y buena fe alcanzan 10 años (art. 1898); sin ellos hacen falta 20 (art. 1899)",
      "El heredero continúa la posesión del causante y el sucesor particular puede unirla a la de su antecesor "
      "(art. 1901)",
      "Si es vivienda única y familiar, evaluar la regularización dominial de la Ley 24.374",
      "Si el cliente ya fue demandado por reivindicación o desalojo, evaluar oponer la usucapión como defensa"],
     ["DNI", "Boleto, cesión o título que tenga", "Comprobantes de impuestos y servicios", "Fotos de mejoras"]),
    ("USU_015", "Previa", "Cómputo del plazo y prueba de la posesión", "ACTORA",
     "Fecha de inicio de la posesión invocada", 0, "SIN_PLAZO", "NO",
     "Arts. 1898, 1899, 1901 y 1903 CCyC; art. 24 Ley 14.159", "NO", "NO",
     ["Fijar la fecha de inicio de la posesión y contar 10 o 20 años",
      "Reunir prueba de la posesión: impuestos y tasas pagados (se consideran especialmente, art. 24 Ley 14.159), "
      "servicios, mejoras, planos de obra, contratos, fotos",
      "La sentencia no puede basarse solo en testigos (art. 679 inc. 1 CPCCBA): conseguir prueba documental",
      "Identificar testigos vecinos con conocimiento directo de la posesión"],
     ["Comprobantes de impuestos y servicios", "Documentación de mejoras", "Lista de testigos"]),
    ("USU_017", "Previa", "Cumplimiento del plazo de posesión", "ACTORA",
     "Inicio de la posesión útil (en la prescripción larga, fecha en que se cumplen 10 años de posesión)", 10,
     "ANIOS", "NO",
     "Arts. 1898 y 1899 CCyC", "NO", "NO",
     ["Prescripción breve: 10 años desde el inicio de la posesión o la registración del justo título (art. 1898)",
      "Prescripción larga: 20 años (art. 1899). La app admite hasta 10 años: cargar como fecha de inicio el día en "
      "que se cumplen los primeros 10 años de posesión (ver duda D01)",
      "Demandar una vez cumplido el plazo"],
     []),
    ("USU_020", "Previa", "Informe de dominio y búsqueda del titular registral", "ACTORA",
     "Pedido del certificado al Registro de la Propiedad", 0, "SIN_PLAZO", "NO",
     "Arts. 679 inc. 2 y 680 CPCCBA", "NO", "NO",
     ["Pedir el certificado del Registro de la Propiedad con la condición jurídica del inmueble y todos los datos "
      "del titular (art. 679 inc. 2)",
      "Si se ignora el propietario, se pide informe del organismo técnico sobre los antecedentes del dominio y los "
      "intereses fiscales (art. 680)",
      "Si el titular murió, buscar su sucesión en el Registro de Juicios Universales para demandar a los herederos",
      "Buscar el último domicilio conocido del titular"],
     ["Certificado de dominio", "Informe del Registro de Juicios Universales"]),
    ("USU_030", "Previa", "Plano de mensura para usucapión y visado de Geodesia", "TRIBUNAL",
     "Presentación del plano ante la Dirección de Geodesia", 0, "SIN_PLAZO", "NO",
     "Art. 679 inc. 3 CPCCBA; art. 24 Ley 14.159", "NO", "NO",
     ["Encargar a un agrimensor matriculado el plano con área, linderos y ubicación (art. 679 inc. 3)",
      "Presentarlo para el visado de la Dirección Provincial de Geodesia (organismo y trámite, a verificar)",
      "Pedir la valuación fiscal y la partida inmobiliaria en ARBA (base de la tasa de justicia, a verificar)",
      "Si el plano es observado, corregirlo y volver a presentarlo"],
     ["Plano de mensura visado", "Informe catastral y valuación fiscal"]),
    ("USU_045", "Previa", "Evaluación de la regularización dominial de la Ley 24.374", "ACTORA",
     "Fecha de la consulta", 0, "SIN_PLAZO", "NO",
     "Ley 24.374 (requisitos y vigencia, a verificar)", "NO", "NO",
     ["Controlar los requisitos: vivienda única y permanente, ocupación pacífica, pública y continua con causa "
      "lícita durante el plazo legal (a verificar)",
      "El trámite es administrativo, ante el organismo provincial y un escribano de registro (a verificar)",
      "La inscripción se consolida como dominio después de 10 años (a verificar)"],
     ["Constancias de ocupación", "Declaración jurada"]),
    ("USU_060", "Previa", "Oposición de la usucapión como defensa en el juicio en contra del cliente", "ACTORA",
     "Notificación del traslado de la demanda de reivindicación o desalojo", 15, "HABILES_JUDICIALES", "SI",
     "Art. 1905 CCyC; arts. 354 y 679 CPCCBA", "NO", "NO",
     ["El plazo es el de contestación del juicio en contra: 15 días en el ordinario; si es sumario (por ejemplo, "
      "desalojo), editar a 10",
      "Oponer la prescripción adquisitiva al contestar, con la prueba de la posesión",
      "El traslado de la excepción ordena de oficio la anotación de litis (art. 1905)",
      "Evaluar reconvenir por usucapión para obtener una sentencia inscribible",
      "El juicio en contra se sigue como otro caso en la app"],
     ["Escrito de contestación", "Prueba de la posesión"]),
]

_QUITAR = ["USU_700", "USU_705", "USU_710", "USU_720", "USU_730", "USU_805"]

_ETAPA_NODOS, _ETAPA_TRANSICIONES = etapa_judicial(
    "USU", "sumario",
    agregar={
        "USU_300": [
            "La usucapión tramita por juicio sumario con las reglas del art. 679 CPCCBA",
            "Acompañar el certificado del Registro de la Propiedad (art. 679 inc. 2) y el plano visado (inc. 3)",
            "Demandar al titular registral o a sus herederos; si hay intereses fiscales, son parte el Fiscal de "
            "Estado o la Municipalidad (art. 679 inc. 4)",
            "Pedir la citación por edictos de quienes se consideren con derecho sobre el inmueble (art. 681)",
            "Indicar la fecha en que se cumplió el plazo de prescripción: la sentencia debe fijarla (art. 1905 CCyC)",
            "Verificar si corresponde la mediación previa (ver duda D02)"],
        "USU_330": [
            "La resolución que da traslado ordena de oficio la anotación de litis (art. 1905 CCyC)",
            "Traslado al titular, o al Fiscal de Estado o la Municipalidad, en su caso (art. 681)"],
        "USU_340": [
            "Si el titular se allana, el proceso sigue siendo contencioso y hay que probar la posesión (art. 1905 "
            "CCyC; art. 679 inc. 1 CPCCBA)"],
        "USU_400": [
            "Se admite toda clase de prueba, pero la sentencia no puede basarse solo en testigos (art. 679 inc. 1)",
            "Pedir el reconocimiento judicial del inmueble o una pericia de agrimensura que constate la posesión"],
        "USU_420": [
            "Pericia típica: agrimensor que constate la ubicación, los límites y la ocupación del inmueble"],
        "USU_500": [
            "La sentencia debe fijar la fecha en que se adquirió el dominio (art. 1905 CCyC)",
            "La sentencia de prescripción larga no es retroactiva; la de prescripción breve sí (arts. 1903 y 1905)",
            "La sentencia que acoge la demanda hace cosa juzgada material (art. 682)"],
        "USU_800": [
            "Un acuerdo con el titular no reemplaza la sentencia: el proceso debe ser contencioso (art. 1905 CCyC). "
            "Si el titular acepta escriturar, se desiste del juicio y se escritura"],
    },
    quitar=_QUITAR,
    redirigir={"USU_700": "USU_750", "USU_805": "USU_990"},
    omitir=[("USU_330", "Se ordena el traslado de la demanda")],
)

_PROPIOS = [
    ("USU_332", "Citaciones", "Anotación de litis en el Registro de la Propiedad", "TRIBUNAL",
     "Resolución que da traslado de la demanda o de la excepción de usucapión", 0, "SIN_PLAZO", "NO",
     "Art. 1905 CCyC", "NO", "NO",
     ["El juez la ordena de oficio al dar traslado (art. 1905): controlar que se libre y diligencie el oficio",
      "Pagar la tasa registral y controlar la toma de razón"],
     ["Oficio de anotación de litis", "Constancia de inscripción"]),
    ("USU_334", "Citaciones", "Informes sobre el último domicilio del titular", "TRIBUNAL",
     "Libramiento de los oficios", 0, "SIN_PLAZO", "NO",
     "Art. 681 CPCCBA", "NO", "NO",
     ["Pedir informes a la secretaría electoral y a las delegaciones locales de policía y correo sobre el último "
      "domicilio conocido o supuesto del titular (art. 681)",
      "Reiterar los oficios no contestados (art. 400)"],
     ["Oficios diligenciados"]),
    ("USU_336", "Citaciones", "Publicación de edictos al titular y a quienes se consideren con derecho", "ACTORA",
     "Libramiento de los edictos", 0, "SIN_PLAZO", "NO",
     "Arts. 145 a 147 y 681 CPCCBA", "NO", "NO",
     ["Publicar por 10 días en el Boletín Judicial y en un diario de la zona (art. 681)",
      "El edicto previene que, si el citado no se presenta y contesta, se le nombra Defensor Oficial de Ausentes",
      "Agregar un ejemplar y el recibo de pago de cada publicación (art. 146)",
      "La resolución se tiene por notificada al día siguiente de la última publicación (art. 147)"],
     ["Edictos publicados", "Recibos de pago"]),
    ("USU_338", "Citaciones", "Plazo para comparecer de los citados por edictos", "DEMANDADA",
     "Día siguiente a la última publicación de los edictos", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 147, 484 y 681 CPCCBA (plazo, a verificar)", "NO", "NO",
     ["La matriz usa el plazo de contestación del sumario (10 días); editar si el edicto fijó otro",
      "Si nadie comparece y el titular fue citado por edictos, pedir la designación del Defensor Oficial"],
     []),
    ("USU_339", "Citaciones", "Contestación del Defensor Oficial de Ausentes", "DEMANDADA",
     "Notificación al Defensor Oficial de su designación", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 341 y 681 CPCCBA (plazo, a verificar)", "NO", "NO",
     ["El Defensor Oficial representa al titular ausente y controla la prueba",
      "Suele pedir que se acredite la búsqueda del titular y la publicación de los edictos"],
     []),
    ("USU_342", "Citaciones", "Contestación del Fisco de Estado y de la Municipalidad", "DEMANDADA",
     "Notificación del traslado al Fisco de Estado y a la Municipalidad", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 679 inc. 4 y 681 CPCCBA (plazo especial del Fisco de Estado, a verificar)", "NO", "NO",
     ["Son parte si hay intereses fiscales provinciales o municipales comprometidos (art. 679 inc. 4)",
      "Controlar si informan deudas de impuestos o tasas, o si el inmueble es del dominio público",
      "Si el Fisco de Estado tiene un plazo distinto, editar (ver duda D06)"],
     []),
    ("USU_750", "Inscripción", "Pedido de inscripción de la sentencia", "ACTORA",
     "Sentencia firme que acoge la demanda", 0, "SIN_PLAZO", "NO",
     "Art. 682 CPCCBA", "NO", "NO",
     ["Pedir el testimonio y el oficio de inscripción con la cancelación del dominio anterior (art. 682)",
      "Acompañar el plano visado y pagar las tasas registrales",
      "Pagar la tasa de justicia y los aportes pendientes antes de inscribir (a verificar)"],
     ["Testimonio de la sentencia", "Oficio al Registro de la Propiedad", "Plano visado"]),
    ("USU_760", "Inscripción", "Inscripción en el Registro de la Propiedad", "TRIBUNAL",
     "Presentación del testimonio en el Registro de la Propiedad", 0, "SIN_PLAZO", "NO",
     "Art. 682 CPCCBA; Ley 17.801", "NO", "NO",
     ["Controlar la inscripción a nombre del cliente y la cancelación del dominio anterior",
      "Si el Registro observa el documento, subsanar en el plazo de la inscripción provisional (a verificar)",
      "Pedir el levantamiento de la anotación de litis"],
     ["Constancia de inscripción"]),
    ("USU_770", "Inscripción", "Alta catastral y tributaria a nombre del cliente", "ACTORA",
     "Inscripción del dominio a nombre del cliente", 0, "SIN_PLAZO", "NO",
     "Código Fiscal PBA (a verificar)", "NO", "NO",
     ["Pedir el cambio de titularidad de la partida en ARBA y en la Municipalidad",
      "Entregar al cliente el título y las constancias"],
     ["Constancias de ARBA y de la Municipalidad"]),
]

NODOS = sorted(_PREVIA + _ETAPA_NODOS + _PROPIOS, key=lambda n: n[0])

_PREPARAR = "Posesión propia: se prepara la demanda de usucapión"
_NO_REUNE = "No reúne los requisitos: se prepara la demanda de usucapión"
_CONOCIDO = "Se ordena el traslado al titular con domicilio conocido"
_IGNORADO = "Titular o domicilio ignorados: se piden informes"

TRANSICIONES = ordenar(NODOS, [
    ("USU_010", _PREPARAR, "USU_015"),
    ("USU_010", _PREPARAR, "USU_020"),
    ("USU_010", _PREPARAR, "USU_030"),
    ("USU_010", "Vivienda única: se evalúa la Ley 24.374", "USU_045"),
    ("USU_010", "El cliente fue demandado: se opone la usucapión como defensa", "USU_060"),
    ("USU_015", "Plazo cumplido y prueba reunida", ""),
    ("USU_015", "Todavía no se cumplió el plazo", "USU_017"),
    ("USU_017", "Plazo cumplido", ""),
    ("USU_020", "Informe recibido y titular identificado o declarado ignorado", ""),
    ("USU_030", "Plano visado: se presenta la demanda", "USU_300"),
    ("USU_045", "Se regulariza por la Ley 24.374", "USU_990"),
    ("USU_045", _NO_REUNE, "USU_015"),
    ("USU_045", _NO_REUNE, "USU_020"),
    ("USU_045", _NO_REUNE, "USU_030"),
    ("USU_060", "Defensa opuesta: se ordena la anotación de litis", "USU_332"),
    *_ETAPA_TRANSICIONES,
    ("USU_330", _CONOCIDO, "USU_340"),
    ("USU_330", _CONOCIDO, "USU_332"),
    ("USU_330", _CONOCIDO, "USU_336"),
    ("USU_330", _CONOCIDO, "USU_342"),
    ("USU_330", _IGNORADO, "USU_334"),
    ("USU_330", _IGNORADO, "USU_332"),
    ("USU_330", _IGNORADO, "USU_342"),
    ("USU_332", "Litis anotada", ""),
    ("USU_334", "Informes negativos: se cita por edictos al titular y a los interesados", "USU_336"),
    ("USU_334", "Se encuentra el domicilio: se notifica al titular", "USU_340"),
    ("USU_334", "Se encuentra el domicilio: se notifica al titular", "USU_336"),
    ("USU_336", "Edictos publicados", "USU_338"),
    ("USU_338", "Nadie comparece y el titular fue citado por edictos: interviene el Defensor Oficial", "USU_339"),
    ("USU_338", "Comparece un interesado, o el titular fue notificado en su domicilio", ""),
    ("USU_339", "Contestación del Defensor Oficial presentada o plazo vencido", "USU_400"),
    ("USU_342", "Contestan o vence el plazo", ""),
    ("USU_750", "Testimonio y oficio librados", "USU_760"),
    ("USU_760", "Dominio inscripto a nombre del cliente", "USU_770"),
    ("USU_760", "Documento observado: se subsana", "USU_750"),
    ("USU_770", "Trámites terminados", "USU_990"),
])

_PROPIAS = [
    ("Años máximos",
     "La prescripción larga exige 20 años de posesión (art. 1899 CCyC) y la app admite hasta 10 años (ANIOS) o 120 "
     "meses. La matriz pide cargar como inicio la fecha en que se cumplen los primeros 10 años. ¿Se acepta ese "
     "recurso o hay que ampliar el máximo (ver la duda de producto en la matriz del sucesorio)?",
     "USU_017"),
    ("Mediación",
     "¿La demanda de usucapión exige mediación previa (Ley 13.951)? Si el titular es ignorado o el Fisco es parte, la "
     "mediación no parece posible (art. 4: causas en que el Estado es parte). La matriz no incluye hitos de "
     "mediación.",
     "USU_300"),
    ("Plano y Geodesia",
     "¿Qué organismo visa hoy el plano de mensura para usucapión (Dirección Provincial de Geodesia, a verificar), con "
     "qué antigüedad máxima y en qué plazo? ¿Hace falta un hito con plazo para la visación?",
     "USU_030"),
    ("Edictos",
     "Los edictos se publican por 10 días en el Boletín Judicial y en un diario de la zona (art. 681). ¿Qué plazo "
     "tienen los citados para comparecer después de la última publicación? La matriz usa 10 días hábiles (plazo de "
     "contestación del sumario).",
     "USU_336, USU_338"),
    ("Defensor Oficial",
     "¿En qué plazo contesta el Defensor Oficial de Ausentes y desde cuándo corre? ¿El rol DEMANDADA es correcto para "
     "él, aunque sea un funcionario?",
     "USU_339"),
    ("Fisco de Estado",
     "El Fisco de Estado y la Municipalidad son parte si hay intereses fiscales (art. 679 inc. 4). ¿El Fisco de Estado "
     "tiene un plazo especial para contestar (ley orgánica de Fiscalía de Estado, a verificar)? ¿Se los cita siempre "
     "o solo si el informe del art. 680 muestra intereses fiscales?",
     "USU_342"),
    ("Anotación de litis",
     "El art. 1905 CCyC obliga al juez a ordenar de oficio la anotación de litis al dar traslado. ¿Igual conviene "
     "pedirla en la demanda? ¿Quién diligencia el oficio?",
     "USU_332"),
    ("Unión de posesiones",
     "¿Cómo se acredita la unión de posesiones con la del antecesor (art. 1901 CCyC) y desde qué fecha se cuenta el "
     "plazo si hay cesiones de derechos posesorios?",
     "USU_015"),
    ("Ley 24.374",
     "¿Sigue vigente el régimen de regularización dominial de la Ley 24.374 en PBA al 13/11/2026, con qué plazo de "
     "ocupación exigido y qué organismo lo tramita? La matriz solo lo deja como alternativa.",
     "USU_045"),
    ("Usucapión como defensa",
     "Cuando el cliente es demandado por reivindicación o desalojo, la usucapión se opone como defensa (art. 1905 "
     "CCyC). La matriz la modela como un solo hito con el plazo de contestación y el juicio en contra sigue como otro "
     "caso. ¿Conviene reconvenir siempre?",
     "USU_060"),
    ("Herederos del titular",
     "Si el titular murió, ¿se demanda a los herederos declarados, a la sucesión, o se cita por edictos? ¿Hace falta "
     "abrir el sucesorio del titular?",
     "USU_020, USU_330"),
    ("Tasa de justicia",
     "¿La tasa de justicia de la usucapión se calcula sobre la valuación fiscal del inmueble y cuándo se paga (al "
     "iniciar o antes de inscribir, a verificar)?",
     "USU_300, USU_750"),
    ("Inscripción",
     "Si el Registro observa el testimonio, ¿qué plazo hay para subsanar antes de que caduque la inscripción "
     "provisional (Ley 17.801, a verificar)? ¿Hace falta un hito con plazo?",
     "USU_760"),
]

DUDAS = [(f"D{i:02d}", *d)
         for i, d in enumerate(_PROPIAS + [DUDA_PRODUCTO, DUDA_ETAPA_COMUN], start=1)]
