import pandas as pd

dic={
     'v\y':['Capital', 'Interior', 'Outra', 'Total'],
    'Ensino Fundamental': [4, 3, 5, 12],
    'Ensino Médio': [5, 7, 6, 18],
    'Superior': [2, 2, 2, 6],
    'Total': [11, 12, 13, 36]
}

dados= pd.DataFrame(dic)

# Retira os índices numéricos para fazer a busca pela coluna V
dados.set_index('v\y', inplace=True)

print(dados)

# Soma total geral (última célula da tabela)
total_geral = dados.loc['Total', 'Total']

# Criar nova tabela com frequência relativa, mantendo estrutura
frequencia_relativa = dados.applymap(lambda x: round(x / total_geral, 2))

print(frequencia_relativa)

frequencia_relativa.to_csv('Dados Frequencia relativa.csv', index= False)