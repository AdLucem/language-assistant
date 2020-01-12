from nltk.corpus import wordnet as wn 
import spacy
from wikipedia_articles import fact

"""So the purpose of this application is simple. The user gives it a verb, it returns the frame of that verb as a fill-in-the-blanks"""


print("NLP libraries are initializing. I'm sorry it takes so much time. Here, read about a random topic in the meanwhile:")

print(fact("Cats"))

class Token:
	"""My program's definition of token"""

	nlp = spacy.load("en_core_web_md")

	def __init__(self, synset_id=None, text=""):
		"""Make a Token from a WordNet synset id"""

		if synset_id:
			self.synset_id = synset_id
		else:
			self.synset_id = None

		if text != "":
			self.text = text
		else:
			self.text = self.synset_id.name().split(".")[0]

		self.spacy = Token.nlp(self.text)

	def show(self):
		return self.text

	def frames(self):

		frames = ""
		for lemma in self.synset_id.lemmas():
			frames = " | ".join(lemma.frame_strings())
		return frames

	def similarity(self, token2):

		return self.spacy.similarity(token2.spacy)


def initialize_nltk():

	import nltk
	nltk.download('wordnet')

try:
	verb = input("Enter a verb:")
	original = Token(text=verb)

	synset = wn.synsets(verb, pos=wn.VERB)
	synonyms = [Token(synset_id=syn) for syn in synset]

	max_similarity = 0.0
	most_similar = ""

	for token in synonyms:
		if original.similarity(token) > max_similarity:
			max_similarity = original.similarity(token)
			most_similar = token

	print(most_similar.frames())

except LookupError:

	initialize_nltk()

## TODO: make the wikipedia random topics widget work
## - look up command line-selecting among the frames
## - how to make the program understand which frame?
## - make frames into fill-in-the-blanks