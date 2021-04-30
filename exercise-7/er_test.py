import os
import er

def test_main():
  haystack = "test_haystack.txt"
  needles = "test_needle.txt"
  output = "test_output.csv"
  
  with open(haystack, 'w') as f:
    f.write("124\tI live in Augsbühl Früttingshof")

  with open(needles, 'w') as f:
    f.write("1\tAugsbühl Früttingshof\n")
    f.write("2\tFrüttingshof")
  
  er.main(haystack, needles, output)

  with open(output) as f:
    sample = f.readlines()
    assert(sample[0].split(',')[1] == "4")
    assert(sample[0].split(',')[2].strip() == "Augsbühl Früttingshof")

  os.remove(haystack)
  os.remove(needles)
  os.remove(output)

def test_docstring():
  assert(er.main.__doc__)
  assert('parameters' in er.main.__doc__.lower())