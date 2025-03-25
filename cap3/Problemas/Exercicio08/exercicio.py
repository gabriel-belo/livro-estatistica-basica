import pandas as pd

dados= pd.read_csv('../data/exercicio08/Idade_NumFilhos.csv')

print(dados)

#valores da coluna idade
idades_df= dados['Idade']

idade_max= idades_df.max()
idade_min= idades_df.min()
idade_Q1= idades_df.quantile(0.25)
idade_Q2= idades_df.quantile(0.50)
idade_Q3= idades_df.quantile(0.75)

idade_IQR= idade_Q3- idade_Q1

#limite inferior
limite_inferior= idade_Q1 - 1.5 * idade_IQR

#limite superior
limite_superior= idade_Q1 + 1.5 * idade_IQR

print(idade_max, idade_min, idade_Q1, idade_Q2, idade_Q3, idade_IQR, limite_inferior, limite_superior)

#valores da coluna Número de filhos
num_filhos_df= dados['Numero de filhos']

num_filhos_max=  num_filhos_df.max()
num_filhos_min= num_filhos_df.min()
num_filhos_Q1= num_filhos_df.quantile(0.25)
num_filhos_Q2= num_filhos_df.quantile(0.50)
num_filhos_Q3= num_filhos_df.quantile(0.75)

num_filhos_IQR= num_filhos_Q3 - num_filhos_Q1

#limite inferior
limite_inferior2= num_filhos_Q1 - 1.5 * num_filhos_IQR

#limite superior
limite_superior2= num_filhos_Q1 + 1.5 * num_filhos_IQR

print(num_filhos_max, num_filhos_min, num_filhos_Q1, num_filhos_Q2, num_filhos_Q3, num_filhos_IQR, limite_inferior2, limite_superior2)