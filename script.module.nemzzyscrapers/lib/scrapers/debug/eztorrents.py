import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
from cfscrape import *
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
scraper = cfscrape.CloudflareScraper()
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('EZTORRENTS')
class Scraper:
	def __init__(self):
		self.Base = 'https://eztv1.unblocked.to/'
		self.Search = ('search/%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			pass
		else:
			try:
				if torrents == 'Allowed':
					filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
					check1 = ('s%se%s' % (year,imdb))
					term = term.replace(' ','-')
					link = scraper.get(self.Base+self.Search % term, headers=Headers).content
					soup = BeautifulSoup(link, 'html5lib')
					content = soup.find_all('td', class_={'forum_thread_post'})
					for links in content:
						mags = links.find('a',class_={'magnet'})
						if mags:
							sources = mags['href']
							if check1.lower() in sources.lower():
								if '360' in sources.lower():
									title = ('EZTOR ( Torrent ) | SD | %s' % filmname)
									quality = '8'
								elif '480' in sources.lower():
									title = ('EZTOR ( Torrent ) | SD | %s' % filmname)
									quality = '8'
								elif '720' in sources.lower():
									title = ('EZTOR ( Torrent ) | HD | %s' % filmname)
									quality = '7'
								elif 'hdtv' in sources.lower():
									title = ('EZTOR ( Torrent ) | HD | %s' % filmname)
									quality = '7'
								elif '1080' in sources.lower():
									title = ('EZTOR ( Torrent ) | FHD | %s' % filmname)
									quality = '6'
								elif '2160' in sources.lower():
									title = ('EZTOR ( Torrent ) | 4K | %s' % filmname)
									quality = '5'
								else:
									title = ('EZTOR ( Torrent ) | Unkown | %s' % filmname)
									quality = '8'
								self.links.append({'title': title, 'url': sources, 'quality': quality})
					return self.links
				else: pass
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)

