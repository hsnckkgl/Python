# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:52:08 2020

@author: hsn
"""


#Lists

list = [12,14,15,36,87,52,46,95,21,45,63]
print(list[0])
print(list[0:5]) #first number included, last number excluded

for num in list:
    print(num,end=' ')

total = 0
for number in list:
    total = total + number
print('the total amount is=',total) #easy way is sum()

total = sum(list)
print('the total amount is=',total)

findMax = 0
for num in list:
    if num > findMax:
        findMax = num
print('max value is:',findMax) #easy way is max()

maxNum = max(list)
print('max value is:',maxNum)

minNum = min(list)
print('min value is:',minNum)

for i in range(6):
    print(list[i])
    print(list[i+1])

# Bubble Sort

data = [12,14,15,36,87,52,46,95,21,45,63]
data_copy = data[:]
for i in range(len(data_copy)):
    for j in range(0,len(data_copy)-i-1):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]
print(data_copy)


# Python has its own function

list = [12,14,15,36,87,52,46,95,21,45,63] #Easiest sorting algorithm
print(sorted(list))

# Common list methods

my_list = [10,35,25,74]
my_list.append(100) #.append()
print(my_list)

my_list.remove(25)  #.remove()
print(my_list)

my_list.reverse()
print(my_list)

my_list.extend([51,52,53])
print(my_list)

print(my_list.index(35)) #Shows index number of value

print(list(range(10)))

print(list(range(0, 20, 4)))

myList = [[1,2,3],[4,5,6],[7,8,9]]  # More than 1 dimension
print(myList[0])
print(myList[1][1])     # To access 5
print(myList[2][0])     # To access 7


















