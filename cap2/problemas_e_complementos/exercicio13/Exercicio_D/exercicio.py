import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados= pd.read_excel('homens.xlsx')
dados_df= pd.DataFrame(dados)
print(dados_df)