import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
import resolveurl
import xbmcaddon
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('WATCHSERIES')
class Scraper:
	def __init__(self):
		self.Base = 'https://watchserieshd.cc/'
		self.Search = ('search.html?keyword=%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			pass
		else:
			try:
				MainSite = 'https://watchserieshd.cc'
				filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
				cleanterm = term.replace(' ','%20')
				Season = year
				Episode = imdb
				Season = int(Season)
				Episode = int(Episode)
				link = requests.get(self.Base+self.Search % cleanterm, headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				data = soup.find_all('div' , class_={'video_image_container sdimg'})
				check = ('season %s' % Season)
				check2 = ('Episode %s' % Episode)
				for items in data:
					titles = items.a['title']
					if term.lower() and check in titles.lower():
						url = items.a['href']
						if not MainSite in url: url = MainSite+url
						link = requests.get(url+'/season',headers=Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						data = soup.find_all('div' , class_={'vid_info'})
						for content in data:
							titles = content.a['title']
							if check2 in titles:
								url = content.a['href']
								if not MainSite in url: url = MainSite+url
								link = requests.get(url,headers=Headers).content
								pattern = r'''data-video=['"]([^'"]+)'''
								getsources = re.findall(pattern,link,flags=re.DOTALL)
								for source in getsources:
									if 'streaming.php' in source:
										if not 'https' in source: source = 'https:'+source
										link = requests.get(source,headers=Headers).content
										Patternz = [r'''file:\s+['"](.*?)['"].*?label:\s+['"](.*?)['"]''',
													r'''['"]([^'"]+m3u8.*?).*?:.*?['"](.*?)['"]''']
										for Pattern in Patternz:
											GetSources = re.findall(Pattern,link,flags=re.DOTALL)
											for url,quality in GetSources:
												if 'redirector' in url and 'Auto' not in quality:
													if '360' in quality:
														title = ('WATCHSERIESHD | SD | DIRECT | %s' % filmname)
														quality = '4'
													elif '480' in quality:
														title = ('WATCHSERIESHD | SD | DIRECT | %s' % filmname)
														quality = '4'
													elif '720' in quality:
														title = ('WATCHSERIESHD | HD | DIRECT | %s' % filmname)
														quality = '3'
													elif 'hls' in quality.lower():
														title = ('WATCHSERIESHD | HD | DIRECT | %s' % filmname)
														quality = '3'
													elif '1080' in quality:
														title = ('WATCHSERIESHD | FHD | DIRECT | %s' % filmname)
														quality = '2'
													else:
														title = ('WATCHSERIESHD | Unkown | DIRECT | %s' % filmname)
														quality = '4'
													self.links.append({'title': title, 'url': url, 'quality': quality})
												elif 'm3u8' in url and 'Auto' not in quality:
													if '360' in quality:
														title = ('WATCHSERIESHD | SD | DIRECT | %s' % filmname)
														quality = '4'
													elif '480' in quality:
														title = ('WATCHSERIESHD | SD | DIRECT | %s' % filmname)
														quality = '4'
													elif '720' in quality:
														title = ('WATCHSERIESHD | HD | DIRECT | %s' % filmname)
														quality = '3'
													elif 'hls' in quality.lower():
														title = ('WATCHSERIESHD | HD | DIRECT | %s' % filmname)
														quality = '3'
													elif '1080' in quality:
														title = ('WATCHSERIESHD | FHD | DIRECT | %s' % filmname)
														quality = '2'
													else:
														title = ('WATCHSERIESHD | Unkown | DIRECT | %s' % filmname)
														quality = '4'
													url = ('%s|Referer=%s' % (url,source))
													self.links.append({'title': title, 'url': url, 'quality': quality})
									else:
										if resolveurl.HostedMediaFile(source).valid_url():
											title = ('WATCHSERIESHD | HD | RESOLVEURL | %s' % filmname)
											quality = '3'
											self.links.append({'title': title, 'url': source, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)

