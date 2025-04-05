import  pandas as pd
import numpy as np

dados= pd.read_csv('../../data/exercicio33/Invest em Educacao.csv')

media= 15.9


variancia= ((dados['Investimento'] - media) **2).sum()/ (len(dados['Investimento']) -1)
dp= round(np.sqrt(variancia), 2)

#Eliminar o conjunto de dados que forem superiores à media inicial mais duas vezes o dp, ou inferiores a media
#inicial  menos duas vezes o dp

superior= media + 2 * dp
inferior= media - 2 * dp
print(superior, inferior)

dados_validos= dados.query(' Investimento <= @superior and Investimento >= @inferior')

print(dados_validos)