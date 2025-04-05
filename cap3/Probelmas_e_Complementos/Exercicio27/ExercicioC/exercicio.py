import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados= pd.read_csv('../../data/exercicio27/Peso frangos.csv')

print(dados)

#sns.relplot(data= dados, x= 'Peso (gramas)', y='Frequência Absoluta', kind= 'line')
sns.histplot(dados, bins=6, kde=True, color="blue")
plt.show()
