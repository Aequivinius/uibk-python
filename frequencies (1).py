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
  
 #we take an empty list to fill it with the elements of files and directory
  onlyfiles = []
  files_and_directories = os.listdir(path) 
 
  for f in files_and_directories:
    
    fpath = os.path.join(path, f)
    # We add path to a file and a directory
    if os.path.isfile(fpath):
     
      onlyfiles.add(fpath)


# We take a path, open the file, read it in and tokenze it's elements

def tokenize_file(path):
  f = open(path)
  content = f.read()
  # TODO: open and read file contents into the string tokens
  tokens = content.split()
  # TODO: then tokenize and normalize the string:
  #  1. split on whitespace
  #  2. lowercase it
  #  3. strip whitespace
  #  4. strip (that is, remove at beginning and end) 
  # special characters such as , . ! ? [ ] ( ) = - ...
  cleared_tokens = [token.lower().strip(",.!?[]()=-...") for token in tokens]
  for token in cleared_tokens:
    if len(token) == 0:
  #  5. check that there are no empty strings in the list      
      cleared_tokens.remove(token)
  return cleared_tokens

# this function takes a list of paths, and for every
# file it calls tokenize_file. Then it populates a 
# dictionary that for every token lists how many
# times it occurs in the entire corpus, so { word : count }
def compute_counts(pathlist):
  counts = {}
  for path in pathlist:
    tokens = tokenize_file(path)
    for token in tokens:
      counts[token] = counts.get(token, 0) + 1
  return counts
# TODO: populate the counts dictionary
    # Check if a token is already in it. If so, add
    # 1 to its count; if not, create a new entry by using
    # counts[word] = 1

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
  # TODO: open the file at path in write mode
  # then for every item in the list write a new line
  # the format of the .csv file is as follows:
  # rank,token,count,frequency
  sum_words = 0
  rank = 0
  for l in frequencies:
    sum_words = sum_words + l[1]
  with open("path", "w") as f:
    for l in frequencies:
      rank = rank + 1
      f.write(f'{rank},{l[0]},{l[1]},{l[1]/sum_words}')
  # The rank runs starts at 1, so the most frequent word
  # has rank 1; the second most frequent 2 etc. 
  # the frequency is calculated by dividing the count by the
  # sum of all counts. sum([list of numbers]) could be
  # handy in this case.
  return

#TODO: You can comment in the following lines to check your work. When you're finished, it 
#files = traverse_directory('corpus')
#counts = compute_counts(files)
#sorted_counts = sort_counts(counts)
#write_frequencies(sorted_counts, 'frequencies.csv')
