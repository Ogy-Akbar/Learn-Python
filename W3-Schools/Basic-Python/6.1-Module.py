#62 Python - Module

# module is a code library, containing a set of function
# Create module by saving the code with the file extension .py

#in the file named mymodule.py
'''
def greeting(name):
  print("Hello, " + name)
'''

#other python file
'''
import mymodule

mymodule.greeting("Jonathan")
'''

# when using a function from a module, use the syntax: module_name.function_name

# module can contain functions, also variables of all types (arrays, dictionaries, objects, etc)

#save this code in the file mymodule.py
'''
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
  }

'''

#other python file
'''
import mymodule

a = mymodule.person1["age"]
print(a)
'''

# Renaming a module by using as keyword

'''
import mymodule as mx

a = mx.person1["age"]
print(a)
'''

# Built-in Modules are modules made in python for general purposes

'''
import platform

x = platform.system()
print(x)
'''

# dir() function is a built-in function to list all the function names (or variable) in a module.
# The dir() function can be used on all modules, also the ones you create yourself.

'''
import platform

x = dir(platform)
print(x)
'''

# import from module, can choose certain parts from a module, by using the from keyword.
#  When importing using the from keyword, do not use the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]

#in a module named mymodule.py
'''
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"}
'''
'''
# import only the person1 from mymodule.py
from mymodule import person1

print (person1["age"])
'''

