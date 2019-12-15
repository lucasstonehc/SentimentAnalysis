import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import tkinter
import matplotlib
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from collections import defaultdict
import re

matplotlib.use('TkAgg')
centroids = None

def has_days_in_month(month):
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return months[month]

def acc_minutes(): #this function return to us the month before the currently month
    months_acc = []
    months_acc.append(0)
    sum_minutes = 0

    for month in range(1,13,1):
        minutes = has_days_in_month(month) * 1440 # return to us days and calc minutes into the month
        sum_minutes += minutes 
        months_acc.append(sum_minutes)

    return months_acc
        
def day_month_transform(day, month):
    #ax + y(b-1)
    #a = day 
    #b = month
    #months_acc is a vector to save all accumulated values of month in minutes
    months_acc = acc_minutes()
    minutes =  1440
    if(month == 1):
        return day*minutes
    else:
        return (day*minutes) + months_acc[month-1]

def k_means_get_anxiety_twitters():
    months = []
    words = {
        'Prova de Proficiência':1,
        'Avaliação Global':2,
        'Avaliação Área Técnica':3,
        'Avaliação Global  - Fim 1ª Etapa':4,
        'Conselho de Classe da 1ª Etapa':5,
        'OBMEP 1ª fase':6,
        'OBMEP':7,
        'Conselho de Classe da 2ª Etapa':8,
        'Conselho de Classe':9,
        'Semana Nacional C&T':10,
        'Semana Nacional':11,
        'Mostra de Profissões/Feira de Ciências':12,
        'Mostra de Profissões':13,
        'Feira de Ciências':14,
        'Preparação para Recuperação':15,
        'Recuperação':16,
        'Exames Finais':17,
        'Apresentações de TCC':18,
        'Reunião de Pais/Responsáveis de alunos':19,
        'Encontro de Pais e Mestres - Resultados 1º trim':20,
        'Encontro de Pais e Mestres':21,
        'Recuperação Final':22,
        'Retorno das férias':23,
        'Proficiência e Aproveitamento de Estudos':24,
        'Proficiência':25,
        'Data final para lançamentos notas de recuperação':26,
        'lançamentos de notas':27,
        'Atividades Avaliativas':28,
        'Prova':29,
    }

    data = pd.read_csv('cluster_calenders.csv', delimiter=',', error_bad_lines=False, encoding='utf-8')

    x = []
    y = []

    size = len(data)
    for i in range(1,size, 1):
        #here to transform to one date
        day = data.iloc[i][0]
        month = data.iloc[i][1]
        x.append(day_month_transform(day,month))
        for word in words:
            match = re.search(word, data.iloc[i][2])
            if(match):
                y.append(words[word])

    arr =  np.empty((size,2))
    for i in range(0,size-1,1):
        arr[i][0] = x[i] 
        arr[i][1] = y[i]
        #print(arr[i][0]," ", arr[i][1])
    # X is day
    # Y is date 
    #ax + y(b-1)
    #a = day 
    #b = month
    #vector one to month currently
    #vector two to minutes 
   
    clustering = DBSCAN(eps=12, min_samples=4).fit(arr)
    k = len(list(dict.fromkeys(clustering.labels_)))

    Kmean = KMeans(n_clusters=k)
    Kmean.fit(arr)
    centroids = Kmean.cluster_centers_
    #here started code to show the elements
    '''
    print(centroids)
    plt.xlabel("Metrica")
    plt.ylabel("Targets of calenders")
    plt.scatter(arr[ : -1 , 0], arr[  : -1, 1], s = len(arr), c = 'b')
    for i in range(0,len(centroids),1):
        plt.scatter(centroids[i][0], centroids[i][1], s= len(arr), c='g', marker='s')
    plt.show()
    '''
    #prints days
    for i in range(0,len(centroids),1):
        #print('day ',int(centroids[i][0]/1440))
        #print('Month', int((centroids[i][0]/1440)/30))
        months.append(int((centroids[i][0]/1440)/30))

    #to do comparation
    #totally of twitters - (anxiety twitters + date twitters)
    return months
'''
if __name__ == '__main__':
    #kmeans_with_month()
    for month in k_means_get_anxiety_twitters():
        print(month)
''' 