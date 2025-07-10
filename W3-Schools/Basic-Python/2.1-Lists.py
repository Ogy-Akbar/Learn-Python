#22 Python Lists

'''
* Lists are used to store multiple items in a single variable
* Lists are created using square bracket

exp:
thislist = ["apple", "banana", "cherry"]
print(thislist)

* List Items are ordered, changeable, and allow duplicate values
* List Items are indexed with the first index is [0]

* List Length to determine how many items in a list:

exp:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

* List can be any data type and different data types in one list

exp:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

* data type list

exp:
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

* The List Constructor. use the list() constructor when creating a new list. 

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

* There are four collection data types in the Python programming language:

	- List is a collection which is ordered and changeable. Allows duplicate members.
	- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	- Dictionary is a collection which is ordered** and changeable. No duplicate members.
 '''
