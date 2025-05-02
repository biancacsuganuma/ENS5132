# -*- coding: utf-8 -*-
"""
Created on Thu May  1 12:34:44 2025

@author: Carlos - SC
"""
import pandas as pd
import numpy as np
import os

#Função para estutrurar os dados"

def FlowMaxAnalysis(uf,repoPath):
    uf = 'GO'
    repoPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01"
    dataDir = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01\inputs" +'/'+ uf
    
    # Lista de arquivos dentro da pasta
    dataList = os.listdir(dataDir)
    #print(dataList)  
#%% Lendo os dados da planilha e os salvando em uma única lista     
    # Criando lista vazia
    allFiles  =[]
    
    # Abrir os dados de vazão, objeto de estudo, em um dataframe
    # Função para apular linhas == skiprows=15 
    aqPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01\inputs\GO\60810000_Vazoes.csv"
    aqData = pd.read_csv(aqPath, encoding='latin1', sep=';', engine='python', quotechar='"', skiprows=15)
    
    # adicionar elementos a uma lista
    allFiles.append(aqData)
    
    #%% ignorando colunas desnecessárias, de horas (pq é = nam), estatísticas
    # Lista com colunas por posição
    cols_position = list(aqData.columns[0:2]) + list(aqData.columns[3:16])
    # Lista com colunas por nome
    cols_name = list(aqData.loc[:, 'Vazao01Status':'Vazao31Status'].columns)
    
    # Junta tudo que eu quero excluir
    cols_drop = cols_position + cols_name
    
    # Remove coluna hora do DataFrame, todo o dado é NAN
    aqData.drop(columns = cols_drop, inplace=True)
    
    # A função pd.to_datetime transforma a strins de data em objetos datetime do pandas, 
    # permitindo que façamos operações com base na data e hora, como filtar,
    # ordemar ou extrair partes específicas como ano, mes, dia 
    # quando esta escrito %d/%m/%Y  esta indicando para o pd como é o formado da data no arquivo, 
    # para ele conseguir converter corretamente
    datetimeDf = pd.to_datetime(aqData.Data, format='%d/%m/%Y')
    aqData['datetime'] = datetimeDf
    aqData= aqData.set_index(aqData['datetime'])
    
    #%%  Derretendo as colunas de vazões diárias 
    # A função melt trasforma linhas em colunas
    # criando outra variavel para preencher com os dados arrumados
    
    meltedDf = aqData.melt(id_vars=['datetime'], 
                      value_vars=[col for col in aqData.columns if 'Vazao' in col], 
                      var_name='day', 
                      value_name='flow')
    
    # Extrai o número do dia da coluna day (ex: 'Vazao01' → 1)
    meltedDf['day'] = meltedDf['day'].str.extract('(\d+)').astype(int)
    
    # Cria coluna com ano e mês da linha original
    meltedDf['year'] = meltedDf['datetime'].dt.year
    meltedDf['month'] = meltedDf['datetime'].dt.month
    
    # Cria coluna com a data completa
    meltedDf['Date'] = pd.to_datetime({'year': meltedDf['year'],
                                                  'month': meltedDf['month'],
                                                  'day': meltedDf['day']}, errors='coerce')
    # Remove datas inválidas (ex: 31 de fevereiro)
    meltedDf.dropna(subset=['Date'], inplace=True)
    
    # Cria as colunas separadas com a coluna Date, data corrigida  
    meltedDf['year'] = meltedDf['Date'].dt.year
    meltedDf['month'] = meltedDf['Date'].dt.month
    meltedDf['day'] = meltedDf['Date'].dt.day
    
    # Ordena cronologicamente
    meltedDf.sort_values(by='Date', inplace=True)

    # Reorganiza as colunas (se quiser deixar bonitinho)
    meltedDf = meltedDf[['Date', 'year', 'month', 'day', 'flow']]

#%% Salvando aos editados 
    # criando pasta chamada outputs para salvar os dado, caso a pasta já exista o parâmetro exist_ok=true faz o codigo não gerar outra pasta 
    os.makedirs(repoPath +'/'+'outputs/'+uf,exist_ok=True)
     
    # Salvando em csv 
    meltedDf.to_csv(repoPath +'/'+'outputs/'+uf+'/'+'flow.csv')

    return  meltedDf
    
    