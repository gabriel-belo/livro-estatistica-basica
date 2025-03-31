import pandas as pd
import re

dados= pd.read_csv("Valores.csv")

dados['Frequência Absoluta']= dados['Frequência Relativa'] * 100

def calculoPontosMedio(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= (int(numeros[1]) + int(numeros[0])) / 2
    return conta

dados['Pontos Médio']= dados['Faixa'].apply(calculoPontosMedio)

dados.to_csv('Valores.csv', index= False)