# exercise-10 `matplotlib`

You learned how to process data with `jupyter` and create data-driven narratives using code and markdown. Today we're looking at how to add visualisations with [`matplotlib`](https://matplotlib.org/). It's a `python` library, but shares some syntax with MATLAB.

It allows you to transform your data into all sorts of plots, and take control over labels, colors, grids etc. In this exercise, we are looking at line and bar plots.

## Getting started

Install the library with `poetry add matplotlib` and `import` is at the beginning of your code with `import matplotlib.pyplot as plt`. We haven't seen this syntax before: The `as` keyword allows us to rename the library while we're using it so that we don't have to type its full name every time. While we could rename it to anything we like, it has become somewhat standard to call it `plt`, so this is what you'll find in most tutorials and examples.

You begin by drawing your `figure`, which can contain one or multiple plots, which in `plt` lingo are called `axes` (as in *a set of x- and y-axes*), often abbreviated as `ax`:

```python
import matplotlib.pyplot as plt
# creates a figure containing 1 × 2 plots or set of axes.
# play around with the parameters to see their effect!
figure, ax = plt.subplots(1, 2, figsize=(20,6))
```

After this, we can set different attributes on the `figure` element which impact everything, or access the individual plots like a list with `ax`. For example, with `figure.suptitle("Title")` you set the title of your `figure`. Use `plt.show()` to display your `figure` in `jupyter` cleanly.

## Plotting data

For the largest part, `matplotlib` is designed to deal with two-dimensional data; and whether you are creating `bar` or `scatter` or `pie` or line `plot`s, they will always take two arguments:

* a list containing the values for the x-axis
* a list containing the values for the y-axis

➡️ The lists need to be of equal length, and the elements at the respective index need to correspond: So if you have a two points `(0,1)` and `(2,3)` that you want to plot, you need two lists of the same length (2, in this case), one containing `[0, 2]` and the other one `[1, 3]`. Refer to `exercise-10-demonstration.ipynb` to see how to create those 4 basic plot types.

This may be counterintuitive at first, but it makes working with the data much easier in the long run; as we will see in the next example: If we don't want to plot data, but a function `y = f(x)`, we start with a simple array x values: `x = range(0, 100)`, then we compute the corresponding `y` values: `[xi * 2 for xi in x]`.

⚠️ Note that while comprehensions are very elegant, for this sort of work you'll usually use the `numpy` library, which allows you to deal with numerical data in a much more efficient manner and is practically always used when working with plots.

🎨 It's best to stick to the [Tableau Palette](https://matplotlib.org/stable/gallery/color/named_colors.html), which was developed to contain colours that are maximally differentiable from each other. 

## Plotting data nicely

* All plots will take a `label` argument, which you can later display with `ax.legend()` to display more information about the data.
* When you create the plots, the function will take several arguments such as `linewidth`, `color` or `linestyle`.
* The `ax` objects themselves have a whole truckload of functions that allow tinkering with their appearance in every aspect: `set_title()`, `set_xlabel()` and `grid()` are quite important. You can also play around with the labels on the axes by using `tick_params()`, which you might want to [check out](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html) for the exercise.

## Zipf's law

American linguist and statistician who in the 1930s discovered that the most frequently used word in the English language is about twice as frequent as the second most frequent word and so forth. Mathematically speaking, if all words are sorted by the frequency, the *rank* $r $ of a word is its position in this sorting, with rank 1 being the most frequent word and so on. The probability that a word is used can thus be predicted as $P(r) = 0.1 / r $ (for the $r < 1000 $).

## exercise-10

🕰 Submit your exercise at least 15' before the next session starts. 

* In the `exercise-10/corpus` directory you find a sample of 1.6 million words containing spoken contemporary English from TV episodes ranging from 1950 to today, obtained from [Corpusdata](https://www.corpusdata.org/formats.asp).
* Your goal is to create in `jupyter` a figure with two bar plots to compare the 100 most frequent words in contemporary spoken English using this exercise's corpus and the prosaic English of Shakespeare from exercise-5. The plots should show the 100 most frequent words on the x-axis, and on the y-axis their frequency, that is, every word's number of occurrences divided by the total number of tokens in each corpus to compute it's probability.
* Additionally, both plots should contain a curve displaying the predicted probability of each rank according to Zipf's law.

⚠️ Note that this exercise is not automatically evaluated, so make sure there is exactly one `pull request` with your name by the time of submission.

