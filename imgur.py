import syslog
import time
import sys
import random
import threading
import urllib.parse
import urllib.request
import json

def get_imgur(transcript):
    types = ['png', 'jpg', 'gif', 'anigif']
    rtype = types[random.randint(0, len(types) - 1)]
    words = transcript.split()
    words = sorted(words, key=len)
    word = words[len(words) - 1]
    url = 'https://api.imgur.com/3/gallery/search?q=' + urllib.parse.quote(word) +'&q_type=' + rtype
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Client-ID 62a1dd4dde196de')
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    urls = []
    for item in data['data']:
        try:
            url = item['link']
            if url.startswith('http'):
                urls.append(url)
        except:
            pass

    if urls:
        n = random.randint(0, len(urls) - 1)
        print('found image: %s' % urls[n])
        return urls[n]
    else:
        print('found no image')
    return ' '

get_imgur('monocle coffees')
