import pandas as pd

dic = {
    'v\\y': ['Capital', 'Interior', 'Outra', 'Total'],
    'Ensino Fundamental': [4, 3, 5, 12],
    'Ensino Médio': [5, 7, 6, 18],
    'Superior': [2, 2, 2, 6],
    'Total': [11, 12, 13, 36]
}

# Criando o DataFrame e definindo 'v\y' como índice
df = pd.DataFrame(dic)
df.set_index('v\\y', inplace=True)

print(df)

# Soma total geral (última célula da tabela)
total_geral = df.loc['Total', 'Total']

# Criar nova tabela com frequência relativa, mantendo estrutura
frequencia_relativa = df.applymap(lambda x: round(x / total_geral, 2))

print(frequencia_relativa)

#df.sum(axis=1) → soma os valores de cada linha.
#.div(..., axis=0) → divide cada linha pelos seus respectivos totais.
#df.drop(columns='Total') -> retira a coluna total
frequencia_relativa_linha= (df.drop(columns='Total').div(df['Total'], axis=1).round(2))*100

print(frequencia_relativa_linha)