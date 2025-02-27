import numpy as np
import matplotlib.pyplot as plt

redacao= np.array([8.6, 7, 8, 8.6, 8, 8.5, 8.2, 7.5, 9.4, 7.9, 8.6, 8.3, 7, 8.6, 8.6, 9.5, 6.3,
                   7.6, 6.8, 7.5, 7.7, 8.7, 7.3, 8.5, 7], dtype= float)
plt.title('Notas em Redação')
plt.xlabel('Notas')
plt.hist(redacao)

plt.show()
