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
		self.Base = 'http://www.seehd.pl/'
		self.Search = ('%s-watch-online/')
		self.links = []

	def main(self, Term):
		#time.sleep(randint(1,10))
		Term = Term.split('|||')[0]
		Term = Term.replace(' ','-').replace(':','')
		link = scraper.get(self.Base+self.Search %Term).content
		try: quality = re.findall('<strong>Quality:</strong>(.*?)<',link,flags=re.DOTALL)[0].strip()
		except IndexError: quality = 'Unkown'
		pattern = r'''<iframe.+?src=['"](.*?)['"]'''
		sources = re.findall(pattern,link,flags=re.DOTALL)
		if not sources:
			return False
		for source in sources:
			title = 'SeeHD | ' + quality
			if 'bluray' in quality.lower(): sort = '1'
			elif 'high' in quality.lower(): sort = '2'
			else : sort = '3'
			self.links.append({'title': title, 'url': source, 'quality' : sort})
		return self.links
