import csv

def output_search():
    data = input('Найти: ').title()
    with open('phone_book.csv', 'r') as f:   # чтение с csv
        data_search = csv.reader(f)
        for row in data_search:
            if data in row:
                print(f'\n{row[0]} {row[1]}\n{row[2]} ({row[3]})')
    # with open('phone_book.txt', 'r', encoding='utf-8') as j:    # чтение с txt
    #     search = j.readlines()
    #     for line in search:
    #         lst = line.split(';')
    #         if data in lst:
    #             print(f'\n{lst[0]} {lst[1]}\n{lst[2]} ({lst[3]})')

def output_all():
    with open('phone_book.csv', 'r') as f:
        data = csv.reader(f)
        for row in data:
            print(f'\n{row[0]} {row[1]}')
            print(f'{row[2]} ({row[3]})')