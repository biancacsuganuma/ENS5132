# -*- coding: utf-8 -*-
"""
Created on Thu May  1 15:02:43 2025

@author: Carlos - SC
"""
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import stats
import statsmodels.api as sm
import pandas as pd
#%% Fazendo o HISTOGRAMA 

def FlowMaxHistograma(meltedDf,uf,repoPath):
    uf = 'GO'
    repoPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01"
    #flowPath = repoPath +'/'+ 'outputs' + '/' + uf + '/' + 'flow'
    # Criando diretório
    os.makedirs(repoPath+'/'+'figuras/'+uf, exist_ok=True)

    # Removendo os NANs
    dropnaDF = meltedDf.dropna()
    

    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Criando o histograma da coluna 'flow' com bins automáticos
    n, bins, patches = ax.hist(dropnaDF['flow'], bins='auto', edgecolor='black', color='skyblue', label='Vazão')
    
    # Adicionando título e rótulos aos eixos
    ax.set_title('Histograma da Vazão (flow)', fontsize=14)
    ax.set_xlabel('Valor da Vazão (flow)', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)
    
    # Colocando os intervalos dos bins em cima das barras, na vertical
    for i in range(len(bins)-1):
        bin_left = bins[i]  # Pega o valor de início de cada intervalo
        bin_right = bins[i+1]  # Pega o valor de fim de cada intervalo
        # Exibindo o intervalo completo (bin_left - bin_right) acima da barra, na vertical
        ax.text(
            (bin_left + bin_right) / 2,  # Posição X: centro de cada bin
            n[i],  # Posição Y: a altura da barra
            f'{bin_left:.1f} - {bin_right:.1f}',  # Texto: Exibindo o intervalo completo
            ha='center',  # Alinhamento horizontal no centro
            va='bottom',  # Alinhamento vertical em relação à barra
            fontsize=9,  # Tamanho da fonte
            color='black',  # Cor do texto
            rotation=90  # Texto rotacionado na vertical
            )
    
    # Remover os valores do eixo X (já que estão sendo exibidos em cima das barras)
    ax.set_xticklabels([])  # Remove os rótulos de texto no eixo X 
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/histograma.png', bbox_inches='tight')
    
    # Exibindo o gráfico
    plt.show()

#%%
        


