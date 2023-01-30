#Модуль добавления предметов

from pathlib import Path

def new_pred():
    first= input('Введите добавляемый предмет: ')
    slett= first[1:]
    flett= first[0]
    name= flett.upper()+ slett
    first1= []
    first1.append(name)    
    return first1
#new_pred()

def dob_pred():

    pred= new_pred()
    pred= ' '.join(pred)  
    directory = Path()
    for path in directory.rglob('*.csv'):
        if path.is_file():
           print(path.name)
           with open(path, 'a', encoding='UTF-8') as file:                 
                 file.write(f'{pred} \n '  )
                 file.write(f' \n '  )
            
            

               
        #return pred
#dob_pred()
