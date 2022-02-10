#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:52:21 2022

@author: zionn
"""

house = {}
print(house)

house['Alice'] = '1004'
print(house)

house['Alice'] = '1009'
print(house)

print(house['Alice'])

house['Bob'] = '0213'
print(house)

house['Sunny'] = '1167'
print(house)

#house.pop('Alice')
#print(house)
print('#'*20, '\n')

# extra
print(len(house))

print('Sunny' in house)

house_2 = {'Cherry': '0999', 'Dora': '5678'}
print(house_2)

house.update(house_2)
print(house)

print(house_2)