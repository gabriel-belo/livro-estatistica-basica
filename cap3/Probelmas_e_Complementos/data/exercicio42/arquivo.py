import pandas as pd

dic={'População': [1453756, 652385, 3221040, 395725, 7065573, 587311, 1243627, 6118995, 3032435, 8185250,
                   3013740, 3641397, 8486638, 3037231, 1939426, 14080670, 19273533, 3351669, 15420450, 39827690,
                   10284503, 5866487, 10582287, 2265813, 2854642, 5647035, 2455903]}
dic['População'].sort()

dados= pd.DataFrame(dic)

dados.to_csv('CD Brasil. csv', index= False)
