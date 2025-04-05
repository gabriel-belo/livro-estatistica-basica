import pandas as pd

dic={
    'Idade': ['[18 20)', '[20 22)', '[22 26)', '[26 30)', '[30 36)'],
    'Frequencia':[18, 12, 10, 8, 2],
    'Porcentagem':[36, 24, 20, 16, 4]
}

dados= pd.DataFrame(dic)

dados.to_csv('Candidatos_a_vaga.csv', index=False)