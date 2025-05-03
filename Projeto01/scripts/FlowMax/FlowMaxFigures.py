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
    
    # Títulos e rótulos
    plt.title('Gráfico de Linha da Vazão')
    plt.xlabel('Data')
    plt.ylabel('Vazão (m³/s)')
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/hidrograma.png', bbox_inches='tight')
#%% Fazendo o HIDROGRAMA médias mensais 

# Média mensal por ano

def FlowHydroMonth(meltedDf,uf,repoPath):
    os.makedirs(repoPath+'/figuras/'+uf, exist_ok=True)
    
    dropnaDF = meltedDf.dropna()
    
    # Média mensal por ano
    meanMonth = dropnaDF.groupby(['year', 'month'])['flow'].mean().reset_index()
    
    # Média de todos os anos por mês (média mensal histórica)
    meanGeral = dropnaDF.groupby('Mes')['flow'].mean().reset_index()

    # Criando uma figura e um eixo
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # hidrograma 
    ax.plot(x, y, linestyle='-', color='purple', label='Vazão diária')
    
    # Títulos e rótulos
    plt.title('Gráfico de Linha da Vazão')
    plt.xlabel('Data')
    plt.ylabel('Vazão (m³/s)')
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/hidrograma.png', bbox_inches='tight')
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
    ax.hist(dropnaDF['flow'], edgecolor='black', color='skyblue', label='Vazão')
    plt.yscale('log')  # Y em escala logarítmica
    
    # Adicionando título e rótulos aos eixos
    ax.set_title('Histograma da Vazão', fontsize=14)
    ax.set_xlabel('Vazão (m³/s)', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)
    
    # Remover os valores do eixo X (já que estão sendo exibidos em cima das barras)
    #ax.set_xticklabels([])  # Remove os rótulos de texto no eixo X 
    
    # Salvando o gráfico
    fig.savefig(repoPath+'/figuras/'+uf+'/histograma.png', bbox_inches='tight')
    


    
    
    

