#Fromas de verificar dispersão entre valores em python

#1º forma
#A função math.isclose() verifica se dois valores estão próximos dentro de uma tolerância definida.
#O rel_tol ajusta a sensibilidade da comparação.

import math

a = 10.0001
b = 10.0002

# Verifica se a e b estão próximos com uma tolerância relativa de 0.0001
proximos = math.isclose(a, b, rel_tol=1e-4)  # Tolerância relativa de 0.0001 (0.01%)

print(proximos)  # Saída: True

#2º forma
#Comparando a Diferença Absoluta Manualmente
#A função abs() em Python retorna o valor absoluto de um número, ou seja, transforma
#números negativos em positivos, mantendo os positivos inalterados.

a = 10.0001
b = 10.0002

epsilon = 0.0002  # Define um limite de proximidade

proximos = abs(a - b) < epsilon

print(proximos)  # Saída: True

#3º forma
# Para Arrays/Números em NumPy (numpy.isclose())
#Se estiver lidando com arrays ou cálculos vetorizados, use numpy.isclose():
import numpy as np

a = np.array([1.0001, 2.0002, 3.0003])
b = np.array([1.0002, 2.0003, 3.0004])

proximos = np.isclose(a, b, atol=1e-4)  # atol é a tolerância absoluta

print(proximos)  # Saída: [ True  True  True ]
