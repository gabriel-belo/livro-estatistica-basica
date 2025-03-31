import pandas as pd
import numpy as np

dados= pd.read_csv('../../data/exercicio25/Salario Anual.csv')

media= round(((dados["Pontos Médio"] * dados["Frequência"]).sum()) / dados['Frequência'].sum(), 2)
print(media)

variancia= ((dados["Pontos Médio"] - media) ** 2 * dados["Frequência"]).sum() / dados['Frequência'].sum()
print(variancia)

desvio_padrao= np.sqrt(variancia)
print(desvio_padrao)
