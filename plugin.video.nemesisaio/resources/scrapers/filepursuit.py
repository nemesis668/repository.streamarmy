import requests
import re
#import cfscrape
import xbmc
import xbmcgui
import time
dialog = xbmcgui.Dialog()
#scraper = cfscrape.CloudflareScraper()
ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
class Scraper:
	def __init__(self):
		self.Base = 'https://filepursuit.com'
		self.Search = ('/pursuit?q=%s&type=video')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term:
			Term = Term.replace('TV|||','')
			Term = Term.split('|||')[0]
			Term = Term.replace(' ','+',1)
			Term = Term.replace(' ','',)
			link = requests.get(self.Base+self.Search % Term, headers={"User-Agent":ua}).content
			possiblelink = re.findall('''<td>.*?a\s+href=['"](/file.*?)['"]''',link,flags=re.DOTALL)
			for links in possiblelink:
				if 'trailer' in links.lower(): continue
				if not self.Base in links: links = self.Base + links
				if '720' in links:
					title = 'File Pursuit | HD'
					sort = '2'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				elif '1080' in links:
					title = 'File Pursuit | HD 1080'
					sort = '1'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				elif 'UHD' in links:
					title = 'File Pursuit | 4K'
					if '4k' in links.lower(): sort = '0'
					elif 'uhd' in links.lower(): sort = '0'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				else: continue 
			return self.links
		else:
			Term = Term.replace('|||',' ')
			titles = []
			linksfound = []
			combined = []
			Term = Term.replace(' ','+').replace(':','')
			link = requests.get(self.Base+self.Search % Term, headers={"User-Agent":ua}).content
			possiblelink = re.findall('''<td>.*?a\s+href=['"](/file.*?)['"]''',link,flags=re.DOTALL)
			for links in possiblelink:
				if 'trailer' in links.lower(): continue
				if not self.Base in links: links = self.Base + links
				if '720' in links:
					title = 'File Pursuit | HD'
					sort = '2'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				elif '1080' in links:
					title = 'File Pursuit | HD 1080'
					sort = '1'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				elif 'UHD' in links:
					title = 'File Pursuit | 4K'
					if '4k' in links.lower(): sort = '0'
					elif 'uhd' in links.lower(): sort = '0'
					self.links.append({'title': title, 'url': links , 'quality' : sort})
				else: continue 
			return self.links

