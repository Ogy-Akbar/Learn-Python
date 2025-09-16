#43 Python - Join Sets

# Several Ways to join two or more sets in Python:

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# 'union' method returns a new set with all items from both sets.

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
'''

# another way is to use the '|' operator instead of union() method

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
'''

# 'union' method can be used to join multiple sets
# just add more sets in the paretheses, seperated by commas

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
'''

# also can be done by using | operator, seperate the sets with more | operators

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
'''

# the 'union()' method allows to join a set with other data types, like lists or tuples

'''
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
'''
# The  | operator only allows to join sets with sets, and not with other data types like it can with the  union() method.

# The 'update()' method inserts all items from one set into another
# The 'update()' changes the original set and does not return a new set

'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
'''

# Both union() and update() will exclude any duplicate items.

# Intersection -only keep the duplicates
# The 'intersection()' method will return a new set, that only contains items that are present in both sets.

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
'''

# another way is to use '&' operator instead of intersection() method

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
'''

# The & operator only allows to join sets with sets, and not with other data types like it can with the intersection() method.

# The 'intersection_update() method will also keep only the duplicates
# But it will change the original set instead of returning a new set
# this method no need another variable as an output of intersection
# rather the existing sets will be changed for its item

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
'''

# The values True and 1 are considered the same value. The same goes for False and 0.

'''
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
'''

# The 'difference()' method will return a new set that will contain only the items from the first set that are not present in the other set.

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
'''

# another way is to use the '-' instead of the 'difference()' method

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
'''

# The - operator only allows you to join sets with sets, and not with other data types like it can with the difference() method.

# The difference_update() method will also keep the items from the first set that are not in the other set 
# but it will change the original set instead of returning a new set.

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
'''

# The 'symmetric_difference()' method will keep only the elements that are NOT present in both sets

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
'''

# Another way is to use the ^ operator instead of the 'symmetric_difference()'

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
'''

# The ^ operator only allows you to join sets with sets, and not with other data types like it can with the symmetric_difference() method.

# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
'''
