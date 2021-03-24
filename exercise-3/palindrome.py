# This is the skeleton for exercise-3
# The goal is to create a crude tokenizer that
# separates the input string into a list of
# strings on whitespace.

# In a second step, check if the string is a
# palindrome, i. e. whether it reads the same
# backwards and forwards, ignoring case and
# whitespace. For this, it might make sense to
# glue the tokenized list back together directly

def tokenize(input_string):
 tokens = input_string.split(" ")
 return tokens

def is_palindrome(input_string):
 tokens = "".join(tokenize(input_string)).lower()
 if tokens == tokens[::-1]:
   return True
 else:
  return False
  

	
	# Change this to return True if the string
	# is indeed a palindrom and False otherwise

# You can use this for fast testing
print(is_palindrome("test"))
