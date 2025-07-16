#32 Python - Tuple

# Tuple is one of 4 built-in data types in Python used to store collections of data
# Tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets

'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
'''

# Tuple Items are ordered means that the items have a defined order, and that order will not change.
# Tuples are unchangeable means cannot be changed, added or removed items after the tuple has been created.
# Tuples  allow duplicates meaning that Tuples are indexed, they can have items with the same value:

'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
'''

# To determine how many items in a tuple, use the len() function:

'''
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
'''

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recongnize it as a tuple

'''
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
'''

# Tuple can be any data type and can contain different data types

'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
'''

# Python define tuples as objects with the data type tuple

'''
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
'''
# The tuple() constructor to make a tuple

'''
thistuple = tuple(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thistuple)
'''

'''
There are four collection data types in the Python programming language:

#	List is a collection which is ordered and changeable. Allows duplicate 		members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#	Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

#	Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

'''
