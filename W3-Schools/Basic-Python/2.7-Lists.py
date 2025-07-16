#28 Python - Sort Lists

# using sort() method will sort list alphanumerically, ascending, by default

'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
'''

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
'''

# use the keyword argument 'reverse = True' to sort descending

'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
'''

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
'''

# Customize sort function, using the keyword argument 'key = function' 
# The function will return a number that will be used to sort the list (the lowest number first)
# The returned list will be sorted based on the function

'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
'''

# Case Insensitive Sort, by default sort() method is case sensitive
# capital letters being sorted before lower case letters

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
'''

# use str.lower as a key function to make the sort to be case-insensitive

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
'''

# use reverse() method to reverse the current sorting order of element regardless of alphabet

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
'''
