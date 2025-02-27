#Qual é o desvio padrão
import pandas as pd

dados= pd.read_csv('../data/exercicio01/erros_impressao.csv')

media=0.66

dados['modulo']= dados['Erros']- media
dm= dados['modulo'].sum()
dm= dm/50
print(dm)