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
	seperated_words = input_string.split(" ")
	return seperated_words

def is_palindrome(input_string):
  tokens = tokenize(input_string.upper())
  string = "".join(tokens)
  length = len(string)
  index_right = length - 1
  for character in string:
    if character == string[index_right]:
      pass
    else:
      return False
    index_right = index_right - 1
  return True
  # Change this to return True if the string
	# is indeed a palindrom and False otherwise
	
# You can use this for fast testing
print(is_palindrome("Ottonormal"))



