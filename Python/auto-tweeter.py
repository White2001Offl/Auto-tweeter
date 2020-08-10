import requests
from html.parser import HTMLParser
from requests.exceptions import HTTPError
import json
c = 1
counter = 0

def get_words():
    try:
        response = requests.get('https://random-word-api.herokuapp.com/word?number=15')
        # access JSOn content
        jsonResponse = response.json()
        data = ''
        for i in range(0,len(jsonResponse)):
            data = data + jsonResponse[i] + ' '
        return data

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return '0'
    except Exception as err:
        print(f'Other error occurred: {err}')
        return '0'

def send_request(data, token , csrf , cookie_data):
    try:
        header = {
            'Host': 'api.twitter.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'authorization': f'Bearer {token}',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
            'x-csrf-token': f'{csrf}',
            'Origin': 'https://twitter.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://twitter.com/',
            'Cookie': f'{cookie_data}',
        }
        response = requests.post('https://api.twitter.com/1.1/statuses/update.json',
                         data='include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&simple_quoted_tweet=true&trim_user=false&include_ext_media_color=true&include_ext_media_availability=true&auto_populate_reply_metadata=false&batch_mode=off&status={}'.format(data),
                         headers=header)
        # access JSOn content
        jsonResponse = response.json()
        print('Tweet of ID {} has been submitted'.format(jsonResponse['id_str']))
        try:
            if jsonResponse['id_str']:
                return 'Tweet Successful'
        except KeyError:
            error = jsonResponse['errors'][0]['code']
            return error

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return '0'
try:
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['data']:
            input_data = p['hastag']
            token = p['token']
            csrf = p['csrf']
            cookie_data = p['cookie']
            data = get_words() + '\n' + input_data
            result = send_request(data,token,csrf,cookie_data)
            if result == '326' or result == 326:
                print('Account Locked, Relogin to your account and follow process to unlock your account')
                c=0
                break
            elif result == '185' or result == 185:
                print('Your Daily Status Tweet Limit has over Try again tomorrow')
                c=0
                break
            elif result == '353' or result == 353:
                print('Your Previous Data is expired. Enter new data')
                c=0
                raise Exception('Expired')
            elif result == '32' or result == 32:
                print('Incorrect Details. Please recheck your details')
                c=0
                raise Exception('Incorrect Details')
        
except FileNotFoundError:
    input_data = input('Enter your hastags / mentions: ')
    token = input('Enter Authorization Token : ')
    csrf = input('Enter CSRF Token: ')
    cookie_data = input('Enter Cookie Data: ')
    tweet = {}
    tweet['data'] = []
    tweet['data'].append({
        'hastag': '{}'.format(input_data),
        'token': '{}'.format(token),
        'csrf': '{}'.format(csrf),
        'cookie': '{}'.format(cookie_data)
    })
    with open('data.txt', 'w') as outfile:
        json.dump(tweet, outfile)
    
    data = get_words() + '\n' + input_data
    result = send_request(data,token,csrf,cookie_data)
    if result == '326' or result == 326:
        print('Account Locked, Relogin to your account and follow process to unlock your account')
        c=0
    elif result == '185' or result == 185:
        print('Your Daily Status Tweet Limit has over Try again tomorrow')
        c=0
    elif result == '353' or result == 353:
        print('Your Previous Data is expired. Enter new data')
        c=0
    elif result == '32' or result == 32:
        print('Incorrect Details. Please recheck your details')
        c=0

except Exception as err:
    c=1
    input_data = input('Enter your hastags / mentions: ')
    token = input('Enter Authorization Token : ')
    csrf = input('Enter CSRF Token: ')
    cookie_data = input('Enter Cookie Data: ')
    tweet = {}
    tweet['data'] = []
    tweet['data'].append({
        'hastag': '{}'.format(input_data),
        'token': '{}'.format(token),
        'csrf': '{}'.format(csrf),
        'cookie': '{}'.format(cookie_data)
    })
    with open('data.txt', 'w') as outfile:
        json.dump(tweet, outfile)
        
    data = get_words() + '\n' + input_data
    result = send_request(data,token,csrf,cookie_data)
    if result == '326' or result == 326:
        print('Account Locked, Relogin to your account and follow process to unlock your account')
        c=0
    elif result == '185' or result == 185:
        print('Your Daily Status Tweet Limit has over Try again tomorrow')
        c=0
    elif result == '353' or result == 353:
        print('Your Previous Data is expired. Enter new data')
        c=0
    elif result == '32' or result == 32:
        print('Incorrect Details. Please recheck your details')
        c=0

while c != 0 and counter < 60:
    data = get_words() + '\n' + input_data
    result = send_request(data,token,csrf,cookie_data)
    if result == '326' or result == 326:
        print('Account Locked, Relogin to your account and follow process to unlock your account')
        c=0
    elif result == '185' or result == 185:
        print('Your Daily Status Tweet Limit has over Try again tomorrow')
        c=0
    elif result == '353' or result == 353:
        print('Your Previous Data is expired. Enter new data')
        c=0
    elif result == '32' or result == 32:
        print('Incorrect Details. Please recheck your details')
        c=0
    else:
        counter = counter + 1
