def tokenize(input):
  return [token.lower().strip(".,!") for token in input.split()]

print(tokenize("Wenn es nur einmal so ganz stille wäre!"))