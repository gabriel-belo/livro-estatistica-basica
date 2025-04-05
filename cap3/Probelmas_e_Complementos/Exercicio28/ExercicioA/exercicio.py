import pandas as pd

dados= pd.read_csv('../../data/exercicio28/Candidatos_a_vaga.csv')
print(dados)
media= (dados['Pontos Médio'] * dados['Frequencia']).sum()/ dados['Frequencia'].sum()
print(media)
