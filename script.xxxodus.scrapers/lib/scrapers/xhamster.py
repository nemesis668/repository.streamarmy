import xbmc,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import scraper_updater
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://m.xhamster.com'
base_name    = base_domain.replace('m.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 236
content_mode = 237
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'search.php?from=&new=&q=%s&qcat=video')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	scraper_updater.check(filename)

	try:
		url = urlparse.urljoin(base_domain,'categories')
		c = client.request(url)
		r = re.findall('<ul class="allcats page clearfix">(.*?)</ul>',c, flags=re.DOTALL)[0]
		pattern = r""".+?<a\s*href=['"]([^'"]+).+?>([^'"]+)<"""
		r = re.findall(pattern,r, flags=re.DOTALL)
		if ( not r ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
			quit()
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()

	dirlst = []

	for url,name in r:
		try:
			if not base_domain in url: url = base_domain + url
			icon = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % filename))
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url, 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except: pass

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()

@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		c = client.request(url)
		r = re.findall('<div class="item-container">(.*?)</a>',c, flags=re.DOTALL)
		if ( not r ) and ( not searched ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
	dirlst = []
		
	for i in r:
		try:
			name = re.findall('<div\s+class="item_name">(.*?)</div>', i, flags=re.DOTALL)[0]
			url2 = re.findall('<a\s+href="(.*?)"', i, flags=re.DOTALL)[0]
			icon = re.findall('<img\s+class="thumb"\s+src="(.*?)"', i, flags=re.DOTALL)[0]
			desc = re.findall('<div\s+class="time">(.*?)</div>', i, flags=re.DOTALL)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name + '[COLOR yellow] [ ' + desc + ' ] [/COLOR]', 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': desc, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		
		try:
			search_pattern = '''\<link\s*rel\=['"]next['"]\s*href\=['"]([^'"]+)'''
			parse = base_domain        
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)