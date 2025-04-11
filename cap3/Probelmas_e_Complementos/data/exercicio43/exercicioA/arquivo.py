#Dados de CO da tabela Poluição de São Paulo
#CO= monóxido de carbono
import pandas as pd

dic={'CO':[6.6, 6.2, 7.9, 8.6, 8.8, 6.4, 6.9, 7.9, 8.2, 8.7, 6.3, 6.3, 6.3, 6.4, 7.7, 7.9, 7.9, 7.7, 6.9, 6.2]}

dados= pd.DataFrame(dic)

dados.to_csv('CO SP. csv', index= False)
