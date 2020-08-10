import pandas as pd

df_edad = pd.read_csv(r'C:\Users\Martu\Downloads\notificaciones_grupo_etario.csv')

print(df_edad.head(), '\n\n', df_edad.describe(), '\n\n', df_edad.info())

# En las columnas que deberían ser numéricas, hay datos tipo enteros. En todas las columnas se ingresó la misma cantidad de datos no nulos, por lo cual no hay datos faltantes. Los valores de mínimos, máximos y promedio son congruentes con los datos reportados. Teniendo en cuenta toda esta información, considero que los datos cargados están limpios y listos para ser analizados.

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

#Formateo la fecha
df_edad['Fecha strp'] = pd.to_datetime(df_edad['Fecha'])

#Inicio el gráfico vacío con las dimensiones deseadas
fig = plt.figure(figsize=(12, 9))

#Grafico por grupo etario y formateo eje x
ax = fig.add_subplot(2, 2, 1)
ax = sns.lineplot(x = 'Fecha strp', y = 'Confirmados', data = df_edad.loc[df_edad['Grupo etario'].isin(['0-<1', '1-4', '5-9', '10-14', '15-19'])], hue ="Grupo etario")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Casos confirmados')

ax = fig.add_subplot(2, 2, 2)
ax = sns.lineplot(x = 'Fecha strp', y = 'Confirmados', data = df_edad.loc[df_edad['Grupo etario'].isin(['20-24', '25-29', '30-34', '35-39', '40-44'])], hue ="Grupo etario")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Casos confirmados')

ax = fig.add_subplot(2, 2, 3)
ax = sns.lineplot(x = 'Fecha strp', y = 'Confirmados', data = df_edad.loc[df_edad['Grupo etario'].isin(['45-49', '50-54', '55-59', '60-64', '65-69'])], hue ="Grupo etario")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Casos confirmados')

ax = fig.add_subplot(2, 2, 4)
ax = sns.lineplot(x = 'Fecha strp', y = 'Confirmados', data = df_edad.loc[df_edad['Grupo etario'].isin(['70-74', '75-79', '80-84', '85-89', '90-94'])], hue ="Grupo etario")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=15))
ax.set(xlabel='Fecha', ylabel='Casos confirmados')

# En las figuras se puede observar que, si bien todos los grupos etarios están presentando una mayor cantidad de casos con el correr de los días, la mayor cantidad de contagios se concentra en personas de entre 20 y 69 años.

#Calculo porcentaje de confirmados según edad
edad_porc = df_edad.tail(20)
edad_porc.index = edad_porc['Grupo etario']
edad_porc = edad_porc['Confirmados']/(edad_porc['Confirmados'].sum())*100
edad_porc.name = 'Porcentaje de casos confimados según grupo etario '

#Grafico porcentaje según edad
fig, ax = plt.subplots(figsize=(12,6))
ax1 = ax.bar(x = edad_porc.index, height = edad_porc)
ax.set_ylabel('Porcentaje del total de casos confirmados (%)')
ax.set_xlabel('Grupo etario')
ax.set_title('Porcentaje de casos confimados según grupo etario')
