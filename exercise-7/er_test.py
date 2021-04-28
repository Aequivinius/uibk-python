import os
import er


def test_main():
  haystack = "test.txt"
  needles = "test2.txt"
  output = "test.csv"
  
  with open(haystack, 'w') as f:
    f.write("I live in Augsbühl Früttingshof")

  with open(needles, 'w') as f:
    f.write("1,Augsbühl Früttingshof")
    f.write("2,Früttingshof")
  
  er.main(haystack, needles, output)



  with open(output) as f:
    f.readlines()

  os.remove(haystack)
  os.remove(needles)