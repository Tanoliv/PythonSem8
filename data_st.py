#Модуль формирования списка и дневникв учеников 

import pandas as pd #Импортируем библиотеку Pandas.
import numpy as np


filename = 'students_book.txt'
file= open(filename, 'a', encoding='UTF-8')
file.close

# Ввод имени и фамилии
def first_name():
    first= input('Введите  имя: ')
    slett= first[1:]
    flett= first[0]
    name= flett.upper()+ slett
    first1= []
    first1.append(name)    
    return first1

def last_name():
    first= input('Введите фамилию: ')
    slett= first[1:]
    flett= first[0]
    name= flett.upper()+ slett
    first1= []
    first1.append(name)    
    return first1

def FailName():
    file= input('Введите латиницей имя файла для формирования дневника: ')
    r='.csv'
    file= file.lower() + r  
    return file

def dnevnik():
    firstname= first_name()
    lastname= last_name()
    file= FailName()
    print(file)
    sps_st= {'Фамилия': lastname, 'Имя': firstname}
    data_st= pd.DataFrame(sps_st)
    #print(data_st)

    flname= file
    f= open(flname, 'a', encoding='UTF-8')
    f.write(f'{data_st}\n') 
    f.close
    file=open(filename, 'a', encoding='UTF-8')
    file.write(f'{data_st}\n') 
    print(f'Новая запись в классном журнале:\n {data_st} ')
    return data_st
   
#print(dnevnik())
#dnevnik()