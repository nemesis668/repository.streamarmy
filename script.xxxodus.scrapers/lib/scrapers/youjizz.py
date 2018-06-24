import xbmc,xbmcplugin,xbmcgui,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir
dialog	= xbmcgui.Dialog()

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'https://www.youjizz.com'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 244
content_mode = 245
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'search/%s-1.html')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
	lover.checkupdates()

	try:
		headers = {'User-Agent': 'Google Chrome Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
		url = urlparse.urljoin(base_domain,'tags')
		c = client.request(url, headers=headers)
		r = dom_parser2.parse_dom(c, 'li')
		r = [i.content for i in r if 'href' in i.content and 'span' in i.content]

		r = [(dom_parser2.parse_dom(i, 'a', req='href'), \
			dom_parser2.parse_dom(i, 'span')) \
			for i in r]
		r = [(i[0][0].attrs['href'].replace(' ','%20'), re.sub('<.+?>','',i[0][0].content), i[1][0].content.replace('(','').replace(')','')) for i in r]
		r = [(i[0], i[1], i[2]) for i in r if i[2].isdigit()]
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
			name = kodi.sortX(i[1].encode('utf-8'))
			name = name.title() + ' - [ %s ]' % i[2]
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
	if not base_domain in url: url = base_domain + url
	try:
		headers = {'User-Agent': 'Google Chrome Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
		c = client.request(url, headers = headers)
		r = re.findall('<div class="video-item">(.*?)</select>',c, flags=re.DOTALL)
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
			name = re.findall("""<a href='.+?'>(.*?)</a>""",i, flags=re.DOTALL)[0]
			url2 = re.findall('href="(.*?)"',i, flags=re.DOTALL)[0]
			if not base_domain in url2: url2 = base_domain + url2
			icon = re.findall('src="(.*?)"',i, flags=re.DOTALL)[0]
			if not 'https' in icon: icon = 'https:' + icon
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'folder': False})
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
			search_pattern = '''\s*href\=['"]([^'"]+)['"]\>Next'''
			parse = base_domain        
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)