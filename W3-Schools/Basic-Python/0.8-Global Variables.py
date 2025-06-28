#9 Python - Global Variables

'''
* Global Variables: Variables that can be used both inside and outside of a function

* To create global variable, the variable needs to be outside of a function.

	ex: 
	x = "awesome"

	def myfunc():
  	  print("Python is " + x)

	myfunc()

* if a variable is created inside a function then it will be local variables (means only apply inside the function only)

	ex:
	x = "awesome"

	def myfunc():
  	 x = "fantastic"
  	 print("Python is " + x)

	myfunc()

	print("Python is " + x)

* Global keyword, use the global keyword to make it as a global variable whether it is inside or outside of the function

	ex:
	def myfunc():
  	 global x
  	 x = "fantastic"

	myfunc()

	print("Python is " + x)

* use Global keyword to change global variable inside a function

	ex:
	x = "awesome"

	def myfunc():
  	 global x
  	 x = "fantastic"

	myfunc()

	print("Python is " + x)
 '''

