import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('../data/exercicio03/Casas.csv')

print(dados)

plt.boxplot(dados['Casas por Quarteirao'])
plt.show()