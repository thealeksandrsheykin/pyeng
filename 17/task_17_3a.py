# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""

import re
import yaml


def generate_topology_from_cdp(list_of_files,save_to_filename=None):
      '''
      Функция обрабатывает вывод команды show cdp neighbor из нескольких файлов и возвращает словарь, который
      описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.
      list_of_files - список файлов из которых надо считать вывод команды show cdp neighbor
      save_to_filename - имя файла в формате YAML, в который сохранится топология.
            * значение по умолчанию None
      '''
      result = dict()
      regex = (r'(\S+)[>|#]'
               r'|([\w]+) +([\S ]+?) +\d+ +[^\d]+ +\S+ +(.*)')
      for file in list_of_files:
            with open(file, 'r')as src:
                  for line in src:
                        match = re.search(regex,line)
                        if match:
                              if match.group(1):
                                    key = match.group(1)
                                    result[key] = dict()
                              else:
                                    result[key][match.group(3)] = {match.group(2):match.group(4)}
                        else: continue
      if save_to_filename:
            with open(save_to_filename, 'w') as dst:
                  yaml.dump(result,dst)
      else: pass
      return result
                 

if __name__ == '__main__':
      list_of_files = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_r4.txt','sh_cdp_n_r5.txt','sh_cdp_n_r6.txt']
      for i,j in generate_topology_from_cdp(list_of_files,'result.yaml').items():
            print(i,j)
            
      

