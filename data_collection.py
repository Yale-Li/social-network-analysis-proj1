import requests
import json

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGRGlgEAAAAAAm75qarmeNp3oZLmLmxvUAFjRKQ%3DwvzR3y8uGOJeuMLM5Y7pxJ2WU5AHYCMhcuo62EMSnHbYine95p'
yale_id = '1620651618038419456'

search_url = 'https://api.twitter.com/2/tweets/search/recent'
search_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}

following_url = 'https://api.twitter.com/2/users/{}/following'.format(yale_id)
me_url = 'https://api.twitter.com/2/users/me'


def oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    return r

def get(url, params={}):
    response = requests.get(url, auth=oauth, params=params)
    return response.json()

if __name__ == '__main__':
    json_response = get(following_url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
