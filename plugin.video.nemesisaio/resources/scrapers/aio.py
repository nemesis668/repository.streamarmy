import requests
import re
import xbmc
import xbmcgui
import time
from random import randint
dialog = xbmcgui.Dialog()
ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
class Scraper:
	def __init__(self):
		self.Base = 'https://pastebin.com/raw/y8nYuUPP'
		self.Search = ('/%s-watch-online/')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term: return False
		Term = Term.split('|||')[0]
		link = requests.get(self.Base, headers={"User-Agent":ua}).content
		matches = re.findall('<list>(.*?)</list>',link,flags=re.DOTALL)
		for content in matches:
			if '<movies>' in content:
				checkurl = re.findall('<movies>(.*?)</movies>',content,flags=re.DOTALL)
				for links in checkurl:
					searchcontent = requests.get(links).content
					lists = re.findall('<content>(.*?)</content>',searchcontent,flags=re.DOTALL)
					for expand in lists:
						if Term in expand:
							title = re.findall('<title>(.*?)</title>',expand,flags=re.DOTALL)[0]
							link = re.findall('<link>(.*?)</link>',expand,flags=re.DOTALL)
							if link > 1 :
								for links in link:
									if 'trailer' in links.lower(): continue
									if 'uhd' in title.lower():
										title = 'NemesisAio Content | 4K | ' + title
										quality = '0'
									elif '4k' in title.lower():
										title = 'NemesisAio Content | 4K | ' + title
										quality = '0'
									elif '1080' in title.lower():
										title = 'NemesisAio Content | 1080 | ' + title
										quality = '1'
									elif '720' in title.lower():
										title = 'NemesisAio Content | HD | ' + title
										quality = '2'
									else:
										title = 'NemesisAio Content | SD | ' + title
										quality = '3'
									self.links.append({'title': title, 'url': links , 'quality' : quality})
							else:
								if 'trailer' in link.lower(): continue
								if 'uhd' in title.lower():
									title = 'NemesisAio Content | 4K | ' + title
									quality = '0'
								elif '4k' in title.lower():
									title = 'NemesisAio Content | 4K | ' + title
									quality = '0'
								elif '1080' in title.lower():
									title = 'NemesisAio Content | 1080 | ' + title
									quality = '1'
								elif '720' in title.lower():
									title = 'NemesisAio Content | HD | ' + title
									quality = '2'
								else:
									title = 'NemesisAio Content | SD | ' + title
									quality = '3'
								self.links.append({'title': title, 'url': links , 'quality' : quality})
		return self.links
