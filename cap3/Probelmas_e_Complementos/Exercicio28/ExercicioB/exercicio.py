import pandas as pd
import numpy as np

# Lê os dados
dados = pd.read_csv('../../data/exercicio28/Candidatos_a_vaga.csv')

# Calcula a média ponderada
media = (dados['Pontos Médio'] * dados['Frequencia']).sum() / dados['Frequencia'].sum()
print("Média:", media)

diferenca= round(media - 22, 2)

print(f"Resultado diferença 1: {diferenca}")

# Calcula o desvio padrão amostral ponderado
# Passo 1: (xi - media)^2 * fi
soma_dif_quadrada = ((dados['Pontos Médio'] - media)**2 * dados['Frequencia']).sum()

# Passo 2: divide pela soma das frequências - 1 (desvio padrão amostral)
dp_amostral = np.sqrt(soma_dif_quadrada / (dados['Frequencia'].sum() - 1))
print("Desvio padrão amostral:", dp_amostral)

# Calcula a margem de erro com 95% de confiança (2dp / √n)
erro = 2 * dp_amostral / np.sqrt(dados['Frequencia'].sum())
print("Margem de erro:", erro)

