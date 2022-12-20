from data_input import d_input
import data_output as search
import data_output as all

def phone_book():
    print('Выберите действие. Добавить абонента - 1. Найти абонента - 2. Показать всю телефонную книгу - 3')
    print('Для выхода наджмите "q"')
    while True:
        action = input('\n' + 'Действие: ')
        if action == '1':
            d_input()
        elif action == '2':
            search.output_search()
        elif action == '3':
            all.output_all()
        elif action == 'q':
            break
        else:
            print('Неверный ввод!')