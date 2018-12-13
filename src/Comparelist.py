#Exercise-5 - to compare 2 lists and identify common elements

#Import Random libraru
#import random

#Create a list with random numbers between 1 to 30
list1=list(range(1,8))

#Create second list with random numbers between 1 to 40
list2=list(range(1,10))

#Create a list to store the result
Common_numbers=[]

#Find common elements
for num in list1:
    if num in list2:
        Common_numbers.append(num)
         
#Print common numbers
print(Common_numbers)


