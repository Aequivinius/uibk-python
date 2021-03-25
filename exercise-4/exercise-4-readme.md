# exercise-4

## More data types: `dict` and `comprehension`

* Last week, you learned about the list, which a way of organising objects in an ordered way. Remember the syntax: `mylist = ["What", "a", "nice", "day"]`. These objects, however, can only be accessed by their `index` in this way, for example: `mylist[2]`.
* The list can contain any type of objects, including any of the data types we have seen so far: the `int` (for *integer*, which is a number), the `boolean` (which can be either `True` or `False`) and the `string`.
* Remember also, that we use `python path/to/file.py` to instruct the *interpreter* to run our code. The interpreter reads the code and tries to translate it into actions. For it to understand the code, the code needs to adhere to the language rules of `python`.

🎉 There's another way to store objects in an organised way in `python`: the `dict` for *dictionary*. Dictionaries are `{ key : value }`-pairs, which are declared exactly in that way. The `key` is a `string`, the `value` can be anything. For example, you can use a `python dict` to implement a dictionary in the classical sense: `french_dict = { "katze" : "chat", "stuhl" : "chaise" }` and use it as follows: `french_dict["katze"]`.
* To go through all the elements in a `list`, you use this syntax: `for item in mylist`. To iterate through a `dict`, however, you use: `for key, value in mydict.items()`.
* But you can also use different types in a `dict` like this `{ "name" : "rudolf", "points" : 1, "is_reindeer" : True, "likes" : [ "truffles", "carrots"] }`.

🎉 Finally, there are `comprehension`s: Imagine you want to perform an action to every item in a `list` or a `dict`.

```python
tokens = ["Katze", "Stuhl", "sushi"]
lowercase_tokens = []
for token in tokens:
  lowercase_tokens.add(token.upper())
```

💡 Notice that if we had a really long list, we could also write it as follows:

```python
tokens = ["Katze",
          "Stuhl",
          "sushi"]
```

* This we can do much more elegantly using `comprehension`s, which are a shorthand way for this: `[ token.upper() for token in tokens ]`. Here, the `token.upper()` can be replaced by any operation you want to perform on `token` (or whatever you chose to name the items of your `list`).
* Or, we could get a `list` of `dict`s, where every `dict` has a `token` and a `stem` element, given a `stem()` and a `tokenize()`function: `[ { word : stem(word) } for word in tokenize(text)]`

## exercise-4

🕰 Submit your exercise at least 15' before the next session starts. 

1. Read the [original paper](https://tartarus.org/martin/PorterStemmer/def.txt) about the Porter stemmer. 
2. Check out the `exercise-4/porter.py` file and the sample code. All of the conditions that are described in the paper have already been programmed. You can test them by calling the method in question at the end of the file, such as `print(ends_in_cvc("cococ"))`.
3. The first step of stage 1A also has been written for you already, so you can get an idea how to proceed.
4. Implement `stage_1a` and all the other stages, and test your code with `pytest`.

💡 Take special note of this part: *In a set of rules written beneath each other, only one is obeyed, and this will be the one with the longest matching*
💡 Watch out: `*v*` means to test if the *stem* of a word contains a vowel, that is, the word without the suffix in question. Likewise, the conditions regarding the measure also apply only to the *measure of the stem*!
💡 If a suffix matches a rule, but the condition does not, the rule is not applied and the other rules for the step are not matched! (This is how, for example, *feed* is not subjected to the `ED ->` rule in step 1b.)
💡 Because step 1b is the hardest step, there's already some code to help you. Try to understand it, as it might make it easier for you to solve the other exercises, but don't worry too much if you don't. Mimic the code that is already in `def step_1b()` to finish that step and move on.