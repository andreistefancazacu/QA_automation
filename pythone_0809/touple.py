
"""
TUPLE
"""
#paranteze rotunde
#imutable
#ex : gps coordinates

my_tuple = (1,2,5,7,2,1)

print(my_tuple[3])
#print(my_tuple[4]) out of range
print(len(my_tuple))

#if an element is present in a tuple
print(5 in my_tuple)

print(18 in my_tuple)
#how many times an element is repeating in a tuple
print(my_tuple.count(1))

##err due to imutability
#my_tuple[0] = 7
#print(my_tuple)

tup = 2,3,4;
print(type(tup))