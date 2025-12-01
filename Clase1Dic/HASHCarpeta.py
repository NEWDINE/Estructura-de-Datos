import hashlib
import os

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

ruta = input("Ingresa la ruta: ")
carpeta = input("Ingresa el nombre de la carpeta: ")

ruta_completa = os.path.join(ruta, carpeta)

if not os.path.isdir(ruta_completa):
    print("La carpeta no existe.")
    exit()

for archivo in os.listdir(ruta_completa):
    archivo_path = os.path.join(ruta_completa, archivo)

    if os.path.isfile(archivo_path):
        print(f"\nArchivo: {archivo}")

        try:
            with open(archivo_path, "r", encoding="utf-8") as f:
                contenido = f.read()
            print("\nContenido (texto):")
            print(contenido)
        except:
            print("\nContenido no mostrado (archivo binario).")

        hashed = hash_file(archivo_path)
        print("\nSHA-256:")
        print(hashed)
