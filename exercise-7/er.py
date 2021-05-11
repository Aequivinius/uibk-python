def find_cities(path, cities, output):
    with open(path) as f:
        texts = f.readlines()
        print(len(texts))

        # texts = texts[:50]
    with open(output, "w") as g:
        for object in texts:
            split_objects = object.split()
            if split_objects:
                article_id = split_objects[0]
                split_objects = [
                    token for token in split_objects if token[0] not in ["@", "<"]
                ]

                counter = 0
                for word in split_objects:
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
                                    split_objects[counter : counter + len(hay.split())]
                                )

                            if hay == longest_match:
                                # print("tst: " + tst)
                                longest = hay_length
                                match = longest_match

                        # print("Found city: " + word)
                        if match:
                            g.write(
                                article_id + "," + str(counter) + "," + match + "\n"
                            )
                    counter += 1


def make_city_dictionary(path):
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
    for word_form in filters:
        if word_form in cities:
            cities[f] = [city for city in cities[word_form] if city != word_form]

    # print(cities["University"])

    # print(cities)
    return cities


def main(haystack, needles, output):
    """
    entity recogniser that loads city names from a file
    finds occurrences (needles) of them
    in some free text (haystack)

    Parameters
    ---------
    haystack = file to be examined
    needles = file containing the city names that are looked for
    output = file where result is stored
    Returns
    -------
    occurrences of city names
    """
    cities = make_city_dictionary(needles)
    find_cities(haystack, cities, output)


if __name__ == "__main__":
    main("text.txt", "cities15000.txt", "output.txt")
