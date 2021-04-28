import sys
import helper
import csv


def write(input_string, output_path):
  with open(output_path, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    tokens = helper.tokenize(input_string)
    normalizations = []
    tokens_and_normalizations = []

    for token in tokens: #normalizing and storing in list
      normalizations.append(helper.normalize(token))
    
    for i in range(len(tokens)): #creating pairs and storing
      temporary_pair = []        #them in a nested list
      temporary_pair.append(tokens[i])
      temporary_pair.append(normalizations[i])
      tokens_and_normalizations.append(temporary_pair)
    
    writer.writerows(tokens_and_normalizations)



def parse_arguments():
  if sys.argv[1] == "-s":
    input_string = sys.argv[2]
    
  elif sys.argv[1] == "-f":
    with open(sys.argv[2], "r") as f:
      input_string = f.read()
  else:
    print("Wrong flag")
 
  output_file = sys.argv[3]
  return input_string, output_file



if __name__ == "__main__":
  input_string, output_file = parse_arguments()
  write(input_string, output_file)