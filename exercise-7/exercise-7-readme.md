# exercise-7 Good practises 

## Why worry about readability?

As you have possibly discovered by now, `python` gives you quite some options for how you write things, particularly in regards to spaces: `a_list = [ 'a' , 'b' , 'c' ]` is the same as `a_list=['a','b'  , 'c']`; and `def b_function(some_parameter, another_parameter)` can also be written as:
```
def a_function ( some_parameter ,
                 another_parameter ,)
```

However, some styles have proven to be more *readable*, and this matters: 

❝ Code is read much more often than it is written! ❞

## Consistency and PEP8

Write your code in such a way that it becomes easy to understand for a human reader (which may well be a future you!). [PEP8](https://pep8.org/) is a set of rules that can help you make your code more readable, especially in regards to whitespaces, and its quite reasonable to stick to it.

It also lays out some recommendations for naming variables and documentation, which we'll look at at greater detail now.

## Variable names

Good code should be self-explanatory, so ideally, you name your variables and your functions in such a way that it is easy to understand what they do and can be read out in plain English.

* For starters, all names (except for `Class` names, which you don't have to worry about for now) should be lowercase and use _ (`my_variable` as opposed to `meineVariable`). They should be in English, and not contain any non-ASCII characters.
* Function names should be a verb, and their parameters be named as its objects: `def correct(exercise)`.
* For `bool`s, it makes sense to prefix variables with `is_`, so that they can be evaluated as `if (is_correct)`.
* For other variables, avoid putting  `type` information (so no `yearString = '5'`) in the name, and be consistent in your naming of concepts.

## Comments and documentation

Following the above rules, most of your code should be easy to understand without any comments. If you feel the need to add comments, bear in mind that they shoud explain *why* you do something as opposed to *how*. If the *how* is not clear from the code, check again to see if you can't find better names for your variables.

For example:
```python
# Using dictionaries here because lookup is much faster.
my_list = ['a','b','c']
my_dict = {name : False for name in my_list}
if 'a' in my_dict:
  ...
```

⚠️ Particularly, make sure the comments don't repeat information from your code. It is easy to forget to change it, too, when you're changing your code, leading to inconsistencies.

However, `docstring`s are an exception to the rule. They are a special type of comment that uses three quotation signs and sits in the first line after a function definition.
```python
def do_something():
  """This could be a docstring"""
```

 Your IDE will use these comments to generate automatically a documentation of your code, making it much easier to work with. 
 
 They should begin with a one line summary of the function, and, if necessary, proceed to describe the parameters the function can take and finish with a description of the return value.

 ```python
def load_cities(input_path):
  """Loads and filters city names from a text file.

  Parameters
  ----------
  input_path points to a tsv-file that contains a list of cities...

  Returns
  -------
  A dictionary...
  """

  cs = ld(needles)
```

## exercise-7

🕰 Submit your exercise at least 15' before the next session starts. 

1. Read the sections on [Hobgoblins](https://pep8.org/#a-foolish-consistency-is-the-hobgoblin-of-little-minds), [maximum line length](https://pep8.org/#maximum-line-length) and [whitespace](https://pep8.org/#whitespace-in-expressions-and-statements) in the PEP8 documentation.
2. `er.py` is a perfect example for how you shouldn't code - it's an entity recogniser that loads from a file city names (obtained from [GeoNames](http://download.geonames.org/export/dump/)) and finds occurences of them in some free text (from [corpusdata.org](https://www.corpusdata.org/) here). 
Try to understand the code and change the variable and function names so that the code becomes readable *without changing its functionality*.

💡 Since the files are quite large, you can use `head -n 100 cities15000.txt`, for example, in the console to show the first 100 lines of the file.

🩺 Begin by adding a docstring to the `main` function, after this, `pytest` should run without errors.

⚠️ Don't change the name or the parameters of the `main` function, it is needed for the tests. As you can see, running `pytest er.py` causes no erros, and this is how you can check that you're not changing the functionality of the `er.py`.

3. Use `pip install flake8` to install a linter, that is, a tool to automatically check PEP8 conformity. Use `flake8 --extend-ignore=E111 exercise-7/er.py` and the [online documentation](https://www.flake8rules.com/) to fix the errors. (Rule E111 deals with indentation, which should be four spaces according to PEP8, but can be annoying if you use replit.)
