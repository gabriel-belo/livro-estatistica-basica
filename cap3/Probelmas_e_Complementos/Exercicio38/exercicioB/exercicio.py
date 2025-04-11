import numpy as np

notas= np.array([9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7, 9, 9, 7, 8, 9, 4, 7, 7, 8, 10, 9, 9])

media= np.mean(notas)

dp= round(np.std(notas),2)

print(media, dp)

Z= np.array([(notas - media)/ dp])

print(Z)