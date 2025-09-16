#67 Python - RegEX

# RegEx or Regular Expression is a sequence of characters that forms a search pattern

# RegEx can be used to check if a string contains the specified search pattern

# Python has a built-in RegEx Module called re

'''
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
'''

# RegEx Functions

'''
Function	Description
findall		Returns a list containing all matches
search		Returns a Match object if there is a match anywhere in the string
split		Returns a list where the string has been split at each match
sub		Replaces one or many matches with a string
'''

# Meta Characters

'''
Character	Description		Example	
[]		A set of characters	"[a-m]"	
\		Signals a special sequence (can also be used to escape special characters)	"\d"	
.		Any character (except newline character)	"he..o"	
^		Starts with	"^hello"	
$		Ends with	"planet$"	
*		Zero or more occurrences	"he.*o"	
+		One or more occurrences	"he.+o"	
?		Zero or one occurrences	"he.?o"	
{}		Exactly the specified number of occurrences	"he.{2}o"	
|		Either or	"falls|stays"	
()		Capture and group	

'''

'''
# Example Metacharacters

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)
'''

# Flags, add flags to the pattern

'''
Flag		Shorthand	Description	
re.ASCII	re.A		Returns only ASCII matches	
re.DEBUG			Returns debug information	
re.DOTALL	re.S		Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I		Case-insensitive matching	
re.MULTILINE	re.M		Returns only matches at the beginning of each line	
re.NOFLAG			Specifies that no flag is set for this pattern	
re.UNICODE	re.U		Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	re.X		Allows whitespaces and comments inside patterns. Makes the pattern more readable
'''

# Example Flags

'''
import re

txt = "Åland"

#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall("\w", txt))


#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))
'''

# Special Sequences, is a \ followed by one of the characters that has a special meaning

'''
Character	Description	Example	
\A		Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b		Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
												r"ain\b"	

\B		Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")																								r"\Bain"
												r"ain\B"	

\d		Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D		Returns a match where the string DOES NOT contain digits	"\D"	
\s		Returns a match where the string contains a white space character	"\s"	
\S		Returns a match where the string DOES NOT contain a white space character	"\S"	
\w		Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W		Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z		Returns a match if the specified characters are at the end of the string	"Spain\Z"
'''

#Example of Special Sequences

'''
import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
'''

# Sets, returns a match for any characters inside the square bracket []

'''
Set		Description	
[arn]		Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]		Returns a match for any lower case character, alphabetically between a and n	
[^arn]		Returns a match for any character EXCEPT a, r, and n	
[0123]		Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]		Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]		In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

#Example of Sets

'''
import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
'''

# findall() function, returns a list containing all matches

# The list contains the matches in the order they are found

'''
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
'''

# search() function searches the string for a match
# and returns a match object if there is a match
# if there is more than one match, only the first occurence of the match will be returned

'''
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start)
'''

# if no matches are found, the value 'none' is returned

'''
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
'''

# split() function, returns a list where the string has been split at each match

'''
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
'''
# control the number of split by using maxsplit

'''
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
'''

# sub() function, replaces the matches with the text of your choice

'''
import re

# replace every white space-character with the number 9

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
'''

# control number of replacement by using count parameter

'''
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
'''

# Match Object, is an object containing information about the search and the result
# if there is no match, the value None will be returned, instead of the Match Object

'''
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
'''

#The Match object has properties and methods used to retrieve information about the search
# .span(), returns a tuple containing the start-, and end positions of the match
#.string(), returns the string passed into the function
# .group() returns the part of the string where there was a match

'''
import re

# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S"

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
'''

'''
import re

#Print the string passed into  the function

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
'''

import re

# Print the part of the string where there was a match.

# The regular expression looks for any words that starts with an upper case "S":

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
