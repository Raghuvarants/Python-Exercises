#Verify whether user entered input text is palindrome
#This exercise uses string reverse
#12-07-2018 

#Get the user entered string digit
wrd = input("Please say your digit: ")

#Convert user input into string
wrd=str(wrd)

#Reverse the string
rvs=wrd[::-1]

print(rvs)

#Compare String
if wrd == rvs:
    print ("The word is Palindrome")
else:
    print ("The word is not Palindrome")
