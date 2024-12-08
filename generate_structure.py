import os

def generate_structure(root_dir, output_file):
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(dirpath)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for filename in filenames:
                f.write(f'{subindent}{filename}\n')

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))  # Directorio del proyecto
    output_file = os.path.join(root_directory, 'estructura_proyecto.txt')
    generate_structure(root_directory, output_file)
    print(f"Estructura del proyecto guardada en: {output_file}")