#!/usr/bin/env python
# coding: utf-8
"""
Writing a program to calculate sum of even and odd number in an array.
"""
#setting an array using variable num
num = [11,13,75,3,43,56]

#defining my function using numbers().
def numbers():
#setting my even and odd count to 0
    even = 0
    odd = 0
#Using for loop to iterate over the list
    for i in num:
#using if statement to define even number. If the remainder of any number divides by 2 is zero then
#it must be an even number otherwise is odd.
        if i%2==0:
#adding any even number to a variable called even
            even = even + i
#An else if statemet if the if statement is false, ie odd.
        elif i%2==1:
#adding any odd number to a variable called odd
            odd = odd + i
#storing the total even numbers and odd numbers to a variable array_sum and converting it to list
        array_sum = even, odd
    print(list(array_sum))
numbers()


# I will be putting an input statement just to ensure the script display result
# before closing
input("Enter q to close:  ")


