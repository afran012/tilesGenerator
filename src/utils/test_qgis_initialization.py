import os
import sys

# Asegúrate de que la variable de entorno QGIS_PREFIX_PATH esté configurada correctamente
qgis_prefix_path = os.environ.get('QGIS_PREFIX_PATH', 'C:/OSGeo4W/apps/qgis')
os.environ['QGIS_PREFIX_PATH'] = qgis_prefix_path

# Agregar las rutas necesarias a sys.path
sys.path.append(os.path.join(qgis_prefix_path, 'python'))
sys.path.append(os.path.join(qgis_prefix_path, 'python', 'plugins'))

try:
    from qgis.core import QgsApplication, QgsRasterLayer
    from qgis.analysis import QgsNativeAlgorithms
    import processing

    # Inicializar QGIS
    QgsApplication.setPrefixPath(qgis_prefix_path, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    
    # Añadir algoritmos nativos de QGIS
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

    print("QGIS inicializado correctamente.")
    
    # Finalizar QGIS
    qgs.exitQgis()
    print("QGIS finalizado.")
except ImportError as e:
    print(f"Error al importar módulos de QGIS: {e}")
except Exception as e:
    print(f"Error al inicializar QGIS: {e}")