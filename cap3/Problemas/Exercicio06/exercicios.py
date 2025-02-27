import pandas as pd
import numpy as np
dados_df= pd.read_csv('../data/exercicio06/Filhos_por_familia.csv')

# Expandindo os dados de acordo com a frequência
dados_expandido = np.repeat(dados_df["Número de filhos"], dados_df["Frequencia de familias"])

# Calculando a mediana
mediana = np.median(dados_expandido)

moda= 2

print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
