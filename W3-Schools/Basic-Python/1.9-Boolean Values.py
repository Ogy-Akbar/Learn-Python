#20 Boolean Values

'''
* When two values are compared, the expression is evaluatefd and python returns the Boolean answer

exp:
print(10 > 9)
print(10 == 9)
print(10 < 9)

* This statement will return True of False.

* The bool() function allows to evaluate any value, and give true or false in return

* Almost any value is evaluated to True. Any string is True, except empty strings. Any Number is True, except 0.

* these values are evaluated as False such as (), [], {}, "", 0, None.

exp:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

* A value or an object in this case, evaluates to False and that is if you have an object that us made from a class with a __len__ function that return 0 or false

exp: 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

* create function that returns a Boolean Value

exp:
def myFunction() :
 return True

print(myFunction())

exp:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

* use isinstance() function to determina if an object is of a certin data type

exp:
x = 200
print(isinstance(x, int))
'''
