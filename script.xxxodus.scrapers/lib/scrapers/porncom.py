import xbmc,xbmcgui,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from bs4 import BeautifulSoup
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir #CODE BY NEMZZY AND ECHO
dialog = xbmcgui.Dialog()

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://www.porn.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 220
content_mode = 221
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'videos/search?q=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
	lover.checkupdates()

	try:
		url = base_domain
		c = client.request(url)
		soup = BeautifulSoup(c, 'html5lib')
		content = soup.find_all('div', class_={'list-global__item'})
		if ( not content ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
			quit()
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()
		
	dirlst = []

	for i in content:
		try:
			title = re.findall('''a\shref=.*?title=['"](.*?)['"]''',str(i),flags=re.DOTALL)[0]
			icon = i.img['data-src']
			url2 = re.findall('''a\shref=['"](.*?)['"]''',str(i),flags=re.DOTALL)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': title, 'url': url2, 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		#url = url.replace('-','+')
		c = client.request(url)
		soup = BeautifulSoup(c, 'html5lib')
		content = soup.find_all('div', class_={'list-global__thumb'})
		if ( not content ) and ( not searched ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
		
	dirlst = []
		
	for i in content:
		try:
			title = i.a['title']
			url2 = i.a['href']
			icon = i.img['data-src']
			if not base_domain in url2: url2 = base_domain+url2
			if searched: description = 'Result provided by %s' % base_name.title()
			else: description = title
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': title, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': description, 'folder': False})
		except Exception as e:
			pass
			#log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		
		try:
			search_pattern = '''href=['"]([^'"]+)['"].*?Next'''
			parse = base_domain        
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)