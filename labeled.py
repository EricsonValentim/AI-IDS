import csv
import sys
import datetime
from dateutil import parser
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

# Artigo

in = 'C:/AI-IDS/Sample/In/captureCSV-CICFlowMeter.csv'

out = 'C:/AI-IDS/Sample/Out/labeled.csv'

# Converter ataques em Binário

data = pd.read_csv(in) # Carrega o arquivo gerado pelo CICFlowMeter

data = shuffle(data) # Misturar o conjunto de dados

data.drop_duplicates() # Remover duplocados

# Converte os Label em binário - Tráfego Bening = 0 e Tráfego de Ataque = 1
data['Label'] = data['Label'].map(
    {'No Label': 0})

#data['Label'] = data['Label'].map(
#    {'No Label': 1})
    
# Salva o novo Dataset Binário
# Header = False - Remove os Rotulos o Cabeçalho do Dataframe 
data.to_csv(out, header=True, index=False)  # Remove a primeira linha do Dataset. Linha dos Rotulos - Label 
