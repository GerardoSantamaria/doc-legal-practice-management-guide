FLUJO = {
    "Flujo": "Proceso sucesorio (ab intestato y testamentario) - Provincia de Buenos Aires",
    "Jurisdicción": "PBA",
    "Fuero": "Civil y Comercial",
    "Régimen procesal": "CPCCBA (Decreto-Ley 7425/68, arts. 724 a 773) y CCyC Libro Quinto",
    "Versión": "1 (borrador)",
    "Fecha del borrador": "13/11/2026",
    "Validado por (equipo legal)": "",
    "Fecha de validación": "",
    "Notas": "Ejemplo armado para validar con el equipo legal. Las citas se cotejaron con textos actualizados al "
             "13/11/2026 (normas.gba.gob.ar, leyes-ar.com, digesto de la SCBA); las que no se pudieron confirmar "
             "dicen '(a verificar)' y tienen su duda. Es el primer flujo del fuero Civil y Comercial: el catálogo "
             "de regímenes de la app todavía no tiene uno civil (duda D44). Sirve también para los Juzgados de Paz "
             "Letrados competentes en sucesiones (art. 61 Ley 5827), a confirmar en la duda D03.",
}

FASES = ["Previa", "Apertura", "Edictos y citación", "Declaratoria o aprobación del testamento", "Administración",
         "Inventario y avalúo", "Partición", "Inscripción", "Impuestos y tasas", "Recursos e incidentes", "Cierre"]
ROLES = ["ACTORA", "DEMANDADA", "TRIBUNAL", "AMBAS"]
PLAZO_TIPOS = [
    ("HABILES_JUDICIALES", "Días hábiles judiciales (calendario judicial PBA). Admite gracia."),
    ("CORRIDOS", "Días corridos, como la citación por edictos. Si el último día es inhábil, se puede cumplir el hábil siguiente (regla R2). Admite gracia."),
    ("HABILES_ADMINISTRATIVOS", "Días hábiles administrativos: lunes a viernes sin feriados; las ferias judiciales no suspenden (regla R6). Sin gracia. Este flujo no lo usa."),
    ("MESES", "Meses, de fecha a fecha (regla R7), como la rendición de cuentas trimestral o los 24 meses del ITGB. Admite gracia."),
    ("ANIOS", "Años, de fecha a fecha (regla R7), como la caducidad de 10 años del derecho de aceptar la herencia. Admite gracia."),
    ("HORAS", "Horas corridas desde la fecha y hora del disparador (regla R8). Sin gracia. Este flujo no lo usa."),
    ("FECHA_FIJADA", "Acto con fecha y hora fijadas, como una audiencia o la diligencia de inventario (valor 0). El abogado carga la fecha y la hora. Sin gracia."),
    ("ANTICIPACION_HABILES_JUDICIALES", "Días hábiles judiciales contados hacia atrás desde un acto fijado (regla R9). Sin gracia. Este flujo no lo usa."),
    ("SIN_PLAZO", "Sin plazo perentorio (valor 0). Depende del juzgado, de un organismo o de la parte, o el plazo lo fija el juez y se carga como plazo suelto. Sin gracia."),
]
CON_VALOR_CERO = ["SIN_PLAZO", "FECHA_FIJADA"]
CON_GRACIA = ["HABILES_JUDICIALES", "CORRIDOS", "MESES", "ANIOS"]
ESTADOS = ["PENDIENTE", "VALIDADO", "CORREGIR"]

# Grupos de fases del diagrama: (título de la sección, fases que incluye)
GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Apertura", ["Apertura"]),
    ("Edictos y citación", ["Edictos y citación"]),
    ("Declaratoria y aprobación del testamento", ["Declaratoria o aprobación del testamento"]),
    ("Administración e inventario", ["Administración", "Inventario y avalúo"]),
    ("Partición", ["Partición"]),
    ("Inscripción", ["Inscripción"]),
    ("Impuestos, tasas, honorarios y cierre", ["Impuestos y tasas", "Cierre"]),
    ("Recursos e incidentes", ["Recursos e incidentes"]),
]

ROL_TEXTO = {"ACTORA": "Heredero que representamos", "DEMANDADA": "Otros interesados",
             "TRIBUNAL": "Juzgado u organismo", "AMBAS": "Cualquier interesado"}
LEYENDA_ROLES = ("celeste = el heredero o interesado que promueve y al que representamos (ACTORA); "
                 "naranja = otros interesados con intereses opuestos en una incidencia: coherederos que impugnan, "
                 "acreedores, el cónyuge en la liquidación de los gananciales (DEMANDADA); "
                 "gris = el juzgado o la espera de un organismo, como un registro o ARBA (TRIBUNAL); "
                 "violeta = cualquiera de los interesados (AMBAS).")
EJEMPLO_PARALELO = ("la publicación de edictos corre mientras se esperan los informes del Registro de Juicios "
                    "Universales y del Registro de Testamentos")
ROLES_DESCRIPCION = [
    ("ACTORA", "El heredero o interesado que promueve el sucesorio y al que representamos."),
    ("DEMANDADA", "Otros interesados con intereses opuestos en una incidencia: coherederos que impugnan, acreedores, "
                  "el cónyuge supérstite en la liquidación de los gananciales. El sucesorio no tiene demandado (duda D41)."),
    ("TRIBUNAL", "El juzgado o la espera de un organismo (Registro de Juicios Universales, Registro de la Propiedad, "
                 "ARBA); el nombre del hito aclara cuál. La app muestra 'Esperando resolución'."),
    ("AMBAS", "Cualquiera de los interesados: recursos, traslados, audiencias, administración."),
]
INSTRUCCIONES_ADICIONALES = [
    ("Particularidades del sucesorio", True),
    ("Roles: el sucesorio no tiene demandado. ACTORA es el heredero o interesado que promueve y al que representamos; "
     "DEMANDADA, otros interesados con intereses opuestos en una incidencia; TRIBUNAL, el juzgado o un organismo "
     "(aclarado en el nombre del hito); AMBAS, cualquiera de los interesados. Ver la hoja Valores y las dudas D41 y D42.", False),
    ("Fase Previa: son los hitos anteriores a la promoción del sucesorio. La app los separa en un flujo PREJUDICIAL "
     "(duda D43).", False),
    ("Plazos que fija el juez (partidor, aceptación de cargos, diferimiento de la declaratoria): el hito es SIN_PLAZO "
     "y el checklist indica que el abogado lo carga como plazo suelto.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
NODOS = [
    ("SUC_010", "Previa", "Consulta inicial por el fallecimiento del causante", "ACTORA",
     "Fecha de fallecimiento que consta en la partida de defunción", 0, "SIN_PLAZO", "NO",
     "Arts. 2277 y 2280 CCyC", "SI", "NO",
     ["Registrar la fecha y el lugar del fallecimiento y el último domicilio real del causante",
      "Identificar a quién representamos: heredero forzoso (descendiente, ascendiente o cónyuge), colateral, "
      "heredero instituido, legatario o acreedor",
      "Armar el árbol familiar con los posibles herederos y sus domicilios",
      "Preguntar por matrimonio vigente, divorcio o unión convivencial: el conviviente no hereda, pero puede invocar "
      "el derecho real de habitación del art. 527 CCyC",
      "Detectar herederos menores de edad o con capacidad restringida",
      "Detectar si el causante era extranjero, vivía en el exterior o tenía bienes fuera de PBA o del país",
      "Si hay acreedores que presionan, tener en cuenta que pueden promover el sucesorio pasados 4 meses del "
      "fallecimiento (art. 729 CPCCBA)",
      "Firmar el poder o pactar el patrocinio, y el convenio de honorarios (Ley 14.967)"],
     ["DNI del consultante", "Partida de defunción (si ya la tiene)", "Poder o carta poder"]),
    ("SUC_015", "Previa", "Control de la caducidad del derecho de aceptar la herencia", "ACTORA",
     "Fallecimiento del causante (apertura de la sucesión)", 10, "ANIOS", "NO",
     "Arts. 2277, 2288 y 2293 CCyC", "NO", "NO",
     ["Si el heredero que representamos todavía no aceptó, aceptar antes del vencimiento: promover el sucesorio o "
      "cualquier acto que suponga la aceptación alcanza (art. 2293 CCyC)",
      "Al vencimiento, el heredero que no aceptó es tenido por renunciante",
      "Si el llamado es en defecto de un heredero que aceptó y después fue excluido, el plazo corre desde la "
      "exclusión: editar la fecha de inicio"],
     []),
    ("SUC_016", "Previa", "Vencimiento máximo del ITGB: 24 meses desde el fallecimiento", "ACTORA",
     "Fallecimiento del causante", 24, "MESES", "NO",
     "Art. 322 inc. b Código Fiscal PBA (Ley 10.397); Ley 14.044", "NO", "NO",
     ["El ITGB vence a los 15 días de pedir la inscripción o la entrega de los bienes, o a los 24 meses del "
      "fallecimiento, lo que ocurra primero",
      "Si se cumplen los 24 meses sin haber pedido la inscripción, presentar la declaración jurada y pagar igual "
      "(SUC_910)",
      "Las cesiones de derechos hereditarios anteriores a los 24 meses siguen la misma regla",
      "Aunque la herencia no supere el mínimo no imponible, puede corresponder presentar la declaración jurada, "
      "salvo las transmisiones exentas del art. 320 del Código Fiscal"],
     []),
    ("SUC_020", "Previa", "Reunión de las partidas que acreditan el fallecimiento y el vínculo", "ACTORA",
     "Decisión de promover el sucesorio", 0, "SIN_PLAZO", "NO",
     "Art. 724 CPCCBA; arts. 103, 109 y 2340 CCyC", "NO", "NO",
     ["Pedir la partida de defunción actualizada al Registro Provincial de las Personas",
      "Pedir las partidas de nacimiento de los hijos y, si heredan nietos por representación, la del hijo premuerto",
      "Pedir la partida de matrimonio actualizada y controlar las notas marginales de divorcio",
      "En la sucesión de colaterales, reunir las partidas que unan a cada heredero con el causante hasta el "
      "ascendiente común",
      "Si hay menores o personas con capacidad restringida, reunir la designación del representante y prever la "
      "intervención del Ministerio Público (art. 103 CCyC)",
      "Si el representante es coheredero del menor, prever la designación de un tutor especial (art. 109 inc. a CCyC)",
      "Partidas extranjeras: apostilla o legalización y traducción pública"],
     ["Partida de defunción", "Partidas de nacimiento", "Partida de matrimonio",
      "Sentencia de restricción de la capacidad o designación del representante (si corresponde)",
      "Apostilla y traducción pública (partidas extranjeras)"]),
    ("SUC_030", "Previa", "Último domicilio del causante y juzgado competente", "ACTORA",
     "Partidas reunidas", 0, "SIN_PLAZO", "NO",
     "Arts. 2336, 2643 y 2644 CCyC; art. 61 Ley 5827", "NO", "NO",
     ["Acreditar el último domicilio real del causante (DNI, partida de defunción u otra constancia)",
      "Definir el departamento judicial",
      "Verificar si en el partido es competente el Juzgado de Paz Letrado (art. 61 ap. II inc. l Ley 5827: todos los "
      "partidos salvo los 20 del ap. I) o el Juzgado Civil y Comercial",
      "Tener en cuenta el fuero de atracción: la petición de herencia, la nulidad del testamento y los litigios de la "
      "administración y la partición van ante el juez del sucesorio (art. 2336 CCyC)",
      "Si el causante vivía en el exterior, evaluar la jurisdicción (art. 2643 CCyC) y la ley aplicable (art. 2644 "
      "CCyC: los inmuebles en el país se rigen por el derecho argentino)",
      "Si hay un testamento otorgado en el exterior, revisar su validez formal (art. 2645 CCyC)",
      "No corresponde mediación previa: el sucesorio está excluido (art. 4 inc. 8 Ley 13.951)"],
     ["Constancia del último domicilio"]),
    ("SUC_040", "Previa", "Búsqueda de testamento", "ACTORA",
     "Decisión de promover el sucesorio", 0, "SIN_PLAZO", "NO",
     "Arts. 2339, 2473, 2477 y 2479 CCyC; art. 724 CPCCBA", "NO", "NO",
     ["Preguntar a la familia y revisar los papeles del causante: el ológrafo tiene que estar íntegramente escrito, "
      "fechado y firmado de puño y letra (art. 2477 CCyC)",
      "Si hay testamento por acto público, identificar al escribano y el registro notarial",
      "El informe formal del Registro de Testamentos del Colegio de Escribanos lo pide el juzgado por oficio, después "
      "de la apertura (art. 724 CPCCBA)",
      "Si el causante vivió o testó en otra jurisdicción, evaluar pedir informe al registro de esa jurisdicción "
      "(a verificar cuál)",
      "Testamento cerrado: el CCyC solo admite las formas que regula (art. 2473 CCyC); un cerrado solo podría valer "
      "si se otorgó antes del 01/08/2015 o en el extranjero (duda D09)"],
     ["Testamento original o datos de la escritura (si existe)"]),
    ("SUC_050", "Previa", "Relevamiento del acervo: bienes y deudas", "ACTORA",
     "Consulta inicial", 0, "SIN_PLAZO", "NO",
     "Arts. 2317, 2335, 2356 y 2360 CCyC", "NO", "NO",
     ["Inmuebles: copia del título, partida inmobiliaria y valuación fiscal de ARBA",
      "Automotores: título y cédula; informe de dominio del DNRPA",
      "Cuentas, plazos fijos y cajas de seguridad: identificar los bancos (los saldos se informan por oficio judicial)",
      "Participaciones societarias: estatuto o contrato social y cláusulas sobre la incorporación de herederos",
      "Créditos, haberes pendientes, seguros y otros bienes registrables",
      "Determinar si cada bien es propio o ganancial (fecha y título de adquisición)",
      "Bienes en otra provincia o en el exterior",
      "Deudas: impuestos y tasas (ARBA, municipio), expensas, préstamos, tarjetas y juicios contra el causante",
      "Si el pasivo supera al activo, evaluar el concurso o la quiebra de la masa (art. 2360 CCyC); el heredero "
      "responde hasta el valor de los bienes recibidos (art. 2317 CCyC)",
      "El pago de gastos funerarios y de última enfermedad no implica aceptar la herencia (art. 2296 inc. b CCyC)"],
     ["Copias de los títulos", "Partidas inmobiliarias y valuaciones fiscales", "Títulos de los automotores",
      "Estatutos o contratos sociales", "Estados de deuda"]),
    ("SUC_100", "Apertura", "Escrito de inicio del sucesorio", "ACTORA",
     "Partidas reunidas y juzgado competente definido", 0, "SIN_PLAZO", "NO",
     "Arts. 724, 725 y 727 CPCCBA; arts. 2339 y 2340 CCyC; art. 3 Ley 8480; art. 13 Ley 6716", "NO", "NO",
     ["Justificar el carácter de parte legítima y acompañar la partida de defunción (art. 724 CPCCBA)",
      "Denunciar el nombre y el domicilio de los herederos conocidos",
      "Expresar si el derecho es exclusivo o si concurren otros herederos (art. 2340 CCyC)",
      "Presentar el testamento o indicar dónde está (art. 724 CPCCBA)",
      "Pedir el oficio al Registro de Testamentos, la comunicación al Registro de Juicios Universales y la publicación "
      "de edictos",
      "Estimar el haber hereditario: si prima facie no supera 900 Jus, los edictos van solo en el Boletín Judicial "
      "(art. 734 inc. 2 CPCCBA)",
      "Si hay bienes que necesitan gestión urgente, pedir medidas de seguridad (art. 725) o un administrador "
      "provisional (art. 727 CPCCBA)",
      "Constituir domicilio electrónico",
      "Pagar el bono de la Ley 8480 y el anticipo previsional (jus previsional) del art. 13 de la Ley 6716",
      "Presentar por la Receptoría General de Expedientes del departamento o ante el Juzgado de Paz"],
     ["Poder o patrocinio", "Partida de defunción", "Partidas del vínculo",
      "Testamento o datos de la escritura (si existe)", "Bono Ley 8480",
      "Anticipo previsional Ley 6716 (jus previsional)",
      "Planilla de sucesiones y ausencias del Registro de Juicios Universales, por duplicado (Ley 7205)"]),
    ("SUC_105", "Apertura", "Cumplimiento de los recaudos observados por el juzgado", "ACTORA",
     "Notificación de la providencia que intima a cumplir recaudos", 0, "SIN_PLAZO", "NO",
     "Arts. 724 y 725 CPCCBA", "NO", "NO",
     ["Cargar como plazo suelto el que fije el juzgado",
      "Completar las partidas, bonos, aportes o datos de los herederos que se pidieron",
      "Si la observación es improcedente, plantear la reposición en 3 días (SUC_800)"],
     ["Escrito cumpliendo lo ordenado"]),
    ("SUC_110", "Apertura", "Providencia de apertura del sucesorio", "TRIBUNAL",
     "Presentación del escrito de inicio", 0, "SIN_PLAZO", "NO",
     "Arts. 725, 734, 739 y 742 CPCCBA; arts. 2339 y 2340 CCyC", "NO", "NO",
     ["Controlar que el juez se declare competente (art. 725 CPCCBA)",
      "Controlar qué edictos ordena: cuántos días, en qué medios y por cuánto tiempo cita (duda D05)",
      "Controlar que ordene las cédulas u oficios a los herederos denunciados con domicilio conocido (art. 734 inc. 1)",
      "Controlar el oficio al Registro de Testamentos y la comunicación al Registro de Juicios Universales",
      "Si hay incapaces, controlar la vista al Ministerio Público",
      "Si se presentó un testamento ológrafo, controlar la fijación de la audiencia (art. 739)"],
     []),
    ("SUC_112", "Apertura", "Radicación ante el juez competente", "TRIBUNAL",
     "Notificación de la resolución que declara la incompetencia", 0, "SIN_PLAZO", "NO",
     "Arts. 4 y 725 CPCCBA; art. 2336 CCyC; art. 61 Ley 5827", "NO", "NO",
     ["Controlar a qué juzgado se remite (Juzgado de Paz Letrado o Civil y Comercial)",
      "Si no se comparte, apelar en 5 días (SUC_810)",
      "Una vez radicada la causa, pedir que se provea la apertura"],
     []),
    ("SUC_120", "Apertura", "Informe del Registro de Juicios Universales", "TRIBUNAL",
     "Recepción de la comunicación por el Registro", 10, "HABILES_JUDICIALES", "NO",
     "Arts. 2, 3, 3 bis, 4 y 7 Ley 7205", "NO", "NO",
     ["La secretaría comunica el inicio dentro de los 3 días; si se lo pide, el letrado diligencia la planilla "
      "(art. 3 bis)",
      "Completar la planilla de sucesiones y ausencias por duplicado y hacerla firmar y sellar por secretaría",
      "Agregar el duplicado con el número de inscripción",
      "Controlar si hay otro sucesorio del mismo causante; si lo hay, pedir la acumulación (art. 731 CPCCBA)",
      "Sin este informe el juez no puede dictar la declaratoria (art. 4 Ley 7205)",
      "Reclamar si el Registro no informa en 10 días (art. 7 Ley 7205)"],
     ["Duplicado de la planilla con la constancia de inscripción"]),
    ("SUC_130", "Apertura", "Informe del Registro de Testamentos del Colegio de Escribanos", "TRIBUNAL",
     "Libramiento del oficio al Registro de Testamentos", 0, "SIN_PLAZO", "NO",
     "Arts. 724 y 731 CPCCBA", "NO", "NO",
     ["Diligenciar el oficio y agregar la respuesta",
      "Si el informe es positivo, el juez pide al notario el testimonio (acto público) o la entrega del original",
      "Un testamento que aparece en una sucesión ab intestato cambia el trámite; si hay dos juicios, evaluar la "
      "acumulación (art. 731 CPCCBA)"],
     ["Oficio diligenciado", "Informe del Registro de Testamentos"]),
    ("SUC_140", "Apertura", "Vista al Ministerio Público", "TRIBUNAL",
     "Providencia que da vista al Ministerio Público", 0, "SIN_PLAZO", "NO",
     "Art. 103 CCyC; art. 728 inc. 1 CPCCBA; Ley 14.442 (a verificar)", "NO", "NO",
     ["Con herederos menores o con capacidad restringida, la intervención de la Asesoría de Incapaces es obligatoria: "
      "su falta causa nulidad relativa (art. 103 inc. a CCyC)",
      "Controlar el dictamen y cumplir lo que observe",
      "La intervención cesa con la declaratoria, la aprobación del testamento o la vacancia (art. 728 inc. 1 CPCCBA), "
      "pero el ministerio pupilar vuelve a intervenir en el inventario y la partición",
      "Si no hay incapaces, confirmar si igual corresponde vista al agente fiscal (duda D10)"],
     []),
    ("SUC_150", "Apertura", "Audiencia de reconocimiento del testamento ológrafo o cerrado", "AMBAS",
     "Fecha y hora de la audiencia fijada por el juzgado", 0, "FECHA_FIJADA", "NO",
     "Arts. 739 y 741 CPCCBA; arts. 2339 y 2477 CCyC", "NO", "NO",
     ["Ofrecer dos testigos que reconozcan la letra y la firma del testador (art. 739 CPCCBA)",
      "Pedir la pericia caligráfica que exige el art. 2339 CCyC y acompañar cuerpos de escritura indubitados "
      "(duda D08)",
      "Citar a los beneficiarios y a los presuntos herederos con domicilio conocido; si es cerrado, también al "
      "escribano y a los testigos",
      "Si viene en sobre cerrado, se abre en la audiencia ante el secretario",
      "Las objeciones sobre las formalidades tramitan como incidente (art. 741 CPCCBA)",
      "La protocolización no impide impugnar después la autenticidad o la validez (art. 2339 CCyC)"],
     ["Testamento original", "Datos de los dos testigos", "Cuerpos de escritura indubitados del testador"]),
    ("SUC_160", "Apertura", "Protocolización del testamento o agregación del testimonio", "TRIBUNAL",
     "Reconocimiento de la letra y la firma, o informe del notario", 0, "SIN_PLAZO", "NO",
     "Arts. 724 y 740 CPCCBA; art. 2339 CCyC", "NO", "NO",
     ["Ológrafo o cerrado: controlar que el juez rubrique el principio y el fin de cada página y designe escribano "
      "para protocolizarlo",
      "Proponer escribano y seguir la protocolización",
      "Acto público: controlar que el notario remita el testimonio de la escritura",
      "Pedir copia certificada del testamento si hace falta (art. 2339 CCyC)"],
     ["Testimonio de la protocolización o de la escritura"]),
    ("SUC_200", "Edictos y citación", "Publicación de edictos y plazo de citación de herederos y acreedores", "AMBAS",
     "Última publicación del edicto", 30, "CORRIDOS", "NO",
     "Arts. 145 a 147 y 734 CPCCBA; art. 2340 CCyC", "NO", "NO",
     ["Publicar según lo que ordenó la providencia: 1 día en el diario de publicaciones oficiales (art. 2340 CCyC) o "
      "3 días en el Boletín Judicial y en un diario del último domicilio (art. 734 inc. 2 CPCCBA); si el haber prima "
      "facie no supera 900 Jus, solo en el Boletín Judicial (duda D05)",
      "Cargar como Día Cero la fecha de la última publicación (duda D06)",
      "Agregar un ejemplar de cada publicación y el recibo de pago (art. 146 CPCCBA)",
      "Diligenciar las cédulas u oficios a los herederos denunciados con domicilio conocido en el país (art. 734 "
      "inc. 1); en otra provincia, por oficio Ley 22.172; en el exterior, por exhorto",
      "La citación es por 30 días corridos (art. 734 CPCCBA)",
      "Un heredero que se presenta después puede pedir la ampliación de la declaratoria"],
     ["Ejemplares de los edictos publicados", "Recibos de pago de las publicaciones",
      "Cédulas u oficios diligenciados"]),
    ("SUC_220", "Edictos y citación", "Citación de herederos instituidos, beneficiarios y albacea", "AMBAS",
     "Notificación personal al último de los herederos instituidos, beneficiarios y albacea", 30, "CORRIDOS", "NO",
     "Arts. 145 y 742 CPCCBA; arts. 2347 y 2523 CCyC", "NO", "NO",
     ["Notificar personalmente o por cédula a cada heredero instituido, a los legatarios y al albacea",
      "Si se ignora el domicilio, citar por edictos (art. 145 CPCCBA)",
      "Publicar además los edictos del art. 734 inc. 2 (SUC_200)",
      "El art. 742 no dice si los 30 días son corridos: la matriz los toma como corridos (duda D07)",
      "Controlar la aceptación del cargo de albacea, si el testador lo designó"],
     ["Cédulas diligenciadas"]),
    ("SUC_230", "Edictos y citación", "Intimación a un heredero a aceptar o renunciar la herencia", "DEMANDADA",
     "Notificación de la intimación judicial al heredero", 1, "MESES", "NO",
     "Arts. 2289, 2293, 2299 y 2301 CCyC", "NO", "NO",
     ["La intimación no puede pedirse hasta pasados 9 días de la muerte",
      "El juez fija entre 1 y 3 meses: editar el valor del plazo (por defecto, 1 mes)",
      "Se puede prorrogar una sola vez por justa causa",
      "Si vence sin respuesta, el heredero es tenido por aceptante",
      "La renuncia se hace por escritura pública o por acta judicial (art. 2299 CCyC); el renunciante es tratado como "
      "si nunca hubiera sido llamado (art. 2301 CCyC)"],
     ["Escrito pidiendo la intimación"]),
    ("SUC_300", "Declaratoria o aprobación del testamento", "Pedido de la declaratoria de herederos", "ACTORA",
     "Vencimiento del plazo de citación por edictos", 0, "SIN_PLAZO", "NO",
     "Arts. 735 y 736 CPCCBA; art. 4 Ley 7205", "NO", "NO",
     ["Acreditar los edictos publicados y el vencimiento del plazo de 30 días",
      "Acreditar las cédulas u oficios a los herederos denunciados",
      "Agregar el informe del Registro de Juicios Universales (sin él no hay declaratoria) y el del Registro de "
      "Testamentos",
      "Acreditar el vínculo de cada heredero con las partidas",
      "Si un heredero no acreditó el vínculo, el juez difiere la declaratoria por el plazo que fije (art. 735): "
      "cargarlo como plazo suelto",
      "Los herederos mayores pueden admitir por unanimidad a coherederos que no justificaron el vínculo (art. 736 "
      "CPCCBA)"],
     ["Edictos y recibos", "Cédulas u oficios diligenciados",
      "Informes del Registro de Juicios Universales y del Registro de Testamentos"]),
    ("SUC_310", "Declaratoria o aprobación del testamento", "Dictado de la declaratoria de herederos", "TRIBUNAL",
     "Pedido de la declaratoria", 0, "SIN_PLAZO", "NO",
     "Arts. 735 y 737 CPCCBA; arts. 2337, 2338 y 2433 CCyC", "NO", "NO",
     ["Controlar nombres, documentos y vínculos de cada heredero: un error obliga a pedir aclaratoria",
      "Controlar el carácter del cónyuge: concurriendo con descendientes no hereda en los gananciales del causante "
      "(art. 2433 CCyC)",
      "La declaratoria se dicta sin perjuicio de terceros (art. 737 CPCCBA)",
      "Informar al cliente"],
     []),
    ("SUC_320", "Declaratoria o aprobación del testamento", "Aprobación formal del testamento", "TRIBUNAL",
     "Vencimiento del plazo de citación de los herederos instituidos", 0, "SIN_PLAZO", "NO",
     "Art. 743 CPCCBA; arts. 2338, 2340, 2444 y 2445 CCyC", "NO", "NO",
     ["Controlar que el juez se pronuncie sobre la validez formal del testamento",
      "La aprobación da la posesión de la herencia a los herederos que no la tienen de pleno derecho",
      "Si el testamento no dispone de todos los bienes, por el resto se pide la declaratoria (art. 2340 CCyC)",
      "Si hay legados, controlar que no afecten la legítima (arts. 2444 y 2445 CCyC)"],
     []),
    ("SUC_330", "Declaratoria o aprobación del testamento",
     "Elección del trámite posterior a la declaratoria o a la aprobación del testamento", "ACTORA",
     "Notificación de la declaratoria o de la aprobación del testamento", 0, "SIN_PLAZO", "NO",
     "Arts. 732, 733 y 751 CPCCBA; arts. 2342, 2369 y 2371 CCyC", "NO", "NO",
     ["Si todos los herederos son capaces y están de acuerdo: denuncia de bienes e inscripción de la declaratoria "
      "(condominio) o partición privada",
      "Si hay incapaces, ausentes, oposición de terceros o desacuerdo: inventario y partición judiciales "
      "(art. 2371 CCyC)",
      "Si lo piden los acreedores, el fisco o un heredero, el inventario es judicial (art. 751 CPCCBA)",
      "Con todos capaces y de acuerdo, se puede seguir extrajudicialmente (art. 733 CPCCBA)",
      "Unión convivencial: el conviviente no hereda; si invoca el derecho real de habitación (art. 527 CCyC), "
      "registrarlo y cargar como plazo suelto su máximo de 2 años (duda D24)",
      "Cesión de derechos hereditarios: por escritura pública (art. 1618 CCyC); tiene efectos frente a los demás "
      "herederos desde que se agrega al expediente (art. 2302 CCyC)"],
     []),
    ("SUC_340", "Declaratoria o aprobación del testamento", "Ampliación de la declaratoria de herederos", "AMBAS",
     "Presentación de un heredero omitido", 0, "SIN_PLAZO", "NO",
     "Art. 738 CPCCBA", "NO", "NO",
     ["Acreditar el vínculo del nuevo heredero",
      "Pedir la ampliación: procede en cualquier estado del proceso",
      "Si la declaratoria ya se inscribió, inscribir también la ampliación",
      "Reajustar las porciones, la tasa de justicia y el ITGB"],
     ["Partidas del heredero omitido"]),
    ("SUC_350", "Declaratoria o aprobación del testamento", "Herencia vacante y designación del curador", "TRIBUNAL",
     "Vencimiento de la citación sin herederos que acrediten su título", 0, "SIN_PLAZO", "NO",
     "Arts. 735, 768, 770 y 771 CPCCBA; arts. 2424 y 2441 a 2443 CCyC", "NO", "NO",
     ["El curador provisional es el Fiscal de Estado o el letrado que lo represente (art. 768 CPCCBA)",
      "Con la vacancia, el curador pasa a ser definitivo e insta el inventario (art. 770)",
      "La vacancia se inscribe en los registros por oficio (art. 2441 CCyC)",
      "Los bienes se rematan para pagar deudas y legados, y el resto va al Estado donde están situados "
      "(arts. 2424 y 2443 CCyC)",
      "Quien reclame después tiene que promover la petición de herencia (art. 771 CPCCBA)",
      "Si representamos a un acreedor o a quien denunció la vacancia, instar el trámite (art. 768)"],
     []),
    ("SUC_400", "Administración", "Audiencia de designación de administrador, inventariador y tasador", "AMBAS",
     "Fecha y hora de la audiencia fijada por el juzgado", 0, "FECHA_FIJADA", "NO",
     "Arts. 732, 744, 754 y 757 CPCCBA; arts. 2346 y 2347 CCyC", "NO", "NO",
     ["Notificar por cédula a los herederos, a los legatarios de parte alícuota y a los funcionarios (art. 732)",
      "Llevar la propuesta de administrador: a falta de acuerdo, el cónyuge supérstite y después el propuesto por la "
      "mayoría (art. 744 CPCCBA; art. 2346 CCyC)",
      "Si el testador designó administrador o albacea, se respeta (art. 2347 CCyC)",
      "Proponer escribano inventariador y perito tasador: basta la mayoría de los herederos presentes (art. 754)",
      "Confirmar la asistencia del cliente"],
     ["Cédulas de citación a la audiencia"]),
    ("SUC_410", "Administración", "Aceptación del cargo de administrador", "AMBAS",
     "Notificación de la designación del administrador", 0, "SIN_PLAZO", "NO",
     "Arts. 745, 746 y 750 CPCCBA; arts. 2345, 2349 y 2350 CCyC", "NO", "NO",
     ["Aceptar el cargo ante el secretario; cargar como plazo suelto el que fije el juzgado",
      "Pedir el testimonio del nombramiento y la puesta en posesión por oficial de justicia (art. 745)",
      "Constituir la garantía si se la exige (art. 2350 CCyC)",
      "Pedir expediente de administración separado si la gestión es compleja (art. 746)",
      "Abrir o identificar la cuenta judicial en el Banco de la Provincia de Buenos Aires",
      "El administrador no cobra honorarios definitivos hasta que se apruebe la cuenta final (art. 750)"],
     ["Acta de aceptación del cargo", "Testimonio del nombramiento"]),
    ("SUC_420", "Administración", "Rendición de cuentas del administrador", "AMBAS",
     "Aceptación del cargo o presentación de la rendición anterior", 3, "MESES", "NO",
     "Arts. 748 y 749 CPCCBA; arts. 2355 y 2362 CCyC", "NO", "NO",
     ["Rendir cuentas cada 3 meses, salvo otro plazo acordado por la mayoría o fijado por el juez: editar el valor",
      "Las rendiciones parciales quedan 5 días en secretaría para observaciones; la final, 10 días (art. 748)",
      "Si no se observan, el juez las aprueba; si se observan, tramitan como incidente",
      "Si representamos a otro heredero, controlar la rendición y observarla en término",
      "Por mal desempeño se puede pedir la remoción, por incidente (art. 749 CPCCBA)",
      "Al terminar la administración, presentar la cuenta final"],
     ["Rendición de cuentas con comprobantes"]),
    ("SUC_440", "Administración", "Pago de deudas y legados, y venta de bienes con autorización", "AMBAS",
     "Aceptación del cargo de administrador o albacea", 0, "SIN_PLAZO", "NO",
     "Arts. 2353, 2354, 2356 a 2358 y 2526 CCyC; arts. 736 y 747 CPCCBA", "NO", "NO",
     ["Recibir la denuncia de los acreedores y pedir la declaración de legítimo abono de los créditos reconocidos "
      "(arts. 2356 y 2357 CCyC; art. 736 CPCCBA)",
      "Pagar a los acreedores según el orden de la ley de concursos y después los legados, dentro de la porción "
      "disponible (art. 2358 CCyC)",
      "Para vender bienes que no sean perecederos: acuerdo unánime de los herederos o autorización judicial "
      "(art. 2353 CCyC)",
      "Pedir la autorización por escrito fundado, con tasación, y con vista al Ministerio Público si hay incapaces",
      "Depositar el precio en la cuenta judicial",
      "Cobrar créditos e iniciar acciones requiere autorización judicial o de los copartícipes (art. 2354 CCyC)",
      "Si actúa el albacea, paga los legados con conocimiento de los herederos (art. 2526 CCyC)"],
     ["Escrito pidiendo la autorización de venta", "Tasación del bien", "Boleta de depósito del precio"]),
    ("SUC_500", "Inventario y avalúo", "Inventario y avalúo judiciales", "AMBAS",
     "Fecha, hora y lugar de la diligencia de inventario notificados a los interesados", 0, "FECHA_FIJADA", "NO",
     "Arts. 751 y 753 a 758 CPCCBA; arts. 2341 y 2343 CCyC", "NO", "NO",
     ["El inventario lo hace el escribano designado, con citación personal de las partes, los acreedores, los "
      "legatarios y el representante de ARBA (art. 756)",
      "Concurrir a la diligencia, denunciar bienes y dejar constancia de las observaciones en el acta",
      "Bienes fuera de la jurisdicción: se comisiona al juez del lugar (art. 755)",
      "El avalúo lo hace el perito designado, en lo posible junto con el inventario (art. 757)",
      "Con conformidad de partes, valuación fiscal para los inmuebles y cotización para los títulos (art. 758)",
      "El valor se fija a la época más próxima posible a la partición (art. 2343 CCyC)"],
     ["Acta de inventario", "Dictamen de avalúo"]),
    ("SUC_505", "Inventario y avalúo", "Inventario intimado por acreedores o legatarios", "ACTORA",
     "Notificación de la intimación judicial a los herederos para hacer el inventario", 3, "MESES", "NO",
     "Arts. 2321 inc. a y 2341 CCyC", "NO", "NO",
     ["Hacer el inventario dentro de los 3 meses de la intimación",
      "Si no se hace, el heredero responde con sus propios bienes (art. 2321 inc. a CCyC)",
      "No ocultar bienes ni exagerar el pasivo (art. 2321 incs. b y c CCyC)"],
     ["Inventario presentado"]),
    ("SUC_510", "Inventario y avalúo", "Denuncia de bienes y valuación por los herederos", "ACTORA",
     "Acuerdo de los herederos para reemplazar el inventario", 0, "SIN_PLAZO", "NO",
     "Arts. 751 y 758 CPCCBA; art. 2342 CCyC; art. 337 inc. f Código Fiscal", "NO", "NO",
     ["Procede por voluntad unánime, salvo que el inventario lo pidan los acreedores o lo imponga la ley "
      "(art. 2342 CCyC)",
      "Con incapaces, hace falta la conformidad del ministerio pupilar (art. 751)",
      "Denunciar cada bien con sus datos registrales y su carácter propio o ganancial",
      "Valuar: valuación fiscal de los inmuebles y cotización de los títulos al día del fallecimiento, con "
      "conformidad de partes (art. 758)",
      "Preparar la declaración jurada patrimonial firmada por los letrados para la tasa de justicia (art. 337 inc. f "
      "Código Fiscal)",
      "ARBA puede oponerse; en ese caso resuelve el juez (art. 751)"],
     ["Escrito de denuncia de bienes", "Valuaciones fiscales e informes de dominio",
      "Declaración jurada patrimonial"]),
    ("SUC_520", "Inventario y avalúo", "Liquidación de los gananciales con el cónyuge supérstite", "DEMANDADA",
     "Denuncia o inventario con bienes gananciales", 0, "SIN_PLAZO", "NO",
     "Arts. 481, 497, 498, 2383 y 2433 CCyC; art. 337 inc. f Código Fiscal", "NO", "NO",
     ["La indivisión poscomunitaria por muerte se rige por las reglas de la indivisión hereditaria (art. 481 CCyC)",
      "Separar los bienes propios y los gananciales del causante",
      "El cónyuge recibe la mitad de los gananciales como socio, no como heredero; los herederos reciben la otra "
      "mitad (art. 498 CCyC)",
      "Concurriendo con descendientes, el cónyuge no hereda en los gananciales del causante (art. 2433 CCyC)",
      "Derecho real de habitación del cónyuge sobre el último hogar conyugal (art. 2383 CCyC)",
      "La tasa de justicia se calcula sin la parte ganancial del cónyuge (art. 337 inc. f Código Fiscal)"],
     ["Títulos con la fecha de adquisición de cada bien"]),
    ("SUC_530", "Inventario y avalúo", "Traslado del inventario y avalúo o de la denuncia de bienes", "AMBAS",
     "Notificación por cédula de la puesta de manifiesto del inventario y avalúo", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 759 y 760 CPCCBA; art. 2344 CCyC", "NO", "NO",
     ["Revisar la inclusión y exclusión de bienes y los valores",
      "Oponerse dentro de los 5 días (art. 759)",
      "Los reclamos sobre inclusión o exclusión de bienes tramitan como incidente; los del avalúo, en audiencia con "
      "el perito, y la resolución no es recurrible (art. 760)",
      "Si se demuestra que el valor no es correcto, se ordena la retasa (art. 2344 CCyC)",
      "Para la denuncia de bienes, confirmar si también se pone de manifiesto (duda D22)"],
     ["Escrito de conformidad u oposición"]),
    ("SUC_540", "Inventario y avalúo", "Aprobación del inventario y avalúo", "TRIBUNAL",
     "Vencimiento del traslado sin oposición o resolución de las reclamaciones", 0, "SIN_PLAZO", "NO",
     "Art. 759 CPCCBA; arts. 2365 y 2372 CCyC", "NO", "NO",
     ["Controlar la resolución que aprueba",
      "Desde la aprobación se puede pedir la partición (art. 2365 CCyC)",
      "Para pedir la licitación de un bien hay 30 días desde la aprobación de la tasación (art. 2372 CCyC): cargarlo "
      "como plazo suelto (duda D25)",
      "Decidir con el cliente: inscripción en condominio, partición privada o partición judicial"],
     []),
    ("SUC_600", "Partición", "Partición privada", "ACTORA",
     "Acuerdo de todos los copartícipes presentes y plenamente capaces", 0, "SIN_PLAZO", "NO",
     "Art. 761 CPCCBA; arts. 2369, 2374, 2375, 2380, 2381 y 2385 CCyC", "NO", "NO",
     ["Confirmar que todos estén presentes y sean plenamente capaces (art. 2369 CCyC)",
      "Armar los lotes: partición en especie, salvo división antieconómica (arts. 2374 y 2375 CCyC)",
      "Considerar la atribución preferencial de la vivienda o del establecimiento (arts. 2380 y 2381 CCyC)",
      "Incluir la colación de donaciones, si corresponde (art. 2385 CCyC)",
      "Instrumentar el acuerdo y presentarlo para su aprobación (forma a verificar, duda D25)",
      "Puede ser total o parcial"],
     ["Convenio de partición firmado por todos", "Escrito pidiendo la aprobación"]),
    ("SUC_610", "Partición", "Designación del partidor y presentación de la cuenta particionaria", "TRIBUNAL",
     "Aceptación del cargo por el partidor", 0, "SIN_PLAZO", "NO",
     "Arts. 762 a 764 CPCCBA; arts. 2371 a 2373 CCyC", "NO", "NO",
     ["La partición es judicial si hay incapaces, ausentes, oposición de terceros o desacuerdo (art. 2371 CCyC)",
      "El partidor tiene que ser abogado y se designa como el inventariador (art. 762)",
      "Cargar como plazo suelto el que fije el juez para presentar la cuenta, bajo apercibimiento de remoción "
      "(art. 763)",
      "Dar al partidor la información y participar de la audiencia en la que oye a los interesados (art. 764)",
      "La licitación no se puede pedir pasados 30 días de la aprobación de la tasación (art. 2372 CCyC)"],
     ["Escrito proponiendo partidor"]),
    ("SUC_620", "Partición", "Traslado de la cuenta particionaria", "AMBAS",
     "Notificación por cédula de la puesta de manifiesto de la cuenta particionaria", 10, "HABILES_JUDICIALES", "SI",
     "Arts. 766 y 767 CPCCBA", "NO", "NO",
     ["Revisar la formación de la masa, las deducciones y las hijuelas",
      "Oponerse dentro de los 10 días",
      "Si hay oposición, el juez cita a audiencia y, sin acuerdo, resuelve dentro de los 10 días (art. 767)",
      "Quien impugnó y no va a la audiencia queda desistido, con costas",
      "Sin oposición, el juez aprueba la cuenta previa vista al ministerio pupilar; solo es apelable la resolución "
      "que la rechaza (art. 766)"],
     ["Escrito de conformidad u oposición"]),
    ("SUC_650", "Partición", "Colación y reducción para proteger la legítima", "AMBAS",
     "Reclamo de un coheredero por donaciones o disposiciones que afectan su legítima", 0, "SIN_PLAZO", "NO",
     "Arts. 2336, 2385, 2386, 2445, 2452, 2453 y 2459 CCyC", "NO", "NO",
     ["Identificar las donaciones del causante a descendientes o al cónyuge",
      "Calcular la legítima: 2/3 para los descendientes, 1/2 para los ascendientes, 1/2 para el cónyuge "
      "(art. 2445 CCyC)",
      "Colación: el valor se determina a la época de la partición (art. 2385 CCyC)",
      "Reducción: primero las disposiciones testamentarias y después las donaciones, de la última a la primera "
      "(arts. 2452 y 2453 CCyC)",
      "Tramita como juicio ante el juez del sucesorio (art. 2336 CCyC); verificar la mediación previa y la "
      "prescripción (dudas D04 y D26)"],
     ["Demanda de colación o reducción"]),
    ("SUC_660", "Partición", "Continuación extrajudicial del sucesorio", "ACTORA",
     "Declaratoria dictada o testamento aprobado, con todos los herederos capaces y de acuerdo", 0, "SIN_PLAZO", "NO",
     "Art. 733 CPCCBA", "NO", "NO",
     ["Hacer el inventario, el avalúo, la partición y la adjudicación con la intervención y la conformidad de los "
      "organismos administrativos",
      "Las desinteligencias entre herederos o con los organismos vuelven al juez del sucesorio",
      "Agregar al expediente copia de las actuaciones: sin eso no se regulan honorarios ni se expide el certificado "
      "del secretario para inscribir",
      "Los honorarios son los mismos que si el trámite se hubiera hecho en el juzgado"],
     ["Copia de las actuaciones extrajudiciales", "Certificado del secretario"]),
    ("SUC_700", "Inscripción", "Pedido de la orden de inscripción", "ACTORA",
     "Aprobación del inventario o la partición, o decisión de inscribir la declaratoria en condominio", 0,
     "SIN_PLAZO", "NO",
     "Art. 765 CPCCBA; arts. 322 inc. b y 338 inc. c Código Fiscal", "NO", "NO",
     ["Pedir la inscripción de la declaratoria, del testamento o de las hijuelas",
      "Este pedido es el Día Cero del ITGB (15 días) y el momento de pagar la tasa de justicia",
      "Pedir los certificados de dominio e inhibición de los inmuebles (art. 765 CPCCBA)",
      "Pedir la regulación de honorarios",
      "Si hay bienes en otra jurisdicción, pedir que se libre oficio Ley 22.172"],
     ["Escrito pidiendo la inscripción", "Certificados de dominio e inhibición"]),
    ("SUC_740", "Inscripción", "Orden de inscripción y libramiento de oficios y testimonios", "TRIBUNAL",
     "Acreditación del pago de la tasa de justicia, el ITGB, los honorarios y los aportes", 0, "SIN_PLAZO", "NO",
     "Art. 765 CPCCBA; art. 341 Código Fiscal; art. 21 Ley 6716; art. 2 inc. b Ley 7205", "NO", "NO",
     ["Controlar que estén pagados o afianzados la tasa, el ITGB, los honorarios y los aportes: sin eso el juez no "
      "ordena la transferencia (art. 341 Código Fiscal; art. 21 Ley 6716)",
      "Preparar el testimonio para el Registro de la Propiedad Inmueble con los recaudos que exija (a verificar)",
      "Preparar los oficios al DNRPA, a los bancos y a las sociedades",
      "Comunicar la inscripción de la declaratoria al Registro de Juicios Universales (art. 2 inc. b Ley 7205)"],
     ["Testimonios y oficios firmados"]),
    ("SUC_750", "Inscripción", "Inscripción en el Registro de la Propiedad Inmueble de PBA", "TRIBUNAL",
     "Ingreso del testimonio en el Registro de la Propiedad", 0, "SIN_PLAZO", "NO",
     "Decreto-Ley 11.643/63; Ley 17.801; art. 2363 CCyC", "NO", "NO",
     ["Ingresar el testimonio con el certificado de dominio vigente y pagar las tasas registrales",
      "Seguir el trámite y subsanar las observaciones del Registro",
      "La partición de bienes registrables es oponible a terceros desde su inscripción (art. 2363 CCyC)",
      "Retirar el testimonio inscripto y entregarlo al cliente"],
     ["Testimonio inscripto"]),
    ("SUC_752", "Inscripción", "Inscripción de automotores en el DNRPA", "TRIBUNAL",
     "Presentación del oficio en el Registro Seccional", 0, "SIN_PLAZO", "NO",
     "Decreto-Ley 6582/58 y normas técnico-registrales del DNRPA (a verificar)", "NO", "NO",
     ["Presentar el oficio o el testimonio en el Registro Seccional del automotor",
      "Usar la solicitud tipo que indique el Registro (a verificar)",
      "Controlar las deudas de patentes e infracciones",
      "Retirar el título a nombre de los herederos"],
     ["Oficio al Registro Seccional", "Título del automotor"]),
    ("SUC_754", "Inscripción", "Transferencia de fondos y de participaciones societarias", "TRIBUNAL",
     "Diligenciamiento de los oficios a los bancos y a las sociedades", 0, "SIN_PLAZO", "NO",
     "Art. 725 CPCCBA; art. 17 Ley 6716 (a verificar); Ley General de Sociedades 19.550 (artículos a verificar)",
     "NO", "NO",
     ["Oficiar a los bancos para transferir los saldos a la cuenta judicial o a los herederos",
      "Pedir el libramiento de giros desde la cuenta judicial del Banco de la Provincia de Buenos Aires",
      "Oficiar a las sociedades para registrar a los herederos en el libro de accionistas o inscribir la adjudicación "
      "de cuotas",
      "Controlar las retenciones de aportes en las libranzas"],
     ["Oficios a bancos y sociedades", "Constancias de transferencia"]),
    ("SUC_756", "Inscripción", "Venta por los herederos con tracto abreviado", "ACTORA",
     "Decisión de vender un bien sin inscribir antes la declaratoria", 0, "SIN_PLAZO", "NO",
     "Art. 16 Ley 17.801 (inciso a verificar)", "NO", "NO",
     ["Coordinar con el escribano: la escritura se otorga con la declaratoria o el testamento, sin inscribirlos antes",
      "Pagar igual la tasa de justicia y el ITGB",
      "Si hay incapaces, hace falta autorización judicial",
      "Pedir la orden judicial que necesite el escribano"],
     ["Testimonio de la declaratoria para el escribano", "Certificados de dominio e inhibición"]),
    ("SUC_758", "Inscripción", "Inscripción de bienes en otra jurisdicción por oficio Ley 22.172", "ACTORA",
     "Libramiento del oficio a la otra jurisdicción", 0, "SIN_PLAZO", "NO",
     "Ley 22.172 (adhesión de PBA y de la jurisdicción de destino a verificar)", "NO", "NO",
     ["Confeccionar el oficio con los recaudos del convenio y autorizar a un letrado de la otra jurisdicción",
      "Pagar las tasas y aportes locales que correspondan",
      "Seguir la inscripción y agregar las constancias"],
     ["Oficio Ley 22.172", "Constancia de inscripción en la otra jurisdicción"]),
    ("SUC_900", "Impuestos y tasas", "Pago de la tasa de justicia y de la contribución para la Caja de Abogados",
     "ACTORA",
     "Pedido de inscripción de la declaratoria, el testamento o las hijuelas", 0, "SIN_PLAZO", "NO",
     "Arts. 332, 337 inc. f, 338 inc. c y 341 Código Fiscal; Ley Impositiva 2026 (Ley 15.558); art. 12 inc. g "
     "Ley 6716", "NO", "NO",
     ["Liquidar sobre el valor del activo, sin la parte ganancial del cónyuge supérstite (art. 337 inc. f Código "
      "Fiscal), con la alícuota de la Ley Impositiva vigente (a verificar: 22 por mil)",
      "Usar la valuación fiscal vigente a la fecha del auto que ordena la inscripción (art. 332 Código Fiscal)",
      "Presentar la declaración jurada patrimonial firmada por los letrados",
      "Pagar junto con la tasa la contribución del 5% para la Caja de Abogados (art. 12 inc. g Ley 6716)",
      "Sin la tasa pagada no se ordenan entregas ni transferencias (art. 341 Código Fiscal)",
      "Si la tasa se pagó antes, integrar la diferencia si cambió la valuación (duda D28)"],
     ["Boleta de la tasa de justicia", "Boleta de la contribución Ley 6716", "Declaración jurada patrimonial"]),
    ("SUC_910", "Impuestos y tasas", "Declaración jurada y pago del ITGB ante ARBA", "ACTORA",
     "Solicitud judicial de inscripción, entrega de bienes o libramiento de fondos", 15, "CORRIDOS", "NO",
     "Ley 14.044; arts. 320 y 322 inc. b Código Fiscal; art. 728 inc. 3 CPCCBA", "NO", "NO",
     ["Generar la declaración jurada en el sistema TGB de ARBA, con CUIT y CIT, incluyendo al causante, a cada "
      "beneficiario y cada bien",
      "Presentarla aunque no se supere el mínimo no imponible, salvo las transmisiones exentas del art. 320 del "
      "Código Fiscal",
      "Pagar o adherir a un plan de pagos (a verificar)",
      "La presentación y el pago tienen que ser previos o simultáneos a la inscripción o la entrega de los bienes",
      "Acompañar al expediente la constancia de presentación y el comprobante de pago",
      "Si antes se cumplen los 24 meses desde el fallecimiento, rige ese vencimiento (SUC_016)"],
     ["Constancia de presentación de la declaración jurada del ITGB", "Comprobante de pago"]),
    ("SUC_920", "Impuestos y tasas", "Regulación de honorarios", "TRIBUNAL",
     "Pedido de regulación de honorarios", 0, "SIN_PLAZO", "NO",
     "Arts. 28 inc. c y 35 Ley 14.967; art. 733 CPCCBA", "NO", "NO",
     ["Pedir la regulación sobre el acervo, incluidos los gananciales (art. 35 Ley 14.967)",
      "Si un solo abogado representa a todos, escala del 6% al 20%; etapas: 1/4 por la iniciación, 1/4 hasta la "
      "declaratoria o la aprobación del testamento y 1/2 hasta la orden de inscripción",
      "Inmuebles por valuación fiscal, o por tasación o venta si es mayor; vivienda única familiar: mínimo de la "
      "escala",
      "Controlar la notificación de la regulación"],
     ["Escrito pidiendo la regulación"]),
    ("SUC_925", "Impuestos y tasas", "Apelación de la regulación de honorarios", "AMBAS",
     "Notificación de la regulación de honorarios", 5, "HABILES_JUDICIALES", "SI",
     "Art. 57 Ley 14.967", "NO", "NO",
     ["Apelar dentro de los 5 días; el recurso solo puede fundarse en el mismo escrito",
      "No hay sustanciación; la Cámara resuelve dentro de los 10 días de recibido el expediente",
      "No hay recurso si la regulación la hizo la Cámara o la Suprema Corte"],
     ["Escrito de apelación fundado"]),
    ("SUC_930", "Impuestos y tasas", "Pago de honorarios y depósito de los aportes de la Ley 6716", "ACTORA",
     "Fecha en que queda firme el auto regulatorio", 60, "CORRIDOS", "NO",
     "Arts. 12 inc. a, 13, 14 y 21 Ley 6716", "NO", "NO",
     ["Depositar el 10% a cargo del abogado y el 5% a cargo del obligado al pago, por ser un juicio voluntario "
      "(art. 12 inc. a Ley 6716)",
      "Descontar el anticipo pagado al inicio (art. 13)",
      "Pasados los 60 días corridos se deben intereses (art. 14)",
      "Sin honorarios y aportes pagados o afianzados, el juez no ordena la adjudicación ni la transferencia ni el "
      "archivo (art. 21)"],
     ["Boleta de aportes", "Recibo de honorarios"]),
    ("SUC_800", "Recursos e incidentes", "Reposición contra una providencia simple", "AMBAS",
     "Notificación de la providencia", 3, "HABILES_JUDICIALES", "SI",
     "Arts. 238 a 240 y 248 CPCCBA", "NO", "NO",
     ["Interponer y fundar por escrito dentro de los 3 días",
      "Si la providencia causa un gravamen irreparable, plantear la apelación en subsidio: no se funda por separado "
      "(art. 248)",
      "Controlar la resolución"],
     ["Escrito de reposición"]),
    ("SUC_810", "Recursos e incidentes", "Apelación de una resolución del sucesorio", "AMBAS",
     "Notificación de la resolución", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 166 inc. 2, 242 a 245 y 275 CPCCBA", "NO", "NO",
     ["Apelar dentro de los 5 días; fuera de la sentencia del juicio ordinario o sumario, se concede en relación "
      "(art. 243)",
      "Limitarse a interponer el recurso: se funda en el memorial (art. 245)",
      "Si la resolución tiene errores materiales (por ejemplo, nombres o documentos en la declaratoria), pedir "
      "aclaratoria dentro de los 3 días (art. 166 inc. 2; aplicación a la declaratoria a verificar)",
      "Si se deniega la apelación, queja ante la Cámara en 5 días (art. 275)",
      "Si la Cámara revoca, retomar manualmente la etapa que corresponda"],
     ["Escrito de apelación"]),
    ("SUC_815", "Recursos e incidentes", "Memorial de la apelación en relación", "AMBAS",
     "Notificación de la providencia que concede el recurso", 5, "HABILES_JUDICIALES", "SI",
     "Art. 246 CPCCBA", "NO", "NO",
     ["Fundar el recurso dentro de los 5 días; si no, se declara desierto",
      "Del memorial se da traslado a la otra parte por el mismo plazo",
      "Controlar la resolución de la Cámara"],
     ["Memorial"]),
    ("SUC_850", "Recursos e incidentes", "Acción de nulidad o impugnación del testamento", "DEMANDADA",
     "Interposición de la demanda de nulidad o impugnación", 0, "SIN_PLAZO", "NO",
     "Arts. 2336, 2339 y 2474 CCyC; art. 741 CPCCBA", "NO", "NO",
     ["La impugnación de la autenticidad o la validez va por proceso contencioso ante el juez del sucesorio "
      "(arts. 2339 y 2336 CCyC)",
      "La falta de formas causa la nulidad total del testamento (art. 2474 CCyC)",
      "Verificar si corresponde mediación previa (duda D04)",
      "Contestar la demanda en el plazo del tipo de proceso: cargarlo como plazo suelto",
      "Si representamos a quien impugna, revisar el rol del expediente (duda D42)"],
     ["Demanda o contestación"]),
    ("SUC_860", "Recursos e incidentes", "Impugnación de la declaratoria o petición de herencia", "DEMANDADA",
     "Interposición de la demanda por quien se pretende heredero", 0, "SIN_PLAZO", "NO",
     "Art. 737 CPCCBA; arts. 2310, 2311 y 2336 CCyC", "NO", "NO",
     ["La declaratoria se dicta sin perjuicio de terceros: el pretendiente puede demandar para excluir a un heredero o "
      "para ser reconocido con él (art. 737 CPCCBA)",
      "La petición de herencia es imprescriptible, salvo la prescripción adquisitiva de cosas singulares "
      "(art. 2311 CCyC)",
      "Tramita ante el juez del sucesorio (art. 2336 CCyC); verificar la mediación previa (duda D04)",
      "Contestar la demanda en el plazo del tipo de proceso: cargarlo como plazo suelto"],
     ["Demanda o contestación"]),
    ("SUC_870", "Recursos e incidentes", "Control de la caducidad de instancia en un incidente con controversia",
     "AMBAS",
     "Última petición, resolución o actuación que impulsó el incidente", 3, "MESES", "NO",
     "Arts. 310, 311 y 313 inc. 2 CPCCBA (plazo de los incidentes a verificar)", "NO", "NO",
     ["El sucesorio no caduca, pero sí los incidentes en los que se suscita controversia (art. 313 inc. 2)",
      "Impulsar el incidente antes del vencimiento; la matriz propone 3 meses, el plazo más corto posible "
      "(duda D36)",
      "El plazo corre también en días inhábiles, salvo las ferias (art. 311): el vencimiento real puede ser posterior",
      "Cada acto de impulso reinicia el plazo: editar la fecha de inicio"],
     []),
    ("SUC_875", "Recursos e incidentes", "Intimación a activar el incidente bajo apercibimiento de caducidad",
     "AMBAS",
     "Notificación de la intimación del art. 315 CPCCBA", 5, "HABILES_JUDICIALES", "SI",
     "Arts. 315 y 316 CPCCBA", "NO", "NO",
     ["Manifestar la intención de continuar y producir actividad útil dentro de los 5 días",
      "Si después pasa igual plazo sin actividad útil, se tiene por decretada la caducidad"],
     ["Escrito activando el incidente"]),
    ("SUC_980", "Cierre", "Entrega de hijuelas y testimonios, y rendición al cliente", "ACTORA",
     "Orden de inscripción dictada", 0, "SIN_PLAZO", "NO",
     "Arts. 2363 y 2403 CCyC", "NO", "NO",
     ["Controlar que cada inscripción quede registrada",
      "Entregar a cada heredero sus testimonios, títulos y constancias",
      "Rendir cuentas al cliente de los gastos y los fondos",
      "Devolver la documentación original"],
     ["Recibo de entrega de la documentación"]),
    ("SUC_990", "Cierre", "Archivo del expediente", "AMBAS",
     "Finalización del sucesorio", 0, "SIN_PLAZO", "NO",
     "Art. 21 Ley 6716", "NO", "SI",
     ["Verificar que no queden tasas, ITGB, honorarios ni aportes pendientes",
      "Pedir el archivo"],
     []),
]

_APERTURA_AB_INTESTATO = "Apertura ab intestato: se ordenan edictos, cédulas y oficios"
_OLOGRAFO = "Se presentó un testamento ológrafo o cerrado"
_ACTO_PUBLICO = "Se presentó o se informó un testamento por acto público"

# origen, condicion, destino ("" = cierra ese camino paralelo)
TRANSICIONES = [
    ("SUC_010", "Consulta tomada: se prepara la sucesión", "SUC_015"),
    ("SUC_010", "Consulta tomada: se prepara la sucesión", "SUC_016"),
    ("SUC_010", "Consulta tomada: se prepara la sucesión", "SUC_020"),
    ("SUC_010", "Consulta tomada: se prepara la sucesión", "SUC_040"),
    ("SUC_010", "Consulta tomada: se prepara la sucesión", "SUC_050"),
    ("SUC_015", "Herencia aceptada, o plazo vencido: quien no aceptó es tenido por renunciante", ""),
    ("SUC_016", "ITGB declarado y pagado antes de los 24 meses", ""),
    ("SUC_016", "Se cumplen 24 meses sin haber pedido la inscripción", "SUC_910"),
    ("SUC_020", "Partidas reunidas", "SUC_030"),
    ("SUC_030", "Juzgado competente definido", "SUC_100"),
    ("SUC_040", "Búsqueda terminada, con o sin testamento", ""),
    ("SUC_050", "Relevamiento terminado", ""),
    ("SUC_100", "Escrito de inicio presentado", "SUC_110"),
    ("SUC_105", "Recaudos cumplidos", "SUC_110"),
    ("SUC_110", _APERTURA_AB_INTESTATO, "SUC_120"),
    ("SUC_110", _APERTURA_AB_INTESTATO, "SUC_130"),
    ("SUC_110", _APERTURA_AB_INTESTATO, "SUC_140"),
    ("SUC_110", _APERTURA_AB_INTESTATO, "SUC_200"),
    ("SUC_110", _OLOGRAFO, "SUC_120"),
    ("SUC_110", _OLOGRAFO, "SUC_130"),
    ("SUC_110", _OLOGRAFO, "SUC_140"),
    ("SUC_110", _OLOGRAFO, "SUC_150"),
    ("SUC_110", _ACTO_PUBLICO, "SUC_120"),
    ("SUC_110", _ACTO_PUBLICO, "SUC_130"),
    ("SUC_110", _ACTO_PUBLICO, "SUC_140"),
    ("SUC_110", _ACTO_PUBLICO, "SUC_160"),
    ("SUC_110", "El juzgado observa recaudos previos", "SUC_105"),
    ("SUC_110", "El juzgado observa recaudos previos", "SUC_800"),
    ("SUC_110", "El juez se declara incompetente", "SUC_112"),
    ("SUC_110", "El juez se declara incompetente", "SUC_810"),
    ("SUC_112", "Causa radicada ante el juez competente", "SUC_110"),
    ("SUC_120", "Informe agregado (si hay otro sucesorio, se pide la acumulación)", ""),
    ("SUC_130", "Informe negativo", ""),
    ("SUC_130", "Informe positivo: testamento ológrafo depositado", "SUC_150"),
    ("SUC_130", "Informe positivo: testamento por acto público", "SUC_160"),
    ("SUC_140", "Dictamen sin observaciones, u observaciones cumplidas", ""),
    ("SUC_150", "Letra y firma reconocidas, y objeciones resueltas", "SUC_160"),
    ("SUC_150", "Se impugna la autenticidad o la validez del testamento", "SUC_850"),
    ("SUC_160", "Testamento protocolizado o testimonio agregado", "SUC_200"),
    ("SUC_160", "Testamento protocolizado o testimonio agregado", "SUC_220"),
    ("SUC_200", "Vencida la citación: sucesión ab intestato, o testamento que no dispone de todos los bienes",
     "SUC_300"),
    ("SUC_200", "Vencida la citación: el testamento instituye herederos por todos los bienes", ""),
    ("SUC_200", "Un heredero citado no acepta ni renuncia: se lo intima", "SUC_230"),
    ("SUC_220", "Vencido el plazo o presentados los instituidos", "SUC_320"),
    ("SUC_220", "Un heredero instituido no acepta ni renuncia: se lo intima", "SUC_230"),
    ("SUC_230", "Acepta o renuncia, o vence sin respuesta y se lo tiene por aceptante", ""),
    ("SUC_230", "Prórroga por justa causa (una sola vez)", "SUC_230"),
    ("SUC_300", "Pedido presentado", "SUC_310"),
    ("SUC_310", "Declaratoria dictada y notificada", "SUC_330"),
    ("SUC_310", "Declaratoria dictada y notificada", "SUC_810"),
    ("SUC_310", "Se difiere la declaratoria por un vínculo no acreditado", "SUC_300"),
    ("SUC_310", "Ningún heredero acredita su título: herencia vacante", "SUC_350"),
    ("SUC_320", "Testamento aprobado y notificado", "SUC_330"),
    ("SUC_320", "Testamento aprobado y notificado", "SUC_810"),
    ("SUC_330", "Herederos capaces y de acuerdo: denuncia de bienes", "SUC_510"),
    ("SUC_330", "Inventario y avalúo judiciales", "SUC_400"),
    ("SUC_330", "Un acreedor o legatario intima a inventariar", "SUC_400"),
    ("SUC_330", "Un acreedor o legatario intima a inventariar", "SUC_505"),
    ("SUC_330", "Continuación extrajudicial (art. 733 CPCCBA)", "SUC_660"),
    ("SUC_330", "Aparece un heredero omitido", "SUC_340"),
    ("SUC_330", "Un tercero impugna la declaratoria o reclama la herencia", "SUC_860"),
    ("SUC_330", "Un interesado impugna el testamento aprobado", "SUC_850"),
    ("SUC_340", "Declaratoria ampliada", "SUC_330"),
    ("SUC_350", "Bienes liquidados y entregados al Estado", "SUC_990"),
    ("SUC_350", "Se presenta quien invoca derecho a la herencia", "SUC_860"),
    ("SUC_400", "Se designan administrador, inventariador y tasador", "SUC_410"),
    ("SUC_400", "Se designan administrador, inventariador y tasador", "SUC_500"),
    ("SUC_400", "Se designan inventariador y tasador, sin administrador", "SUC_500"),
    ("SUC_410", "Cargo aceptado", "SUC_420"),
    ("SUC_410", "Cargo aceptado", "SUC_440"),
    ("SUC_420", "Rendición aprobada sin observaciones", "SUC_420"),
    ("SUC_420", "Rendición observada: se resuelve por incidente", "SUC_420"),
    ("SUC_420", "Rendición observada: se resuelve por incidente", "SUC_870"),
    ("SUC_420", "Cuenta final aprobada: termina la administración", ""),
    ("SUC_440", "Deudas, cargas y legados pagados", ""),
    ("SUC_500", "Inventario y avalúo presentados", "SUC_530"),
    ("SUC_500", "Inventario y avalúo presentados, con bienes gananciales", "SUC_530"),
    ("SUC_500", "Inventario y avalúo presentados, con bienes gananciales", "SUC_520"),
    ("SUC_505", "Inventario hecho, o vencido el plazo (el heredero responde con sus propios bienes)", ""),
    ("SUC_510", "Denuncia presentada", "SUC_530"),
    ("SUC_510", "Denuncia presentada, con bienes gananciales", "SUC_530"),
    ("SUC_510", "Denuncia presentada, con bienes gananciales", "SUC_520"),
    ("SUC_520", "Calificación de los bienes acordada o resuelta", ""),
    ("SUC_530", "Sin oposición, o reclamaciones resueltas", "SUC_540"),
    ("SUC_530", "Hay oposición: incidente o audiencia con el perito (art. 760)", "SUC_530"),
    ("SUC_530", "Hay oposición: incidente o audiencia con el perito (art. 760)", "SUC_870"),
    ("SUC_540", "Inscripción de la declaratoria o del testamento en condominio, sin partición", "SUC_700"),
    ("SUC_540", "Partición privada", "SUC_600"),
    ("SUC_540", "Partición judicial", "SUC_610"),
    ("SUC_540", "Un coheredero reclama colación o reducción", "SUC_650"),
    ("SUC_600", "Partición presentada y aprobada", "SUC_700"),
    ("SUC_600", "No hay acuerdo: partición judicial", "SUC_610"),
    ("SUC_610", "Cuenta particionaria presentada", "SUC_620"),
    ("SUC_610", "El partidor no la presenta en término: remoción y nueva designación", "SUC_610"),
    ("SUC_620", "Cuenta aprobada, con o sin oposición", "SUC_700"),
    ("SUC_620", "Cuenta rechazada", "SUC_610"),
    ("SUC_620", "Cuenta rechazada", "SUC_810"),
    ("SUC_650", "Sentencia firme o acuerdo: se ajusta la masa partible", "SUC_610"),
    ("SUC_660", "Operaciones cumplidas y copias agregadas al expediente", "SUC_700"),
    ("SUC_660", "Desinteligencias entre herederos u organismos: vuelve al juez", "SUC_400"),
    ("SUC_700", "Inscripción pedida", "SUC_740"),
    ("SUC_700", "Inscripción pedida", "SUC_900"),
    ("SUC_700", "Inscripción pedida", "SUC_910"),
    ("SUC_700", "Inscripción pedida", "SUC_920"),
    ("SUC_740", "Orden de inscripción dictada", "SUC_750"),
    ("SUC_740", "Orden de inscripción dictada", "SUC_752"),
    ("SUC_740", "Orden de inscripción dictada", "SUC_754"),
    ("SUC_740", "Orden de inscripción dictada", "SUC_980"),
    ("SUC_740", "Los herederos venden con tracto abreviado", "SUC_756"),
    ("SUC_750", "Inscripción registrada, o no hay inmuebles en PBA", ""),
    ("SUC_750", "Observada por el Registro: subsanar y reingresar", "SUC_750"),
    ("SUC_750", "Hay inmuebles en otra jurisdicción", "SUC_758"),
    ("SUC_752", "Inscripción registrada, o no hay automotores", ""),
    ("SUC_754", "Fondos y participaciones transferidos, o no hay", ""),
    ("SUC_756", "Escritura otorgada e inscripta", "SUC_980"),
    ("SUC_758", "Inscripción registrada en la otra jurisdicción", ""),
    ("SUC_900", "Tasa y contribución pagadas sin observaciones", ""),
    ("SUC_900", "El juzgado observa la liquidación: integrar la diferencia", "SUC_900"),
    ("SUC_910", "Declaración jurada presentada y pagada, o no corresponde", ""),
    ("SUC_910", "ARBA observa: rectificar la declaración jurada", "SUC_910"),
    ("SUC_920", "Regulación notificada", "SUC_925"),
    ("SUC_920", "Regulación notificada", "SUC_930"),
    ("SUC_925", "Regulación firme: no apelada o resuelta por la Cámara", ""),
    ("SUC_930", "Honorarios y aportes pagados", ""),
    ("SUC_800", "Reposición resuelta (o la apelación en subsidio), o plazo vencido sin recurrir", ""),
    ("SUC_810", "No se apela, o se deniega el recurso (queja o queda firme)", ""),
    ("SUC_810", "Apelación concedida en relación", "SUC_815"),
    ("SUC_815", "La Cámara resuelve, o el recurso se declara desierto", ""),
    ("SUC_850", "Sentencia firme: testamento válido y todavía sin protocolizar", "SUC_160"),
    ("SUC_850", "Sentencia firme: testamento válido y ya aprobado", "SUC_330"),
    ("SUC_850", "Sentencia firme: testamento nulo, sigue como sucesión ab intestato", "SUC_200"),
    ("SUC_860", "Sentencia firme: se amplía o modifica la declaratoria", "SUC_340"),
    ("SUC_860", "Demanda rechazada por sentencia firme", "SUC_330"),
    ("SUC_860", "Demanda rechazada en una herencia vacante", "SUC_350"),
    ("SUC_870", "El incidente se resolvió", ""),
    ("SUC_870", "Se pide la caducidad: el juez intima a activar", "SUC_875"),
    ("SUC_875", "Se activa el incidente en término", "SUC_870"),
    ("SUC_875", "No se activa: se decreta la caducidad", ""),
    ("SUC_980", "Inscripciones terminadas y documentación entregada", "SUC_990"),
]

# id, tema, pregunta, nodos
DUDAS = [
    ("D01", "Régimen procesal y vigencia",
     "¿Sigue vigente al 13/11/2026 el CPCCBA (Decreto-Ley 7425/68) sin reformas posteriores que toquen los arts. 724 a "
     "773? La última reforma encontrada es la Ley 15.513 (BO 03/01/2025), que no toca el sucesorio; los textos de "
     "leyes-ar.com usados están actualizados al 16/10/2026. La noticia de noviembre de 2026 sobre un nuevo código "
     "procesal civil es de Santa Fe, no de PBA. Propuesta: la matriz se arma sobre el Decreto-Ley 7425/68. Fuentes: "
     "normas.gba.gob.ar (Leyes 11.511 y 15.513) y leyes-ar.com.", "Todos"),
    ("D02", "Citas normativas",
     "Validar artículo por artículo las citas del CPCCBA, del CCyC, del Código Fiscal y de las Leyes 7205, 6716, "
     "14.967 y 13.951. Las marcadas '(a verificar)' no se pudieron confirmar en una fuente oficial o actualizada.",
     "Todos"),
    ("D03", "Juzgados de Paz Letrados",
     "Según el art. 61 de la Ley 5827 (texto Ley 13.645), los Juzgados de Paz Letrados conocen en sucesiones (ap. II "
     "inc. l), salvo los de los 20 partidos del ap. I (Almirante Brown, Avellaneda, Lanús, Tigre, Vicente López y "
     "otros). ¿Hay opción por el Juzgado Civil y Comercial cuando el peticionante no domicilia en el partido (art. 3 "
     "inc. 6 Ley 9229, citado por la Cámara de Trenque Lauquen el 28/04/2022)? ¿El trámite es el mismo? Propuesta: un "
     "solo flujo para los dos órganos; el tribunal elegido define el régimen. Fuente: normas.gba.gob.ar (Ley 5827).",
     "SUC_030, SUC_100, SUC_112"),
    ("D04", "Mediación previa",
     "La Ley 13.951 (art. 4 inc. 8) excluye de la mediación los 'juicios sucesorios y voluntarios' (verificado en "
     "normas.gba.gob.ar). ¿Las acciones contenciosas conexas (nulidad de testamento, petición de herencia, colación, "
     "reducción, partición contenciosa) necesitan mediación previa? Propuesta: el checklist de esos hitos avisa que "
     "hay que verificarlo.", "SUC_650, SUC_850, SUC_860"),
    ("D05", "Edictos: publicaciones y medio",
     "El CCyC (art. 2340) manda un edicto por un día en el diario de publicaciones oficiales; el CPCCBA (art. 734 inc. "
     "2) manda tres días en el Boletín Judicial y en otro diario del último domicilio, o solo en el Boletín Judicial "
     "si el haber prima facie no supera 900 Jus. ¿Qué se ordena hoy en cada departamento: lo del CCyC, lo del "
     "CPCCBA o una combinación? "
     "¿El diario de publicaciones oficiales es el Boletín Oficial de PBA o el Boletín Judicial? La matriz no depende "
     "de la respuesta: el Día Cero es la última publicación, sea cual sea su número. Fuentes: leyes-ar.com (art. 734) "
     "y blogs.scba.gov.ar.", "SUC_100, SUC_110, SUC_200"),
    ("D06", "Edictos: cómputo",
     "El art. 734 CPCCBA dice 'treinta (30) días corridos' y el art. 2340 CCyC 'treinta días' (art. 6 CCyC: días "
     "continuos, sin excluir inhábiles). ¿El Día Cero es la última publicación o el día siguiente, en que la "
     "resolución se tiene por notificada (art. 147 CPCCBA)? ¿La feria suspende el plazo? Propuesta (la más temprana): "
     "corridos, Día Cero en la última publicación y sin descontar la feria.", "SUC_200"),
    ("D07", "Citación de herederos instituidos",
     "El art. 742 CPCCBA da 30 días para que se presenten los herederos instituidos, los beneficiarios y el albacea, "
     "sin decir si son corridos o hábiles. Si son varios, ¿corre desde la última notificación? Propuesta (la más "
     "temprana): corridos, desde la última notificación personal.", "SUC_220"),
    ("D08", "Testamento ológrafo",
     "El CPCCBA (art. 739) pide dos testigos que reconozcan la letra y la firma; el CCyC (art. 2339) exige pericia "
     "caligráfica. ¿Qué se hace en la práctica: audiencia con testigos, pericia o ambas? ¿La audiencia es "
     "FECHA_FIJADA o depende de la pericia?", "SUC_150, SUC_160"),
    ("D09", "Testamento cerrado",
     "El CCyC solo admite las formas que regula (art. 2473): el ológrafo y el acto público. ¿Un testamento cerrado "
     "solo puede valer si se otorgó antes del 01/08/2015 o en el extranjero (art. 2645 CCyC)? ¿El art. 739 CPCCBA "
     "sigue aplicándose a esos casos?", "SUC_040, SUC_150"),
    ("D10", "Ministerio Público",
     "¿En qué casos interviene en el sucesorio en PBA: la Asesoría de Incapaces siempre que haya menores o personas "
     "con capacidad restringida (art. 103 CCyC), y el agente fiscal en las vacantes o con ausentes? ¿Con qué norma "
     "orgánica (Ley 14.442, a verificar)? El art. 728 inc. 1 CPCCBA dice que cesa con la declaratoria. ¿Hay un plazo "
     "para contestar sus observaciones?", "SUC_140, SUC_350"),
    ("D11", "Intervención de ARBA",
     "El art. 728 inc. 3 CPCCBA da intervención al organismo recaudador por el ITGB. ¿Se le da vista en el "
     "expediente? ¿Puede oponerse a la denuncia de bienes (art. 751) y en qué plazo?", "SUC_510, SUC_910"),
    ("D12", "Registro de Juicios Universales",
     "La Ley 7205 manda comunicar el inicio en 3 días (art. 3) y al Registro, informar en 10 días (art. 4). ¿Esos 10 "
     "días son hábiles judiciales? ¿Se diligencia hoy en forma electrónica? Propuesta: hábiles judiciales, sin "
     "gracia (es un plazo del Registro). Fuente: normas.gba.gob.ar (Ley 7205).", "SUC_120"),
    ("D13", "Declaratoria de herederos",
     "¿Qué requisitos controlan los juzgados antes de dictarla (edictos, cédulas, informes de los registros, "
     "partidas)? ¿Hay un plazo para que el juez la dicte, para alertar demoras?", "SUC_300, SUC_310"),
    ("D14", "Recursos contra la declaratoria",
     "¿La declaratoria y la aprobación del testamento se apelan en 5 días, con concesión en relación y memorial en "
     "otros 5 (arts. 243, 244 y 246 CPCCBA)? ¿Procede la aclaratoria del art. 166 inc. 2 para errores de nombres o "
     "documentos, y suspende el plazo de la apelación?", "SUC_310, SUC_320, SUC_810, SUC_815"),
    ("D15", "Impugnación de la declaratoria",
     "La impugnación del art. 737 CPCCBA y la petición de herencia (art. 2311 CCyC: imprescriptible), ¿tramitan por "
     "juicio ordinario ante el juez del sucesorio? ¿Qué plazo de contestación corresponde cargar?", "SUC_860"),
    ("D16", "Intimación a aceptar o renunciar",
     "El art. 2289 CCyC deja al juez fijar entre 1 y 3 meses. La matriz propone 1 mes (el más temprano). ¿Se computa "
     "de fecha a fecha desde la notificación? ¿Admite gracia?", "SUC_230"),
    ("D17", "Caducidad del derecho de opción",
     "El art. 2288 CCyC fija 10 años desde la apertura de la sucesión (la muerte). Propuesta: sin gracia (es un plazo de "
     "fondo) y con límite a las 24:00 del día del vencimiento, la misma pregunta que la duda D28 de la matriz laboral "
     "hace para la prescripción. "
     "¿Es correcto?", "SUC_015"),
    ("D18", "Acreedores que promueven el sucesorio",
     "El art. 729 CPCCBA permite a los acreedores iniciar el sucesorio pasados 4 meses del fallecimiento (el juez "
     "puede ampliar o reducir el plazo). La norma cita el art. 3314 del Código Civil derogado. ¿Conviene un hito "
     "propio (MESES, 4) o alcanza con el aviso del checklist?", "SUC_010"),
    ("D19", "Rendición de cuentas",
     "Art. 748 CPCCBA y art. 2355 CCyC: trimestral; las parciales quedan 5 días en secretaría y la final 10. ¿Esos "
     "plazos son hábiles judiciales y corren desde la notificación? ¿El trimestre se cuenta desde la aceptación del "
     "cargo o por trimestre calendario?", "SUC_420"),
    ("D20", "Venta de bienes",
     "El CCyC (art. 2353) permite vender con acuerdo unánime o autorización judicial; el CPCCBA (art. 747) limita al "
     "administrador a actos conservatorios. ¿Qué exigen los juzgados en la práctica (tasación, vista al Ministerio "
     "Público, subasta o venta privada)?", "SUC_440"),
    ("D21", "Inventario intimado",
     "El art. 2341 CCyC da 3 meses desde la intimación judicial de acreedores o legatarios, y el art. 2321 inc. a hace "
     "responder al heredero con sus bienes si no cumple. ¿Sin gracia y con límite a las 24:00? ¿El Día Cero es la "
     "notificación de la intimación?", "SUC_505"),
    ("D22", "Denuncia de bienes",
     "¿La denuncia de bienes se pone de manifiesto 5 días, como el inventario y avalúo (art. 759 CPCCBA)? ¿Qué "
     "valuación aceptan los juzgados (fiscal, art. 758)? La matriz la hace pasar por el mismo traslado.",
     "SUC_510, SUC_530"),
    ("D23", "Cónyuge supérstite y gananciales",
     "¿Cómo se trata la indivisión poscomunitaria dentro del sucesorio (art. 481 CCyC): quién califica los bienes, si "
     "hace falta acuerdo expreso con el cónyuge y cómo impacta en la tasa (art. 337 inc. f Código Fiscal) y en los "
     "honorarios (art. 35 Ley 14.967, que incluye los gananciales en la base)?", "SUC_520, SUC_900, SUC_920"),
    ("D24", "Unión convivencial",
     "El conviviente no hereda, pero puede invocar el derecho real de habitación gratuito por hasta 2 años (art. 527 "
     "CCyC). ¿Hace falta un hito propio en la V1? Propuesta: aviso en el checklist y plazo suelto.",
     "SUC_010, SUC_330"),
    ("D25", "Partición",
     "Privada (art. 2369 CCyC y 761 CPCCBA): ¿cómo se instrumenta (escrito con firmas certificadas, escritura) y se "
     "aprueba? Judicial: el traslado de la cuenta particionaria es de 10 días (art. 766), ¿hábiles y con gracia? "
     "Licitación (art. 2372 CCyC: 30 días desde la aprobación de la tasación): ¿conviene un hito propio?",
     "SUC_540, SUC_600, SUC_610, SUC_620"),
    ("D26", "Colación y reducción",
     "¿Qué vía procesal y qué prescripción rigen para la colación (¿el plazo genérico de 5 años del art. 2560 CCyC, "
     "o se reclama dentro de la partición, que es imprescriptible mientras dure la indivisión según el art. 2368?) y "
     "para la reducción (art. 2459 CCyC: no procede contra el donatario que poseyó 10 años)? ¿Se reclama dentro del "
     "sucesorio o en juicio aparte?", "SUC_650"),
    ("D27", "Trámite extrajudicial",
     "¿Se usa el art. 733 CPCCBA en la práctica? ¿Qué organismos intervienen y cómo se acredita su conformidad?",
     "SUC_660"),
    ("D28", "Tasa de justicia",
     "Según el Código Fiscal, se paga al pedir la inscripción (art. 338 inc. c) sobre la valuación vigente a la fecha "
     "del auto que la ordena (art. 332), sin la parte ganancial del cónyuge (art. 337 inc. f); así lo aplicó la Cám. "
     "Civ. y Com. Trenque Lauquen el 11/04/2024. ¿Algún juzgado exige un pago a cuenta al inicio? ¿La alícuota de la "
     "Ley Impositiva 2026 (Ley 15.558) es 22 por mil y se presume un 10% de otros bienes? La contribución para la "
     "Caja de Abogados es del 5% de la tasa en el texto vigente del art. 12 inc. g Ley 6716 (normas.gba.gob.ar); "
     "fuentes anteriores dicen 10%.", "SUC_100, SUC_700, SUC_900"),
    ("D29", "Bono y anticipo previsional",
     "El bono de la Ley 8480 y el jus previsional del art. 13 de la Ley 6716 se pagan al iniciar. ¿Por cada letrado? "
     "¿Cada heredero que se presenta con otro abogado paga los suyos?", "SUC_100"),
    ("D30", "ITGB: plazos",
     "El art. 322 inc. b del Código Fiscal da 15 días desde la solicitud judicial de inscripción, entrega o "
     "libramiento de fondos, o 24 meses desde el fallecimiento, lo que ocurra primero (texto en leyes-ar.com, "
     "actualizado al 16/10/2026). ¿Los 15 días son corridos o hábiles administrativos? ¿Qué escrito cuenta como "
     "'solicitud judicial de inscripción'? Propuesta (la más temprana): corridos, desde el escrito que pide la "
     "inscripción. La Ley 14.044 incorporó el impuesto al Código Fiscal desde el 01/01/2010.", "SUC_016, SUC_700, SUC_910"),
    ("D31", "Honorarios y aportes",
     "Art. 57 Ley 14.967: apelación en 5 días, fundada en el mismo acto. ¿Son hábiles judiciales desde la "
     "notificación por cédula y admiten gracia? Art. 14 Ley 6716: aportes dentro de 60 días corridos de firme la "
     "regulación. ¿Cuándo se pide la regulación en la práctica (al pedir la inscripción o por etapas)?",
     "SUC_920, SUC_925, SUC_930"),
    ("D32", "Inscripción de bienes",
     "¿Qué recaudos exigen hoy el Registro de la Propiedad Inmueble de PBA (testimonio o minuta, tasas, vigencia de "
     "los certificados), el DNRPA (solicitud tipo), los bancos y las sociedades (libro de accionistas, DPPJ)? Ver el "
     "Decreto-Ley 11.643/63 y la Ley 17.801.", "SUC_740, SUC_750, SUC_752, SUC_754"),
    ("D33", "Tracto abreviado",
     "¿Qué inciso del art. 16 de la Ley 17.801 se aplica a la venta por los herederos declarados y qué requisitos "
     "pide el Registro de PBA?", "SUC_756"),
    ("D34", "Bienes en otra jurisdicción",
     "Confirmar la adhesión de PBA y de las jurisdicciones de destino a la Ley 22.172 y los recaudos (letrado "
     "autorizado, tasas y aportes locales). ¿También se paga allí tasa de justicia?", "SUC_200, SUC_758"),
    ("D35", "Causante extranjero o con bienes en el exterior",
     "Arts. 2643 a 2648 CCyC. ¿Conviene un flujo aparte cuando el causante tenía domicilio en el exterior, o alcanza "
     "con el checklist de la competencia? ¿Cómo se acreditan las partidas y los testamentos extranjeros?",
     "SUC_030, SUC_040"),
    ("D36", "Caducidad de instancia",
     "El sucesorio no caduca, salvo que se suscite controversia (art. 313 inc. 2 CPCCBA). ¿Qué plazo rige en los "
     "incidentes: 6 meses (art. 310 inc. 1, primera instancia) o 3 meses? La matriz propone 3, el más temprano. El "
     "art. 311 descuenta las ferias y el tipo MESES del motor no lo hace, así que el aviso queda antes del "
     "vencimiento real.", "SUC_870, SUC_875"),
    ("D37", "Ferias judiciales",
     "La SCBA fija por acordada la feria de enero y dos semanas en invierno. Propuesta: los plazos en días hábiles "
     "judiciales se congelan; los corridos y los de meses y años no se suspenden (art. 6 CCyC); la caducidad sí "
     "descuenta las ferias (art. 311). ¿Es correcto para cada hito? Las reglas R1 a R9 del motor se validan en las "
     "dudas D26 a D34 de la matriz laboral y valen también para este flujo.", "Todos"),
    ("D38", "Plazo de gracia",
     "La matriz aplica la gracia del art. 124 CPCCBA solo a las presentaciones de parte en plazos procesales en días "
     "hábiles judiciales; no a los plazos de fondo del CCyC, del fisco (ITGB, aportes) ni de los organismos. "
     "¿Es correcto?", "SUC_015, SUC_016, SUC_200, SUC_220, SUC_230, SUC_420, SUC_505, SUC_910, SUC_930"),
    ("D39", "Notificaciones electrónicas",
     "Según el reglamento de la SCBA (Acuerdo 4013, texto ordenado por el Acuerdo 4039, art. 13), la notificación "
     "electrónica se perfecciona el martes o viernes siguiente a quedar disponible; la compilación de la SCBA al "
     "02/11/2026 lo mantiene vigente. ¿Qué notificaciones del sucesorio siguen siendo por cédula en papel (herederos "
     "denunciados sin domicilio electrónico, citación de instituidos)? Fuente: digesto.scba.gov.ar y scba.gob.ar.",
     "SUC_200, SUC_220, SUC_530, SUC_620"),
    ("D40", "Reposición y apelación",
     "Confirmar que en el sucesorio rigen la reposición en 3 días (art. 239 CPCCBA), la apelación en 5 (art. 244), "
     "el memorial en 5 (art. 246) y la queja en 5 (art. 275), todos en días hábiles judiciales y con gracia.",
     "SUC_800, SUC_810, SUC_815"),
    ("D41", "Producto: roles del sucesorio",
     "El enum Rol_Responsable (ACTORA, DEMANDADA, TRIBUNAL, AMBAS) se usó así: ACTORA, el heredero que promueve y al "
     "que representamos; DEMANDADA, otros interesados con intereses opuestos; TRIBUNAL, el juzgado o un organismo; "
     "AMBAS, cualquier interesado. ¿Hacen falta roles propios del sucesorio, como INTERESADO u ORGANISMO? Propuesta "
     "para la V1: mantener el enum y aclarar en el nombre del hito.", "Todos"),
    ("D42", "Producto: rol representado",
     "legal_cases.represented_role solo admite ACTORA o DEMANDADA, pero el sucesorio no tiene demandado. Si "
     "representamos a un coheredero que impugna, al cónyuge en la liquidación de gananciales o al heredero intimado "
     "a aceptar, las alertas de 'te toca a vos' quedan invertidas. ¿Se elige DEMANDADA en esos casos, se agrega un "
     "valor nuevo o el rol se define por hito? Solo se registra; no se modifica el contrato de API.",
     "SUC_230, SUC_520, SUC_850, SUC_860"),
    ("D43", "Producto: flujo prejudicial y judicial",
     "La fase Previa (SUC_010 a SUC_050) va al flujo PREJUDICIAL. Pero SUC_015 (10 años) y SUC_016 (24 meses del "
     "ITGB) corren desde la muerte y siguen durante el juicio, y SUC_016 lleva a SUC_910, que es del flujo judicial. "
     "¿Cómo se conservan esos plazos al pasar al flujo judicial? ¿Se admite una transición entre flujos, como en el "
     "laboral?", "SUC_010, SUC_015, SUC_016, SUC_020, SUC_030, SUC_040, SUC_050, SUC_910"),
    ("D44", "Producto: catálogos",
     "El catálogo de regímenes solo tiene PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057; hace falta uno civil (por ejemplo, "
     "PBA_CIV_DL_7425) y el fuero CIVIL_COMERCIAL en legal_branches. Además, courts.court_type (TRIBUNAL_TRABAJO, "
     "JUZGADO_LABORAL, CAMARA_APELACION) no tiene Juzgado Civil y Comercial ni Juzgado de Paz Letrado, y "
     "legal_cases.closed_reason no tiene un motivo para la sucesión terminada por inscripción. Solo se registra; no "
     "se modifican el contrato de API ni el modelo de datos.", "Todos"),
    ("D45", "Producto: caminos que deben esperar a otros",
     "La app abre caminos en paralelo, pero no tiene un hito que espere a que terminen todos. Por ejemplo, la "
     "declaratoria necesita la citación vencida y el informe del Registro de Juicios Universales, y la orden de "
     "inscripción necesita la tasa, el ITGB, los honorarios y los aportes pagados. Propuesta para la V1: lo controla "
     "el checklist; evaluar para la V2 una espera explícita.", "SUC_300, SUC_740"),
]
