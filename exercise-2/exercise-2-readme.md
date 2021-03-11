# exercise-2 Introduction and installation of `python`

* review exercise-1
* What is `python`?
* Dealing with replit.com
* exercise-2

## Review exercise-1

👏 Seems like the `pull requests` are working out, and that most of you discovered that there were `.md` errors not only in the `correctme.md`, but also in the `readme.md`.

## What is `python`? What is *pythonic*?

* `python` is one of the most popular programming languages with a strong community in research and machine learning. 
* Its development started in 1989 by Guido van Rossum, and is named after *Monty Python's Flying Circus*.
* It's cross-platform, and praised for its simplicity and readability. A big part of its appeal is also its big community and ecosystem.

![python](img/python.png)

* `python` 2.7 was released in 2010, and support was ended in 2020. All new projects should use `python` 3.x, which is not directly compatible with the previous version. 
* When people speak about *pythonic*, they refer to a vague shared understanding that code should be easy to read, to understand and to maintain. If you want to be more precise, *pythonic* means using [idiomatic expressions](https://docs.python-guide.org/writing/style/#idioms) specific to `python`.
* If you're new to programming, realise that `python` itself (the interpreter) is a program that reads a file (your code) and tries to execute it. This program usually needs installing, updating etc. However, for the simplicity of this course, we will use a browser-based program that helps you write your code and run it (integrated development environment, IDE). If you still want to install `python` locally on your machine, make sure to follow [these instructions](https://docs.python-guide.org/starting/installation/), which will make your life much easier.
* To run your program, you need to invoke the interpreter. This usually happens through the command line interface (CLI) in the form of typing `python path/to/my/file.py`.

## replit.com

* github.com repositories are represented as *repls* in replit.com. This is the equivalent of having a local copy of your repository on your machine, only that in replit.com's case, your code now is copied to their server. In your account settings, connect your replit.com account with your github.com account.
* To run a file, type `python filename.py` into the console. For example, for seeing the outputs of your exercise, type `python exercise-2/fizzbuzz.py` and for seeing the output of the example code, type `python exercise-2/exercise-2-example.py`


💡 You can use the arrow up key to select previously executed commands in the console.

* To run the tests that will be run when you create a `pull request` on github.com, type `pip install pytest` once to install the testing tool on your virtual machine on replit.com's servers, then `pytest` for every test.

## exercise-2

🕰 Submit your exercise at least 15' before the next session starts. 

⚠️ Make sure you prefix your `pull request` with your last name, otherwise your submission cannot be attributed to you even if it is successful.

1. Create a `pull request` from the [course repository](https://github.com/Aequivinius/uibk-python) to your repository to get an up-to-date version. If there are conflicts, delete or rename the offending files.
2. Create an account at [replit.com](Replit.com), and checkout *your* forked repository. Make sure you select `python` as your language in your `.replit` configuration file, if necessary. 
3. Inspect the file `exercise-2/exercise-2-example.py` to understand the following basic `python` concepts: comments, variables, assignments, functions, return values, parameters, `if` and `print` statements.
4. Change the file `exercise-2/fizzbuzz.py` so that the function `fizzbuzz(number)` behaves as described in the comments.
5. `commit` and `push` your changed files from replit.com to your repository, and create a `pull request` from your repository to the course repository.
