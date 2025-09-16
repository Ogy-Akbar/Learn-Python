#66 Python - JSON

# JSON is a syntax for storing and exchanging data

# JSON is text, written with javascript object notation

# Python has a built-in package called json, which is used to work with JSON data

# Javascripts comments use // to write one line comments
# Javascripts for commenting multiple lines use the /* and ends with */

# Parse JSON, convert from JSON to Python using the json.loads()

# The result of the purse will be python dictionary

'''
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])
'''

# Convert Python to JSON using json.dumps()

'''
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
	}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
'''

# Python can convert these python objects into JSON string

'''
import json

# Import Dict.
print(json.dumps({"name": "John", "age": 30}))
# Import List
print(json.dumps(["apple", "bananas"]))
# Import Tuples
print(json.dumps(("apple", "bananas")))
# Import String
print(json.dumps("hello"))
# Import int
print(json.dumps(42))
# Import float
print(json.dumps(31.76))
# Import True
print(json.dumps(True))
# Import False
print(json.dumps(False))
# Import None
print(json.dumps(None))
'''

# When converting from Python to JSON the equivalents are listed below:

'''
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
'''

# Format The Result, the previous example prints JSON string
# but the string is not very easy to read, with no indentations and line breaks
# use json.dumps() to make the string easier to read

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
	}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
'''

# define seperators, default value is (", ", ": ")
# which means using a comma and a space to seperate each object
# and a colon and a space to seperate each keys from values

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
 }

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
'''

# use the sort_keys in json.dumps() to order the keys

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
