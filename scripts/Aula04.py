# -*- coding: utf-8 -*-
"""
Neste script utilizei durante a Aula04
"""
#%% Importando meus pacotes
import numpy as np
import pandas as pd

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

vecBool = (x>20) | (x<-10) # estou usando esse simbolo para | para or 

# extraindo valores errados 
valErrado = x[vecBool]

# Substituindo os valores errados por 0 
x2 = x.copy() # criando uma cópia independente 
x2[vecBool] = 0 # só pega true 
print('Esta é a média de x substituindo valores errados por 0: ' 
      + str(np.mean(x2)))

# Certo: substituir por um NAN - not a number
x3 = x.copy() # criando uma cópia independente 
x3[vecBool] = 0 # só pega true 
print('Esta é a média de x substituindo valores errados por 0: ' 
      + str(np.mean(x3)))

print('Esta é a média de x usando np.nanmean de x sbstiyuindo valores errados: ' 
      + str(np.nanmean(x3)))

# Substituir nan pela média, para que não tenha interruções na série, alterei 
# x de novo
x4 = x.copy() # criando uma cópia independente 
x4[vecBool] = 0 # só pega true 
print('Esta é a média de x substituindo valores errados por 0: ' 
      + str(np.mean(x4)))



