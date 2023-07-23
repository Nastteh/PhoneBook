import os
import controller as cr
import model as hc
import html_create as hc
os.system('CLS')
print('\n\tВы работаете с базой данных Люди - Номера телефонов - Адрес эл.почты')


def ls_menu():  # Модуль пользовательского интерфейса
    while True:
        print('\nДоступны следующие действия :')
        print('0. Показать все записи в базе данных.')
        print('1. Поиск по ID-номеру.')
        print('2. Поиск по фамилии.')
        print('3. Поиск по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись в базу данных.')
        print('6. Изменить существующую запись в базе данных.')
        print('7. Удалить запись из базы данных.')
        print('8. Закрыть программу.\n')
        n = сhecking_the_number(input('Что сделать для Вас ? :'))

        if n == 0:
            data_list = cr.retrive()
            for index, val in enumerate(data_list, start=1):
                print(index, val)

        elif n == 1:
            search = input('Введите ID-номер: ')
            print(cr.retrive(id=search))

        elif n == 2:
            search = input('Введите фамилию: ')
            print(cr.retrive(surname=search))

        elif n == 3:
            search = input('Введите имя: ')
            print(cr.retrive(name=search))

        elif n == 4:
            search = input('Введите номер  телефона: ')
            print(cr.retrive(number=search))

        elif n == 5:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            email = input('Введите электронную почту: ')
            cr.create(name, surname, number, email)

        elif n == 6:
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            print('4. Поиск по ID-номеру ')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                search = input('Введите фамилию: ')
                cr.retrive(surname=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                search = input('Введите имя: ')
                cr.retrive(name=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                search = input('Введите номер телефона: ')
                cr.retrive(number=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            elif change == 4:
                search = input('Введите ID-номер: ')
                cr.retrive(id=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                cr.update(id=user_id, new_number=new_number)

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            print('4. Поиск по ID-номеру.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                search = input('Введите фамилию: ')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            elif deleting == 2:
                search = input('Введите имя: ')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            elif deleting == 3:
                search = input('Введите номер телефона: ')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            elif deleting == 4:
                search = input('Введите ID-номер: ')
                print(cr.retrive(id=search))
                user_id = input('Введите id записи: ')
                cr.delete(id=user_id)

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            print('\n\tРабота программы завершена!')
            data_list = cr.retrive()
            # Создание HTML-файла с базой данных со всеми изменениями
            hc.create_html_file(data_list)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'base_phone.csv')
            os.remove(path)  # Удаление базы данных после окончания работы
            break
        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
