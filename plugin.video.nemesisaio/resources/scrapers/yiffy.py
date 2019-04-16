import requests
import re
import xbmc
import xbmcgui
import time
from resources.libs.modules import cfscrape
from random import randint
dialog = xbmcgui.Dialog()
ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
class Scraper:
	def __init__(self):
		self.Base = 'https://ytss.unblocked.is/api/v2/list_movies.json?query_term=%s'
		self.Search = ('?query_term=%s')
		self.links = []

	def main(self, Term):
		#time.sleep(randint(1,10))
		Term = Term.split('|||')[0]
		Checker = Term
		Term = Term.replace(' ','%20').replace(':','')
		link = requests.get(self.Base %Term ,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}).json()
		for i in link['data']['movies']:
			title = i['title']
			if title.lower() == Checker.lower():
				pattern = r''''hash'.+?['"](.*?)['"].+?quality.+?['"](.*?)['"]'''
				findsource = re.findall(pattern,str(i),flags=re.DOTALL)
				for hashs,quality in findsource:
					if '4k' in quality.lower(): sort = '0'
					elif 'UHD' in quality.lower(): sort = '0'
					elif '1080' in quality.lower(): sort = '1'
					elif '3d' in quality.lower(): sort = '1'
					elif '720' in quality.lower(): sort = '2'
					else : sort = '3'
					finallink = ('magnet:?xt=urn:btih:%s' %hashs)
					title = 'Yiffy ( TORRENTS ) | ' + quality
					self.links.append({'title': title, 'url': finallink , 'quality' : sort})
		return self.links
