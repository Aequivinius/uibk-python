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
  tokens_list = input_string.split()
  tokens_list = input_string.split(" ")
  return tokens_list

def is_palindrome(input_string):
  palindromes_string = ""
  tokens = tokenize(input_string)
  for token in tokens: 
    token = token.lower()
    palindromes_string = palindromes_string + token
  
  for word in tokens:
    palindromes_string = palindromes_string + word.lower()
  if palindromes_string == palindromes_string[::-1]:
    return True
  else: 
    return False
