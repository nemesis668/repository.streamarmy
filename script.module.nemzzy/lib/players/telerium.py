from HTMLParser import HTMLParser
from lib import jsunpack
import requests
import urllib
import base64
import json
import re

parser = HTMLParser()
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2989.0 Safari/537.36"

class Scraper:
    def __init__(self):
        self.domain = 'telerium.tv'
        self.packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
        self.sample = 'http://totalsport.me/sx10/1live.html'
        
    def resolve(self, link):
        player, channel, referer = link.split('|||')
        
        embedd = 'https://telerium.tv/embed/{0}.html'.format(channel)
        print embedd
        resp = requests.get(embedd, headers={'User-Agent':USER_AGENT, 'Referer':referer}).content
        print resp
        packed = self.packer.findall(resp)[0]
        unpacked = jsunpack.unpack(packed)
        print unpacked
        varNames = re.compile('\$\.ajax\(\s*\{\s*url\s*:\s*atob\(rSt\((.+?)\)\)\s*\+\s*atob\(rSt\((.+?)\)\)\s*,dataType\s*:\s*[\'\"]json[\'\"]')
        vars = varNames.findall(unpacked)[0]
        part1Reversed = re.compile('{0}\s*=\s*[\'\"](.+?)[\'\"];'.format(vars[0])).findall(unpacked)[0]
        part2Reversed = re.compile('{0}\s*=\s*[\'\"](.+?)[\'\"];'.format(vars[1])).findall(unpacked)[0]
        part1 = base64.b64decode(part1Reversed[::-1])
        part2 = base64.b64decode(part2Reversed[::-1])
        
        realtoken = self.getRealToken('https:{0}{1}'.format(part1, part2), embedd)
        
        stream = 'https:{0}{1}|Referer={2}&User-Agent={3}&Origin=https://telerium.tv&Connection=keep-alive&Accept=*/*'
        stream = stream.format(part1, realtoken, urllib.quote(embedd, safe=''), USER_AGENT)
        return stream
        
    def getRealToken(self, link, referer):
        print 'requesting '+link+ ' with referer '+referer
        h = {}
        h['Accept'] = 'application/json, text/javascript'
        h['User-Agent'] = USER_AGENT
        h['Referer'] = referer
        realResp = requests.get(link, headers=h).content[1:-1]
        print 'new string is '+ realResp[::-1]
        return realResp[::-1]