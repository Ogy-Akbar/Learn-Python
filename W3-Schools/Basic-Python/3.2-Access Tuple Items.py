# 33 Python - Access Tuple Items

# Tuple Items can be accessed by referring to the index number, inside square brackets. first items start with index 0

'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
'''

# Negative Indexing means start from the end, -1 refers to the last item, and so goes on

'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
'''

# Range of Indexes

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#The search will start at index 2 (included) and end at index 5 (not included).
'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from the beginning to, but NOT included, "kiwi"
'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#This example returns the items from "cherry" and to the end
'''

# Range of Negative Indexing 

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
'''

# Check if item exists, use the 'in' keyword

'''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
'''
