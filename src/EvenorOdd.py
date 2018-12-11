#Exercise-2: Determine whether a number is even or odd

#Get the number from user
Userdigit = int(input("Please enter your number"))

#Validate whether the user entered number is even or odd
if Userdigit % 2 == 0:
    print (Userdigit, "is an even number")
else:
    print (Userdigit, "is a odd number")