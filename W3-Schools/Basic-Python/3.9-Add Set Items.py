#40 Python - Add Set Items

# Change Items, Once a set is created, you cannot change its items, but you can add new items.
# To add one item into a set use the add() method

'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
'''

# Add Sets, add items from another set into the current set.
# use the 'update()' method

'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
'''

# Add any iterable, 'update()' method does not have to be a set.
# it can be any iterable object (Tuples, List, Dictionaries, etc.)
# the added iterable object will  become set also

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
