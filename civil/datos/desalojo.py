from comun import (CON_GRACIA, CON_VALOR_CERO, DUDA_ETAPA_COMUN, DUDA_PRODUCTO, ESTADOS, ROLES, etapa_judicial,
                   flujo, mediacion, ordenar, plazo_tipos)

FLUJO = flujo(
    "Desalojo de inmuebles (falta de pago, vencimiento, intrusión, tenencia precaria o comodato) - Provincia de "
    "Buenos Aires",
    "CPCCBA (Decreto-Ley 7425/68), juicio sumario (arts. 676 a 678 bis); CCyC arts. 1217 a 1225 (texto según DNU "
    "70/2023, a verificar); Ley 13.951 (mediación optativa)",
    "Borrador para validar con el equipo legal. Citas cotejadas al 13/11/2026 con normas.gba.gob.ar y leyes-ar.com; "
    "lo que no se pudo confirmar dice '(a verificar)' y tiene su duda. La etapa judicial sale de civil/datos/comun.py "
    "sin la ejecución dineraria, que se reemplaza por el lanzamiento. El cobro de alquileres va en un juicio "
    "ejecutivo aparte. Las dudas de la etapa común se responden en matriz_civil_danos_y_perjuicios_pba.xlsx y las de "
    "producto en matriz_civil_sucesorio_pba.xlsx.",
)

FASES = ["Previa", "Postulación", "Prueba", "Sentencia", "Recursos", "Lanzamiento", "Acuerdo", "Cierre"]

PLAZO_TIPOS = plazo_tipos({
    "HABILES_JUDICIALES": "En este flujo: toda la etapa judicial (contestación, traslados, prueba, recursos y "
                          "honorarios).",
    "CORRIDOS": "En este flujo: intimación de pago (10 días, art. 1222 CCyC), plazo de la mediación optativa "
                "(30 días) y plazo para desocupar después de la sentencia (no menor a 10 días, art. 1223 CCyC).",
    "MESES": "En este flujo: caducidad de instancia (3 meses en el sumario).",
    "FECHA_FIJADA": "En este flujo: audiencias de mediación, preliminar y de vista de causa, y la diligencia de "
                    "lanzamiento.",
    "ANTICIPACION_HABILES_JUDICIALES": "En este flujo: dictamen pericial 5 días antes de la audiencia de prueba "
                                       "(art. 492 CPCCBA).",
    "SIN_PLAZO": "En este flujo: intimaciones con plazo fijado por el locador o el contrato, actos del juzgado y "
                 "del oficial de justicia, y plazos que fija el juez.",
})

GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Prueba", ["Prueba"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Lanzamiento", ["Lanzamiento"]),
    ("Acuerdo", ["Acuerdo"]),
    ("Cierre", ["Cierre"]),
]

ROL_TEXTO = {"ACTORA": "Locador o propietario", "DEMANDADA": "Locatario u ocupante",
             "TRIBUNAL": "Juzgado u organismo", "AMBAS": "Cualquiera de las partes"}
LEYENDA_ROLES = ("celeste = el locador, propietario o comodante que pide el desalojo (ACTORA); naranja = el "
                 "locatario, sublocatario, intruso, tenedor precario u otro ocupante (DEMANDADA); gris = el juzgado, "
                 "el oficial de justicia, el mediador o un organismo (TRIBUNAL); violeta = cualquiera de las partes "
                 "(AMBAS).")
EJEMPLO_PARALELO = ("el cobro ejecutivo de los alquileres adeudados se inicia mientras corre la intimación de pago "
                    "previa al desalojo")
ROLES_DESCRIPCION = [
    ("ACTORA", "Quien pide el desalojo: locador, propietario, comodante o quien tenga derecho a recibir el inmueble."),
    ("DEMANDADA", "Quien debe restituir el inmueble: locatario, sublocatario, tenedor precario, comodatario, intruso "
                  "u otro ocupante (art. 676 CPCCBA)."),
    ("TRIBUNAL", "El juzgado, la Cámara, la SCBA, el oficial de justicia que cumple el lanzamiento, el mediador o un "
                 "organismo (Ministerio de Infraestructura en el caso del art. 678 bis). La app muestra 'Esperando "
                 "resolución'."),
    ("AMBAS", "Cualquiera de las partes: audiencias, prueba, recursos, honorarios y acuerdos de desocupación."),
]
INSTRUCCIONES_ADICIONALES = [
    ("Particularidades del desalojo", True),
    ("La consulta inicial abre una variante según la causal: falta de pago, vencimiento o resolución del contrato, "
     "intrusión, o tenencia precaria y comodato.", False),
    ("La mediación es optativa para quien pide el desalojo (art. 5 Ley 13.951): se puede demandar directamente.",
     False),
    ("La etapa judicial es la común del fuero civil para el juicio sumario, salvo la ejecución dineraria: la "
     "sentencia se cumple con el plazo para desocupar y el lanzamiento.", False),
    ("Plazos que fija el locador, el contrato o el juez: el hito es SIN_PLAZO y el checklist indica que el abogado "
     "lo carga como plazo suelto.", False),
    ("", False),
]

# id, fase, nombre, rol, evento, valor, tipo, gracia, base, inicial, final, checklist, documentacion
_PREVIA = [
    ("DES_010", "Previa", "Consulta inicial por la recuperación del inmueble", "ACTORA",
     "Fecha de la consulta", 0, "SIN_PLAZO", "NO",
     "Art. 676 CPCCBA; arts. 1217 a 1223 CCyC", "SI", "NO",
     ["Identificar la causal: falta de pago, vencimiento del plazo, resolución por otro incumplimiento (art. 1219), "
      "intrusión, tenencia precaria o comodato",
      "Pedir el título del cliente (escritura, informe de dominio) y el contrato de locación o de comodato, si lo hay",
      "Identificar a todos los ocupantes: locatario, sublocatarios, familiares, intrusos",
      "Destino del inmueble: si es vivienda, la intimación del art. 1222 es obligatoria antes de demandar por falta "
      "de pago",
      "Detectar si viven menores, personas con discapacidad o si el inmueble está en una villa o asentamiento "
      "(art. 678 bis)",
      "Verificar el régimen de locaciones vigente para el contrato (DNU 70/2023, ver duda D01)",
      "Pactar honorarios y firmar el poder"],
     ["Título o informe de dominio", "Contrato de locación o comodato", "Recibos y estado de deuda", "Poder"]),
    ("DES_020", "Previa", "Intimación de pago de alquileres (art. 1222)", "DEMANDADA",
     "Recepción de la intimación por el locatario", 10, "CORRIDOS", "NO",
     "Arts. 1219 inc. c y 1222 CCyC", "NO", "NO",
     ["Intimar por medio fehaciente al pago de lo adeudado, con un plazo no menor a 10 días corridos desde la "
      "recepción y el lugar de pago (art. 1222); si se dio un plazo mayor, editar",
      "La notificación al domicilio denunciado en el contrato vale aunque el locatario se niegue a recibirla "
      "(art. 1222)",
      "La resolución por falta de pago exige dos períodos consecutivos impagos (art. 1219 inc. c)",
      "Intimar también a los fiadores para el cobro (art. 1225)"],
     ["Carta documento con aviso de recibo", "Contrato de locación", "Estado de deuda"]),
    ("DES_030", "Previa", "Intimación fehaciente a restituir el inmueble", "ACTORA",
     "Decisión de pedir la restitución", 0, "SIN_PLAZO", "NO",
     "Arts. 1217, 1218, 1219, 1536 y 1539 CCyC", "NO", "NO",
     ["Vencimiento del contrato: si el locatario sigue ocupando, la locación continúa hasta que una parte la da por "
      "concluida por comunicación fehaciente (art. 1218)",
      "Resolución por cambio de destino, falta de conservación, abandono o causa contractual (art. 1219)",
      "Comodato sin plazo: el comodante puede pedir la restitución en cualquier momento (art. 1536 inc. e); con "
      "plazo, antes solo por necesidad urgente o cambio de destino (art. 1539)",
      "Fijar un plazo para restituir y cargarlo como plazo suelto"],
     ["Carta documento con aviso de recibo"]),
    ("DES_040", "Previa", "Restitución del inmueble por el ocupante", "DEMANDADA",
     "Vencimiento del plazo de la intimación o extinción de la locación", 0, "SIN_PLAZO", "NO",
     "Arts. 1222 y 1223 CCyC", "NO", "NO",
     ["Extinguida la locación, el locatario debe restituir la tenencia (arts. 1222 y 1223)",
      "El locador no puede negarse a recibir las llaves; si lo hace, el locatario puede consignarlas (art. 1222)",
      "Al recibir el inmueble, labrar acta del estado y de los muebles que queden, con reserva por las deudas",
      "Si se acuerda una fecha de desocupación, cargarla como plazo suelto"],
     ["Acta de entrega y de estado del inmueble"]),
    ("DES_050", "Previa", "Constatación de la ocupación del inmueble", "ACTORA",
     "Fecha en que se detectó la ocupación", 0, "SIN_PLAZO", "NO",
     "Art. 676 CPCCBA; art. 181 Código Penal", "NO", "NO",
     ["Constatar la ocupación por acta notarial: quiénes ocupan, desde cuándo y con qué título invocan",
      "Evaluar la denuncia penal por usurpación (art. 181 CP) y el pedido de restitución en sede penal (a verificar "
      "en el CPP PBA)",
      "Si la ocupación es reciente, evaluar las acciones posesorias o el interdicto (a verificar)"],
     ["Acta de constatación", "Título o informe de dominio"]),
    ("DES_055", "Previa", "Denuncia penal por usurpación y restitución en sede penal", "TRIBUNAL",
     "Presentación de la denuncia penal", 0, "SIN_PLAZO", "NO",
     "Art. 181 Código Penal; CPP PBA (restitución provisoria, a verificar)", "NO", "NO",
     ["Seguir la causa y pedir la restitución provisoria del inmueble si procede",
      "La causa penal no impide demandar el desalojo en sede civil"],
     ["Copia de la denuncia"]),
    ("DES_080", "Previa", "Cobro ejecutivo de alquileres adeudados (juicio aparte)", "ACTORA",
     "Decisión de reclamar los alquileres", 0, "SIN_PLAZO", "NO",
     "Arts. 521 inc. 6 y 523 inc. 2 CPCCBA; arts. 1225 y 2562 inc. c CCyC", "NO", "NO",
     ["El crédito por alquileres es título ejecutivo (art. 521 inc. 6)",
      "Preparar la vía: citar al demandado a que reconozca si es locatario y exhiba el último recibo (art. 523 inc. 2)",
      "Demandar también a los fiadores: su obligación cesa al vencer el plazo de la locación, salvo la derivada de "
      "no restituir a tiempo (art. 1225)",
      "Los alquileres prescriben a los 2 años (art. 2562 inc. c)",
      "Se tramita como otro caso en la app"],
     ["Contrato de locación", "Estado de deuda", "Intimaciones"]),
]

_MED_NODOS, _MED_TRANSICIONES = mediacion("DES", ("070", "072", "074", "076"), demanda="DES_300",
                                          acuerdo="DES_800", optativa=True, reanudacion=False)

_EJECUCION = ["DES_700", "DES_705", "DES_710", "DES_720", "DES_730"]

_ETAPA_NODOS, _ETAPA_TRANSICIONES = etapa_judicial(
    "DES", "sumario",
    agregar={
        "DES_300": [
            "El desalojo tramita por juicio sumario, contra locatario, sublocatario, tenedor precario, intruso u otro "
            "ocupante cuya obligación de restituir sea exigible (art. 676)",
            "Se puede demandar antes del vencimiento del contrato (condena de futuro, art. 677)",
            "Acompañar la intimación del art. 1222 si el destino es habitacional y la causal es falta de pago",
            "La mediación es optativa (art. 5 Ley 13.951): si no se hizo, no hace falta acta de cierre"],
        "DES_330": [
            "Pedir que la cédula se diligencie en el inmueble y que se haga saber la demanda a todos los ocupantes "
            "(práctica y artículo aplicable, a verificar: ver duda D06)"],
        "DES_340": [
            "Defensas típicas: pago, consignación de llaves (art. 1222), falta de legitimación o existencia de otro "
            "título para ocupar",
            "Si el demandado se allana y desocupa en la condena de futuro, las costas son del actor (art. 677)"],
        "DES_500": [
            "La sentencia fija el plazo para desocupar, que no puede ser menor a 10 días (art. 1223 CCyC)"],
    },
    quitar=_EJECUCION,
    redirigir={"DES_700": "DES_750", "DES_710": "DES_760"},
)

_PROPIOS = [
    ("DES_325", "Postulación", "Entrega o desocupación inmediata bajo caución real", "ACTORA",
     "Traba de la litis (contestación de la demanda o vencimiento de su plazo)", 0, "SIN_PLAZO", "NO",
     "Arts. 676 bis y 676 ter CPCCBA", "NO", "NO",
     ["Procede contra tenedor precario o intruso (art. 676 bis) y por falta de pago o vencimiento del contrato "
      "(art. 676 ter)",
      "Acreditar la verosimilitud del derecho y el grave perjuicio de esperar la sentencia (art. 676 bis)",
      "Ofrecer caución real por los daños que pueda causar la medida",
      "Si se ocultó la relación locativa o el pago de alquileres, hay multa y daños (art. 676 ter)"],
     ["Escrito de pedido", "Caución real"]),
    ("DES_750", "Lanzamiento", "Plazo para desocupar fijado en la sentencia", "DEMANDADA",
     "Notificación de la sentencia firme (en la condena de futuro, vencimiento del plazo contractual)", 10,
     "CORRIDOS", "NO",
     "Art. 1223 CCyC; art. 677 CPCCBA", "NO", "NO",
     ["El plazo no puede ser menor a 10 días (art. 1223): editar si la sentencia fijó otro",
      "En la condena de futuro, la sentencia se cumple al vencer el plazo convenido (art. 677)",
      "Si el demandado desocupa, recibir las llaves y labrar acta"],
     ["Sentencia firme"]),
    ("DES_760", "Lanzamiento", "Pedido y libramiento del mandamiento de lanzamiento", "ACTORA",
     "Vencimiento del plazo para desocupar sin entrega del inmueble", 0, "SIN_PLAZO", "NO",
     "Arts. 497 y 678 bis CPCCBA", "NO", "NO",
     ["Pedir el mandamiento con facultades para usar la fuerza pública, allanar domicilio y llamar a un cerrajero",
      "Pedir que se inventaríen los muebles que queden y se designe depositario",
      "Si hay menores o personas vulnerables, prever la intervención del Ministerio Público y de los servicios "
      "sociales (a verificar)",
      "Si el inmueble está en una villa o asentamiento, el juez oficia antes al Ministerio de Infraestructura "
      "(art. 678 bis)"],
     ["Mandamiento de lanzamiento"]),
    ("DES_765", "Lanzamiento", "Consulta al Registro de Villas y Asentamientos y audiencia de relocalización",
     "TRIBUNAL",
     "Libramiento del oficio al Ministerio de Infraestructura", 0, "SIN_PLAZO", "NO",
     "Art. 678 bis CPCCBA; arts. 28, 29 y 70 Ley 14.449", "NO", "NO",
     ["Si el asentamiento está registrado, no se ordena el desalojo durante el plazo del art. 70 Ley 14.449 "
      "(duración, a verificar): cargarlo como plazo suelto",
      "Excepción: peligro real e inminente para la seguridad de las personas; el juez cita a una audiencia para un "
      "plan de relocalización con solución habitacional definitiva (art. 678 bis)"],
     ["Respuesta del Ministerio de Infraestructura", "Acta de la audiencia"]),
    ("DES_770", "Lanzamiento", "Diligencia de lanzamiento", "TRIBUNAL",
     "Fecha y hora fijadas por el oficial de justicia", 0, "FECHA_FIJADA", "NO",
     "Art. 497 CPCCBA (a verificar)", "NO", "NO",
     ["Coordinar con el oficial de justicia, la fuerza pública y el cerrajero",
      "Concurrir con el cliente para recibir el inmueble",
      "Si la diligencia se suspende o se reprograma, editar la fecha"],
     ["Mandamiento diligenciado"]),
    ("DES_780", "Lanzamiento", "Toma de posesión, llaves y destino de los muebles", "ACTORA",
     "Entrega del inmueble o cumplimiento del lanzamiento", 0, "SIN_PLAZO", "NO",
     "Arts. 1222 y 1223 CCyC", "NO", "NO",
     ["Labrar acta del estado del inmueble y de los muebles que queden",
      "Retirar o depositar los muebles según lo que ordene el juzgado",
      "Cambiar cerraduras y dar de baja o pasar a nombre del cliente los servicios",
      "Reclamar daños al inmueble y alquileres impagos en el juicio ejecutivo o por separado"],
     ["Acta de toma de posesión"]),
]

NODOS = sorted(_PREVIA + _MED_NODOS + _ETAPA_NODOS + _PROPIOS, key=lambda n: n[0])

_PAGO = "Falta de pago de alquileres"
_RESTITUIR = "Vencimiento o resolución del contrato, tenencia precaria o comodato"
_NO_RESTITUYE_MED = "No paga o no restituye: se pide la mediación optativa"
_NO_RESTITUYE_DEM = "No paga o no restituye: se demanda directamente"

TRANSICIONES = ordenar(NODOS, [
    ("DES_010", _PAGO, "DES_020"),
    ("DES_010", _PAGO, "DES_080"),
    ("DES_010", _RESTITUIR, "DES_030"),
    ("DES_010", "Intrusión u ocupación sin título", "DES_050"),
    ("DES_020", "Paga en el plazo: sigue la locación", "DES_990"),
    ("DES_020", "No paga en el plazo: debe restituir", "DES_040"),
    ("DES_030", "Intimación recibida", "DES_040"),
    ("DES_040", "Restituye el inmueble", "DES_780"),
    ("DES_040", _NO_RESTITUYE_MED, "DES_070"),
    ("DES_040", _NO_RESTITUYE_DEM, "DES_300"),
    ("DES_050", "Ocupación constatada: se demanda el desalojo", "DES_300"),
    ("DES_050", "Ocupación constatada: se demanda y se denuncia la usurpación", "DES_300"),
    ("DES_050", "Ocupación constatada: se demanda y se denuncia la usurpación", "DES_055"),
    ("DES_055", "Causa penal en trámite o terminada (se informa al juez civil)", ""),
    ("DES_055", "Restitución ordenada en sede penal", "DES_780"),
    ("DES_080", "Ejecución iniciada como otro caso", ""),
    *_MED_TRANSICIONES,
    *_ETAPA_TRANSICIONES,
    ("DES_360", "Traslado contestado o plazo vencido, con pedido de desocupación inmediata", "DES_325"),
    ("DES_360", "Traslado contestado o plazo vencido, con pedido de desocupación inmediata", "DES_400"),
    ("DES_325", "Entrega ordenada: se libra el mandamiento", "DES_760"),
    ("DES_325", "Pedido denegado", ""),
    ("DES_325", "Se apela la resolución", "DES_650"),
    ("DES_750", "Desocupa y entrega las llaves", "DES_780"),
    ("DES_750", "No desocupa en el plazo", "DES_760"),
    ("DES_760", "Mandamiento librado y diligencia fijada", "DES_770"),
    ("DES_760", "El inmueble está en una villa o asentamiento (art. 678 bis)", "DES_765"),
    ("DES_765", "No está registrado, o hay peligro inminente y plan de relocalización", "DES_770"),
    ("DES_765", "Está registrado: el desalojo se suspende por el plazo legal", "DES_760"),
    ("DES_770", "Lanzamiento cumplido", "DES_780"),
    ("DES_770", "Diligencia frustrada o suspendida", "DES_760"),
    ("DES_780", "Inmueble recuperado y proceso terminado", "DES_990"),
    ("DES_780", "Inmueble recuperado por desocupación inmediata: sigue el juicio", ""),
])

_PROPIAS = [
    ("Régimen de locaciones",
     "La matriz cita los arts. 1198, 1199, 1221 y 1222 CCyC con el texto que surge de leyes-ar.com, que refleja el "
     "DNU 70/2023 (derogó la Ley 27.551). ¿Sigue vigente el DNU 70/2023 en materia de locaciones al 13/11/2026 y hay "
     "alguna norma posterior? ¿Los contratos firmados bajo la Ley 27.551 siguen regidos por ella (a verificar)?",
     "DES_010, DES_020, DES_030"),
    ("Intimación del art. 1222",
     "La intimación previa es obligatoria solo con destino habitacional y su plazo no puede ser menor a 10 días "
     "corridos desde la recepción. La matriz usa 10 días corridos. ¿Se usa también en los otros destinos por "
     "práctica? ¿Corren durante la feria judicial (son de fondo)?",
     "DES_020"),
    ("Mediación optativa",
     "En desalojo la mediación es optativa para el reclamante (art. 5 Ley 13.951) y dura hasta 30 días corridos "
     "(art. 12). La matriz no suma la reanudación de la prescripción porque el desalojo no se pierde por el paso del "
     "tiempo mientras la obligación de restituir sea exigible. ¿Es correcto?",
     "DES_070, DES_074"),
    ("Desocupación inmediata",
     "La entrega inmediata (art. 676 bis) y la desocupación inmediata (art. 676 ter) se piden después de trabada la "
     "litis y bajo caución real. La matriz las abre desde el traslado de la contestación y el juicio sigue en "
     "paralelo. ¿Se pueden pedir con la demanda? ¿Qué tipo de caución se acepta en la práctica?",
     "DES_325, DES_360"),
    ("Plazo para desocupar",
     "La sentencia fija el plazo para desocupar, no menor a 10 días (art. 1223 CCyC). La matriz usa 10 días corridos "
     "porque es una norma de fondo. ¿Los juzgados lo cuentan en días hábiles? ¿El CPCCBA tiene una norma propia?",
     "DES_750"),
    ("Notificación en el inmueble",
     "En el CPCCN el oficial notificador hace saber la demanda a sublocatarios y ocupantes (art. 684 CPCCN). No "
     "encontramos una norma igual en los arts. 676 a 678 bis CPCCBA. ¿Cómo se notifica a los ocupantes "
     "desconocidos en PBA y qué pasa si la sentencia no los alcanzó?",
     "DES_330"),
    ("Lanzamiento",
     "¿Qué norma del CPCCBA rige el mandamiento de lanzamiento (la matriz cita el art. 497, a verificar)? ¿Hace falta "
     "pedir en forma expresa el allanamiento y la fuerza pública? ¿Qué se hace con los muebles que quedan?",
     "DES_760, DES_770, DES_780"),
    ("Ocupantes vulnerables",
     "Antes de desalojar en una villa o asentamiento, el juez oficia al Ministerio de Infraestructura (art. 678 bis) "
     "y, si está registrado, no puede ordenarlo durante el plazo del art. 70 Ley 14.449. ¿Cuánto dura ese plazo? Con "
     "menores o personas con discapacidad fuera de ese supuesto, ¿qué intervención se exige (Ministerio Público, "
     "servicios sociales)?",
     "DES_760, DES_765"),
    ("Intrusos y sede penal",
     "Frente a un intruso, ¿se recomienda la denuncia por usurpación con pedido de restitución en sede penal (artículo "
     "del CPP PBA, a verificar), las acciones posesorias o directamente el desalojo? La matriz permite combinar "
     "denuncia y desalojo.",
     "DES_050, DES_055"),
    ("Cobro de alquileres",
     "El cobro de alquileres va en un juicio ejecutivo aparte (arts. 521 inc. 6 y 523 inc. 2 CPCCBA), que se cargaría "
     "como otro caso. ¿Conviene una matriz propia de ejecución de alquileres? ¿Se acumula el reclamo contra los "
     "fiadores?",
     "DES_080"),
    ("Comodato y tenencia precaria",
     "La restitución de la cosa dada en comodato tramita por sumario (art. 320 inc. 2 ll) y el desalojo alcanza al "
     "tenedor precario (art. 676). ¿Se usa siempre la vía del desalojo para el comodato de inmuebles?",
     "DES_030, DES_300"),
]

DUDAS = [(f"D{i:02d}", *d)
         for i, d in enumerate(_PROPIAS + [DUDA_PRODUCTO, DUDA_ETAPA_COMUN], start=1)]
