import numpy as np

#1 se for capital, 0 se for interior ou outra0,
dados= np.array([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0])
media = np.mean(dados)
moda = np.median(dados)
mediana = np.median(dados)

variancia= round(((dados - media)**2).sum()/ (len(dados) - 1),2)
variancia2= np.var(dados)
print(variancia, variancia2, media)