
def find_cities(path, cities, output_filename):
  with open(path) as f:
    texts = f.readlines()
    print(len(texts))

  # texts = texts[:50]
  with open(output_filename, 'w') as g:
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
                hay_len = len(hay)
                if hay_len > longest:
                  longest_match = " ".join(tokens[counter:counter + len(hay.split())])

              if hay == longest_match:
                  # print("tst: " + tst)
                  longest = hay_len
                  match = longest_match
                
                  # print("Found city: " + word)
          if match:
              g.write(article_id 
                      + ","
                      + str(counter)
                      + ","
                      + match
                      + "\n")
        counter += 1


def city_dictonary(path):
    cities = {}
    with open(path) as f:
      line = [line.split("\t")[1] for line in f.readlines()]
    for city in line:
        cities_split = city.split()
        if  cities_split[0] not in cities:
          cities[cities_split[0]] = [city.strip()]
        else:
          cities[cities_split[0]].append(city.strip())
    
    for city in list(cities)[:6]:
        print(city + " : " + ",".join(cities[city]))
    
    # print(cits["University"])

    filters = ["University", "Police", "Of", "Central"]
    for word in filters:
        if word in cities:
            cities[word] = [city for city in cities[word]
                            if city != word]

    # print(cits["University"])
    # print(cits)
    return cities

def main(haystack, needles, output):
    """ Finds specific words (needles) in large texts (haystack).
        Then returns the resulting occurrences in a new file (output).
        Parameters
        ----------
        haystack name of file that will be searched through
        needles name of file that that contains content to be looked for
        output name of file where the search result will be gathered
        Returns
        -------
        A new file that contains the search results
    """
    cities = city_dictonary(needles)
    find_cities(haystack, cities, output)

if __name__ == "__main__":
    main('text.txt', 'cities15000.txt', 'output.txt')