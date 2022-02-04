# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:08:49 2022

@author: kaieu
"""

i = int(input('Please enter a number: '))

if i % 4 == 0:
    print('The number is even and divisible by 4')
elif i % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
    
num = int(input('Please enter a number: '))
check = int(input('Please enter a number: '))

if num % check == 0: 
    print('The numbers are divisible')
else:
    print('The numbers are not divisible')