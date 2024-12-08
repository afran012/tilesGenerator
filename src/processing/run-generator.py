import os
import sys

def validate_proj_lib():
    # Posibles ubicaciones de PROJ_LIB
    possible_proj_libs = [
        os.path.join(os.path.dirname(sys.executable), 'Library', 'share', 'proj'),
        r"C:\Program Files\PostgreSQL\15\share\contrib\postgis-3.5\proj"
    ]

    for proj_lib in possible_proj_libs:
        if os.path.exists(proj_lib):
            os.environ['PROJ_LIB'] = proj_lib
            print(f"Usando PROJ_LIB: {proj_lib}")
            return True

    print("Error: No se encontró una instalación válida de PROJ.")
    return False

# Validar PROJ_LIB
if not validate_proj_lib():
    sys.exit(1)

# Agregar el directorio del módulo tile_generation al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'processing'))

from tile_generation import TileGenerator

# Configura tus rutas
INPUT_FILE = r"E:\entrenamientomaquina\tilescompletos\raster2018.tif"
OUTPUT_DIR = r"E:\entrenamientomaquina\tiles generados\2018"

# Ejecuta el generador
generator = TileGenerator(INPUT_FILE, OUTPUT_DIR)
generator.generate_tiles(zoom_min=12, zoom_max=15)