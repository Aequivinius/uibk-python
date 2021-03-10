
def is_divisible(number, divisor):
	if number % divisor == 0:
		return True
	else:
		return False

def fizzbuzz(number):
	if is_divisible(number, 15):
		return "fizzbuzz"
	elif is_divisible(number, 3):
		return "fizz"
	elif is_divisible(number, 5):
		return "buzz"
	else:
		return number

if __name__ == "__main__":
	for number in range(0,46):
		print(fizzbuzz(number))

