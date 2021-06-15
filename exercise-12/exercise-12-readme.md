

# exercise-12 `spaCy`

## Review exercise-11

⚠️ Take a moment to check out the sample solutions - while they are quite straight forward, note the use of `tqdm`, which is very useful when working with large datasets.

## Getting started

Similarly to `NLKT`, you don't only need to `import spacy`, but you also need to download some *language models* (see [complete list](https://spacy.io/models/en)), which is, roughly speaking, data that allows `spaCy` to make sense of text. We will be using the `en_core_web_sm` model (`sm` as in small). So after you `poetry add spacy`, you need to `poetry run python -m spacy download en_core_web_sm` to download the model.

```python
import spacy # can take a while
nlp = spacy.load("en_core_web_sm")
document = nlp("This is the document we want to perform our magic on. Can be serveral sentences.")
```

The resulting `document` is a `spaCy` representation of our text, which hosts all the various NLP functions offered by `spaCy`.

## Tokenisation, lemmatisation and NER

Check the demonstration for how to access tokens and lemmata with `spaCy`: 

💡 Note that `spaCy` internally references all strings to an ID, which in turn contains the text the string is made of - so `token.lemma`, `token.lower` and `token.lang`, for example, all return a number. If you want to access the text, use `token.lemma_`, `token.lower_` or `token.lang_` instead. Luckily, at least `token.text` does what it seems to do.

By default, `spaCy` will also perform named entity recognition (NER), which means finding names of people, places, organisations. These we can access through `document.ents`.

## Dependency Parsing

Admittedly, these things we pretty much already knew how to do. Let's move on: Using `token.pos_` we can get the part of speech tags of each token, which is quite useful. In older algorithms, the PoS tag would've been determined by a rule-based approach and used to inform dependency parsing; but these days, the two go actually hand in hand. To see what this is all about:

```python
from spacy import displacy
document = nlp("I asked the executives to pencil in the 11th of January.")
displacy.render(document, style="dep", jupyter=True)
```

`spaCy` uses the [universal dependencies scheme](https://spacy.io/api/annotation#dependency-parsing) which uses tags such as `nsubj` (for subject), `dobj` (for direct object) and `ROOT` (for the main verb). These can be read from `token.dep_`:

* `token.head` will indicate the `token` that *governs* the current `token`
* `token.subtree` will give you a sequence of `token`s that *are governed* by the current `token`

Remeber how in the last exercise we couldn't really make out what people really think? Now we can!

```python
for token in sentence:
  if token.head.lemma_ == "think" and token.dep_ == "ccomp":
    print(sentence)
    print(" ".join([t.text for t in token.subtree])
```

## exercise-12

🕰 Submit your exercise at least 75' before the next session starts. 

In the `corpus` directory you find a subsample of the [Enron E-Mail Dataset](https://www.cs.cmu.edu/~./enron/), which features half a million real world e-mails. The `exercise-12-demo.ipynb` file shows you how to read those files in; and if you want, you can download the rest of the corpus from the website and place it in the `corpus` directory.

In either case, your goal is to do a little experiment: Are people focused on themselves, or on their correspondence? So for every person in your corpus, read in the first few hundred e-mail and parse them using `spaCy`.

➡️ There's no real need to filter away the e-mail headers, as `spaCy` will just not give very convincing parses for those. So you can just keep them.

For every person, determine how many sentences use *I* as the subject of the sentence, and how many use *you* as the subject (by checking `token.dep_ == "nsubj"`). By now, you should feel comfortable enough with `matplotlib` to create normalised, stacked bar charts with your results just as you did in exercise-11.

⚠️ Now we are approaching serious sizes of data, and processing times can spike dramatically. Use list slicing (e.g. `documents[:100]` to trim your data set to manageable sizes, or leave your computer running over night once you are sure your experiment is set up properly.

⚠️ Note that this exercise is not automatically evaluated, so make sure there is exactly one `pull request` with your name by the time of submission.

