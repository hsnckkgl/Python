# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:06:55 2020

@author: hsn
"""

# Everything in Python is an object!

x = 1
help(x)     # class int(object)
dir(x)

y = [1,2,3]
help(y)     # class list(object)
dir(y)

z = {'a':1}
help(z)     # class dict(object)
dir(z)

class Patient(object):
    ''' Medical center patient '''
    pass            # Empty object for now

x = Patient()
print(x)
x.name = 'Hasan'
x.age = 31
print(x.name,x.age)     # now we stored some data in object

class Patient(object):
    ''' Medical center patient '''
    
    status = 'patient'      # Class variable
    
    def __init__(self,name,age):    # Constructor method!
        
        self.name = name
        self.age = age
        
    def get_details(self):
        print(f'Patient record: Status: {self.status}, {self.name}, {self.age} years')

steve = Patient('Steven A', 35)
abigail = Patient('Abigail B', 40)

print(steve.status,steve.name,steve.age)
print(abigail.status,abigail.name,abigail.age)

print(steve.get_details())
print(abigail.get_details())

class Patient(object):      # Parent object of 'Infant' object!
    
    ''' Medical center patient 
        Attributes
        ----------
        name: Patient name
        age: Patient age
        conditions: Existing medical conditions
    '''
    
    status = 'patient'      # Class variable
    
    def __init__(self,name,age):    # Instance variable
        
        self.name = name
        self.age = age
        self.conditions = []
        
    def get_details(self):
        print(f'Patient record: Status: {self.status}, {self.name}, {self.age} years \n' 
              f'Current information: {self.conditions}.')
        
    def add_info(self,information):
        self.conditions.append(information)
        

steve = Patient('Steven A', 35)
abigail = Patient('Abigail B', 40)

steve.add_info('Patient treated for ear infection - amoxycilin prescribed')
print(steve.get_details())

class Infant(Patient):      # Child object of 'Patient' object!
    ''' Patient under 2 years '''
    
    def __init__(self,name,age):
        self.vaccination = []
        super().__init__(name, age)     # Variable is derived from parent class! super()
        
    def add_vac(self,vaccine):
        self.vaccination.append(vaccine)
        
    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.' \
              f'Patient has {self.vaccination} vaccines.' \
              f'Current information: {self.conditions}.' \
              f'\n{self.name} IS AN INFANT. HAS HE HAD ALL HIS CHECKS?')

archie = Infant('Archie A', 0)
archie.add_vac('MMR')
print(archie.get_details())

    
# Exercises
# Question 1

class BankAccount(object):
    ''' Simple ATM processes '''
    
    def __init__(self,balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f'Your balance is {self.balance}')
        
    def make_deposit(self):
        amount = float(input('How much would you like to deposit?:> '))
        self.balance += amount
        print(f'Balance is now {self.balance}.')
        
    def make_withdrawal(self):
        amount = float(input('How much would you like to withdraw?:> '))
        if amount > self.balance:
            print(f'You do not have sufficient funds, your balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Withdrawal successful: balance is now {self.balance}.')
            
myBank = BankAccount(300)
print(myBank.display_balance())

myBank.make_deposit()

myBank.make_withdrawal()


# Question 2

import math

class Circle(object):
    ''' Represents a circle with radius. Calculates area.'''
    
    def __init__(self,radius):
        self.radius = radius
        
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area

myCirc = Circle(8)
print(myCirc.calc_area())
