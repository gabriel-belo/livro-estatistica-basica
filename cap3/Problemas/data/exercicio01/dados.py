import pandas as pd
import os

# Criando um DataFrame
dados = {'Erros': [0, 1, 2, 3, 4], 'Frequencia': [25, 20, 3, 1, 1]}

erros_impressao = pd.DataFrame(dados)

# Criando diretório "data" caso não exista
#os.makedirs("data", exist_ok=True)

# Salvando como CSV
erros_impressao.to_csv("erros_impressao.csv", index=False)