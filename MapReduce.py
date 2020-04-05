from functools import *
lst = [12,34,5,3,24,23,65,34,35]

evens = list(filter(lambda a : a%2==0,lst))  # For filtering values from given set of values
print (evens)

doubles = list(map(lambda a : a*2,evens))    # For mapping i.e. doing calculations on the filtered set of values
print (doubles)

sum = reduce(lambda a,b : a+b, doubles)    # Aggregating the values received from upstream, two inputs and 1 output always
print (sum)