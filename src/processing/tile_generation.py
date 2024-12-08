import os
import subprocess
import sys
from osgeo import gdal

class TileGenerator:
    def __init__(self, input_file, output_dir):
        self.input_file = input_file
        self.output_dir = output_dir

    def generate_tiles(self, zoom_min=0, zoom_max=18):
        # Validar que el archivo de entrada exista
        if not os.path.exists(self.input_file):
            print(f"Error: El archivo de entrada no existe: {self.input_file}")
            return

        # Validar que el archivo de entrada sea un dataset reconocido por GDAL
        dataset = gdal.Open(self.input_file)
        if dataset is None:
            print(f"Error: El archivo de entrada no es un dataset reconocido por GDAL: {self.input_file}")
            return

        # Validar que el directorio de salida exista, si no, crearlo
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Directorio de salida creado: {self.output_dir}")

        # Ruta completa de gdal2tiles.py
        gdal2tiles_path = os.path.join(os.path.dirname(sys.executable), 'Scripts', 'gdal2tiles.py')

        # Comando para generar tiles usando gdal2tiles.py
        command = [
            sys.executable,  # Usar el ejecutable de Python del entorno actual
            gdal2tiles_path,
            '-z', f'{zoom_min}-{zoom_max}',
            '-w', 'none',
            '-r', 'near',  # Resampling method
            '-p', 'mercator',  # Profile
            '-t', 'tiles',  # Title
            self.input_file,
            self.output_dir
        ]

        # Mostrar el comando que se va a ejecutar
        print(f"Ejecutando comando: {' '.join(command)}")

        # Ejecutar el comando
        try:
            subprocess.run(command, check=True)
            print(f"Tiles generados exitosamente en: {self.output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error al generar tiles: {e}")
        except OSError as e:
            print(f"Error al ejecutar gdal2tiles.py: {e}")