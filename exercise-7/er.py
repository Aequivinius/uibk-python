def find_cities(path, cities, output_file):
  with open(path) as city_file:
    texts = city_file.readlines()
    print(len(texts))

# texts = texts[:50]
  with open(output_file, 'w') as g:
    for token in texts:
      city = token.split()
      if city:
        art_id = city[0]
        city = [w for w in city
                if w[0] not in ["@", "<"]]

        counter = 0
        for word in city:
          if word in cities:
            haystack = cities[word]

            longest = 0
            match = ""
            for h in haystack:
              haystack_len = len(h)
              if haystack_len > longest:
                  longest_match = " ".join(
                    city[counter:counter+len(h.split())]
                    )

              if h == longest_match:
                longest = haystack_len
                match = longest_match

            if match:
              g.write(art_id + "," + str(counter) + "," + match + "\n")
          counter += 1


def create_dict(path):
    city_dict = {}
    with open(path) as f:
      lines = [lines.split("\t")[1] for lines in f.readlines()]
    for cit in lines:
      cities = cit.split()
      if cities[0] not in city_dict:
        city_dict[cities[0]] = [cit.strip()]
      else:
        city_dict[cities[0]].append(cit.strip())

    for cit in list(city_dict)[:6]:
      print(cit + " : " + ",".join(city_dict[cit]))

    filters = ["University", "Police", "Of", "Central"]
    for filter in filters:
      if filter in city_dict:
        city_dict[filter] = [c for c in city_dict[filter] if c != filter]

    return city_dict


def main(haystack, needles, output):
  """Loads city names (needles) from a long file and finds \
  occurences of them in some free text (haystack).

  Parameters
  ----------
  haystack does x\n
  needles does y\n
  output does z

  Returns
  ----------
  The output file containing the results
  """

  cities = create_dict(needles)
  find_cities(haystack, cities, output)


if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')
