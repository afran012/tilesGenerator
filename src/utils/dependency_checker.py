# src/utils/dependency_checker.py
import os
import importlib

class DependencyChecker:
    def __init__(self):
        self.required_packages = ['torch', 'qgis.core', 'osgeo.gdal', 'numpy', 'processing']
        
    def check_cuda(self):
        try:
            import torch
            return {
                'available': torch.cuda.is_available(),
                'device_name': torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
                'device_count': torch.cuda.device_count() if torch.cuda.is_available() else 0
            }
        except ImportError:
            return {'available': False, 'device_name': None, 'device_count': 0}

    def check_qgis_path(self):
        paths = [
            "C:/OSGeo4W/apps/qgis",
            "C:/Program Files/QGIS 3.40.1",
            os.environ.get('QGIS_PREFIX_PATH', '')
        ]
        for path in paths:
            if path and os.path.exists(path):
                return path
        return None

    def check_package(self, package):
        try:
            importlib.import_module(package)
            return True
        except ImportError:
            return False

    def validate_environment(self):
        return {
            'cuda': self.check_cuda(),
            'qgis_path': self.check_qgis_path(),
            'packages': {pkg: self.check_package(pkg) for pkg in self.required_packages}
        }

    def print_status(self, status):
        print("\n=== Estado del Ambiente ===")
        
        print("\nCUDA:")
        print(f"Disponible: {status['cuda']['available']}")
        if status['cuda']['available']:
            print(f"GPU: {status['cuda']['device_name']}")
            print(f"Dispositivos: {status['cuda']['device_count']}")
            
        print("\nRuta QGIS:")
        print(f"Válida: {status['qgis_path'] is not None}")
        if status['qgis_path']:
            print(f"Ruta: {status['qgis_path']}")
        else:
            print("No se encontró una ruta válida para QGIS. Verifica las siguientes rutas y variables de entorno:")
            print("Rutas verificadas:")
            print("  - C:/OSGeo4W/apps/qgis")
            print("  - C:/Program Files/QGIS 3.40.1")
            print(f"Variable de entorno QGIS_PREFIX_PATH: {os.environ.get('QGIS_PREFIX_PATH', 'No configurada')}")
            
        print("\nPaquetes:")
        for package, installed in status['packages'].items():
            print(f"{package}: {'✓' if installed else '✗'}")

if __name__ == "__main__":
    checker = DependencyChecker()
    status = checker.validate_environment()
    checker.print_status(status)