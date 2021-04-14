def tokenize(text):
    return text.split()

# call this using is_consonant(word, i)
def is_consonant(word, index):
	if word[index] in ['a', 'e', 'i', 'o', 'u']:
		return False
	if word[index] == 'y':
		if index == 0:
			return True
		else:
			return not is_consonant(word, index - 1)
	return True


def is_vowel(word, index):
	return not is_consonant(word, index)


def measure(word):
	cvs = ""
	for i in range(len(word)):
		if is_consonant(word, i):
			cvs = cvs + "c"
		else:
			cvs = cvs + "v"

	return cvs.count("vc")


def contains_vowel(word):
	for index in range(len(word)):
		if not is_consonant(word, index):
			return True
	return False


def ends_in_double_consonant(word):
	if len(word) >= 2 and is_consonant(word, len(word) - 1):
		if word[-1] == word[-2]:
			return True
	return False


def ends_in_cvc(word):
	if len(word) > 3:
		if is_consonant(word, len(word) - 3) and not is_consonant(word, len(word) - 2) and is_consonant(word, len(word) - 1) and word[-1] not in ['w', 'x', 'y']:
			return True
	return False

def replace(word, suffix, replacement):
    return word[:-len(suffix)] + replacement

def ends(word, suffix):
  return word[-len(suffix):] == suffix


def step_1a(word):

  if word[-4:] == "sses":
    return word[:-4] + "ss"

  if word[-3:] == "ies":
      return word[:-3] + "i"

  if word [-2:] == "ss":
      return word[:-2] + "ss"

  if word[-1:] == "s" :
      return word[:-1] + ""
  else:
    return word

def step_1b(word):

  if ends(word, "eed"):
    if measure(word[:-3]) > 0:
      return replace(word, "eed", "ee")
    else:
      return word

  if ends(word, "ed"):
    if contains_vowel(word[:-2]):
      stem = replace(word, "ed", "")
      return step_1b_helper(stem)
    else:
      return word

  if ends(word, "ing"):
      if contains_vowel(word[:-3]):
          return replace(word, "ing", "")
      else:
          return word
  return word

def step_1b_helper(word):

  # notice how we're iterating through a list of lists here
  for suffix_pair in [ [ "at", "ate" ],
                       [ "bl", "ble" ],
                       [ "iz", "ize" ] ]:
    suffix = suffix_pair[0]
    replacement = suffix_pair[1]
    if ends(word, suffix):
      return replace(word, suffix, replacement)

  if ends_in_double_consonant(word) and word[len(word) - 1] not in [ "l", "s", "z"]:
    return word[:-1]

  if measure(word) == 1 and ends_in_cvc(word):
    return word + "e"

  return word

def step_1c(word):
  if ends(word, "y"):
      if contains_vowel(word[:-1]):
          return replace(word, "y", "i")
      else:
          return word
  return word

def step_2(word):
  if measure(word) > 0:
    if ends(word, "ational"):
      return replace(word, "ational", "ate")
    if ends(word, "tional"):
      return replace(word, "tional", "tion")
    if ends(word, "enci"):
      return replace(word, "enci", "ence")
    if ends(word, "anci"):
      return replace(word, "anci", "ance")
    if ends(word, "izer"):
      return replace(word, "izer", "ize")
    if ends(word, "abli"):
      return replace(word, "abli", "able")
    if ends(word, "alli"):
      return replace(word, "alli", "al")
    if ends(word, "entli"):
      return replace(word, "entli", "ent")
    if ends(word, "eli"):
      return replace(word, "eli", "e")
    if ends(word, "ousli"):
      return replace(word, "ously", "ous")
    if ends(word, "ization"):
      return replace(word, "ization", "ize")
    if ends(word, "ation"):
      return replace(word, "ation", "ate")
    if ends(word, "ator"):
      return replace(word, "ator", "ate")
    if ends(word, "alism"):
      return replace(word, "alism", "al")
    if ends(word, "iveness"):
      return replace(word, "iveness", "ive")
    if ends(word, "fulness"):
      return replace(word, "fulness", "ful")
    if ends(word, "ousness"):
      return replace(word, "ousness", "ous")
    if ends(word, "aliti"):
      return replace(word, "aliti", "al")
    if ends(word, "iviti"):
      return replace(word, "iviti", "ive")
    if ends(word, "biliti"):
      return replace(word, "biliti", "ble")
  return word

def step_3(word):
  if measure(word) > 0:
    if ends(word, "icate"):
      return replace(word, "icate", "ic")
    if ends(word, "ative"):
      return replace(word, "ative", "")
    if ends(word, "alize"):
      return replace(word, "alize", "al")
    if ends(word, "iciti"):
      return replace(word, "iciti", "ic")
    if ends(word, "ical"):
      return replace(word, "ical", "ic")
    if ends(word, "ful"):
      return replace(word, "ful", "")
    if ends(word, "ness"):
      return replace(word, "ness", "")
  return word

def step_4(word):
  endings = ["al",
            "ance",
            "ence",
            "er",
            "ic",
            "able",
            "ible",
            "ant",
            "ement",
            "ment",
            "ent",
            "ou",
            "ism",
            "ate",
            "iti",
            "ous",
            "ive",
            "ize"]
  for ending in endings:
      if measure(word) > 1:
        if ends(word, ending):
            return replace(word, ending, "")
  if ends(word, "ion"):
      if word[:-3] == "t":
          return replace(word, "ion", "")
      if word[:-3] == "s":
          return replace(word, "ion", "")

  return word

def step_5a(word):
  if measure(word) > 1:
      if ends(word, "e"):
          return replace(word, "e", "")
  if measure(word) == 1:
      if ends(word, "e"):
          if word[:-1] != "o":
            return replace(word, "e", "")
  return word

def step_5b(word):
  if measure(word) > 1:
      if ends_in_double_consonant(word):
          return replace(word, word[-1], "")
  if ends(word, "i"):
      return replace(word, "i", "y")
  return word

def stem(word):
  stem = step_1a(word)
  stem = step_1b(stem)
  stem = step_1c(stem)
  stem = step_2(stem)
  stem = step_3(stem)
  stem = step_4(stem)
  stem = step_5a(stem)
  stem = step_5b(stem)

  return stem

result = [ { word : stem(word) } for word in tokenize("I agreed with the greatest minds of my generalization destroyed by caresses")]
print(result)
