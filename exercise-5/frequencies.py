# these import statements give us access to
# collections of code written for specific
# purposes that not every python programm will
# need. We can use the functions they contain in
# our code by using a dot after their name, such
# as os.listdir() (see below)
import os

# this function takes a path and returns a list
# of all the .txt files that lie within it. 
def traverse_directory(path):
  return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  
  # A comprehension! How beautiful! How pythonic!
  # A longer way to write this follows below.
  # Note how this part of the code is not executed
  # because a function stops when it hits a return
  # statement just like the one above.
  onlyfiles = []
  files_and_directories = os.listdir(path) 
  # Lists all the contents of the path, files and
  # directories.
  for f in files_and_directories:
    # You'd be tempted to call your temporary 
    # variable 'file', but 'file' is often already
    # used in python, so it's seldom a good idea
    fpath = os.path.join(path, f)
    # Remember how unix-systems use / in paths
    # and windows uses \? The os.path.join() method
    # joins together a path to a directory and a
    # file it contains using the correct separator
    # depending on the OS you're on. 

    # Also, remember that we already know a join()
    # function - we use it to glue together a list
    # on a character like 
    # " ".join(['the', 'cats', 'pyjamas']), which yields
    # "the cats pyjamas" - you can also join on other 
    # characters!
    # This is why we need modules, to differentiate
    # different methods that have the same name.
    if os.path.isfile(fpath):
      # Check if the path points to a file or 
      # a directory.
      onlyfiles.add(fpath)


# This function takes a path, opens the file
# reads its contents and tokenizes them. Returns
# a list of normalized tokens.
def tokenize_file(path):
  f = open(path)
  content = f.read()
  tokens = content.split()
  normalized_tokens = [token.lower().strip(",.!?[]()=-...") for token in tokens]
  for token in normalized_tokens:
    if len(token) == 0:
      normalized_tokens.remove(token)
#tokens = ""
#normalized_tokens = []
  return normalized_tokens

# this function takes a list of paths, and for every
# file it calls tokenize_file. Then it populates a 
# dictionary that for every token lists how many
# times it occurs in the entire corpus, so { word : count }
def compute_counts(pathlist):
  counts = {}
  for path in pathlist:
    tokens = tokenize_file(path)
    for token in tokens: counts[token] = counts.get(token, 0) + 1
  return counts


# Dictionaries are great, but they have no order. 
# { key1 : value1, key2 : value2 } is the same as 
# { key2 : value2, key1 : value1 }
# So if we want to order a dictionary, we need to resort to
# lists again, which are ordered (using indexes).
# This function takes a dictionary as the 
# compute_counts() creates, and returns a list of lists
# [ [ word1, count1 ], [ word2, count2 ], ... ]
def sort_counts(counts):
  sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
  return sorted_tuples


# this function takes a list of lists as is produced by
# sort_counts(), opens a new file handle and
# writes the frequencies in csv format to that file
def write_frequencies(frequencies, path):
  sum = 0
  rank = 0
  for lex in frequencies:
    sum = sum + lex[1]
  with open("path", "w") as f:
    for lex in frequencies:
      rank = rank + 1
    f.write(f"{rank}, {lex[0]}, {lex[1]}, {lex[1]/sum}\n")
  return

# TODO: You can comment in the following lines to check
# your work. When you're finished, it 
#files = traverse_directory('corpus')
#counts = compute_counts(files)
#sorted_counts = sort_counts(counts)
#write_frequencies(sorted_counts, 'frequencies.csv')
