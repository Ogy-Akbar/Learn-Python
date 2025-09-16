#41 Python - Remove Set Items


# To remove an item in a set, use the 'remove()', or the 'discard()'

# If the item to remove does not exist, remove() will raise an error.

'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
'''

# If the item to remove does not exist, discard() will NOT raise an error.

'''
thisset = {"apple", "banana", "cherry"}

thisset.discard("apple")

print(thisset)
'''

# Use 'pop' method to remove an item, but this method will remove a random item
# cannot be sure which item that gets removed
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

'''
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
'''

# Use 'clear' method to empty the set

'''
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
'''

# Use 'del' keyword will delete the set completely

'''
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
'''
