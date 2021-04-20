# exercise-6 `import` and arguments



## `import` statements

In the last exercise, you have seen your first `import` statement. You might not minded it much, but being able to `import` libraries, that is, collections of code aimed at a specific purpose, is quite important in `python` (and generally). 

Once `import`ed, the library offers you a series of different functions that you did not write yourself, in the following way. The documentation for which library offers which functions you find on the official `python` [documentation](https://docs.python.org/3/library/) for system libraries (that is, libraries that every installation of `python` has), or, ideally, for third-party libraries, on the [Python Package Index](https://pypi.org/).

```python
import somelibrary

somelibrary.run_some_function()
```

Some libraries (such as `sys`, which we'll see below) also set some variables, which you access in a similar fashion: `somelibrary.some_variable`. 

🏁 It is customary to keep all your `import` statements at the beginning of the code. 

## The `if __name__ == "__main__":`-block:

So far, we have structured our `.py`-files as follows:

```python
# bad_importee.py
def tokenize(input):
  return input.split()

tokenize("Wenn es nur einmal so ganz stille wäre")
```

In this case, the `python` interpreter takes the code, sees a function definition and at the end a statement to execute that function.

However, say we wanted to write our own library, and use it through an `import` statement, the last line would be executed as soon as we `import bad-importee`. (Note the omission of the final `.py` when importing code from files.) However, this is not the intended behaviour, since we only want the `tokenize("Wenn ...")`-bit to be executed when we're running `python bad_importee.py`, but not when we're `import`ing to make its function accessible.

Because of this, it is standard to use the following way to structure your code:

```python
# good_importee.py
def tokenize(input):
  return input.split()

if __name__ == "__main__":
  tokenize("Wenn das Zufällige und Ungefähre")
```

`__name__` is a special variable that `python` sets depending on whether your file is run explicitly or just `import` it. In the first case, we will load the function definitions and run the `tokenize("Wenn das...")`-bit, in the second case, we just load the function definitions and make them available to the importer.

⚠️ The `if __name__ == "__main__":`-part is quite standard and your scripts should use it henceforth.

## User arguments

You know you can run your `python` scripts using `python myscript.py`, and other people, provided they have `python` installed, can do solikewise! However, consider the example below:

```python
def tokenize_file(path):
  with open(path) as f:
    return f.read().split()

if __name__ == "__main__":
  tokenize_file("erste_gedichte.txt")
```

This works, but if somebody wants to tokenize a different text, they would have to change your code. This is called *hardcoded*, and you want to avoid this as much as possible. Instead, opt to *parametrize* your code: Wouldn't it be great if anyone could run your code on any file without having to change your code? If, for example, they could type `python myscript.py path/to/my/file.txt`? 

`python` allows this in the following way. In the example above, `path/to/my/file.txt` is the first *parameter* with which we call our script. You can add as many parameters as you want. When you run your script from the command line, the parameters you run it with are accessible as `string`s from within the `python` code in the `sys.argv` list. This you do as follows:

```python
import sys

def tokenize_file(path):
  with open(path) as f:
    return f.read().split()

if __name__ == "__main__":
  # sys.argv[0] is the name of your script
  print(sys.argv[0])
  
  # this stores the first argument
  first_argument = sys.argv[1]
  
  # this gives you all the arguments the user provided
  # classic list syntax
  all_arguments = sys.argv[1:]
  
  tokenize_file(first_argument)
```

## exercise-6

🕰 Submit your exercise at least 15' before the next session starts. 

This time, you'll not program much functionality, but you make the functions accessbile to your user: Fill in the `tokenizer.py` script so that it takes three user parameters. The first one can be either `-s` (for string) or `-f` (for file).

* If the first argument is `-s`, the second is the input string. (For example: `python tokenizer.py -s "verstummte und das nachbarliche Lachen" output.tsv`)
* If the first argument is `-f`, the second is the input file. (For example: `python tokenizer.py -f input.txt output.tsv`)

Using the code provided in `helpers.py`, `tokenize.py` reads the input (either from file or directly as `string`), tokenizes it, and prints out a `.tsv` containing all the tokens and their normalised form.