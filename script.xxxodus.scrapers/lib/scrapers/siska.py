import xbmc,xbmcplugin,os,urlparse,re,requests
import client
import kodi
import dom_parser2
import log_utils
import lover
from resources.lib.modules import utils
from resources.lib.modules import helper
import xbmcgui
from bs4 import BeautifulSoup
buildDirectory = utils.buildDir #CODE BY NEMZZY AND ECHO
dialog = xbmcgui.Dialog()
filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'http://siska.video/'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 332
content_mode = 333
player_mode  = 801
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'/search.php?s=%s&search=search')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():

	lover.checkupdates()

	try:
		url = 'http://siska.video/category.php'
		c = requests.get(url,headers=headers).content
		soup = BeautifulSoup(c,'html.parser')
		r = soup.find_all('div', class_={'thumb'})
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
			name = i.h3.text
			icon = i.img['src']
			url2 = i.a['href']
			if not base_domain in url2: url2 = base_domain+url2
			if not base_domain in icon: icon = base_domain+icon
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (name,base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()

@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):


	try:
		c = client.request(url)
		soup = BeautifulSoup(c, 'html5lib')
		r = soup.find_all('div', class_={'thumb'})
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
			name = i.h3.text.strip()
			icon = i.img['data-src']
			url2 = i.a['href']
			if not base_domain in url2: url2 = base_domain+url2
			if not base_domain in icon: icon = base_domain+icon
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': name, 'folder': False})
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
			search_pattern = '''href=['"]([^'"]+)['"]>Next'''
			parse = base_domain        
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)