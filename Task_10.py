#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 10
#To output the most occuring string in a string

#declaring a variable name to hold the string
name = "afhuusnimr443o0sggg"

#importing counter from collections to cout
from collections import Counter
#using most_commont method in counter to find the most common word
c= Counter(name).most_common(1)
#converting the returned list to dictionary and setting it to variable mostCommon
mostCommon = dict(c).keys()
print("Most common letter is: {}".format(mostCommon))


# In[4]:


name = "afhuuusnimr443o0sggg"
all_freq = {} 
for i in name: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)  

print(res)

