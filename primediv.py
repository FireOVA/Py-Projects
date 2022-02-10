# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:25:30 2022

@author: kaieu
"""

def prime():
    li = [True] * 1001
    li[0] = False
    li[1] = False
    n = 2
    while (n <= 1000):
        for i in range(n+1,1001):
            if i % n == 0:
                li[i]=False
        n+=1
        continue
    for p in range(1001):
        if li[p]:
            print(p)

prime()