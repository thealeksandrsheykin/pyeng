# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology

def create_network_map(filenames):
      '''
      Функция обрабатывает вывод команды show cdp neighbors из несколько файлов и обхединяет его в одну общую топологию.
      filenames - список с именами файлов, в которых находится вывод команды show cdp neighbors.
      '''
      result = dict()
      for file in filenames:
            with open(file, 'r') as data:
                  for i in data:
                        if '>' in i:
                              local = i.split('>')[0]
                        elif 'Eth' in i:
                              remote,ltype,lport,*other,rtype,rport = i.split()
                              local_port = '{}{}'.format(ltype,lport)
                              remote_port = '{}{}'.format(rtype,rport)
                              key = (local,local_port)
                              value = (remote,remote_port)
                              if not result.get(value):
                                    result[key] = value
                        else: continue
      draw_topology(result)
      return result


if __name__ == '__main__':
      filenames = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt']
      ports = create_network_map(filenames)
      for i,j in ports.items():
            print(i,j)
      
      
