
def find_cs(path, cs,out, ):
  with open(path ) as f:
    texts = f.readlines ( )
    print(len(texts))

  # texts = texts[:50]
  with open (out,'w') as g:
    for t in texts:
      c = t.split()
      if c :
        artid =c[ 0 ]
        c = [w for w in c \
            if w[0] not in [ "@", "<" ] ]

        counter = 0
        for word in c:
          if word in cs:
                # find longest match
                # print("word: " + word)
            hayst = cs[word]
                    
            longest = 0
            match = ""
            for h in hayst:
              hlen = len(h)
              if hlen > longest:
                  tst = " ".join(c[counter:counter+len(h.split())])

              if h == tst:
                  # print("tst: " + tst)
                  longest = hlen
                  match = tst
                
                  # print("Found city: " + word)
            if match:
                   g.write(artid + "," + str(counter) + "," + match + "\n")
          counter += 1

  

def ld(path):

    cits = {}
    with open(path) as f:
      l = [l.split("\t")[1] for l in f.readlines() ]
    for cit in l:
        cs = cit.split()
        if  cs[0] not in cits:
          cits[cs[0]] = [ cit.strip() ]
        else:
          cits[cs[0]].append(cit.strip())
    
    for cit in list(cits)[:6]:
        print(cit + " : " + ",".join(cits[cit]))
    
    # print(cits["University"])

    filters = ["University", "Police", "Of", "Central"]
    for f in filters :
        if f in cits:
            cits[f] = [ c for c in cits[f] if c != f ]

    # print(cits["University"])

    # print(cits)
    return cits

def main(haystack, needles, output):
  
  cs = ld(needles)
  find_cs(haystack, cs, output)

if __name__ == "__main__":
  main('text.txt', 'cities15000.txt', 'output.txt')