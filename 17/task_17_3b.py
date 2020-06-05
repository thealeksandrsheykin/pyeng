# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import yaml
from draw_network_graph import draw_topology

def transform_topology(filename):
      '''
      Функция преобразует топологию в формат подходящий для функции draw_topology. Функция возвращает словарь такого вида:
            {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
             ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}
      filename - имя файла в формате YAML, в котором хранится топология.
      '''
      result = dict()
      with open(filename, 'r') as src:
            data = yaml.load(src)
            for key,val in data.items():
                  for subkey,subval in val.items():
                        if result.get(list(subval.items())[0]):
                              continue
                        else:
                              result[(key,subkey)] = list(subval.items())[0]
      draw_topology(result)
      return result
                     

if __name__ == '__main__':
      for i,j in transform_topology('topology.yaml'):
            print(i,j)
