"""Implementación de referencia del motor de plazos.

Reproduce los casos de prueba de la sección 5 de
logica_matematica_calculadora_de_dias_habiles_judiciales.md y falla si alguno
no da el resultado esperado. Uso: python motor_plazos_referencia.py
"""
import calendar
import datetime as d
from zoneinfo import ZoneInfo

ZONA = ZoneInfo("America/Argentina/Buenos_Aires")
HORA_CIERRE = d.time(14, 0)
HORA_FIN_GRACIA = d.time(12, 0)
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
CON_GRACIA = {"HABILES_JUDICIALES", "CORRIDOS", "MESES", "ANIOS"}
CON_PRORROGA = {"HABILES_JUDICIALES", "HABILES_ADMINISTRATIVOS", "CORRIDOS"}


class CalendarioNoCargado(Exception):
    pass


def D(texto):
    return d.date.fromisoformat(texto)


def rango(desde, hasta):
    a, b = D(desde), D(hasta)
    return {a + d.timedelta(i) for i in range((b - a).days + 1)}


def es_inhabil(fecha, inhabiles, cubierto_hasta):
    if fecha > cubierto_hasta:
        raise CalendarioNoCargado(fecha)
    return fecha.weekday() >= 5 or fecha in inhabiles


def siguiente_habil(fecha, inhabiles, cubierto_hasta):
    fecha += d.timedelta(1)
    while es_inhabil(fecha, inhabiles, cubierto_hasta):
        fecha += d.timedelta(1)
    return fecha


def anterior_habil(fecha, inhabiles, cubierto_hasta):
    fecha -= d.timedelta(1)
    while es_inhabil(fecha, inhabiles, cubierto_hasta):
        fecha -= d.timedelta(1)
    return fecha


def contar_habiles(desde, total, inhabiles, cubierto_hasta):
    fecha, contados = desde, 0
    while contados < total:
        fecha += d.timedelta(1)
        if not es_inhabil(fecha, inhabiles, cubierto_hasta):
            contados += 1
    return fecha


def sumar_meses(fecha, meses):
    indice = fecha.month - 1 + meses
    anio, mes = fecha.year + indice // 12, indice % 12 + 1
    return d.date(anio, mes, min(fecha.day, calendar.monthrange(anio, mes)[1]))


def limite(dia, tipo_limite):
    if tipo_limite == "FIN_DEL_DIA":
        return d.datetime.combine(dia + d.timedelta(1), d.time(0, 0), ZONA)
    return d.datetime.combine(dia, HORA_CIERRE, ZONA)


def calcular(tipo, inicio, valor, inhabiles=frozenset(), inhabiles_admin=frozenset(), gracia=False,
             prorroga=0, cubierto_hasta="2025-12-31", tipo_limite="CIERRE_HORARIO_JUDICIAL",
             estado_calendario="OFICIAL"):
    hasta = D(cubierto_hasta)
    if prorroga and tipo not in CON_PRORROGA:
        raise ValueError("la prórroga solo aplica a plazos en días")
    if gracia and tipo not in CON_GRACIA:
        raise ValueError(f"{tipo} no admite plazo de gracia")
    total = valor + prorroga
    if tipo == "SIN_PLAZO" or (tipo != "FECHA_FIJADA" and total == 0):
        return {"estado": "SIN_VENCIMIENTO"}

    r = {"estado": "CALCULADO", "calendario_provisorio": estado_calendario == "PROVISORIO",
         "calendario_incompleto": False, "advertencias": [], "limite_con_gracia": None}
    try:
        if tipo in ("HORAS", "FECHA_FIJADA"):
            instante = d.datetime.fromisoformat(inicio).replace(tzinfo=ZONA)
            if tipo == "HORAS":
                instante += d.timedelta(hours=total)
            r.update(nominal=instante.date(), efectivo=instante.date(), limite_ordinario=instante)
            if tipo == "FECHA_FIJADA" and es_inhabil(instante.date(), inhabiles, hasta):
                r["advertencias"].append("FECHA_EN_DIA_INHABIL")
            return r

        if tipo == "ANTICIPACION_HABILES_JUDICIALES":
            ultimo_libre = anterior_habil(D(inicio), inhabiles, hasta)
            for _ in range(total - 1):
                ultimo_libre = anterior_habil(ultimo_libre, inhabiles, hasta)
            dia = anterior_habil(ultimo_libre, inhabiles, hasta)
            r.update(nominal=dia, efectivo=dia, limite_ordinario=limite(dia, tipo_limite))
            return r

        if tipo == "HABILES_JUDICIALES":
            nominal = efectivo = contar_habiles(D(inicio), total, inhabiles, hasta)
        elif tipo == "HABILES_ADMINISTRATIVOS":
            nominal = efectivo = contar_habiles(D(inicio), total, inhabiles_admin, hasta)
        elif tipo in ("MESES", "ANIOS"):
            nominal = sumar_meses(D(inicio), total * (12 if tipo == "ANIOS" else 1))
            if nominal > hasta:
                r.update(nominal=nominal, efectivo=nominal, limite_ordinario=limite(nominal, tipo_limite),
                         calendario_incompleto=True)
                return r
            efectivo = siguiente_habil(nominal, inhabiles, hasta) if es_inhabil(nominal, inhabiles, hasta) else nominal
        else:
            nominal = D(inicio) + d.timedelta(total)
            efectivo = siguiente_habil(nominal, inhabiles, hasta) if es_inhabil(nominal, inhabiles, hasta) else nominal

        r.update(nominal=nominal, efectivo=efectivo, limite_ordinario=limite(efectivo, tipo_limite))
        if gracia:
            dia_gracia = siguiente_habil(efectivo, inhabiles, hasta)
            r["limite_con_gracia"] = d.datetime.combine(dia_gracia, HORA_FIN_GRACIA, ZONA)
        return r
    except CalendarioNoCargado:
        return {"estado": "CALENDARIO_NO_CARGADO"}


def fmt(instante):
    return f"{DIAS[instante.weekday()]} {instante:%d/%m/%Y %H:%M}"


JUNIO = {D("2024-06-17"), D("2024-06-20"), D("2024-06-21")}
SEMANA_SANTA = {D("2024-03-24"), D("2024-03-28"), D("2024-03-29"), D("2024-04-02")}
FERIA_INVIERNO = rango("2024-07-15", "2024-07-26")
FIN_DE_ANIO = {D("2024-12-25")} | rango("2025-01-01", "2025-01-31")
HJ = "HABILES_JUDICIALES"


def caso(tipo, inicio, valor, **kw):
    return dict(tipo=tipo, inicio=inicio, valor=valor, **kw)


# caso, argumentos, esperado: estado, o dict con los campos a comprobar
CASOS = [
    ("1", caso(HJ, "2024-06-03", 10, gracia=True), dict(nominal="2024-06-17", limite="2024-06-17 14:00", gracia="2024-06-18")),
    ("2", caso(HJ, "2024-06-03", 10, inhabiles=JUNIO, gracia=True), dict(nominal="2024-06-18", limite="2024-06-18 14:00", gracia="2024-06-19")),
    ("3", caso(HJ, "2024-03-20", 5, inhabiles={D("2024-03-24")}, gracia=True), dict(nominal="2024-03-27", limite="2024-03-27 14:00", gracia="2024-03-28")),
    ("3b", caso(HJ, "2024-03-20", 5, inhabiles=SEMANA_SANTA, gracia=True), dict(nominal="2024-03-27", limite="2024-03-27 14:00", gracia="2024-04-01")),
    ("4", caso(HJ, "2024-07-11", 5, inhabiles=FERIA_INVIERNO, gracia=True), dict(nominal="2024-08-01", limite="2024-08-01 14:00", gracia="2024-08-02")),
    ("5", caso(HJ, "2024-12-20", 10, inhabiles=FIN_DE_ANIO, gracia=True), dict(nominal="2025-02-06", limite="2025-02-06 14:00", gracia="2025-02-07")),
    ("6", caso(HJ, "2024-12-20", 10, inhabiles={D("2024-12-25")}, gracia=True, cubierto_hasta="2024-12-31"), "CALENDARIO_NO_CARGADO"),
    ("7", caso(HJ, "2024-06-03", 0, inhabiles=JUNIO, gracia=True), "SIN_VENCIMIENTO"),
    ("8", caso(HJ, "2024-06-03", 10, inhabiles=JUNIO), dict(nominal="2024-06-18", limite="2024-06-18 14:00", gracia=None)),
    ("9", caso(HJ, "2024-06-03", 10, inhabiles=JUNIO, gracia=True, prorroga=1), dict(nominal="2024-06-19", limite="2024-06-19 14:00", gracia="2024-06-24")),
    ("10", caso(HJ, "2024-06-01", 3, gracia=True), dict(nominal="2024-06-05", limite="2024-06-05 14:00", gracia="2024-06-06")),
    ("11", caso("CORRIDOS", "2024-06-12", 5, inhabiles=JUNIO, gracia=True), dict(nominal="2024-06-17", limite="2024-06-18 14:00", gracia="2024-06-19")),
    ("12", caso(HJ, "2024-07-17", 3, inhabiles=FERIA_INVIERNO, gracia=True), dict(nominal="2024-07-31", limite="2024-07-31 14:00", gracia="2024-08-01")),
    ("13", caso(HJ, "2024-06-03", 10, inhabiles=JUNIO, tipo_limite="FIN_DEL_DIA"), dict(nominal="2024-06-18", limite="2024-06-19 00:00", gracia=None)),
    ("14", caso(HJ, "2024-06-03", 10, gracia=True, estado_calendario="PROVISORIO"), dict(nominal="2024-06-17", limite="2024-06-17 14:00", gracia="2024-06-18", provisorio=True)),
    ("15", caso("HABILES_ADMINISTRATIVOS", "2024-07-11", 2, inhabiles=FERIA_INVIERNO), dict(nominal="2024-07-15", limite="2024-07-15 14:00", gracia=None)),
    ("16", caso("HABILES_ADMINISTRATIVOS", "2024-06-14", 2, inhabiles=JUNIO, inhabiles_admin=JUNIO), dict(nominal="2024-06-19", limite="2024-06-19 14:00", gracia=None)),
    ("17", caso("MESES", "2025-01-31", 1), dict(nominal="2025-02-28", limite="2025-02-28 14:00", gracia=None)),
    ("18", caso("ANIOS", "2024-02-29", 2, cubierto_hasta="2026-12-31", tipo_limite="FIN_DEL_DIA"), dict(nominal="2026-02-28", limite="2026-03-03 00:00", gracia=None)),
    ("19", caso("ANIOS", "2024-02-29", 2, tipo_limite="FIN_DEL_DIA"), dict(nominal="2026-02-28", limite="2026-03-01 00:00", gracia=None, incompleto=True)),
    ("20", caso("HORAS", "2024-06-07T10:30", 48), dict(nominal="2024-06-09", limite="2024-06-09 10:30", gracia=None)),
    ("21", caso("FECHA_FIJADA", "2024-06-17T09:00", 0, inhabiles=JUNIO), dict(nominal="2024-06-17", limite="2024-06-17 09:00", gracia=None, advertencias=["FECHA_EN_DIA_INHABIL"])),
    ("22", caso("ANTICIPACION_HABILES_JUDICIALES", "2024-06-12", 3), dict(nominal="2024-06-06", limite="2024-06-06 14:00", gracia=None)),
    ("23", caso("ANTICIPACION_HABILES_JUDICIALES", "2024-06-24", 3, inhabiles=JUNIO), dict(nominal="2024-06-13", limite="2024-06-13 14:00", gracia=None)),
]
RECHAZOS = [
    ("E1", caso("HORAS", "2024-06-07T10:30", 48, gracia=True)),
    ("E2", caso("MESES", "2025-01-31", 1, prorroga=1)),
]

fallas = 0
for nombre, argumentos, esperado in CASOS:
    r = calcular(**argumentos)
    if isinstance(esperado, str):
        ok, detalle = r["estado"] == esperado, r["estado"]
    else:
        gracia = r["limite_con_gracia"]
        ok = (r["estado"] == "CALCULADO"
              and r["nominal"] == D(esperado["nominal"])
              and f"{r['limite_ordinario']:%Y-%m-%d %H:%M}" == esperado["limite"]
              and (gracia.date() if gracia else None) == (esperado["gracia"] and D(esperado["gracia"]))
              and r["calendario_provisorio"] == esperado.get("provisorio", False)
              and r["calendario_incompleto"] == esperado.get("incompleto", False)
              and r["advertencias"] == esperado.get("advertencias", []))
        detalle = (f"nominal {fmt(r['nominal'])[:14]} | límite ordinario {fmt(r['limite_ordinario'])}"
                   + (f" | gracia {fmt(gracia)}" if gracia else "")
                   + (" | calendario provisorio" if r["calendario_provisorio"] else "")
                   + (" | calendario incompleto" if r["calendario_incompleto"] else "")
                   + "".join(f" | {a}" for a in r["advertencias"]))
    fallas += not ok
    print(f"{'OK ' if ok else 'ERR'} caso {nombre}: {detalle}")

for nombre, argumentos in RECHAZOS:
    try:
        calcular(**argumentos)
        fallas += 1
        print(f"ERR caso {nombre}: debía rechazarse")
    except ValueError as error:
        print(f"OK  caso {nombre}: rechazado ({error})")

raise SystemExit(1 if fallas else 0)
