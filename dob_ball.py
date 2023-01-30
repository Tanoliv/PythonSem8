#Модуль выставления и вывода оценок

import pandas as pd #Импортируем библиотеку Pandas.
import numpy as np

def main_foonc():

    filename1=input('Введите фамилию ученика латиницей: ')
    #print(type(filename1))
    r='.csv'
    filename2= filename1.lower() + r
    #print(filename2)

    filename = filename2
    file= open(filename, 'r', encoding='UTF-8')
    sps=file.readlines()
    file.close
    #print(sps)
    #print(sps[5])

    predmet= input('Введите предмет: ')
    slett= predmet[1:]
    flett= predmet[0]
    predmet= flett.upper()+ slett
    first1= []
    first1.append(predmet)

    def index():
    
        pattern = predmet
        for i in range(len(sps)):
            if pattern in sps[i]:
            #print(i)
            #print(sps[i])
                return i
    index()
    i=index()

    #print(sps[i])
    #print(type(sps[i]))
    ball= input('Введите оценку: ')
    text= f'{sps[i]}: {ball}'
    def replace_line():
        lines = open(filename, 'r', encoding='UTF-8')
        lines= lines.readlines()
        lines[i] = text
        out = open(filename, 'w', encoding='UTF-8')
        out.writelines(lines)
        out.close()
        print(lines)
    replace_line()
    print(replace_line)

   
#main_foonc()
