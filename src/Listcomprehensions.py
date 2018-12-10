#Exercise 7 - Get first list of numbers and create a second list and store only even numbers from first list

#Create a list with random numbers
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Create another list with only even numbers taken from list 1
b = [number for number in a if number % 2 == 0]

print(b)


    