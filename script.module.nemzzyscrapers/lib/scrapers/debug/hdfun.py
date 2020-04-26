import re, requests, json
import xbmcgui
import xbmc
import random
dialog = xbmcgui.Dialog()
import xbmcaddon
_addon_id_ = 'plugin.video.Flex'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Enabled = _self_.getSetting('HDFUN')

class Scraper:
	def __init__(self):
		self.Base = 'https://api.hdv.fun/embed/'
		self.Search = ('%s')
		self.links = []
	def Index(self,type,term,year,imdb,torrents):
		if Enabled == 'false': return False
		if type == 'MOVIE':
			try:
				import random
				ip = ".".join(map(str, (random.randint(0, 255) 
										for _ in range(4))))
				session = requests.Session()
				ref = ('https://api.hdv.fun/embed/%s' % imdb)
				ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
				headers = {'User-Agent': ua,
				'Referer': ref,
				'X-Requested-With': 'XMLHttpRequest'}
				post_data = {'imdb': imdb,
				'ip': ip}
				filmname = term.title()
				url = 'https://api.hdv.fun/l1'
				link2 = session.post(url, data=post_data, headers=headers).content
				data = json.loads(link2)
				data = str(data)
				pattern = r'''src['"]:\su['"](.*?)['"].*?label.*?u['"](.*?)['"]'''
				sources = re.findall(pattern,data,flags=re.DOTALL)
				for url2,qual in sources:
					if '360' in qual:
						title = ('HDFUN | SD | DIRECT | %s' % filmname)
						quality = '4'
					elif '480' in qual:
						title = ('HDFUN | SD | DIRECT | %s' % filmname)
						quality = '4'
					elif '720' in qual:
						title = ('HDFUN | HD | DIRECT | %s' % filmname)
						quality = '3'
					elif '1080' in qual:
						title = ('HDFUN | FHD | DIRECT | %s' % filmname)
						quality = '2'
					else:
						title = ('HDFUN | Unkown | DIRECT | %s' % filmname)
						quality = '4'
					self.links.append({'title': title, 'url': url2, 'quality': quality})
				return self.links
			except Exception as c:
				xbmc.log("ERROR ::: %s" %c , level=xbmc.LOGNOTICE)
		else: pass

