def find_cities(path, cities, output_file):
  with open(path) as f:
    texts = f.readlines()
    print(len(texts))
    # texts = texts[:50]
  with open(output_file, 'w') as g:
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
              hay_length = len(hay)
              if hay_length > longest:
                  longest_match = " ".join(
                    tokens[counter:counter+len(hay.split())])
              if hay == longest_match:
                # print("longest_match: " + longest_match)
                  longest = hay_length
                  match = longest_match
                # print("Found city: " + word)
            if match:
              g.write(article_id + "," + str(counter) + "," + match + "\n")
          counter += 1
def create_cities_dict(path):
    cities = {}
    with open(path) as f:
      line = [line.split("\t")[1] for line in f.readlines()]
    for city in line:
        city_names = city.split()
        if city_names[0] not in cities:
          cities[city_names[0]] = [city.strip()]
        else:
          cities[city_names[0]].append(city.strip())
    for city in list(cities)[:6]:
        print(city + " : " + ",".join(cities[city]))
    # print(cities["University"])
    filters = ["University", "Police", "Of", "Central"]
    for filter in filters:
        if filter in cities:
            cities[filter] = [city for city in cities[f] if city != filter]
    # print(cities["University"])
    # print(cities)
    return cities
def main(haystack, needles, output):
  """load city names from text file
    Parameters
    haystack: the file to be searched in
    needles: the file containing the searched words
    output: the file contains the found words
    Returns
    the file with the search result
  """

  cities = create_cities_dict(needles)
  find_cities(haystack, cities, output)

if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')