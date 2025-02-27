#Construa a distribuição de frequência da variavel Metodologia e faça um gráfico
#para indicar essa distribuição

import numpy as np
import matplotlib.pyplot as plt
import  pandas as pd

dados_metodologia= np.array(['A', 'C', 'B', 'C', 'A', 'A', 'C', 'C', 'B', 'C', 'B', 'B', 'C',
                             'B', 'B', 'A', 'C', 'C', 'C', 'B', 'B', 'A', 'C', 'A', 'A'])

total_de_metodolofia= len(dados_metodologia)

valores_unicos, contagens = np.unique(dados_metodologia, return_counts=True)

proporcao_metodologia= []

for elemento in contagens:
    calculo= elemento / total_de_metodolofia
    proporcao_metodologia.append(calculo)

porcentagem_metodologia=[]

for elemento in proporcao_metodologia:
    calculo= elemento * 100
    porcentagem_metodologia.append(calculo)

dic={'Classes metodologia': valores_unicos, 'Frequência': contagens, 'Proporção': proporcao_metodologia,
     'Porcentagem': porcentagem_metodologia}

metodologia_df= pd.DataFrame(dic)

print(metodologia_df)

plt.subplot(2,1,1)
plt.pie(metodologia_df['Porcentagem'], labels= metodologia_df['Classes metodologia'], autopct='%1.1f%%')

plt.subplot(2,1,2)
plt.hist(dados_metodologia)

plt.show()
