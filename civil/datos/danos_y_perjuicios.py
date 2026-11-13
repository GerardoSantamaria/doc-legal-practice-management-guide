from comun import (CON_GRACIA, CON_VALOR_CERO, DUDA_MOTOR, DUDA_PRODUCTO, ESTADOS, FASES_COMUNES, GRUPOS, ROLES,
                   dudas_etapa_comun, etapa_judicial, flujo, mediacion, ordenar, plazo_tipos)

FLUJO = flujo(
    "Daños y perjuicios (tránsito, mala praxis, contractual y daños a bienes) - Provincia de Buenos Aires",
    "CPCCBA (Decreto-Ley 7425/68), juicio sumario (art. 320 inc. 2 k); CCyC arts. 1708 a 1780; Ley 17.418 "
    "(art. 118); Ley 13.951 (mediación)",
    "Borrador para validar con el equipo legal. Citas cotejadas al 13/11/2026 con normas.gba.gob.ar, leyes-ar.com y "
    "argentina.gob.ar; lo que no se pudo confirmar dice '(a verificar)' y tiene su duda. La etapa judicial sale de "
    "civil/datos/comun.py y sus dudas (tema 'Etapa común') se responden solo en esta matriz. Las dudas de producto "
    "del fuero civil están en matriz_civil_sucesorio_pba.xlsx.",
)

FASES = FASES_COMUNES

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": "En este flujo: toda la etapa judicial (contestación, citación en garantía, traslados, "
                          "prueba, recursos, liquidación y honorarios).",
    "CORRIDOS": "En este flujo: respuesta de la aseguradora al reclamo (30 días, a verificar), plazo de la mediación "
                "y reanudación de la prescripción después de la mediación (20 días, art. 2542 CCyC).",
    "MESES": "En este flujo: suspensión de la prescripción por interpelación (6 meses, art. 2541 CCyC) y caducidad "
             "de instancia (3 meses en el sumario).",
    "ANIOS": "En este flujo: prescripción de la acción (3 años, art. 2561 CCyC).",
    "HORAS": "En este flujo: entrega de la copia de la historia clínica (48 horas, art. 14 Ley 26.529).",
    "FECHA_FIJADA": "En este flujo: audiencias de mediación, preliminar y de vista de causa.",
    "ANTICIPACION_HABILES_JUDICIALES": "En este flujo: dictamen pericial 5 días antes de la audiencia de prueba "
                                       "(art. 492 CPCCBA).",
    "SIN_PLAZO": "En este flujo: relevamiento del caso, causa penal, actos del juzgado y plazos que fija la carta "
                 "documento o el juez.",
})

ROL_TEXTO = {"ACTORA": "Damnificado", "DEMANDADA": "Responsable o aseguradora",
             "TRIBUNAL": "Juzgado u organismo", "AMBAS": "Cualquiera de las partes"}
LEYENDA_ROLES = ("celeste = el damnificado que reclama (ACTORA); naranja = el responsable del daño o su aseguradora, "
                 "también la citada en garantía (DEMANDADA); gris = el juzgado, el mediador o un organismo "
                 "(TRIBUNAL); violeta = cualquiera de las partes (AMBAS).")
EJEMPLO_PARALELO = "la prescripción de 3 años sigue corriendo mientras se reclama a la aseguradora"
ROLES_DESCRIPCION = [
    ("ACTORA", "El damnificado que reclama la indemnización: la víctima, sus herederos o quien sufrió el daño en sus "
               "bienes."),
    ("DEMANDADA", "El responsable del daño (conductor, dueño o guardián, profesional, establecimiento de salud, "
                  "contratante incumplidor) y su aseguradora, también cuando está citada en garantía."),
    ("TRIBUNAL", "El juzgado, la Cámara, la SCBA, el mediador o un organismo (fiscalía penal, establecimiento que "
                 "custodia la historia clínica cuando el juez lo intima). El nombre del hito dice cuál. La app muestra "
                 "'Esperando resolución'."),
    ("AMBAS", "Cualquiera de las partes: audiencias, prueba, recursos, honorarios y acuerdos."),
]
INSTRUCCIONES_ADICIONALES = [
    ("Particularidades de daños y perjuicios", True),
    ("La consulta inicial abre una variante: tránsito, mala praxis, incumplimiento contractual o daños a bienes. "
     "Todas confluyen en la mediación y en la etapa judicial común.", False),
    ("La etapa judicial (hitos DYP_300 en adelante) es la común del fuero civil para el juicio sumario. Sus dudas se "
     "responden en esta matriz (tema 'Etapa común').", False),
    ("Plazos que fija la carta documento o el juez: el hito es SIN_PLAZO y el checklist indica que el abogado lo carga "
     "como plazo suelto.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
_PREVIA = [
    ("DYP_010", "Previa", "Consulta inicial por el daño sufrido", "ACTORA",
     "Fecha del hecho dañoso", 0, "SIN_PLAZO", "NO",
     "Arts. 1716, 1737 a 1740 CCyC", "SI", "NO",
     ["Registrar fecha, lugar y circunstancias del hecho, y la fecha en que se conoció el daño",
      "Identificar al damnificado: víctima directa, herederos o damnificados indirectos (art. 1741)",
      "Identificar a los posibles responsables y a sus aseguradoras",
      "Encuadrar el caso: tránsito, mala praxis médica, incumplimiento contractual o daño a un inmueble u otro bien",
      "Si el responsable es el Estado provincial o un municipio (por ejemplo, un hospital público), el reclamo va al "
      "fuero contencioso administrativo y no sigue este flujo",
      "Relevar los rubros: lesiones, gastos, ingresos perdidos, daños materiales, consecuencias no patrimoniales",
      "Pactar honorarios y firmar el poder o acta poder"],
     ["DNI", "Constancias médicas", "Fotos y presupuestos", "Poder o acta poder"]),
    ("DYP_015", "Previa", "Control de prescripción de la acción", "ACTORA",
     "Fecha del hecho dañoso o en que el daño se manifestó (ver duda D02)", 3, "ANIOS", "NO",
     "Arts. 2554 y 2561 CCyC", "NO", "NO",
     ["La acción por daños prescribe a los 3 años (art. 2561); los daños del contrato de transporte de personas o "
      "cosas, a los 2 años (art. 2562 inc. d): editar si es el caso",
      "Se suspende por una sola vez y hasta 6 meses con la interpelación fehaciente (art. 2541) y durante la "
      "mediación (art. 2542): sumar ese tiempo y editar el vencimiento",
      "Se interrumpe con la demanda, aunque sea ante juez incompetente (art. 2546), y con el reconocimiento del "
      "deudor (art. 2545)",
      "Demandar antes del vencimiento"],
     ["Constancia de la fecha del hecho"]),
    ("DYP_017", "Previa", "Suspensión de la prescripción por la interpelación fehaciente", "ACTORA",
     "Recepción de la carta documento por el responsable", 6, "MESES", "NO",
     "Art. 2541 CCyC", "NO", "NO",
     ["La suspensión opera una sola vez y dura 6 meses (art. 2541)",
      "Sumar el período de suspensión al vencimiento de la prescripción (hito DYP_015)",
      "Si hay mediación, su suspensión es aparte (art. 2542)"],
     ["Carta documento con aviso de recibo"]),
    ("DYP_020", "Previa", "Relevamiento del siniestro de tránsito", "ACTORA",
     "Fecha del siniestro", 0, "SIN_PLAZO", "NO",
     "Arts. 1757, 1758 y 1769 CCyC; Ley 17.418", "NO", "NO",
     ["Pedir la denuncia policial o la exposición, y las actuaciones penales si las hay",
      "Identificar vehículos, titulares (informe de dominio del DNRPA), conductores y aseguradoras",
      "Responden el dueño y el guardián de la cosa riesgosa (art. 1758) y el conductor",
      "Reunir fotos, testigos, cámaras, presupuestos de reparación y constancias de atención médica",
      "Si el cliente es asegurado, denunciar el siniestro a su propia aseguradora dentro de los 3 días (art. 46 "
      "Ley 17.418)",
      "Si el siniestro es con transporte público, controlar la franquicia del seguro del transportista (ver duda D09)"],
     ["Denuncia policial", "Informe de dominio", "Datos de las pólizas", "Fotos y presupuestos"]),
    ("DYP_024", "Previa", "Respuesta de la aseguradora del responsable al reclamo", "DEMANDADA",
     "Presentación del reclamo del tercero con la documentación completa", 30, "CORRIDOS", "NO",
     "Art. 56 Ley 17.418 (plazo previsto para el asegurado; para el tercero damnificado, a verificar)", "NO", "NO",
     ["Presentar el reclamo con la documentación y pedir el número de siniestro",
      "Guardar la constancia de presentación: es el disparador del plazo",
      "Evaluar la oferta con el cliente: rubros, montos y forma de pago",
      "Si hay menores o personas con capacidad restringida, el acuerdo necesita aprobación judicial (a verificar)"],
     ["Reclamo presentado", "Constancia de recepción", "Oferta de la aseguradora"]),
    ("DYP_030", "Previa", "Seguimiento de la causa penal", "TRIBUNAL",
     "Inicio de la investigación penal (lesiones u homicidio culposo)", 0, "SIN_PLAZO", "NO",
     "Arts. 1774 a 1777 y 1780 CCyC", "NO", "NO",
     ["Evaluar presentarse como particular damnificado en la causa penal (a verificar en el CPP PBA)",
      "Pedir copias de las pericias accidentológicas, médicas y de la autopsia",
      "Si la causa penal sigue abierta, el juez civil no dicta sentencia hasta que termine, salvo las excepciones "
      "del art. 1775 (extinción de la acción penal, dilación que frustra la indemnización o factor objetivo)",
      "La condena penal hace cosa juzgada en el civil sobre el hecho y la culpa (art. 1776)"],
     ["Copias de la causa penal"]),
    ("DYP_042", "Previa", "Entrega de la copia de la historia clínica", "DEMANDADA",
     "Recepción del pedido de historia clínica por el establecimiento o el profesional", 48, "HORAS", "NO",
     "Arts. 14, 19 y 20 Ley 26.529", "NO", "NO",
     ["Pedir por escrito copia autenticada de la historia clínica completa (art. 14), con estudios y consentimientos",
      "Pueden pedirla el paciente, su representante y, con su autorización, el cónyuge, el conviviente o los "
      "herederos forzosos (art. 19)",
      "Ante la negativa, la demora o el silencio, procede el habeas data (art. 20) o la prueba anticipada"],
     ["Pedido de historia clínica con constancia de recepción", "Copia de la historia clínica"]),
    ("DYP_044", "Previa", "Evaluación médico-legal del caso de mala praxis", "ACTORA",
     "Recepción de la historia clínica", 0, "SIN_PLAZO", "NO",
     "Arts. 1753 y 1768 CCyC; arts. 5 a 7 Ley 26.529", "NO", "NO",
     ["Consultar a un médico de parte sobre la relación entre la atención y el daño",
      "El profesional responde por culpa (obligación de medios, art. 1768); el establecimiento, la obra social o la "
      "prepaga, por los profesionales que actúan para ellos (art. 1753)",
      "Controlar el consentimiento informado: escrito en internación, cirugía y procedimientos invasivos (art. 7 "
      "Ley 26.529)",
      "Identificar a la aseguradora del profesional y del establecimiento para citarlas en garantía"],
     ["Historia clínica", "Informe del médico de parte"]),
    ("DYP_046", "Previa", "Prueba anticipada: secuestro de la historia clínica, pericia o reconocimiento", "ACTORA",
     "Presentación del pedido de prueba anticipada", 0, "SIN_PLAZO", "NO",
     "Arts. 326 y 327 CPCCBA", "NO", "NO",
     ["Justificar el riesgo de que la prueba se pierda o se vuelva muy difícil (art. 326)",
      "Indicar el nombre y el domicilio de la futura contraria (art. 327)",
      "La resolución solo es apelable si deniega la diligencia (art. 327)",
      "El plazo de producción lo fija el juzgado: cargarlo como plazo suelto"],
     ["Escrito de prueba anticipada"]),
    ("DYP_050", "Previa", "Análisis del contrato y del incumplimiento", "ACTORA",
     "Fecha del incumplimiento", 0, "SIN_PLAZO", "NO",
     "Arts. 1716, 1728, 1738 y 1747 CCyC; Ley 24.240", "NO", "NO",
     ["Identificar la obligación incumplida, la mora y los daños previsibles al contratar (art. 1728)",
      "Revisar cláusula penal y cláusulas de limitación de responsabilidad",
      "Si es una relación de consumo, rige la Ley 24.240: proceso más abreviado y beneficio de gratuidad (art. 53)",
      "Si el cliente quiere resolver el contrato o exigir el cumplimiento, ver la matriz de contratos",
      "Proceso: por incumplimiento contractual es sumario hasta 4.500 Jus (art. 320 inc. 1 CPCCBA) y ordinario por "
      "encima (ver duda D01)"],
     ["Contrato", "Comprobantes de pago", "Comunicaciones entre las partes"]),
    ("DYP_060", "Previa", "Constatación del daño al inmueble o a otros bienes", "ACTORA",
     "Fecha en que se detectó el daño", 0, "SIN_PLAZO", "NO",
     "Arts. 1711, 1757 y 1973 CCyC; art. 326 CPCCBA", "NO", "NO",
     ["Constatar el daño por acta notarial, fotos y presupuestos",
      "Identificar el origen (filtraciones, obras vecinas, ruina, incendio) y al responsable",
      "Si el daño sigue produciéndose, evaluar la acción preventiva (art. 1711) o una medida cautelar",
      "Si el estado del bien puede cambiar, pedir prueba anticipada (art. 326 inc. 2)"],
     ["Acta de constatación", "Fotos", "Presupuestos"]),
    ("DYP_070", "Previa", "Respuesta del responsable a la carta documento", "DEMANDADA",
     "Recepción de la carta documento por el responsable", 0, "SIN_PLAZO", "NO",
     "Arts. 886 y 2541 CCyC", "NO", "NO",
     ["Enviar carta documento al responsable (y a su aseguradora, si se conoce) reclamando la indemnización",
      "Fijar un plazo para responder y cargarlo como plazo suelto",
      "La carta documento recibida suspende la prescripción (art. 2541): abrir el hito DYP_017"],
     ["Carta documento con aviso de recibo", "Respuesta del responsable"]),
    ("DYP_090", "Previa", "Convenio extrajudicial y cobro", "AMBAS",
     "Firma del convenio extrajudicial", 0, "SIN_PLAZO", "NO",
     "Arts. 1641 y siguientes CCyC", "NO", "NO",
     ["Revisar el convenio: monto, rubros, plazo de pago, renuncia de acciones, honorarios y gastos",
      "Si el damnificado es menor o tiene capacidad restringida, pedir la aprobación judicial (a verificar)",
      "Cargar como plazos sueltos las cuotas o el plazo de pago pactado"],
     ["Convenio firmado", "Comprobante de pago"]),
]

_MED_NODOS, _MED_TRANSICIONES = mediacion("DYP", ("080", "082", "084", "086"), demanda="DYP_300",
                                          acuerdo="DYP_800")

_ETAPA_NODOS, _ETAPA_TRANSICIONES = etapa_judicial(
    "DYP", "sumario",
    agregar={
        "DYP_300": [
            "Proceso: sumario si el daño deriva de un delito o cuasidelito, cualquiera sea el monto (art. 320 inc. 2 k); "
            "por incumplimiento contractual, sumario hasta 4.500 Jus (art. 320 inc. 1) y ordinario por encima",
            "Rubros: incapacidad física y psíquica (art. 1746 CCyC), consecuencias no patrimoniales (art. 1741), "
            "gastos médicos, de farmacia y de traslado (se presumen, art. 1746), lucro cesante y pérdida de chance "
            "(art. 1738), daño emergente, privación de uso y desvalorización del vehículo",
            "Demandar a todos los responsables: conductor, dueño y guardián (art. 1758), principal (art. 1753), "
            "profesional y establecimiento de salud",
            "Pedir la citación en garantía de la aseguradora (art. 118 Ley 17.418): se puede hasta la apertura a "
            "prueba, y la demanda va ante el juez del lugar del hecho o del domicilio de la aseguradora",
            "La demanda interrumpe la prescripción (art. 2546 CCyC)"],
        "DYP_340": [
            "La demandada puede citar en garantía a su propia aseguradora en el mismo plazo (art. 118 Ley 17.418)",
            "Defensas típicas: hecho del damnificado o de un tercero, caso fortuito (arts. 1729 a 1731 CCyC)"],
        "DYP_420": [
            "Pericias típicas: médica (incapacidad), psicológica, accidentológica o mecánica y contable (lucro cesante)",
            "En mala praxis, la pericia médica es la prueba central: proponer puntos de pericia con el médico de parte"],
        "DYP_500": [
            "Controlar que la condena alcance a la aseguradora citada en la medida del seguro (art. 118 Ley 17.418)",
            "Controlar los intereses desde cada perjuicio (art. 1748 CCyC) y la tasa que fija la sentencia"],
        "DYP_800": [
            "Si el damnificado es menor o tiene capacidad restringida, interviene el Ministerio Público y el acuerdo "
            "necesita aprobación judicial (a verificar)"],
    },
)

_PROPIOS = [
    ("DYP_345", "Postulación", "Contestación de la citación en garantía por la aseguradora", "DEMANDADA",
     "Notificación de la citación en garantía", 10, "HABILES_JUDICIALES", "SI",
     "Art. 118 Ley 17.418; arts. 94 y 484 CPCCBA (plazo igual al de la contestación, a verificar)", "NO", "NO",
     ["La aseguradora puede aceptar la cobertura o declinarla por causas anteriores al siniestro (art. 118)",
      "Si declina la cobertura, responder en el traslado y ofrecer prueba sobre la póliza",
      "Pedir copia certificada de la póliza: límite de cobertura y franquicia"],
     ["Póliza", "Escrito de contestación"]),
    ("DYP_495", "Sentencia", "Suspensión del dictado de la sentencia por la causa penal", "TRIBUNAL",
     "Pase de los autos para sentencia con causa penal en trámite", 0, "SIN_PLAZO", "NO",
     "Arts. 1775 a 1777 CCyC", "NO", "NO",
     ["Informar al juzgado el estado de la causa penal",
      "Pedir que se dicte sentencia si se da una excepción del art. 1775: extinción de la acción penal, dilación que "
      "frustra la indemnización o responsabilidad objetiva (por ejemplo, riesgo de la cosa en un choque)",
      "Controlar periódicamente la causa penal"],
     ["Copia de la resolución penal"]),
    ("DYP_725", "Ejecución", "Pago de la aseguradora citada: límite de cobertura y franquicia", "DEMANDADA",
     "Notificación de la intimación de pago de la liquidación aprobada", 0, "SIN_PLAZO", "NO",
     "Art. 118 Ley 17.418", "NO", "NO",
     ["La sentencia es ejecutable contra la aseguradora en la medida del seguro (art. 118)",
      "Controlar el límite de cobertura y la franquicia de la póliza (ver duda D09)",
      "El plazo de pago lo fija la sentencia o la intimación: cargarlo como plazo suelto",
      "Si queda un saldo, se ejecuta al asegurado y a los demás condenados",
      "Si la aseguradora está en liquidación, verificar el crédito ante el liquidador (a verificar)"],
     ["Póliza", "Liquidación aprobada", "Comprobante de depósito"]),
]

NODOS = sorted(_PREVIA + _MED_NODOS + _ETAPA_NODOS + _PROPIOS, key=lambda n: n[0])

TRANSICIONES = ordenar(NODOS, [
    ("DYP_010", "Accidente de tránsito", "DYP_015"),
    ("DYP_010", "Accidente de tránsito", "DYP_020"),
    ("DYP_010", "Mala praxis médica", "DYP_015"),
    ("DYP_010", "Mala praxis médica", "DYP_042"),
    ("DYP_010", "Daño por incumplimiento contractual", "DYP_015"),
    ("DYP_010", "Daño por incumplimiento contractual", "DYP_050"),
    ("DYP_010", "Daño a un inmueble o a otros bienes", "DYP_015"),
    ("DYP_010", "Daño a un inmueble o a otros bienes", "DYP_060"),
    ("DYP_015", "Demanda presentada antes del vencimiento, o reclamo abandonado", ""),
    ("DYP_017", "Suspensión agotada o demanda presentada", ""),
    ("DYP_020", "Hay lesiones o muerte: se sigue la causa penal", "DYP_024"),
    ("DYP_020", "Hay lesiones o muerte: se sigue la causa penal", "DYP_030"),
    ("DYP_020", "Solo daños materiales: se reclama a la aseguradora", "DYP_024"),
    ("DYP_020", "El responsable no tiene seguro: se lo intima", "DYP_070"),
    ("DYP_024", "Oferta aceptada", "DYP_090"),
    ("DYP_024", "Rechazo, silencio u oferta insuficiente", "DYP_080"),
    ("DYP_030", "Causa penal concluida, archivada o en trámite (se informa al juez civil)", ""),
    ("DYP_042", "Historia clínica entregada", "DYP_044"),
    ("DYP_042", "No entregada o incompleta", "DYP_046"),
    ("DYP_044", "Caso viable: se intima al responsable", "DYP_070"),
    ("DYP_044", "Caso no viable: se informa al cliente", "DYP_990"),
    ("DYP_046", "Historia clínica obtenida", "DYP_044"),
    ("DYP_046", "Pericia o reconocimiento judicial producido", "DYP_070"),
    ("DYP_050", "Incumplimiento y daños identificados: se intima", "DYP_070"),
    ("DYP_060", "Daño constatado: se intima al responsable", "DYP_070"),
    ("DYP_060", "Hace falta prueba anticipada", "DYP_046"),
    ("DYP_070", "Acuerdo extrajudicial", "DYP_090"),
    ("DYP_070", "Rechazo o silencio: se pide la mediación", "DYP_017"),
    ("DYP_070", "Rechazo o silencio: se pide la mediación", "DYP_080"),
    ("DYP_090", "Convenio cumplido", "DYP_990"),
    ("DYP_090", "Convenio incumplido", "DYP_080"),
    *_MED_TRANSICIONES,
    *_ETAPA_TRANSICIONES,
    ("DYP_330", "Se ordena el traslado de la demanda y la citación en garantía", "DYP_340"),
    ("DYP_330", "Se ordena el traslado de la demanda y la citación en garantía", "DYP_345"),
    ("DYP_345", "Contesta aceptando o declinando la cobertura, o vence el plazo", ""),
    ("DYP_450", "Alegatos presentados o plazo vencido, con causa penal en trámite", "DYP_495"),
    ("DYP_495", "Causa penal concluida o se aplica una excepción del art. 1775", "DYP_500"),
    ("DYP_705", "Liquidación aprobada: se intima el pago a la demandada y a la aseguradora citada", "DYP_725"),
    ("DYP_725", "La aseguradora paga todo", "DYP_730"),
    ("DYP_725", "Paga hasta el límite o la franquicia, o no paga: se ejecuta el saldo", "DYP_710"),
    ("DYP_725", "Paga hasta el límite o la franquicia, o no paga: se ejecuta el saldo", "DYP_730"),
])

_PROPIAS = [
    ("Tipo de proceso",
     "La matriz usa el juicio sumario: los daños por delitos y cuasidelitos tramitan así cualquiera sea el monto "
     "(art. 320 inc. 2 k CPCCBA). Los daños por incumplimiento contractual son sumario hasta 4.500 Jus (art. 320 "
     "inc. 1) y ordinario por encima. ¿La mala praxis de un establecimiento privado (responsabilidad contractual con "
     "el paciente) se trata como cuasidelito? ¿Hace falta una versión ordinaria de esta matriz para los contractuales "
     "de monto alto?",
     "DYP_050, DYP_300, DYP_340"),
    ("Prescripción",
     "La matriz usa 3 años (art. 2561 CCyC) para todas las variantes, desde el hecho o desde que el daño se "
     "manifestó (art. 2554: desde que es exigible). ¿Es correcto para el incumplimiento contractual o rige el plazo "
     "general de 5 años (art. 2560)? En mala praxis, ¿desde cuándo se cuenta si el daño aparece después?",
     "DYP_015"),
    ("Suspensión por interpelación",
     "La interpelación fehaciente suspende la prescripción una sola vez y hasta 6 meses (art. 2541). La matriz abre "
     "un hito de alerta de 6 meses, pero el vencimiento de DYP_015 no se corre solo: el abogado lo edita. ¿Alcanza "
     "o la app debería recalcularlo?",
     "DYP_015, DYP_017"),
    ("Reclamo a la aseguradora",
     "El plazo de 30 días para que la aseguradora se pronuncie (art. 56 Ley 17.418) está previsto para el asegurado. "
     "¿Hay un plazo para responder al tercero damnificado (normativa de la Superintendencia de Seguros, a verificar)? "
     "Si no lo hay, ¿el hito pasa a SIN_PLAZO?",
     "DYP_024"),
    ("Historia clínica",
     "La copia se entrega dentro de las 48 horas de pedida (art. 14 Ley 26.529). El tipo HORAS cuenta horas corridas, "
     "incluidos fines de semana. ¿Es el criterio correcto?",
     "DYP_042"),
    ("Mediación",
     "La mediación prejudicial es obligatoria para los reclamos de daños (Ley 13.951), salvo, entre otras, las "
     "acciones de menores con intervención del Ministerio Público (art. 4). ¿Se requiere también a la aseguradora? "
     "¿Qué reglamentación vigente fija el pago inicial y el formulario (a verificar)?",
     "DYP_080, DYP_082, DYP_084"),
    ("Citación en garantía",
     "El damnificado puede citar a la aseguradora hasta que la causa se abre a prueba (art. 118 Ley 17.418). La matriz "
     "lo deja en el checklist de la demanda y da a la aseguradora el mismo plazo que a la demandada (10 días en el "
     "sumario). ¿Es ese el plazo? ¿Conviene un hito con vencimiento en la apertura a prueba?",
     "DYP_300, DYP_345, DYP_400"),
    ("Causa penal",
     "El juez civil no dicta sentencia mientras la causa penal sigue abierta, salvo las excepciones del art. 1775 "
     "CCyC; en los choques suele aplicarse la del factor objetivo (riesgo de la cosa). La matriz pone la suspensión "
     "como un hito antes de la sentencia. ¿Es el lugar correcto o se plantea antes?",
     "DYP_030, DYP_495"),
    ("Límite de cobertura y franquicia",
     "La sentencia se ejecuta contra la aseguradora en la medida del seguro (art. 118 Ley 17.418). ¿Qué criterio "
     "sigue hoy la SCBA sobre la oponibilidad del límite de cobertura y la franquicia del transporte público al "
     "damnificado (a verificar)? ¿Hace falta un hito propio para el reclamo del saldo?",
     "DYP_020, DYP_725"),
    ("Acuerdos con incapaces",
     "Si el damnificado es menor de edad o tiene capacidad restringida, el acuerdo extrajudicial o judicial necesita "
     "intervención del Ministerio Público y aprobación del juez (a verificar). ¿El convenio extrajudicial debe pasar "
     "por la homologación (DYP_800) en ese caso?",
     "DYP_024, DYP_090, DYP_800"),
    ("Estado como responsable",
     "Si el responsable es el Estado provincial o un municipio (hospital público, calle en mal estado), el reclamo "
     "va al fuero contencioso administrativo. La matriz solo lo advierte en la consulta. ¿Hace falta otro flujo?",
     "DYP_010"),
    ("Relación de consumo",
     "En los reclamos de consumo rige el proceso más abreviado de la jurisdicción (art. 53 Ley 24.240), que en PBA "
     "podría ser el sumarísimo (art. 496), y el beneficio de gratuidad. ¿Qué proceso se usa y cómo se carga la "
     "gratuidad frente a la tasa de justicia?",
     "DYP_050, DYP_300"),
    ("Prueba anticipada",
     "La prueba anticipada (arts. 326 y 327 CPCCBA) no tiene plazo legal: el juzgado fija la producción. La matriz la "
     "deja SIN_PLAZO. ¿Es correcto? ¿Se usa también el habeas data del art. 20 Ley 26.529 para la historia clínica?",
     "DYP_046"),
    ("Daños a bienes",
     "Cuando el daño sigue produciéndose (filtraciones, obras vecinas), se puede pedir la acción preventiva "
     "(art. 1711 CCyC) o una cautelar. La matriz no tiene un hito propio. ¿Hace falta?",
     "DYP_060, DYP_320"),
]

DUDAS = [(f"D{i:02d}", *d)
         for i, d in enumerate(_PROPIAS + dudas_etapa_comun("DYP") + [DUDA_PRODUCTO, DUDA_MOTOR], start=1)]
