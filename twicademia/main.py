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


def run(args):

    if args.search == "own":
        tweets = user_text(
            sc.get_own_timeline(api))

    if args.search == "keyword":
        tweets = text(sc.get_search(api, args.topic))

    return tweets


def display(tweets):

    for tweetails in tweets:
        for detail in tweetails:
            print(detail)
        print("---------------------------------------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', type=str, default='own',
                        help='What kind of search to perform')
    parser.add_argument('--topic', type=str, default='',
                        help='Topic to search for')
    args = parser.parse_args()

    display(run(args))
