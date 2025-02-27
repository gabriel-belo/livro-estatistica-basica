import pandas as pd
import os

dados={'Número de filhos':[0, 1, 2, 3, 4, 5, 6],
       'Frequencia de familias': [17, 20, 28, 19, 7, 4, 5]}

dados= pd.DataFrame(dados)

dados.to_csv('Filhos_por_familia.csv', index= False)
