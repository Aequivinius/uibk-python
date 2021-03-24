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
  token_list = input_string.split()
  token_list = input_string.split(" ")
  return token_list


def is_palindrome(input_string):
  palindrome_string = ""
  tokens = tokenize(input_string)
  for token in tokens:
    token = token.lower()
    palindrome_string = palindrome_string + token

  for word in tokens:
    palindrome_string = palindrome_string + word.lower()
    if palindrome_string == palindrome_string[::-1]:
      return True

  else:
    print("This is not a palindrome")
