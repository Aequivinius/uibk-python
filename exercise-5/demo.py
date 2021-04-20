path = 'corpus/a-midsummer-nights-dream_TXT_FolgerShakespeare.txt'
f = open(path)
print(type(path))
print(type(f))
content = f.read()
print(type(content))
print(content[:15])
w = open('demo.txt','w')
w.write("If the shadows have offended")
w.write("Seconder Text")
w.close() # to show why we need to close

with open('demo.txt','w') as f:
  f.write('Se tu non vi pensi,\nhai persi li sensi')
  f.write("test")

#composers = { 'brahms' : 'german', 'mozart' : 'austrian', 'chopin' : 'polish'}
#with open('demo.txt', 'w') as f:
  #for key, value in composers.items():
    #f.write(key.capitalize() + " was " + value.capitalize())

  #[f.write(key.capitalize() + " was " + value.capitalize() + "\n") for key, value in composers.items()]