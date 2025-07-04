#17 Python - Format - Strings

'''
* in Python combining string and numbers cannot be done

ex: 
age = 36
txt = "My name is John, I am " + age
print(txt)

* an f-string is introduced for formatting the strings, simply put an f in front of the string, and add curly bracket as the placholders for variables and other operations. a placeholder can contain variables, operations, functions and modifiers.

ex:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

* placeholder can be a modifier by adding colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

ex:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

* a placeholder can be a math operations

ex:
txt = f"The price is {20 * 59} dollars"
print(txt)
'''

