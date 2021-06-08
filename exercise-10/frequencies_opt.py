import os


def traverse_directory(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def tokenize_file(path):  # untested
    with open(path, "r") as f:
        complete_string = f.read()
        tokens = []
        normalized_tokens = []
        tokens = complete_string.split()

    for token in tokens:
        object = token.lower().strip(",;.!?[]()=-")
        if object != "":
            normalized_tokens.append(object)

    return normalized_tokens


def compute_counts_and_sum(pathlist):
    counts = {}
    sum = 0
    for path in pathlist:
        tokens = tokenize_file(path)
        sum += len(tokens)
        for token in tokens:
            if token in counts:
                counts[token] = counts[token] + 1
            else:
                counts[token] = 1

    return counts, sum


def sort_counts(counts):
    sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_tuples


def write_frequencies(list, path, number, sum):
    rank = 0

    all_data = ""



    for object in list[:number]:
        rank += 1
        token = object[0]  # redundant variables, I know
        count = object[1]
        frequency = float(object[1]) / (sum)
        data_line = str(rank) + "," + str(token) + "," + str(count) + "," + str(frequency) + "\n"
        all_data += data_line

    with open(path, "w") as f:
        f.write(str(all_data))

    return 1



def printFormatedFrequencies(list, number, sum):

    rank = 0

    for object in list[:number]:
        rank += 1
        token = object[0]
        count = object[1]
        frequency = float(object[1]) / (sum) * 100

        if (len(token) > 1):
            print("Rank %3d\t|\tWord: %s\t|\tCount: %s\t|\tFrequency: %5.3f%%\n" % (rank, token, count, frequency))
        else:
            print("Rank %3d\t|\tWord: %s \t|\tCount: %s\t|\tFrequency: %5.3f%%\n" % (rank, token, count, frequency))



def printToFileFrequency(path, output_file, number):
    files = traverse_directory(path)
    counts, sum = compute_counts_and_sum(files)
    sorted_counts = sort_counts(counts)
    write_frequencies(sorted_counts, output_file, number, sum)



def stdoutFrequency(path, number):
    files = traverse_directory(path)
    counts, sum = compute_counts_and_sum(files)
    sorted_counts = sort_counts(counts)
    printFormatedFrequencies(sorted_counts, number, sum)



def listFrequency(path, number):
    """
    returns a list of tuples sorted by rank
    """
    files = traverse_directory(path)
    counts, sum = compute_counts_and_sum(files)
    sorted_counts = sort_counts(counts)[0]




    sorted_frequencies = [(val[0], val[1] / sum)
                          for val in sorted_counts[:number]]

    return sorted_frequencies



def frequencyTupleListSplit(list, which_list):
    """
    splits words and their frequencies into to lists respectively
    which_list: enter "words" or 0 to return all the words
    which_list: enter "frequencies" or 1 to return all the frequencies
    """
    words = [val[0] for val in list]
    frequencies = [val[1] for val in list]

    if which_list == "words" or which_list == 0:
        return words
    if which_list == "frequencies" or which_list == 1:
        return frequencies

def listSortedFrequencies(path, number):

    files = traverse_directory(path)
    counts, sum = compute_counts_and_sum(files)
    sorted_counts = sort_counts(counts)

    sorted_frequencies = [(x[1]/sum) for x in sorted_counts[:number]]

    return sorted_frequencies


if __name__ == "__main__":
    path="corpus"
    #printToFileFrequency()