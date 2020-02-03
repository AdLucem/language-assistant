"""Various tweet search techniques"""

from whoosh.index import create_in
from whoosh.fields import *


class WhooshSearch:

	def __init__(self, indexdir):

		self.schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
		index = create_in("indexdir", schema)
		writer = ix.writer()
class Search:

	def __init__(self, list=[], num_tweets_returned=[]):

		self._list = list
		self.num_tweets_ret = num_tweets_returned



	def keyword_search(self):
