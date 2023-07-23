import model as dg
import view as view
import controller

dg.start()  # генерация базы данных
controller.init_data_base('base_phone.csv')  # Модуль работы с базой данных
view.ls_menu()  # Модуль пользовательского интерфейса
