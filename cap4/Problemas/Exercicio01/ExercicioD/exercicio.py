import numpy as np

dados= np.array([3, 7, 2])
total= dados.sum()

dados= np.round(dados / total, 2)
dados= dados * 100

print(dados)

#58% dos funcionários do interior tem ensino médio
