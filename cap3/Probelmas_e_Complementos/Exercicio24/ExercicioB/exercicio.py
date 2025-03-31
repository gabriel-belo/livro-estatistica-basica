import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('../Consumo de Leite.csv')

plt.bar(dados['Consumo de Leite'], dados['Frequencia Relativa'])
plt.show()