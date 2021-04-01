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
            return not is_consonant(word, index - 1)        # it is no a C
    return True


def is_vowel(word, index):
    return not is_consonant(word, index)


def measure(word):                 # [C] (VC) {m} [V]
    cvs = ""
    for i in range(len(word)):
        if is_consonant(word, i):
            cvs = cvs + "c"
        else:
            cvs = cvs + "v"

    return cvs.count("vc")          # counts how often CV sequence appears in the word


def contains_vowel(word):
    for index in range(len(word)):
        if not is_consonant(word, index):   # if there is no consonant, return true
            return True
    return False


def ends_in_double_consonant(word):
    if len(word) >= 2 and is_consonant(word, len(word) - 1):    # if the penultimate character is a consonant:
        if word[-1] == word[-2]:                                # and if the last character is the same as the penultimate
            return True                                         # return True because it ends in doulbe consonant
    return False


def ends_in_cvc(word):
    if len(word) > 3:   # if the word ends in CVC and the last C is not a w, x or y: return True
        if is_consonant(word, len(word) - 3) and not is_consonant(word, len(word) - 2) and is_consonant(word, len(
                word) - 1) and word[-1] not in ['w', 'x', 'y']:
            return True
    return False


def replace(word, suffix, replacement):
    return word[:-len(suffix)] + replacement        # return word minus the suffix, then add replacement


def ends(word, suffix):
    return word[-len(suffix):] == suffix            # returns the suffix


def step_1a(word):
    if word[-4:] == "sses":
        return replace(word, "sses", "ss")
    elif word[-3:] == "ies":
        return replace(word, "ies", "i")
    elif word[-2:] == "ss":
        return replace(word, "ss", "ss")
    elif word[-1] == "s":
        return replace(word, "s", "")
    return word


def step_1b(word):
    if ends(word, "eed") and measure(word[:-3]) > 0:      # [:-3] is needed because we want to measure only the stem
        return replace(word, "eed", "ee")   # if the measure of the stem is > 0 (so at least VC + either C or V at some position), replace eed with ee

    if ends(word, "ed") and contains_vowel(word[:-2]):   # if the stem contains a vowel
        stem = replace(word, "ed", "")  # cut "ed" off
        return step_1b_helper(stem)

    if ends(word, "ing") and contains_vowel(word[:-3]):
        stem = replace(word, "ing", "") # cut off "ing"
        return step_1b_helper(stem)
    return word


def step_1b_helper(word):
    # notice how we're iterating through a list of lists here
    for suffix_pair in [["at", "ate"],
                        ["bl", "ble"],
                        ["iz", "ize"]]:
        suffix = suffix_pair[0]
        replacement = suffix_pair[1]
        if ends(word, suffix):
            return replace(word, suffix, replacement)

    if ends_in_double_consonant(word) and word[len(word) - 1] not in ["l", "s", "z"]:
        return word[:-1]    # remove the last consonant of the stem if it ends in double (except l,s,z)

    if measure(word) == 1 and ends_in_cvc(word):
        return word + "e"
    return word


def step_1c(word):
    if word[-1] == "y" and contains_vowel(word[:-1]):
        return replace(word, "y", "i")
    else:
        return word


def list_replace_helper(word, suffix_pair, m=0):    # default m == 0
    for suffix in suffix_pair:
        if ends(word, suffix[0]):
            if measure(word[:-len(suffix[0])]) > m:
                return replace(word, suffix[0], suffix[1])
            else:
                return word
    return word


def step_2(word):		# divided into sections to enhance performance (if I understood correctly)
    if len(word) > 2:		# necessary to avoid index error
        if word[-2] == "a":
            suffix_pair = [["ational", "ate"], ["tional", "tion"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "c":
            suffix_pair = [["enci", "ence"], ["anci", "ance"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "e":
            suffix_pair = [["izer", "ize"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "l":
            suffix_pair = [["abli", "able"], ["alli", "al"],
                           ["entli", "ent"], ["eli", "e"], ["ousli", "ous"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "o":
            suffix_pair = [["ization", "ize"], ["ation", "ate"], ["ator", "ate"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "s":
            suffix_pair = [["alism", "al"], ["iveness", "ive"],
                           ["fulness", "ful"], ["ousness", "ous"]]
            return list_replace_helper(word, suffix_pair)
        elif word[-2] == "t":
            suffix_pair = [["aliti", "al"], ["iviti", "ive"], ["biliti", "ble"]]
            return list_replace_helper(word, suffix_pair)
    return word


def step_3(word):
    suffix_pairs = [["icate", "ic"], ["ative", ""],
                    ["alize", "al"], ["iciti", "ic"],
                    ["ical", "ic"], ["ful", ""], ["ness", ""]]
    return list_replace_helper(word, suffix_pairs)


def step_4(word):
    suffixes = ["al", "ance", "ence", "er", "ic", "able", "ible",
                "ant", "ement", "ent", "ion", "ou", "ism", "ate",
                "iti", "ous", "ive", "ize"]
    for suffix in suffixes:
        if ends(word, suffix) and measure(word[:-len(suffix)]) > 1:
            if suffix == "ion":
                if word[-len(suffix)-1] == "t" or word[-len(suffix)-1] == "s":
                    return replace(word, suffix, "")
                else:
                    return word
            else:
                return replace(word, suffix, "")
    return word


def step_5a(word):
    if ends(word, "e"):
        if measure(word[:-1]) == 1 and not ends_in_cvc(word[:-1]):
            return replace(word, "e", "")
        elif measure(word[:-1]) > 1:
            return replace(word, "e", "")
    return word


def step_5b(word):
    if ends_in_double_consonant(word) and word[-1] == "l":
        if measure(word[:-1]) > 1:
            return word[:-1]
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


result = [{word: stem(word)} for word in
          tokenize("I agreed with the greatest minds of my generalization destroyed by caresses")]
print(result)
