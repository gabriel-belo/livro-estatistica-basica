import pandas as pd

dados= pd.read_csv('../data/exercicio02/info_acoes.csv')

media= round(dados['Taxa de Juros'].sum()/ dados['Taxa de Juros'].count(),2)
mediana= dados['Taxa de Juros'].median()
dam= 0.03
print(f'Mediana: {mediana}')
print(f'Média: {media}')
print(f'Desvio Padrão: {dam}')


