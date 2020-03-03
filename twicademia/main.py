import twitter
import json
import argparse
import scraping_functions as sc
from filters import user_text, text


CONFIG_FILE = "config.json"

with open(CONFIG_FILE, "r+") as f:
	keys = json.load(f)

api = twitter.Api(consumer_key=keys["consumer_key"],
                  consumer_secret=keys["consumer_secret"],
                  access_token_key=keys["access_token"],
                  access_token_secret=keys["access_token_secret"])

tweets = text(sc.get_search(api, "coronavirus"))

for tweetails in tweets:
	for detail in tweetails:
		print(detail)
	print("---------------------------------------------")