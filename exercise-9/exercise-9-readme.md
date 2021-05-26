# exercise-9 `jupyter`

## What is `jupyter`?

In previous exercises we have already processed some data to gain insights: What are the most frequent words on a corpus, for example. Imagine, however, you want to take your analysis further: What are the most frequent non-stop words? Can we make a histogram of the words and their frequencies? 

`python` is frequently used for this sort of work, but it's still somewhat cumbersome to develop, test and run a script to evaluate a specific data set in a specific format, output it to the console or a file to check the data at an intermediate step only to then read the preprocessed data again for further processing. Indeed, much of data analysis (and NLP) is to find a pipeline that manipulates data in various ways to gain insights.

`jupyter` is a program that runs in your browser and is suited for this particular workflow; it allows you to mix code and output into a *notebook* that tells a story with your data. It works as follows:

* The *notebook* is a `.ipynb` file which contains *cells* of code. When you run a cell, the resulting state of your program and its output is saved, allowing you to go back and forth to different cells and see their output or change their content.
* `jupyter` itself is a program that runs a server on your machine. The server takes the notebook and generates a web page from it which you can see and manipulate in your browser; and it takes the code of your notebook and sends it to your `python` installation for it to run.

☝️ `jupyter` is developing to support more languages than `python`, and it works by using *kernels* rather than your `python` installation directly. However, for the sake of simplicity, we're ignoring this fact.

## Installing `jupyter`

You can either run `jupyter` on your machine or rely on an online service not too dissimilar from replit: [binder](https://mybinder.org/). Instructions follow below for how to install `jupyter` on your machine, and while I do my best to help you, please use binder if you run into any problems.

☁️ On binder, supply the URL of your (or the course) repository to get a copy of your files. Note that if you are not actively using bender, the kernel will shut down and you might lose your work; so download a copy of your file when taking a break. Unlike replit, binder unfortunately can't upload files back to your repository, so this has to happen manually. 

📍 To run `jupyter` on your machine, make sure you have `python3` installed ([instructions](https://python-docs.readthedocs.io/en/latest/starting/installation.html)). To be on the safe side, use `python3` instead of `python` in all the subsequent commands. Next, [install `poetry`](https://python-poetry.org/docs/), then install navigate your command line to your `uibk-python` directory (using `cd path/to/directory`) and `poetry init`. (You can check what directory your command line is in by typing `pwd`.) Install `jupyter` by typing `poetry add jupyter`, then run it with `poetry run jupyter notebook` - your browser should open with `jupyter` running.

## Using `jupyter`

Create a new Python 3 notebook using the top right button. Once your notebook is loaded, you can start typing your code as you normally would in your first cell.

To execute a cell, you can use the shortcut ⬆+ ⏎. Take note of how to the left of the cell, `in []` changes to `in [*]` to show that computation is in progress, and then to `in [1]` to indicate that execution has finished. The number in the brackets increments every time you run a cell. You can also use the *cell*-menu to run all cells above the selected cell, which is very useful if you're changing previous bits in your code.

In order to facilitate making your argument with the notebook, you can also use the *cell* menu to change an existing cell to a markdown cells, which you can fill with explanations.

## exercise-9

🕰 Submit your exercise at least 15' before the next session starts. 

Reimplement exercise-5 using `jupyter` and submit your `.ipynb` file: If you are using binder, you need to download the file from the *file* menu, and add it to github.
Your notebook should tell a story of how you, given exercise-5's corpus, find the most common 100 words that Shakespeare employed, using code cells, at least one markdown cell and the code cell's output.


⚠️ Note that this exercise is not automatically evaluated, so make sure there is exactly one `pull request` with your name by the time of submission.
