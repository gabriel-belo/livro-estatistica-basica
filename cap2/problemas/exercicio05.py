import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Usando os resultados do problema 2 e a tabela 2.3:
#a)construa um histograma para a variável idade
# criando tabela
list_idade= np.random.randint(20, 50, 36)

idade_df= pd.DataFrame(list_idade, columns=['Idade'])
print(idade_df)

plt.hist(idade_df['Idade'])
plt.show()

