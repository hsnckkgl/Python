# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

radius = float(input('give me a radius: '))
pi = 3.14
area = pi * radius**2
print('the area of the circle is: ', area)

fah = float(input('please give me a fahreneit tempereture '))
cel = (fah-32) * 5/9
print('this' ,fah, 'is equal to this' ,cel )

num1 = int(input('please give me the first number: '))
num2 = int(input('please give me the second number: '))
print('the first number is: ' + str(num1) + ' the second number is: ' + str(num2) + ' the sum is: ' + str(num1+num2))

num1 = int(input('write the first number: '))
num2 = int(input('write the second number: '))
sum = num1 * num2
print ('the sum is: ' ,sum)

num1,num2,num3 = 10,20,30
print(num1<25 and num3<25)
print(num2>40 or num1>5)

print('not True is: ', not True)
print('not False is: ', not False)

condition = False
if condition:
    print('condition is True')
else:
    print('condition is False')
    
temp = int(input('Please write a celcius tempereture: '))
if temp > 30:
    print('t-shirt and sun cream')
elif temp <= 30 and temp > 20:
    print('wear sweetshirt')
elif temp <= 20 and temp >10:
    print('wear jacket')
else:
    print('stay home')

myString = 'Python'
print(len(myString))
print(myString[0]) #first letter
print(myString[0:4]) #not include 4. index
print(myString[-1]) #last letter again

print(myString.upper()) #all upper case
print(myString.lower()) #all lower case

guess = input('guess what is the season: ')
guess = guess.lower()
if guess == 'summer':
    print('Yes it is summer')
elif guess == 'winter':
    print('No it is not winter')
elif guess == 'spring':
    print('No it is not spring')
elif guess== 'autumn':
    print('No it is not autumn')
else:
    print(guess.capitalize(), ' is not a season!') #capitalize() first letter is upper case

number = int(input('please enter a number between 1 and 5: '))
if number == 1:
    print('one')
elif number == 2:
    print('two')
elif number == 3:
    print('three')
elif number == 4:
    print('four')
elif number == 5:
    print('five')
else:
    print('invalid number')

number = input('please enter a number as string between one and five: ')
numberLowerCase = number.lower()
if numberLowerCase == 'one':
    print('1')
elif numberLowerCase == 'two':
    print('2')
elif numberLowerCase == 'three':
    print('3')
elif numberLowerCase == 'four':
    print('4')    
elif numberLowerCase == 'five':
    print('5')
else:
    print('enter a invalid number')

secretNumber = 5
guess = int(input('guess the number between 1 and 10: '))
if guess == secretNumber:
    print('you are correct')
elif guess >= secretNumber and guess <= 10:
    print('you say too high')
elif guess <= secretNumber and guess >= 1:
    print('you say low')
else:
    print('invalid guess')

name = input('please enter your name: ')
nameLenght = len(name)
if nameLenght > 3:
    print('your name has ',nameLenght, 'chracter')
else:
    print('it is too short, I will not write it')
    

    


































