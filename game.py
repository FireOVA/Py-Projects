# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:30:42 2022

@author: kaieu
"""

import random

num = int(random.randrange(1,1001))
at = 0

def game():
    while True:
        global at
        global num
        print('Number of guesses:', at)
        i = (int(input('Guess a number between 1 and 1000 with the fewest guesses: ')))
             
        if i < num:
            print('Your number is too low, try again.')
            at = at + 1
            continue
        elif i > num: 
                print('Your number is too high, try again.')
                at = at + 1
                continue
        elif i == num:
                print('You got it! You did it in', at, 'attempts.')
                ag = (str(input('Do you want to play again? y/n  ')))
                if ag == 'y':
                    num = int(random.randrange(1,1001))
                    at = 0
                    continue
                else:
                    if ag == 'n':
                        break
                
game()