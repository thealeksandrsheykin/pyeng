#-*- coding: utf-8 -*-
#!/usr/bin/env python3

import sqlite3
import os

def check_db(db_name):
      '''
      Функция - проверяет существует ли БД. Если нет, то возвращает False иначе True
      db_name - имя базы данных, которую нужно проверить.
      '''
      if os.path.exists(db_name): return False
      else: return True
            

def create_db(db_name):
      '''
      Функция проверяет существует ли база данных и если существует,
      то сообщает об этом, а если нет создает её. Функция ничего не возвращает.
      db_name - имя базы данных которую нужно создать.
      '''

      if check_db(db_name):
            print(f'Creating database {db_name} ...')
            connection = sqlite3.connect(db_name)
            connection.commit()
            connection.close()
      else: print(f'Database {db_name} already exist...')
      return None

def write_schema_into_db(db_name,db_schema):
      '''
      Функция согласно описанию схемы БД должна наполнить БД.
      Функция ничего не возвращает.
      db_name - имя базы в которую нужно записать схему
      db_schema - схема которую нужно записать в БД
      '''
      
      connection = sqlite3.connect(db_name)
      with open(db_schema, 'r') as file:
            schema = file.read()
      try:
            connection.executescript(schema)
      except sqlite3.OperationalError as error:
            print(f'Error occurred: {error}')
            pass
      connection.commit()
      connection.close()
      return None

if __name__ == '__main__':
      DB_NAME   = 'dhcp_snooping.db'
      DB_SCHEMA = 'dhcp_snooping_schema.sql'
      create_db(DB_NAME)
      write_schema_into_db(DB_NAME,DB_SCHEMA)


