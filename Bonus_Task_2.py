#!/usr/bin/env python
# coding: utf-8

# In[4]:


# program to replace a consonant with its next concosnant 

#Starting by definig what is vowel and what is not. Vowel are just: a,e,i,o,u

#defining a function with the name vowel and its argument v
def vowel(v): 
#if statement to taste if the word containing any of the letters of vowel
    if (v != 'a' and v != 'e' and 
        v != 'i' and v != 'o' and 
        v != 'u'): 
#the program should return false is it doesn't
        return False
#returning true if the word containings vowel letter(s)
    return True

#Now to have a function to replace a consonant 
#Here, I am defining my function with the name replaceConsonants and argument c
def replaceConsonants(c): 
      
#looping through range of the length of c 
    for i in range(len(c)): 
        if (vowel(c[i])==False): 
#replacing z with b and not a
            if (c[i] == 'z'): 
                c[i] = 'b' 
#an else statement to defining another condition if the argument is not z
            else: 
#here I am replacing the consonant with the next one with the method ord
                c[i] = chr(ord(c[i]) + 1)
# checking and relacing the word if the next word above is a vowel. No two consecutive word is a vowel in alphabet
                if (vowel(c[i])==True): 
                    c[i] = chr(ord(c[i]) + 1) 
                    
  
    return ''.join(c)
  
# taking input from the user for word to replace its consonants 
# and converting it to lowercase using .lower method
c = input("Enter a sentence to replace its consonants: ")

#storing my function in a variable called string and converting it to list

string = replaceConsonants(list(c))

#replacing ! with nothing because by default the program will replace any space with exclamation
string = string.replace("!", " ")
#printing final result
print(string)

