import os

# Directorios de datos
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
OUTPUT_DATA_DIR = os.path.join(DATA_DIR, 'output')

# Archivo de entrada específico
INPUT_FILE = r"E:\work\ProyectoCatasPro\06 ORTOFOTOS - copia\Ortofoto_Itagui_2021.ecw"

# Directorio de salida específico
OUTPUT_DIR = r"E:\entrenamientomaquina\tiles generados\2021"