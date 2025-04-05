import pandas as pd

dados= pd.read_csv('../../data/exercicio27/Peso frangos.csv')
print(dados)

media= (dados['Pontos Médio'] * dados['Frequência Absoluta']).sum()/ dados['Frequência Absoluta'].sum()

variancia= ((dados["Pontos Médio"] - media) ** 2 * dados["Frequência Absoluta"]).sum() / dados['Frequência Absoluta'].sum()
print(variancia)