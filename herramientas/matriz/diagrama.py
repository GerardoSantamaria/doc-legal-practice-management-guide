import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

from openpyxl import load_workbook

CIERRA = "CIERRA_CAMINO"
GRUPOS = [
    ("Etapa previa", ["Previa"]),
    ("Demanda y contestación", ["Postulación"]),
    ("Prueba y audiencia de vista de causa", ["Prueba", "Vista de causa"]),
    ("Sentencia y recursos", ["Sentencia", "Recursos"]),
    ("Ejecución, acuerdo y cierre", ["Ejecución", "Acuerdo", "Cierre"]),
]
ROL_TEXTO = {"ACTORA": "Actora", "DEMANDADA": "Demandada", "TRIBUNAL": "Tribunal", "AMBAS": "Ambas partes"}
PENDIENTES = {"HABILES_ADMINISTRATIVOS", "ANIOS", "FECHA_FIJADA"}
ESTILOS = [
    "classDef actora fill:#DCE9F9,stroke:#1F4E79,color:#000",
    "classDef demandada fill:#FBE3D6,stroke:#C55A11,color:#000",
    "classDef tribunal fill:#E7E6E6,stroke:#595959,color:#000",
    "classDef ambas fill:#E9DDF5,stroke:#7030A0,color:#000",
    "classDef externo fill:#FFFFFF,stroke:#8C8C8C,color:#404040,stroke-dasharray:4 3",
    "classDef paralelo fill:#FFF2CC,stroke:#BF9000,color:#000",
    "classDef fin fill:#F2F2F2,stroke:#A6A6A6,color:#404040",
]


def leer_hoja(wb, nombre):
    filas = wb[nombre].iter_rows(values_only=True)
    encabezado = next(filas)
    return [dict(zip(encabezado, f)) for f in filas if f[0]]


def texto(valor):
    return str(valor or "").replace('"', "#quot;").strip()


def plazo(nodo):
    tipo, valor = nodo["Plazo_Tipo"], nodo["Plazo_Valor_Default"]
    gracia = " + gracia" if nodo["Aplica_Gracia"] == "SI" else ""
    descripcion = {
        "HABILES_JUDICIALES": f"{valor} días hábiles judiciales{gracia}",
        "CORRIDOS": f"{valor} días corridos{gracia}",
        "HABILES_ADMINISTRATIVOS": f"{valor} días hábiles (LCT) - tipo pendiente",
        "ANIOS": f"{valor} años - tipo pendiente",
        "FECHA_FIJADA": "Fecha fijada por el tribunal - tipo pendiente",
        "SIN_PLAZO": "Sin plazo",
    }
    return descripcion.get(tipo, f"{valor} {tipo}")


def etiqueta(nodo):
    prefijo = "INICIO - " if nodo["Es_Inicial"] == "SI" else ""
    return (f'{prefijo}<b>{nodo["ID_Paso"]}</b> {texto(nodo["Nombre_Hito"])}'
            f'<br/>Responsable: {ROL_TEXTO.get(nodo["Rol_Responsable"], nodo["Rol_Responsable"])}'
            f'<br/>{plazo(nodo)}')


def grupos_de(nodos):
    grupos = OrderedDict((titulo, fases) for titulo, fases in GRUPOS)
    conocidas = {f for fases in grupos.values() for f in fases}
    for fase in dict.fromkeys(n["Fase_Proceso"] for n in nodos):
        if fase not in conocidas:
            grupos[fase] = [fase]
    return grupos


def diagrama_detalle(titulo, fases, nodos, por_id, salidas, grupo_de):
    lineas = ["```mermaid", "flowchart TD"]
    propios = [n for n in nodos if n["Fase_Proceso"] in fases]
    ids_propios = {n["ID_Paso"] for n in propios}
    for fase in fases:
        de_la_fase = [n for n in propios if n["Fase_Proceso"] == fase]
        if not de_la_fase:
            continue
        lineas.append(f'  subgraph F_{fases.index(fase)}["{fase}"]')
        for n in de_la_fase:
            clase = n["Rol_Responsable"].lower()
            lineas.append(f'    {n["ID_Paso"]}["{etiqueta(n)}"]:::{clase}')
        lineas.append("  end")

    externos = set()

    def externo(nid, sufijo):
        clave = f"EXT_{nid}_{sufijo}"
        if clave not in externos:
            externos.add(clave)
            destino = por_id[nid]
            lineas.append(f'  {clave}["{nid} {texto(destino["Nombre_Hito"])}<br/>'
                          f'(ver {grupo_de[destino["Fase_Proceso"]]})"]:::externo')
        return clave

    for origen, condiciones in salidas.items():
        for i, (condicion, destinos) in enumerate(condiciones.items(), start=1):
            if origen in ids_propios:
                destinos_reales = [d for d in destinos if d != CIERRA]
                nodo_salida = origen
                if len(destinos) > 1:
                    fork = f"P_{origen}_{i}"
                    lineas.append(f'  {fork}(["Se abren en paralelo"]):::paralelo')
                    lineas.append(f'  {origen} -->|"{texto(condicion)}"| {fork}')
                    nodo_salida, etiqueta_arista = fork, ""
                else:
                    etiqueta_arista = f'|"{texto(condicion)}"|'
                if CIERRA in destinos:
                    fin = f"FIN_{origen}_{i}"
                    lineas.append(f'  {fin}(["Fin de este camino"]):::fin')
                    lineas.append(f"  {nodo_salida} -->{etiqueta_arista} {fin}")
                for d in destinos_reales:
                    objetivo = d if d in ids_propios else externo(d, "destino")
                    lineas.append(f"  {nodo_salida} -->{etiqueta_arista} {objetivo}")
            else:
                for d in destinos:
                    if d in ids_propios:
                        fuente = externo(origen, "origen")
                        lineas.append(f'  {fuente} -.->|"{texto(condicion)}"| {d}')

    for n in propios:
        if n["Plazo_Tipo"] in PENDIENTES:
            lineas.append(f"  style {n['ID_Paso']} stroke-dasharray:6 4")
        if n["Es_Inicial"] == "SI" or n["Es_Final"] == "SI":
            lineas.append(f"  style {n['ID_Paso']} stroke-width:3px")
    lineas += [f"  {e}" for e in ESTILOS]
    lineas.append("```")
    return "\n".join(lineas)


def diagrama_general(nodos, por_id, salidas, grupos):
    fases = [f for fs in grupos.values() for f in fs if any(n["Fase_Proceso"] == f for n in nodos)]
    ids = {f: f"FASE_{i}" for i, f in enumerate(fases, start=1)}
    lineas = ["```mermaid", "flowchart LR"]
    for f in fases:
        cantidad = sum(1 for n in nodos if n["Fase_Proceso"] == f)
        lineas.append(f'  {ids[f]}["{f}<br/>{cantidad} {"hito" if cantidad == 1 else "hitos"}"]')
    pares = []
    for origen, condiciones in salidas.items():
        for destinos in condiciones.values():
            for d in destinos:
                if d == CIERRA:
                    continue
                a, b = por_id[origen]["Fase_Proceso"], por_id[d]["Fase_Proceso"]
                if a != b and (a, b) not in pares:
                    pares.append((a, b))
    lineas += [f"  {ids[a]} --> {ids[b]}" for a, b in pares]
    lineas.append("```")
    return "\n".join(lineas)


def main():
    excel, salida_detalle, salida_general = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    wb = load_workbook(excel)
    nodos = leer_hoja(wb, "Nodos")
    transiciones = leer_hoja(wb, "Transiciones")
    flujo = {f[0]: f[1] for f in wb["Flujo"].iter_rows(values_only=True) if f[0]}
    por_id = {n["ID_Paso"]: n for n in nodos}

    salidas = defaultdict(lambda: OrderedDict())
    for t in sorted(transiciones, key=lambda t: (t["ID_Paso_Origen"], t["Orden"] or 0)):
        salidas[t["ID_Paso_Origen"]].setdefault(t["Condicion_Salida"], []).append(t["ID_Paso_Destino"])

    grupos = grupos_de(nodos)
    grupo_de = {f: titulo for titulo, fases in grupos.items() for f in fases}
    general = diagrama_general(nodos, por_id, salidas, grupos)

    partes = [
        f"# Diagrama de Flujo: {flujo.get('Flujo', '')}",
        "",
        f"**Régimen:** {flujo.get('Régimen procesal', '')} · **Versión:** {flujo.get('Versión', '')}",
        "",
        f"> Este documento se genera a partir de `{Path(excel).name}`. No se edita a mano: "
        "las correcciones se hacen en la planilla y luego se vuelve a generar el diagrama.",
        "",
        "## Cómo leer los diagramas",
        "",
        "* **Cada caja es un hito** de la hoja `Nodos`: muestra el ID, el nombre, quién debe actuar y el plazo.",
        "* **Cada flecha es un camino** de la hoja `Transiciones`, rotulado con su condición de salida.",
        "* **Color de la caja según el responsable:** celeste = Actora; naranja = Demandada; gris = Tribunal; violeta = Ambas partes.",
        "* **Borde punteado:** el tipo de plazo todavía no está soportado por el motor (días hábiles de la LCT, años, fecha fijada).",
        "* **Borde grueso:** hito inicial o hito final.",
        "* **\"Se abren en paralelo\"** (amarillo): esa condición abre varios hitos a la vez; por ejemplo, la prescripción corre mientras avanza el reclamo.",
        "* **\"Fin de este camino\"** (gris claro): el camino paralelo termina sin abrir otro hito.",
        "* **Cajas blancas con borde discontinuo:** hitos de otra etapa; el texto indica en qué diagrama están. "
        "Las flechas punteadas muestran desde dónde se llega a esta etapa.",
        "",
        "## Vista general por fases",
        "",
        general,
    ]
    for i, (titulo, fases) in enumerate(grupos.items(), start=1):
        if not any(n["Fase_Proceso"] in fases for n in nodos):
            continue
        partes += ["", f"## {i}. {titulo}", "",
                   diagrama_detalle(titulo, fases, nodos, por_id, salidas, grupo_de)]
    salida_detalle.write_text("\n".join(partes) + "\n", encoding="utf-8")
    salida_general.write_text(general + "\n", encoding="utf-8")
    print(f"OK: {salida_detalle} y {salida_general}")


main()
