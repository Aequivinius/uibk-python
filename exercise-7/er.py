
def find_cities(text_path, cs, out_path):
  with open(text_path) as f:
    texts = f.readlines()
    print(len(texts))
    # texts = texts[:50]

  with open(out_path, 'w') as f:
    for line in texts:
      c = line.split()
      if c:
        art_id = c[0]
        c = [word for word in c if word[0] not in ["@", "<"]]
        counter = 0

        for word in c:
          if word in cs:
            # find longest match
            # print("word: " + word)
            hayst = cs[word]
            longest = 0
            match = ""
            for h in hayst:
              hlen = len(h)
              if hlen > longest:
                  tst = " ".join(c[counter:counter+len(h.split())])
              if h == tst:
                # print("tst: " + tst)
                longest = hlen
                match = tst
                # print("Found city: " + word)
            if match:
              f.write(art_id + "," + str(counter) + "," + match + "\n")
          counter += 1


def get_cities(path):
  cities = {}
  with open(path) as f:
    lines = [line.split("\t")[1] for line in f.readlines()]

  for city in lines:
    cs = city.split()
    if cs[0] not in cities:
      cities[cs[0]] = [city.strip()]
    else:
      cities[cs[0]].append(city.strip())

  for city in list(cities)[:6]:
    print(city + " : " + ",".join(cities[city]))

  filters = ["University", "Police", "Of", "Central"]
  for filter_word in filters:
    if filter_word in cities:
      cities[filter_word] = [c for c in cities[filter_word]
                             if c != filter_word]

# print(cities)
  return cities


def main(haystack, needles, output):
  """Finds city names in a text file.

  Parameters
  ----------
  haystack a txt-file that contains the text you want to analyze
  needles points to a txt-file that contains the cities
  output points to a txt-file for the output

  Returns
  -------
  None
  """

  cities = get_cities(needles)
  find_cities(haystack, cities, output)


if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')
