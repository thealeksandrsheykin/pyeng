# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re

def get_ints_without_description(filename):
      '''
      функция обрабатывает конфигурацию и возвращает список имен интерфейсов,
      на которых нет описания(команды description)
      filename - имя файла, в котором находится конфигурация устройства.
      '''
      result = list()
      regex = r'^interface +(?P<interface>\S+)|^ +description +(?P<description>.*)'
      with open(filename, 'r') as f:
            for line in f:
                  match = re.search(regex,line)
                  if match:
                        if match.lastgroup == 'interface':
                              interface = match.group(match.lastgroup)
                              result.append(interface)
                        elif interface:
                              result.remove(interface)          
                  else:continue
      return result
            

if __name__ == '__main__':
      print(get_ints_without_description('config_r1.txt'))
