#21 Python Operators

'''
* Operators used to perform operations on variables and values
* Python divides the operators in the following groups:
  - Arithmetic operators
  - Assignment operators
  - Comparison operators
  - Logical operators
  - Identity operators
  - Membership operators
  - Bitwise operators

* Arithmetic Operator:
	+	Addition	x + y	
	-	Subtraction	x - y	
	*	Multiplication	x * y	
	/	Division	x / y	
	%	Modulus	x % y	
	**	Exponentiation	x ** y	
	//	Floor division	x // y

* Assignment Operator:
	=	x = 5		x = 5	
	+=	x += 3		x = x + 3	
	-=	x -= 3		x = x - 3	
	*=	x *= 3		x = x * 3	
	/=	x /= 3		x = x / 3	
	%=	x %= 3		x = x % 3	
	//=	x //= 3		x = x // 3	
	**=	x **= 3		x = x ** 3	
	&=	x &= 3		x = x & 3	
	|=	x |= 3		x = x | 3	
	^=	x ^= 3		x = x ^ 3	
	>>=	x >>= 3		x = x >> 3	
	<<=	x <<= 3		x = x << 3	
	:=	print(x := 3)	x = 3
				print(x)

* Comparison Operator:
	==	Equal				x == y	
	!=	Not equal			x != y	
	>	Greater than			x > y	
	<	Less than			x < y	
	>=	Greater than or equal to	x >= y	
	<=	Less than or equal to		x <= y

* Logical Operator:
	and 	Returns True if both statements are true			x < 5 and  x < 10	
	or	Returns True if one of the statements is true			x < 5 or x < 4	
	not	Reverse the result, returns False if the result is true	not	(x < and x < 10)

	ex:
	x = 5

	print(x > 3 and x < 10)

* Identity Operator:
	is 	Returns True if both variables are the same object	x is y	
	is not	Returns True if both variables are not the same object	x is not y

* Membership Operator:
	in 	Returns True if a sequence with the specified value is present in the object	x in y	
	not in	Returns True if a sequence with the specified value is not present in the object	x not in y

* Bitwise Operator:

	& 	AND	Sets each bit to 1 if both bits are 1											x & y	
	|	OR	Sets each bit to 1 if one of two bits is 1										x | y	
	^	XOR	Sets each bit to 1 if only one of two bits is 1										x ^ y	
	~	NOT	Inverts all the bits													~x	
	<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off			x << 2	
	>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

* Operator Precedence:
 - Expression inside parentheses must be calculated first
 - 2nd is multiplication or division before addition and substraction
 - 3rd calculate from the left to the right, (if There are no prantheses and multiplication/ starfish)
'''
