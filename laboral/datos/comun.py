import datos

ROLES = datos.ROLES
PLAZO_TIPOS = datos.PLAZO_TIPOS
CON_VALOR_CERO = datos.CON_VALOR_CERO
CON_GRACIA = datos.CON_GRACIA
ESTADOS = datos.ESTADOS
FASES = datos.FASES

GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Prueba y audiencia de vista de causa", ["Prueba", "Vista de causa"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Ejecución, acuerdo y cierre", ["Ejecución", "Acuerdo", "Cierre"]),
]

DUDA_MATRIZ_GENERAL = (
    "Matriz general",
    "Las reglas del motor (D26 a D34), el régimen procesal (D01, D24 y D25) y las dudas de la etapa judicial (D07 a D23) "
    "se responden una sola vez en matriz_flujo_laboral_pba_ley_11653.xlsx y valen para esta matriz. "
    "¿Esta matriz reemplaza a la general para este tipo de reclamo cuando se firme, o conviven?",
    "Todos",
)

CAMPOS = {"nombre": 2, "rol": 3, "evento": 4, "valor": 5, "tipo": 6, "gracia": 7, "base": 8,
          "checklist": 11, "documentacion": 12}


def flujo(nombre, notas):
    return {
        "Flujo": nombre,
        "Jurisdicción": "PBA",
        "Fuero": "Laboral",
        "Régimen procesal": "Ley 11.653 (Tribunales de Trabajo, instancia única)",
        "Versión": "1 (borrador)",
        "Fecha del borrador": "13/11/2026",
        "Validado por (equipo legal)": "",
        "Fecha de validación": "",
        "Notas": notas,
    }


def etapa_judicial(prefijo, ajustes):
    """Juicio ordinario de la Ley 11.653 (demanda, prueba, sentencia, recursos, ejecución y acuerdo), tomado de datos.py
    con los IDs del flujo. `ajustes` reemplaza campos por ID, por ejemplo {"DSP_050": {"checklist": [...]}}."""
    judiciales = {n[0] for n in datos.NODOS if n[1] != "Previa"}

    def renombrar(nid):
        return nid.replace("LAB", prefijo, 1) if nid else ""

    nodos = []
    for n in datos.NODOS:
        if n[0] not in judiciales:
            continue
        nodo = list(n)
        nodo[0] = renombrar(n[0])
        for campo, valor in ajustes.get(nodo[0], {}).items():
            nodo[CAMPOS[campo]] = valor
        nodos.append(tuple(nodo))
    transiciones = [(renombrar(o), c, renombrar(d)) for o, c, d in datos.TRANSICIONES if o in judiciales]
    return nodos, transiciones
