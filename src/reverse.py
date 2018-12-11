#Get a string as input from user and reverse the string and store it in different variable
def reverse_v4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)

#Get user input
test1 = input("Enter a sentence: ")

#Print test result
print (reverse_v4(test1))

