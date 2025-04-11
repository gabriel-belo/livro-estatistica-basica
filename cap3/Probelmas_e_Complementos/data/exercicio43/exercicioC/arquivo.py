#Preço de carros em 1999 em dólares
import pandas as pd

dic={'Veículo': ['Asia Towner', 'Audi A3', 'Chevrolet Astra', 'Chevrolet Blazer', 'Chrevolet Corsa', 'Chevrolet Tigra',
                 'Chevrolet Vectra', 'Chrysler Neon', 'Dodge Dakota', 'Fiat Fiorino', 'Fiat Marea', 'Fiat Uno Mille', 'Fiat Palio', 'Fiat Siena',
                 'Ford Escort', 'Ford Fiesta', 'Ford Ka', 'Ford Mondeo', 'Honda Civic', 'Hyundai Accent', 'Peugeot 106', 'Renault Clio',
                 'Toyota Corolla', 'Toyota Perua', 'VW Gol', 'VW Golf', 'VW Parati', 'VW Polo', 'VW Santana', 'VW Saveiro'],
     'Preço': [9440, 38850, 10532, 16346, 6176, 12890, 13140, 31640, 11630, 6700, 12923, 5257, 6260, 7780, 10767, 6316, 5680, 33718, 14460, 21500,
               13840, 13700, 15520, 24632, 6340, 22200, 9300, 12018, 11386, 7742]}

dados= pd.DataFrame(dic)

dados.to_csv('Preços Veiculos.csv', index=False)



