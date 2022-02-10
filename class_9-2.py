#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:47:54 2022

@author: zionn
"""

# list
mylist = [1, 3, 5, 7, 9]
for i in mylist:
    print(i)
    
# dict
house_2 = {'Cherry': '0999', 'Dora': '5678'}
for k in house_2:
    print(k)
    
for v in house_2.values():
    print(v)
    
#print(house_2.values())

print('\n')

for k, v in house_2.items():
    print(k, v)