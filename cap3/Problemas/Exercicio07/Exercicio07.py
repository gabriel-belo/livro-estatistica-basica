import pandas as pd

dados = pd.read_csv('../data/exercicio03/Casas.csv')

min_valor = dados['Casas por Quarteirao'].min()
max_valor = dados['Casas por Quarteirao'].max()

def CalcularQuantis(dados, quantil):
    valores = dados['Casas por Quarteirao'].sort_values().reset_index(drop=True)  # Ordenar os dados

    if quantil == 25:
        posicao = (len(valores) + 1) / 4
    elif quantil == 50:
        posicao = 2 * (len(valores) + 1) / 4
    elif quantil == 75:
        posicao = 3 * (len(valores) + 1) / 4
    else:
        return 'Valor indisponível'

    # Se a posição for um número inteiro, retorna diretamente
    if posicao.is_integer():
        return valores.iloc[int(posicao) - 1]  # Índice começa em 0, então ajustamos com -1

    # Se for um número decimal, faz a média dos dois valores adjacentes
    else:
        posicao_inferior = int(posicao) - 1
        posicao_superior = posicao_inferior + 1
        media = (valores.iloc[posicao_inferior] + valores.iloc[posicao_superior]) / 2
        return media

# Exemplo de uso:
quantil_25 = CalcularQuantis(dados, 25)
quantil_50 = CalcularQuantis(dados, 50)
quantil_75 = CalcularQuantis(dados, 75)

print("Quantil 25:", quantil_25)
print("Quantil 50:", quantil_50)
print("Quantil 75:", quantil_75)


#distância interquarti, dq=q3- q1

dist_interquartil= quantil_75 - quantil_25
print(dist_interquartil)


