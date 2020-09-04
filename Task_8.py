#!/usr/bin/env python
# coding: utf-8

# In[20]:


"""
Program to count the number of 3s that appear in all the numbers between 0 and n (inclusive)

"""
#defining the function named number_in_range3 with argument number
def number_in_range3(number): 
#setting an empty string of c
    c = "" 
#iterating over range of number from zero
    for i in range(0,number+1):
#setting the string c to the value of i
        c+=str(i) 
#counting 3s and converting it to list
    return(list(c).count('3')) 
#taking a value from the user and storing it to number
  
number = int(input("Enter a number: "))
#storing my function to a variable called count
count = number_in_range3(number)
#printing my value
print('The count of 3s in {} is {}'.format(number,count))

