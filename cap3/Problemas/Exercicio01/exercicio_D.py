import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dados= pd.read_csv('../data/exercicio01/erros_impressao.csv')

sns.histplot(dados, kde=True, color="blue", stat="density", alpha=0.5)

plt.ylabel('Frequencia')
plt.xlabel('Erros')
plt.show()