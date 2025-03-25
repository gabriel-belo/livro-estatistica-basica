import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dados= pd.read_csv('../cap3/Problemas/data/exercicio03/Casas.csv')

q1 = np.percentile(dados['Casas por Quarteirao'], 25)
q2 = np.percentile(dados['Casas por Quarteirao'], 50)
q3 = np.percentile(dados['Casas por Quarteirao'], 75)

plt.hist(dados, bins=30, edgecolor='black')
plt.axvline(q1, color='orange', linestyle='--', label='Q1')
plt.axvline(q2, color='green', linestyle='-', label='Mediana (Q2)')
plt.axvline(q3, color='red', linestyle='--', label='Q3')

plt.title('Histograma com Quartis - Simetria')
plt.legend()
plt.show()
