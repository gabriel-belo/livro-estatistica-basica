import numpy as np
import matplotlib.pyplot as plt

# Gerando dados aleatórios com distribuição normal
dados = np.random.randn(1000)

# Criando os histogramas
plt.figure(figsize=(10, 5))

# Histograma normal
plt.subplot(1, 2, 1)
plt.hist(dados, bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.title("Histograma Normal")

# Histograma normalizado (densidade de probabilidade)
plt.subplot(1, 2, 2)
plt.hist(dados, bins=20, density=True, color='red', alpha=0.7, edgecolor='black')
plt.xlabel("Valores")
plt.ylabel("Densidade de Probabilidade")
plt.title("Histograma Normalizado")

plt.show()
