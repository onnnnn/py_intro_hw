#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:50:34 2022

@author: zionn
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

position = mc.player.getTilePos()
x, y, z = position
