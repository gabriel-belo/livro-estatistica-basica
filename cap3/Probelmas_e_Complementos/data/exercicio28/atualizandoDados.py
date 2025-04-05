import pandas as pd
import re

dados= pd.read_csv('Candidatos_a_vaga.csv')

def calculoAmplitude(intervalo):
    numeros= re.findall(r'\d+', intervalo)
    calculo= int(numeros[1]) - int(numeros[0])
    return calculo

dados['Amplitude']= dados['Idade'].apply(calculoAmplitude)


def calculoPontosMedio(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= (int(numeros[1]) + int(numeros[0])) / 2
    return conta

dados['Pontos Médio']= dados['Idade'].apply(calculoPontosMedio)



dados['Densidade Frequencia']= round(dados['Frequencia']/ dados['Amplitude'], 2)

dados.to_csv('Candidatos_a_vaga.csv', index= False)