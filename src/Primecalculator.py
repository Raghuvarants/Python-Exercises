# Exercise to calculate Prime numbers between 0 and Limit, where Limit is the Parameter.

#Get the value of Limit
limit = int(input("Please enter the limit: "))

listrange = list(range(1, limit))

#Create a second list to store the results
divisorlist=[]

#Identify all the divisors
for i in listrange:
    if limit % 2 == 0:
        divisorlist.append(i)
       
#Print new list
print (divisorlist)

   

