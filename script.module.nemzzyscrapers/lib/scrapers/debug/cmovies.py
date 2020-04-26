import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
import resolveurl
import xbmcaddon
from cloudscraper2 import CloudScraper
CF = CloudScraper.create_scraper()
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }
GoodFiles = ['.mp4', '.mkv']


class Scraper:
	def __init__(self):
		self.Base = 'https://api.ocloud.stream/cmovieshd//movie/search/%s?link_web=https://www1.cmovieshd.bz/'
		self.Search = ('%s')
		self.links = []
		self.servermain = 'https://www2.cmovieshd.bz/'
	def Index(self,type,term,year,imdb,torrents):

		if type == 'MOVIE':
			try:
				filmname = ('%s %s' % (term.title(), year))
				term = term.replace(' ','-')
				link = requests.get(self.Base % term, headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				for links in content:
					if term.lower() in links['href']:
						Movietitle = links.img['alt']
						followlink = links['href'] + '/watching.html'
						link = CF.get(followlink, headers=Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						content = soup.find('div', class_={'pas-list'})
						for links in content.find_all('a', href=True):
							if self.servermain not in links['href']: links = self.servermain+links['href']
							link = CF.get(links, headers=Headers).content
							soup = BeautifulSoup(link, 'html5lib')
							content = soup.find('div', class_={'pa-main anime_muti_link'})
							for links in content.find_all('li'):
								sources = links['data-video']
								if not 'https' in sources: sources = ('https:%s' % sources)
								if not 'vidcloud.icu' in sources:
									if resolveurl.HostedMediaFile(sources).valid_url():
										title = ('CMOVIES | FHD | RESOLVEURL | %s' % Movietitle)
										quality = '6'
										self.links.append({'title': title, 'url': sources, 'quality': quality})
								else:
									pass

					return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else:
			pass
			# filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
			# term = term.replace(' ','-')
			# Season = year
			# Episode = imdb
			# Season = int(Season)
			# Episode = int(Episode)
			# check1 = ('Season-%s' % Season)
			# check2 = ('ep=%s' % Episode)
			# link = scraper.get(self.Base % term, headers=Headers).content
			# soup = BeautifulSoup(link, 'html5lib')
			# content = soup.find_all('a')
			# for links in content:
				# if check1.lower() in links['href']:
					# followlink = links['href'] + '/watching.html'
					# link = scraper.get(followlink, headers=Headers).content
					# soup = BeautifulSoup(link, 'html5lib')
					# content = soup.find('div', class_={'pas-list'})
					# for links in content.find_all('a', href=True):
						# if check2 in links['href']:
							# if self.servermain not in links['href']: links = self.servermain+links['href']
							# link = scraper.get(links, headers=Headers).content
							# soup = BeautifulSoup(link, 'html5lib')
							# content = soup.find('div', class_={'pa-main anime_muti_link'})
							# for links in content.find_all('li'):
								# sources = links['data-video']
								# if not 'https' in sources: sources = ('https:%s' % sources)
								# if not 'vidcloud.icu' in sources:
									# if resolveurl.HostedMediaFile(sources).valid_url():
										# title = ('CMOVIES | FHD | RESOLVEURL | %s' % filmname)
										# quality = '6'
										# self.links.append({'title': title, 'url': sources, 'quality': quality})
								# else:
									# link = scraper.get(sources, headers=Headers).content
									# Patternz = [r'''file:\s+['"](.*?)['"].*?label:\s+['"](.*?)['"]''',
												# r'''['"]([^'"]+m3u8.*?).*?:.*?['"](.*?)['"]''']
									# for Pattern in Patternz:
										# GetSources = re.findall(Pattern,link,flags=re.DOTALL)
										# for url,quality in GetSources:
											# if 'redirector' in url or '.m3u8' in url:
												# if 'm3u8' in url: url = ('%s|Referer=%s' % (url,sources))
												# if not 'auto' in quality.lower():
													# if '360' in quality:
														# title2 = ('CMOVIES | SD | DIRECT | %s' % filmname)
														# quality = '4'
													# elif '480' in quality:
														# title2 = ('CMOVIES | SD | DIRECT | %s' % filmname)
														# quality = '4'
													# elif '720' in quality:
														# title2 = ('CMOVIES | HD | DIRECT | %s' % filmname)
														# quality = '3'
													# elif 'hls' in quality:
														# title2 = ('CMOVIES | HD | DIRECT | %s' % filmname)
														# quality = '2'
													# elif '1080' in quality:
														# title2 = ('CMOVIES | FHD | DIRECT | %s' % filmname)
														# quality = '2'
													# else:
														# title2 = ('CMOVIES | Unkown | DIRECT | %s' % filmname)
														# quality = '4'
													# self.links.append({'title': title2, 'url': url, 'quality': quality})
			# return self.links

