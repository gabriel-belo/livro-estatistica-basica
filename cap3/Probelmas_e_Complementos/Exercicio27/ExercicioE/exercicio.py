import pandas as pd
import numpy as np
dados= pd.read_csv('../../data/exercicio27/Peso frangos.csv')
print(dados)

media= (dados['Pontos Médio'] * dados['Frequência Absoluta']).sum()/ dados['Frequência Absoluta'].sum()

variancia= ((dados["Pontos Médio"] - media) ** 2 * dados["Frequência Absoluta"]).sum() / dados['Frequência Absoluta'].sum()

desvio_padrao= np.sqrt(variancia)

#Peso inferior a dois desvios padrão, receber ração reforçada
dois_desvPadrao=  desvio_padrao * 2
valor= round(media - dois_desvPadrao, 2)

#Frangos para reprodução
valor2= round(media + (desvio_padrao * 1.5),2)
print(valor, valor2)

#Parte dos frangos da última classe irão receber ração reforçada
#Todos os frangos da última classe seram utilizados para reprodução
