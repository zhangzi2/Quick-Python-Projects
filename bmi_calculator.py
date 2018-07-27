# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:45:05 2016

@author: kevinzhang
"""
#CSE 231 section 730, 6/9/16


infile = open('data.txt', 'r')
outfile = open('output.txt', 'w')
heightSum = 0
weightSum = 0
bmiSum = 0
headCount = 0
min_height = float(1000)
min_weight = float(1000)
min_bmi = float(1000)
max_height = float(0)
max_weight = float(0)
max_bmi = float(0)
for line in infile:
    colName = line.split()[0]
    colHeight = line.split()[1]
    colWeight = line.split()[2]
    
    if colName == 'Name':
        print('{:<12}{:<14}{:<14}{:<10}'.format('Name', 'Height(m)', 'Weight(kg)', 'BMI'),\
        file = outfile)
    else:    
        bmi = float(colWeight)/float(colHeight)**2
        i = float(colHeight)
        j = float(colWeight)
        k = float(bmi)
        print('{:<12}{:<14}{:<14}{:<10.2f}'.format(colName, colHeight, colWeight, bmi),\
        file = outfile)
        heightSum += i
        weightSum += j
        bmiSum += k
        headCount += 1
        if float(colHeight) < float(min_height):
            min_height = float(colHeight)
        if float(colWeight) < float(min_weight):
            min_weight = float(colWeight)
        if float(bmi) < float(min_bmi):
            min_bmi = float(bmi)
        if float(colHeight) > float(max_height):
            max_height = float(colHeight)
        if float(colWeight) > float(max_weight):
            max_weight = float(colWeight)
        if float(bmi) >float(max_bmi):
            max_bmi = float(bmi)
            
print('')
heightAvg = heightSum/headCount
weightAvg = weightSum/headCount
bmiAvg = bmiSum/headCount
print('{:<12}{:<14.2f}{:<14.2f}{:<10.2f}'.format('Average', heightAvg, weightAvg, bmiAvg),\
file = outfile)
print('{:<12}{:<14.2f}{:<14.2f}{:<10.2f}'.format('Min', min_height, min_weight, min_bmi),\
file = outfile)
print('{:<12}{:<14.2f}{:<14.2f}{:<10.2f}'.format('Max', max_height, max_weight, max_bmi),\
file = outfile)
outfile.close()