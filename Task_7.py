#!/usr/bin/env python
# coding: utf-8


#To calculate Standard Deviation of an array

"""
In this task, I will be importing statistics modules in python since we were not restricted

"""
#importing statistics modules with an alias of st
import statistics as st

#Setting my array with a variable called num

num = [2,3,4,5,6,7]

#Invoking the stdev function in python using 'sd' as the variable name to hold it.

sd = st.stdev(num)

print(sd)

# I will be putting an input statement just to ensure the script display result
# before closing
input("Enter q to close: ")



