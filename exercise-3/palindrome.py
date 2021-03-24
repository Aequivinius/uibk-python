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
  input_l = input_string.lower()
  token_list = input_l.split(" ")
  return token_list

def is_palindrome(input_string):
  token = "".join(tokenize(input_string))
  return(token == token[::-1])

# You can use this for fast testing
print(tokenize("Hello WoRlD"))
print(is_palindrome("salT AN AtlaS"))
