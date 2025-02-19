import seaborn as sns
import matplotlib.pyplot as plt
import  numpy as np

dados = np.random.randn(1000)
# Criando um histograma normalizado com uma curva de densidade
sns.histplot(dados, bins=20, kde=True, color='purple', stat="density")

plt.xlabel("Valores")
plt.ylabel("Densidade de Probabilidade")
plt.title("Histograma Normalizado com Curva KDE")
plt.show()
