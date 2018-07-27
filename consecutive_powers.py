# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:40:51 2016

@author: kevinzhang
"""

def squares(start, terms):
    return sum([i**2 for i in range(start, terms+1)])

def cubes(start, terms):
    return sum([i**3 for i in range(start, terms+1)])
    
user_str = input('Enter a command: ')
if user_str == 'squares':
    start_sq = int(input('Enter a starting integer: '))
    terms_sq = int(input('Enter the number of terms: '))
    result = squares(start_sq, terms_sq)
    print(result)
else:
    print('***Invalid Choice***')
    user_str = int(input('Try again: '))
if user_str == 'cubes':
    start_cb = int(input('Enter a starting integer: '))
    terms_cb = int(input('Enter the number of terms: '))
    result = squares(start_cb, terms_cb)
    print(result)
else:
    print('***Invalid Choice***')
    user_str = int(input('Try again: '))
if user_str == 'exit':
    print('Program halted normally')
else:
    print('***Invalid Choice***')
    user_str = int(input('Try again: '))    


    