import sys
from collections import defaultdict, deque

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

from cargar_datos import cargar, prefijo

CIERRA = "CIERRA_CAMINO"
SALIDA_XLSX = sys.argv[1]
SALIDA_MD = sys.argv[2]
_datos = cargar(sys.argv[3] if len(sys.argv) > 3 else None)
CON_GRACIA, CON_VALOR_CERO, DUDAS, ESTADOS = _datos.CON_GRACIA, _datos.CON_VALOR_CERO, _datos.DUDAS, _datos.ESTADOS
FASES, FLUJO, NODOS, PLAZO_TIPOS = _datos.FASES, _datos.FLUJO, _datos.NODOS, _datos.PLAZO_TIPOS
ROLES, TRANSICIONES = _datos.ROLES, _datos.TRANSICIONES
PREFIJO = prefijo(NODOS)
EJEMPLO_PARALELO = getattr(_datos, "EJEMPLO_PARALELO", "la prescripción corre en paralelo con el reclamo")
INSTRUCCIONES_ADICIONALES = getattr(_datos, "INSTRUCCIONES_ADICIONALES", [])
ROLES_DESCRIPCION = getattr(_datos, "ROLES_DESCRIPCION", [
    ("ACTORA", "Debe actuar la parte actora."),
    ("DEMANDADA", "Debe actuar la parte demandada."),
    ("TRIBUNAL", "Depende del tribunal (la app muestra 'Esperando resolución')."),
    ("AMBAS", "Puede o debe actuar cualquiera de las partes (recursos, impugnaciones, audiencias)."),
])


def validar():
    ids = [n[0] for n in NODOS]
    assert len(ids) == len(set(ids)), "IDs duplicados"
    por_id = {n[0]: n for n in NODOS}
    iniciales = [n[0] for n in NODOS if n[9] == "SI"]
    assert len(iniciales) == 1, f"Debe haber un nodo inicial: {iniciales}"
    salidas = defaultdict(list)
    for o, c, d in TRANSICIONES:
        assert o in por_id, f"Origen inexistente {o}"
        assert d == "" or d in por_id, f"Destino inexistente {d}"
        salidas[o].append(d)
    tipos = {t for t, _ in PLAZO_TIPOS}
    for n in NODOS:
        nid, fase, _, rol, _, valor, tipo, gracia, _, _, final = n[:11]
        assert fase in FASES and rol in ROLES and tipo in tipos, nid
        if final == "SI":
            assert not salidas[nid], f"Final con salidas {nid}"
        else:
            assert salidas[nid], f"Sin salidas {nid}"
        if tipo in CON_VALOR_CERO:
            assert valor == 0, nid
        else:
            assert valor > 0, nid
        assert gracia == "NO" or tipo in CON_GRACIA, nid
    vistos, cola = {iniciales[0]}, deque(iniciales)
    while cola:
        for d in salidas[cola.popleft()]:
            if d and d not in vistos:
                vistos.add(d)
                cola.append(d)
    inalcanzables = set(ids) - vistos
    assert not inalcanzables, f"Inalcanzables {inalcanzables}"


HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(bold=True, color="FFFFFF")
CTRL_FILL = PatternFill("solid", fgColor="D9D9D9")
ERROR_FILL = PatternFill("solid", fgColor="F8CBAD")
OK_FILL = PatternFill("solid", fgColor="C6EFCE")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def encabezado(ws, columnas, anchos, control_desde=None):
    for i, (titulo, ancho) in enumerate(zip(columnas, anchos), start=1):
        c = ws.cell(row=1, column=i, value=titulo)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BORDER
        ws.column_dimensions[c.column_letter].width = ancho
    if control_desde:
        for i in range(control_desde, len(columnas) + 1):
            ws.cell(row=1, column=i).fill = PatternFill("solid", fgColor="595959")
    ws.freeze_panes = "B2"
    ws.row_dimensions[1].height = 32


def lista(ws, rango, origen):
    dv = DataValidation(type="list", formula1=origen, allow_blank=True,
                        showErrorMessage=True, errorTitle="Valor no permitido",
                        error="Elegí un valor de la lista (hoja Valores).")
    ws.add_data_validation(dv)
    dv.add(rango)


def hoja_instrucciones(wb):
    ws = wb.active
    ws.title = "Instrucciones"
    ws.column_dimensions["A"].width = 120
    lineas = [
        ("Matriz de flujo procesal — Instrucciones para el equipo legal", True),
        ("", False),
        ("Para qué sirve", True),
        ("Esta planilla es la fuente que se importa a la app. Cada fila de 'Nodos' es un hito del proceso; cada fila de 'Transiciones' es un camino posible entre hitos.", False),
        ("Es un borrador para validar: revisá cada fila, marcá Estado_Validacion (PENDIENTE, VALIDADO o CORREGIR) y escribí tus observaciones en la columna de comentarios.", False),
        ("", False),
        ("Hojas", True),
        ("Flujo: datos generales (régimen, versión, quién valida).", False),
        (f"Nodos: un hito por fila. El ID es único (ej. {PREFIJO}_050). Se numera de 10 en 10 para poder intercalar hitos (ej. {PREFIJO}_015).", False),
        ("Transiciones: un camino por fila. Si un hito tiene 3 salidas posibles, ocupa 3 filas con el mismo origen y distinta condición.", False),
        ("Dudas_a_validar: preguntas abiertas que hay que responder para cerrar la matriz.", False),
        ("Valores: listas de valores permitidos (no modificar sin avisar al equipo técnico).", False),
        ("", False),
        ("Reglas de carga", True),
        ("1. Plazo_Tipo SIN_PLAZO: el valor del plazo es 0 y Aplica_Gracia es NO (etapas que dependen del tribunal).", False),
        ("2. Plazo_Tipo FECHA_FIJADA (audiencias): el valor es 0; el abogado carga la fecha y hora del acto en cada expediente.", False),
        ("3. Aplica_Gracia = SI solo en HABILES_JUDICIALES, CORRIDOS, MESES y ANIOS. La hoja Valores explica cada tipo de plazo.", False),
        ("4. Checklist_Abogado y Documentacion_Requerida: separar cada ítem con punto y coma ( ; ).", False),
        (f"5. Caminos en paralelo: si la misma condición de salida aparece en varias filas con distinto destino, se abren todos esos hitos a la vez (ej. {EJEMPLO_PARALELO}).", False),
        ("6. Destino CIERRA_CAMINO: la fila cierra ese camino paralelo sin abrir otro hito. El destino nunca queda vacío.", False),
        ("7. Día Cero: el plazo empieza a correr el día hábil siguiente al Evento_Disparador.", False),
        ("8. Un solo nodo con Es_Inicial = SI. Los nodos con Es_Final = SI no tienen transiciones de salida.", False),
        ("", False),
        *INSTRUCCIONES_ADICIONALES,
        ("Columnas de control (encabezado gris oscuro)", True),
        ("Se calculan solas y marcan en rojo los errores: IDs duplicados, hitos sin salida o sin entrada, destinos inexistentes y plazos incoherentes. No hay que editarlas.", False),
        ("Las columnas Estado_Validacion y Comentarios no se importan a la app.", False),
    ]
    for i, (texto, negrita) in enumerate(lineas, start=1):
        c = ws.cell(row=i, column=1, value=texto)
        c.font = Font(bold=negrita, size=14 if i == 1 else 11)
        c.alignment = Alignment(wrap_text=True)


def hoja_flujo(wb):
    ws = wb.create_sheet("Flujo")
    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 90
    for i, (k, v) in enumerate(FLUJO.items(), start=1):
        ws.cell(row=i, column=1, value=k).font = Font(bold=True)
        c = ws.cell(row=i, column=2, value=v)
        c.alignment = WRAP
    fila = len(FLUJO) + 2
    ws.cell(row=fila, column=1, value="Control: nodos iniciales").font = Font(bold=True)
    c = ws.cell(row=fila, column=2, value='=IF(COUNTIF(Nodos!J:J,"SI")=1,"OK","Debe haber exactamente un nodo inicial")')
    ws.conditional_formatting.add(f"B{fila}", FormulaRule(formula=[f'B{fila}<>"OK"'], fill=ERROR_FILL))
    ws.cell(row=fila + 1, column=1, value="Control: filas pendientes").font = Font(bold=True)
    ws.cell(row=fila + 1, column=2,
            value='=COUNTIF(Nodos!N:N,"PENDIENTE")+COUNTIF(Nodos!N:N,"CORREGIR")+COUNTIF(Transiciones!E:E,"PENDIENTE")+COUNTIF(Transiciones!E:E,"CORREGIR")')


def hoja_valores(wb):
    ws = wb.create_sheet("Valores")
    columnas = ["Fase_Proceso", "Rol_Responsable", "Plazo_Tipo", "SI_NO", "Estado_Validacion", "", "Plazo_Tipo", "Descripción"]
    encabezado(ws, columnas, [18, 18, 26, 8, 20, 3, 26, 80])
    ws.freeze_panes = None
    ws.cell(row=1, column=6).fill = PatternFill(fill_type=None)
    for col, valores in enumerate([FASES, ROLES, [t for t, _ in PLAZO_TIPOS], ["SI", "NO"], ESTADOS], start=1):
        for i, v in enumerate(valores, start=2):
            ws.cell(row=i, column=col, value=v)
    for i, (t, d) in enumerate(PLAZO_TIPOS, start=2):
        ws.cell(row=i, column=7, value=t)
        c = ws.cell(row=i, column=8, value=d)
        c.alignment = WRAP
    base = len(PLAZO_TIPOS) + 4
    ws.cell(row=base, column=7, value="Rol_Responsable").font = Font(bold=True)
    for i, (r, d) in enumerate(ROLES_DESCRIPCION, start=base + 1):
        ws.cell(row=i, column=7, value=r)
        ws.cell(row=i, column=8, value=d).alignment = WRAP


def hoja_nodos(wb):
    ws = wb.create_sheet("Nodos")
    columnas = ["ID_Paso", "Fase_Proceso", "Nombre_Hito", "Rol_Responsable", "Evento_Disparador",
                "Plazo_Valor_Default", "Plazo_Tipo", "Aplica_Gracia", "Base_Normativa", "Es_Inicial", "Es_Final",
                "Checklist_Abogado", "Documentacion_Requerida", "Estado_Validacion", "Comentarios_Equipo_Legal",
                "Control"]
    encabezado(ws, columnas, [11, 14, 34, 14, 36, 10, 24, 9, 32, 8, 8, 60, 50, 14, 40, 22], control_desde=16)
    for r, n in enumerate(NODOS, start=2):
        valores = list(n[:11]) + ["; ".join(n[11]), "; ".join(n[12]), "PENDIENTE", ""]
        for col, v in enumerate(valores, start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.alignment = WRAP
            c.border = BORDER
        cero = ",".join(f'G{r}="{t}"' for t in CON_VALOR_CERO)
        con_gracia = ",".join(f'G{r}="{t}"' for t in CON_GRACIA)
        ws.cell(row=r, column=16, value=(
            f'=IF(A{r}="","",'
            f'IF(COUNTIF($A:$A,A{r})>1,"ID duplicado",'
            f'IF(AND(K{r}="NO",COUNTIF(Transiciones!$A:$A,A{r})=0),"Sin salidas",'
            f'IF(AND(K{r}="SI",COUNTIF(Transiciones!$A:$A,A{r})>0),"Final con salidas",'
            f'IF(AND(J{r}="NO",COUNTIF(Transiciones!$C:$C,A{r})=0),"Sin entradas",'
            f'IF(AND(OR({cero}),F{r}<>0),"El plazo debe ser 0",'
            f'IF(AND(H{r}="SI",NOT(OR({con_gracia}))),"Este tipo no lleva gracia",'
            f'IF(AND(NOT(OR({cero})),F{r}=0),"Plazo 0: usar SIN_PLAZO",'
            f'"OK"))))))))'
        )).fill = CTRL_FILL
    ultima = 500
    lista(ws, f"B2:B{ultima}", f"Valores!$A$2:$A${len(FASES) + 1}")
    lista(ws, f"D2:D{ultima}", f"Valores!$B$2:$B${len(ROLES) + 1}")
    lista(ws, f"G2:G{ultima}", f"Valores!$C$2:$C${len(PLAZO_TIPOS) + 1}")
    lista(ws, f"H2:H{ultima}", "Valores!$D$2:$D$3")
    lista(ws, f"J2:K{ultima}", "Valores!$D$2:$D$3")
    lista(ws, f"N2:N{ultima}", f"Valores!$E$2:$E${len(ESTADOS) + 1}")
    entero = DataValidation(type="whole", operator="between", formula1="0", formula2="365",
                            showErrorMessage=True, error="Entero entre 0 y 365.")
    ws.add_data_validation(entero)
    entero.add(f"F2:F{ultima}")
    ws.conditional_formatting.add(f"P2:P{ultima}", FormulaRule(formula=['AND(P2<>"",P2<>"OK")'], fill=ERROR_FILL))
    ws.conditional_formatting.add(f"N2:N{ultima}", FormulaRule(formula=['N2="VALIDADO"'], fill=OK_FILL))
    ws.conditional_formatting.add(f"N2:N{ultima}", FormulaRule(formula=['N2="CORREGIR"'], fill=ERROR_FILL))
    ws.auto_filter.ref = f"A1:P{len(NODOS) + 1}"


def hoja_transiciones(wb):
    ws = wb.create_sheet("Transiciones")
    columnas = ["ID_Paso_Origen", "Condicion_Salida", "ID_Paso_Destino", "Orden",
                "Estado_Validacion", "Comentarios_Equipo_Legal", "Nombre_Origen", "Nombre_Destino", "Control"]
    encabezado(ws, columnas, [14, 50, 14, 8, 14, 40, 34, 34, 20], control_desde=7)
    orden = defaultdict(int)
    ultimo_par = {}
    for r, (o, cond, d) in enumerate(TRANSICIONES, start=2):
        if ultimo_par.get(o) != cond:
            orden[o] += 1
            ultimo_par[o] = cond
        for col, v in enumerate([o, cond, d or CIERRA, orden[o], "PENDIENTE", ""], start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.alignment = WRAP
            c.border = BORDER
        ws.cell(row=r, column=7, value=f'=IFERROR(VLOOKUP(A{r},Nodos!$A:$C,3,FALSE),"")').fill = CTRL_FILL
        ws.cell(row=r, column=8,
                value=f'=IF(C{r}="{CIERRA}","(cierra este camino)",IFERROR(VLOOKUP(C{r},Nodos!$A:$C,3,FALSE),""))').fill = CTRL_FILL
        ws.cell(row=r, column=9, value=(
            f'=IF(A{r}="","",'
            f'IF(COUNTIF(Nodos!$A:$A,A{r})=0,"Origen inexistente",'
            f'IF(B{r}="","Falta la condición",'
            f'IF(C{r}="","Falta el destino",'
            f'IF(C{r}="{CIERRA}","OK",'
            f'IF(COUNTIF(Nodos!$A:$A,C{r})=0,"Destino inexistente","OK"))))))'
        )).fill = CTRL_FILL
    ultima = 1000
    lista(ws, f"E2:E{ultima}", f"Valores!$E$2:$E${len(ESTADOS) + 1}")
    ws.conditional_formatting.add(f"I2:I{ultima}", FormulaRule(formula=['AND(I2<>"",I2<>"OK")'], fill=ERROR_FILL))
    ws.conditional_formatting.add(f"E2:E{ultima}", FormulaRule(formula=['E2="VALIDADO"'], fill=OK_FILL))
    ws.conditional_formatting.add(f"E2:E{ultima}", FormulaRule(formula=['E2="CORREGIR"'], fill=ERROR_FILL))
    ws.auto_filter.ref = f"A1:I{len(TRANSICIONES) + 1}"


def hoja_dudas(wb):
    ws = wb.create_sheet("Dudas_a_validar")
    columnas = ["ID", "Tema", "Pregunta", "Nodos_Afectados", "Respuesta_Equipo_Legal", "Estado"]
    encabezado(ws, columnas, [6, 24, 80, 22, 60, 14])
    for r, (i, tema, preg, nodos) in enumerate(DUDAS, start=2):
        for col, v in enumerate([i, tema, preg, nodos, "", "PENDIENTE"], start=1):
            c = ws.cell(row=r, column=col, value=v)
            c.alignment = WRAP
            c.border = BORDER
    lista(ws, "F2:F200", f"Valores!$E$2:$E${len(ESTADOS) + 1}")
    ws.conditional_formatting.add("F2:F200", FormulaRule(formula=['F2="VALIDADO"'], fill=OK_FILL))


def markdown():
    nombres = {n[0]: n[2] for n in NODOS}
    filas = ["| ID_Paso | Fase_Proceso | Nombre_Hito | Rol_Responsable | Evento_Disparador | Plazo_Valor_Default | "
             "Plazo_Tipo | Aplica_Gracia | Base_Normativa | Es_Inicial | Es_Final | Checklist_Abogado | Documentacion_Requerida |",
             "| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |"]
    for n in NODOS:
        celdas = list(n[:11]) + ["; ".join(n[11]) or "—", "; ".join(n[12]) or "—"]
        celdas[0] = f"**{celdas[0]}**"
        filas.append("| " + " | ".join(str(c) for c in celdas) + " |")
    trans = ["| ID_Paso_Origen | Condicion_Salida | ID_Paso_Destino |", "| ----- | ----- | ----- |"]
    for o, c, d in TRANSICIONES:
        destino = f"**{d}** ({nombres[d]})" if d else f"`{CIERRA}`"
        trans.append(f"| **{o}** | {c} | {destino} |")
    dudas = ["| ID | Tema | Pregunta | Nodos |", "| ----- | ----- | ----- | ----- |"]
    for i, t, p, ns in DUDAS:
        dudas.append(f"| {i} | {t} | {p} | {ns} |")
    with open(SALIDA_MD, "w", encoding="utf-8") as f:
        f.write("<!-- NODOS -->\n" + "\n".join(filas) + "\n\n<!-- TRANSICIONES -->\n" + "\n".join(trans)
                + "\n\n<!-- DUDAS -->\n" + "\n".join(dudas) + "\n")


validar()
wb = Workbook()
hoja_instrucciones(wb)
hoja_flujo(wb)
hoja_nodos(wb)
hoja_transiciones(wb)
hoja_dudas(wb)
hoja_valores(wb)
wb.save(SALIDA_XLSX)
markdown()
print(f"OK: {len(NODOS)} nodos, {len(TRANSICIONES)} transiciones, {len(DUDAS)} dudas")
