#-*- coding: utf-8 -*-
#!/usr/bin/env python3

import sqlite3
import yaml
import re
from os import path

def check_db(db_name):
      '''
      Функция проверяет наличие БД. Функция возвращает True или False.
      db_name - имя база данных
      '''
      if path.exists(db_name):
            return True
      else: return False
      

def connect_db(db_name):
      '''
      Функция проверяет существование БД и соединяет с ней.
      Функция возвращает курсор
      db_name - имя базы данных
      '''
      if check_db(db_name):
            connection = sqlite3.connect(db_name)
            return connection
      
def close_db(connect):
      '''
      Функция делает commit всему и завершает соединение с БД.
      Функция ничего не возварщает.
      connect- действующий курсор БД.
      '''
      connect.commit()
      connect.close()


def add_into_table_switches(connect,data):
      '''
      Функция добавляет данные в БД в таблицу switches
      Функция ничего не возварщает.
      connect - курсор из соединения с БД
      data - данные которые нужно добавить
      '''
      query = 'INSERT into switches values (?,?)'
      print('Добавляю данные в таблицу switches...')
      for file in data:
            with open(file, 'r') as f:
                  for key,value in (yaml.safe_load(f)).items():
                        for subkey,subvalue in value.items():
                              try:
                                    connect.execute(query,(subkey,subvalue))
                              except sqlite3.IntegrityError as error:
                                    print(f'При добавлении данных: {(subkey,subvalue)} Возникла ошибка: {error}')
      connect.commit()
      return None
            
                                    
def add_into_table_dhcp(connect,data):
      '''
      Функция добавляет данные в БД в таблицу dhcp
      Функция ничего не возварщает.
      connect - курсор из соединения с БД
      data - данные которые нужно добавить
      '''
      connect.execute('UPDATE dhcp set active = 0')
      query = 'REPLACE into dhcp values (?,?,?,?,?,1,datetime(\'now\'))'
      regex = r'([\w:]+) +([\w\.]+) +\d+ +\S+ +(\d+) +(.*)'
      print('Добавляю данные в таблицу dhcp...')
      for file in data:
            hostname,*other = (path.basename(file)).split('_')
            with open(file, 'r') as f:
                  result = re.finditer(regex,f.read())
            for match in result:
                  tmp_list = list(match.groups())
                  tmp_list.append(hostname)
                  connect.execute(query,(tmp_list))
      connect.commit()
      return None
      


if __name__ == '__main__':
      db_name = 'dhcp_snooping.db'
      data_of_switch = ['switches.yml']
      #data_of_dhcp = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
      data_of_dhcp = ['new_data/sw1_dhcp_snooping.txt', 'new_data/sw2_dhcp_snooping.txt', 'new_data/sw3_dhcp_snooping.txt']
      connect = connect_db(db_name)
      if connect:
            add_into_table_switches(connect,data_of_switch)
            add_into_table_dhcp(connect,data_of_dhcp)
            close_db(connect)
      else: pass
      
      


