# -*- coding: utf-8 -*-
"""
Neste script utilizei durante a Aula04
"""
#%% Importando meus pacotes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#%%
# Revisão numpy 
# Criando um vetor com arranjo de dados 
x = np.arange(-10,20,0.15)

# Brincando com indexação - acessando índices
print('Este é a quarta posição do meu vetor x:' + str(x[3]))

print('Estes são os 3 primeiros valores:' + str(x[0:3]))

# Substituir um valor dentro do vetor 
x[9] = 99999999 #exemplo de medição errada
x[11] = -999999 #exemplo de medição errada

# Extraindo a média
meanX =  np.mean(x)
print(meanX)

# Operação booleana - lógica
# and = &
# or = | 
# Encontrando valores errados

# True se o valor correspondente de x 
# for maior que 20 ou menor que -10
# False caso contrário
vecBool = (x>20) | (x<-10) # estou usando esse simbolo para | para or 

# Extraindo apenas valores errados usando lógica booleana
valErrado = x[vecBool]

# Substituindo os valores errados por 0 
x2 = x.copy() # criando uma cópia independente 
x2[vecBool] = 0 # substitui os valores true por 0 

print('Esta é a média de x substituindo valores errados por 0: ' 
      + str(np.mean(x2)))

# Certo: substituir por um NAN - not a number
x3 = x.copy() # criando uma cópia independente 
x3[vecBool] = np.nan # troca true por NAN

print('Esta é a média de x substituindo valores errados por nan: ' 
      + str(np.nanmean(x3)))

# Substituir nan pela média, para que não tenha interruções na série
x4 = x.copy() # criando uma cópia independente 
x4[vecBool] = np.nanmean(x3) # só pega true e troca pela média, c/ nan
print('Esta é a média de x substituindo valores errados por nan: ' 
      + str(np.mean(x4)))

#%% Usando matplotlib para inspecionar vetores 
# gerando gráficos 

fig, ax = plt.subplots(4)
ax[0].plot(x)
ax[1].plot(x2)
ax[2].plot(x3)
ax[3].plot(x4)

#%% Loop em python

# Loop utilizando Range e acumulando em um vetor 
# Em cada iteração:
# ii assume valores de 0 a 9.
for ii in range (0,10):
    val = 2**ii
    print(val)
    
# Loop utilizando Range e acumulando em um vetor
vetor = []
for ii in range (0,10):
    val = 2**ii
    vetor.append(val)
    print(val)
    
# Loop utilizando Range e acumulando em um vetor 
vetorAcumulado = []
val = 0
for ii in range (0,10):
    val = val + 2**ii
# Adiciona esse novo valor acumulado na lista vetorAcumulado
    vetorAcumulado.append(val)
    
# Loop utilizando uma lista 
alunas = ['Mariana','Bianca','AnaJúlia', 'Mariah']

for aluna in alunas:
    print('Anota da '+aluna+' é: ' +str(np.random.rand(1)*10))

#%% Trabalhando com pandas

# Criando um DataFrame manualmente
df = pd.DataFrame(columns=['date','NH3'],
                  data=[['2025/04/01',0.35],
                        ['2025/04/01',1.01]])

# Criando mais coisas dentro do df 
df['NO3'] = np.nan
df['O2'] = [2, 10]
df['SO2'] = np.nan
df.loc[0, 'SO4'] = 10


#%% Baixando dados
# Trabalhando com dado real
# Criando variável com o nome do estado

dataDir = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\dados\SP"

# Lista de arquivos dentro da pasta
dataList = os.listdir(dataDir)

# Movendo para a pasta de dados/uf
os.chdir(dataDir)

allFiles = []
# Loop na lista datalist 
for fileInList in dataList:
    print(fileInList)
    dfConc = pd.read_csv(fileInList,encoding='latin1')
    allFiles.append(dfConc)

# Concatenando meus DataFrames 
allFiles = pd.concat(allFiles)

# Extraindo nomes das estações sem redundância
stations = pd.unique(allFiles['Estacao'])

# Usando lógica 
stationDf = allFiles[allFiles['Estacao'] == stations]

# Criando coluna DataTime
datetimeDf = pd.to_datetime(stationDf.Data, format='%Y-%m-%d')

# Criando coluna datetime dentro de station 
stationDf['datatime']= datetimeDf

# Transformando a coluna de datetime em index
stationDf = stationDf.set_index(stationDf['datetime'])

# Extrair o ano e mês
stationDf['year'] = stationDf.index.year
stationDf['month'] = stationDf.index.month
stationDf['day'] = stationDf.index.day

# Extraindo a hora
horas  = stationDf.Hora.str.split(':')

horaDf = []
for hora in horas:
    print(hora)
    horaDf.append(hora)

stationDf['hour'] = horaDf


# Corrigindo a coluna datetime
stationDf['datetime'] = pd.to_datetime(
    stationDf[['year', 'month','day','hour']],format='%Y%m%d %H')
#%%

pasta_saida = r'C:\Users\Carlos - SC\Documents\GitHub\ENS5132\dados\SP'

# Loop para exportar os dados de cada estação
for estacao in stations:
    # Filtra os dados dessa estação dentro do stationDf
    df_estacao = stationDf[stationDf['Estacao'] == estacao]
    
    # Cria um nome de arquivo "limpo" (sem espaços ou acentos)
    nome_arquivo = estacao.replace(' ', '_').replace('/', '_') + '.csv'
    
    # Caminho completo para salvar
    caminho_csv = os.path.join(pasta_saida, nome_arquivo)
    
    # Exporta o DataFrame para CSV
    df_estacao.to_csv(caminho_csv, index=False, encoding='utf-8')
    
    print(f'Arquivo salvo: {caminho_csv}')


