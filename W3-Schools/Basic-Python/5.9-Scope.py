#60 Python - Scope

# scope defines whether a variable is local or global or the region where the variable can be applied

# local scope: variable created inside a function and only be used inside the function

'''
def myfunc():
  x = 300
  print(x)

myfunc()
'''

# local variable is not available outside the function
# but it is availabe for any function inside the function

# Global Variable is variable created in the main body of the python code
# this variable belongs to the global scope & can be used by anyone

'''
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
'''

# Naming variables, same variable name but different scope will be treated as two seperate variables

'''
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
'''

# use the global keyword to make the variable global inside a function / local scope

'''
def myfunc():
  global x
  x = 300

myfunc()

print(x)
'''

# use the global keyword to change a global variable inside a function

'''
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
'''

# nonlocal keyword is used for variables inside nested functions

# the nonlocal keyword makes the variable belong to the outer function

'''
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
'''
