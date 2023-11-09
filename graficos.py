import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

# Inicializar la aplicacion Dash
app = dash.Dash(__name__)

# Diseno del dashboard
app.layout = html.Div(children=[
    html.H1(children='Mi Dashboard'),

    dcc.Graph(
        id='ejemplo-grafico',
        figure=px.histogram(df, x='x', y='y', title='Grafico de ejemplo')
    )
])

# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)
