# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:17:21 2022

@author: kaieu
"""

li=[]
t=[]
for i in range(1,25):
    t+=[i]
    if i % 3 == 0: 
        li += [t]
        t = []
        
print(li)

