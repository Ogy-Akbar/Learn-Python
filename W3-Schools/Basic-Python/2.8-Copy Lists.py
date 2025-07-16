#29 Python - Copy Lists

# copying list cannot be as simple as list2 = list1
# because list2 will only reference to list1
# changes made in list1 will automatically also be made in list2

# use 'copy()' to copy a list

'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
'''

# another way to copy list is by using the 'list()' method

'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
'''

# another way again to copy list is by using the ':' (slice) operator

'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
'''
