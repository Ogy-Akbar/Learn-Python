#35 Python - Loop Tuples

# Loop thorugh the tuple items by using 'for' loop

'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
'''
  
# Loop Through the Index Numbers, loop through tuple items by referrring the index number.
# Use Use the range() and len() functions to do the loop through

'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
'''

# Using 'while' loop to loop through the tuple items.
# use the len() to determine the length of the tuple
# then start at 0 and loop the tuple items by referring to their indexes
# remember to increase the index by 1 after each iteration

'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
'''
