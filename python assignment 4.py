#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.
# 
# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.
# 
# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
# 
# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[7]:


import functools


# In[29]:


"""1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass"""

class AreaTriangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_area(self):
        """using the Herons formula find the triangle area using 2 steps step1 : find the s '
        half of the triangles perimeter'step 2: find the area """
        s = (self.a + self.b + self.c)/2
        area = (s*(s-(self.a))*(s-(self.b))*(s-(self.c))) ** 0.5
        return f"the area of the triangle of {self.a},{self.b},{self.c} is {area}"


# In[30]:


a1 = AreaTriangle(5,5,5)
print(a1.get_area())
a2 = AreaTriangle(10,12,15)
print(a2.get_area())


# In[31]:


a,b,c = 10,12,15
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)


# In[9]:


"""1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n."""



number = int(input(" enter the number : "))
a = ["tommy", "baker", "alen","farmer","mathew","tylor"]
list(filter(lambda a: a if len(a)>number else 0, a))


# In[10]:


"""2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list."""

a = ["tommy", "baker", "alen","farmer","mathew","tylor"]
list(map(lambda a: len(a) if a else False, a))


# In[2]:


"""2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise."""

def check_vowel():
    char_in = input("enter the charecter : ")
    if len(char_in) == 1:
        vowel = ["a", "e", "i", "o", "u"]
        if char_in in vowel:
            return True , "the char is in vowel"
        else:
            return False , "its not a vowel"
    else:
        print("enter a single char")

check_vowel()

