def tokenize(input_string):
	# Change this to return a list
	return input_string
def tokenize(input_string): 
  tokens = input_string.split(" ")
  return tokens 

def is_palindrome(input_string):
	tokens = tokenize(input_string)

	# Change this to return True if the string
	# is indeed a palindrom and False otherwise
	return True

def is_palindrome(input_string): 
  tokens = "".join(tokenize(input_string)).lower()
  if tokens == tokens[::-1]:
    return True
  else:
    return False

# You can use this for fast testing
print(is_palindrome("test"))





