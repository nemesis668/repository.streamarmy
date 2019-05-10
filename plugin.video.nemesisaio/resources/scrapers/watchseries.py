import requests
import re
import xbmc
import xbmcgui
import time
from resources.libs.modules import cfscrape
from random import randint

dialog = xbmcgui.Dialog()
scraper = cfscrape.CloudflareScraper()
class Scraper:
	def __init__(self):
		self.Base = 'https://watchepisodeseries.unblocked.win/'
		self.Search = ('%s')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term:
			Term = Term.replace('TV|||','')
			Term = Term.split('|||')[0]
			split = re.findall('(S[0-9].*?E[0-9].)',Term)[0]
			Term = Term.replace(split,'')
			Term = Term.strip()
			Term = Term.replace(' ','-')
			link = scraper.get(self.Base+self.Search %Term).content
			pattern = r'''href=['"]([^'"]+)['"]'''
			getlinks = re.findall(pattern,link)
			if not getlinks: return False
			for link in getlinks:
				if split.lower() in link:
					link2 = scraper.get(link, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}).content
					pattern = r'''<div class="domain">.+?href=['"](.*?)['"]>(.*?)<'''
					getlink = re.findall(pattern,link2,flags=re.DOTALL)
					for url,title in getlink:
						title = ('WatchSeries | %s' %title.title())
						qual = '1'
						self.links.append({'title': title, 'url': url, 'quality' : qual})
			return self.links
		else: return False
