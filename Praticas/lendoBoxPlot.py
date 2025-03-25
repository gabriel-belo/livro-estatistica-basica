import matplotlib.pyplot as plt
import numpy as np

# Distribuição simétrica
simetrica = np.random.normal(loc=50, scale=10, size=100)

# Distribuição assimétrica positiva (assimetria à direita)
assimetrica_pos = np.random.exponential(scale=10, size=100)

# Distribuição assimétrica negativa (assimetria à esquerda)
assimetrica_neg = 100 - np.random.exponential(scale=10, size=100)

# Criando o boxplot
plt.boxplot([simetrica, assimetrica_pos, assimetrica_neg], patch_artist=True,
            boxprops=dict(facecolor='lightblue'),
            medianprops=dict(color='red'))

# Títulos e eixos
plt.title('Comparando Distribuições Simétrica e Assimétricas')
plt.ylabel('Valores')
plt.xticks([1, 2, 3], ['Simétrica', 'Assimétrica +', 'Assimétrica -'])

plt.show()
