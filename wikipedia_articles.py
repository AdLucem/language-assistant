import wikipedia

def fact(topic):

	return wikipedia.summary(topic)

## TODO: get list of wikipedia unusual articles: https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles
## - randomly choose one among them
## - get facts(that_article)