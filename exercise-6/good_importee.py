def tokenize(input):
  return [token.lower().strip(".,!") for token in input.split()]

if __name__ == "__main__":
  print(tokenize("Wenn das Zufällige und Ungefähre"))