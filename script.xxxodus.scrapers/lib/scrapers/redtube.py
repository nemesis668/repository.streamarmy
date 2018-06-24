import xbmc,xbmcplugin,xbmcgui,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir
dialog = xbmcgui.Dialog()

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://www.redtube.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 228
content_mode = 229
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'?search=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
	lover.checkupdates()

	try:
		url = urlparse.urljoin(base_domain,'categories')
		c = client.request(url)
		r = re.findall('<div class="category_item_wrapper">(.*?)</div>',c, flags=re.DOTALL)
		if ( not r ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
			quit()
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []

	for i in r:
		try:
			name = re.findall('<strong>(.*?)</strong>',i, flags = re.DOTALL)[0].strip()
			url  = re.findall('<a href="(.*?)"',i, flags = re.DOTALL)[0]
			if not base_domain in url: url = base_domain + url
			icon  = re.findall('data-thumb_url="(.*?)"',i, flags = re.DOTALL)[0]
			desc  = re.findall('<span class="category_count">(.*?)</span>',i, flags = re.DOTALL)[0].strip()
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url, 'mode': content_mode, 'icon': icon, 'fanart': fanarts,'description': desc, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):
	if not base_domain in url: url = base_domain + url
	try:
		c = client.request(url)
		r = re.findall('<div class="preloadLine">(.*?)<span class="video_count">',c, flags=re.DOTALL)
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
			name = re.findall('alt="(.*?)"',i, flags=re.DOTALL)[0]
			url2  = re.findall('<a.+?href="(.*?)"',i, flags=re.DOTALL)[0]
			if not base_domain in url2: url2 = base_domain + url2
			icon = re.findall('data-thumb_url\s* =\s*"(.*?)"',i, flags=re.DOTALL)[0]
			desc = re.findall('<span class="duration">(.*?)</span>',i, flags=re.DOTALL)[0].strip()
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': desc, 'folder': False})
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
			search_pattern = '''<li id="wp_navNext".+?\s*<a\s*href=['"]([^'"]+)['"]\s*>'''
			parse = base_domain       
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)