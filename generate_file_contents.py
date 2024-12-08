import os

def generate_file_contents(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                f.write(f'Archivo: {filename}\n')
                f.write(f'Ruta: {file_path}\n')
                f.write('Contenido:\n')
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        f.write(file.read())
                except Exception as e:
                    f.write(f'Error al leer el archivo: {e}\n')
                f.write('\n' + '-'*80 + '\n\n')

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))  # Directorio del proyecto
    output_file = os.path.join(root_directory, 'contenido_proyecto.txt')
    generate_file_contents(root_directory, output_file)
    print(f"Contenido del proyecto guardado en: {output_file}")