# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:01:27 2025

@author: Carlos - SC
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm


# Função para decomposição da série temporal
def timeSeriesDecompose(meltedDf, uf, repoPath):
    uf= 'GO'
    repoPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01"
    os.makedirs(repoPath+'/figuras/'+uf, exist_ok=True)
    
    # Calcular a média dos valores de 'flow', ignorando os NaN
    mean_flow = meltedDf['flow'].mean()
    
    meanDF = meltedDf.copy()
    
    meanDF['flow'] = meanDF['flow'].fillna(mean_flow)
    
    # Decomposição da série temporal
    
    # Seleciona apenas a coluna das vazões
    dataDecompose = meanDF[['Date', 'flow']]
    
    #transformando datetime em im index
    dataDecompose = dataDecompose.set_index('Date')
    
    # Agrupa por mês e calcula a média mensal
    dataDecomposeMonthly = dataDecompose.groupby(pd.Grouper(freq="Y")).mean()
    
    # Converte para a função de decomposição do statsmodel
    # Agora a variável 'dataDecomposeMonthly' é definida corretamente
    dataDecomposeMonthly = pd.Series(np.array(dataDecomposeMonthly['flow']), index=pd.to_datetime(dataDecomposeMonthly.index))
    
    # Gerando um índice periódico com os meses
    full_index = pd.date_range(start=dataDecomposeMonthly.index.min(), end=dataDecomposeMonthly.index.max(), freq='M')
    
    # Reindexando para preencher os dados faltantes com NaN
    complete_data = dataDecomposeMonthly.reindex(full_index)
    
    # Interpolando dados que possuem NaN
    complete_data = complete_data.interpolate().dropna()
    
    # Decompondo a série temporal utilizando a decomposição sazonal do statsmodel
    res = sm.tsa.seasonal_decompose(complete_data, period=12)
    
    # Gerando figura para a decomposição
    fig, axes = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(10, 8))
    
    res.observed.plot(ax=axes[0], legend=False, color='green')
    axes[0].set_ylabel('Original')
    axes[0].set_title('Decomposição da Série Temporal (Vazão)')
    
    res.trend.plot(ax=axes[1], legend=False, color='red')
    axes[1].set_ylabel('Tendência')
    
    res.seasonal.plot(ax=axes[2], legend=False, color='yellow')
    axes[2].set_ylabel('Sazonalidade')
    
    res.resid.plot(ax=axes[3], legend=False, color='gray')
    axes[3].set_ylabel('Ruído')
    
    fig.tight_layout()
    
    # Salvar figura
    fig.savefig(repoPath+'/figuras/'+uf+'/Decomposicao.png', bbox_inches='tight')
    
    return fig

