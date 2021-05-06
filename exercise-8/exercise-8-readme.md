# exercise-8 `pip` and `poetry`

## Review exercise-7

If you found exercise-7 particularly frustrating or didn't even end up understanding what the code did, don't worry too much - that is precisely what this exercise is about: 

❝ Badly written code is practically impossible to understand! ❞

You were still able to solve the exercise and get points for it by just adding the docstring comments! 

The exercise also demonstrated the importance and usefulness of tests: While it is beyond the scope of this course, `pytest` is not normally used for grading exercises, but instead to ensure the code (even if you write it yourself) does what you want it to do. The advantage is that you can easily check if your changes to your code break something, as you did in exercise-7.

Also, note that manually removing trailing whitespaces just to conform to PEP8 is not a terribly good use of your time. It is good to know about PEP8 and write code that adheres to it, but usually you'll want to use a tool for that. 

One example which I recommend you to use henceforth is `black`. Black is similar to the `flake8` you met in exercise-7, with the slight but important difference that it not only finds crimes against PEP8, but also rectifies them directly. You install it with `pip install black` and run it with `black your_file.py`. 

⚠️ This will overwrite your file with the new format! You can use `black --diff --color your_file.py` to see what changed would be made. Also note that `black` sets the maximal line length to 88 characters, while PEP8 recomments 79. If you run `black --line-length 79`, you change that default behaviour.

## What are package managers?

You might have wondered what `pip install pytest` (or `flake8` or `black`), which you have been using so far, means. `pip` stands for **package installer for python**; and if you remember exercise-6, you might remember the [Python Package Index](https://pypi.org/). All that `pip` does is that it automatically installs third-party libraries from the [Python Package Index](https://pypi.org/), and makes them available for `import`ing and for use in the console.

⚠️ Note that replit will automatically run `pip install ...` in the background if you `import` a third-party library, but if you are coding on your machine, you normally have to download and install the package before you can `import` it.

By default, `pip` will download the most up-to-date version of a library, but you can also specify which version to install.

## What are virtual environments?

Unfortunately, that is not enough. If you work on multiple projects, say A and B, for example, you might run into the problem that project A uses a third-party library at version 2, and project B uses the same library at version 3 - and the different versions of the library are not compatible.

So either you use `pip` to install and uninstall the correct version everytime you switch between projects, or you find a better way: Enter virtual environments.

Instead of installing all your packages globally on your machine, instead you create a virtual environment **specific to each project**, in which you explain which versions of which libraries you use. Then, everytime you want to run your project, you launch it **within** the virtual environment you created, which only knows about the libraries you install for it, but not of the others.

This has the added benefit of making sure your code can run everywhere, because everyone can then take your code along with the virtual environment specification, and download the necessary packages in their correct version.

## `poetry`

There are various tools such as `venv` and `pipenv` that create such environments, but possibly the simplest is `poetry`, which is conveniently also used by replit, so you don't have to worry about installing it. If you want to use it on your machine though, check the [installation instructions](https://python-poetry.org/docs/).

The way `poetry` works is that it keeps track of what libraries you are using in two files called `pyproject.toml` and `poetry.lock`. The fact that two files are used has to do with dependencies, that is, libraries that need other libraries to run). When you first begin using `poetry`, you navigate into your project directory and `poetry init`, which creates a basically empty `pyproject.toml` (and a virtual environment). To add your libraries, use `poetry add library`, which will prompt `poetry` to take note of the library and install it to the project's virtual environment. Now you can use `poetry run python my_script.py` to run your code using the virtual environment with all the packages you installed there; or or `poetry run black`, for example, to use directly a package you installed in the virtual environment. 

If you want to share your project (and the libraries you used), run `poetry install` on your machine to generate the `poetry.lock` file, share your code together with that file, and run `poetry install` again on the new machine.

## exercise-8

🕰 Submit your exercise at least 15' before the next session starts. 

1. Use `poetry` to add `pytest`, `black` and `flake8` to your project. Try to run `black` on some of your files within the virtual environment!

2. Create a `pull request` containing both `pyproject.toml` and `poetry.lock`.

⚠️ Note that this exercise is not automatically evaluated, so make sure there is exactly one `pull request` with your name by the time of submission.
