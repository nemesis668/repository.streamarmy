import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
GoodFiles = ['.mp4', '.mkv']

class Scraper:
	def __init__(self):
		self.Base = 'http://blaxup.in/'
		self.Search = ('search/?words=%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if type == 'MOVIE':
			try:
				#links = []
				filmname = term.title()
				found = 0
				term = term.replace(' ','+')
				#print '########### RESULTS FROM BLAXUP ###########'
				link = requests.get(self.Base+self.Search % term, headers = Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				data = soup.find('section' , class_={'block_style11 w_px_re_3'})
				results = data.find_all('a')
				for links in results:
					checklink = links['href']
					if year in checklink:
						link = requests.get(checklink, headers = Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						data = soup.find('div', class_={'tab-content'})
						sources = data.find_all('ul')
						for content in sources:
							try: source = content.a['href']
							except: continue
							if any(x in source for x in GoodFiles):
								found += 1
								if '480' in source:
									title = ('BLAX | SD | DIRECT | %s' % filmname)
									quality = '4'
								elif '720' in source:
									title = ('BLAX | HD | DIRECT | %s' % filmname)
									quality = '3'
								elif '1080' in source:
									title = ('BLAX | FHD | DIRECT | %s' % filmname)
									quality = '2'
								else:
									title = ('BLAX | Unkown | DIRECT | %s' % filmname)
									quality = '6'
								self.links.append({'title': title, 'url': source, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else: pass

