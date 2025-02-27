#Sorteando ao acasso um dos 25 funcionários, qual a probabilidade de que ele tenha
# obtido grau A em Metodologia
import numpy as np

dados_metodologia= np.array(['A', 'C', 'B', 'C', 'A', 'A', 'C', 'C', 'B', 'C', 'B', 'B', 'C',
                             'B', 'B', 'A', 'C', 'C', 'C', 'B', 'B', 'A', 'C', 'A', 'A'])

total_de_metodolofia= len(dados_metodologia)

valores_unicos, contagens = np.unique(dados_metodologia, return_counts=True)


proporcao_metodologia= []

for elemento in contagens:
    calculo= elemento / total_de_metodolofia
    proporcao_metodologia.append(calculo)

print(f"A probabilidade de tirar um funcionário que tenha obtido A em Metodologia é: {proporcao_metodologia[0]}")
