import os
import json


def reduce_data(origen, destino, count):
    # Verificar si el archivo de origen existe
    if not os.path.isfile(origen):
        print(f"El archivo {origen} no existe.")
        return

    # Leer el contenido del archivo JSON de origen
    try:
        with open(origen, "r") as file:
            datos = json.load(file)
    except Exception as e:
        print(f"Error al leer el archivo {origen}: {e}")
        return

    # Crear las carpetas necesarias para la dirección de destino si estas no existen
    directorio_destino = os.path.dirname(destino)
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    datos["products"] = datos["products"][:count]
    try:
        with open(destino, "w") as file:
            json.dump(datos, file, indent=4)
        print(f"Archivo copiado exitosamente a {destino}")
    except Exception as e:
        print(f"Error al escribir el archivo {destino}: {e}")


reduce_data(
    "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/chatbot/data/padel_store/tiendapadelpoint.json",
    "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/chatbot/data/padel_store_short/tiendapadelpoint.json",
    20,
)
