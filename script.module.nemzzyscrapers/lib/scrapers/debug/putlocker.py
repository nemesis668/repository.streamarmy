import re, requests,xbmc
from bs4 import BeautifulSoup
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
GoodFiles = ['.mp4', '.mkv']
import xbmcgui
dialog = xbmcgui.Dialog()
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('PUTLOCKER')
class Scraper:
	def __init__(self):
		self.Base = 'http://putlocker32.com/'
		self.Search = ('full-movie-search/%s.html')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			try:
				found = 0
				check = term
				term = term.replace(' ','+')
				link = requests.get(self.Base+self.Search % term, headers = Headers).content
				pattern = r'''<div\s+class="item">.*?href=['"](.*?)['"].*?<i>(.*?)<.*?<b>Release:(.*?)<'''
				findmatches = re.findall(pattern,link,flags=re.DOTALL)
				for link,title,date in findmatches:
					if year == date.strip() and check.lower() in title.lower():
						nextphase = requests.get(link).content
						pattern = r'''<p class="server_version">.*?href=['"](.*?)['"]'''
						findall = re.findall(pattern,nextphase,flags=re.DOTALL)
						for links in findall: 
							if not 'other.html' in links:
								found += 1
								source = ('PUTLOCKER | UNKOWN | %s' %check.upper())
								quality = '9'
								self.links.append({'title': source, 'url': links, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else: pass