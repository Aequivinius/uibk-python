import sys
import helper
import csv


def write(input_string, output_path):
  with open(output_path, "w", newline = "") as f:
    writer = csv.writer(f, delimiter = "\t")
    tokens = helper.tokenize(input_string)
    tokens_and_normalizations = [ [token, helper.normalize(token)] for token in tokens ]
    writer.writerows(tokens_and_normalizations)


def parse_arguments():
  # TODO: Complete the code below so that
  # input_string contains the string to be tokenized
  # either from file or from user arguments.
  if sys.argv[1] == "-s":
    input_string = sys.argv[2]
  if sys.argv[1] == "-f":
    with open(sys.argv[2]) as f:
      input_string = f.read()

  # TODO: Change the line below, so that output_file
  # contains the third user-supplied argument
  output_file = sys.argv[3]
  return input_string, output_file
