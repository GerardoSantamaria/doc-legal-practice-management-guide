import re
import sys
from pathlib import Path

MARCA_SECCION = "## 4. Matriz de Flujos Procesales"

documento = Path(sys.argv[1])
tablas = Path(sys.argv[2]).read_text(encoding="utf-8")
diagrama = Path(sys.argv[3]).read_text(encoding="utf-8")
plantilla = Path(__file__).with_name("secciones.md").read_text(encoding="utf-8")

partes = re.split(r"<!-- (NODOS|TRANSICIONES|DUDAS) -->\n", tablas)
bloques = dict(zip(partes[1::2], (p.strip() for p in partes[2::2])))
bloques["DIAGRAMA"] = diagrama.strip()

cuerpo = plantilla
for clave, valor in bloques.items():
    cuerpo = cuerpo.replace("{{" + clave + "}}", valor)
assert "{{" not in cuerpo, "Quedaron marcadores sin reemplazar en secciones.md"

actual = documento.read_text(encoding="utf-8")
assert MARCA_SECCION in actual, f"No se encontró '{MARCA_SECCION}' en {documento}"
cabecera = actual.split(MARCA_SECCION)[0].rstrip() + "\n\n"
documento.write_text(cabecera + cuerpo, encoding="utf-8")
print(f"Actualizado {documento} (secciones 4 a 6)")
