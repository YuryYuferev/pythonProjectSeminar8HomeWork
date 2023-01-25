from logger import data_student, honers_list, journal_ball_student, oliVali, print_place, search_data, search_data_name, student_place

def interface():
    print('Для получения данных выберите пункт от 1 до 8.\n'
          '1. Добавление данных ученика в базу данных\n'
          '2. Добавление ученика в таблицу рассадки в кабинетах\n'
          '3. Таблица рассадки учеников в кабинетах\n'
          '4. Вывод данных учеников школы\n'
          '5. Поиск ученика по имени в табл. рассадки\n'
          '6. Поиск данных ученика по имени\n'
          '7. Журнал оценок учеников всей школы\n'
          '8. Список отличников')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 8:
        print('Неверное значение, повторите')
        command = int(input("Введите номер операции: "))
    if command == 1:
        oliVali()
    elif command == 2:
        student_place()
    elif command == 3:
        print_place()
    elif command == 4:
        data_student()
    elif command == 5:
        search_data()
    elif command == 6:
        search_data_name()
    elif command == 7:
        journal_ball_student()
    elif command == 8:
        honers_list()
interface()
