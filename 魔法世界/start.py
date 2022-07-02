#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:39:10 2022

@author: zionn
"""

from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()  # magic spell

a = 0
while a < 5: 
    #print('hello world')
    a = a + 1
    
number = random.choice([1, 3, 5])

#print(number)
#print(number + 10)

a = 0
while a < 10:
    number = random.choice([1, 1, 1, 1, 1, 1, 3, 5])
    #print(number)
    a += 1

#print(random.randint(1, 6))

time.sleep(3)
x, y, z = mc.player.getTilePos()
steps = random.randint(8, 20)
mc.player.setTilePos(x+steps, y, z)












