import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('GOWATCH')
class Scraper:
	def __init__(self):
		self.Base = 'https://www5.gowatchseries.video/'
		self.Search = ('search.html?keyword=%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			try:
				filmname = term.title()
				found = 0
				cleanterm = term.replace(' ','%20')
				link = requests.get(self.Base+self.Search %cleanterm , headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				content = soup.find('ul', class_={'listing items'})
				for matches in content.find_all('li'):
					link = matches.a['href']
					MovieTitle = matches.find('div', class_={'name'}).text
					if term.lower() in MovieTitle.lower():
						if not self.Base in link: link = self.Base+link
						link = requests.get(link , headers=Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						content = soup.find('div', class_={'watch infonation'})
						YearCheck = re.findall('<li><span>Release:\s+</span>(.*?)</li>',str(content),flags=re.DOTALL)[0]
						if YearCheck == year:
							link = content.a['href']
							if not self.Base in link: link = self.Base+link
							link = requests.get(link , headers=Headers).content
							soup = BeautifulSoup(link, 'html5lib')
							Playerframe = re.findall('''<iframe src=['"](.*?)['"]''',link,flags=re.DOTALL)[0]
							if not 'https' in Playerframe: Playerframe = ('https:%s' % Playerframe)
							link = requests.get(Playerframe , headers=Headers).content
							Pattern = r'''file:\s+['"](.*?)['"].*?label:\s+['"](.*?)['"]'''
							GetSources = re.findall(Pattern,link,flags=re.DOTALL)
							for url,quality in GetSources:
								if 'redirector' in url and 'Auto' not in quality:
									found += 1
									if '360' in quality:
										title = ('GOWATCH | SD | DIRECT | %s' % filmname)
										quality = '4'
									elif '480' in quality:
										title = ('GOWATCH | SD | DIRECT | %s' % filmname)
										quality = '4'
									elif '720' in quality:
										title = ('GOWATCH | HD | DIRECT | %s' % filmname)
										quality = '3'
									elif 'hls' in quality.lower():
										title = ('GOWATCH | HD | DIRECT | %s' % filmname)
										quality = '3'
									elif '1080' in quality:
										title = ('GOWATCH | FHD | DIRECT | %s' % filmname)
										quality = '2'
									else:
										title = ('GOWATCH | Unkown | DIRECT | %s' % filmname)
										quality = '4'
									self.links.append({'title': title, 'url': url, 'quality': quality})
								elif 'm3u8' in url and 'Auto' not in quality:
									found += 1
									if '360' in quality:
										title = ('GOWATCH | SD | DIRECT | %s' % filmname)
										quality = '0'
									elif '480' in quality:
										title = ('GOWATCH | SD | DIRECT | %s' % filmname)
										quality = '0'
									elif '720' in quality:
										title = ('GOWATCH | HD | DIRECT | %s' % filmname)
										quality = '3'
									elif 'hls' in quality.lower():
										title = ('GOWATCH | HD | DIRECT | %s' % filmname)
										quality = '3'
									elif '1080' in quality:
										title = ('GOWATCH | FHD | DIRECT | %s' % filmname)
										quality = '2'
									else:
										title = ('GOWATCH | Unkown | DIRECT | %s' % filmname)
										quality = '6'
									url = ('%s|Referer=%s' % (url,Playerframe))
									self.links.append({'title': title, 'url': url, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else:
			try:
				filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
				Season = year
				Episode = imdb
				Season = int(Season)
				Episode = int(Episode)
				cleanterm = term.replace(' ','%20')
				link = requests.get(self.Base+self.Search % cleanterm, headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				content = soup.find('ul', class_={'listing items'})
				for matches in content.find_all('li'):
					link = matches.a['href']
					check1 = ('Season-%s' % Season)
					check2 = ('Episode-%s' % Episode)
					if check1.lower() in link.lower():
						if not self.Base in link: link = self.Base+link
						link = requests.get(link, headers=Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						content = soup.find_all('li', class_={'child_episode'})
						for links in content:
							epilinks = links.a['href']
							if check2.lower() in epilinks:
								if not self.Base in epilinks: epilinks = self.Base+epilinks
								link = requests.get(epilinks , headers=Headers).content
								soup = BeautifulSoup(link, 'html5lib')
								Playerframe = re.findall('''<iframe src=['"](.*?)['"]''',link,flags=re.DOTALL)[0]
								if not 'https' in Playerframe: Playerframe = ('https:%s' % Playerframe)
								link = requests.get(Playerframe , headers=Headers).content
								Patternz = [r'''file:\s+['"](.*?)['"].*?label:\s+['"](.*?)['"]''',
												r'''['"]([^'"]+m3u8.*?).*?:.*?['"](.*?)['"]''']
								for Pattern in Patternz:
									GetSources = re.findall(Pattern,link,flags=re.DOTALL)
									for url,quality in GetSources:
										if 'redirector' in url and 'Auto' not in quality:
											if '360' in quality:
												title = ('GOWATCH | SD | DIRECT | %s' % filmname)
												quality = '4'
											elif '480' in quality:
												title = ('GOWATCH | SD | DIRECT | %s' % filmname)
												quality = '4'
											elif '720' in quality:
												title = ('GOWATCH | HD | DIRECT | %s' % filmname)
												quality = '3'
											elif 'hls' in quality.lower():
												title = ('GOWATCH | HD | DIRECT | %s' % filmname)
												quality = '3'
											elif '1080' in quality:
												title = ('GOWATCH | FHD | DIRECT | %s' % filmname)
												quality = '2'
											else:
												title = ('GOWATCH | Unkown | DIRECT | %s' % filmname)
												quality = '6'
											self.links.append({'title': title, 'url': url, 'quality': quality})
										elif 'm3u8' in url and 'Auto' not in quality:
											if '360' in quality:
												title = ('GOWATCH | SD | DIRECT | %s' % filmname)
												quality = '4'
											elif '480' in quality:
												title = ('GOWATCH | SD | DIRECT | %s' % filmname)
												quality = '4'
											elif '720' in quality:
												title = ('GOWATCH | HD | DIRECT | %s' % filmname)
												quality = '3'
											elif 'hls' in quality.lower():
												title = ('GOWATCH | HD | DIRECT | %s' % filmname)
												quality = '3'
											elif '1080' in quality:
												title = ('GOWATCH | FHD | DIRECT | %s' % filmname)
												quality = '2'
											else:
												title = ('GOWATCH | Unkown | DIRECT | %s' % filmname)
												quality = '6'
											url = ('%s|Referer=%s' % (url,Playerframe))
											self.links.append({'title': title, 'url': url, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)

