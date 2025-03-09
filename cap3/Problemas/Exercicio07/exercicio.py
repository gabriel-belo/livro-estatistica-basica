#forma de resolução com a utilização de métodos
import pandas as pd

# Carregar os dados
dados = pd.read_csv('../data/exercicio03/Casas.csv')

# Selecionar a coluna que queremos analisar
coluna = 'Casas por Quarteirao'
valores = dados[coluna]

#valores máximo e mínimo
max= valores.max()
min= valores.min()

print(max, min)

# Calcular os quartis
Q1 = valores.quantile(0.25)  # Primeiro quartil (25%)
Q2 = valores.quantile(0.50)  # Segundo quartil (50%)
Q3 = valores.quantile(0.75)  # Terceiro quartil (75%)

# Calcular o IQR (Intervalo Interquartil)
IQR = Q3 - Q1

# Calcular os limites inferior e superior para outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar os outliers
outliers = valores[(valores < limite_inferior) | (valores > limite_superior)]


# Calcular quartis e extremos
x1 = valores.min()  # Valor mínimo
xn = valores.max()  # Valor máximo
q1 = valores.quantile(0.25)  # Primeiro quartil (25%)
q2 = valores.quantile(0.50)  # Mediana (50%)
q3 = valores.quantile(0.75)  # Terceiro quartil (75%)

# Calcular as diferenças
diff1 = abs((q2 - x1) - (xn - q2))  # Deve ser ≈ 0
diff2 = abs((q2 - q1) - (q3 - q2))  # Deve ser ≈ 0
diff3 = abs((q2 - x1) - (xn - q3))  # Deve ser ≈ 0

# Definir uma tolerância para considerar os valores próximos
tolerancia = 0.1 * (xn - x1)  # 10% da amplitude total dos dados

# Verificar se as diferenças estão dentro da tolerância
simetria1 = diff1 < tolerancia
simetria2 = diff2 < tolerancia
simetria3 = diff3 < tolerancia

# Exibir os resultados
print(f'Q1 (25%): {Q1}')
print(f'Q3 (75%): {Q3}')
print(f'IQR: {IQR}')
print(f'Limite inferior: {limite_inferior}')
print(f'Limite superior: {limite_superior}')
print(f'Outliers encontrados:\n{outliers}')
print(f'Diferença 1 (q2 - x1 ≈ xn - q2): {diff1} -> {"OK" if simetria1 else "Assimétrico"}')
print(f'Diferença 2 (q2 - q1 ≈ q3 - q2): {diff2} -> {"OK" if simetria2 else "Assimétrico"}')
print(f'Diferença 3 (q2 - x1 ≈ xn - q3): {diff3} -> {"OK" if simetria3 else "Assimétrico"}')

# Conclusão geral
if simetria1 and simetria2 and simetria3:
    print("A distribuição parece ser simétrica. ✅")
else:
    print("A distribuição pode estar assimétrica. ⚠️")


