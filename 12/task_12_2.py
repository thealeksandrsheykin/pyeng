# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
import ipaddress


def check_ip(ip):
      '''
      Функция проверяет корректность IP-адреса.Если адрес корректный возвращает True,
      а иначе False.
      ip - IP-адрес ввиде кортежа диапозонов: [1.1.1.1,3],[172.21.41.128,172.21.41.132]
      '''

      try:
            ipaddress.ip_address(ip)
            return True
      except ValueError:
                  return False


     

      

def convert_ranges_to_ip_list(list_of_ips):
      '''
      Функция конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.
      list_of_ips - список IP-адресов и/или диапозон IP-адресов.
      '''
      result = list()
      for ips in list_of_ips:
            if '-' in ips:
                  ip1,ip2 = ips.split('-')
                  if ip2.isdigit():
                        *other,start = ip1.split('.')
                        end = ip2
                        ip2 ='{}.{}'.format('.'.join(other),ip2)
                  else:
                        *other1,start = ip1.split('.')
                        *other2,end = ip2.split('.')
                        if other1 == other2: other = other1
                        else: continue
                  if check_ip(ip1) and check_ip(ip2):
                        for i in range(int(start),int(end)+1):
                              result.append('{}.{}'.format('.'.join(other),str(i)))
                  else: continue
            else:
                  if check_ip(ips):
                        result.append(ips)
                  else: continue
      return result
            
 


if __name__ == '__main__':
      list_of_ips = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
      ips = convert_ranges_to_ip_list(list_of_ips)
      print(ips)
      

