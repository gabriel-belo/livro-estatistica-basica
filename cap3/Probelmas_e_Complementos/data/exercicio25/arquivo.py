import pandas as pd
import os
dic={'Faixa salarial':['[0 2)', '[2 4)', '[4 6)', '[6 8)', '[8 10)', '[10 12)', '[12 14)'],
     'Frequência':[10000, 3900, 2000, 1100, 800, 700, 2000]}

dados=pd.DataFrame(dic)

dados.to_csv('Salario Anual.csv', index= False)
