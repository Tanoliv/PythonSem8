import data_st as ds
import dob_ball as db
import dob_predmet as dp
import ball_st as bs

filename = 'students_book.txt'
file= open(filename, 'a', encoding='UTF-8')
file.close

filename1 = 'predmet_book.csv'
file1= open(filename1, 'a')
file.close

def main_menu():
    print('МЕНЮ\n')
    print('1. Вывести список учеников')
    print('2. Добавить данные ученика и его дневник')
    print('3. Выставить оценку в дневник')
    print('4 Посмотреть дневник')
    print('5. Добавить предмет')
    print('6. Вывести список предметов')
    print('7. Выйти')
    point= input('Выберите пункт меню: ')
    if point=='1':
        file= open(filename, 'r', encoding='UTF-8')
        sps= file.read()
        if len(sps)==0:
            print('список пуст')
        else:
            
            print(sps)
        file.close
        enter= input('Продолжить - ENTER')      
        main_menu()

    elif point=='2':
       ds.dnevnik()
       enter= input('Продолжить - ENTER')
       main_menu()

    elif point=='3':
       db.main_foonc()
       enter= input('Продолжить - ENTER')       
       main_menu()

    elif point=='4':
       bs.gl_foonc()
       enter= input('Продолжить - ENTER')       
       main_menu()

    elif point=='5':
        dp.dob_pred()
        enter= input('Продолжить - ENTER')
        main_menu() 

    elif point=='6':
        file1= open(filename1, 'r', encoding='UTF-8')
        sps1= file1.read()
        if len(sps1)==0:
            print('список пуст')
        else:
            
            print(sps1)
        file1.close
        enter= input('Продолжить - ENTER')      
        main_menu()

    elif point=='7':
        print('Спасибо')
    else:
        print('Введите корректный пункт меню')
        enter= input('Продолжить - ENTER')
        main_menu() 