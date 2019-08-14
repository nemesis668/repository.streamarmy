# -*- coding: utf-8 -*-

import re,json,urllib,urlparse,base64,unicodedata,os

import client
import cache
import workers
import jsunpack
import utils
import kodi
import xbmc
import log_utils
import xbmcgui
import resolveurl
import requests
import cfscrape
from bs4 import BeautifulSoup
dialog	= xbmcgui.Dialog()
scraper = cfscrape.create_scraper()
def CLEANUP(text):

    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />','\n')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&#39;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&#8211;',"&")
    text = text.replace('&#8217;',"'")
    text = text.replace('&#038;',"&")
    text = text.lstrip(' ')
    text = text.lstrip('	')

    return text
class streamer:

	def resolve(self, url, pattern=None):

		if pattern: 
			u = self.generic(url, pattern)
			
		else:
		
			if 'eporner.com' in url: u = self.eporner(url)
			
			elif 'girlfriendvideos.com' in url: u = self.girlfriendvideos(url)

			elif 'porn00' in url: u = self.porn00(url)
			
			elif 'justporno.tv' in url: u = self.justporno(url)

			elif '4tube.com' in url: u = self.fourtube(url)

			elif 'perfectgirls.net' in url: u = self.perfectgirls(url)

			elif 'pornhub.com' in url: u = self.pornhub(url)
			
			elif 'pornheel.com' in url: u = self.pornheel(url)
			
			elif 'pandamovie.info' in url: u = self.pandamovie(url)

			elif 'winporn.com' in url: u = self.winporn(url)

			elif 'yuvutu.com' in url: u = self.yuvutu(url)

			elif 'huge6.com' in url: u = self.hugesix(url)

			elif 'boobsandtits.co.uk' in url: u = self.boobntit(url)
			
			elif 'sexmax.co' in url: u = self.sexmax(url)
			elif 'adult-channels.com' in url: u = self.adultchannels(url)

			elif 'drtube' in url: u = self.drtube(url)
			
			elif 'nuvid' in url: u = self.nuvid(url)
			
			elif 'solopornoitaliani' in url: u = self.solopornoitaliani(url)
			
			elif 'spreadporn.org' in url: u = self.spreadporn(url)

			elif 'befuck.com' in url: u = self.befuck(url)
			
			elif 'megasesso' in url: u = self.megasesso(url)
			
			elif 'freeones' in url: u = self.freeones(url)
			
			elif 'fuqer.com' in url: u = self.fuqer(url)
			
			elif 'siska' in url: u = self.siska(url)
			
			elif 'satan18av' in url: u = self.satan18av(url)

			elif 'overthumbs' in url: u = self.overthumbs(url)

			elif 'streamate.com' in url: u = self.streamate(url)

			elif 'mixhdporn.com' in url: u = self.mixhd(url)      
			
			elif 'xtheatre.net' in url: u = self.xtheatre(url)                      
			
			elif 'youporn.com' in url: u = self.youporn(url)                      

			elif 'chaturbate.com' in url: u = self.chaturbate(url)                      

			elif 'nxgx.com' in url: u = self.nxgx(url)

			elif 'hqporner.com' in url: u = self.hqporner(url)

			#elif '3movs.com' in url: u = self.threemovs(url)
			
			elif 'hclips.com' in url: u = self.hclips(url)
			
			elif 'watchxxxfree.tv' in url: u = self.watchxxxfree(url)
			
			elif 'youngpornvideos.com' in url: u = self.youngpornvideos(url)
			
			elif 'javhihi.com' in url: u = self.javhihi(url)
			
			elif 'txxx.com' in url: u = self.txxx(url)
			
			elif 'vrsumo.com' in url: u = self.vrsumo(url)
			
			elif 'anysex.com' in url: u = self.anysex(url)
			
			elif '123pandamovie.me' in url: u = self.pandamovie(url)
			
			elif 'pornxs.com' in url: u = self.pornxs(url)
			
			elif 'http://streamingporn.xyz' in url: u = self.streamingporn(url)
			
			elif '3movs.com' in url: u = self.threemovs(url)
			
			elif 'watchmygf.me' in url: u = self.watchmygf(url)
			
			elif 'vrsmash.com' in url: u = self.vrsmash(url)
			
			elif 'spankbang.com' in url: u = self.spankbang(url)


			else: u = self.generic(url, pattern=None)

		return u

	def generic(self, url, pattern=None):

		try:
			r = client.request(url)
			if pattern: s=re.findall(r'%s' % pattern, r)
			else:
				patterns = [
							r'''\s*=\s*[\'\"](http.+?)[\'\"]''', \
							r'''\s*=\s*['"](http.+?)['"]''', \
							r'''['"][0-9_'"]+:\s[\'\"]([^'"]+)''', \
							r'''\(\w+\([\'\"]([^\'\"]*)''', \
							r'''[\'\"]\w+[\'\"]:['"]([^'"]*)''', \
							r'''\s*=\s*[\'\"](http.+?)[\'\"]''', \
							r'''\s*:\s*[\'\"](//.+?)[\'\"]''', \
							r'''\:[\'\"](\.+?)[\'\"]''', \
							r'''\s*\(\s*[\'\"](http.+?)[\'\"]''', \
							r'''\s*=\s*[\'\"](//.+?)[\'\"]''', \
							r'''\w*:\s*[\'\"](http.+?)[\'\"]''', \
							r'''\w*=[\'\"]([^\'\"]*)''', \
							r'''\w*\s*=\s*[\'\"]([^\'\"]*)''', \
							r'''(?s)<file>([^<]*)''', \
							]
				
				s = []
				for pattern in patterns: 
					l = re.findall(pattern, r)
					s += [i for i in l if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]

				if s: s = [i for i in s if (urlparse.urlparse(i).path).strip('/').split('/')[-1].split('.')[-1] in ['mp4', 'flv', 'm3u8']]
				else: s = client.parseDOM(r, 'source', ret='src', attrs = {'type': 'video.+?'})
				
				if not s: 
					log_utils.log('Error resolving %s :: Error: %s' % (url,str(e)), log_utils.LOGERROR)
					return
					
				s = ['http:' + i if i.startswith('//') else i for i in s]
				s = [urlparse.urljoin(url, i) if not i.startswith('http') else i for i in s]
				s = [x for y,x in enumerate(s) if x not in s[:y]]

			self.u = []
			def request(i):
				try:
					i = i.replace(' ','%20')
					c = client.request(i, output='headers', referer=url)
					checks = ['video','mpegurl','html']
					if any(f for f in checks if f in c['Content-Type']): self.u.append((i, int(c['Content-Length'])))
				except:
					pass
			threads = []
			for i in s: threads.append(workers.Thread(request, i))
			[i.start() for i in threads] ; [i.join() for i in threads]

			u = sorted(self.u, key=lambda x: x[1])[::-1]
			
			mobile_mode = kodi.get_setting('mobile_mode')
			if mobile_mode == 'true': u = client.request(u[-1][0], output='geturl', referer=url)
			else: u = client.request(u[0][0], output='geturl', referer=url)
			log_utils.log('Returning %s from XXX-O-DUS Resolver' % str(u), log_utils.LOGNOTICE)
			return u
		except Exception as e:
			log_utils.log('Error resolving %s :: Error: %s' % (url,str(e)), log_utils.LOGERROR)

	# needed to generate hash for eporner
	def encode_base_n(self, num, n, table=None):
		FULL_TABLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if not table:
			table = FULL_TABLE[:n]

		if n > len(table):
			raise ValueError('base %d exceeds table length %d' % (n, len(table)))

		if num == 0:
			return table[0]

		ret = ''
		while num:
			ret = table[num % n] + ret
			num = num // n
		return ret

	def girlfriendvideos(self, url):
		
		try:
			r = client.request(url)
			r = r.replace('\\','')
			pattern = r"""<video src="([^"]+)"""
			link = re.findall(pattern,r)[0]
			u = 'http://www.girlfriendvideos.com' + link
			return u
		except: return 

	def eporner(self, url):
		
		try:
			r = client.request(url)
			pattern = r"""{\s*vid:\s*'([^']+)',\s*hash\s*:\s*["\']([\da-f]{32})"""
			id,hash = re.findall(pattern,r)[0]
			hash_code = ''.join((self.encode_base_n(int(hash[lb:lb + 8], 16), 36) for lb in range(0, 32, 8)))
			load_url = 'https://www.eporner.com/xhr/video/%s?hash=%s&device=generic&domain=www.eporner.com&fallback=false&embed=false&supportedFormats=mp4' % (id,hash_code)
			r = client.request(load_url).replace("\/", "/")
			r = json.loads(r).get("sources", {}).get('mp4', {})
			r = [(i, r[i].get("src")) for i in r]
			u = sorted(r, key=lambda x: int(re.search('(\d+)', x[0]).group(1)), reverse=True)
			return u
		except: return 

	def watchxxxfree(self, url):
		
		try:
			r = client.request(url)
			pattern = r"""<iframe.+?src=['"]([^'"]+)"""
			e = re.findall(pattern,r)
			for links in e:
				return links
		except: return

	def porn00(self, url):
		
		try:
			r = client.request(url)
			pattern = r'''<ul>.+?iframe.+?\?v=([\d]+)'''
			id=re.findall(pattern,r,re.DOTALL)[0]
			url = 'http://www.porn00.org/plays/?v=%s' % id
			cookie = client.request(url, output='cookie')
			r = client.request(url, cookie=cookie)
			pattern = r'''(?:)file\:\s*[\'\"]([^\'\"]+)[\'\"]\,\s*\w+\:\s*[\'\"]([^\'\"]+)'''
			r=re.findall(pattern,r)
			r = [(i[1],i[0]) for i in r if i]
			u = sorted(r, key=lambda x: int(re.search('(\d+)', x[0]).group(1)), reverse=True)
			return u
		except: return

	def justporno(self, url):
		try:        
			r = client.request(url)
			s = re.findall('''source\s*src=['"]+([^'"]+)''', r)[0]
			ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
			headers = {'User-Agent': ua}
			response = requests.get(s, headers=headers, stream=True)
			play = response.url
			xbmc.Player().play(play)
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
		except:
			return

	def adultchannels(self, url):
		try:
			#dialog.ok("HERE","HERE")
			ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
			headers = {'User-Agent': ua}
			c = requests.get(url, headers=headers).content
			soup = BeautifulSoup(c, 'html5lib')
			r = soup.find('div', class_={'desc'})
			play = r.a['href']
			u = resolveurl.HostedMediaFile(play).resolve()
			xbmc.Player().play(u)
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
		except:
			return
			
	def fourtube(self, url):
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		headers = {'User-Agent': ua}
		link = requests.get(url, headers=headers).content
		soup = BeautifulSoup(link, 'html5lib')
		content = soup.find('div', class_={'links-list'})
		names = []
		srcs  = []
		for i in content.find_all('button'):
			IDS = i['data-id']
			quality = i['data-quality']
			names.append(quality)
			srcs.append(IDS)
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			token = srcs[selected]
			qual = names[selected]
			apiurl = ('https://token.4tube.com/%s/desktop/%s' % (token,qual))
			ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
			headers = {'User-Agent': ua,
						'Referer' : url,
						'Origin' : 'https://www.4tube.com'}
			link = requests.post(apiurl, headers=headers).content
			data = json.loads(link)
			play = data[qual]['token']
			xbmc.Player().play(play)
			xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
			
	def spankbang(self, url):
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		headers = {'User-Agent': ua}
		link = requests.get(url, headers=headers).content
		soup = BeautifulSoup(link, 'html5lib')
		content = soup.find('div', id={'video'})['data-streamkey']
		apiurl = 'https://spankbang.com/api/videos/stream'
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		headers = {'User-Agent': ua,
					'Referer' : url,
					'X-Requested-With': 'XMLHttpRequest'}
		post_data = {'id': content}
		link = requests.post(apiurl, data=post_data, headers=headers).content
		pattern = r'''['"](http.*?)['"]'''
		getlinks = re.findall(pattern,link,flags=re.DOTALL)
		names = [] ; srcs  = []
		for links in getlinks:
			if '2160p' in links: title = '4K'
			elif '1080p' in links: title = '1080'
			elif '720p' in links: title = '720'
			elif '480p' in links: title = '480'
			else: title = 'SD'
			names.append(title)
			srcs.append(links)
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			play = srcs[selected]
			xbmc.Player().play(play)
			xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
			xbmc.executebuiltin('Dialog.Close(busydialog)')
	def freeones(self, url):
		try:        
			u = client.request(url)
			e = re.findall('_script"\ssrc="([^"]*)', u)[0]
			return self.generic(e)
		except:
			return
			
	def fuqer(self, url):
		try:        
			u = client.request(url)
			e = re.findall('config:\'([^\']*)', u)[0]
			return self.generic(e)
		except:
			return

	def perfectgirls(self, url):
		try:
			r = client.request(url)
			pattern = r'''source\s*src=\"([^"]+)\"\s*res=\"\d+\"\s*label="([^"]+)"'''
			r = re.findall(pattern, r)
			r = [(i[1],i[0]) for i in r if i]
			u = sorted(r, key=lambda x: int(re.search('(\d+)', x[0]).group(1)), reverse=True)
			return u
		except:
			return


	def pornhub(self, url):
		try:
			r = client.request(url)
			vars = re.findall('var\s+(.+?)\s*=\s*(.+?);', r)
			link = re.findall('quality_\d+p\s*=\s*(.+?);', r)[0]
			link = [i.strip() for i in link.split('+')]
			link = [i for i in link if i.startswith('*/')]
			link = [re.sub('^\*/', '', i) for i in link]
			link = [(i, [x[1] for x in vars if x[0] == i]) for i in link]
			link = [i[1][0] if i[1] else i[0] for i in link]
			link = ''.join(link)
			link = re.sub('\s|\+|\'|\"', '', link)
			return link
		except:
			return 
	#pornheel gets url and provider name list
	def pornheel(self, url):
		try:
			u = client.request(url)
			e = re.findall('<a\shref="([^"]*)".+?">Streaming\s([^<]*)', u)
			e = [(client.request(i[0], output='geturl'), i[1]) for i in e if i]
			return e
		except:
			return 

	# def pandamovie(self, url):
		# try:
			# u = client.request(url)
			# e = re.findall('<li>.+?on ([^"]*).+?f="([^"]*)', u)
			# e = [(i[0],i[1]) for i in e if 'pandamovie' not in i[1]]
			# return e
		# except:
			# return


	def winporn(self, url):
		try:
			r = client.request(url)
			link = re.findall('var video_id = "(.+?)"', r)[0]
			r = 'http://nl.winporn.com/player_config_json/?vid=' + link + '&aid=0&domain_id=0&embed=0&ref=&check_speed=0'
			return self.generic(r)
		except:
			return


	def yuvutu(self, url):
		try:
			r = client.request(url)
			r = client.parseDOM(r, 'iframe', ret='src')
			r = [i for i in r if 'embed' in i][0]
			r = urlparse.urljoin(url, r)
			return self.generic(r)
		except:
			return
			
						
	def hugesix(self, url):
		try:
			main = client.request(url)
			links = re.findall('config=(.+?)",', main)[0] 
			link = links
			link = client.request(link)
			express1 = '<filehd>(.+?)</filehd>'
			express2 = '<file>(.+?)</file>'
			play = re.compile(express1, re.MULTILINE|re.DOTALL).findall(link)
			if not play: play = re.compile(express2, re.MULTILINE|re.DOTALL).findall(link)
			play = play[0]
			return play
		except:
			return

	def boobntit(self, url):
		try:
			main = client.request(url)
			link = client.parseDOM(main, 'div', attrs = {'id': 'player'})
			link = client.parseDOM(link, 'iframe', ret='src')
			link = link[0]
			return self.generic(link)
		except:
			return self.generic(url)
			
	def sexmax(self, url):
		try:        
			url = client.request(url)
			express = '<div id="player-embed">.+?<iframe src="(.+?)"'
			link = re.compile(express, re.MULTILINE|re.DOTALL).findall(url)[0]
			dir = client.request(link)
			dir = dir.replace('\/', '/')
			express = '"src":"(.+?)"'
			link = re.compile(express, re.MULTILINE|re.DOTALL).findall(dir)[0]
			return link
		except:
			return

	def drtube(self, url):
		try:        
			url = client.request(url)
			express = 'vid:(.+?),'
			link = re.compile(express, re.MULTILINE|re.DOTALL).findall(url)[0]
			link = 'http://www.drtuber.com/player_config_json/?vid=' + link + '&aid=0&domain_id=0&embed=0&ref=&check_speed=0'
			return self.generic(link)
		except:
			return
			
	def nuvid(self, url):
		try:        
			url = client.request(url)
			express = 'vid:(.+?),'
			link = re.compile(express, re.MULTILINE|re.DOTALL).findall(url)[0]
			link = 'http://www.nuvid.com/player_config_json/?vid=' + link + '&aid=0&domain_id=0&embed=0&ref=&check_speed=0'
			html = client.request(link)
			html = html.replace('\/', '/')
			express2 = '"hq":"(.+?)"'
			express3 = '"lq":"(.+?)"'
			play = re.compile(express2, re.MULTILINE|re.DOTALL).findall(html)
			if not play: play = re.compile(express3, re.MULTILINE|re.DOTALL).findall(html)
			play = play[0]
			return play
		except:
			return
			
	def solopornoitaliani(self, url):
		try:        
			url = client.request(url)
			express = '\'videoid\',\'(.+?)\''
			link = re.compile(express, re.MULTILINE|re.DOTALL).findall(url)[0]
			link = 'http://www.solopornoitaliani.xxx/vdata/' + link + '.flv'
			return link
		except:
			return
			
	def megasesso(self, url):
		try:        
			u = client.request(url)
			u = client.parseDOM(u, 'div', attrs = {'class': 'player-iframe'})
			u = [(client.parseDOM(i, 'iframe', ret='src')) for i in u]
			u = [(client.replaceHTMLCodes(i[0]).encode('utf-8')) for i in u]
			u = 'http://www.megasesso.com' + u[0]
			return self.generic(u)
		except:
			return

			
	def siska(self, url):
		try:        
			u = client.request(url)
			e = re.findall('document\.write\(base64_decode\(\'([^\']*)', u)[0]
			b64 = base64.b64decode(e)            
			play = re.findall('rc="([^"]*)', b64)[0]
			return play
		except:
			return

	def overthumbs(self, url):
		try:
			u = client.request(url)
			e = re.findall('(?s)id="play".+?src="([^"]*)', u)[0]
			e = ('http://overthumbs.com' + e)
			r = client.request(e)
			unpack = jsunpack.unpack(r)
			return re.findall('file.+?"([^"]*)',unpack)[0]
		except:
			return

	def streamate(self, url):
		try:
			u = client.request(url)
			e = re.findall('iframe\.src = \'([^\']*)', u)
			e = 'https://www.streamate.com' + e[0]
			r = client.request(e)
			r = re.findall('data-manifesturl="([^"]*)', r)[0]
			return self.generic(r)
		except:
			return

	#spreadporn gets link and provider name and provider logo
	def spreadporn(self, url):
		try:
			u = client.request(url)
			e = re.findall('(?s)<li class.+?"stream".+?k="([^"]*).+?c="([^"]*)"\salt="([^"]*)', u)
			return e
		except:
			return
			
	def satan18av(self, url):
		try:
			u = client.request(url)
			e = re.findall('<iframe src="([^"]*)', u)[0]
			return e
		except:
			return

	def befuck(self, url):
		try:
			u = client.request(url)
			e = re.findall('<source src="([^"]*)', u)[0]
			return e
		except:
			return      
	#mixhd gets link and provider  
	def mixhd(self, url):
		try:
			u = client.request(url)
			u = re.findall('<iframe src="([^"]*)', u)
			u = [(i,i.split('//')[-1].split('.')[0]) for i in u]
			return u
		except:
			return
	#xtheatre gets link and provider   
	def xtheatre(self, url):
		try:
			u = client.request(url)
			u = re.findall('<iframe src="([^"]*)', u)
			u = [(i,i.split('//')[-1].split('.')[0]) for i in u]
			return u
		except:
			return

	def youporn(self, url):
		try:        
			r = client.request(url)
			pattern = r"""quality[\'\"]\:[\'\"](\d+)[\'\"]\,[\'\"]videoUrl[\'\"]\:[\'\"]([^\'\"]+)"""
			i = re.findall(pattern,r)
			r = [(e[0], e[1].replace('\/','/')) for e in i]
			log_utils.log('%s' % str(r), log_utils.LOGERROR)
			u = sorted(r, key=lambda x: int(re.search('(\d+)', x[0]).group(1)), reverse=True)
			return u
		except: 
			return 
			
	def chaturbate(self, url):
		try:        
			r = client.request(url)
			pattern = r"""initHlsPlayer\(jsplayer,\s*["']([^'"]+)"""
			u = re.findall(pattern,r)[0]
			return u
		except: 
			return 'offline'
			
	def nxgx(self, url):
		try:        
			r = client.request(url)
			pattern = r"""iframe\s*src=['"]([^'"]+)"""
			u = re.findall(pattern,r)[0]
			u = resolveurl.HostedMediaFile(u).resolve()
			return u
		except: 
			return

	def hqporner(self, url):
		try:
			r = client.request(url)
			pattern = r"""iframe\s*width=['"]\d+['"]\s*height=['"]\d+['"]\s*src=['"]([^'"]+)"""
			url = re.findall(pattern,r)[0]
			url = url if url.startswith('http') else 'https:' + url
			r = client.request(url)
			pattern = r"""\s*file:\s*['"]([^'"]+)['"]\,\s*label:\s*['"]([^;"]+)"""
			urls = re.findall(pattern,r)
			links = []
			for i in urls:
				if i[0] not in str(links): links.append((i[0], i[1]))
			links = [(i[1], i[0] if i[0].startswith('http') else 'http:' + i[0]) for i in links]
			return links
		except:
			return
			
	# def threemovs(self, url):
		# try:
			# r = client.request(url)
			# pattern = r"""video_url:.+?'(.+?)'"""
			# url = re.findall(pattern,r)[0]
			# xbmc.Player().play(url)
		# except:
			# return
			
	def hclips(self, url):
		try:
			r = client.request(url)
			pattern = r'''<iframe width=['"]\d+['"]\s*height=['"]\d+['"]\s* src="(.*?)"'''
			url = re.findall(pattern,r)[0]
			r = client.request(url)
			pattern = r'''var\s*video_url="(.+?)"'''
			url2 = re.findall(pattern,r)[0]
			url2 = url2 + '|referer=' + url
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			xbmc.Player().play(url2)
		except:
			return
			
	def youngpornvideos(self,url):
			r = client.request(url)
			pattern = r'''file:\s+['"]([^'"]+).+?\s+label:\s+['"]([^'"]+)'''
			r = re.findall(pattern,r)
			names = []
			srcs  = []
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			for url,quality in sorted(r, reverse=False):
				names.append(kodi.giveColor(quality,'white',True))
				srcs.append(url)
			selected = kodi.dialog.select('Select a link.',names)
			if selected < 0:
				kodi.notify(msg='No option selected.')
				kodi.idle()
				quit()
			else:
				url2 = srcs[selected]
				xbmc.Player().play(url2)
	def javhihi(self,url):
			r = client.request(url)
			pattern = r'''<source\s+src=['"]([^'"]+)['"]\s.+?data-res=['"]([^'"]+)'''
			r = re.findall(pattern,r)
			names = []
			srcs  = []
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			for url,quality in sorted(r, reverse=True):
				names.append(kodi.giveColor(quality,'white',True))
				srcs.append(url)
			selected = kodi.dialog.select('Select a link.',names)
			if selected < 0:
				kodi.notify(msg='No option selected.')
				kodi.idle()
				quit()
			else:
				url2 = srcs[selected]
				xbmc.Player().play(url2)
	def anysex(self,url):
		r = client.request(url)
		pattern = r'''<source\s+id=['"]video_source.+?src=['"]([^'"]+)['"].+?title=['"](.*?)['"]'''
		r = re.findall(pattern,r,flags=re.DOTALL)
		names = []
		srcs  = []
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		for url,quality in sorted(r, reverse=True):
			names.append(kodi.giveColor(quality,'white',True))
			srcs.append(url)
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			url2 = srcs[selected]
			xbmc.Player().play(url2)

	def pandamovie(self,url):
		
		r = client.request(url)
		r = re.findall('<div id="pettabs">(.*?)</div>',r, flags=re.DOTALL)[0]
		pattern = r'''href=['"]([^'"]+)['"].+?>(.*?)<'''
		r = re.findall(pattern,r)
		names = []
		srcs  = []
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		for url,quality in sorted(r, reverse=True):
			names.append(kodi.giveColor(quality,'white',True))
			srcs.append(url)
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			url2 = srcs[selected]
			if resolveurl.HostedMediaFile(url2).valid_url(): 
				stream_url = resolveurl.HostedMediaFile(url2).resolve()
			#liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
			#liz.setPath(stream_url)
				xbmc.Player ().play(stream_url)
			else:
				xbmc.Player().play(url2)
		
	def txxx(self, url):
		try:
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			r = client.request(url)
			pattern = r'''<div class="download__link".+?<a href="(.*?)"'''
			url = re.findall(pattern,r)[0]
			url = CLEANUP(url)
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			xbmc.Player().play(url)
		except:
			return
			
	def vrsumo(self, url):
		try:
			r = client.request(url)
			pattern = r'''iframe\s+src=['"]([^'"]+)['"]'''
			url = re.findall(pattern,r)[1]
			r = client.request(url)
			pattern = r'''url:\s+['"]([^'"]+)['"]'''
			url = re.findall(pattern,r)[0]
			xbmc.executebuiltin("Dialog.Close(busydialog)")
			xbmc.Player().play(url)
		except:
			return
			
	def streamingporn(self,url):
		dialog.notification('XXX-O-DUS', '[COLOR yellow]Getting Links Now[/COLOR]', xbmcgui.NOTIFICATION_INFO, 5000)
		r = scraper.get(url).content
		r = re.findall('<em>(.*?)</div>',r, flags=re.DOTALL)[0]
		pattern = r'''<a\s+href=['"]([^'"]+)['"].+?.>(.*?)<'''
		r = re.findall(pattern,r)
		names = []
		srcs  = []
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		for url,name in r:
			name = name.replace('Download','').strip()
			names.append(kodi.giveColor(name,'white',True))
			srcs.append(url)
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			url2 = srcs[selected]
			if resolveurl.HostedMediaFile(url2).valid_url(): 
				stream_url = resolveurl.HostedMediaFile(url2).resolve()
			#liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
			#liz.setPath(stream_url)
				xbmc.Player ().play(stream_url)
			else:
				xbmc.Player().play(url2)
				
	def threemovs(self,url):
		link = client.request(url)
		play = re.findall('<div class="dropdown_submenu">.+?href="(.*?)"',link,flags=re.DOTALL)[0]
		xbmc.Player().play(play)
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
		
	def watchmygf(self,url):
		link = client.request(url)
		play = re.findall('''video_url.+?/0/(.*?)['"]''',link,flags=re.DOTALL)[0]
		play = play + '?rnd=1556547788367'
		xbmc.Player().play(play)
		
	def vrsmash(self,url):
		link = client.request(url)
		play = re.findall('''"contentUrl":\s+"(.*?)"''',link,flags=re.DOTALL)[0]
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		xbmc.Player().play(play)
