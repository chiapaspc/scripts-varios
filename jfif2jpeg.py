import os
from PIL import Image

def convert_jfif_to_jpeg(directory):
    # Asegúrate de que el directorio existe
    if not os.path.isdir(directory):
        print(f"El directorio {directory} no existe.")
        return

    # Itera sobre los archivos en el directorio
    for filename in os.listdir(directory):
        # Verifica si el archivo tiene la extensión .jfif
        if filename.lower().endswith('.jfif'):
            jfif_path = os.path.join(directory, filename)
            jpeg_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.jpeg")

            # Abre la imagen y la guarda en formato JPEG
            try:
                with Image.open(jfif_path) as img:
                    img.save(jpeg_path, 'JPEG')
                print(f"Convertido: {filename} a {jpeg_path}")
                # Elimina el archivo .jfif original
                os.remove(jfif_path)
                print(f"Eliminado: {jfif_path}")
            except Exception as e:
                print(f"No se pudo convertir {filename}: {e}")

    print("Conversión completada.")

# Obtiene el directorio donde se encuentra el script
directorio = os.path.dirname(os.path.abspath(__file__))

# Llama a la función para convertir las imágenes
convert_jfif_to_jpeg(directorio)
