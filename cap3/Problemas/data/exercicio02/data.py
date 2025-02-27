import pandas as pd
import os

dados={'Ação':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
       'Taxa de Juros':[2.59, 2.64, 2.6, 2.62, 2.57, 2.55, 2.61, 2.5, 2.63, 2.64]}

info_acoes= pd.DataFrame(dados)

info_acoes.to_csv('info_acoes.csv', index=False)