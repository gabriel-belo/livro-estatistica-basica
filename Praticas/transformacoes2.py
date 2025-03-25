import numpy as np
import matplotlib.pyplot as plt

# Simulação de dados assimétricos à esquerda (cauda à esquerda)
np.random.seed(42)

dados = 10 - np.random.exponential(scale=2, size=1000)
dados = dados[dados > 0]  # Mantém valores positivos

plt.subplot(1, 2, 1)
plt.hist(dados, bins=30, color='skyblue', edgecolor='black')
plt.title("ANTES - Assimetria à Esquerda (Cauda à Esquerda)")
plt.xlabel("Tempo de Resposta")
plt.ylabel("Frequência")


# Transformação com p = -1 (inverso dos valores)
dados_transformados = -dados**-1  # Potência negativa

plt.subplot(1, 2, 2)
plt.hist(dados_transformados, bins=30, color='lightgreen', edgecolor='black')
plt.title("DEPOIS - Mais Simétrico Após Transformação (p < 0)")
plt.xlabel("Valor Transformado")
plt.ylabel("Frequência")
plt.show()
