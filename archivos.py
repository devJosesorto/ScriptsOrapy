import os
import glob

# CARPETA
pathCarpeta = r'C:\Users\Jose\Documents\Python\Notes\carpetas'
patron = '*.csv'

archivosEncontrados = []

# Utiliza os.walk para recorrer todas las subcarpetas
for carpeta_actual, subcarpetas, archivos in os.walk(pathCarpeta):
    archivos_en_carpeta = glob.glob(os.path.join(carpeta_actual, patron))
    archivosEncontrados.extend(archivos_en_carpeta)

# Imprime la lista de archivos encontrados
for ruta in archivosEncontrados:
    print(ruta)
