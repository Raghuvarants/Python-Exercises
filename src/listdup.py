# Write a function that takes a list and returns a new list that contains 
# all the elements of the first list minus duplicates.

# this one uses a for loop
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print (a)
print (dedupe_v2(a))

