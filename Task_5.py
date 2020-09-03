#!/usr/bin/env python
# coding: utf-8

#Task 5
#To replace all spaces with %20
#I will be using a function for re-usable sake
"""
In this task, we are to write a program to take in input and replace the spaces with %20. 
Input: "Mr John Smith " 
Output: "Mr%20John%20Smith"
"""
#Defining my function using noSpace().
def noSpace():
#Setting a variable name to take input from the user
    name = input("Write a short sentence with spaces:")
#replacing spaces from the input with %20 using replace method.
    result = name.replace(" ", "%20")
#printing the result
    print (result)
#calling the function
noSpace()


# I will be putting an input statement just to ensure the script display result
# before closing
input("Enter q to close:  ")





