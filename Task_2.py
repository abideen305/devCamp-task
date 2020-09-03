#!/usr/bin/env python
# coding: utf-8



#program to know if a positive number is a prime or not

#picking a variable named num 
num = 20
#using for loop from 2 since 1 is not a prime number from knowledge of mathematics
#I set the range from 2 to the number set

for i in range(2,num):
#An if statement to validate if the i % num is equal to zero 
       if (num % i) == 0:
#printing not a prime number if the above condition is true. 
        print(num,"is not a prime number")
        break
#an else statement to print otherwise if the above statement is not true
else:
    print(num,"is a prime number")


# # I will be putting an input statement just to ensure the script display result
# before closing
input("Enter q to close:  ")







