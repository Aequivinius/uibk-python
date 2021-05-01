
def find_cities(path, cities, output):
  with open(path) as f:
    texts = f.readlines()
    print(len(texts))

  # texts = texts[:50]
  with open(output,'w') as g:
    for items in texts:
      split_items = items.split()
      if split_items:
        article = split_items[0]
        split_items = [token for token in split_items \
        if token[0] not in ["@", "<"]]

        counter = 0
        for word in split_items:
          if word in cities:
                # find longest match
                # print("word: " + word)
            haystack = cities[word]
                    
            longest = 0
            match = ""
            for hay in haystack:
              hay_len = len(hay)
              if hay_len > longest:
                  long_match = " ".join(split_items[counter:counter+len(hay.split())])

              if hay == long_match:
                # print("long_match:" + long_match)
                longest = hay_len
                match = long_match
                
                # print("Found city:" + word)
            if match:
              g.write(article + "," + str(counter) + "," + match + "\n")
          counter += 1

  def dict(path):
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
        print(city + ":" + ",".join(cities[city]))
    
    # print(cities["University"])

    filters = ["University", "Police", "Of", "Central"]
    for string in filters:
      if string in cities:
        cities[string] = [city for city in cities[f] if city != string]

    # print(cities["University"])
    # print(cities)
    return cities

def main(haystack, needles, output):
  
  cities = dict(needles)
  find_cities(haystack, cities, output)

if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')