import math
#dados
lista = [1, 2, 3, 4, 10, 20, 50, 100]
lista_resultados=[]
#se p > 0, a cauda é comprimida
for x in lista:
    x_transf = x**0.5
    lista_resultados.append(round(x_transf,1))

print(lista_resultados)
#[1.0, 1.41, 1.73, 2.0, 3.16, 4.47, 7.07, 10.0]

#se p = 0, Ainda mais comprimido, ajuda muito a controlar caudas longas.
lista_resultados=[]
for x in lista:
    x_transf =  math.log(x)
    lista_resultados.append(round( x_transf,1))

print(lista_resultados)
#[0.0, 0.69, 1.09, 1.39, 2.30, 3.00, 3.91, 4.61]

#Se p < 0,Agora você inverteu os valores e mudou o sentido da distribuição.
lista_resultados=[]
for x in lista:
    x_transf = -x**-1
    lista_resultados.append(round(x_transf, 1))

print(lista_resultados)
#[-1.0, -0.5, -0.33, -0.25, -0.1, -0.05, -0.02, -0.01]
