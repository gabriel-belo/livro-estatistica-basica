import pandas as pd

dados= pd.read_csv('../data/exercicio03/Casas.csv')

print(dados)

decil_10= dados['Casas por Quarteirao'].quantile(0.10)
Q1= dados['Casas por Quarteirao'].quantile(0.25)
Q2= dados['Casas por Quarteirao'].quantile(0.50)
Q3= dados['Casas por Quarteirao'].quantile(0.75)
decil_90= dados['Casas por Quarteirao'].quantile(0.90)

print(decil_10, Q1, Q2, Q3, decil_90)
