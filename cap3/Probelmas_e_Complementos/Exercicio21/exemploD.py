import numpy as np
#O que acontece com a media, mediana e desvio padrão de uma série de dados quando: subtrai-se à
dados=np.array([2, 4, 7, 3, 8, 9, 10 , 23, 12, 8, 5, 6 , 3, 2, 7])

media= np.mean(dados)
mediana= np.median(dados)
desvio_padrao= np.std(dados)

print(f'media: {media}  mediana: {mediana}  desvio padrão: {desvio_padrao}')

resultado= (dados - media) / desvio_padrao

media= np.mean(resultado)
mediana= np.median(resultado)
desvio_padrao= np.std(resultado)
print(f'media: {media}  mediana: {mediana}  desvio padrão: {desvio_padrao}')
