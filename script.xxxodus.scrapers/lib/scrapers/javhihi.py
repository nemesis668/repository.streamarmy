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
base_domain  = 'http://javhihi.com/'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'scenes'
menu_mode    = 307
content_mode = 308
player_mode  = 801

search_tag   = 0
search_base  = urlparse.urljoin(base_domain,'search/video/%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()

	try:
		url = base_domain
		c = client.request(url)
		r = re.findall('<div class="col-sm-4"><a\s+href="(.*?)"\s+title="(.*?)"',c, flags=re.DOTALL)
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []

	for url,name in r:
		try:
			if base_domain not in url: url = base_domain + url
			icon = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % base_name))
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
		r = re.findall('<div\s+class="item-thumbnail">(.*?)<div\s+class="item-detail">',c, flags=re.DOTALL)
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
			icon = re.findall('<img src="(.*?)"',i, flags=re.DOTALL)[0]
			if not 'http' in icon: icon = 'http:' + icon
			time = re.findall('<span class="duration">(.*?)</span>',i, flags=re.DOTALL)[0]
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
		search_pattern = '''<a\s*href=['"]([^'"]+)['"]\s.+?>View\s+more<'''
		parse = base_domain
		helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)