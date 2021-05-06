
def find_cities(path, cities, out,):
  with open(path) as f:
    texts = f.readlines()
    print(len(texts))

  # texts = texts[:50]
  with open(out, 'w') as g:
    for t in texts:
      tokens = t.split()
      if tokens:
        artid = tokens[0]
        tokens = [token for token in tokens if token[0] not in ["@", "<"]]

        counter = 0
        for word in tokens:
          if word in cities:
            # find longest match
            # print("word: " + word)
            hayst = cities[word]

            longest = 0
            match = ""
            for h in hayst:
              hlen = len(h)
              if hlen > longest:
                tst = " ".join(tokens[counter:counter+len(h.split())])

              if h == tst:
                # print("tst: " + tst)
                longest = hlen
                match = tst

            # print("Found city: " + word)
            if match:
              g.write(artid + "," + str(counter) + "," + match + "\n")
          counter += 1


def create_city_list(path):
  cities = {}
  with open(path) as f:
    lines = [line.split("\t")[1] for line in f.readlines()]
  for city_name in lines:
    city = city_name.split()
    if city[0] not in cities:
      cities[city[0]] = [city_name.strip()]
    else:
      cities[city[0]].append(city_name.strip())

    for city in list(cities)[:6]:
      print(city + " : " + ",".join(cities[city]))

  filters = ["University", "Police", "Of", "Central"]
  for filter in filters:
    if filter in cities:
      cities[filter] = [city for city in cities[filter] if city != filter]

  return cities


def main(input_text, city_names, output):
  """ NER function.
  Parameters:
  ---------------

  1. Text (file) on which NER is run
  2. NE list (txt. file)
  3. name of output file
  """

  cs = create_city_list(city_names)
  find_cities(input_text, cs, output)


if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')
