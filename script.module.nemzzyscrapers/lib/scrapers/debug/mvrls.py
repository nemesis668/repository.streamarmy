import re, requests
from bs4 import BeautifulSoup
from cfscrape import *
import xbmc
import xbmcgui
dialog = xbmcgui.Dialog()

Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
scraper = cfscrape.CloudflareScraper()
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('MVRLS')
class Scraper:
	def __init__(self):
		self.Base = 'http://mvrls.com/'
		self.Search = ('search/%s/feed/rss2/')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			try:
				found = 0
				MovieName = term.upper()
				term = term.replace(' ','+')
				link = scraper.get(self.Base+self.Search %imdb , headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				data = soup.find_all('item')
				for content in data:
					links = content.find_all('enclosure')
					for sources in links:
						source = sources['url']
						found += 1
						if 'nitroflare' in source:
							if '3d' in source:
								title = ('MVRLS ( RD ) | 3D | %s' %MovieName )
								quality = '6'
							elif '2160' in source:
								title = ('MVRLS ( RD ) | UHD ( 4K ) | %s' %MovieName )
								quality = '5'
							elif '1080' in source:
								title = ('MVRLS ( RD ) | FHD | %s' %MovieName )
								quality = '6'
							elif '720' in source:
								title = ('MVRLS ( RD ) | HD | %s' %MovieName )
								quality = '7'
							elif 'BRRip' in source:
								title = ('MVRLS ( RD ) | FHD | %s' %MovieName )
								quality = '6'
							elif 'bluray' in source:
								title = ('MVRLS ( RD ) | FHD | %s' %MovieName )
								quality = '6'
							elif 'bdrip' in source:
								title = ('MVRLS ( RD ) | FHD | %s' %MovieName )
								quality = '6'
							else:
								title = ('MVRLS ( RD ) | SD | %s' %MovieName )
								quality = '8'
							self.links.append({'title': title, 'url': source, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else: pass