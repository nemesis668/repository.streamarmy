import requests
import re
import xbmc
import xbmcgui
import time
from resources.libs.modules import cfscrape
from random import randint
dialog = xbmcgui.Dialog()
scraper = cfscrape.create_scraper()
class Scraper:
	def __init__(self):
		self.Base = 'http://pirateiro.com/torrents/'
		self.Search = ('?search=%s')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term:
			Term = Term.replace('TV|||','')
			Term = Term.split('|||')[0]
			Term = Term.replace(' ','+')
			Term = Term.replace(' ','',)
			cj = cfscrape.get_cookie_string('http://pirateiro.com/')
			headers = {'User-Agent' : cj[1],
						'Referer' : 'http://pirateiro.com/',
						'Cookie' : cj[0]}
			Term = Term.replace(' ','+')
			link = scraper.get(self.Base+self.Search %Term , headers=headers).content
			pattern = r'''<td\s+align=left.*?<b>(.*?)</b>.*?href=['"](magnet:?.*?)&'''
			findlinks = re.findall(pattern,link,flags=re.DOTALL)

			for title,magnet in findlinks:
				title = title.replace('.',' ')
				if 'uhd' in title.lower(): sort = '0' ; qual = '4K UHD'
				elif '2160' in title.lower(): sort = '0'; qual = '4K UHD'
				elif '1080' in title.lower(): sort = '1'; qual = '1080'
				elif '720' in title.lower(): sort = '2'; qual = '720'
				else : sort = '3'; qual = 'SD'
				title = 'Pirateiro ( Torrent ) | ' + qual + ' | ' + title
				self.links.append({'title': title, 'url': magnet, 'quality' : sort})
			return self.links
		else:
			cj = cfscrape.get_cookie_string('http://pirateiro.com/')
			headers = {'User-Agent' : cj[1],
						'Referer' : 'http://pirateiro.com/',
						'Cookie' : cj[0]}
			Year = Term.split('|||')[1]
			Year = Year.strip()
			Term = Term.split('|||')[0]
			CheckMe = Term
			Term = Term.replace(' ','+')
			link = scraper.get(self.Base+self.Search %Term , headers=headers).content
			pattern = r'''<td\s+align=left.*?<b>(.*?)</b>.*?href=['"](magnet:?.*?)&'''
			findlinks = re.findall(pattern,link,flags=re.DOTALL)
			for title,magnet in findlinks:
				title = title.replace('.',' ')
				if CheckMe.lower() in title.lower():
					if Year in title:
						if 'uhd' in title.lower(): sort = '0' ; qual = '4K UHD'
						elif '2160' in title.lower(): sort = '0'; qual = '4K UHD'
						elif '1080' in title.lower(): sort = '1'; qual = '1080'
						elif '720' in title.lower(): sort = '2'; qual = '720'
						else : sort = '3'; qual = 'SD'
						title = 'Pirateiro ( Torrent ) | ' + qual + ' | ' + title
						self.links.append({'title': title, 'url': magnet, 'quality' : sort})
			return self.links

