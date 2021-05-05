def find_cities(path, cities, output_file, ):
    with open(path) as f:
        texts = f.readlines()
        print(len(texts))

    # texts = texts[:50]
    with open(output_file, 'w') as g:
        for text in texts:
            tokens = text.split()
            if tokens:
                article_id = tokens[0]
                tokens = [token for token in tokens if token[0] not in ["@", "<"]]

                counter = 0
                for word in tokens:
                    if word in cities:
                        # find longest match
                        print("word: " + word)
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
                            g.write(article_id + "," + str(counter) + "," + match + "\n")
                    counter += 1


def create_dict_cities(path):
    cities = {}
    with open(path) as f:

        line = [line.split("\t")[1] for line in f.readlines()]
    for city in line:
        city_name = city.split()
        if city_name[0] not in cities:
            cities[city_name[0]] = [city.strip()]
        else:
            cities[city_name[0]].append(city.strip())

    for city in list(cities)[:6]:
        print(city + " : " + ",".join(cities[city]))

    # print(cities["University"])

    filters = ["University", "Police", "Of", "Central"]
    for filtr in filters:
        if filtr in cities:
            cities[filtr] = [city for city in cities[filtr] if city != filtr]

    # print(cities["University"])

    # print(cities)
    return cities


def main(haystack, needles, output):
    cities = create_dict_cities(needles)
    find_cities(haystack, cities, output)
    """ 
      Finds city names(needles) in a larger text(haystack) and returns the found names into a new file.
        Parameters
        ----------
        haystack: examined file
        needles: file containing the city names looked for
        output: output file with stored city names
        
        Returns
        -------
        a file containing found city names
    """


if __name__ == "__main__":
    main('text.txt', 'cities15000.txt', 'output.txt')
