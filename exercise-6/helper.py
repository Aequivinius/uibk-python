# returns a list of strings
def tokenize(input):
  return input.split()

def normalize(input):
  return input.strip().strip(".,!").lower()