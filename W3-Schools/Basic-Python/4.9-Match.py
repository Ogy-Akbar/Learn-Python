#51 Python - Match
# match statement is used to perform different actions based on different conditions

# instead of use many if..else statements, use 'match' statement selects one of many code blocks to be executed

'''
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
'''

# the match expression is evaluated once
# the value of the expression is compared with the values of each case
# if there is a match, the associated block of code is executed

'''
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
'''

# use the _ character as the last case to execute when there are not other matches

'''
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
'''

#Use the pipe character | as an operator in the case evaluation to check for more than one value match in one case

'''
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
'''

# add if statements in the case evaluation as an extra condition-check:

'''
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
'''
