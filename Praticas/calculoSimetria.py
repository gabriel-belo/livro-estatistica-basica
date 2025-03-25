#dificuldade com este cálculo
import numpy as np

dados=[0.5, 2.3, 4, 6.4, 8, 9.8, 12, 13.5, 15.3]

def calculoSimetria(dados, lista_resultados, Q2, n, i, y):
    lista_calculo=[]

    if  len(lista_resultados) == len(dados):
        return lista_resultados

    ui= Q2 - dados[y]
    vi= (n + 1 - i)- Q2

    lista_calculo.append(ui)
    lista_calculo.append(vi)
    lista_resultados.append(lista_calculo)

    return calculoSimetria(dados, lista_resultados, Q2, n, i, y + 1)

Q2= np.percentile(dados, 50)
lisa_resultados=[]
n= len(dados) -1
i= (len(dados) + 1)/2
print(calculoSimetria(dados,lisa_resultados, Q2, n, i, y=0))

