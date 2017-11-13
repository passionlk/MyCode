#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:50:55 2017

@author: passionlk
"""
valid_input = True

Fahrenheit = input("Enter a temperature in Fahrenheit: ")

try:
      Fahrenheit = float(Fahrenheit)
except:
    valid_input =  False

if valid_input ==  True:
    
        Celsius = (Fahrenheit - 32) * 5.0/9.0

        print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " Celsius")
else:
    print("Invalid input.")