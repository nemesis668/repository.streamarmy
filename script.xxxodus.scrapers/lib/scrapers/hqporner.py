import xbmc,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://hqporner.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 303
content_mode = 304
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'?s=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()

	try:
		url = urlparse.urljoin(base_domain,'categories')
		c = client.request(url)
		match = re.findall('<section class="box feature">(.+?)</section>', c, flags=re.DOTALL)
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []
	for items in match:
		try:
			name = re.findall('alt="(.*?)"', items, flags=re.DOTALL)[0]
			name = name.title()
			url = re.findall('<a href="(.*?)"', items, flags=re.DOTALL)[0]
			icon = re.findall('<img src="(.*?)"', items, flags=re.DOTALL)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			desc = re.findall('<p>(.*?)</p>', items, flags=re.DOTALL)[0]
			if not 'https:' in url: url = 'https://hqporner.com/' + url
			if not 'https:' in icon: icon = 'https://hqporner.com/' + icon
			dirlst.append({'name': name, 'url': url, 'description': desc, 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item. %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		c = client.request(url)
		match = re.findall ('<div class="6u">(.*?)</section>', c, flags=re.DOTALL)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
	dirlst = []
	for items in match:
		try:
			name = re.findall ('alt="(.*?)"', items, flags=re.DOTALL)[0]
			name = name.title()
			url2 = re.findall ('<a href="(.*?)"',items, flags=re.DOTALL)[0]
			icon = re.findall ('''<div onmouseleave=.*?"(.*?)"''',items, flags=re.DOTALL)[0]
			length = re.findall ('<span class="icon fa-clock-o meta-data">(.*?)</span>',items, flags=re.DOTALL)[0]
			if not 'https:' in url2: url2 = 'https://hqporner.com' + url2
			if not 'https:' in icon: icon = 'https:' + icon
			desc = '[COLOR yellow]Video Length :: [/COLOR]' + length
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': desc, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item. %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		search_pattern = '''<a\s*href=['"]([^'"]+)['"]\s*class=['"]button\s*mobile-pagi pagi-btn['"]>Next<\/a>'''
		parse = base_domain
		helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)