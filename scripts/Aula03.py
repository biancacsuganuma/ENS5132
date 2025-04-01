# -*- coding: utf-8 -*-
"""
Spyder Editor
Esse roteiro foi criado na terceira aula da disciplina ENS5132. Nessa aula, trabalharemos com:
    - Matrizes numpy
    - Pandas DataFrame 
    - Matplotlib 
    
    *Requisitos: pip install spyder numpy pandas matplotlib 
"""
#%% Importando pacotes 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%% Relembrando listas 

#Criando uma lista com strings e float 
listA = [1,2,3,'salve o Corinthians',20.5]
print(listaA)
#Criando uma lista com inteiros e float
listB = [1,2,3,20.5]

#%% Trabalhando com o numpy
# Criando um array numpy
arr = np.array ([0.7,0.75,1.85])
print(arr)

#Criando um array numpy a partir de uma lista mista 
arr2 = np.array(listA)

# Criando um array numpy a partir de uma lista apenas com números
arr3 = np.array(listB)

# Criando uma matriz 
precip = np.array([[1.07,0.44,1.50],[0.27,1.33,1.72]])


#acessando valor da primeira linha e coluna 
print(precip[0,0])

# acessando todos os valores da primeira linha 
print(precip[0,:])

# acessando todos os valores da primeira coluna
print(precip[:,0])

# cortando lista - selecional todos as linhas da primeira coluna
precipSlice = precip[:,0]

# extrai os dois primeiros valores da primeira linha
# índice 2 não é incluído, pois o intervalo em Python é aberto no final
 print(precip[0,0:2])
 
# -1 e -1 extrai o último valor da última linha da última coluna 
print(precip[-1,-1])

#%%
# Criando matrizes de múltiplas dimensões 

# Criar um arranjo de dados com início, fim e passo 
# Cria um array com valores de 1 a 15, com passo 1 
x= np.arange(1,16,1 )

# Mudando o shape/ dimensão da matriz
xReshape = x.reshape(3,5)

#Transposta 
print(xReshape.transpose())

# Criando matriz de números aleatórios, 3 dimensões, com 10, 100 e 100 unidades 
# De 0 até 1, excluso 
matRand = np.random.rand(10,100,100)

# Recortando matriz - todos os valores da 1º matriz
matRandSlice = matRand[0,:,:]

# Criando matriz com 4D 
# 3 blocos com matrizes de 10x100x100 - usada um vídeos
matRand4D = np.random.rand(3,10,100,100)

# Dimensão da matriz 
print(matRand4D.ndim)

# Shape da matriz 
print(matRand4d.shape)

# Número de elementos 
print(matRand4d.size)

# Multiplicando escalar 
print(matRand4D*3.9)

# Média da matriz 4D
print(matRand4D.mean()) #média da matriz inteira 

# O máximo, axis=0 → Opera ao longo das linhas
print(matRand4D.max(axis=0))

maxMat4d = matRand4D.max(axis=0)

#%% Pandas DataFrame

# Abrir dados de um arquivo de texto
dataSample = np.loadtxt(r"C:\Users\Leonardo.Hoinaski\Documents\ENS5132\data\dataSample.txt")

# Abrir arquivo com formato separado por vírgula .csv, bom apenas para números
# encoding='Latin1' lê caracteres especiais
dataSample2 = np.loadtxt(r"C:\Users\Leonardo.Hoinaski\Documents\ENS5132\data\dataSample2.csv",
                         delimiter=',', encoding='Latin1')
# Melhor para arquivo diverso
dataSample2 = pd.read_csv(r"C:\Users\Leonardo.Hoinaski\Documents\ENS5132\data\MQAR\SP\SP201501.csv",
                          encoding='Latin1')

# Este comando gera estatísticas descritivas dos dados numéricos do DataFrame
df.describe()

# Este comando mostra informações gerais do DataFrame
df.info()

# df.Poluente->seleciona a coluna do poluentes, quando == 'MP10'
# .Valor seleciona a coluna dos valores do MP10
# .plot() plota o gráfico
df[df.Poluente=='MP10'].Valor.plot()
