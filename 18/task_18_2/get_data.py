#-*- coding: utf-8 -*-
#!/usr/bin/env python3

import sqlite3
from tabulate import tabulate
from os import path
from sys import argv


def check_db(db_name):
      '''
      Функция проверяет наличие базы данных в директории.
      Функция возвращает True или False
      db_name - имя БД.
      '''
      if path.exists(db_name): return True
      else: False
      
def check_args(connection,args):
      '''
      Функция проверяет существует аргумент заданный пользователем в БД.
      Функция проверят количество аргументов введенных пользователем и если аргументов
      больше двух, то выводит сообщение, что скрипт поддерживает только два или ноль аргументов
      Функция возвращает True или False
      connection - соединение с БД.
      args - списко аргументов введенные пользователем
      '''
      if len(args) == 0:
            return True
      elif len(args) == 2:
            name,value = args
            cursor = connection.execute('SELECT * from dhcp')
            header = list(map(lambda i: i[0], cursor.description))
            if name in header:
                  return True
            else:
                  print('Данный параметр не поддерживается.')
                  print('Допустимые значения параметров: {}'.format(','.join(header)))
                  return False
      else:
            print('Пожалуйста, введите два или ноль аргументов')
            return False


def create_connection(db_name):
      '''
      Функция cоздает соединение с БД. Функция возвращает
      данное соединение.
      db_name - имя БД.
      '''
      if check_db(db_name):
            return sqlite3.connect(db_name)
      else: return None

def close_connection(connection):
      '''
      Функция закрывает соединение с БД. Функция ничего не возвращает.
      connection - соединение с БД.
      '''
      connection.close()
      return None

def select_data_from_db(connection,args):
      '''
      Функция отправляет запрос в БД для выдачи информации из нее.
      Если нет аргументов, то выводит все содержимое таблицы dhcp
      Если с двумя аргументами, выводит информацию из таблицы dhcp, которая соответствует полю и значению.
      connection - соединение с БД.
      args - список аргументов предоставляемые пользователем.
      '''
      if check_args(connection,args):
            cursor = connection.cursor()
            if not args:
                  print('В таблице dhcp такие записи:')
                  query = 'SELECT * from dhcp'
                  print(tabulate(cursor.execute(query)))  
            else:
                  print('Информация об устройствах с такими параметрами: {}'.format(' '.join(args)))
                  query = 'SELECT * from dhcp WHERE {} = \'{}\''
                  print(tabulate(cursor.execute(query.format(*args))))
                        

      else: return None




if __name__ == '__main__':
      db_name = 'dhcp_snooping.db'
      args = argv[1:]
      connection = create_connection(db_name)
      if connection:
            select_data_from_db(connection,args)
            close_connection(connection)
      else: pass
