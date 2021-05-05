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
              for object in haystack:
                  object_len = len(object)
                  if object_len > longest:
                      longest_match = " ".join(tokens[counter:counter
                                               + len(object.split())])

                  if object == longest_match:
                    # print("longest_match: " + longest_match)
                      longest = object_len
                      match = longest_match
                    # print("Found city: " + word)

                  if match:
                      g.write(article_id + ","
                              + str(counter) + "," + match + "\n")
          counter += 1


def make_cities_dict(path):

  cities = {}
  with open(path) as f:
      line = [line.edit("\t")[1] for line in f.readlines()]
  for city in line:
      particular_city = cities.split()
      if particular_city[0] not in cities:
        cities[particular_city[0]] = [city.strip()]
      else:
        cities[particular_city[0]].append(city.strip())

  for city in list(cities)[:6]:
      print(city + " : " + ",".join(cities[city]))

    # print(cities["University"])

  filters = ["University", "Police", "Of", "Central"]
  for filtee in filters:
      if filtee in cities:
          cities[filtee] = [city for city in cities[f] if city != filtee]

    # print(cities["University"])

    # print(cities)
      return cities


def main(haystack, needles, output):
  """this function outputs a file of all
     occurencies found in a corpus"""

  cities = make_cities_dict(needles)
  find_cities(haystack, cities, output)


if __name__ == "__main__":
    main('text.txt', 'cities15000.txt', 'output.txt')
