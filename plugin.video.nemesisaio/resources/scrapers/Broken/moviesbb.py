import requests
import re
import cfscrape
import xbmc
import xbmcgui
import time
scraper = cfscrape.CloudflareScraper()

class Scraper:
	def __init__(self):
		self.Base = 'https://movieswbb.nocensor.icu'
		self.Search = ('/?s=%s')
		self.links = []

	def main(self, Term):
		Content = []
		GoodMatchs = ['rapidgator.net/file','filepup']
		qualitys = []
		finallinks = []
		combined = []
		Term = Term.replace(' ','+').replace(':','')
		link = scraper.get(self.Base+self.Search %Term).content
		pattern = r'''<div class="blog-category">.+?href=.+?>(.*?)<.+?</ul>.+?href=['"](.*?)['"]'''
		results = re.findall(pattern,link,flags=re.DOTALL)
		if not results:
			return False
		for quality,link in results:
			if quality == '': quality = 'Unkown'
			qualitys.append(quality)
			findplays = scraper.get(link).content
			pattern = r'''href=['"]([^'"]*)['"]'''
			plays = re.findall(pattern,findplays,flags=re.DOTALL)
			for links in plays:
				if any(x in links for x in GoodMatchs):
					title = '[COLOR lime]MoviesBB ( REAL DEBRID ) | ' + quality + '[/COLOR]'
					self.links.append({'title': title, 'url': links})
		return self.links