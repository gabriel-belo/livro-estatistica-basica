#Salário em 1979(em francos suíços) para mecânicos em 30 cidades de países diferentes
import pandas as pd

dic={'Cidade':['Amsterdã', 'Atenas', 'Bogotá', 'Bruxelas', 'Buenos Aires', 'Caracas', 'Chicago', 'Cid. México',
               'Dublin', 'Estocolmo', 'Genebra', 'Hong-kong', 'Istambul', 'Londres', 'Los Angeles', 'Madri',
               'Manila', 'Milão', 'Montreal', 'Nova Iorque', 'Paris', 'Rio de Janeiro', 'San Francisco',
               'São Paulo', 'Singapura', 'Sydney', 'Tel Aviv', 'Tóquio', 'Toronto', 'Zurique'],
     'Mecânico':[26542, 12456, 3806, 25528, 6574, 20068, 39790, 8304, 13840, 25950, 37022, 5822, 6228, 17646,
                 36330, 12110, 1730, 13494, 23528, 32870, 15916, 8650, 39946, 11072, 5190, 20068, 9688,
                 16954, 25950, 34600]}

dados= pd.DataFrame(dic)

dados.to_csv('Salários Mecanicos.csv', index= False)
