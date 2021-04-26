# For this exercise, you'll need several modules:
# the sys module, which you've seen in the readme
# but also the helper module, which contains some
# very basic helper functions, and finally the
# csv module, which makes writing .csv and .tsv
# much easier. 
# TODO: Import them here, one on each line.

import sys
import helper 
import csv


def write(input_string, output_path):
   with open(output_path, "w", newline="") as f:
    # To write .csv and .tsv, you first open a
    # file, then you call csv.writer() and give
    # it the file as an argument as seen below.
    # (It doesn't work if you haven't imported
    # the csv module above.)
    

    # The csv.writer() method can either just take
    # one argument, the file it will write to, in
    # which case it looks just as above. It can,
    # however, take a second argument, and look
    # as follows:
    # csv.writer(f, delimiter=",")
    writer = csv.writer(f, delimiter='\t')
    # which will tell the csv module explicitly
    # that we want to use , as a symbol to separate
    # the individual fields.
    # TODO: Change the csv.writer() call above so
    # that the csv module uses the tab as a 
    # delimiter. Check exercise-5-readme.md
    # if you are unsure.

    # Then, you can use writer.writerows() to write
    # your .csv file. The writerows() function
    # takes as argument a list of lists. For example,
    # calling writerows( [ [ a , b ] , [ c , d ] ])
    # will result in the following .csv file:
    # a,b
    # c,d
  
    # TODO: construct a list of lists in the
    # following form: 
    # [ [ token1, normalised_form1 ] ,
    #   [ token2, normalised_form2 ] ,
    #  ... ]
    # using the helper.tokenize() and 
    # helper.normalize() functions, then change
    # the below call to use your list of lists
    tokens = helper.tokenize(input_string)
    tokens_and_normalizations = [[token, helper.normalize(token)] for token in tokens]
    writer.writerows(tokens_and_normalizations)


def parse_arguments():
  # this function returns two values - yes,
  # python can do that! It checks the arguments
  # from the user: if the first user-supplied
  # argument (remember, that will be sys.argv[1])
  # is -s, it will use the second argument as a
  # string to be tokenized, if it is -f, it will
  # take it as a file path. It reads the contents
  # of the file, and uses those contents as string
  # to be tokenized.

  input_string = ""
  
  # TODO: Complete the code below so that
  # input_string contains the string to be tokenized
  # either from file or from user arguments.
  # if sys.argv[1] == ...

  # TODO: Change the line below, so that output_file
  # contains the third user-supplied argument
 # outputfile = ""
  #return input_string, output_file

  if sys.argv[1] == "-s":
    input_string = sys.argv[2]
  if sys.argv[1] == "-f":
    with open(sys.argv[2], "r") as f:
      input_string = f.read()

  output_file = str(sys.argv[3])
  return input_string, output_file

if __name__ == "__main__":
  # Here you see how we deal with functions that
  # return two values:
  input_string, output_file = parse_arguments()
  write(input_string, output_file)