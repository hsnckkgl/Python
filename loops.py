# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:00:13 2020

@author: hsn
"""

for i in range(10):
    print(i)
    
for i in range(10):
    print(i,end=' ')

for i in range(1,10):
    print(i,end=' ')
    
help(range)

for i in range(0,100,3):
    print(i,end=' ')
    
for i in range(100,0,-3):
    print(i,end=' ')
    
word = 'python'
for i in word:
    print(i,end=' ')

word = 'python'    
for char in word: #char can be anything like i
    print(char)
    
x = 5
x = x + 1
print('x =',x)

x = 5
x += 1 #same as x = x + 1
print('x =',x)

# While Loops

n = 10
while n > 0:
    print(n)
    n = n-1

userInput = int(input('Please write the ages of students. To the end type -1: '))
ages = []
while userInput > 0:
    ages.append(userInput)
    userInput = int(input('The next age: '))
print('The ages of students are :',ages)
    
count = 0
classNames = []
name = input('Please enter the name type n to stop: ')
while name != 'n':
    count += 1
    classNames.append(name)
    print(f'{name} has been added.')    # f is the new print method
    name = input('Next name: ')
print(f'There are {count} people in the class, they are {classNames}')

# Modulus
# FizzBuzz

n = 100
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:   # If this statement is not written on the top, we have never got 'FizzBuzz'
        print(i,': FizzBuzz')
    elif i % 3 == 0:
        print(i,': Fizz')
    elif i % 5 == 0:
        print(i,': Buzz')
    else:
        print(i)

# Exercises
# First exercise
        
num1 = int(input('Please enter first number between 1 and 100: '))
num2 = int(input('Please enter second number between 1 and 100: '))

while num1 < 0 or num2 < 0 or num1 > 100 or num2 > 100 or num1 == num2:
    print('Number must be different values between 1 and 100, try again')
    num1 = int(input('Please enter a number between 1 and 100: '))
    num2 = int(input('Please enter a number between 1 and 100: '))
if num1 < num2:
    for i in range(num1,num2+1):
        print(i,end=' ')
else:
    for i in range(num2,num1+1):
        print(i,end=' ')
        
# Second exercise

word = input('Please enter a word: ')
reverseString = ''
for char in word:
    reverseString = char + reverseString # Order of these variables is crucial!!!
print(reverseString)
print(word[::-1]) # Easy way to do it

# Third exercises

userInput = input('Please enter a number between 1 and 12: ')
while (not userInput.isdigit() or int(userInput) < 1 or int(userInput) > 12):
    print('Please enter a valid number between 1 and 12: ')
    userInput = input('Please make a selection: ')
userInput = int(userInput)
print('=============================')
print()
print(f'This is the {userInput} times table')
print()

for i in range(1,13):
    print(f'{i} * {userInput} = {i * userInput}')

# Forth exercise
    
n = int(input('Please write a number to factorial: '))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
    
# Fifth exercise(Fibonacci)

n = 20
a = 0
b = 1

fibNumbers = []
for i in range(n):
    fibNumbers.append(a)
    a,b = b,a+b
print(f'The first {n} Fibonacci numbers are {fibNumbers}. ')
    
# Sixth exercise

n = 100
odds = []
evens = []

for i in range(n):
    if i % 2 == 0:
        evens.append(i)
    elif i % 2 == 1:
        odds.append(i)
print(f'The odds are: {odds}')
print(f'The evens are: {evens}')















