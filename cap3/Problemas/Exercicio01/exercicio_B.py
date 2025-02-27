#Qual o número mediano
import pandas as pd

dados= pd.read_csv('../data/exercicio01/erros_impressao.csv')

mediana= dados['Frequencia'].median()

print(mediana)

