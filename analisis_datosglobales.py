### Casos confimados por fecha y fallecidos en la provincia

import pandas as pd

df_total = pd.read_csv(r'C:\Users\Martu\Downloads\notificaciones_total_provincial.csv')

print(df_total.head(), '\n\n', df_total.describe(), '\n\n', df_total.info())

# En las columnas que deberían ser numéricas, hay datos tipo enteros. En todas las columnas se ingresó la misma cantidad de datos no nulos, por lo cual no hay datos faltantes. Los valores de mínimos, máximos y promedio son congruentes con los datos reportados. Teniendo en cuenta toda esta información, considero que los datos cargados están limpios y listos para ser analizados.

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

#Formateo la fecha
df_total['Fecha strp'] = pd.to_datetime(df_total['Fecha'])

#Inicio el gráfico vacío con las dimensiones deseadas
fig = plt.figure(figsize=(20, 10))

#Grafico por casos confimados y fallecidos
ax = fig.add_subplot(1, 2, 1)
ax = sns.lineplot(x = 'Fecha strp', y = 'Confirmados', data = df_total)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Casos confirmados', title='Casos confimados en la provincia de Santa Fe')

ax = fig.add_subplot(1, 2, 2)
ax = sns.lineplot(x = 'Fecha strp', y = 'Fallecidos', data = df_total)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Fallecidos', title='Fallecidos en la provincia de Santa Fe')

