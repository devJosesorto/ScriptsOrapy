import csv
import random

# Ruta del archivo CSV a crear
ruta_archivo = 'archivo.csv'

# Encabezados del archivo CSV
encabezados = ['ID', 'Nombre', 'Edad', 'Puntuacion']

# Función para generar datos aleatorios
def generar_datos():
    nombres = ['Juan', 'María', 'Carlos', 'Laura', 'Pedro']
    edad = random.randint(18, 50)
    puntuacion = random.uniform(0, 100)
    return [str(random.randint(1, 1000)), random.choice(nombres), str(edad), str(round(puntuacion, 2))]

# Crear y escribir en el archivo CSV
with open(ruta_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir encabezados
    escritor_csv.writerow(encabezados)
    
    # Escribir 1000 registros
    for _ in range(1000):
        escritor_csv.writerow(generar_datos())

print(f'Se ha creado el archivo CSV con 1000 registros en "{ruta_archivo}".')
