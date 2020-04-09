# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 02:10:25 2020

@author: hsn
"""

import math

print(math.pi)
print(math.cos(0))

import random # Or
import random as r
# print(random.randint(1, 100))
for i in range(100):
    print(random.randint(1,100),end=' ')

import webbrowser

# Dictionaries

capitals = {'France':'Paris', 'Spain':'Madrid', 'Greece':'Athens', 'Germany':'Berlin',
            'United Kingdom':'London', 'South Korea':'Seul',
            'Turkey':'Ankara'} # Turkey:keys, Ankara:values, Both:items
print(capitals['Germany'])
print(capitals.get('Germany'))
capitals['South Korea'] = 'Seoul' # Changing the value of key
print(capitals['South Korea'])
print(capitals.items())

print(capitals.keys())
print(capitals.values())

for country in capitals:
    print(country)

for country,city in capitals.items():
    print(f'The capital of {country} is {city}')
    
if 'France' in capitals:
    print('It contains France')

L = [1,2,3,4,5,6]
print(2 in L)   # It will give Boolean expression 


# Text analyse

sherlock = '''Mr. Sherlock Holmes

IN THE year 1878 I took my degree of Doctor of Medicine of the University of London, 
and proceeded to Netley to go through the course prescribed for surgeons in the Army. 
Having completed my studies there, I was duly attached to the Fifth Northumberland 
Fusiliers as assistant surgeon. The regiment was stationed in India at the time, 
and before I could join it, the second Afghan war had broken out. On landing at Bombay, 
I learned that my corps had advanced through the passes, and was already deep in the enemy's 
country. I followed, however, with many other officers who were in the same situation 
as myself, and succeeded in reaching Candahar in safety, where I found my regiment, 
and at once entered upon my new duties.

The campaign brought honours and promotion to many, but for me it had nothing but 
misfortune and disaster. I was removed from my brigade and attached to the Berkshires,
with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder 
by a Jezail bullet, which shattered the bone and grazed the subclavian artery. 
I should have fallen into the hands of the murderous Ghazis had it not been for 
the devotion and courage shown by Murray, my orderly, who threw me across a 
packhorse, and succeeded in bringing me safely to the British lines.
'''

letterCount = {}
for letter in sherlock:     # Classic method
    letterCount[letter.lower()] = letterCount.get(letter,0) + 1
print(letterCount)

import matplotlib.pyplot as plt

x,y = zip(*letterCount.items())     # To plot a graph
plt.bar(x,y)
plt.show()

letterCountClean = {}
for k,v in letterCount.items():
    if k.isalpha():
        letterCountClean[k] = v
print(letterCountClean)     # Show only letters

x,y = zip(*letterCountClean.items())
plt.bar(x,y)
plt.show()

countries = {'France':{'capital':'Paris','language':'French'},
              'Spain':{'capital':'Madrid','language':'Spanish'},
              'Greece':{'capital':'Athens','language':'Greek'},
              'Germany':{'capital':'Berlin','language':'German'},
              'United Kingdom':{'capital':'London','language':'English'},
              'South Korea':{'capital':'Seoul','language':'Korean'},
              'Turkey':{'capital':'Ankara','language':'Turkish'}}

print(countries['France'])

for key,value in countries.items():
    print(key,value)

for key,value in countries.items():
    print(f'{value["capital"]} is the capital of {key}, they speak {value["language"]}.')

sherlock = '''Mr. Sherlock Holmes

IN THE year 1878 I took my degree of Doctor of Medicine of the University of London, 
and proceeded to Netley to go through the course prescribed for surgeons in the Army. 
Having completed my studies there, I was duly attached to the Fifth Northumberland 
Fusiliers as assistant surgeon. The regiment was stationed in India at the time, 
and before I could join it, the second Afghan war had broken out. On landing at Bombay, 
I learned that my corps had advanced through the passes, and was already deep in the enemy's 
country. I followed, however, with many other officers who were in the same situation 
as myself, and succeeded in reaching Candahar in safety, where I found my regiment, 
and at once entered upon my new duties.

The campaign brought honours and promotion to many, but for me it had nothing but 
misfortune and disaster. I was removed from my brigade and attached to the Berkshires,
with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder 
by a Jezail bullet, which shattered the bone and grazed the subclavian artery. 
I should have fallen into the hands of the murderous Ghazis had it not been for 
the devotion and courage shown by Murray, my orderly, who threw me across a 
packhorse, and succeeded in bringing me safely to the British lines.
'''

from collections import Counter

print(Counter(sherlock.lower()))

newDict = dict(Counter(sherlock.lower()))   # It makes a dictionary

newDict = {k:v for k,v in newDict.items() if k.isalpha()}   # Only letters
print(newDict)

L = [x**2 for x in range(1,11)]     # for loop in a single line
print(L)

# Question 1

capitals = {'France':'Paris', 'Spain':'Madrid', 'Greece':'Athens', 'Germany':'Berlin',
            'United Kingdom':'London', 'South Korea':'Seul',
            'Turkey':'Ankara'}
userInput = input('Which country would you like to check? :')
userInput = userInput.lower()

while('france' not in userInput and not userInput.isalpha()):
    if userInput == 'spain':
        break
    print('You must input a string!')
    userInput = input('Which country would you like to check? :')
    
userInput = userInput.title()

if userInput in capitals:
    print(f'The capital of {userInput} is {capitals[userInput]}')
else:
    print('No data available!')
    
# Question 2 (Fibonacci dictionary)

n = 12
a = 0
b = 1
d = dict()  # or d = {}
for i in range(1,n+1):
    d[i] = a
    a,b = b,a+b
print(d)

# Question 3 (Stock prices)

companies = ['Python1','Python2','Python3','Python4']
keyNames = ['open','high','low','close']
prices = [[12.87, 11.34, 13.14, 12.34],[23.25,25.36,21.89,22.74],
          [98.74,102.56,99.58,100.41],[203.65,202.65,207.78,205.97]]

d1 = {}
for i in range(len(keyNames)):
    d1[companies[i]] = dict(zip(keyNames,prices[i]))

print(d1)

# Question 4 (Different modules)

import datetime

today = datetime.date.today()   # Function of today's date
print(f"Today's date is {today}")

newYear = datetime.date(2021,1,1)
howManyDays = newYear - today
print(f"Just {howManyDays.days} days until new year!")

# Question 5 (Graph)

import random
import matplotlib.pyplot as plt

keys = 'abcdefghijklmnopqrstuvwxyz'
d = dict()
for letter in keys:
    d[letter] = random.randint(1,100)
print(d)

x,y = zip(*d.items())
plt.bar(x,y)

# Question 6 (Cards)

suit = ['Spades','Clubs','Hearts','Diamonds']
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

deck = dict()
for i in suit:
    deck[i] = rank
    
print(deck)

































    










