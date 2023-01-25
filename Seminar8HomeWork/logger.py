from input_data import Number_cab, Variant_desk, Desk, Name, Surname, Age, Nomer_clas
import pandas as pd
import numpy as np
# Данные ученика
# Добавление данных ученика в базу данных
def oliVali():
    old_data_frame = pd.read_csv('data_student.csv')
    new_record = pd.DataFrame (
    {"Name":[Name()],
    "Surname":[Surname()],
    "Nomer clas":[Nomer_clas()],
    "Age":[Age()]})
    old_data_frame = pd.concat([old_data_frame,new_record])
    print(old_data_frame)
    old_data_frame.to_csv('data_student.csv', index=False)
# Добавление ученика в таблицу рассадки в кабинетах
def student_place():
    old_data = pd.read_csv('data_pr.csv')
    new_data = pd.DataFrame (
    {"Name":[Name()],
    "Surname":[Surname()],
    'Number_cab':[Number_cab()],
    'Variant_desk':[Variant_desk()],
    'Desk':[Desk()]})
    old_data = pd.concat([old_data,new_data])
    print(old_data)
    old_data.to_csv('data_pr.csv', index=False)
# Таблица рассадки учеников в кабинетах
def print_place():
    fd = pd.read_csv('data_pr.csv')
    print ('Рассадка учеников в кабинете.','\n', fd)
    return fd
# Вывод данных учеников школы
def data_student():
    fd1 = pd.read_csv('data_student.csv')
    print ('Данные ученика.','\n',fd1)
    return fd1
#print_place()
# Поиск ученика по имени в табл. рассадки
def search_data():
    df = pd.read_csv('data_pr.csv')
    print(df)
    a = input('Поиск ученика по имени в таблице рассадки: ')
    print(df.loc[df['Name'] == a])
#search_data()
# Поиск данных ученика по имени
def search_data_name():
    df = pd.read_csv('data_student.csv')
    print(df)
    a = input('Поиск данных ученика: ')
    print(df.loc[df['Name'] == a])
# Журнал оценок учеников
def journal_ball_student():
    df_ball = pd.read_csv('data_student.csv')
    del df_ball['Age']
    df_ball["Ball"] = np.nan
    df_ball.fillna(value=90, inplace=True)
    new_record = pd.DataFrame (
    {"Name":['Roma'],
    "Surname":['Ivanov'],
    "Nomer clas":['5v'],
    "Ball":[30]})
    df_ball = pd.concat([df_ball,new_record])
    print(df_ball)
    print(df_ball)
    df_ball.to_csv('Jurnal.csv', index=False)
    return df_ball
# Список отличников
def honers_list():
    df_ball = pd.read_csv('Jurnal.csv')

    df_ball = df_ball[df_ball['Ball'] > 80]
    print(df_ball)
    df_ball.to_csv('Honer_list.csv', index=False)
