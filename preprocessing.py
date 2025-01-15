import csv
import sys
import datetime
from dateutil import parser
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

entrada = 'C:/AI-IDS/Sample/In/captureCSV-CICFlowMeter.csv'

saida = 'C:/AI-IDS/Sample/Out/preprossesing.csv'

contador = 1
salvarDados = {}
linhasApagadas = 0

print("")
print('Iniciando a Preparacão dos Dados')
print("")
print('Caminho Entrada: {}'.format(entrada))
print("")
print('Caminho Saída: {}'.format(saida))
print("")

with open(entrada, 'r') as entradaCSV:   # Inicia a leitura do arquivo CSV de entrada
  dados = entradaCSV.readlines() # Retorna uma string para cada linha do arquivo CSV
  numeroLinhas = len(dados) # Numero total de linhas do arquivo CSV
  print('Total de linhas do arquivo CSV = {}'.format(numeroLinhas))
  
  for linha in dados[1:]:   # Inicia a leitura apartir da segunda linha do arquivo CSV. A primeira são os rótulos linha 0
    linha = linha.strip() # Copia a string de uma linha
    # Remover caracteres especiais do arquivo -  + E AM PM
    linha = linha.replace("No Label", "1")
    linha = linha.replace("E", "0")
    linha = linha.replace("e", "0")
    linha = linha.replace("+", "0")
    linha = linha.replace("-", "0")
    linha = linha.replace(" PM", "")
    linha = linha.replace(" AM", "")
    coluna = linha.split(',')  # Divide cada coluna do dataset em strings separadas pela virgula (,) E monta uma lista de Strings
    label = coluna[-1]   # Recebe o valor da ultima coluna o Label = Bening ou Algum Ataque

    # Renove linha com cabeçalho duplicados, com valores Infinity e valores NaN
    if linha.startswith('Dst') or linha.find('Infinity') >= 0 or linha.find('infinity') >= 0 or linha.find('NaN') >= 0:
        linhasApagadas += 1
        continue

    # Remover caracteres especiais do arquivo -  + E AM PM
    linha = linha.replace("No Label", "1")
    linha = linha.replace("E", "0")
    linha = linha.replace("e", "0")
    linha = linha.replace("+", "0")
    linha = linha.replace("-", "0")
    linha = linha.replace(" PM", "")
    linha = linha.replace(" AM", "")
    
    # Converter Data para valor numerico  com datetime
    data = parser.parse(coluna[6])  # '1/3/18 8:17'     #Seleção do valor da coluna TimeStanp
    conversao = (data - datetime.datetime(1970, 1, 1)).total_seconds() # Conversão da valor da coluna TimeStamp
    coluna[6] = str(conversao)  # Coluna Time Stamp recebe o novo valor convertido
    linha = ','.join(coluna)  # linha recebe o novo valor # Linha completa
    
    contador += 1
    
    # If para selecionar a primeira linha a ser salva
    if label in salvarDados:
        salvarDados[label].append(linha)
        
    else:
        salvarDados[label] = [linha]
        

with open(saida, 'w') as saidaCSV:
    #saidaCSV.write(dados[0])  # Salva a primeira linha do CSV - Rotulos dos atributos
    for label in salvarDados:
        linha = '\n'.join(salvarDados[label])
        saidaCSV.write('{}\n'.format(linha))

        print()
        #print(linha)
        print()

print("")
print("Processo Finalizado!")
print("")
print('Linhas Salvas = {}.'.format(contador))
print("")
print('Linhas Apagadas = {}.'.format(numeroLinhas - contador))
print("")
print("Fim da Execução")



# Converter ataques em Binário

#dados = pd.read_csv(saida) # Carrega o dataset PreProcessado anteriormente

#dados = shuffle(dados) # Misturar o conjunto de dados

#dados.drop_duplicates() # Remover duplocados

# Converte os Label em binário - Bening = 0 e Ataque = 1
#dados['Label'] = dados['Label'].map(
#    {'Benign': 0, 'Attak': 1})
    
# Salva o novo Dataset Binário
# Header = False - Remove os Rotulos o Cabeçalho do Dataframe 
#dados.to_csv(saidaBinario, header=False, index=False)  # Remove a primeira linha do Dataset. Linha dos Rotulos - Label  




