#Compare e indique as diferenças existentes entre as distribuições das variáveis:
#Direito, Política e Estatística

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

direito=np.array([9.0] * 25)
estatistica= np.array([9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 9, 7, 8, 9, 4, 7, 7, 8, 10, 9, 9])
politica= np.array([9, 6.5, 9, 6,6.5, 6.5, 9, 6, 10, 9, 10, 6.5, 6, 10, 10, 9, 10, 6, 6, 6, 6.5, 6, 9, 6.5, 9], dtype= float)
dic={'Direito': direito, 'Estatistica': estatistica, 'Politica': politica}
dados_df= pd.DataFrame(data= dic)
dados_df.index= np.arange(1,26)
print(dados_df)

plt.subplot(2, 2, 1)
plt.hist(dados_df['Direito'])
plt.title('Direito')

plt.subplot(2, 2, 2)
plt.hist(dados_df['Estatistica'])
plt.title('Estatística')

plt.subplot(2, 2, 3)
plt.hist(dados_df['Politica'])
plt.title('Política')

plt.tight_layout()

plt.show()

#Resposta: As notas em Direito estão centradas em 9 sem ter tido uma variação maio, já as notas de
#Política e Estatística apresentam uma maior variação as notas em Política apresentam variação de 6 a 10
#e em Estatística de 4 a 10, porém com maior quantidade das notas entre 8 e 10.