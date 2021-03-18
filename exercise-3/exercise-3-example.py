# Now we're talking about string manipulation
# For this demonstration we'll use a short and a
# long string - the latter we're loading from a
# file. Don't worry if you don't understand how
# we're loading the file quite yet. Also, for 
# demonstration of indexes, a number string

short_string = "Alle meine Entchen"

import os
this_file = os.path.dirname(os.path.abspath(__file__))
long_string = open(os.path.join(this_file, 'howl.txt')).read()
number_string = "123456789"

# First, the length of a string:
print("The length of our strings: ")
print(len(short_string))
print(len(long_string))
print("------------")
print("-" * 10)

# Fun fact: In my python, strings can be
# multiplied

# Indexing and slicing
# Since strings can be thought of as lists of 
# characters, we can access individual
# characters using square brackets
print("First character of short string: " + 
      short_string[0])
print("Third character of short string: " +
      short_string[2])
long_string_length = len(long_string)
print("Last character of long string: " +
      long_string[long_string_length - 1])
print("Or simpler: " +
      long_string[-2])
print("Likewise, the 5th last character: " +
      long_string[-5])
print("\n")

# We can use this notation to extract substrings
print("2nd up to and including 4th character " +
      number_string[1:4])
print("5th last character to 2nd last: " +
      number_string[-5:-2])
print("Last 5 characters: "+
      number_string[-5:])
print("\n")     
      
# Notice the print("\n")? 
# "\n" is a special character that denotes a new
# line
print(short_string + "\n" + short_string)
print(short_string + short_string)
print("\n")  

# Our long string, for example, has quite a lot
# of them
print(long_string.count("\n"))
print("\n")

# We can also split our string into a list of
# strings - note we could split on different
# characters such as dots etc.
lines = long_string.split("\n")

# Let's print the first 5 lines now
for line in lines[:5]:
	print(line)
	
# Notice the difference if we don't split our
# string first:
print("\n")
print("Using the in operator with a string: ")
for character in long_string[:5]:
	print(character, end=". ")

# We could also check which of these characters
# is a white space
print("Looking for whitespaces: ")
for character in long_string[:5]:
	if character == " ":
		print("character \"" + character + "\" is a whitespace!")
	elif character =="\n":
		print("character \"" + character + "\" is a newline!")
	else:
		print("character \"" + character + "\" is something else!")
# notice how we're using \" to print " within a 
# string - with the backslash we can prevent
# python from thinking it has reached the end
# of the string

# Also, note how we're introducing 'elif' which
# stands for 'else if condition', which checks
# if the condition is true in the case that the
# if statement before it did apply. 'else' is 
# used as the 'catch-all' part of the 
# if-elif-else statement, which applies if none
# of the conditions before it applied.

# A different way would be using .strip(), which
# removed leading and trailing whitespaces in a
# string - this is a very useful function when
# dealing with texts!
for character in long_string[:15]:
	if character.strip() == "":
		print("Stripped character is empty")
# "" is called the empty string

# we can also change the capitalisation of 
# strings - you can use .lower() in the same way
# which is very useful for comparing strings
print(long_string[:20].upper())

# Finally, we can put lists of strings together
# again - we could also different strings than 
# the whitespace, such as the newline, for
# example, or "[SPACE]"
print(" ".join(lines[:5]))