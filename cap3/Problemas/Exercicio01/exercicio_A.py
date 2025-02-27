#Qual o número médio de erros por página
import pandas as pd
import numpy as np
dados= pd.read_csv('../data/exercicio01/erros_impressao.csv')

#soma de todos os valores
soma_valores= np.array([dados["Frequencia"] * dados['Erros']])
soma_valores= soma_valores.sum()

#Numero total de elemento
total_elementos= dados["Frequencia"].sum()


media= soma_valores/ total_elementos


print(dados)
print(f'A média de erros por página é: {media}')
