from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import csv

# Reemplaza 'usuario', 'contrasena', 'host:puerto/servicio' con tus propias credenciales
# Ejemplo: 'oracle://usuario:contrasena@localhost:1521/orcl'

oracle_url = "oracle://C##JSORTO:72776400@localhost:1521/XE"

# Crear el motor de la base de datos
engine = create_engine(oracle_url, echo=True)

# Crear una sesion de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Usar text() para declarar la expresion SQL explicitamente
    query = text("SELECT * FROM COMPRAS")

    # Intentar ejecutar la consulta

    result = session.execute(query)

    print('================CSV====================')

    with open('resultados.csv', 'w', newline='') as csvfile:
        # Crear un objeto escritor CSV
        csv_writer = csv.writer(csvfile)

        for row in result.fetchall():
            csv_writer.writerow(row)

    print('================CSV====================')
    # Imprimir todos los resultados
    print("Conexion exitosa. Resultado de la consulta:")

except Exception as e:
    print("Error de conexion:", e)
finally:

    # Cerrar la sesion
    session.close()
