import numpy as np
import pandas as pd
from statsmodels import robust


dados= pd.read_csv('../data/exercicio42/CD Brasil. csv')
#1. Forma com statsmodels
mad1 = robust.mad(dados['População'])
print(mad1)

#2. Forma com numpy
mediana= np.median(dados['População'])
desvio= np.abs(dados['População'] - mediana)
dam2= np.median(desvio)

print(dam2)