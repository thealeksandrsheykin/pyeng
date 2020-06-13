# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sqlite3
import os
import re
import yaml
from tabulate import tabulate

# Default values
DFLT_DB_NAME = 'dhcp_snooping.db'
DFLT_DB_SCHEMA = 'dhcp_snooping_schema.sql'
SWITCH_OF_FILES = ['switches.yml']
DHCP_OF_FILES = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']

def check_exist_db(name):
      '''
      Функция проверяет существует ли БД.
      Функция возвращает True или False.
      name - имя БД.
      '''
      if os.path.exists(name): return False
      else: return True

def create_db(name,schema):
      '''
      Функция создает БД.
      Функция ничего не возвращает.
      name - имя БД.
      schema - схема БД.
      '''
      if check_exist_db(name):
            connect = sqlite3.connect(name)
            with open(schema, 'r') as file:
                  connect.executescript(file.read())
            connect.commit()
            connect.close()
      else: return None

def add_data(db_file,filenames):
      '''
      Функция добавляет данные в таблицу БД dhcp.
      Функция ничего не возвращает.
      db_file - имя БД.
      filenames - список файлов с выводом команды show ip dhcp snooping
      '''
      regex = r'([\w:]+) +([\w\.]+) +\d+ +\S+ +(\d+) +(.*)'
      query = 'INSERT OR REPLACE into dhcp values(?,?,?,?,?,1,datetime(\'now\'))'
      connect = sqlite3.connect(db_file)
      connect.execute('UPDATE dhcp set active = 0')
      tmp = list()
      for file in filenames:
            hostname,*other = file.split('_')
            with open(file, 'r') as data:
                  result = re.finditer(regex,data.read())
            for match in result:
                  tmp_list = list(match.groups())
                  tmp_list.append(hostname)
                  tmp_tuple = tuple(tmp_list)
                  connect.execute(query,tmp_tuple)
      connect.commit()
      connect.close()
      return None

def add_data_switches(db_file,filenames):
      '''
      Функция добавляет данные в таблицу БД switches.
      Функция ничего не возвращает.
      db_file - имя БД.
      filenames - список файлов с описанием коммутатора.
      '''
      query = 'INSERT into switches values(?,?)'
      connect = sqlite3.connect(db_file)
      for file in filenames:
            with open(file, 'r') as data:
                  result = yaml.safe_load(data)
            for i,j in result.items():
                  for key,value in j.items():
                        try:
                              connect.execute(query,(key,value))
                        except sqlite3.IntegrityError as error:
                              print(f'При добавлении данных: {(key,value)} Возникла ошибка: {error}')
      connect.commit()
      connect.close()
      return None


                        
def get_all_data(db_file):
      '''
      Функция формирует запрос на вывод всех данных из таблицы БД dhcp.
      Функция ничего не возвращает
      db_file - имя БД.
      '''
      query = 'SELECT * from dhcp WHERE active = ?'
      data_output_to_screen(db_file,query)
      return None
      
def get_data(db_file,key,value):
      '''
      Функция формирует запрос для вывода данных из таблицы БД dhcp основываясь на параметрах, которые задал пользователь.
      Функция ничего не возвращает.
      db_file - имя БД.
      key,value - два параметра, которые задает пользователь
      '''
      query = 'SELECT * from dhcp WHERE {} = \'{}\' and active = ?'.format(key,value)
      data_output_to_screen(db_file,query)
      return None
      
def data_output_to_screen(db_file,query):
      '''
      Функция выводить данные из таблицы БД dhcp на экран, основываясбь на запросе.
      Функция ничего не возвращает.
      db_file - имя БД
      query - запрос 
      '''
      status = ['Неактивные записи', 'Активные записи']
      connect = sqlite3.connect(db_file)
      cursor = connect.cursor()
      for i in range(1,-1,-1):
            cursor.execute(query,str(i))
            result = cursor.fetchall()
            if result:
                  print(f'\n{status[i]}:\n\n{tabulate(result)}')
            else: pass  
      connect.commit()
      connect.close()
      return None


if __name__ == '__main__':
      create_db(DFLT_DB_NAME,DFLT_DB_SCHEMA)
      add_data(DFLT_DB_NAME,DHCP_OF_FILES)
      add_data_switches(DFLT_DB_NAME,SWITCH_OF_FILES)
      get_all_data(DFLT_DB_NAME)
      get_data(DFLT_DB_NAME,'vlan',10)
