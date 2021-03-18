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
	if len(word >= 2) and is_consonant(word, len(word) - 1):
		if word[-1] == word[-2]:
			return True
	return False
		
		
def ends_in_cvc(word):
	if len(word) > 3:
		if is_consonant(word, len(word) - 3) and not is_consonant(word, len(word) - 2) and is_consonant(word, len(word) - 1) and word[-1] not in ['w', 'x', 'y']:
			return True
	return False
				
	
def step_1A(word):
	stem = word
	
	if stem[-4:] == "sses":
		stem = stem[:-4] + "ss"
	
	elif stem[-3:] == "ies":
		stem = stem[:-3] + "i"
	
	elif stem[-2:] == "ss":
		stem = stem
		
	elif stem[-1:0] == "s":
		stem = stem[:-1]
	
	return stem
		
def step_1B(word)
	