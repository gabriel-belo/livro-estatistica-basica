import numpy as np
from scipy.stats import  trim_mean
salarios=np.array([4.0, 4.56, 5.25, 5.73, 6.26, 6.66, 6.86, 7.39, 7.59, 7.44, 8.12, 8.46, 8.74, 8.95, 9.13, 9.35, 9.77,
          9.8, 10.53, 10.76, 11.06, 11.59, 12.0, 12.79, 13.23, 13.60, 13.85, 14.69, 14.71, 15.99, 16.22, 16.61,
          17.26, 18.75, 19.4, 23.3])

salario_final= salarios * 1.518

# Média aparada a 10% (remove 10% do início e 10% do fim dos dados)
media_aparada10 = trim_mean(salarios, proportiontocut=0.1)

print("Média aparada a 10%:", media_aparada10)


media_aparada25 = trim_mean(salarios, proportiontocut=0.25)

print("Média aparada a 25%:", media_aparada25)