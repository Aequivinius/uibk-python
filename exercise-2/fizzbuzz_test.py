import fizzbuzz

def test_fizzbuzz():
  assert fizzbuzz.fizzbuzz(3) == "fizz"
  assert fizzbuzz.fizzbuzz(5) == "buzz"
  assert fizzbuzz.fizzbuzz(15) == "fizzbuzz"
  assert fizzbuzz.fizzbuzz(48) == "fizz"
  assert fizzbuzz.fizzbuzz(225) == "fizzbuzz"