import pandas as pd

dados= pd.read_csv('../ExercicioA/Tabela Conjunta.csv', index_col=0)

print(dados)
print((dados.at['baixo','baixo']/dados.at['baixo', 'All'])*100)