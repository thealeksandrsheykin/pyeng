# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re

def parse_sh_ip_int_br(filename):
      '''
      Функция обрабатывает вывод команд show ip int br и возвращает такие поля:
            * Interface
            * IP-address
            * Status
            * Protocol
      filename - имя файла, в котором находися вывод команды show ip int br
      '''

      regex = r'(\S+) +([\w.]+) +\S+ +\S+ +(up|down|administratively down) +(up|down)'
      with open(filename, 'r') as file:
            result = re.finditer(regex,file.read())
      return [i.groups() for i in result]

                  
                  

if __name__ == '__main__':
      print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
