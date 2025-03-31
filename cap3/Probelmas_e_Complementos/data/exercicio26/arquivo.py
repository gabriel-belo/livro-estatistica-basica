import pandas as pd

dic={'Faixa':['[2 4)', '[4 6)',  '[6 8)', '[8 10)', '[10 12)'],
     'Frequência Absoluta': [15, 25, 20, 30, 10]}


dados= pd.DataFrame(dic)

dados.to_csv('Valores.csv', index= False)