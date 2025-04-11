import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


taxas_medias= np.array([3.67, 1.82, 3.73, 4.10, 4.30, 1.28, 8.14, 2.43, 4.17, 5.36, 3.96, 6.54,
                        5.84, 7.35, 3.63, 2.93, 2.82, 8.45, 5.28, 5.41, 7.77, 4.65, 1.88, 2.12,
                        4.26, 2.78, 5.54, 0.90, 5.09, 4.07])

sns.boxplot(x= taxas_medias)
plt.title('Taxas geométricas de incremento anual')
plt.show()