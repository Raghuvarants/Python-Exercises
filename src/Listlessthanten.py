# Exercise 3 - Get a number from list and add any number less than user entered input in another list

#Create a list with ten numbers
numberlist = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Get user input
Userdigit = int(input("Please enter your number: "))

#Create Second list to store numbers less than the user entered digit
newlist=[]

#Compare User entered digit with numbers in the list
for i in numberlist:
    if Userdigit < i:
            newlist.append(i)

#Print new list
print (newlist)

   

