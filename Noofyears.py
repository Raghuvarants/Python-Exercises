#Exercise -1 : Character Input Solution
#12-06-2018

#Import Date time function
import datetime

#Getting user input
name = input("What is your name: ")
age = int(input("How old are you: "))

#Getting Current year
now = datetime.datetime.now()
currentyear = now.year

#calculating age
year = str((currentyear-age)+100)

#Print answer
print(name + " will be 100 years old in the year " + year)