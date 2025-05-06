# -*- coding: utf-8 -*-
"""
Created on Sat May  3 15:31:11 2025

@author: Carlos - SC
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os



def normalityCheck(meltedDf, uf, repoPath):
    uf= 'GO'
    repoPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01"
    os.makedirs(repoPath + '/figuras/' + uf, exist_ok=True)
    dropnaDF = meltedDf.dropna()
    
    # Criando a figura com 3 subplots
    fig, ax = plt.subplots(3, figsize=(12, 9))

    # Log transformando os dados de vazão (fluxo)
    ax[0].hist(np.log(dropnaDF['flow']), facecolor='red')
    ax[0].set_title('Log')
    ax[0].set_xlabel('Vazão (log)')
    ax[0].set_ylabel('Frequência')

    # Box-Cox transformação
    flow_data = dropnaDF['flow']
    if (flow_data > 0).all():
        transformed_data, _ = stats.boxcox(flow_data)
        ax[1].hist(transformed_data, facecolor='green')
        ax[1].set_title('BoxCox')
        ax[1].set_xlabel('Vazão (Box-Cox)')
        ax[1].set_ylabel('Frequência')
    else:
        ax[1].hist(flow_data, facecolor='green')
        ax[1].set_title('BoxCox (Dados não podem ser transformados)')
        ax[1].set_xlabel('Vazão')
        ax[1].set_ylabel('Frequência')

    # Dados originais
    ax[2].hist(flow_data, facecolor='blue')
    ax[2].set_title('Dado original')
    ax[2].set_xlabel('Vazão')
    ax[2].set_ylabel('Frequência')

    # Ajusta o layout para não sobrepor os gráficos
    fig.tight_layout()

    # Salva o histograma gerado como uma imagem
    fig.savefig(repoPath + '/figuras/' + uf + '/histogramDataNormalization_' + 'flow' + '.png')
    
    return fig
