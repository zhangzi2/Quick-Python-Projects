# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:01:36 2016

@author: kevinzhang
"""
#Lab 03, CSE 231 online section 730, May 24, 2016#

n = int(input('Enter an integer (enter zero to terminate): '))

count_odd = int(0) #list of variables set initially to 0
count_even = int(0)
count_pos = int(0)
sum_odd = int(0)
sum_even = int(0)

while n != 0: #as long as n is not 0, the loop continues 

    if n > 0: #specifies that counting and summing only occurs when n is positive
        count_pos += 1
        if n%2 == 1:
            count_odd += 1
            sum_odd += n
        else:
            count_even += 1
            sum_even += n
    else:
        print('Negative integer entered, please enter a positive integer.')
         
    print('Entered integer: ', n) #displays all calculations 
    print('Odd count: ', count_odd)   
    print('Odd sum: ', sum_odd)
    print('Even count: ', count_even)     
    print('Even sum: ', sum_even)
    print('Positive integer count: ', count_pos)
    n = int(input('Enter another integer: '))
    
print('done')





