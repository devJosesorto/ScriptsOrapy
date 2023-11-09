import dash
from dash import dcc, html
import pandas as pd

# Ruta de tu archivo CSV
archivo_csv = 'Scripts/resultados.csv'
tabla_dinamica = ''

# Cargar el CSV en un DataFrame sin encabezado con codificacion ISO-8859-1
df = pd.read_csv(archivo_csv, header=None, encoding='ISO-8859-1')


# Ponle nombres a las columnas
nombres_columnas = ['ID', 'Precio', 'Nombre']  # Reemplaza con tus nombres
df.columns = nombres_columnas
# Visualizar el DataFrame

tabla_dinamica = df.groupby('Nombre').size().reset_index(name='Cantidad')


# Visualiza la tabla dinamica
# print(tabla_dinamica)


app = dash.Dash(__name__)

# Disemo de la aplicacion
app.layout = html.Div(children=[
    html.H1(children='Tabla Dinamica'),

    dcc.Graph(
        id='tabla-dinamica-grafico',
        figure={
            'data': [
                {'x': tabla_dinamica['Nombre'], 'y': tabla_dinamica['Cantidad'],
                    'type': 'bar', 'name': 'Cantidad 2021'},
                {'x': tabla_dinamica['Nombre'], 'y': tabla_dinamica['Cantidad'],
                    'type': 'bar', 'name': 'Cantidad 2022'}
            ],
            'layout': {
                'title': 'Frecuencia de Nombres'
            }
        }
    )
])

# Ejecuta la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)
