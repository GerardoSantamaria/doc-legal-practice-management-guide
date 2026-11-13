import importlib.util
import sys
from pathlib import Path


def cargar(ruta=None):
    if ruta is None:
        import datos
        return datos
    ruta = Path(ruta).resolve()
    sys.path.insert(0, str(ruta.parent))
    spec = importlib.util.spec_from_file_location(ruta.stem, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def prefijo(nodos):
    return nodos[0][0].split("_")[0]
