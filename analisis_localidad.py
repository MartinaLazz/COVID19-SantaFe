import pandas as pd

df_localidad = pd.read_csv(r'C:\Users\Martu\Downloads\notificaciones_localidad.csv')

print(df_localidad.head(), '\n\n', df_localidad.describe(), '\n\n', df_localidad.info())

# En las columnas que deberían ser numéricas, hay datos tipo enteros. En todas las columnas se ingresó la misma cantidad de datos no nulos, por lo cual no hay datos faltantes. Los valores de mínimos, máximos y promedio son congruentes con los datos reportados. Teniendo en cuenta toda esta información, considero que los datos cargados están limpios y listos para ser analizados.

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

#Formateo la fecha
df_localidad['Fecha strp'] = pd.to_datetime(df_localidad['Fecha'])

#Hago lista de ciudades
localidades = df_localidad['Localidad'].unique()

#Trabajo con la ciudad ingresada
ciudad = input('Localidad a buscar: ').upper()

if ciudad not in localidades:
    print('La localidad ingresada no corresponde a la provincia de Santa Fe o no reportó casos confirmados a la fecha') 
else:
#Grafico por ciudad buscada y formateo eje x
    fig = plt.figure(figsize=(12,6))
    ax = plt.axes()
    ax.plot(df_localidad.loc[df_localidad['Localidad'] == ciudad, 'Fecha strp'], df_localidad.loc[df_localidad['Localidad'] == ciudad, 'Confirmados'])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
    ax.set(xlabel='Fecha', ylabel='Casos confirmados', title='Casos confirmados según fecha en %s'%(ciudad.title()))
    print(fig)
