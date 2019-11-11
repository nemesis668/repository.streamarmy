import xbmc,xbmcgui,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from resources.lib.modules import utils
from resources.lib.modules import helper
from bs4 import BeautifulSoup
buildDirectory = utils.buildDir #CODE BY NEMZZY AND ECHO
dialog = xbmcgui.Dialog()

filename     = 'pandamovie'
base_domain  = 'https://adult-channels.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'movies'
menu_mode    = 500
content_mode = 501
player_mode  = 801

search_tag   = 0
search_base  = urlparse.urljoin(base_domain,'search.fcgi?query=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()
	url = urlparse.urljoin(base_domain,'erotic-films/')
	content(url)

        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):
	try:
		c = client.request(url)
		soup = BeautifulSoup(c, 'html5lib')
		r = soup.find('div', class_={'videos-list'})
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
		
	for a in r.find_all('a'):
		try:
			title = a['title']
			url2 = a['href']
			icon = a.img['data-src']
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': title, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': title, 'folder': False})
		except Exception as e:
			log_utils.log('Error: %s' % str(e), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		
		try:
			search_pattern = '''<a\s*href=['"]([^'"]+)['"]>Next'''
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)