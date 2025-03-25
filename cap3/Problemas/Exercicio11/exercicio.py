#duvida neste exercicio
import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('../data/exercicio11/Orçamento_Companhia.csv')

print(dados)
plt.boxplot(dados['Frequência absoluta'])
plt.show()