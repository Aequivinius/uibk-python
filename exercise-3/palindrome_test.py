import palindrome

def test_tokenize():
  assert palindrome.tokenize("the stale beer in desolate Fugazzi\'s") == ["the", "stale", "beer", "in", "desolate", "Fugazzi\'s"]
  assert palindrome.tokenize("")

def test_palindrome():
  assert palindrome.palindrome("sagas") == True
  assert palindrome.palindrome("saga") == False
  assert palindrome.palindrome("Sagas") == True
  assert palindrome.palindrome("salt an ATLAS") == True
  assert palindrome.palindrome("Satan oscillate my metallic sonatas") == True
  assert palindrome.palindrome("Satan oscillate my wooden sonatas") == False