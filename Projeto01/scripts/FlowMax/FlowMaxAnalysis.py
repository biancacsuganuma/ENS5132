# -*- coding: utf-8 -*-
"""
primeira do trabalho 1 

Este script será utilizado para analisar os dados de qualidade do ar disponibi-
lizados pela plataforma do Instituto Energia e Meio Ambiente. 


     Abrir corretamente o dado
     Inserir coluna datetime 
     Criar coluna com estação do ano
     Filtrar dataframe
     Extrair estatísticas básicas
     Estatísticas por agrupamento
     Exportar estatísticas agrupadas
     Criar uma função para realizar as tarefas acima
     Criar função para gerar figuras 
     Loop para qualquer arquivo dentro da pasta
     Estatística univariada e bivariada – função exclusiva
     Análise de dados usando o statsmodel
"""
import pandas as pd
import numpy as np
import os


# -------------------------- Abrir os dados -----------------------------------
# Criando variável com o nome do estado   

def FlowMaxAnalysis(uf):
       uf = 'GO'
       dataDir = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01\inputs" +'/'+ uf
       
       # Lista de arquivos dentro da pasta
       dataList = os.listdir(dataDir)
       
       # Mudando do diretório atual para o que foi colocado no dataDir
       os.chdir(dataDir)
       
       
#%%    # Lendo os dados da planilha e os salvando em uma única lista 
       # Criando lista vazia
       allFiles  =[]
       # Como eu só quero ler a planilha das vazões 
       # Caminho para um dos arquivos
       # separador - sep=';'
       # define as aspas como delimitador de texto - quotechar='"'
       # pular linhas - skiprows=15 
       aqPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto01\inputs\GO\60810000_Vazoes.csv"
       # Abrir os dados de vazão, objeto de estudo, em um dataframe
       aqInt = pd.read_csv(aqPath, encoding='latin1', sep=';', engine='python', quotechar='"', skiprows=15)
       aqData = pd.read_csv(aqPath, encoding='latin1', sep=';', engine='python', quotechar='"', skiprows=15)
       print(aqData)
#%%    # ignorando colunas desnecessárias, de horas (pq é = nam), estatísticas
       
       # Lista com colunas por posição
       cols_position = list(aqData.columns[0:2]) + list(aqData.columns[3:16])

       # Lista com colunas por nome
       cols_name = list(aqData.loc[:, 'Vazao01Status':'Vazao31Status'].columns)

       # Junta tudo que eu quero excluir
       cols_drop = cols_position + cols_name

       # Remove do DataFrame
       aqData.drop(columns = cols_drop, inplace=True)
        
       # Adiciona esse DataFrame à lista allFiles
       allFiles.append(aqData)
       
       
#%%    Inserir coluna datetime
       # Criando a coluna datetimeDf 
       #datetimeDf = pd.to_datetime(aqData.Data, format = '%d/%m/%Y' )
       # Criando coluna datetime dentro de aqData
       #aqData['datetime'] = datetimeDf
       # aqData['date'] = aqData['date'].dt.date
       # Transformando a coluna de date em index
       #aqData = aqData.set_index(aqData['datetime'])
       
       # Garante que aqData['Data'] é datetime
       aqData['datetime'] = pd.to_datetime(aqData['datetime'], dayfirst=True, errors='coerce')

       # Derrete as colunas de vazões diárias
       meltedDf = aqData.melt(id_vars=['datetime'], 
                       value_vars=[col for col in aqData.columns if 'Vazao' in col], 
                       var_name='day', 
                       value_name='flow')

       # Extrai o número do dia (ex: 'Vazao01' → 1)
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

       # Organiza o resultado final
       #meltedDf = meltedDf[['Date', 'flow']]
       
       #meltedDf.sort_values(by='Date', inplace=True)
       
       # Cria as colunas separadas
       meltedDf['year'] = meltedDf['Date'].dt.year
       meltedDf['month'] = meltedDf['Date'].dt.month
       meltedDf['day'] = meltedDf['Date'].dt.day

       # Ordena cronologicamente
       meltedDf.sort_values(by='Date', inplace=True)

       # Reorganiza as colunas (se quiser deixar bonitinho)
       meltedDf = meltedDf[['Date', 'year', 'month', 'day', 'flow']]
       
       
       
       
       
       
       
     
       
       # Extraindo a hora
       #horas  = aqData.Hora.str.split(':')
       
       #horaDf = []
       
       #for hora in horas:
           #print(hora[0])
           # pegando só HH de HH:hh
           #horaDf.append(hora[0])
           
       #aqData['hour'] = horaDf
       
       # Corrigindo a coluna datetime
       #aqData['datetime'] = pd.to_datetime(
          # aqData[['year', 'month','day','hour']],format='%Y%m%d %H')
       # Reiniciando minha index datetime
       
       #aqData = aqData.set_index(aqData['datetime'])
       
       
#%%    Criando uma coluna de Estacao com NaN 
       aqData['Season'] = np.nan
       # Verão
       aqData['Season'][(aqData.month==1) | (aqData.month==12) | 
                      (aqData.month==2) ] = 'Verão'
       # Outono
       aqData['Season'][(aqData.month==3) | (aqData.month==5) | 
                      (aqData.month==4) ] = 'Outono'
       # Inverno
       aqData['Season'][(aqData.month==6) | (aqData.month==7) | 
                      (aqData.month==8) ] = 'Inverno'
       # Primavera
       aqData['Season'][(aqData.month==9) | (aqData.month==10) | 
                      (aqData.month==11) ] = 'Primavera'
#%% Estatística básica       
       # Extraindo o nome dos poluentes 
       pollutants = np.unique(aqData.Poluente)
       
       # criando pasta para salvar os dado
       os.makedirs(r'C:\Users\Leonardo.Hoinaski\Documents\ENS5132\projeto01\outputs'
                     +'/'+uf,exist_ok=True)
       
       # Loop para cada poluente e extraindo as estatísticas básicas
       # for st in stations:
           #     print(st)
           #     statAll =[]
           #     for pol in pollutants:
       #       #         print(pol)
       #       #         basicStat = aqData['Valor'][(aqData.Poluente==pol) & 
       #       #                      (aqData.Estacao==st)].describe()
       #       #         basicStat = pd.DataFrame(basicStat)
       #       #         basicStat.columns =[pol]
       #       #         statAll.append(basicStat)       
               
       #       #      Unindo as estatísticas por poluente
       #       #      dfmerge = pd.concat(statAll,axis=1)
               
       #       #      Salva as estatísticas por estação    
       #       #     dfmerge.to_csv(r'C:\Users\Leonardo.Hoinaski\Documents\ENS5132\projeto01\outputs'
       #       #                          +'/'+uf+'/basicStat_'+st+'.csv')
               
       # Estatística básica usando groupby
       statGroup = aqData.groupby(['Estacao','Poluente']).describe()
               
       # Salvando em csv
       statGroup.to_csv(r'C:\Users\Leonardo.Hoinaski\Documents\ENS5132\projeto01\outputs'
                         +'/'+uf+'/basicStat_ALL.csv')
       aqData = aqData.set_index(pd.DatetimeIndex(aqData['datetime']))
       
       return aqData, stations
    
       
      

