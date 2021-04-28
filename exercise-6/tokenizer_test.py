import tokenizer
import sys

def test_parse_arguments(monkeypatch):

  with monkeypatch.context() as m:
    m.setattr(sys, 'argv', ['tokenizer.py','-s', 'Loret', 'out.csv'])
    inp, outp = tokenizer.parse_arguments()

    assert(inp == "Loret")
    assert(outp.endswith("out.csv"))
  
  with monkeypatch.context() as m:
    m.setattr(sys, 'argv', ['tokenizer.py','-f', 'erste_gedichte.txt', 'lol'])
    inp, outp = tokenizer.parse_arguments()
    assert("Die Stadt verschwimmt wie hinter Glas." in inp)

def test_write():
  tokenizer.write("Die Stadt verschwimmt wie hinter Glas.", 'test.csv')
  with open('test.csv','r') as f:
    test_file = f.readlines()
    test_line = test_file[1].split('\t')
    assert(test_line[0] == 'Stadt')
    assert(test_line[1].strip() == 'stadt')

  

