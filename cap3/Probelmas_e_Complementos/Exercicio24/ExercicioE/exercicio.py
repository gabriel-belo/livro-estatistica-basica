import pandas as pd
import re
dados= pd.read_csv('../Consumo de Leite.csv')

def calculoAmplitude(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= int(numeros[1]) - int(numeros[0])
    return conta

dados['Amplitude']= dados['Consumo de Leite'].apply(calculoAmplitude)

#fórmula calcular  quartis
#Li = limite inferior da classe em que esta o quartil
#K= fração do qaurtil
#fi= frequencia acumulada final
#k.fi= buscar a posição do quartil
#Se fizermos total de valores dividido por 4 achamos a posição dp primeiro quartil
#Fa = frequência acumulada da classe anterior à classe do quatil
#fintervalo= frequência absolta do intervalo
#h = amplitude da classe (largura do intervalo)

Li= 1
k= 1/4
fi= dados['Frequencia Acumulada'].iloc[3]
Fa= 20
f= 50
h=1

q1= Li +((k*fi-Fa)/f) * h


print(q1)