import pandas as pd

dados= pd.read_csv('../data/exercicio26/Valores.csv')

#media
media= round((dados['Pontos Médio'] * dados['Frequência Absoluta']).sum() /dados['Frequência Absoluta'].sum(), 2)
print(media)

#moda
moda=dados.loc[dados['Frequência Absoluta'].idxmax(), 'Pontos Médio']
print(moda)

#mediana
#L = limite inferior da classe mediana
#N = soma total das frequências absolutas
#Fa = frequência acumulada da classe anterior à classe mediana
#fm= frequência absoluta da classe mediana
#h = amplitude da classe (largura do intervalo)
L= 6
h= 2
N= dados['Frequência Absoluta'].sum()
Fa= 40
fm= 60
mediana= round(L+(((N/2) - Fa)/ fm) * h, 2)
print(mediana)

#Variância
variancia=  ((dados["Pontos Médio"] - media) ** 2 * dados["Frequência Absoluta"]).sum() / dados['Frequência Absoluta'].sum()
print(variancia)

#1º quartil
#fórmula calcular  quartis
#Li = limite inferior da classe em que esta o quartil
#K= fração do qaurtil
#fi= frequencia acumulada final
#k.fi= buscar a posição do quartil
#Se fizermos total de valores dividido por 4 achamos a posição dp primeiro quartil
#Fa = frequência acumulada da classe anterior à classe do quatil
#fintervalo= frequência absolta do intervalo
#h = amplitude da classe (largura do intervalo)

Li= 4
k= 1/4
fi= dados['Frequência Absoluta'].sum()
Fa= 15
f= 40
h=2

q1= Li +((k*fi-Fa)/f) * h

print(q1)

print(dados)