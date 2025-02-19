#Construa um histograma, um ramp-e-folhas e um gráfico de dispersão unidimensional
# para o conjunto de dados 2(CD_Municiapl)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dic_pop_municipios={'Municipios':['São Paulo', 'Rio de Janeiro', 'Salvador', 'Belo Horizonte', 'Fortaleza', 'Brasília', 'Curitiba', 'Recife', 'Porto Alegre', 'Manaus',
            'Belém', 'Goiânia', 'Guarulhos', 'Campinas', 'São Gonçalo', 'Nova Iguaçu', 'São Luís', 'Maceió', 'Duque de Caxias', 'São Bernardo do Campo',
            'Natal', 'Teresina', 'Osasco', 'Santo André', 'Campo Grange', 'João Pessoa', 'Jaboatão', 'Contagem', 'São José dos Campos', 'Ribeirão Preto'],
            'Populacao':[998.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.8, 119.4, 116.0, 102.3, 101.8, 92.4, 84.7, 83.9, 80.2, 74.7, 72.7, 68.4,
                         66.8, 66.8, 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]}

pop_municipios_df= pd.DataFrame(dic_pop_municipios)
pop_municipios_df.index= np.arange(1, 31)
print(pop_municipios_df)

#Gráfico de dispersão
#plt.scatter(pop_municipios_df['Populacao'], [1] * len(pop_municipios_df['Populacao']))
#plt.show()

#Histograma
plt.title('Populações de Municípios do Brasil')
plt.xlabel('Populações(em 10.000 habitantes)')
plt.hist(pop_municipios_df['Populacao'], color='darkcyan', density=True, bins= 30, edgecolor="black")
plt.show()



