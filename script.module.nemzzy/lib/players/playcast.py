import requests
import base64
import json
import re

def resolve(link):
    ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
    curl = re.compile('curl\s*=\s*[\'"](.+?)[\'"]')
    domain = 'playcast.se'
    embedd = 'http://www.playcast.se/stream.php?id='+link+'&width=100%&height=100%&stretching=uniform'
    resp = requests.get(embedd).content
    decoded = base64.b64decode(curl.findall(resp)[0])
    decoded += '|User-Agent=%s&Origin=%s&Referer=%s&' % (ua, 'http://www.playcast.se', embedd)
    return decoded