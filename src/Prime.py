# Prime numbers

def is_prime(number):
    divisors = [num for num in range(2, number) if number % num == 0]
    if divisors == []:
        return True
 
number = int(input("Please enter a number: "))

if is_prime(number):
    print ("The number is Prime")
else:
    print ("number is not prime")