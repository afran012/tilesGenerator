import os
import sys
from osgeo import gdal

def validate_proj_lib():
    # Posibles ubicaciones de PROJ_LIB
    possible_proj_libs = [
        os.path.join(os.path.dirname(sys.executable), 'Library', 'share', 'proj'),
        r"C:\Program Files\PostgreSQL\15\share\contrib\postgis-3.5\proj"
    ]

    valid_proj_libs = []
    for proj_lib in possible_proj_libs:
        if os.path.exists(proj_lib):
            valid_proj_libs.append(proj_lib)
            print(f"Encontrado PROJ_LIB: {proj_lib}")

    if not valid_proj_libs:
        print("Error: No se encontró una instalación válida de PROJ.")
        return False

    return valid_proj_libs

def validate_gdal():
    try:
        gdal_version = gdal.VersionInfo()
        print(f"GDAL version: {gdal_version}")
        return True
    except Exception as e:
        print(f"Error al verificar la versión de GDAL: {e}")
        return False

def validate_environment():
    print("Validando el entorno de desarrollo...\n")

    # Validar PROJ_LIB
    valid_proj_libs = validate_proj_lib()
    if not valid_proj_libs:
        sys.exit(1)

    # Validar GDAL
    if not validate_gdal():
        sys.exit(1)

    print("\nEntorno de desarrollo validado correctamente.")
    print("Instalaciones de PROJ encontradas:")
    for proj_lib in valid_proj_libs:
        print(f"  - {proj_lib}")

if __name__ == "__main__":
    validate_environment()