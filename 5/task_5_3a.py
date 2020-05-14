# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')

ports = {'access':{'template': access_template, 'msg': 'Введите номер VLAN: '},
         'trunk': {'template': trunk_template,  'msg': 'Введите разрешенные VLANs: '}}

vlans = input((ports.get(mode)).get('msg'))

print('\n'+ '-'*30)
print('interface {}'.format(interface))
print('\n'.join((ports.get(mode)).get('template')).format(vlans))

