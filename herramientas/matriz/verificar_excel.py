import collections
import sys

from pycel import ExcelCompiler

from cargar_datos import cargar, prefijo

_datos = cargar(sys.argv[2] if len(sys.argv) > 2 else None)
FLUJO, NODOS, TRANSICIONES = _datos.FLUJO, _datos.NODOS, _datos.TRANSICIONES

xl = ExcelCompiler(filename=sys.argv[1])
res = collections.Counter()
for r in range(2, len(NODOS) + 2):
    res["Nodos:" + str(xl.evaluate(f"Nodos!P{r}"))] += 1
for r in range(2, len(TRANSICIONES) + 2):
    res["Transiciones:" + str(xl.evaluate(f"Transiciones!I{r}"))] += 1
print(res)
fila = len(FLUJO) + 2
print("Nodo inicial:", xl.evaluate(f"Flujo!B{fila}"), "| Filas pendientes:", xl.evaluate(f"Flujo!B{fila + 1}"))
fila_sin_gracia = (next((i for i, n in enumerate(NODOS, start=2) if n[6] == "HABILES_ADMINISTRATIVOS"), None)
                   or next(i for i, n in enumerate(NODOS, start=2) if i > 2 and n[6] not in _datos.CON_GRACIA))
xl.set_value("Nodos!F2", 5)
xl.set_value("Transiciones!C3", f"{prefijo(NODOS)}_999")
xl.set_value(f"Nodos!H{fila_sin_gracia}", "SI")
print("Con errores inyectados:", xl.evaluate("Nodos!P2"), "|", xl.evaluate("Transiciones!I3"),
      "|", xl.evaluate(f"Nodos!P{fila_sin_gracia}"))
