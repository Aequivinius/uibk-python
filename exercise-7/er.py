# öffnet Datei von einem Pfad, gibt die länge des Texts aus
def find_cities(input_path, cities, output_path):
  with open(input_path) as f:
    texts = f.readlines()
    print(len(texts))


# texts = texts[:50]
  with open(output_path, 'w') as g:
    for words in texts:
      token = words.split()
      if token:
        article_id = token[0]
        token = [w for w in token if w[0] not in ["@", "<"]]

        counter = 0
        for word in token:
          if word in cities:
            haystack = cities[word]

            longest = 0
            match = ""
            for hay in haystack:
              hay_len = len(hay)
              if hay_len > longest:
                  tst = " ".join(token[counter:counter+len(hay.split())])

              if hay == tst:
                longest = hay_len
                match = tst

            # print("Found city: " + word)
            if match:
              g.write(article_id + "," + str(counter) + "," + match + "\n")
          counter += 1


def create_output_file(path):
    cities = {}
    with open(path) as f:
      line = [line.split("\t")[1] for line in f.readlines()]
    for city in line:
        cities_split = city.split()
        if cities_split[0] not in cities:
          cities[cities_split[0]] = [city.strip()]
        else:
          cities[cities_split[0]].append(city.strip())

    for city in list(cities)[:6]:
        print(city + " : " + ",".join(cities[city]))
    # print(cits["University"])

    filters = ["University", "Police", "Of", "Central"]
    for word in filters:
        if word in cities:
            cities[f] = [city for city in cities[word] if city != word]

    # print(cities["University"])

    # print(cities)
    return cities


def main(haystack, needles, output):
  """
  Searches throug text to find specific words. Returns result in a new file.

  Parameters
  ----------
  haystack: file that will be searched
  needles: contains specific words which will be searched for
  output: output file

  Returns
  -------
  Returns output file
  """

  cities = create_output_file(needles)
  find_cities(haystack, cities, output)


if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')
