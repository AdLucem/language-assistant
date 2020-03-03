
"""All functions here take a twitter.Api object and return a list of twitter.Status objects"""

def get_own_timeline(api):
	"""Get tweets from authenticating user- your- own timeline"""

	content = api.GetHomeTimeline(count=200, 
		                          exclude_replies=True, 
		                          contributor_details=True
		                          )
	return content

def get_search(api, query):
	"""Get tweets from querying a search term"""

	content = api.GetSearch(count=200,
							term=query,
							lang="en"
							)
	return content

