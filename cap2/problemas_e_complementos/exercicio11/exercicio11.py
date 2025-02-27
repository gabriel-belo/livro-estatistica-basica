import pandas as pd
import matplotlib.pyplot as plt

dic={'Classes de alugueis': ['2 |- 3', '3 |- 5', '5 |- 7', '7 |- 10', '10 |- 15'],
     'Zona urbana frequencia': [10, 40, 80, 50, 20], 'Zona rural frequencia': [30, 50, 15, 5, 0],
     'Amplitude':[1, 2, 2, 3, 5]}

classes_alugueis_df= pd.DataFrame(dic)

#Densidade
densidade_urbana=[]
densidade_rural=[]


for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_densidade= classes_alugueis_df['Zona urbana frequencia'][i] / classes_alugueis_df['Amplitude'][i]
     densidade_urbana.append(round(calculo_densidade))


for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_densidade= classes_alugueis_df['Zona rural frequencia'][i] / classes_alugueis_df['Amplitude'][i]
     densidade_rural.append(round(calculo_densidade))


classes_alugueis_df['Zona urbana densidade']= densidade_urbana
classes_alugueis_df['Zona rural densidade']= densidade_rural

#Proporção
proporcao_urbana=[]
proporcao_rural=[]

total_urbana= classes_alugueis_df['Zona urbana frequencia'].sum()
total_rural= classes_alugueis_df['Zona rural frequencia'].sum()

for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_proporcao= classes_alugueis_df['Zona urbana frequencia'][i] / total_urbana
     proporcao_urbana.append(calculo_proporcao)

for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_proporcao = classes_alugueis_df['Zona rural frequencia'][i]/ total_rural
     proporcao_rural.append(calculo_proporcao)

classes_alugueis_df['Zona urbana proporcao']= proporcao_urbana
classes_alugueis_df['Zona rural proporcao']= proporcao_rural

#Porcentagem

porcentagem_urbana=[]
porcentagem_rural=[]

for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_porcentagem= (classes_alugueis_df['Zona urbana proporcao'][i] / classes_alugueis_df['Amplitude'][i])
     porcentagem_urbana.append(round(calculo_porcentagem, 2))

for i in range(len(classes_alugueis_df['Amplitude'])):
     calculo_porcentagem= (classes_alugueis_df['Zona rural proporcao'][i] / classes_alugueis_df['Amplitude'][i])
     porcentagem_rural.append(round(calculo_porcentagem, 2))

classes_alugueis_df['Zona urbana porcentagem']= porcentagem_urbana
classes_alugueis_df['Zona rural porcentagem']= porcentagem_rural

print(classes_alugueis_df['Zona urbana porcentagem'])

plt.subplot(1,2,1)
plt.hist(classes_alugueis_df['Zona urbana proporcao'])

plt.subplot(1, 2, 2)
plt.hist(classes_alugueis_df['Zona rural proporcao'])

plt.show()

#b