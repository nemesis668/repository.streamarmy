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
base_domain  = 'https://www.porndig.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 246
content_mode = 247
player_mode  = 801

search_tag   = 0
search_base  = urlparse.urljoin(base_domain,'/amateur/search/%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
	lover.checkupdates()

	try:
		url = urlparse.urljoin(base_domain,'video')
		c = client.request(url)
		r = dom_parser2.parse_dom(c, 'a', {'class': 'sidebar_section_item'})
		r = [i for i in r if 'channels' in i.attrs['href']]        
		r = [(urlparse.urljoin(base_domain,i.attrs['href']), i.content + ' - [ Professional ]') for i in r]
		url = urlparse.urljoin(base_domain,'amateur/videos/')
		c = client.request(url)
		e = dom_parser2.parse_dom(c, 'a', {'class': 'sidebar_section_item'})
		e = [i for i in e if 'channels' in i.attrs['href']]
		r += [(urlparse.urljoin(base_domain,i.attrs['href']), i.content + ' - [ Amateur ]') for i in e]        
		r = sorted(r, key=lambda x: x[1])
		if ( not r ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
			quit()
	except Exception as e:
		log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
		kodi.notify(msg='Fatal Error', duration=4000, sound=True)
		quit()

	dirlst = []
	urls = []
	for i in r:
		try:
			name = i[1]
			icon = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % filename))
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': i[0], 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst)    
	else:
		kodi.notify(msg='No Menu Items Found')
		quit()
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		c = client.request(url)
		r = re.findall('data-post_id=(.*?)<span class="pull-right">',c)
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
			name = re.findall('title="(.*?)"',i)[0]
			url = re.findall('href="(.*?)"',i)[0]
			if not base_domain in url: url = base_domain + url
			icon = re.findall('<img src="(.*?)"',i)[0]
			description = re.findall('<span class="pull-left">(.*?)</span>',i)[0]
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': description, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst, stopend=False, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))