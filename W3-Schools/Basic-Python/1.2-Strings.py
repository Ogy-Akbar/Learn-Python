#13 Python Strings

'''
* Strings is surrounded by either single or double quotation marks

* Quotes inside Quotes are permissible as long as it doesn't disrupt with the outermost quotation which define the string.

* String can be assigned into a variable. multiline strings can also be assigned into a variable by surround the string with three single/ double quotes

* Strings in python are also arrays of bytes representing Unicode characters. Python doesn't have a character data type, a single character is a string with a length of 1. use square bracket to access element of the string.

ex: 
a = "Hello, World!"
print(a[1])

* Looping Through String, use for loop to print each character in the string.

ex:
for x in "banana":
  print(x)

* String Length, to get string length, use the len() function

ex:
a = "Hello, World!"
print(len(a))

* Check String, to check the character or phrase in a string using 'in'. Also an if statement can be added. 

ex: 
txt = "The best things in life are free!"
print("free" in txt)

ex: 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

* Check string if there is no certain character or phrase. 

ex:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

'''
