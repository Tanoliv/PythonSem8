#Модуль  вывода оценок

import pandas as pd #Импортируем библиотеку Pandas.
import numpy as np

def gl_foonc():
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

    def out_ball():
        file= open(filename, 'r', encoding='UTF-8')
        sps=file.readlines()
        file.close 
        sps= ' '.join(sps)
        print(sps)
        return sps
    out_ball()
    print(out_ball())
#gl_foonc()