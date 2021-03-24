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
  punctuation = "!@#$%^&*()_+<>?:.,;"  #punctuation for comparison and removal
  for i in input_string: #compares if charachters are punctuation
    if i in punctuation:
      input_string = input_string.replace(i, "") # if yes it replaces with empty string = get erraced

  return input_string.split(" ") # splits on the white spaces
  

def is_palindrome(input_string):
  tokens = tokenize(input_string)
  new_string = "".join(tokens[:]).lower() # joins string together and makes lower case
  if new_string == new_string[::-1]: #compares original string with itself itinerated backwards
    print(input_string + "\n" + new_string, "-> is palindrome!")
    return True
  else:
    print(input_string + "\n" + new_string, " -> not palindrome.")
    return False
  	

# You can use this for fast testing
print(is_palindrome("Borrow or rob?"))
print("\n")
print(is_palindrome("Winter is coming!"))
