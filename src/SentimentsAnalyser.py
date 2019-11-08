import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import cross_val_predict
from openpyxl import Workbook

#Esta base é composta pelas escalas de psicologia
dataset = pd.read_csv('compilado_scalas.csv',encoding='utf-8', delimiter=',')

dataset.head(10)

juncao = pd.read_csv('juncao_final_ifs.csv', delimiter=',')
juncao.head(10)

palavras = juncao.TEXTO.tolist()

dataset.head()

texto = dataset['texto'].values
classes = dataset['classificador'].values

vectorizer = CountVectorizer(analyzer="word")

freq_tweets = vectorizer.fit_transform(texto.astype('U'))

modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

print('Acuracia:' ,metrics.accuracy_score(classes,resultados))
sentimento=[0,1]

print("Precisão, Revocação e Medida f1 de cada classe:\n")
print (metrics.classification_report(classes,resultados,sentimento),)

print("Matriz de Confusão:\n")
print (pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True),'') 

freq_testes = vectorizer.transform(palavras)

classificacao = modelo.predict(freq_testes)

dataset_classificado = pd.DataFrame({'Tweet':palavras,'IF':juncao.IF,'Classificacao':classificacao})

dataset_classificado.loc[dataset_classificado.Classificacao ==0,'Classificacao'] = 'Ansioso'
dataset_classificado.loc[dataset_classificado.Classificacao ==1,'Classificacao'] = 'Feliz'

print(dataset_classificado["Tweet"][0])
print(dataset_classificado["Classificacao"][0])
print(len(dataset_classificado))


workbook = Workbook() #this line is to save it
sheet = workbook.active
count = 1
sheet['A'+str(count)] = "ID"
sheet['B'+str(count)] = "Tweet"
sheet['C'+str(count)] = "Classificacao"

for count in range(0,len(dataset_classificado), 1):
    sheet['A'+str(count+2)] = count
    sheet['B'+str(count+2)] = dataset_classificado["Tweet"][count]
    sheet['C'+str(count+2)] = dataset_classificado["Classificacao"][count]

workbook.save(filename = "sentiments_analysis.xlsx")