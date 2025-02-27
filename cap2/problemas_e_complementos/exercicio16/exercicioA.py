#Construa a distribuição de frequência para a varivável idade e faça o gráfico da
# porcentagem acumulada
import pandas as pd
import matplotlib.pyplot as plt


idades=[26, 32, 36, 20, 40, 28, 41, 43, 34, 23, 33, 27, 37, 44, 30, 38, 31, 39, 25, 37, 30, 34,
        41, 26, 32, 35, 46, 29, 40, 35, 31, 36, 43, 33, 48, 42]


#Criamos bins (range(20, 50, 2)) para definir as faixas de idade com amplitude 2.
bins = list(range(20, 50, 2))  # [20, 22, 24, ..., 48]

#Usamos pd.cut() para classificar as idades nos intervalos.
idades_categorizadas = pd.cut(idades, bins=bins, right=False)  # right=False exclui o limite superior
print(idades_categorizadas)


frequencias = idades_categorizadas.value_counts().sort_index()  # Ordenar pela ordem correta

# Criar um DataFrame com os resultados
idades_df = pd.DataFrame({
    "Intervalo de Idade": frequencias.index.astype(str),  # Converter para string
    "Frequência": frequencias.values
})

idades_df['Frequência acumulada']= idades_df['Frequência'].cumsum()

def funcao_porcentagem(idade):
    return round(idade / 36 * 100, 2)

idades_df['Porcentagem']= idades_df['Frequência'].apply(funcao_porcentagem)


def funcao_porcentagem_acumulada(idade):
    return round(idade/ 36 * 100, 2)

idades_df['Porcentagem Acumulada']= idades_df['Frequência acumulada'].apply(funcao_porcentagem_acumulada)

print(idades_df)


plt.figure(figsize=(12, 8))
plt.plot(idades_df["Intervalo de Idade"], idades_df["Porcentagem Acumulada"], marker="o", linestyle="-", color="b", label="Porcentagem Acumulada")
plt.xlabel("Intervalo de Idade")
plt.ylabel("Porcentagem Acumulada (%)")
plt.title("Gráfico de Porcentagem Acumulada")
plt.ylim(0, 110)  # Mantém o eixo Y entre 0 e 100%
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()

print(idades_df[['Intervalo de Idade',  'Frequência acumulada']])