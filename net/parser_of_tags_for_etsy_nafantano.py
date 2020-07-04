# -*- coding: utf-8 -*-
import requests
import json
from string import ascii_lowercase
import itertools

def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)

def get_data_to_word(query_word):
    client = requests.Session()
    previous_query = 'creepy'
    url = 'https://www.etsy.com/suggestions_ajax.php?extras=%7B%26quot%3Bexpt%26quot%3B%3A%26quot%3Brandomize%26quot%3B%2C%26quot%3Blang%26quot%3B%3A%26quot%3Ben-GB%26quot%3B%2C%26quot%3Bextras%26quot%3B%3A%5B%5D%7D&version=10_12672349415_19&search_query=' + query_word + '&search_type=all&previous_query=' + previous_query
    HEADERS = {
        'Host':             'www.etsy.com',
        'User-Agent':       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept':           'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':  'en-US,en;q=0.5',
        'Accept-Encoding':  'gzip, deflate, br',
        'x-detected-locale': 'USD|en-US',
        'X-Page-GUID': 'e3521598c1e.6a9f668ea6d2b64a4656.00',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer':          'https://www.google.com/search?q=etsy&oq=etsy&aqs=chrome.0.69i59j35i39j0l2j69i60j0.1808j0j7&sourceid=chrome&ie=UTF-8',
        'Content-Type':     'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection':       'keep-alive',
        'TE': 'Trailers',
        'Upgrade-Insecure-Requests': '1',
    }

    output = json.loads(client.get(url).text)

    queries = []
    for result in output['results']:
        if result['query'] == '<span class="copy-text">find shop names containing </span><span class="normal shop-suggestion-item">' + query_word + '</span>':
            continue
        else:
            queries.append(result['query'])

    return queries

output_file = open('result.txt', 'w', encoding='utf8')

for word in iter_all_strings():
	data_to_word = get_data_to_word(word)
	print(word + ' ==>> ' + str(data_to_word) + '\n')
	output_file.write(word + ' ==>> ' + str(data_to_word) + '\n')
	
output_file.close()