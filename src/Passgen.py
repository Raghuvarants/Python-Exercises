# Exercise to generate a password with length "passlen" with no duplicate characters in the password

#Import random module to generate random values
import random

#Create a variable to store list of all acceptable input characters
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#Set Password length
passlen = 8
#Generate random password and store it in a variable
p =  "".join(random.sample(s,passlen ))

#Print the generated password
print (p)