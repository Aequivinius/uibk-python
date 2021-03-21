import porter as p

def test_is_consonant():
  assert p.is_consonant("habibi", 0)
  assert p.is_consonant("yalla", 0)
  assert not p.is_consonant("eglise", 3)
	

def test_contains_vowel():
  assert p.contains_vowel("habibi")
  assert not p.contains_vowel("crwth")

	
def test_ends_in_double_consonant():
  assert not p.ends_in_double_consonant("lock")
  assert not p.ends_in_double_consonant("log")
  assert p.ends_in_double_consonant("logg")
				
	
def test_measure():
  assert p.measure("trouble") == 1
  assert p.measure("troubles") == 2


def test_step_1a():
	assert p.step_1a("caresses") == "caress"
  assert p.step_1a("ponues") == "poni"
  assert p.step_1a("caress") == "caress"
  assert p.step_1a("cats") == "cat"

def test_step_1b():
  assert p.step_1b("feed") == "feed"
  assert p.step_1b("agreed") == "agree"
  assert p.step_1b("plastered") == "plaster"
  assert p.step_1b("sing") == "sing"
  assert p.step_1b("motoring") == "motor"
  assert p.step_1b("conflated") == "conflate"
  assert p.step_1b("hopping") == "hop"
  assert p.step_1b("hissing") == "hiss"
  assert p.step_1b("failing") == "fail"
  assert p.step_1b("filing") == "file"

def test_step_1c():
  assert p.step_1c("happy") == "happi"
  assert p.step_1c("sky") == "sky"

def test_step_2():
  assert p.step_2("relational") == "relate"
  assert p.step_2("sensibiliti") == "sensible"
  assert p.step_2("decisiveness") == "decisive"
  assert p.step_2("radicalli") == "radical"
  assert p.step_2("vileli") == "vile"

def test_step_3():
  assert p.step_3("formative") == "form"
  assert p.step_3("hopeful") == "hope"
  assert p.step_3("goodness") == "good"
  assert p.step_3("electriciti") == "electric"

def test_step_4():
  assert p.step_4("revival") == "reviv"
  assert p.step_4("allowance") == "allow"
  assert p.step_4("dependent") == "depend"
  assert p.step_4("activate") == "activ"
  assert p.step_4("effective") == "effect"

def test_step_5a():
  assert p.step_5a("rate") == "rate"
  assert p.step_5a("probate") == "probat"
  assert p.step_5a("cease") == "ceas"

def test_step_5b():
  assert p.step_5b("controll") == "control"
  assert p.step_5b("roll") == "roll"

