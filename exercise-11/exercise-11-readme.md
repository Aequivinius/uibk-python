

# exercise-11 `nltk` and sentiment analysis

## Updated course schedule

* There will be one exercise less, so there will be 12 total exercises instead of 13. If this poses a problem for you in regards to your grade, get in touch with me by e-mail.

## Big NLP libraries

While `python` is powerful, it owes much of its popularity to the various libraries, some of which are so extensive they could warrant their own course. While their syntax is familiar to you, their functions and underlying ideas need studying. For the aspiring computational linguists, `numpy`, `pandas` and `scikit-learn` are probably the most important libraries to learn, next to `nltk` and `spaCy`, which we will look at in the remaining exercises.

`nltk` is short for *Natural Language Toolkit*, and has been developed since 2001. It offers a vast array of functions such as tokenisation and named entity recognition; but in most regards has been surpassed in performance and speed by the relatively new `spaCy` (2016), a similar library. However, since it has been around for such a long time, you'll probably come across many applications that use `nltk`, which is why it is introduced here. For many of its applications, `nltk` also has different implementations under its hood, which are interesting to check out.

Furthermore, `nltk` has two important features that `spaCy` doesn't have: easy downloading of [corpora](http://www.nltk.org/nltk_data/) from within `python` (though nowadays you might probably use [Hugging Face](https://huggingface.co/datasets)), and sentiment analysis, both of which are part of today's exercise.

## Sentiment analysis 

`nltk` comes with a sentiment analyser called [VADER](https://github.com/cjhutto/vaderSentiment), which is a rule-based approach. That means that it relies on a manually compiled set of  words that carry positive or negative meaning, together with hand-written rules how they are weighted to compute a score for a phrase that indicates wether the phrase expresses a positive or negative sentiment. This also means that it doesn't need training, as you would find in most modern solutions.

Sentiment analysis is very useful in conjunction with topic modeling, as it allows researchers to gather information about the public opinion on specific topics.

## Getting started with `nltk` and `twitter_samples`

As always, `poetry add nltk`, then `import nltk`. Since `nltk` is such a big library, it makes sense to run it on your own machine, forgoing having to download everything anew when you begin a new session on replit. In order to really use `nltk` however, you need to download additional files that are needed for specific functionalities and to access the corpora. For this, once, in your console, or in your notebook, run the following command:

```python
nltk.download(["stopwords", "twitter_samples", "vader_lexicon"])
```

For today we are using the `twitter_samples` corpus, which contains 30 000 tweets and, once downloaded, can be accessed as follows:

```python
tweets = nltk.corpus.twitter_samples.strings()
```

Or, if you prefer a less implicit notation:

```python
from nltk.corpus import twitter_samples
tweets = twitter_samples.strings()
```

⚠️ Note that there are many different corpora within `nltk`, and unfortunately, they all behave differently - so while for the `twitter_sample` corpus, you use `strings()` to get to the text, for the `gutenberg` corpus, for example, you use `words()`; and for other corpora other functions again. An exhaustive list of corpora and how to use them can be found [here](http://www.nltk.org/howto/corpus.html).

## Working with text in `nltk`

There are several tokenizers in `nltk`, which follow different rules and are useful in different situations: We're looking at the default `sent_tokenize`(for splitting text into sentences while taking into account punctuated abbreviations), `word_tokenize` (default, rule-based) and `TweetTokenizer` (tailored for casual texts). Again, `nltk` being a collection of algorithms, watch out for differences in their usage.

While corpus might be somewhat big of a word, there are smaller, useful word lists in `nltk` such as `names` or `stopwords`: These can be useful for a quick harvest of low hanging fruits, so to speak: `stopwords = nltk.corpus.stopwords.words("english")` and a simple comprehension can already be quite useful.

Finally, there is a very easy way to compute frequency distribution with `nltk`, and it is precisely for such easy low-level functionality that `nltk` will still be around for quite some time still:

```python
fd = nltk.FreqDist(tokens)
fd.keys()
frequency_distribution[""]
```

## `SentimentIntensityAnalyzer`

Sentiment analysis in `nltk` is surprisingly easy:

```python
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Hey you handsome sugar mouse")
```

This returns a dictionary with 4 values: `neg`, `neu`, `pos` and `compound`. The `compound` score maps the overall rating into a value between -1 and 1, with -1 being used for a sentence that is maximally negative. Note that the `polarity_scores()` function takes as an argument an entire, single phrase, not tokens!

## exercise-11

🕰 Submit your exercise at least 75' before the next session starts. 

* Play around with the `twitter_sample` data set, and compute the frequency distribution over all tokens - filter out the stop words, and from the most common tokens, select 3 that you find interesting.
* For these 3 tokens, create a new list of tweets that contain them (mimicking a very superficial topic modeling) - make sure the resulting lists contain more than 10 tweets to get more interesting results.
* For the resulting lists, compute the average positive and negative sentiment score and plot them using `matplotlib` as a stacked bar plot. Bonus points if you normalise them! Stacked bar plots are just normal bar plots with an additional `bottom` argument: 

```python
import matplotlib.pyplot as plt
A = [1, 5, 17]
B = [6, 6, 2]
Pos = range(3)
plt.bar(Pos, A)
plt.bar(Pos, B, bottom = A)
plt.show()
```

⚠️ Note that this exercise is not automatically evaluated, so make sure there is exactly one `pull request` with your name by the time of submission.

