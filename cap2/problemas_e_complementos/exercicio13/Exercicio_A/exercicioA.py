import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
dic={'Classe de salarios': ['4  ⊢ 6', '6  ⊢ 8', '8  ⊢ 10', '10  ⊢ 12', '12  ⊢ 14', '14  ⊢ 16', '16  ⊢ 18', '18  ⊢ 20','20  ⊢ 22', '22  ⊢ 24'],
     'Frequencia': [4, 6, 8, 4, 5, 3, 3, 2, 0, 1]}

classe_salarios_df= pd.DataFrame(dic)
classe_salarios_df.index= np.arange(1, 11)
print(classe_salarios_df)

def extrair_ponto_medio(intervalo):
    partes = intervalo.split(' ⊢ ')  # Separar os limites
    return (int(partes[0]) + int(partes[1])) / 2  # Média dos limites

# Criando coluna de pontos médios
classe_salarios_df["Ponto Médio"] = classe_salarios_df["Classe de salarios"].apply(extrair_ponto_medio)

# Criando um array de valores baseados na frequência
valores_expandidos = np.repeat(classe_salarios_df["Ponto Médio"], classe_salarios_df["Frequencia"])

# Plotando o histograma com KDE (alisado)
plt.figure(figsize=(8, 5))
sns.histplot(valores_expandidos, bins=10, kde=True, color="blue", stat="density", alpha=0.5)

# Personalização do gráfico
plt.xlabel("Faixa Salarial")
plt.ylabel("Densidade")
plt.title("Histograma Alisado das Faixas Salariais")
plt.grid(True)

plt.show()
