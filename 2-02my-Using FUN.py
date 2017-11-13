#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:36:32 2017

@author: passionlk
"""
def check_data(data_in):
    valid_input = True

    try:
            data_in = float(data_in)
    except:
            valid_input =  False
    return  valid_input,data_in



Fahrenheit = input("Enter a temperature in Fahrenheit: ")
valid_input,Fahrenheit = check_data(Fahrenheit)

if valid_input ==  True:
    
        Celsius = (Fahrenheit - 32) * 5.0/9.0

        print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " Celsius")
else:
    print("Invalid input.")