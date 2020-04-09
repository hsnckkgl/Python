# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:59:50 2020

@author: hsn
"""

myList1 = [1,2,3,4]
myList2 = ['a','b','c','d']

joined = list(zip(myList1,myList2))     # Combine those variables in a list
print(f'The result of the zip function is {joined} it is of type {type(joined)}')

i,j = zip(*joined)  # Make them tuples(demet)

capitals = {'France':'Paris', 'Spain':'Madrid', 'Greece':'Athens', 'Germany':'Berlin',
            'United Kingdom':'London', 'South Korea':'Seul',
            'Turkey':'Ankara'}

x,y = zip(*capitals.items())    # zip with * unpack it into two seperate tuples!!!
print(x,y)      # x is key, y is value



