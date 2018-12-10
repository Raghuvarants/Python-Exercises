#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

#Import random module
import random

#Create variable to store random number
number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess !=  "exit":
    guess = input("what's your guess?: ")
    
    if guess == "exit" :
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print ("Your guess is too low")
    elif guess > number:
        print ("Your guess is too high")
    else:
        print ("You got it:")
