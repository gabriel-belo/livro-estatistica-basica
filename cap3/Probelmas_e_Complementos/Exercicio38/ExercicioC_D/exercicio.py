import numpy as np

Z= [ 0.598, 0.59, -0.18, -0.18, 0.59, 1.38 -0.18, -0.18, 0.59, -0.18,  1.38, -0.97, -0.97, 0.59, 0.59, -0.97, -0.18, 0.59, -3.33, -0.97, -0.97, -0.18, 1.38, 0.59, 0.59]

z= np.mean(Z)

dp_z= np.std(Z)

lista=[]
for nota in Z:
    if nota > 2*dp_z or nota < -2*dp_z:
        lista.append(nota)

print(z, dp_z, lista)