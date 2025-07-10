#24 - Change List Items

'''
* item inside the list can be changed

exp:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


* the values inside the can be changed using ranges

exp:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

* if more items inserted than the replaced ones, the new items will be inserted where it is specified
* while the remaining items will move accordingly
* The length of the list will change when the number of items inserted does not match the number of items replaced.

exp:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

* if less items inserted than the replaced ones, the new items will be inserted where it is specified, while the remaining will be replaced by the new items 

exp: 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

* insert items without replacing any of existing values, use insert() method to do so

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
'''

