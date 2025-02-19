import numpy as np
import matplotlib.pyplot as plt

erros_de_impressao= ([8, 11, 8, 12, 14, 13, 11, 14, 14, 15, 6, 10, 14, 19, 6, 12, 7, 5, 8, 8,
                      10, 16, 10, 12, 12, 8, 11, 6, 7, 12, 7, 10, 14, 5, 12, 7, 9, 12, 11, 9,
                      14, 8, 14, 8, 12, 10, 12, 22, 7, 15])


#a) represente os dados graficamente
dias= len(erros_de_impressao)

plt.title('Erros de impressão da 1º página do jornal')
#plt.xlabel('Dias')
#plt.ylabel('Erros de impressão por dia')
#plt.plot(np.arange(1,dias+1), erros_de_impressao, color='blue')
#plt.show()

#b)Fazer um histograma e um ramo-e-folhas
numeros_unicos = np.unique(erros_de_impressao)
quantidade_numeros_unicos= len(numeros_unicos)
#plt.hist(erros_de_impressao,bins=quantidade_numeros_unicos, edgecolor="black")
#plt.show()

#Gráfico de dispersão unidimensional
plt.stem(erros_de_impressao, linefmt=None, markerfmt=None, basefmt=None)
plt.show()

