import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados= pd.read_csv('../../data/exercicio25/Salario Anual.csv')


sns.relplot( data= dados, kind="line", x=dados["Faixa salarial"], y=dados["Frequência"])
plt.show()
