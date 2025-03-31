import numpy as np
from scipy import stats
dados= np.array([18, 21, 21, 24, 27, 27, 30, 35, 42, 55])

media= np.mean(dados)
mediana= np.median(dados)
moda= stats.mode(dados)
print(media, mediana, moda)