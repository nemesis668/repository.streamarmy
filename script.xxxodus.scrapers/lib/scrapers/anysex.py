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
base_domain  = 'https://anysex.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 404
content_mode = 405
player_mode  = 801

search_tag   = 0
search_base  = urlparse.urljoin(base_domain,'search/?q=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()

	try:
		url = urlparse.urljoin(base_domain,'/categories/')
		c = client.request(url)
		r = re.findall('<ul class="box">(.+?)</ul>',c,flags=re.DOTALL)[0]
		r = re.findall('<div class="img">(.+?)</div>',r,flags=re.DOTALL)
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []

	for i in r:
		try:
			name = re.findall('<span class="title">(.*?)</span>',i, flags=re.DOTALL)[0]
			url = re.findall('<a href="(.*?)"',i, flags=re.DOTALL)[0]
			icon = re.findall('<img class="thumb"\s+src="(.*?)"',i, flags=re.DOTALL)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % base_name))
			dirlst.append({'name': name, 'url': url,'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
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
		r = re.findall('<li class="item\s+">(.*?)</li>',c,flags=re.DOTALL)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
	dirlst = []
	for i in r:
		try:
			name = re.findall('title="(.*?)"',i, flags=re.DOTALL)[0]
			url2 = re.findall('<a href="(.*?)"',i, flags=re.DOTALL)[0]
			if not base_domain in url2: url2 = base_domain + url2
			icon = re.findall('<img\s+class="thumb"\s+src="(.*?)"',i, flags=re.DOTALL)[0]
			time = re.findall('<span\s+class="time">(.*?)</span>',i, flags=re.DOTALL)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name + '[COLOR yellow] | ' + time + '[/COLOR]', 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item. %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		search_pattern = '''<a\s*href=['"]([^'"]+)['"]\s*class="next"'''
		parse = base_domain
		helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)