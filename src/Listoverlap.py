import random
d= random.sample (range (1,50), random.randint ( 1,20))
e= random.sample (range (1,50), random.randint ( 1,20))
f = set( [i for i in d if i in e ])

print ("First random list=",d)
print ("Second random list=",e)
print ("Random list overlap=", sorted(f))