import requests
import re
import cfscrape
import xbmcgui
import xbmc
from bs4 import BeautifulSoup
dialog = xbmcgui.Dialog()
scraper = cfscrape.create_scraper()

Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
class Scraper:
	def __init__(self):
		self.Base = 'https://zooqle.unblockit.ca/'
		self.Search = ('search?q=%s')
		self.links = []

	def Index(self,type,term,year,imdb,torrents):
		if type == 'MOVIE':
			if torrents == 'Allowed':
				try:
					cleanterm = term.replace(' ','+')
					link = scraper.get(self.Base+self.Search % cleanterm, headers=Headers).content
					dialog.ok("ZQ",str(link))
					soup = BeautifulSoup(link, 'html5lib')
					data = soup.find_all('tr')
					#dialog.ok("HERE",str(data))
					for links in data:
						title = links.find('a').text
						if term.lower() in title.lower() and year in title:
							source = links.find('a', title={'Magnet link'})
							source = source['href']
							if '480' in title:
								title2 = ('ZOOGLE ( Torrent ) | SD | %s' % title)
								quality = '8'
							elif '720' in title:
								title2 = ('ZOOGLE ( Torrent ) | HD | %s' % title)
								quality = '7'
							elif '1080' in title:
								title2 = ('ZOOGLE ( Torrent ) | FHD | %s' % title)
								quality = '6'
							elif '2160' in title:
								title2 = ('ZOOGLE ( Torrent ) | UHD ( 4K ) | %s' % title)
								quality = '5'
							else:
								title2 = ('ZOOGLE | SD | %s' %title )
								quality = '8'
							self.links.append({'title': title2, 'url': source, 'quality': quality})
					return self.links
				except Exception as c:
					xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
			else: pass
		else:
			if torrents == 'Allowed':
				try:
					cleanterm = term.replace(' ','+')
					searchthrase = ('%s+s%se%s' % (cleanterm,year,imdb))
					link = scraper.get(self.Base+self.Search % searchthrase, headers=Headers,timeout=10).content
					soup = BeautifulSoup(link, 'html5lib')
					data = soup.find_all('tr')
					for links in data:
						try:
							title = links.find('a').text
							if term.lower() in title.lower() and year in title:
								source = links.find('a', title={'Magnet link'})
								source = source['href']
								if '480' in title:
									title2 = ('ZOOGLE ( Torrent ) | SD | %s' % title)
									quality = '4'
								elif '720' in title:
									title2 = ('ZOOGLE ( Torrent ) | HD | %s' % title)
									quality = '3'
								elif 'hdtv' in title.lower():
									title2 = ('ZOOGLE ( Torrent ) | HD | %s' % title)
									quality = '3'
								elif '1080' in title:
									title2 = ('ZOOGLE ( Torrent ) | FHD | %s' % title)
									quality = '2'
								elif '2160' in title:
									title2 = ('ZOOGLE ( Torrent ) | UHD ( 4K ) | %s' % title)
									quality = '0'
								else:
									title2 = ('ZOOGLE( Torrent ) | SD | %s' %title )
									quality = '6'
								self.links.append({'title': title2, 'url': source, 'quality': quality})
						except: pass
					return self.links
				except Exception as c:
					xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
			else: pass