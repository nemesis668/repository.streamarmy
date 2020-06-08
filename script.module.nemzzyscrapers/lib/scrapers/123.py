import re, requests, json
import xbmcgui
import xbmc
import random
dialog = xbmcgui.Dialog()
import xbmcaddon
import resolveurl
from bs4 import BeautifulSoup

class JsUnpackerV2:
	def unpackAll(self, data):
		try:
			in_data=data
			sPattern = '(eval\\(function\\(p,a,c,k,e,.*)'
			enc_data=re.compile(sPattern).findall(in_data)

			for enc_val in enc_data:
				try:
					unpack_val=self.unpack(enc_val)
					in_data=in_data.replace(enc_val,unpack_val)
				except:
					pass
			return in_data
		except: 
			traceback.print_exc(file=sys.stdout)
			return data
		
		
	def containsPacked(self, data):
		return ('String.fromCharCode(c+29)' in data and 'p,a,c,k' in data)
		
	def unpack(self, sJavascript,iteration=1, totaliterations=1):

		aSplit = sJavascript.split("rn p}('")

		p1,a1,c1,k1=('','0','0','')
		ss="p1,a1,c1,k1=(\'"+aSplit[1].split(".spli")[0]+')' 
		exec(ss)
		
		k1=k1.split('|')
		aSplit = aSplit[1].split("))'")
		e = ''
		d = ''#32823
		sUnpacked1 = str(self.__unpack(p1, a1, c1, k1, e, d,iteration))
		if iteration>=totaliterations:
			return sUnpacked1
		else:
			return self.unpack(sUnpacked1,iteration+1)

	def __unpack(self,p, a, c, k, e, d, iteration,v=1):
		while (c >= 1):
			c = c -1
			if (k[c]):
				aa=str(self.__itoaNew(c, a))
				p=re.sub('\\b' + aa +'\\b', k[c], p)# THIS IS Bloody slow!
		return p

	def __itoa(self,num, radix):

		result = ""
		if num==0: return '0'
		while num > 0:
			result = "0123456789abcdefghijklmnopqrstuvwxyz"[num % radix] + result
			num /= radix
		return result
	
	def __itoaNew(self,cc, a):
		aa="" if cc < a else self.__itoaNew(int(cc / a),a) 
		cc = (cc % a)
		bb=chr(cc + 29) if cc> 35 else str(self.__itoa(cc,36))
		return aa+bb


class Scraper:
	def __init__(self):
		self.MovieBase = 'https://123files.club/imdb/play/?id=%s'
		self.TvBase = 'https://123files.club/imdb/tv/?id=%s&s=%s&e=%s'
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if type == 'MOVIE':
			try:
				MovieTitle = term
				jsU2 = JsUnpackerV2()
				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
							'Referer' : 'https://123files.club/imdb/play/?id=%s' %imdb}
				data = {'SubmitButtoncolors' : '414TMA98eLEIqQQwNW29iamVjdCBNb3VzZUV2ZW50XSoyNDQqMTEzscBE1zlFrt109',
						'referer' : '123files.club'}
				Base = 'https://123files.club'
				content = requests.post(self.MovieBase % imdb,data=data,headers=headers).text
				soup = BeautifulSoup(content,'html.parser')
				r = soup.find_all('div', class_={'source'})
				for i in r:
					source = i['data-id']
					if not Base in source: source=Base+source
					headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
							'Referer' : source}
					data = requests.get(source,headers=headers).text    
					i = 0
					try:
						while jsU2.containsPacked(data):
							data = jsU2.unpackAll(data)
							i += 1
							if i == 3: raise Exception() 
					except: pass
					try:
						source = re.findall(r'''file:['"](http.*?)['"]''',data,flags=re.DOTALL)[0].replace('\\','')
						source = ('%s|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' % source)
						title = ('123 | FHD | DIRECT | %s' % MovieTitle)
						sort = '2'
						self.links.append({'title': title, 'url': source, 'quality': sort, 'Debrid' : False, 'Direct' : True})
					except:
						try:
							IframeHunt = re.findall(r'''<iframe.*?src=['"](.*?)['"]''',data,flags=re.DOTALL)[0]
							IframeHunt = 'https:%s'%IframeHunt if IframeHunt.startswith('//dood') else IframeHunt
							if IframeHunt.startswith('/play') : continue
							hmf = resolveurl.HostedMediaFile(IframeHunt)
							if hmf.valid_url():
								sort = '6'
								title = ('[COLOR white]123 ( Resolve Url ) | FHD | %s[/COLOR]' % MovieTitle)
								self.links.append({'title': title, 'url': IframeHunt, 'quality': sort, 'Debrid' : False, 'Direct' : False})
						except: pass
				return self.links
			except Exception as c:
				xbmc.log("SCRAPER ERROR 123  ::: %s" %c , level=xbmc.LOGNOTICE)
		else:
			try:
				season = re.findall(r'''(s\d+)''',term.lower(),flags=re.I)[0].replace('s0','').replace('e0','').replace('s','')
				episode = re.findall(r'''(e\d+)''',term.lower(),flags=re.I)[0].replace('e0','').replace('e0','').replace('e','')
				MovieTitle = term
				jsU2 = JsUnpackerV2()
				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
							'Referer' : 'https://123files.club/imdb/play/?id=%s' %imdb}
				data = {'SubmitButtoncolors' : '414TMA98eLEIqQQwNW29iamVjdCBNb3VzZUV2ZW50XSoyNDQqMTEzscBE1zlFrt109',
						'referer' : '123files.club'}
				Base = 'https://123files.club'
				xbmc.log("URL TO CHECK  ::: %s" %self.TvBase % (imdb,season,episode) , level=xbmc.LOGNOTICE)
				content = requests.post(self.TvBase % (imdb,season,episode),data=data,headers=headers).text
				soup = BeautifulSoup(content,'html.parser')
				r = soup.find_all('div', class_={'source'})
				for i in r:
					source = i['data-id']
					if not Base in source: source=Base+source
					headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
							'Referer' : source}
					data = requests.get(source,headers=headers).text    
					i = 0
					try:
						while jsU2.containsPacked(data):
							data = jsU2.unpackAll(data)
							i += 1
							if i == 3: raise Exception() 
					except: pass
					try:
						source = re.findall(r'''file:['"](http.*?)['"]''',data,flags=re.DOTALL)[0].replace('\\','')
						source = ('%s|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' % source)
						title = ('123 | FHD | DIRECT | %s' % MovieTitle)
						sort = '2'
						self.links.append({'title': title, 'url': source, 'quality': sort, 'Debrid' : False, 'Direct' : True})
					except:
						try:
							IframeHunt = re.findall(r'''<iframe.*?src=['"](.*?)['"]''',data,flags=re.DOTALL)[0]
							IframeHunt = 'https:%s'%IframeHunt if IframeHunt.startswith('//dood') else IframeHunt
							if IframeHunt.startswith('/play') : continue
							hmf = resolveurl.HostedMediaFile(IframeHunt)
							if hmf.valid_url():
								sort = '6'
								title = ('[COLOR white]123 ( Resolve Url ) | FHD | %s[/COLOR]' % MovieTitle)
								self.links.append({'title': title, 'url': IframeHunt, 'quality': sort, 'Debrid' : False, 'Direct' : False})
						except: pass
				return self.links
			except Exception as c:
				xbmc.log("SCRAPER ERROR 123  ::: %s" %c , level=xbmc.LOGNOTICE)