import numpy as np

estatistica= np.array([9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 9, 7, 8, 9, 4, 7, 7, 8, 10, 9, 9])

estatistica= np.sort(estatistica)


print("Média:", np.mean(estatistica))
print("Mínimo:", np.min(estatistica))
print("Máximo:", np.max(estatistica))
print("Desvio Padrão:", np.std(estatistica))
print("Mediana:", np.median(estatistica))