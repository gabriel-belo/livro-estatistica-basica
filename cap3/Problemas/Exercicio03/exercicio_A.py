import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('../data/exercicio03/Casas.csv')
frequencia_absoluta= dados['Casas por Quarteirao'].value_counts()
frequencia_absoluta= pd.DataFrame(frequencia_absoluta)
frequencia_absoluta= frequencia_absoluta.reset_index()
frequencia_absoluta.columns= ['Total de casas', 'Frequencia absoluta']
frequencia_absoluta= frequencia_absoluta.sort_values(by="Total de casas")
frequencia_absoluta= frequencia_absoluta.reset_index(drop=True)
print(frequencia_absoluta)

plt.figure(figsize=(10,6))
plt.bar(frequencia_absoluta['Total de casas'], frequencia_absoluta['Frequencia absoluta'])
plt.xlabel('Total de casa por quarteirão')
plt.ylabel('Frequência absoluta')
plt.show()