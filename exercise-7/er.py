
def find_cities(path, cities, output_file):
  with open(path) as f:
    texts = f.readlines()
    print(len(texts))

  # texts = texts[:50]
  with open (output_file,'w') as g:
    for text in texts:
      tokens = text.split()
      if tokens:
        article_id = tokens[0]
        tokens = [token for token in tokens
                  if token[0] not in ["@", "<"]]

        counter = 0
        for word in tokens:
          if word in cities:
            # find longest match
            # print("word: " + word)
            haystack = cities[word] 
            longest = 0
            match = ""
        for hay in haystack:
          hay_lenght = len(hay)
          if hay_lenght > longest:
            longest_match = " ".join(tokens[counter:counter+len(hay.split())])

          if hay == longest_match:
            # print("tst: " + tst)
              longest = hay_lenght
              match = longest_match 
            # print("Found city: " + word)
          if match:
            g.write(article_id + "," + str(counter) + "," + match + "\n")
        counter += 1

  

def create_cities_dict(path):

  cities = {}
  with open(path) as f:
    line = [line.split("\t")[1] for line in f.readlines()]
  for citie in line:
    citie_names = citie.split()
    if  citie_names[0] not in cities:
      cities[citie_names[0]] = [citie.strip()]
    else:
      cities[citie_names[0]].append(citie.strip())
    
  for citie in list(cities)[:6]:
    print(citie + " : " + ",".join(cities[citie]))
    
  # print(cities["University"])

  filters = ["University", "Police", "Of", "Central"]
  for filter in filters:
    if filter in cities:
      cities[filter] = [citie for citie in cities[f] if citie != filter]

  # print(cities["University"])

  # print(cities)
  return cities

def main(haystack, needles, output):
  """ locates words in a given text ans returns its findings into a file.
  parameters
  ----------
  haystack: the file to be searched
  needles: the file containing the words to be looked for
  output: the file to contain the findings

  returns
  ----------
  a file containing the search results
  """
  
  cities = create_cities_dict(needles)
  find_cities(haystack, cities, output)

if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')