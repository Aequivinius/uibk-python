def tokenize(input_string):
  tokens = input_string.split(" ")
  return tokens


def is_palindrome(input_string):
    tokens = tokenize(input_string)
    reformatted_string = "".join(tokens).lower()
    if reformatted_string == reformatted_string[::-1]:
      return True
    else:
      return False


print(is_palindrome("test"))
