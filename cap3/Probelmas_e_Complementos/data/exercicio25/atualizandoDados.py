import pandas as pd
import re

dados= pd.read_csv('Salario Anual.csv')

#Exercicio A já tem as informações necessárias

#Exercicio B precisamos dos pontos médio e da soma total dos valores da frequencia absoluta
def calculoAmplitude(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= int(numeros[1]) - int(numeros[0])
    return conta

def calculoPontosMedio(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= (int(numeros[1]) + int(numeros[0])) / 2
    return conta


dados['Amplitude']= dados['Faixa salarial'].apply(calculoAmplitude)
dados['Pontos Médio']= dados['Faixa salarial'].apply(calculoPontosMedio)
print(dados['Amplitude'], dados['Pontos Médio'])

#Exercicio C tem todos os dados

#Exercicio D precisamos da frequencia acumulada
dados['Frequencia Acumulada']= dados['Frequência'].cumsum()
dados['Frequencia Relativa']= dados['Frequência'] / dados['Frequência'].sum()
dados['Distribuição Acumulada']= dados['Frequencia Relativa'].cumsum()


#Exercico E temos todos as informações
dados.to_csv('Salario Anual.csv', index= False)
