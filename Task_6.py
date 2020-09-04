#!/usr/bin/env python
# coding: utf-8

# In[6]:


#program to determine if three first numbers add up to a value
def addThree(array, b):
    """
This program will evaluate an array, then add any three number then check if it sums up to another value stored as b
Input: [1, 2, 3, 4, 5, 6], 6
Output: [1, 2, 3]
    """
#setting my iteration to zero using variable count, total of the three array
#variable new list for an empty array to print the array if it sums up to b
    count = 0
    total = 0
    newList = []
#for loop to iterate over the array
    for i in array:
#incrementing my count by 1
        count +=1
#setting the value of i to total
        total +=i
#appending value of i to new List
        newList.append(i)
#checking if the count is 3
        if count ==3:
#breaking out of the loop
            break
#evaluating if the total equals b
    if total == b:
#printing newList
        print(newList)
#else statement to print -1 if the above is false
    else:
        print(-1)

#calling the function
addThree([1,2,3,4,5,6],6)



    


# In[ ]:




