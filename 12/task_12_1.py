# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess
import ipaddress


def ping_ip_addresses(*args):
      '''
      Функция проверяет доступность IP-адресов.
      list_ip - список IP-адресов
      Функция возвращает кортеж состоящий из двух списков:
            - доступных IP-адресов
            - недоступных IP-адресов
      '''

      available = list()
      unavailable = list()
      for ip in args[0]:
            #try:
            #      ipaddress.ip_network(ip)
            #except ValueError:
            #      print('IP - адрес {} введен не корректно...'.format(ip))
            #      continue
            CREATE_NO_WINDOW = 0x08000000
            ping = subprocess.run('ping {}'.format(ip),
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE,
                                  encoding='cp866',
                                  creationflags = CREATE_NO_WINDOW)
            if ping.returncode == 0:
                  available.append(ip)
            else: unavailable.append(ip)
      return (available,unavailable)
          


if __name__ == '__main__':
      list_of_ips = ['1.1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
      result = ping_ip_addresses(list_of_ips)
      print(result)
      
