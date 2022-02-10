# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:42:35 2022

@author: kaieu
"""

def prime():
    li = [True] * 1001
    li[0] = False
    li[1] = False
    for i in range(1001):
        if i % 2 == 0:
            if i != 2:
                li[i]=False
        elif i % 3 == 0:
            if i != 3:
                li[i]=False
        elif i % 5 == 0:
            if i != 5:
                li[i]=False
        elif i % 7 == 0:
            if i != 7:
                li[i]=False
        elif i % 9 == 0:
            if i != 9:
                li[i]=False
        elif i % 11 == 0:
            if i != 11:
                li[i]=False
        elif i % 13 == 0:
            if i != 13:
                li[i]=False
        elif i % 17 == 0:
            if i != 17:
                li[i]=False
        elif i % 19 == 0:
            if i != 19:
                li[i]=False
        elif i % 23 == 0:
            if i != 23:
                li[i]=False
        elif i % 29 == 0:
            if i != 29:
                li[i]=False
        elif i % 31 == 0:
            if i != 31:
                li[i]=False
   
    for p in range(1001):
       if li[p]:
           print(p)  
         
prime()

