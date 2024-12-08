import os

def create_project_structure(base_path):
   # Estructura de directorios
   dirs = [
       'data/raw',
       'data/processed',
       'data/output',
       'src/processing',
       'src/utils',
       'notebooks',
       'tests'
   ]
   
   # Crear directorios
   for dir in dirs:
       os.makedirs(os.path.join(base_path, dir), exist_ok=True)

   # Crear archivos
   files = {
       'src/__init__.py': '',
       'src/processing/__init__.py': '',
       'src/processing/tile_generation.py': '',
       'src/utils/__init__.py': '',
       'src/utils/cuda_utils.py': '',
       'src/config.py': '',
       'tests/__init__.py': '',
       'notebooks/exploratory.ipynb': '',
       '.gitignore': '*.pyc\n__pycache__/\n.ipynb_checkpoints/',
       'README.md': '# QGIS Project\n\nDescription of your project here.',
       'environment.yml': '''name: qgis-env
channels:
 - conda-forge
 - pytorch
dependencies:
 - python=3.9
 - pytorch
 - torchvision
 - qgis
 - gdal'''
   }

   for file_path, content in files.items():
       with open(os.path.join(base_path, file_path), 'w') as f:
           f.write(content)

if __name__ == "__main__":
   project_path = input("Ingrese la ruta para el proyecto: ")
   create_project_structure(project_path)
   print(f"Estructura de proyecto creada en {project_path}")