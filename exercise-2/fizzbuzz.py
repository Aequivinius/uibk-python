def compute_remainder(number, divisor):
	return number % divisor


def fizzbuzz(number):
  if compute_remainder(number, 3) == 0 and compute_remainder(number, 5) == 0:
    return "fizzbuzz"
  elif compute_remainder(number, 3) == 0:
    return "fizz"
  elif compute_remainder(number, 5) == 0:
    return "buzz"
  else:
    return(number)


for number in range(0,226):
	print(str(number) + " : " + str(fizzbuzz(number)))