import requests
import re
import xbmc
import xbmcgui
import time
import resolveurl
#from resources.libs.modules import cfscrape
from random import randint
dialog = xbmcgui.Dialog()
#scraper = cfscrape.CloudflareScraper()
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
class Scraper:
	def __init__(self):
		self.Base = 'https://projectfreetv.xyz/serie/%s'
		self.Search = ('%s')
		self.links = []

	def main(self, Term):
		if 'TV|||' in Term:
			Term = Term.replace('TV|||','')
			Term = Term.split('|||')[0]
			split = re.findall('(S[0-9].*?E[0-9].)',Term)[0].replace('S','season-').replace('E','/episode-')
			episodefix = re.findall(r'\d+',split)
			for numbers in episodefix:
				if numbers.startswith(str('0')): numbers2 = numbers.replace('0','') ; split = split.replace(numbers,numbers2)
			showname = Term.rsplit('S',1)[0]
			showname = showname.strip().replace(' ','-')
			link = requests.get(self.Base %showname).content
			soup = BeautifulSoup(link, 'html5lib')
			movie_containers = soup.findAll(class_='video_title')
			searchterm = split
			for links in movie_containers:
				url = links.a['href']
				if not 'https' in url: url = 'https:'+url
				if searchterm in url:
					link2 = requests.get(url, headers=headers).text
					soup = BeautifulSoup(link2, 'html5lib')
					movie_containers = soup.findAll(class_='tblimg')
					for info in movie_containers:
						url = info['href']
						title = 'Project Free Tv | HD'
						hmf = resolveurl.HostedMediaFile(url)
						if hmf.valid_url():
							self.links.append({'title': title, 'url': url, 'quality' : '2'})
					return self.links
		
		
		
		else: return False
		#time.sleep(randint(1,10))
		# Term = Term.split('|||')[0]
		# Term = Term.replace(' ','-').replace(':','')
		# link = scraper.get(self.Base+self.Search %Term).content
		# try: quality = re.findall('<strong>Quality:</strong>(.*?)<',link,flags=re.DOTALL)[0].strip()
		# except IndexError: quality = 'Unkown'
		# pattern = r'''<iframe.+?src=['"](.*?)['"]'''
		# sources = re.findall(pattern,link,flags=re.DOTALL)
		# if not sources:
			# return False
		# for source in sources:
			# title = 'SeeHD | ' + quality
			# if 'bluray' in quality.lower(): sort = '1'
			# elif 'high' in quality.lower(): sort = '2'
			# else : sort = '3'
			# self.links.append({'title': title, 'url': source, 'quality' : sort})
		# return self.links
