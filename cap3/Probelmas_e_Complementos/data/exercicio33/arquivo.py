import pandas as pd

dic={'Cidade':[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
     'Investimento': [20, 16, 14, 8, 19, 15, 14, 16, 19, 18]}

dados= pd.DataFrame(dic)

print(dados)

dados.to_csv('Invest em Educacao.csv', index= False)