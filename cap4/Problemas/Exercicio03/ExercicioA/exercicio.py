import pandas as pd

dic = {'Indivíduo': [i for i in range(1, 41, 1)],
        'X':[1, 3, 2, 3, 2, 2, 3, 1, 2, 3, 2, 3, 1, 2, 3, 4, 1, 2, 2, 2, 2, 3, 4, 1, 2, 3, 4, 1, 4, 3, 2, 1, 4, 2,
          4, 3, 1, 3, 2, 2],
        'Y':[6, 2, 4, 1, 4, 1, 3, 5, 2, 2, 5, 2, 6, 6, 2, 2, 5, 5, 1, 1, 4, 2, 1, 5, 4, 2, 1, 5, 4, 3, 2, 1, 1, 6,
             2, 1, 4, 2, 3, 5]
     }

dados = pd.DataFrame(dic)
dados.set_index('Indivíduo', inplace=True)

# Calculando as medianas
medianaX = dados['X'].median()
medianaY = dados['Y'].median()

print(f'Mediana de X: {medianaX}')
print(f'Mediana de Y: {medianaY}')

# Classificação: 'baixo' se valor <= mediana, senão 'alto'
dados['nivel_X'] = dados['X'].apply(lambda x: 'baixo' if x <= medianaX else 'alto')
dados['nivel_Y'] = dados['Y'].apply(lambda y: 'baixo' if y <= medianaY else 'alto')

# Tabela de frequência conjunta (tabela bidimensional)
#Cruza duas ou mais variáveis categóricas (ou colunas com valores classificados), e
#conta quantas vezes cada combinação aparece
#pd.crosstab(linhas, colunas)
tabela_conjunta = pd.crosstab(dados['nivel_X'], dados['nivel_Y'], margins=True)

tabela_conjunta.to_csv('Tabela Conjunta.csv')
print('\nDistribuição de frequência conjunta:')
print(tabela_conjunta)
