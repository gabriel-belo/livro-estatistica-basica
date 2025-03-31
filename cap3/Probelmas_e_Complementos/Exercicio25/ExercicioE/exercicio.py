import pandas as pd

dados= pd.read_csv("../../data/exercicio25/Salario Anual.csv")

salario_minimo= 16400
riqueza_total= ((dados['Pontos Médio'] *  salario_minimo) * dados['Frequência']).sum()


print(riqueza_total)
