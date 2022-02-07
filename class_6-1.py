#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:33:15 2022

@author: zionn
"""

scores = ['chris', 83, 'david', 96, 'bill', 92, 'amy', 59, 'james', 77]

#print(5*2)
#print(len(scores))

# name
for i in range(0, len(scores), 2):
    print(scores[i])
    
# score
for i in range(0, len(scores), 2):
    print(scores[i+1])

# extra
student_name = [scores[i] for i in range(0, len(scores), 2)]
print(student_name)

student_score = [scores[i+1] for i in range(0, len(scores), 2)]
print(student_score)

max_index = student_score.index(max(student_score))
print(student_name[max_index], max(student_score))

min_index = student_score.index(min(student_score))
print(student_name[min_index], min(student_score))