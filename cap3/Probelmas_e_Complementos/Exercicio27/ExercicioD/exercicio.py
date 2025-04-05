import pandas as pd

dados= pd.read_csv('../../data/exercicio27/Peso frangos.csv')

#print(dados)
dados['Frequência Relativa']= dados['Frequência Absoluta'] / dados['Frequência Absoluta'].sum()
print(dados)

#Pk=L + (((N⋅k/ 100)−Fa) / f)×h

#Onde:
#Pk = Percentil desejado(exemplo: P25 para o 1º quartil).
#L = Limite inferior da classe que contém o percentil.
#N = Total de observações(soma das frequências absolutas).
#k = Percentil desejado(por exemplo, 25 para P25)
#Fa= Frequência acumulada antes da classe que contém o percentil.
#f = Frequência absoluta da classe que contém o percentil.
#h = Amplitude da classe.
L= 980
N= dados['Frequência Absoluta'].sum()
k= 20
Fa= dados['Frequência Acumulada'].iloc[0]
f= dados['Frequência Absoluta'].iloc[1]
h= 20
P20= L + (((N*k/ 100)-Fa) / f)*h
print(P20)

#20% mais leves são os 60 da primeira classe inteira e 140 galos da segunda classe
#Os frangos de 30% a 50% estão 20 na segunda classe e 280 da terceira classe
#Os frangos entre 50% a 80% estão nos 260 da quart classe e mais 40 da quinta classe
#Os últimos 20% etão nos 120 restantes da quinta classe e 80 da sexta classe

print(dados['Frequência Absoluta'].sum()* 50/ 100)
print(dados['Frequência Absoluta'].sum()* 80/ 100)
