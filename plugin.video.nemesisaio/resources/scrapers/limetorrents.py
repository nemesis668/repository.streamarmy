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
		self.Base = 'https://www.limetorrents.zone/'
		self.Search = ('/search/all/%s/leechs/1/')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term:
			Term = Term.replace('TV|||','')
			Term = Term.split('|||')[0]
			Term = Term.replace(' ','-')
			link = scraper.get(self.Base+self.Search %Term, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}).content
			match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]
			pattern = r'''href=['"]([^'"]+)['"]'''
			getlinks = re.findall(pattern,match)
			if not getlinks: return False
			for link in getlinks:
				if self.Base not in link and '.html' in link:
					link = self.Base+link
					if 'uhd' in link.lower(): sort = '0' ; qual = '4K UHD'
					elif '2160' in link.lower(): sort = '0'; qual = '4K UHD'
					elif '1080' in link.lower(): sort = '1'; qual = '1080'
					elif '720' in link.lower(): sort = '2'; qual = '720'
					else : sort = '3'; qual = 'SD'
					title = 'LimeTorrents ( Torrent ) | ' + qual
					self.links.append({'title': title, 'url': link, 'quality' : sort})
			return self.links
		else:
			Year = Term.split('|||')[1]
			Year = Year.strip()
			Term = Term.replace('|||',' ')
			#CheckMe = Term
			Term = Term.strip()
			Term = Term.replace(' ','-')
			link = scraper.get(self.Base+self.Search %Term, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}).content
			match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]
			pattern = r'''href=['"]([^'"]+)['"]'''
			getlinks = re.findall(pattern,match)
			if not getlinks: return False
			for link in getlinks:
				if self.Base not in link and '.html' in link and Year in link:
					link = self.Base+link
					if 'uhd' in link.lower(): sort = '0' ; qual = '4K UHD'
					elif '2160' in link.lower(): sort = '0'; qual = '4K UHD'
					elif '1080' in link.lower(): sort = '1'; qual = '1080'
					elif '720' in link.lower(): sort = '2'; qual = '720'
					else : sort = '3'; qual = 'SD'
					title = 'LimeTorrents ( Torrent ) | ' + qual
					self.links.append({'title': title, 'url': link, 'quality' : sort})
			return self.links
