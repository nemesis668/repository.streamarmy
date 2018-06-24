import xbmc,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
import xbmcgui
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir
dialog = xbmcgui.Dialog()
filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://www.txxx.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 309
content_mode = 310
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'search/?s=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()

	try:
		url = base_domain
		c = client.request(url)
		r = re.findall('<li class="list__item side-cats__item"(.*?)</li>',c)
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []

	for i in r:
		try:
			name = re.findall('title="(.*?)"',i)[0]
			url = re.findall('href="(.*?)"',i)[0]
			if not base_domain in url: url = base_domain + url
			number = re.findall('data-total-videos="(.*?)"',i)[0]
			icon = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % base_name))
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % base_name))
			dirlst.append({'name': name + '[COLOR yellow] [ ' + number + ' ][/COLOR]', 'url': url,'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item. %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()

@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):
	if base_domain not in url: url = base_domain + url
	try:
		c = client.request(url)
		r = re.findall('<div class="un-grid--thumb--content">(.*?)<div class="un-grid--thumb--info">',c)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
	dirlst = []
	for i in r:
		try:
			name = re.findall('alt="(.*?)"',i)[0]
			url2 = re.findall('<a href="(.*?)"',i)[0]
			icon = re.findall('<img src="(.*?)"',i)[0]
			time = re.findall('<div class="thumb__duration">(.*?)</div>',i)[0]
			if not base_domain in url2: url2 = base_domain + url2
			if not 'https' in icon: icon = 'https:' + icon
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name + '[COLOR yellow] [ ' + time + ' ][/COLOR]', 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item. %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		search_pattern = '''href=['"]([^'"]+)['"]\s+title="Next\s+Page"'''
		parse = base_domain
		helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)