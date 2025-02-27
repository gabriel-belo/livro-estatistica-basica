import pandas as pd
import os

dados={'Casas por Quarteirao':[2, 2, 3, 10, 13, 14, 15, 15, 16, 16, 18, 18, 20, 21, 22, 23, 24, 25, 25, 26, 27, 29,
           29, 30, 32, 36, 42, 44, 45, 45, 46, 48, 52, 58, 59, 61, 61, 61, 65, 66, 66, 68, 75,
           78, 80, 89, 90, 92, 97]}

dados_df= pd.DataFrame(dados)

dados_df.to_csv('Casas.csv', index= False)


