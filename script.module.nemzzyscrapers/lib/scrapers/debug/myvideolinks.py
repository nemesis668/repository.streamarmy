import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
import resolveurl
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
GoodFiles = ['.mp4', '.mkv']
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('MYVIDEOLINKS')
class Scraper:
	def __init__(self):
		self.Base = 'http://myvideolinks.69.mu/'
		self.Search = ('?s=%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			try:
				found = 0
				check = term
				cleanterm = term.replace(' ','+')
				link = requests.get(self.Base+self.Search %cleanterm , headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				data = soup.find_all('div', class_={'post-meta'})
				for content in data:
					imdbcheck = [tag['href'] for tag in content.select('p a[href*=imdb]')]
					for matches in imdbcheck:
						if imdb in matches:
							title = content.a['title']
							link = content.a['href']
							link = requests.get(link, headers=Headers).content
							soup = BeautifulSoup(link, 'html5lib')
							data = soup.find('div', class_={'post-content'})
							sources = data.find('ul')
							for source in sources.find_all('a'):
								source = source['href']
								found += 1
								if '480' in title:
									title2 = ('MYVIDEOLINKS ( RD ) | SD  | %s' % title)
									quality = '8'
								elif '720' in title:
									title2 = ('MYVIDEOLINKS ( RD ) | HD | %s' % title)
									quality = '7'
								elif '1080' in title:
									title2 = ('MYVIDEOLINKS ( RD ) | FHD  | %s' % title)
									quality = '6'
								elif '3D' in title:
									title2 = ('MYVIDEOLINKS ( RD ) | 3D  | %s' % title)
									quality = '6'
								else:
									title2 = ('MYVIDEOLINKS | Unkown  | %s' % title)
									quality = '8'
								hmf = resolveurl.HostedMediaFile(source)
								if hmf.valid_url():
									self.links.append({'title': title2, 'url': source, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else: pass

