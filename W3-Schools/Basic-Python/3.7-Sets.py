#38 Python - Sets

# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets

'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
'''

# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable meaning that we cannot change the items after the set has been created.
# Unchangable, but still can remove items and add new items.

# No Duplicates, Sets cannot have two items with the same value.
# Duplicate values will be ignored

'''
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
'''


# The values True and 1 are considered the same value in sets, and are treated as duplicates
# The values False and 0 are considered the same value in sets, and are treated as duplicates

# Length of a Set using len() function

'''
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
'''

# Set items can be any data types

'''
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
'''

# Set can contain different data types

'''
set1 = {"abc", 34, True, 40, "male"}
'''
# In Python, Sets are defined as objects with the data type 'set'

'''
myset = {"apple", "banana", "cherry"}
print(type(myset))
'''

# It is possible to use set() constructor to make a set

'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''

# List is a collection which is ordered and changeable. Allows duplicate members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
