import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('GRABTHEBEST')
class Scraper:
	def __init__(self):
		self.Base = 'https://grabthebeast.com/'
		self.Search = ('search/%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			pass
		else:
			try:
				filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
				Season = year
				Episode = imdb
				Season = int(Season)
				Episode = int(Episode)
				checkterm = term.replace(' ','-')
				term = term.replace(' ','%20')
				link = requests.get(self.Base+self.Search % term, headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				content = soup.find_all('div', class_={'tvsearch-result'})
				for links in content:
					if checkterm.lower() in links.a['href'].lower():
						showid = links.a['href'].rsplit('/',1)[1]
						constructurl = ('https://grabthebeast.com/stream/%s/season/%s/episode/%s' % (showid,Season,Episode))
						link = requests.get(constructurl, headers=Headers).content
						videos = re.findall(r'''<source src=['"](.*?)['"]''',link,flags=re.DOTALL)
						for vids in videos:
							if '360' in vids:
								title = ('GRABTHEBEST | SD | DIRECT | %s' % filmname)
								quality = '4'
							elif '480' in vids:
								title = ('GRABTHEBEST | SD | DIRECT | %s' % filmname)
								quality = '4'
							elif '720' in vids:
								title = ('GRABTHEBEST | HD | DIRECT | %s' % filmname)
								quality = '3'
							elif '1080' in vids:
								title = ('GRABTHEBEST | FHD | DIRECT | %s' % filmname)
								quality = '2'
							else:
								title = ('GRABTHEBEST | Unkown | DIRECT | %s' % filmname)
								quality = '4'
							self.links.append({'title': title, 'url': vids, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)

