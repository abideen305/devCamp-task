#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importing regular expression to parse through the inpus
special=['$','@','#']
import re
#defining the function using validation()

def validation():
#setting while loop to always be true
    while True:
#taking input from the user and storing it to a value called password
        password = input("Enter a password: ")
#searching through the password using search method in re to know if it does not contain a string
        if re.search('[A-Za-z]',password) is None:
#printing 1 and break the loop
            print(1)
            break
#searching through the password using search method in re to know if it does not contain a a number
        elif re.search('[0-9]',password) is None: 
            print(0)
            break
        elif re.match('[0-9A-za-z]',password) == password: 
            print(2)
            break
        else:
            print(3)
            break

validation()

