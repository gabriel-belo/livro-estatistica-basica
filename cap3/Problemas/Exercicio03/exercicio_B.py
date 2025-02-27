import pandas as pd
import math

dados_df= pd.read_csv('../data/exercicio03/Casas.csv')


total= dados_df['Casas por Quarteirao'].sum()
media= math.ceil(total/50)

desvio_medio= (dados_df["Casas por Quarteirao"] - dados_df["Casas por Quarteirao"].mean()).abs().mean() # Calcula o desvio médio (MAD no Pandas).
desvio_padrao=dados_df["Casas por Quarteirao"].std(ddof=1) # Calcula o desvio padrão populacional.
#Se for amostral, use ddof=1.
print(f'Media: {media}')
print(f'Desvio médio: {desvio_medio}')
print(f'Descio Padrão: {desvio_padrao}')