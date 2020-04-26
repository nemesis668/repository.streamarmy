import re, requests
from bs4 import BeautifulSoup
import xbmcgui
import xbmc
import cfscrape
scraper = cfscrape.create_scraper()
dialog = xbmcgui.Dialog()
Headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' }


class Scraper:
	def __init__(self):
		self.Base = 'https://openloadmovies.bz/'
		self.Search = ('?s=%s')
		self.links = []
		self.posturl = 'https://openloadmovies.bz/wp-admin/admin-ajax.php'
	def Index(self,type,term,year,imdb,torrents):
		if type == 'MOVIE':
			try:
				filmname = ('%s %s' % (term.title(), year))
				link = scraper.get(self.Base + self.Search % term.replace(' ','%20'), headers=Headers).content
				soup = BeautifulSoup(link, 'html5lib')
				content = soup.find_all('div', class_={'result-item'})
				CheckTerm = term.replace(' ','-')
				for items in content:
					url = items.a['href']
					if CheckTerm.lower() in url.lower() and year in url.lower():
						link = scraper.get(url,headers=Headers).content
						soup = BeautifulSoup(link, 'html5lib')
						movieid = soup.find('li', attrs={'data-post' : True})
						movieid = movieid['data-post']
						newheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
						'Referer': url, 'X-Requested-With': 'XMLHttpRequest',
						'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
						data = {'action' : 'doo_player_ajax',
						'post' : movieid,
						'nume' : '1',
						'type' : 'movie'}
						link = scraper.post(self.posturl,headers=newheaders, data=data).content
						xbmc.log("OUTPUT ::: %s" %link , level=xbmc.LOGNOTICE)
						pattern = r'''file.*?:['"]([^'"]+)['"].*?['"]label['"].*?['"](.*?)['"]'''
						sources = re.findall(pattern,link,flags=re.DOTALL)
						for source,qual in sources:
							if '360' in qual:
								title2 = ('OPENLOADMOVIES | SD | DIRECT | %s' % filmname)
								quality = '4'
							elif '480' in qual:
								title2 = ('OPENLOADMOVIES | SD | DIRECT | %s' % filmname)
								quality = '4'
							elif '720' in qual:
								title2 = ('OPENLOADMOVIES | HD | DIRECT | %s' % filmname)
								quality = '3'
							elif 'hls' in qual:
								title2 = ('OPENLOADMOVIES | HD | DIRECT | %s' % filmname)
								quality = '3'
							elif '1080' in qual:
								title2 = ('OPENLOADMOVIES | FHD | DIRECT | %s' % filmname)
								quality = '2'
							else:
								title2 = ('OPENLOADMOVIES | Unkown | DIRECT | %s' % filmname)
								quality = '6'
							self.links.append({'title': title2, 'url': source, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else:
			filmname = ('%s Season %s Episode %s ' % (term.title(), year, imdb ))
			Season = year
			Episode = imdb
			Season = int(Season)
			Episode = int(Episode)
			CleanTerm = term.lower().replace(' ','-')
			url = ('https://openloadmovies.bz/episodes/%s-%sx%s/' % (CleanTerm,Season,Episode))
			link = scraper.get(url,headers=Headers).content
			soup = BeautifulSoup(link, 'html5lib')
			movieid = soup.find('li', attrs={'data-post' : True})
			movieid = movieid['data-post']
			newheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
			'Referer': url, 'X-Requested-With': 'XMLHttpRequest',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			data = {'action' : 'doo_player_ajax',
			'post' : movieid,
			'nume' : '1',
			'type' : 'movie'}
			link = scraper.post(self.posturl,headers=newheaders, data=data).content
			pattern = r'''file.*?:['"]([^'"]+)['"].*?['"]label['"].*?['"](.*?)['"]'''
			sources = re.findall(pattern,link,flags=re.DOTALL)
			for source,qual in sources:
				if '360' in qual:
					title2 = ('OPENLOADMOVIES | SD | DIRECT | %s' % filmname)
					quality = '4'
				elif '480' in qual:
					title2 = ('OPENLOADMOVIES | SD | DIRECT | %s' % filmname)
					quality = '4'
				elif '720' in qual:
					title2 = ('OPENLOADMOVIES | HD | DIRECT | %s' % filmname)
					quality = '3'
				elif 'hls' in qual:
					title2 = ('OPENLOADMOVIES | HD | DIRECT | %s' % filmname)
					quality = '3'
				elif '1080' in qual:
					title2 = ('OPENLOADMOVIES | FHD | DIRECT | %s' % filmname)
					quality = '2'
				else:
					title2 = ('OPENLOADMOVIES | Unkown | DIRECT | %s' % filmname)
					quality = '6'
				self.links.append({'title': title2, 'url': source, 'quality': quality})
			return self.links

