import requests
import json
from bs4 import BeautifulSoup

TWITTER_BASE_URL = 'https://twitter.com'

def crawl():
    links = []
    with open("configuration.json") as configurationFile:
        configurations = json.loads(configurationFile.read())

    for url in configurations['sources']:
        request = requests.get(url) 
        
        soup = BeautifulSoup(request.content, 'html5lib') 
        tweets = soup.findAll("div", {"class": "tweet"})

        for tweet in tweets:
            tweetContent = tweet.findAll("div", {"class": "content"})[0]
            #tweetTime = tweetContent.findAll("small", {"class": "time"})[0].a.get('title')
            tweetPost = tweetContent.findAll("p", {"class": "TweetTextSize"})[0]
            tweetText = tweetPost.get_text()
            tweetTextLowerCase = tweetText.lower()
            if any(searchTerm in tweetTextLowerCase for searchTerm in configurations['search_terms']):
                links.append(TWITTER_BASE_URL + tweet['data-permalink-path'])

    return links