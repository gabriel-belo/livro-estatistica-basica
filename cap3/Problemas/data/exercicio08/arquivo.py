import pandas as pd
import os

dic={'Idade':[26, 32, 36, 20, 40, 28, 41, 43, 34, 23, 33, 27, 37, 44, 30, 38, 31, 39, 25, 37, 30, 34,
              41, 26, 32, 35, 46, 29, 40, 35, 31, 36, 43, 33, 48, 42],
     'Numero de filhos':[0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 3, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 2, 2,
                         0, 0, 5, 2, 0, 1, 3, 0, 2, 3]}

dados= pd.DataFrame(dic)

dados.to_csv('Idade_NumFilhos.csv', index= False)