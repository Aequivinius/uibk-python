# tokenizer should separate into a list of strings on whitespace

# ignore case, check if palindrome and return 
# True or False 
# glue the tokenized list back together directly

def tokenize(input_string): #returns list
  tokens = input_string.split(" ")
  return tokens 

#test funciton to glue the tokenized list back together
#def concatenate(input_string):#
  #tokens = "".join(tokenize(input_string)).lower()
  #return tokens

def is_palindrome(input_string): #checks if palindrome or not
  tokens = "".join(tokenize(input_string)).lower()
  if tokens == tokens[::-1]:
    return True
  else:
    return False

print(is_palindrome("test"))
#print(tokenize("hallo ich bin anna"))
#print(concatenate("hallo ich bin anna"))
#print( ',' .join([ "F" , "B" , "I" ])) # 'F,B,I'
