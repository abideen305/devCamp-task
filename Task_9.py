#!/usr/bin/env python
# coding: utf-8


#To determine if a word is palindrome or not

'''
This program will take in a word and reverse it to tell if a word is a palindrome or not.
INPUT: madam
OUTPUT: madam is palindrome
'''
#defining my function using isPalindrome().
def isPalindrome():
#picking a variable intake to take input from user
#Using lower method to convert the input from user to lower case
    intake = input("Write a word:" ).lower()
#reversing input from user using negative indexing. The reversing has been set to variable palindrome
    palindrome = intake[::-1]
#if statement to validate input and the reversing
    if intake == palindrome:
#return statement if the above statement is true
        print("Yes, {} is a palindrome".format(intake))
    else:
        print("No, {} is not a palindrome".format(intake))
#calling the function, isPalindrome().
isPalindrome()

# I will be putting an input statement just to ensure the script display result
# before closing
input("Enter q to close")




