import pandas as pd
dados= pd.read_csv('../data/exercicio01/erros_impressao.csv')

dados_df= pd.DataFrame(dados)
multiplicar= dados_df['Frequencia'] * 10
soma= multiplicar[1]+(multiplicar[2]*2)+(multiplicar[3]*3)+(multiplicar[4]*4)
print(f'O número de erros para 500 páginas de acordo com a proporção é {soma}')