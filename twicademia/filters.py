
"""All functions here take a list of Status objects- as defined in the python-twitter code- and return a list of tuples"""

def user_text(twls):
	"""Username and tweet text"""

	res = map(lambda tw: (tw.user.name, tw.text), twls)
	return list(res)

def text(twls):
	"""Raw text of the tweet- put your parsing/text cleaning functions here"""

	res = map(lambda tw: ('', tw.text), twls)
	return list(res)
