# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command_output):
      '''
      Функция обрабатывает вывод команды show cdp neighbors.
      command_output - ожидает как аргумент вывод одной строкой (не имя файла)
      '''
      result = dict()
      for i in command_output.split('\n'):
            if '>' in i:
                  local = i.split('>')[0]
            elif 'Eth' in i or 'Fa' in i:
                  tmp_list = i.split()
                  tmp_str = ' '.join(tmp_list)
                  remote,ltype,lport,_,_,_,_,_,rtype,rport= i.split()
                  local_port=ltype+lport
                  remote_port=rtype+rport
                  result[(local,local_port)] = (remote,remote_port)
            else: continue
      return result
            
            
            
      
if __name__ == '__main__':
      with open('sh_cdp_n_sw1.txt','r') as file:
            data = file.read()
      ports = parse_cdp_neighbors(data)
      for i,j in ports.items():
            print(i,j)
