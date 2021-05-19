# ## This file contains comments that you would not
# ## in a real project; these are prefixed with # ##
# ## As you can see, in the code below there are very
# ## few normal, # comments, because the code is quite
# ## readable. Remember: When you feel there's the
# ## need to add a comment, think if you can't write
# ## your code in a way that is more self-explaining!

def main(haystack, needles, outpath):
  """Coördinates the pipeline, writing results into a file.

  Parameters
  ----------
  haystack: the path to a file containing articles,
   tab separated ID and plain text, in which to find
    entities.

  needles: the path to a file containing entities to
  be found, tab separated ID and entity

  outpath: the path to desired output file
  """

  # ## Note how the functions were renamed for
  # ## greater clarity, and split into more functions.
  entities = load_entities(needles)
  filtered_entities = filter_entities(entities)
  find_entities(haystack, filtered_entities, outpath)


def load_entities(inpath):
  """Loads from a text file entities and returns them
  as an easy-to-search dictionary.

  Parameters
  ----------
  inpath: path to a tab separated text file containing IDs and entities.

  Returns
  -------
  A dictionary of entities. The dictionary contains
  only single-token keys, pointing to a list of all
  the values, single-token or multiple tokens, that
  start with the single-token key.
  """

  # ## Note that our cities15000.txt contains many
  # ## more columns, but we just look at the first
  # ## two. Also, note that even though we have the
  # ## file extension .txt, we can still treat the
  # ## file as a .tsv - as long as the format
  # ## within is correctly tab-separated.

  # ## This used to be called cits, but we rename it
  # ## to entities, so we can use the code for other
  # ## situations: imagine we wanted to find
  # ## company names instead of city names!

  # ## Finally, someone asked about renaming
  # ## multiple items in replit:
  # ## docs.replit.com/tutorials/10-productivity-hacks
  # ## under 'adding cursors'
  entities = {}

  with open(inpath) as f:
    # ## you could pick a better name for f, but since
    # ## it is only used in a few lines and it's quite
    # ## standard to call your opened file 'f', this
    # ## is okay here.
    lines = f.readlines()
    # ## First element of entity file is the ID, but
    # ## we're only interested in the actual entity
    # ## name for our dictionary, so we read only the
    # ## second item.
    entity_name_index = 1
    entity_names = [line.split("\t")[entity_name_index] for line in lines]
    # ## Calling this entity_names to show we're not
    # ## yet filling in the entities dictionary we
    # ## defined above. Splitting reading the file
    # ## and filtering into two steps makes it much
    # ## easier to read and understand.

  for name in entity_names:
    name_parts = name.split()
    if name_parts[0] not in entities:
      # We're creating a dictionary organised by
      # the first token of the entities.
      new_entry = [name.strip()]
      entities[name_parts[0]] = new_entry
    else:
      entities[name_parts[0]].append(name.strip())

  # ## Note the filtering part is gone here, and
  # ## placed into its own function. A function should
  # ## do one thing and one thing only.
  return entities


def filter_entities(entities,
                    filters_path="filters.txt"):
  """Filters entries from the values list of the entity dictionary.

  Parameters
  ----------
  entities: a dictionary of entities

  filters_path: path to a text file containing
  entries to be removed, defaults to filters.txt

  Returns
  -------
  Filtered dictionary.
  """
  # ## When you saw ["University", "Police", ...
  # ## in the code, hopefully you screamed
  # ## "hardcoded! 🙀". Obviously, we're moving terms
  # ## to be filtered into a separate file, so they
  # ## can be easily changed without having to change
  # ## the code. Using default parameters here again,
  # ## to give the user flexibility to supply their
  # ## own list or use the default list.
  with open(filters_path) as f:
    lines = f.readlines()
    filters = [line.strip() for line in lines]

  # ## filter is already a python keyword, so we're
  # ## using filter_ to differentiate it from the
  # ## default meaning. This is the standard way to
  # ## resolve such naming collisions.
  for filter_ in filters:
    if filter_ in entities and len(entities(filter_)) > 1:
      entities[filter_] = [entity for entity in entities[filter_]
                           if entity != filter_]

  # ## Such statements are not very efficient, but
  # ## they can help an alot with the readability of
  # ## your code.
  filtered_entities = entities
  return filtered_entities


# ## This is some code that was left in the
# ## load_entities function for testing. Not good
# ## practice to leave such code in, better to put it
# ## in its own well-documented function.
def print_entities(entities, n=0):
  """Prints first n elements of a dictionary.

  Parameters
  ----------
  entities: dictionary containing as values lists

  n: number of entries to print
  """
  # ## Note the n=0 part of the parameters: This
  # ## allows us to set default parameters.

  for entity in list(entities)[:n]:
    # ## Here, I'm using _string in the variable name
    # ## because I'm creating a temporary variable
    # ## for a representation of entities that is not
    # ## 'natural' or logical. Also, joining over ", "
    # ## instead of "," because it looks nicer.
    entities_string = ", ".join(entities[entity])
    print(entity + " : " + entities_string)


def find_entities(haystack, entities, outpath):
  """Finds in free text entities and writes them to
  output file.

  Parameters
  ----------
  haystack: the path to a file containing articles,
  tab separated ID and plain text, in which to find
  entities.

  entities: a dictionary containing the first word of
  all the entities to be found as keys, and as value
  a list of all entities that begin with this key.

  output: the path to where the results are written.
   Format is .csv: article ID, token ID, match
  """
  with open(haystack) as f:
    texts = f.readlines()
    # ## Code should contain no print statements
    # ## unless they are in functions explicitly made
    # ## for printing.

  outfile = open(outpath, 'w')
  # ## Here, we're entering a longer block of code,
  # ## and we've used f before. We could use f
  # ## again, but we could confuse the reader, so
  # ## let's use a new name for our outfile. Note
  # ## how we're not using the with syntax to keep
  # ## indentation down.
  for text in texts:
    tokens = text.split()

    # ## This is a very elegant and pythonic way
    # ## to check if a list is empty. Also, to keep
    # ## indentation down, we're inverting the logic
    # ## so that the text get's skipped if there are
    # ## no tokens in it: For this, we use continue
    # ## akin to how we've used return in exercise-4.
    # ## continue will end the current iteration, and
    # ## jump to the next item in the loop (the next
    # ## text in this case).
    if not tokens:
      continue

    # ## Before this was called artid, but it
    # ## we're calling our texts text now - decide
    # ## on one concept name and stick to it!
    text_id = tokens[0]
    bad_characters = ("@", "<")
    filtered_tokens = [token for token in tokens
                       if not token.startswith(bad_characters)]
    # ## Note the use of startswith() above, which
    # ## is much more readable than t[0] == ...

    # ## We've used a counter variable before to
    # ## keep track of token ID, but a more elegant
    # ## way is to use enumerate(), which allows us
    # ## to iterate through a list while keeping
    # ## count of its items.
    for token_index, token in enumerate(filtered_tokens):
      if token in entities:
        # first word is a match, so now we'll try to find
        # the longest matching entry of entities
        haystack = entities[token]
        longest_match = ""
        for entity in haystack:
          if len(entity) > len(longest_match):
            entity_tokens = entity.split()
            start = token_index
            end = start + len(entity_tokens)
            candidate = " ".join(filtered_tokens[start:end])
            if candidate == entity:
              longest_match = candidate

        # ## Again, an elegant way to check if
        # ## a string is empty:
        if longest_match:
          output = ",".join([str(text_id),
                             str(token_index),
                             longest_match])
          outfile.write(output + "\n")

  outfile.close()


if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')
