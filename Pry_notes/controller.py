import csv
import os.path
import random

db_file_name = ''
db = []
global_id = 0


def init_data_base(file_name='base_phone'):

    global global_id
    global db
    global db_file_name

    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if (row[0] != 'ID'):
                    db.append(row)
                    if (int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email=''):  # Поиск по базе данных
    if (name == ''):
        return print("\tНет такого имени в базе данных")
    if (surname == ''):
        return print("\tНет такой фамилии в базе данных")
    if (number == ''):
        return print("Нет такого телефонного номера в базе данных")
    if (email == ''):
        return print("Нет такой электронной почты в базе данных")

    for row in db:
        if (row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("уже существует")
            return
    global global_id
    global_id += 1
    print(random.randint(100, 999))
    new_row = [str(random.randint(100, 999)), name.title(),
               surname.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number='', email=''):
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if (name != '' and row[1] != name.title()):
            continue
        if (surname != '' and row[2] != surname.title()):
            continue
        if (number != '' and row[3] != number):
            continue
        if (email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return print(f'Контакты не найдены')
    else:
        return result


# Обновление данных в базе данных
def update(id='', new_name='', new_surname='', new_number='', new_email=''):
    if (id == ''):
        print('укажите ID для обновления')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if (row[0] == id):
                if (new_name != ''):
                    row[1] = new_name.title()
                if (new_surname != ''):
                    row[2] = new_surname.title()
                if (new_number != ''):
                    row[3] = new_number
                if (new_email != ''):
                    row[4] = new_email.lower()
            writer.writerow(row)


def delete(id=''):  # Удаление данных из базы данных
    if (id == ''):
        return print('укажите ID для удаления')

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    for index, val in enumerate(db, start=1):
        print(index, val)

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)
