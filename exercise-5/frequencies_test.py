import frequencies as f

def test_traverse_directory():
  files = f.traverse_directory('corpus')
  assert 'corpus/venus-and-adonis_TXT_FolgerShakespeare.txt' in files
  assert not '.DS_Store' in files
  assert len(files) == 42

def test_tokenize_file():
  tokens = f.tokenize_file('corpus/antony-and-cleopatra_TXT_FolgerShakespeare.txt')
  assert 'triumvir' in tokens
  assert not 'Cleopatra' in tokens
  assert 'cleopatra' in tokens
  assert not 'Perchance?' in tokens
  assert 'perchance' in tokens
  assert not '\n' in tokens
  assert not '[to' in tokens
  assert not '' in tokens
  assert len(tokens) > 26000
  assert len(tokens) < 27000
  assert len([ token for token in tokens if token[-1] == '.']) == 0

def test_compute_counts():
  fr = f.compute_counts(['corpus/henry-vi-part-2_TXT_FolgerShakespeare.txt'])
  assert fr['crows'] == 2
  assert fr['irish'] == 1
  assert fr['sin'] == 6
  assert len([ token for token, value in fr.items() if value == 0]) == 0

def test_sorted_counts():
  fr = { 'rose' : 15, 'hereby' : 1 , 'die' : 45 }
  fr = f.sort_counts(fr)
  assert fr[0][1] > fr[1][1]

def test_write_frequencies():
  fr = [ [ 'rose', 15 ], 
         [ 'hereby', 1 ] , 
         [ 'die', 45 ] ]
  f.write_frequencies(fr,'test.csv')
  with open('test.csv') as fi:
    lines = fi.read().splitlines()
    assert len(lines) == 3
    assert lines[0].split(',')[0] == '1'
    assert not lines[0][-1] == ','
    assert lines[0].split(',')[1] == 'rose'
    assert lines[0].split(',')[2] == '15'
    assert lines[0].split(',')[3][:4] == str(15/61)[:4]
