#23 Python - Access List Items

'''
* Access by reffering to the index number

exp:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

* use negative indexing to start indexing from the end
* negative index starts from -1

exp:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

* range of indexes to print items inside the list by specifying where to start and where to end the range
* the first index which is the start will be included (to be printed)
* the second index which is the end will not be included
* same thing happen to negative index ranges, but the start of the range index (from the right) will not included.

exp:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

exp:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

* Check if item exists, to check whether the item is in the list or not

exp:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''

