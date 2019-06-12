import requests
import re
import xbmc
import xbmcgui
import time
from resources.libs.modules import cfscrape
from random import randint
dialog = xbmcgui.Dialog()

class Scraper:
	def __init__(self):
		self.Base = 'http://putlocker32.com'
		self.Search = ('/full-movie-search/%s.html')
		self.links = []

	def main(self, Term):

		found = 0
		Year = Term.split('|||')[1]
		Year = Year.strip()
		Term = Term.split('|||')[0]
		CheckMe = Term
		Term = Term.replace(' ','+')#.replace(':','')
		link = requests.get(self.Base+self.Search %Term).content
		pattern = r'''<div\s+class="item">.*?href=['"](.*?)['"].*?<i>(.*?)<.*?<b>Release:(.*?)<'''
		findmatches = re.findall(pattern,link,flags=re.DOTALL)
		for link,name,release in findmatches:
			if CheckMe.lower() in name.lower():
				if Year in release:
					found  += 1
					nextphase = requests.get(link).content
					pattern = r'''<p class="server_version">.*?href=['"](.*?)['"]'''
					findall = re.findall(pattern,nextphase,flags=re.DOTALL)
					for links in findall: 
						if not 'other.html' in links:
							if not 'openload' in links:
								title = 'PutLocker | HD'
								qual = '2'
								self.links.append({'title': title, 'url': links, 'quality' : qual})
		if found == 0:
			return False
		else: return self.links
