import requests
import re
import xbmc
import xbmcgui
import time
dialog = xbmcgui.Dialog()

class Scraper:
	def __init__(self):
		self.Base = 'http://rarbgproxy.org'
		self.Search = ('/torrents.php?search=%s')
		self.links = []

	def main(self, Term):
		Year = Term.split('|||')[1]
		Term = Term.replace('|||','+')
		Term = Term.strip()
		Term = Term.replace(' ','+')
		link = requests.get(self.Base+self.Search % Term, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}).content
		pattern = r'''<tr class="lista2">.*?onmouseout=.*?href="(.*?)"\stitle="(.*?)"'''
		getresults = re.findall(pattern,link)
		if not getresults:
			return False
		else:
			for link,title in getresults:
				if not self.Base in link: link = slef.Base + link
				if not Year in title: continue
				if '4k' in title.lower() or 'uhd' in title.lower():
					sort = '0'
					title = 'Rarbg | 4K'
				elif 'bluray' in title.lower():
					sort = '1'
					title = 'Rarbg | 1080'
				elif '1080' in title.lower():
					sort = '2'
					title = 'Rarbg | 1080'
				elif '720' in title.lower():
					sort = '3'
					title = 'Rarbg | 720'
				else :
					sort = '4'
					title = 'Rarbg | SD'
				self.links.append({'title': title, 'url': link, 'quality' : sort})
		return self.links
