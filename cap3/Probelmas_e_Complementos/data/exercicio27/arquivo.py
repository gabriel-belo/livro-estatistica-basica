import pandas as pd

dic={'Peso (gramas)':['[960 980)', '[980 1000)', '[1000 1020)', '[1020 1040)', '[1040 1060)', '[1060 1080'],
     'Frequência Absoluta': [60, 160, 280, 260, 160, 80]}
dados= pd.DataFrame(dic)

dados.to_csv('Peso frangos1.csv', index= False)
