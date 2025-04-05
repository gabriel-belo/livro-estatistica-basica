import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

dados= pd.read_csv('../../data/exercicio28/Candidatos_a_vaga.csv')


ax=sns.barplot(data= dados, x= 'Idade', y= 'Frequencia', color= 'skyblue', edgecolor= 'black')

# Ajusta o eixo y para mostrar apenas inteiros
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 1),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

plt.show()