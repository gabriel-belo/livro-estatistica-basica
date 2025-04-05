import pandas as pd
import re
dados= pd.read_csv('Peso frangos.csv')
print(dados)

def calculoPontosMedio(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta = (int(numeros[1]) + int(numeros[0])) / 2
    return conta

dados['Pontos Médio']= dados['Peso (gramas)'].apply(calculoPontosMedio)

dados['Frequência Acumulada']= dados['Frequência Absoluta'].cumsum()

dados.to_csv('Peso frangos.csv', index= False)