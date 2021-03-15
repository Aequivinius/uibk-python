# This is the skeleton for exercise-3
# The goal is to create a crude tokenizer that
# separates the input string into a list of
# strings on whitespace.

# In a second step, check if the string is a 
# palindrome, i. e. whether it reads the same
# backwards and forwards, ignoring case and
# whitespace. For this, it might make sense to
# glue the tokenized list back together directly

def tokenize(string):
	# Change this to return a list
	return string

def is_palindrome(string):
	tokens = tokenize(string)
	
	# Change this to return True if the string
	# is indeed a palindrom and False otherwise
	return True

# You can use this for fast testing
print(is_palindrome("test"))
