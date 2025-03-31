import pandas as pd
import os

dic={'Consumo de Leite':['[0 1)', '[1 2)', '[2 3)', '[3 5)'],
     'Frequencia Relativa':[0.2, 0.5, 0.2, 0.1],
     'Frequencia Absoluta': [20, 50, 20, 10],
     'Frequencia Acumulada': [20, 70, 90, 100]}

dados= pd.DataFrame(dic)

dados.to_csv('Consumo de Leite.csv', index= False)
