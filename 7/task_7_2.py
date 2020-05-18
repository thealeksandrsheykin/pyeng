# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

data = argv[1]


with open(data, 'r+') as file:
      for i in file:
            if i.startswith('!'):continue
            else: print(i.strip(' \n'))
