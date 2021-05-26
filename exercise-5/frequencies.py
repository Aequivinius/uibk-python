import os

def traverse_directory(path):
  return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]



def tokenize_file(path): #untested
  with open(path, "r") as f:
    complete_string = f.read()
    tokens = []
    normalized_tokens = []
    tokens = complete_string.split()

  for token in tokens:
    normalized_tokens.append(token.lower().strip(",;.!?[]()=-"))
  
  while ("" in normalized_tokens):
    normalized_tokens.remove("")
  
  return normalized_tokens



def compute_counts(pathlist):
  counts = {}
  for path in pathlist:
    tokens = tokenize_file(path)
    for token in tokens:
      if token in counts:
        counts[token] = counts[token] + 1
      else:
        counts[token] = 1

  return counts



def sort_counts(counts):
  sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
  return sorted_tuples



def write_frequencies(list, path):
  rank = 0
  sum = 0 #NOSONAR
  all_data = ""

  for object in list:
    sum += int(object[1])
  
  print(sum)
  
  for object in list:
    rank += 1
    token = object[0] #redundant variables, I know
    count = object[1]
    frequency = float(object[1]) / (sum)
    data_line = str(rank) + "," + str(token) + "," + str(count) + "," + str(frequency) + "\n"
    all_data += data_line
  
  with open(path, "w") as f:
    f.write(str(all_data))
  
  return 1



if __name__ == "__main__":
  files = traverse_directory('corpus')
  counts = compute_counts(files)
  sorted_counts = sort_counts(counts)
  write_frequencies(sorted_counts, 'frequencies.csv')