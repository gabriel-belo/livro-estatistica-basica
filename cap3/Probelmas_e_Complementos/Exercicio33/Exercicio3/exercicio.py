import pandas as pd

dados= pd.read_csv('../../data/exercicio33/Invest em Educacao.csv')

media= dados['Investimento'].sum()/ len(dados['Investimento'])
print(media)