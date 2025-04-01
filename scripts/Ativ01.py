"""
Atividade 1:
    * Crie uma matriz com números aleatórios com duas dimensões (2D) com 100 linhas e 100 colunas.
    * Recorte a primeira linha e liste os valores
    * Determine o valor da última linha e coluna

CONAMA nº 491/2018:
    MP10 - µg/m³ (média de 24h):
        * Atenção: 250
        * Alerta: 420
        * Emergência: 500
Supondo que em cada célula temos a média (24h) da concentação, as colunas indicam a medição em 100 dias,
e nas linhas 100 lugares diferentes  
 
"""
import numpy as np
import pandas as pd

# gerando uma matriz de números aleatórios com intervalo definido
# np.random.uniform(low, high, size)
Mconc = np.random.uniform(250,600,(100,100))

# Recortando a primeira linha 
Mconc_l1 = Mconc[0, :]
print(Mconc_l1)

# Último valor da última coluna e linha 
Mconc_10000 = Mconc[-1,-1]
print(Mconc_10000)


if Mconc_10000>=500 :
    print(Mconc_10000,"Emergência")
if 500>Mconc_10000>=420 :
    print(Mconc_10000,"Alerta")
if 420>Mconc_10000>=250 :
    print(Mconc_10000,"Atenção")