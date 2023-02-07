import requests
import json
import csv


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGRGlgEAAAAAAm75qarmeNp3oZLmLmxvUAFjRKQ%3DwvzR3y8uGOJeuMLM5Y7pxJ2WU5AHYCMhcuo62EMSnHbYine95p'
yale_id = '1620651618038419456'

search_url = 'https://api.twitter.com/2/tweets/search/recent'
search_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}

userinfo_url = 'https://api.twitter.com/2/users/me'


def oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    return r

def get(url, params={}):
    response = requests.get(url, auth=oauth, params=params)
    j = response.json()
    print(j)
    return j

def get_following(user_id):
    following_url = 'https://api.twitter.com/2/users/{}/following'.format(user_id)
    return get(following_url)

def get_follower(user_id):
    follower_url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    return get(follower_url)

def get_tweet(tweet_id):
    tweet_fields = "tweet.fields=lang,author_id"
    tweet_url = "https://api.twitter.com/2/tweets?{}&{}".format(f'ids={tweet_id}', tweet_fields)
    return get(tweet_url)

def fetch_whole_data():
    json_response = get_following(yale_id)
    users = json_response['data'][:20]
    relationship = set()
    index = 0

    while len(users) < 500:
        userid = users[index]['id']
        count = json_response['meta']['result_count']
        if count > 10:
            count = 10
        for i in range(count):
            users.append(json_response['data'][i])
            relationship.append([userid, json_response['data'][i]['id']])
        # json_response = get_following(userid)
        index += 1
        # print('result', followees, relationship)

    return (users, relationship)
    
def write_to_csv(name, head, data):
    with open(f'{name}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(head)
        write.writerows(data)


if __name__ == '__main__':

    # (followees, relationship) = fetch_whole_data()
    (followees, relationship) = ([], [])
    userlist = set()
    for user in followees:
        userlist.append([user['id'], user['name']])
    write_to_csv('users', ['id', 'name'], userlist)
    write_to_csv('relationship', ['id', 'id'], relationship)