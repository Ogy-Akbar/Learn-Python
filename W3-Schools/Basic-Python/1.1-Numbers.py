#11 Python Numbers

'''
There are three data types of numbers in python:

* int: integer, a whole number, positive or negative, without decimal, with unlimited length

* float: floating point number, positive or negative, containing one or more decimals. can use 'e' to indicate the power of 10

* Complex: imaginary number, using j

* this number data types can be converted from one type to another, but complex number cannot be converted into another number type.

ex:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

* Random Number: python doesn't have a random() function, but has a built-in module called random that can be used to make random numbers

ex:
import random

print(random.randrange(1, 10))
'''

