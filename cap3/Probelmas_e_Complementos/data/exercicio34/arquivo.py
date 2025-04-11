import pandas as pd

dic={
    'Repartição': ['A', 'B'],
    'Mínimo': [18, 18],
    '1ºQuartil': [27, 23],
    'Mediana': [33, 32],
    'Média': [33, 33],
    '3ºQuartil': [39, 42],
    'Máximo': [48, 48],
    'dp': [5, 10]
}

dados= pd.DataFrame(dic)

dados.to_csv('Idade Funcionarios.csv', index=False)