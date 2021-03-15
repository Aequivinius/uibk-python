import palindrome

def test_tokenize():
  assert palindrome.tokenize("the stale beer in desolate Fugazzi\'s") == ["the", "stale", "beer", "in", "desolate", "Fugazzi\'s"]
  assert palindrome.tokenize("")

def test_palindrome():
  assert palindrome.is_palindrome("sagas") == True
  assert palindrome.is_palindrome("saga") == False
  assert palindrome.is_palindrome("Sagas") == True
  assert palindrome.is_palindrome("salt an ATLAS") == True
  assert palindrome.is_palindrome("Satan oscillate my metallic sonatas") == True
  assert palindrome.is_palindrome("Satan oscillate my wooden sonatas") == False