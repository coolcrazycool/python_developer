import pandas as pd
import csv
import logging


# получим логгер для нашего приложения либо создадим новый, если он еще не создан (паттерн Синглтон)
logger_s = logging.getLogger("covid_19_success")
logger_s.setLevel(logging.INFO)
logger_e = logging.getLogger("covid_19_errors")
logger_e.setLevel(logging.INFO)

# опишем, куда и как будем сохранять логи: зададим файл и формат
handler_success = logging.FileHandler('success.log', 'a', 'utf-8')
handler_errors = logging.FileHandler('errors.log', 'a', 'utf-8')

formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")

# установим файлу нужный формат, а нужный файл - логгеру
handler_success.setFormatter(formatter)
handler_errors.setFormatter(formatter)
logger_s.addHandler(handler_success)
logger_e.addHandler(handler_errors)


class patient():
    def __init__(self, name=None, surname=None, birth_date=None, phone_numb=None, doc_type=None, doc_numb=None):
        self.name = name_check(name) if name != None else None
        self.surname = surname_check(surname) if surname != None else None
        self.birth_date = birth_check(birth_date) if birth_date != None else None
        self.phone_numb = number_check(phone_numb) if phone_numb != None else None
        self.doc_type = doc_type_check(doc_type) if doc_type != None else None
        self.doc_numb = doc_numb_check(doc_numb, self.doc_type) if doc_numb != None else None
        logger_s.info('New Patient was added')

    def create(self, name=None, surname=None, birth_date=None, phone_numb=None, doc_type=None, doc_numb=None):
        self.name = name_check(name)
        self.surname = surname_check(surname)
        self.birth_date = birth_check(birth_date)
        self.phone_numb = number_check(phone_numb)
        self.doc_type = doc_type_check(doc_type)
        self.doc_numb = doc_numb_check(doc_numb, self.doc_type)
        logger_s.info('New Patient was added')

    def save(self):
        pass

def number_check(phone):
    white_lts = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for symbol in phone:
        if symbol not in white_lts:
            phone = phone.replace(symbol, '')
    if phone.startswith('8'):
        phone = '7' + phone[1:]
    if not phone.startswith('+'):
        phone = '+' + phone
    if len(phone) > 12:
        raise Exception()
    return phone

def birth_check(birth):
    month_dict = {'Января':'01', 'Февраля':'02', 'Марта':'03', 'Апреля':'04', 'Мая':'05', 'Июня':'06', 'Июля':'07',\
                  'Августа':'08', 'Сентября':'09', 'Октября':'10', 'Ноября':'11', 'Декабря':'12'}
    for symbol in birth:
        if symbol == ' ':
            birth = birth.replace(symbol, '.')
    birth_lst = birth.split('.')
    if len(birth_lst[0]) == 1:
        birth_lst[0] = '0' + birth_lst[0]
    if len(birth_lst[1]) == 1:
        birth_lst[1] = '0' + birth_lst[1]
    elif not birth_lst[1].isdigit():
        birth_lst[1] = month_dict[birth_lst[1].title()]
    if len(birth_lst[2]) == 2 and int(birth_lst[2]) > 20:
        birth_lst[2] = '19' + birth_lst[2]
    elif len(birth_lst[2]) == 2 and int(birth_lst[2]) <= 20:
        birth_lst[2] = '20' + birth_lst[2]
    return birth_lst[0] + '.' + birth_lst[1] + '.' + birth_lst[2]

def name_check(name):
    black_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for symbol in name:
        if symbol in black_lst:
            raise Exception()
    return name.title()

def surname_check(surname):
    black_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for symbol in surname:
        if symbol in black_lst:
            raise Exception()
    return surname.title()

def doc_type_check(doc_type):
    white_lst = ['Паспорт', 'Водительские Права', 'Заграничный Паспорт']
    if not doc_type.title() in white_lst:
        raise Exception()
    return doc_type.title()

def doc_numb_check(doc_numb, doc_type):
    if doc_type == "Водительские Права" and doc_numb != None:
        for symbol in doc_numb:
            if symbol == ' ':
                doc_numb = dock_numb.replace(symbol, '')
        if len(doc_numb) > 10:
            raise Exception()
        return doc_numb[:2] + ' ' + doc_numb[2:4] + ' ' + doc_numb[4:]
    elif doc_type == "Паспорт" and doc_numb != None:
        for symbol in doc_numb:
            if symbol == ' ':
                doc_numb = dock_numb.replace(symbol, '')
        if len(doc_numb) > 10:
            raise Exception()
        return doc_numb[:4] + ' ' + doc_numb[4:]
    elif doc_type == "Заграничный Паспорт" and doc_numb != None:
        for symbol in doc_numb:
            if symbol == ' ':
                doc_numb = dock_numb.replace(symbol, '')
        if len(doc_numb) > 9:
            raise Exception()
        return doc_numb[:2] + ' ' + doc_numb[2:]
    else:
        raise Exception()


class LoggException(Exception):
    def __init__(self):
        pass