import pandas as pd

dados= pd.read_csv('../ExercicioA/Tabela Conjunta.csv', index_col=0)

print(dados)
print((dados.loc['baixo', 'baixo']/ dados.loc['All', 'All']) * 100)
