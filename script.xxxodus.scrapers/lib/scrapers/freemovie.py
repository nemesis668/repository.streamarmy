import xbmc,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
import requests
from bs4 import BeautifulSoup
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir #CODE BY NEMZZY AND ECHO

filename     = 'pandamovie'
base_domain  = 'https://freeomovie.info/'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'movies'
menu_mode    = 410
content_mode = 411
player_mode  = 810

search_tag   = 0
search_base  = urlparse.urljoin(base_domain,'search.fcgi?query=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
	lover.checkupdates()
	url = base_domain
	content(url)
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		headers = {'User-Agent': ua}
		c = requests.get(url, headers=headers).content
		soup = BeautifulSoup(c, 'html5lib')
		r = soup.find_all('li', class_={'TPostMv'})
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
			name = i.find('div', class_={'Title'}).text
			url2 = i.a['href']
			icon = i.img['src']
			#fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': 'dd', 'folder': False})
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
			search_pattern = '''<link rel=['"]next['"]\s*href=['"]([^'"]+)'''
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)