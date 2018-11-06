import re
import kodi
import client
import player
import dom_parser2
import log_utils
import utils
import resolveurl
import xbmcgui
import xbmc
dialog = xbmcgui.Dialog()
@utils.url_dispatcher.register('810', ['url'], ['name', 'iconimage', 'pattern']) 

def find(url, name=None, iconimage=None, pattern=None):

	kodi.busy()

	try: url,site = url.split('|SPLIT|')
	except: 
		site = 'Unknown'
		log_utils.log('Error getting site information from :: %s' % (url), log_utils.LOGERROR)

	try:
		if 'streamingporn.xyz' in url:
			c = client.request(url)
			r = dom_parser2.parse_dom(c, 'a', req=['href','class','rel','target'])
			r = [i for i in r if i.attrs['class'] == 'external']
			r = [client.request(i.attrs['href'], output='geturl') for i in r]
			r = [i for i in r if resolveurl.HostedMediaFile(i).valid_url()]
			url = multi(r)
		elif 'spreadporn.org' in url:
			c = client.request(url)
			r = dom_parser2.parse_dom(c, 'li', req=['data-show','data-link'])
			r = [(i.attrs['data-link']) for i in r]
			url = multi(r)
		# elif 'pandamovie.co' in url:
			# c = client.request(url)
			# r = dom_parser2.parse_dom(c, 'a', req='id')
			# r = [(i.attrs['href']) for i in r]
			# url = multi(r)
		elif 'xxxmoviestream.com' in url:
			c = client.request(url)
			pattern = '''<iframe src="(.+?)" scrolling="no" frameborder="0" width="700"'''
			r = re.findall(pattern,c)
			url = multi(r)
		elif 'sexkino.to' in url:   
			c = client.request(url)
			pattern = '''<iframe class="metaframe rptss" src="(.*?)"'''
			r = re.findall(pattern,c)[0]
			if 'xdrive.cc' in r:
				icon = 'https://lh5.ggpht.com/t6GgBV3lVq1uCb8qpTNjlilauVztXouZ2Eg1iN-HGAQQ1jtI19wTeEiGO77tysnN5KjZ=w300'
				dialog.notification('[COLOR yellow]Nemzzy[/COLOR]', '[COLOR yellow]Using Xdrive Resolver By Nemzzy[/COLOR]', icon, 5000)
				c = client.request(r)
				findid = re.findall('''video_id=(.*?)\'''',c,flags=re.DOTALL)[0]
				requesturl = 'https://xdrive.cc/secure_link?ip=81.12.123.22&video_id='+findid
				c = client.request(requesturl)
				r = re.findall('''\["(.*?)",''',c,flags=re.DOTALL)[0].replace('\\','')
				xbmc.Player().play(r)
			else:
				r = re.findall(pattern,c)
				url = multi(r)
		elif 'watchxxxfreeinhd.com' in url:
			r = client.request(url)
			pattern = r"""<iframe.+?src=['"]([^'"]+)"""
			r = re.findall(pattern,r)
			url = multi(r)
			
		
		

		
	except:
		kodi.idle()
		kodi.notify(msg='Error getting link for (Link Finder) %s' % name)
		kodi.idle()
		quit()

	url += '|SPLIT|%s' % site
	kodi.idle()
	player.resolve_url(url, name, iconimage)
    
def multi(r):
     
	r = [(re.findall('(?://)(?:www.)?([^.]+).', i)[0].title(), i) for i in r if resolveurl.HostedMediaFile(i).valid_url()]
	names = []
	srcs  = []

	if len(r) > 1:
		for i in sorted(r, reverse=True):
			names.append(kodi.giveColor(i[0],'white',True))
			srcs.append(i[1])
		selected = kodi.dialog.select('Select a link.',names)
		if selected < 0:
			kodi.notify(msg='No option selected.')
			kodi.idle()
			quit()
		else:
			url = srcs[selected]
			return url
	else: return r[0][1]
	