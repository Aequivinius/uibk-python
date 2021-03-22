# This is the skeleton for exercise-3
# The goal is to create a crude tokenizer that
# separates the input string into a list of
# strings on whitespace.

# In a second step, check if the string is a 
# palindrome, i. e. whether it reads the same
# backwards and forwards, ignoring case and
# whitespace. For this, it might make sense to
# glue the tokenized list back together directly

test = "hello, my name is Peter, I am 26 years old"

def tokenize(input_string):
  return (input_string.split(" "))

token = tokenize.replace(" ", "")

def lowerword(token):
  return(token.lower())

lowertoken = lowerword

def reverse(lowerword)
  return lowerword[::-1]

reverseword = reverse(lowerword)

def is_palindrome(input_string):
  if lowerword == reverseword
    return("True")
  else 
    return("False")

# You can use this for fast testing
print(is_palindrome(test))
