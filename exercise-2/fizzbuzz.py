# This is the skeleton for exercise-2. The goal is to change the fizzbuzz()
# function so that it returns the string "fizz", if the number passed as an
# argument is divisible by 3, "buzz" if it is divisible by 5, and "fizzbuzz"
# if it is divisible by 3 and 5. You can use the predefined
# computer_remainder() function.

# def compute_remainder(number, divisor):
#	return number % divisor

# def fizzbuzz(number):
# your code goes here
# don't forget to replace the return statement below as appropriate
#	return number

# this part below prints the result of the fizzbuzz function for the first 45
# numbers
# for number in range(0,46):
#	print(str(number) + " : " + str(fizzbuzz(number)))

div3 = 3
div5 = 5
for number in range(1, 46):
    if number % div3 == 0 and number % div5 == 0:
        print(str(number) + ": fizzbuzz")
    elif number % div3 == 0:
        print(str(number) + ": fizz")
    elif number % div5 == 0:
        print(str(number) + ": buzz")
    else:
        print(str(number) + ": ")
