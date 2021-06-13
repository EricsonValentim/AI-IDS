import time
ini = time.time() # Time Execution

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


# Função para carregar o Dataset
def load_data(data, feat_name):
    df= pd.read_csv(data, names=feat_name, low_memory=False)
    return df


colunas_dataset = ['Timestamp', 'Flow Duration', 'Tot Fwd Pkts',
              'Tot Bwd Pkts', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts', 'Fwd Pkt Len Max',
              'Fwd Pkt Len Min', 'Fwd Pkt Len Mean', 'Fwd Pkt Len Std',
              'Bwd Pkt Len Max', 'Bwd Pkt Len Min', 'Bwd Pkt Len Mean',
              'Bwd Pkt Len Std', 'Flow Byts/s', 'Flow Pkts/s', 'Flow IAT Mean',
              'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Tot',
              'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min',
              'Bwd IAT Tot', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max',
              'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags',
              'Bwd URG Flags', 'Fwd Header Len', 'Bwd Header Len', 'Fwd Pkts/s',
              'Bwd Pkts/s', 'Pkt Len Min', 'Pkt Len Max', 'Pkt Len Mean',
              'Pkt Len Std', 'Pkt Len Var', 'FIN Flag Cnt', 'SYN Flag Cnt',
              'RST Flag Cnt', 'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt',
              'CWE Flag Count', 'ECE Flag Cnt', 'Down/Up Ratio', 'Pkt Size Avg',
              'Fwd Seg Size Avg', 'Bwd Seg Size Avg', 'Fwd Byts/b Avg',
              'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg',
              'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg', 'Subflow Fwd Pkts',
              'Subflow Fwd Byts', 'Subflow Bwd Pkts', 'Subflow Bwd Byts',
              'Init Fwd Win Byts', 'Init Bwd Win Byts', 'Fwd Act Data Pkts',
              'Fwd Seg Size Min', 'Active Mean', 'Active Std', 'Active Max',
              'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min', 'Label']


data_frame = load_data('C:/Aula/Mestrado/Entrada/arquiveCICFlowMeterPreprocessing.csv', colunas_dataset) #Sample Path Windows 10


atributos_preditores = ['Timestamp', 'Flow Duration', 'Tot Fwd Pkts',
              'Tot Bwd Pkts', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts', 'Fwd Pkt Len Max',
              'Fwd Pkt Len Min', 'Fwd Pkt Len Mean', 'Fwd Pkt Len Std',
              'Bwd Pkt Len Max', 'Bwd Pkt Len Min', 'Bwd Pkt Len Mean',
              'Bwd Pkt Len Std', 'Flow Byts/s', 'Flow Pkts/s', 'Flow IAT Mean',
              'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Tot',
              'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min',
              'Bwd IAT Tot', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max',
              'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags',
              'Bwd URG Flags', 'Fwd Header Len', 'Bwd Header Len', 'Fwd Pkts/s',
              'Bwd Pkts/s', 'Pkt Len Min', 'Pkt Len Max', 'Pkt Len Mean',
              'Pkt Len Std', 'Pkt Len Var', 'FIN Flag Cnt', 'SYN Flag Cnt',
              'RST Flag Cnt', 'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt',
              'CWE Flag Count', 'ECE Flag Cnt', 'Down/Up Ratio', 'Pkt Size Avg',
              'Fwd Seg Size Avg', 'Bwd Seg Size Avg', 'Fwd Byts/b Avg',
              'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg',
              'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg', 'Subflow Fwd Pkts',
              'Subflow Fwd Byts', 'Subflow Bwd Pkts', 'Subflow Bwd Byts',
              'Init Fwd Win Byts', 'Init Bwd Win Byts', 'Fwd Act Data Pkts',
              'Fwd Seg Size Min', 'Active Mean', 'Active Std', 'Active Max',
              'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min']



atributo_target = ['Label']

x = data_frame[atributos_preditores].values

y = data_frame[atributo_target].values

# 20% do dataset para teste
split_test_size = 0.20

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = split_test_size, random_state = 0)

print("")
print (x_treino.shape)
print (x_teste.shape)
print("")
print (y_treino.shape)
print (y_teste.shape)

print("")


from sklearn.neural_network import MLPClassifier

model = MLPClassifier(solver='adam', alpha=0.001, hidden_layer_sizes=(5,), random_state=1, learning_rate='constant',
                    learning_rate_init=0.01, max_iter=200, activation='logistic', momentum=0.9, verbose=True, tol=0.0001)


from sklearn.preprocessing import  StandardScaler

scaler = StandardScaler()
scaler.fit(x_treino)
x_treino = scaler.transform(x_treino)
x_teste = scaler.transform(x_teste)


# salvar modelo
import pickle
#salvar o modelo (mlp_model) no arquivo rfModel.pkl
with open('C:/Aula/Mestrado/Saida/MLP-Model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Carregar modelo
with open('C:/Aula/Mestrado/Saida/MLP-Model.pkl', 'rb') as f:
    modelLoad = pickle.load(f)
        
model = modelLoad


model.fit(x_treino, y_treino.ravel())

pred = model.predict(x_teste)

print("---------------------------------------")

print("Score :", model.score(x_teste, y_teste))

print("---------------------------------------")


from sklearn import metrics

#MLP_predict_train = model.predict(x_treino)

#print ("Exatidão Acuracy Treino: {0:0.8f}".format(metrics.accuracy_score(y_treino, MLP_predict_train)))
#print("")

rf_predict_test = model.predict(x_teste)

print ("Exatidão Acuracy Teste: {0:0.8f}".format(metrics.accuracy_score(y_teste, rf_predict_test)))
print("")

print("Benign: 0")
print("Attak: 1")
print()

#from IPython.display import Image

print('Confusion Matrix')

print("{0}".format(metrics.confusion_matrix(y_teste, MLP_predict_test)))
print("")

print("Classification Report")

print(metrics.classification_report(y_teste, MLP_predict_test, labels = [0, 1]))


from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)

accuracy = accuracy_score(y_teste, pred)
recall = recall_score(y_teste, pred , average="weighted")
precision = precision_score(y_teste, pred , average="weighted")
f1 = f1_score(y_teste, pred, average="weighted")
print("----------------------------------------------")
print("accuracy")
print("%.8f" %accuracy)
print("precision")
print("%.8f" %precision)
print("racall")
print("%.8f" %recall)
print("f1score")
print("%.8f" %f1)

print("")


fim = time.time()
fim = fim - ini
fim = round(fim, 2)
print ("Tempo Total de Execução: ", fim)

