import matplotlib.pyplot as plt
import numpy as np

dados= np.array([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0])

plt.hist(dados, color= '#0343DF')
plt.show()