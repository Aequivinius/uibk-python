# exercise-5 `comprehension`s, reading and writing files, `.csv`

Imagine you want to perform an action to every item in a `list` or a `dict`.

```python
tokens = ["Katze", "Stuhl", "sushi"]
lowercase_tokens = []
for token in tokens:
  lowercase_tokens.add(token.lower())
```

💡 Notice that if we had a really long list, we could also write it as follows:

```python
tokens = ["Katze",
          "Stuhl",
          "sushi"]
```

* This we can do much more elegantly using `comprehension`s, which are a shorthand way for this: `[ token.lower() for token in tokens ]`. Here, the `token.lower()` can be replaced by any operation you want to perform on `token` (or whatever you chose to name the items of your `list`).

⚠️ The basic syntax for a `comprehension` is `new_list = [ some_action(item) for item in list]`, which performs `some_action()` on every `item` in `list`, and returns a new `list` with the *changed* `item`s. 

* We can also add an `if` statement, which checks every `item` in this way: `[ item for item in list if len(item) > 3]`, which will return a new `list` that only contains `item`s are longer than 3 characters. This is useful for filtering lists!

* Or, we could get a `list` of `dict`s, where every `dict` has a `token` and a `stem` element, given a `stem()` and a `tokenize()`function: `[ { word : stem(word) } for word in tokenize(text)]`

## absolute and relative paths

* The file system on every computer works with files, which contain any sort of data, and directories, which contain files or folders. 
* Every file has a *path*, which indicates where it lies on the machine - in unix-based operating systems, paths look like `/Users/ralfmueller/uibk-python/exercise-6/exercise-6-readme.md` and in Windows like `C:\Users\ralfmueller\Documents\...`. 
* A *path* can either be *absolute* (such as the two examples above), that is, starting from the system's *root*, or it can be *relative*. In relative paths, you reference a file *relative* to your current location, which is usually the directory of your code. For example, if you start from this `exercise-5` directory...
  * the relative path to `frequencies.py` is just that, `frequencies.py`
  * the relative path to one of the files in the `corpus` directory is `corpus/a-midsummer-nights...` (or `corpus\a-midsummer-nights...` if you're on Windows)
  * the relative path to one of the files of the other exercises is `../exercise-3/howl.txt`. Note how `..` means going up one level in the directory hierarchy.
* Usually you want to be using relative paths when programming so that your programs remain portable.

##  files in `python`

* File paths can be represented as plain `string`s in `python`. However, once you actually want to read or write to a file, you need a wrapper, a representation of the actual file within `python`.

⚠️ Make sure you differentiate clearly between *file paths* and *file wrapper*. One is a `string`, which you can concatenate etc., the other is a `python` object with which you can `read()` and `write()`.

* You create a file wrapper with the `open(path, mode)` function. Path is either absolute or relative; mode is either `'r'` for read-only or `'w'` for write. So to create a wrapper that has read and write access to a file, we use `f = open('corpus/a-midsummer-nights...', 'w')`. 
* With `f.read()` you read the entire contents of the file into a `string`, which you can then work with as usual.
* To write to a new or existing file, you use `f.write()`, which takes as argument a `string`. This is important, if you want to be writing `int` or other data types to a file, you need to convert them explicitly to `string`s by using `str(5)`. 

⚠️ Note that under normal circumstances, opening an existing file in write mode will overwrite its existing content.

* When you are finished working with your file, you need to `close()` it. To make this process easier, `python` offers the following syntax (note the `as` and indentation), which automatically closes the file.

```python
with open('demo.txt','w') as f:
  f.write('Se tu non vi pensi,\nhai persi li sensi')
# here the file will be closed
```

This is equivalent to the following:

```python
f = open('demo.txt', 'w')
f.write('sei morto e puoi dire:\nbisogna morire.')
f.close()
```

* As long as the file wrapper exists, you can use `.write()` multiple times. For example, to write a `dict` to a file (note the use of the `+ "\n"` at the end):

```python
composers = { 'brahms' : 'german', 'mozart' : 'austrian', 'chopin' : 'polish'}
with open('demo.txt', 'w') as f:
  for key, value in composers.items():
    f.write(key.capitalize() + " was " + value.capitalize() + "\n")
```

## `.csv`

* stands for *comma separated value*, and is a very common, easy to use format to store tabular data. Each line represents a row in the table, and the columns are separated by `,`. For example:

```csv
student,points,grade
hans,10,6
gretel,10,6
```

* This works very well for all sorts of data that do not contain `,`.

⚠️ Header line is optional.

* A variation is the *tab separated format*, `.tsv`, which is better suited for natural language texts. In this case, the *delimiter* is set to the *tab*, or `\t` in `python`. This will be useful for exercise-6.

## `cd` and `..`

When working with replit, it can make things easier if you change the working directory of your console to the current exercise: use `cd exercise-5` for example, to change into the directory of exercise-5 - then you can call your programms, such as `frequencies.py` without having to say in which directory they lie (just use `python frequencies.py`). Same goes for `pytest`, which looks for tests just in the current directory and its subdirectories - if you've `cd`ed into your exercise directory before running `pytest`, it'll just run the tests for the current exercise. To navigate up one directory, use `cd ..`.

## exercise-5

🕰 Submit your exercise at least 15' before the next session starts. 

The `corups` directory contains the collected works of Shakespeare (as provided by the [Folger Shakespeare](https://shakespeare.folger.edu/cite/)). It contains several `.txt` files, each of which contains an entire play (and one which includes all his sonnets). Your goal is to fill in the party maked with `TODO` in `exercise-5/frequencies.py` to produce a `frequencies.csv` that contains the frequency of every token in the corpus. 