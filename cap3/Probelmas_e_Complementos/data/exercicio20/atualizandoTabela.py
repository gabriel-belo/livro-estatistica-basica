import pandas as pd
import re
dados= pd.read_csv('../../data/exercicio20/Salários do DP.csv')

dados['Pontos médio']= [1, 3, 5, 7]
print(dados)

def Amplitude(intervalo):
    numeros = re.findall(r'\d+', intervalo)
    lm_inferior= int(numeros[0])
    lm_superior= int(numeros[1])
    subtracao= lm_superior - lm_inferior
    return subtracao

dados['Amplitude']= dados['Faixa salarial'].apply(Amplitude)


dados['Frequencia Absoluta']= (dados['Frequência relativa'] * 120).astype(int)

dados['Frequencia Acumulada'] = dados['Frequencia Absoluta'].cumsum()

# Salvar no mesmo arquivo, sobrescrevendo os dados antigos
dados.to_csv("../../data/exercicio20/Salários do DP.csv", index=False)