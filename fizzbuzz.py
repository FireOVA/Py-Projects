# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:49:16 2022

@author: kaieu
"""

for i in range(1,101):
    if i % 15 == 0: 
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)