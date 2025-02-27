#Se, em vez de um, sorteássemos dois, qual a probabilidade de que ambostivessem tido A em
# Metodologia é maior ou menor do que a resposta dada em (e)
import numpy as np

dados_metodologia= np.array(['A', 'C', 'B', 'C', 'A', 'A', 'C', 'C', 'B', 'C', 'B', 'B', 'C',
                             'B', 'B', 'A', 'C', 'C', 'C', 'B', 'B', 'A', 'C', 'A', 'A'])

total_de_metodolofia= len(dados_metodologia)

valores_unicos, contagens = np.unique(dados_metodologia, return_counts=True)


proporcao_metodologia= []


funcionario1= contagens[0] / total_de_metodolofia

funcionario2= (contagens[0] -1)/(total_de_metodolofia - 1)

print(funcionario1, funcionario2)

resultado_probabilidade= funcionario1 * funcionario2

print(f"A chance de ambos terem A em Metodologia é: {resultado_probabilidade}")