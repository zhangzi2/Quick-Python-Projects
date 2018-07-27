# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:15:38 2016

@author: kevinzhang
"""

#1
A = float(10)
B = float(15)
C = 35.74+0.6215*A-35.75*B**0.16+0.4275*A*B**0.16
print("Temperature (degrees F): ", A)
print("Wind Speed (mph): ", B)
print("Wind Chill Temperature Index: ", C)

A = float(0)
B = float(25)
C = 35.74+0.6215*A-35.75*B**0.16+0.4275*A*B**0.16
print("Temperature (degrees F): ", A)
print("Wind Speed (mph): ", B)
print("Wind Chill Temperature Index: ", C)

A = float(-10)
B = float(35)
C = 35.74+0.6215*A-35.75*B**0.16+0.4275*A*B**0.16
print("Temperature (degrees F): ", A)
print("Wind Speed (mph): ", B)
print("Wind Chill Temperature Index: ", C)

#2

temp_str = input("enter a temperature: " )
temp_flt = float(temp_str)

wind_str = input("enter a wind speed: ")
wind_flt = float(wind_str)

A = temp_flt
B = wind_flt
C = 35.74+0.6215*A-35.75*B**0.16+0.4275*A*B**0.16

print("Temperature (degrees F): ", A)
print("Wind Speed (mph): ", B)
print("Wind Chill Temperature Index: ", C)




