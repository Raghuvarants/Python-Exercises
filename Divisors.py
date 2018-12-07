# Exercise 4 - Get a number as input from user and 

#Get user input
Userdigit = int(input("Please enter your number: "))

#Create a list with range of numbers less than user digit to identify divisors
listrange = list(range(1, Userdigit+1))

#Create a second list to store the results
divisorlist=[]

#Identify all the divisors
for i in listrange:
    if Userdigit % i == 0:
        divisorlist.append(i)
       
#Print new list
print (divisorlist)

   

