# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re

def parse_sh_cdp_neighbors(data):
      '''
      Функция обрабатывает вывод команды show cdp neighbors. Функция возвращает словарь, который
      описывает соединение между устройствами.
      data - вывод команды(show cdp neighbours) одной строкой.
      '''
      
      regex = (r'(\S+)[>|#]'
               r'|([\w]+) +([\S ]+?) +\d+ +[\w ]+? +\d+ +(.*)')

      result = dict()
      for match in re.findall(regex,data):
            if match[0]:
                  key = match[0]
                  result[key] = dict()
            else:
                  result[key][match[2]] = {match[1]:match[3]}
      return result


if __name__ == '__main__':
      with open('sh_cdp_n_sw1.txt', 'r') as file:
            print(parse_sh_cdp_neighbors(file.read()))
