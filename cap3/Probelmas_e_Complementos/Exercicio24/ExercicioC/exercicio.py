import pandas as pd
import re
dados= pd.read_csv('../Consumo de Leite.csv')

def calculoAmplitude(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    conta= int(numeros[1]) - int(numeros[0])
    return conta

dados['Amplitude']= dados['Consumo de Leite'].apply(calculoAmplitude)

#L = limite inferior da classe mediana
#N = soma total das frequências absolutas
#Fa = frequência acumulada da classe anterior à classe mediana
#fm= frequência absoluta da classe mediana
#h = amplitude da classe (largura do intervalo)
L= 1
h= 1
N= dados['Frequencia Acumulada'].iloc[3]
Fa= 20
fm= 70
mediana= round(L+(((N/2) - Fa)/ fm) * h, 2)
mediana2= dados['Frequencia Absoluta'].median()

#fórmula calcular  media ponderada com classes intervalares.
lista=[0.5, 1.5, 2.5, 4]
calculo=0
for elemento in lista:
    calculo= (lista * dados['Frequencia Absoluta'])
soma= calculo.sum()
media = soma / dados['Frequencia Acumulada'].iloc[3]
print(media)
print(mediana, mediana2)