import numpy as np
import matplotlib.pyplot as plt

taxas_medias= np.array([3.67, 1.82, 3.73, 4.10, 4.30, 1.28, 8.14, 2.43, 4.17, 5.36, 3.96, 6.54,
                        5.84, 7.35, 3.63, 2.93, 2.82, 8.45, 5.28, 5.41, 7.77, 4.65, 1.88, 2.12,
                        4.26, 2.78, 5.54, 0.90, 5.09, 4.07])

#a)Construa um histograma
plt.title('Taxas geométricas de incremento anual')
plt.hist(taxas_medias, range=(0.5, 9), color='green', bins=5)
plt.show()

#b)Construa um gráfico de dispersão unidimensional



plt.scatter(taxas_medias, [1] * len(taxas_medias), alpha=0.7)  # Define y=1 para manter os pontos alinhados
plt.show()