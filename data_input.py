import csv

def d_input():
    data_user = []
    data_user.append(input('\n' + 'Введите фамилию: ').title())
    data_user.append(input('Введите имя: ').title())
    data_user.append(input('Введите телефон: '))
    data_user.append(input('Введите описание: '))
    with open('phone_book.csv', 'a', newline='') as f:
        p_book = csv.writer(f)
        p_book.writerow(data_user)
    with open('phone_book.txt', 'a', newline='', encoding='utf-8') as j:
        j.write(';'.join(map(str, data_user)))