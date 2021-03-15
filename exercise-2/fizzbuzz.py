# This is the skeleton for exercise-2. The goal is to change the fizzbuzz()
# function so that it returns the string "fizz", if the number passed as an
# argument is divisible by 3, "buzz" if it is divisible by 5, and "fizzbuzz"
# if it is divisible by 3 and 5. You can use the predefined
# computer_remainder() function.


def compute_remainder(number, divisor):
  return number % divisor
a = "fizz"
b = "buzz"
c = "fizzbuzz"

def fizzbuzz(number):
 if compute_remainder(number, 3)==0 and compute_remainder(number, 5)!=0:
   return (a)
 if compute_remainder(number, 5)==0 and compute_remainder(number, 3)!=0:
   return (b)
 if compute_remainder(number, 3)==0 and compute_remainder(number, 5)==0:
   return (c)
 else:
   return (number)

# this part below prints the result of the fizzbuzz function for the first 45
# numbers
for number in range(0,46):
	print(str(number) + " : " + str(fizzbuzz(number)))