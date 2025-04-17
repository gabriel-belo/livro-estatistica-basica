import pandas as pd
#X= Número de emprego nos últimos dois anos
#Y= Salário mais recente, em número de salários mínimos

dic = {'Indivíduo': [i for i in range(1, 41, 1)],
        'X':[1, 3, 2, 3, 2, 2, 3, 1, 2, 3, 2, 3, 1, 2, 3, 4, 1, 2, 2, 2, 2, 3, 4, 1, 2, 3, 4, 1, 4, 3, 2, 1, 4, 2,
          4, 3, 1, 3, 2, 2],
        'Y':[6, 2, 4, 1, 4, 1, 3, 5, 2, 2, 5, 2, 6, 6, 2, 2, 5, 5, 1, 1, 4, 2, 1, 5, 4, 2, 1, 5, 4, 3, 2, 1, 1, 6,
             2, 1, 4, 2, 3, 5]
     }
dados= pd.DataFrame(dic)

dados.to_csv('Rotatividade mao-de-obra.csv', index= False)