import collections
import sys

from pycel import ExcelCompiler

from datos import FLUJO, NODOS, TRANSICIONES

xl = ExcelCompiler(filename=sys.argv[1])
res = collections.Counter()
for r in range(2, len(NODOS) + 2):
    res["Nodos:" + str(xl.evaluate(f"Nodos!P{r}"))] += 1
for r in range(2, len(TRANSICIONES) + 2):
    res["Transiciones:" + str(xl.evaluate(f"Transiciones!I{r}"))] += 1
print(res)
fila = len(FLUJO) + 2
print("Nodo inicial:", xl.evaluate(f"Flujo!B{fila}"), "| Filas pendientes:", xl.evaluate(f"Flujo!B{fila + 1}"))
fila_adm = next(i for i, n in enumerate(NODOS, start=2) if n[6] == "HABILES_ADMINISTRATIVOS")
xl.set_value("Nodos!F2", 5)
xl.set_value("Transiciones!C3", "LAB_999")
xl.set_value(f"Nodos!H{fila_adm}", "SI")
print("Con errores inyectados:", xl.evaluate("Nodos!P2"), "|", xl.evaluate("Transiciones!I3"),
      "|", xl.evaluate(f"Nodos!P{fila_adm}"))
