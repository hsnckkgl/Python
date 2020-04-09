# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:23:34 2020

@author: hsn
"""

myTuple = (1,2,3,4)     # Unchangable (Once tuples have been assigned!)
myList = [5,6,7,8]      # Changable
myString = 'Australia'  # Unchangable

print(myTuple[0])
print(myTuple[:3])

myList[0] = 1000
print(myList)

myTuple[0] = 1000
print(myTuple)      # Gives error because tuples are unchangable

myString[0] = 'a'     # Unchangable too!!!
print(myString)

