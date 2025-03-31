import pandas as pd
import re
import numpy as np
dados= pd.read_csv('../Consumo de Leite.csv')

def calculoAmplitude(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= int(numeros[1]) - int(numeros[0])
    return conta

dados['Amplitude']= dados['Consumo de Leite'].apply(calculoAmplitude)

# Total de observações (N)
N = dados["Frequencia Absoluta"].sum()

# Média
#media = (dados["Pontos Médio"] * dados["Frequencia Absoluta"]).sum() / N

#fórmula calcular  media ponderada com classes intervalares.
lista=[0.5, 1.5, 2.5, 4]
dados['Pontos Médio']= lista
calculo=0
for elemento in lista:
    calculo= (lista * dados['Frequencia Absoluta'])
soma= calculo.sum()
media = soma / dados['Frequencia Acumulada'].iloc[3]

# Variância
variancia = ((dados["Pontos Médio"] - media) ** 2 * dados["Frequencia Absoluta"]).sum() / N

# Desvio padrão
desvio_padrao = np.sqrt(variancia)

print(f"variância: {variancia} e desvio padrão: {desvio_padrao}")