import twitter
import json

CONFIG_FILE = "config.json"

with open(CONFIG_FILE, "r+") as f:
	keys = json.load(f)

api = twitter.Api(consumer_key=keys["consumer_key"],
                  consumer_secret=keys["consumer_secret"],
                  access_token_key=keys["access_token"],
                  access_token_secret=keys["access_token_secret"])

content = api.GetHomeTimeline(count=200, exclude_replies=True, contributor_details=True)

for tweet in content:
	print(tweet.user.name)
	print(tweet.text)
	print("---------------------------------------------")