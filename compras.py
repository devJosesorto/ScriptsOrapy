import pandas as pd
import plotly.express as px


df = pd.read_csv('Scripts/resultados.csv', header=None,
                 names=['Cantidad', 'Precio', 'Descripcion'], encoding='latin1')


df['Cantidad'] = df['Cantidad'].astype(str)
df['Cantidad'] = df['Cantidad'].str.extract('(\d+)').astype(int)

fig = px.bar(df, x='Descripcion', y='Cantidad', title='Ventas por articulo')


fig.show()
