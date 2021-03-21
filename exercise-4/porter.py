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
				
	
def step_1a(word):

  if word[-4:] == "sses":
    # remember, Porter algorithm matches
    # the longest suffix in each step
    # and then finishes the step
    # without checking the other rules
    return word[:-4] + "ss"

  # TODO: the rest is up to you!

  # no rule matches	
  return word
		
def step_1b(word):
  # TODO
  return word

def step_1c(word):
  # TODO
  return word

def step_2(word):
  # TODO
  return word

def step_3(word):
  # TODO
  return word

def step_4(word):
  # TODO
  return word

def step_5a(word):
  # TODO
  return word

def step_5b(word):
  # TODO
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

result = [ { word : stem(word) } for word in tokenize("I saw the best minds of my generation destroyed by caresses")]
print(result)