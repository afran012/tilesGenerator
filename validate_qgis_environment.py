import os
import sys
from pathlib import Path

def setup_qgis_paths():
    # Base QGIS installation path
    qgis_path = Path(r"C:\Program Files\QGIS 3.34.12")
    
    paths = {
        'QGIS_ROOT': qgis_path,
        'QGIS_PREFIX_PATH': qgis_path / 'apps' / 'qgis-ltr',
        'QGIS_PYTHON': qgis_path / 'apps' / 'Python312',
        'QGIS_BIN': qgis_path / 'bin',
    }
    
    # Setup environment variables
    os.environ['QGIS_PREFIX_PATH'] = str(paths['QGIS_PREFIX_PATH'])
    os.environ['PYTHONPATH'] = str(paths['QGIS_PREFIX_PATH'] / 'python')
    os.environ['PATH'] = f"{str(paths['QGIS_BIN'])}{os.pathsep}{os.environ['PATH']}"
    
    # Add paths to sys.path
    python_paths = [
        str(paths['QGIS_PREFIX_PATH'] / 'python'),
        str(paths['QGIS_PYTHON'] / 'Lib' / 'site-packages'),
        str(paths['QGIS_PYTHON']),
        str(paths['QGIS_PREFIX_PATH'] / 'python' / 'plugins'),
    ]
    
    for path in python_paths:
        if path not in sys.path and os.path.exists(path):
            sys.path.append(path)
            print(f"✓ Added to Python path: {path}")
    
    return paths

def validate_paths(paths):
    all_valid = True
    for name, path in paths.items():
        if path.exists():
            print(f"✓ {name} exists: {path}")
        else:
            print(f"✗ {name} not found: {path}")
            all_valid = False
    return all_valid

def test_qgis_imports():
    try:
        print("\nTesting QGIS imports...")
        import qgis.core
        print("✓ Successfully imported qgis.core")
        return True
    except ImportError as e:
        print(f"✗ Failed to import QGIS: {str(e)}")
        return False

def initialize_qgis():
    try:
        print("\nInitializing QGIS...")
        from qgis.core import QgsApplication
        from qgis.analysis import QgsNativeAlgorithms
        
        qgs = QgsApplication([], False)
        qgs.initQgis()
        print("✓ QGIS initialized successfully")
        
        # Test processing algorithms
        print("\nTesting processing algorithms...")
        QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
        print("✓ Native algorithms loaded successfully")
        
        qgs.exitQgis()
        print("✓ QGIS finalized successfully")
        return True
    except Exception as e:
        print(f"✗ Error during QGIS initialization: {str(e)}")
        return False

def main():
    print("QGIS Environment Validator")
    print("-" * 50)
    
    # Setup and validate paths
    print("\nValidating paths...")
    paths = setup_qgis_paths()
    paths_valid = validate_paths(paths)
    
    if not paths_valid:
        print("\n✗ Path validation failed. Please check QGIS installation.")
        return False
    
    # Test QGIS imports
    if not test_qgis_imports():
        print("\n✗ QGIS import test failed. Check Python environment.")
        return False
    
    # Initialize QGIS
    if not initialize_qgis():
        print("\n✗ QGIS initialization failed.")
        return False
    
    print("\n✓ All validations completed successfully!")
    return True

if __name__ == "__main__":
    main()