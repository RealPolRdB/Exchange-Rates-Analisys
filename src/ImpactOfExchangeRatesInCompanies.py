#Importamos los paquetes que vamos a necesitar
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

#Creamos dos arrays
exchange_rates_Python = {}
currencies = ['EURUSD', 'CHFUSD=X', 'AUDUSD', 'GBPUSD']

#API Key
apiKey = #INSERT YOU API KEY HERE

#Creamos el bucle para las divisas
for currency in currencies:
    
    forex = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{currency}?apikey={apiKey}')

    forexJSON = forex.json()

    #Almacenamos en un dict los valores deseados
    exchange_rates_Python[currency] = {}

    for item in forexJSON['historical']:
        adj_close = item['adjClose']
        trade_date = item['date']
        exchange_rates_Python[currency][trade_date] = adj_close

#Salimos del bucle inicial de currencies y cPonvertimos los datos en DataFrame
currenciesDataFrame = pd.DataFrame.from_dict(exchange_rates_Python)

#Convertimos los valores "cabeceros" de las filas a formato tiempo
currenciesDataFrame.index = pd.to_datetime(currenciesDataFrame.index)

#Cogemos los valores de la última semana
currenciesDataFrameLastWeek = currenciesDataFrame.iloc[:30,:]

#Representamos las figuras
fig, axes = plt.subplots(nrows=2, ncols=2)

currenciesDataFrameLastWeek[currencies[0]].plot(ax=axes[0,0])
axes[0,0].set_title(currencies[0])

currenciesDataFrameLastWeek[currencies[1]].plot(ax=axes[0,1])
axes[0,1].set_title(currencies[1])

currenciesDataFrameLastWeek[currencies[2]].plot(ax=axes[1,0])
axes[1,0].set_title(currencies[2])

currenciesDataFrameLastWeek[currencies[3]].plot(ax=axes[1,1])
axes[1,1].set_title(currencies[3])

plt.tight_layout()
plt.show()