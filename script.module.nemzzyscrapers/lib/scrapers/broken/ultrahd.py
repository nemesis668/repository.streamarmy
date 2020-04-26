import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
GoodFiles = ['.mp4', '.mkv']
import xbmcaddon
#_addon_id_ = 'plugin.video.Flex'
#_self_ = xbmcaddon.Addon(id=_addon_id_)
#Enabled = _self_.getSetting('ULTRAHD')
class Scraper:
	def __init__(self):
		self.Base = 'http://ultrahdindir.com/'
		self.Search = ('%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		pass
		#dialog.ok("TERM HD",str(term))
		# if Enabled == 'false': return False
		# if type == 'MOVIE':
			# try:
				# filmname = term.title()
				# found = 0
				# titles =[]
				# post_data = {'do': 'search',
				# 'subaction': 'search',
				# 'story' : imdb}
				# link = requests.post(self.Base, data=post_data, headers=Headers).content
				# match = re.findall('<div class="news-text">(.*?)</div>',link,flags=re.DOTALL)[0]
				# link2 = re.findall('<a href="(.*?)"',match,flags=re.DOTALL)[0]
				# link = requests.get(link2,headers=Headers).content
				# data = re.findall('</iframe>(.+?)QuoteEEnd--><br /><br', link, re.DOTALL)[0]
				# titles += re.findall('''start--><b>(.+?)</b>.+?<b><a href=['"](.+?)['"]''', data, re.DOTALL)
				# for qual,url in titles:
					# if '360' in qual:
						# title = ('ULTRAHD ( RD ) | SD | %s' % filmname)
						# quality = '8'
					# elif '480' in qual:
						# title = ('ULTRAHD ( RD ) | SD | %s' % filmname)
						# quality = '8'
					# elif '720' in qual:
						# title = ('ULTRAHD ( RD ) | HD | %s' % filmname)
						# quality = '7'
					# elif '1080' in qual:
						# title = ('ULTRAHD ( RD ) | FHD | %s' % filmname)
						# quality = '6'
					# elif '4k' in qual.lower():
						# title = ('ULTRAHD ( RD ) | UHD | %s' % filmname)
						# quality = '5'
					# elif 'uhd' in qual.lower():
						# title = ('ULTRAHD ( RD ) | UHD | %s' % filmname)
						# quality = '5'
					# elif '3d' in qual.lower():
						# title = ('ULTRAHD ( RD ) | 3D | %s' % filmname)
						# quality = '5'
					# elif 'blueray' in qual.lower():
						# title = ('ULTRAHD ( RD ) | FHD | %s' % filmname)
						# quality = '6'
					# else:
						# title = ('ULTRAHD ( RD )| Unkown | %s' % filmname)
						# quality = '8'
					# self.links.append({'title': title, 'url': url, 'quality': quality})
				# return self.links
			# except Exception as c:
				# xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		# else: pass

