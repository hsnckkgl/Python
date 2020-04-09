# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 04:01:45 2020

@author: hsn
"""

# We can export all these functions. (Syntax): from (fileName) greetings import (functionName) fib

def fib(n):     # The header of the function
    
    ''' Calculates and returns nth fibonacci number ''' # This is docstring that explains the function!
    
    a = 0       # The body of the function
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a

def fib2(n):    # The function is keep calling itself until finish!
    
    ''' Recursive function '''
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-2) + fib2(n-1)
