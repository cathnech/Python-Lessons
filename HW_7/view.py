import data

def start_menu():
    oper = int(input('Что вы хотите сделать? Выберете вариант\n1 - добавить запись\n2 - удалить запись\n3 - редактировать запись\n4 - вывести записи на экран'))
    if oper == 1:
        data.write_data()
    elif oper == 2:
        data.delet_data()
    elif oper == 3:
        data.edit_data()
    elif oper == 4:
        data.read_all_data()

def end_menu():
    oper = int(input('Вы хотите продолжить? да/нет'))
    if oper == 'да':
        start_menu()
    elif oper == 'нет':
        print('Bye!')
 

