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
from matplotlib.colors import TwoSlopeNorm
import seaborn as sns
#%% Fazendo HIDROGRAMA 
       
def FlowHydro(meltedDf,uf,repoPath):
    os.makedirs(repoPath+'/figuras/'+uf, exist_ok=True)
    
    dropnaDF = meltedDf.dropna()
    
    x = dropnaDF['Date']        # Eixo X (ex: datas ou tempo)
    y = dropnaDF['flow']     # Eixo Y (ex: vazão)
    
    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # hidrograma 
    ax.plot(x, y, linestyle='-', color='purple', label='Vazão diária')
    ax.set_yscale('log') # colocando y na escala logaritmica, para melhor visualização
    
    # Títulos e rótulos
    ax.set_title('Gráfico de Linha da Vazão')
    ax.set_xlabel('Data')
    ax.set_ylabel('Vazão (m³/s)')
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/hidrograma.png', bbox_inches='tight')
#%% Fazendo o HIDROGRAMA médias mensais 

# Média mensal por ano

def FlowHydroMonth(meltedDf,uf,repoPath):
    os.makedirs(repoPath + '/figuras/' + uf, exist_ok=True)
    dropnaDF = meltedDf.dropna()

    # Média mensal por ano
    meanMonth = dropnaDF.groupby(['year', 'month'])['flow'].mean().reset_index()

    # Cria uma coluna datetime com base em year + month no DataFrame 
    meanMonth['DateMonth'] = pd.to_datetime(meanMonth['year'].astype(str) + '-' + meanMonth['month'].astype(str) + '-01')

    # Média geral da série
    meanGeral = dropnaDF['flow'].mean()

    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hidrograma com linha
    ax.plot(meanMonth['DateMonth'], meanMonth['flow'], color='purple', linewidth=1, label='Variação da média mensal')
    ax.axhline(meanGeral, color='red', linestyle='--', linewidth=2, label=f'Média geral ({meanGeral:.2f} m³/s)')

    # Formatação do eixo X
    plt.xticks(rotation=45)
    plt.xlabel('Mês/Ano')
    plt.ylabel('Vazão média mensal (m³/s)')
    plt.title('Hidrograma com Médias Mensais por Ano')
    plt.legend()

    # Salvando o gráfico
    fig.savefig(repoPath + '/figuras/' + uf + '/hidrogramaMédiaMensal.png', bbox_inches='tight')
    
#%% HEATMAP das Médias Mensais com Cores Centradas na Média Geral

def FlowHeatMap(meltedDf, uf, repoPath, meanMonth):
    os.makedirs(repoPath + '/figuras/' + uf, exist_ok=True)
    
    # Cria a tabela pivot (ano vs mês)
    heatmap = meanMonth.pivot(index='year', columns='month', values='flow')
    heatmap = heatmap[sorted(heatmap.columns)]
    
    # Calcula mínimo, máximo e média
    flowMin = heatmap.min().min()
    flowMax = heatmap.max().max()
    flowMedia = heatmap.values.mean()
    
    # Normalização com ponto central na média
    # Garante que não é tudo igual
    if flowMin < flowMedia < flowMax:
        norm = TwoSlopeNorm(vmin=flowMin, vcenter=flowMedia, vmax=flowMax)
    else:
        norm = None  # sem normalização
    
    # Cria a figura e o heatmap
    fig = plt.figure(figsize=(12, 8))
    sns.heatmap(
        heatmap,
        cmap='RdPu',
        annot=True,
        fmt='.1f',
        linewidths=0.5,
        linecolor='white',
        norm=norm,
        cbar_kws={'label': 'Vazão (m³/s)'}
    )
    
    # Títulos e eixos
    plt.title('Heatmap das Médias Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Ano')
    
    # Salvando tabela
    fig.savefig(repoPath + '/figuras/' + uf + '/heatmap.png', bbox_inches='tight')
    
#%% Fazendo o BOXPLOT

# Garante que o DataFrame tem as colunas 'month' (1 a 12) e 'flow'
def FlowBoxPlot(meltedDf, uf, repoPath):
    os.makedirs(repoPath + '/figuras/' + uf, exist_ok=True)
    dropnaDF = meltedDf.dropna()

    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='month', y='flow', data= dropnaDF, color='purple', fliersize=3, linewidth=1)

    # Estilo visual
    plt.xlabel('Mês', fontsize=12)
    plt.ylabel('Vazão Mensal (m³/s)', fontsize=12)
    plt.title('Distribuição da Vazão Mensal por Mês do Ano', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
   
    # Salvando figura
    fig.savefig(repoPath + '/figuras/' + uf + '/boxplot.png', bbox_inches='tight')

#%% Fazendo o HISTOGRAMA 

def FlowHistograma(meltedDf,uf,repoPath):
    uf = 'GO'
    repoPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01"
    # Criando diretório
    os.makedirs(repoPath+'/'+'figuras/'+uf, exist_ok=True)

    # Removendo os NANs
    dropnaDF = meltedDf.dropna()
    
    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Criando o histograma da coluna 'flow' com bins automáticos
    ax.hist(dropnaDF['flow'], edgecolor='black', color='purple', label='Vazão')
    
    # Adicionando título e rótulos aos eixos
    ax.set_yscale('log') # colocando y na escala logaritmica, para melhor visualização
    ax.set_title('Histograma da Vazão', fontsize=14)
    ax.set_xlabel('Vazão (m³/s)', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)
    
    # Remover os valores do eixo X (já que estão sendo exibidos em cima das barras)
    #ax.set_xticklabels([])  # Remove os rótulos de texto no eixo X 
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/histograma.png', bbox_inches='tight')
    


    
    
    

