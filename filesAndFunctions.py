# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:34:17 2020

@author: hsn
"""

# Open or create file

file = open('kipling.txt','w')   # 'w' => write, 'r' => read, 'a' => append
print(type(file))
file.write('I am Hasan Cokakoglu.\n')
file.write('I am a junior ethical hacker.\n')
file.close()  # Do not forget to close the file

file = open('kipling.txt','r')  # 'r' is read mode
print(file.read())
file.close()    # Do not forget to close the file

file = open('kipling.txt','r')
print(file.readline())      # readline() : Only first line
file.close()

file = open('kipling.txt','r')
print(file.readlines())     # readlines() : Write all file as "list"
print(type(file))

content = file.readlines()
print(type(content))    # "List"
file.close()

file = open('kipling.txt','a')  # 'a' is append mode (everytime when we run this code block, it keep append it)
file.write('I am appending this sentence.')
file.close()

file = open('kipling.txt','r')  # 'r' is read mode
print(file.read())
file.close()
print()

with open('kipling.txt','r') as file:   # Easy way of it
    for line in file.readlines():   # We do not have to worry about closing file
        print(line,end='')
        
# F u n c t i o n s

def hello():    # (syntax): def nameoftheFunction()
    print('Hello World!')
hello()     # To call and execute the function!

for i in range(5):
    hello()

def hi(name):   # name is argument of this function! 
    print(f'Hi, {name}!')
hi('Hasan')
hi('Melek')
hi()    # Required an argument!

def hi2(name='Hasan'):
    print(f'Hi, {name}!')
hi2()   # Does not need argument because we put the argument before.
hi2('Melek')    # Now we changed the argument
hi2()   # It will give predefined argiment again!

def fib(n):     # The header of the function
    
    ''' Calculates and returns nth fibonacci number ''' # This is docstring that explains the function!
    
    a = 0       # The body of the function
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a

fibNum = fib(20)
print(fibNum)

for i in range(20):
    print(fib(i))

def calcMean(first,*reminder):  # * is for unknown amount of argument! It can handle all of them.
    '''
    This function calculates mean of numbers
    '''
    mean = (first + sum(reminder)) / (1 + len(reminder))
    print(type(reminder))
    return mean
print(calcMean(14,25,36,87,56,95))

# Recursion

def fib2(n):    # The function is keep calling itself until finish!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-2) + fib2(n-1)    # Use a lot of memory and hard to calculate, inefficient method!
    
x = fib2(35)    # Has much delay until calculate it!!!
print(x)

y = fib(1000) # This is the first function fib() 
print(y)    # Much more faster than recursive method!!!

import timeit

t1 = timeit.Timer("fib(36)","from greetings import fib") # We call fib() from greetings.py !!!
print(t1.timeit(5))

t2 = timeit.Timer("fib2(36)","from greetings import fib2") # We import fib2() from greetings.py !!!
print(t2.timeit(5))
