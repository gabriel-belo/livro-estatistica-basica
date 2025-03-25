import pandas as pd
import os

dic= {'Classes de salários': ['[4,00 a 8,00)', '[8,00 a 12,00)', '[12,00 a 16,00)', '[16,00 a 20,00',
                             '[20,00 a 24,00)'],
      'Frequência absoluta': [10, 12, 8, 5, 1],
      'Porcentagem 100 f1':[22.78, 33.33, 22.22, 13.89, 2.78]}

dados= pd.DataFrame(dic)

dados.to_csv('Orçamento_Companhia.csv', index= False)
