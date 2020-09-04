#!/usr/bin/env python
# coding: utf-8

# In[16]:


# function that accepts an array of positive integers and returns an array of all prime numbers

num = 7
for i in range(2,num):
#An if statement to validate if the i % num is equal to zero 
       if (num % i) == 0:
#printing not a prime number if the above condition is true. 
        print(num,"is not a prime number")
        break
#an else statement to print otherwise if the above statement is not true
else:
    print(num,"is a prime number")

