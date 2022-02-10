#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:30:18 2022

@author: zionn
"""

datas = {'A001': ['小熊軟糖', 20],
         'A002': ['冰棒', 25],
         'A004': ['王子麵', 10],
         'A006': ['汽水', 30]}

while True:
    ans = int(input("1.查詢貨號\n2.結束查詢系統\n請輸入:"))
    if ans == 1:
        num = input('請輸入貨號：')
        
        if num not in datas:
            print('貨號：{} 不存在'.format(num))
            new = input('如果要新增商品請打 Y: ')
            if new == 'Y':
                name = input('請輸入品項：')
                money = int(input('請輸入售價：'))
                datas[num] = [name, money]
                d = datas.get(num)
                print(d)
                print('貨號：{} 品項：{} 價格：{}元'.format(num, d[0], d[1]))
        else:
            print('品項：{} 價格：{}元'.format(datas[num][0], datas[num][1]))
    elif ans == 2:
        break
    else:
        print('輸入錯誤，請重新輸入!')