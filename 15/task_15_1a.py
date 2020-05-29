# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re


def get_ip_from_cfg(file):
      '''
      Функция обрабатывает конфигурацию и возвращает словарь:
            * ключ: имя интерфейса
            * значение: кортеж с двумя строками:
                    * IP-адрес
                    * маска
      file - имя файла, в котором находится конфигурация устройства.
      '''
      result = dict()
      regex = (r'interface (?P<interface>\S+)'
               r'|ip address (?P<ip>[\w.]+)\s(?P<mac>[\w.]+)')
      with open (file, 'r') as f:
            for line in f:
                  match = re.search(regex,line)
                  if match:
                        if match.lastgroup == 'interface':
                              key = match.group(match.lastgroup)
                        elif key:
                              value = (match.group('ip'),match.group('mac'))
                              result[key] = value
                  else: continue
      return result

                  

if __name__ == '__main__':
      print(get_ip_from_cfg('config_r1.txt'))
