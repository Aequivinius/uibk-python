# The python interpreter goes through your code line by line, and tries to make
# sense of it. If it sees a line prefixed with # it ignores it. This is called
# a COMMENT, and is just used to provide more information to other humans
# reading your code.

# However, if it sees a line that is not a comment, it will try to parse it:
# if it succeeds, i. e. the line of code uses proper key words and syntax, it
# executes the line. For example, the following line prints to the console:

print("Hello World")
print("-----------")

# Feel free to change replace "Hello World" with something else.

# Let's begin with VARIABLES: think of variables in python as a bucket which
# has a label (variable name) and may or may not have a content. The bucket is
# not specific to what it can contain, and it's contents can be read and
# changed. Below, we are creating a variable a, and filling it with a number,
# then printings its contents, changing its contents with a different number
# and printing it again. Filling the bucket is then called ASSIGNING a value to
# a variable.

print("Let's print variables:")
a = 5
print(a)
a = 9
print(a)

# We are free to use whatever names we want for our variables as long as it
# doesn't contain spaces. Feel free to change the variable name in the example
# below.

bucket = 11
print(bucket)

# If we want to use text in python, we need to differentiate it from variable
# names. So if we want to deal with variable names, we just type its name
# directly. If we want to actually use text, we surround it by "". This is then
# called a string, and we can use it in variables just like numbers.

bucket = "bucket"
print(bucket)
print("-----------")

# Next are FUNCTIONS, which are a set of statements that we want to execute in
# the same sequence frequently. We declare them as follows, where function_name
# again can't contain spaces. Notice how the statements it contains are
# indented, this is quite important. As soon as the indentation ends, the
# interpreter considers function declaration complete. Notice how the "Let's
# look at functions"-print statement is not part of the function.

def function_name():
	print(a)
	print(bucket)
	print("function_name() finishes")
print("Let's look at functions:")

# Just declaring the function saves the sequence of statements for us to call
# later. To run it, we need to call the function:

print("Calling function_name() twice...")
function_name()
function_name()
print("-----------")

# Functions can be PARAMETRISED, which means giving the statements it contains
# access to variables:

print("Let's look at parameters:")
def function_with_parameters(parameter, another_parameter):
	print(parameter)
	print(another_parameter)

# If you then call the parametrised function, you can give it values that the
# statements it contains can use under the name you gave the parameters when
# declaring the function.

function_with_parameters(13, 17)

# You can also pass it variables you defined outside of the function. In this
# case, the function reads the values in the variables you give it, and makes
# it available for the statements it contains under the parameter name.

function_with_parameters(a, bucket)
print("-----------")

# On top of that, functions can have RETURN values, which is useful if you
# don't just want to group print statements, but perform actual computation
# and organise your code. When the function is called, it finishes as soon
# as it reaches a return statement and makes the value of the return
# statement available where the function is called.

print("Let's look at return values:")
def function_with_return_value(parameter, another_parameter):
	return parameter + another_parameter

result = function_with_return_value(10,13)
print(result)

# Finally, the IF statement allows you to structure the code with conditions.
# There are many different conditions that you can check, but let's consider
# >, == and <. Notice how we use = for assigning values to variables, and == to
# make a comparison between values or variables.

test_value = 29
if test_value > 31:
	print("It's not brobdingnagian")
if test_value < 31:
	print("It's elephantine")
if test_value == 29:
	print("It's gargantuan")


