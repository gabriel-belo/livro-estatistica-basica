import pandas as pd
dic1={('Corretora A', 'Coluna 1'): [45, 62, 38, 55, 54, 65],
     ('Corretora A', 'Coluna 2'):[60, 55, 48, 56, 59, 55],
     ('Corretora A', 'Coluna 3'):[54, 70, 64, 55, 48, 60]
    }

dados1= pd.DataFrame(dic1)

dic2={('Corretora B', 'Coluna 1'): [57, 50, 59, 61, 57, 55, 59],
      ('Corretora B', 'Coluna 2'): [55, 52, 55, 52, 57, 58, 51],
      ('Corretora B', 'Coluna 3'): [58, 59, 56, 53, 50, 54, 56]}

dados2= pd.DataFrame(dic2)

print(dados1)

print(dados2)

dados1.to_csv('Info Corretora A.csv')
dados2.to_csv('Info Corretora B.csv')
