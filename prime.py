# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:55:53 2022

@author: kaieu
"""

def prime():
    li = [True] * 1001
    li[0] = False
    li[1] = False
    n = 2
    while (n <= 1000):
        if(li[n] == True):
           for i in range(n ** 2, 1001, n):
               li[i] = False
        n+=1
        continue
    for p in range(1001):
        if li[p]:
            print(p)

prime()