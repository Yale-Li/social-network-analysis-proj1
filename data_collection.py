import requests
import csv


DEFAULT_ID = '1620651618038419456'
DEFAULT_NAME = 'Yale'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGRGlgEAAAAAAm75qarmeNp3oZLmLmxvUAFjRKQ%3DwvzR3y8uGOJeuMLM5Y7pxJ2WU5AHYCMhcuo62EMSnHbYine95p'

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
    users = read_from_csv('users')
    relationship = read_from_csv('relationship')
    
    index = 0
    if len(users) == 0:
        json_response = get_following(DEFAULT_ID)
        users = [{'id': DEFAULT_ID, 'name': DEFAULT_NAME, 'mark': True}] + json_response['data'][:20]
        relationship = [{'id': DEFAULT_ID, 'following': user['id']} for user in users]
    else:
        for idx, user in enumerate(users):
            if user['mark'] != 'True':
                index = idx
                break

    while len(users) < 400:
        userid = users[index]['id']
        json_response = get_following(userid)

        users[index]['mark'] = True
        count = json_response['meta']['result_count']
        if count > 10:
            count = 10

        for i in range(count):
            users.append(json_response['data'][i])
            relationship.append({'id': userid, 'following': json_response['data'][i]['id']})
        index += 1

    return (users, relationship)

def write_to_csv(name, head, data):
    with open(f'{name}.csv', 'w') as f:
        write = csv.DictWriter(f, fieldnames=head)
        write.writeheader()
        write.writerows(data)

def read_from_csv(name):
    with open(f'{name}.csv', 'r') as f:
        read = csv.DictReader(f)
        # next(read)
        return [row for row in read]


if __name__ == '__main__':

    (users, relationship) = fetch_whole_data()

    write_to_csv('users', ['id', 'name', 'username', 'mark'], users)
    write_to_csv('relationship', ['id', 'following'], relationship)
    # print(read_from_csv('users'))