import requests
import re
from cfscrape import *
import xbmcgui
dialog = xbmcgui.Dialog()
finder = cfscrape.CloudflareScraper()

ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('PIRATEIO')
class Scraper:
	def __init__(self):
		self.Base = 'http://pirateiro.com/torrents/'
		self.Search = ('?search=%s')
		self.links = []

	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			if torrents == 'Allowed':
				try:
					found = 0
					Checker = term.replace(':','')
					term = term.replace(' ','+')
					cj = cfscrape.get_cookie_string('http://pirateiro.com/')
					headers = {'User-Agent' : cj[1],
								'Referer' : 'http://pirateiro.com/',
								'Cookie' : cj[0]}
					link = finder.get(self.Base+self.Search %term , headers=headers,timeout=10).content
					pattern = r'''<td\s+align=left.*?<b>(.*?)</b>.*?href=['"](magnet:?.*?)&'''
					findlinks = re.findall(pattern,link,flags=re.DOTALL)
					for title,magnet in findlinks:
						title = title.replace('.',' ')
						if Checker.lower() in title.lower() and year in title:
							found += 1
							if '480' in title:
								title = ('PIRATE ( Torrent ) | SD | %s' % title)
								quality = '8'
							elif '720' in title:
								title = ('PIRATE ( Torrent ) | HD | %s' % title)
								quality = '7'
							elif '1080' in title:
								title = ('PIRATE ( Torrent ) | FHD | %s' % title)
								quality = '6'
							elif '2160' in title:
								title = ('PIRATE ( Torrent ) | UHD ( 4K ) | %s' % title)
								quality = '5'
							else:
								title = ('PIRATE | SD | %s' %title )
								quality = '8'
							self.links.append({'title': title, 'url': magnet, 'quality': quality})
					return self.links
				except Exception as c:
					xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
			else: pass
		else: pass