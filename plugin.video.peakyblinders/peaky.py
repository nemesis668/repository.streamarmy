#########################################
############CODE BY @NEMZZY668###########


import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,base64,time
from resources.libs.common_addon import Addon
import requests
import resolveurl
from metahandler import metahandlers
from HTMLParser import HTMLParser


addon_id	= 'plugin.video.peakyblinders'
addon		= Addon(addon_id, sys.argv)
selfAddon	= xbmcaddon.Addon(id=addon_id)
AddonTitle	= '[COLOR yellow][B]Peaky Blinders[/B][/COLOR]'
addonPath	= os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'plugin.video.peakyblinders')
fanarts		= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
fanart		= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
icon		= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
IconImage		= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
dp			=	xbmcgui.DialogProgress()
dialog		=	xbmcgui.Dialog()

#########################################################
MainUrl = 'https://putlockermovies.to/series/peaky-blinders/'
seasoninfo = 'Peaky Blinders is a British television crime drama set in 1920s Birmingham, England in the aftermath of World War I. The series, which was created by Steven Knight and produced by Caryn Mandabach Productions, Screen Yorkshire and Tiger Aspect Productions, follows the exploits of the Shelby crime family. It was the first production to benefit from investment through Screen Yorkshire\'s Yorkshire Content Fund, ensuring the bulk of the production was filmed in Yorkshire. Cillian Murphy plays Tommy Shelby, the gang\'s leader, and Sam Neill as Chester Campbell is a commissioned detective who is tasked with suppressing the gang.[2] The series creators have reused the name of Peaky Blinders, a 19th century urban youth gang who were active in the city until the 1890s and were believed to sew razor blades into their caps.The first series aired on BBC Two on 13 September 2013 and ran for six episodes. The second series premiered on 2 October 2014. The third series premiered on 5 May 2016. On 26 May 2016, the BBC announced they had ordered a fourth and fifth series of the show.The fourth series premiered on 15 November 2017 after the series finale broadcast on 20 December 2017, it was announced that the fifth series will be broadcast in 2019'

#########################################################


def GetMenu():

	link = open_url(MainUrl)
	match = re.compile ('<div class="les-title">(.*?)</ul>').findall(link)
	i = 0
	for data in match:
		i += 1
		season = re.compile('''<strong>(.*?)</strong>''').findall(data)[0]
		seasonmatch = 'season-' + str(i) + '-'
		addDir("[COLOR yellow]" + season + "[/COLOR]",seasonmatch,2,icon,fanart,seasoninfo)

def GetContent(url):

	onlyfind = url
	link = open_url(MainUrl)
	match = re.compile ('<div class="les-title">(.*?)</ul>').findall(link)
	multilinks = []
	titles = []
	combined = []
	for data in match:
		title = re.compile('''<a href=".*?">(.*?)</a>''').findall(data)
		for name in title:
			titles.append(name)
		url = re.compile('''<a href="(.*?)"''').findall(data)
		for links in url:
			multilinks.append(links)
		combined = list(zip(titles,multilinks))
	for epi,link in combined:
		if onlyfind in link:
			addLink("[COLOR yellow]" + epi + "[/COLOR]",link,4,icon,fanart,seasoninfo)
			
def grabresolve(url):
	
	link = open_url(url)
	play = re.compile ('<iframe src="(.*?)"').findall(link)[0]
	PLAYLINK(name,play,iconimage)

def open_url(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
		response = urllib2.urlopen(req, timeout=5)
		link=response.read()
		response.close()
		link=link.replace('\n','').replace('\r','')
		return link
	except:quit()

def addDir(name,url,mode,iconimage,fanart,description=''):

	if not iconimage:
		iconimage = icon
	if not fanart:
		fanart = fanarts
	description = description.encode(encoding='UTF-8',errors='strict')
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage,)
	liz.setProperty( "fanart_Image", fanart )
	liz.setProperty( "icon_Image", iconimage )
	liz.setInfo('video', {'Plot': description})
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	view=xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	return ok

def addLink(name, url, mode, iconimage, fanart, description=''):

	if not iconimage:
		iconimage = icon
	if not fanart:
		fanart = fanarts
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setProperty( "fanart_Image", fanart )
	liz.setProperty( "icon_Image", iconimage )
	liz.setInfo('video', {'Plot': description})
	favs=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str('889')+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
	liz.addContextMenuItems([('[COLOR pink]Add To Bishop Favourites[/COLOR]', 'xbmc.RunPlugin('+favs+')')])
	view=xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def PLAYLINK(name,url,iconimage):

	dialog.notification(AddonTitle, '[COLOR yellow]Getting Link By Order Of The Peaky Blinders[/COLOR]', icon, 5000)
	if resolveurl.HostedMediaFile(url).valid_url(): 
		stream_url = resolveurl.HostedMediaFile(url).resolve()
		liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
		liz.setPath(stream_url)
		xbmc.Player ().play(stream_url, liz, False)
		quit()
	else:
		stream_url=url
		liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
		liz.setPath(stream_url)
		xbmc.Player ().play(stream_url, liz, False)
		quit()

def SET_VIEW():

	xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
	version=float(xbmc_version[:4])
	if version >= 11.0 and version <= 11.9:
		codename = 'Eden'
	elif version >= 12.0 and version <= 12.9:
		codename = 'Frodo'
	elif version >= 13.0 and version <= 13.9:
		codename = 'Gotham'
	elif version >= 14.0 and version <= 14.9:
		codename = 'Helix'
	elif version >= 15.0 and version <= 15.9:
		codename = 'Isengard'
	elif version >= 16.0 and version <= 16.9:
		codename = 'Jarvis'
	elif version >= 17.0 and version <= 17.9:
		codename = 'Krypton'
	else: codename = "Decline"
	if codename == "Jarvis":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	elif codename == "Krypton":
		xbmc.executebuiltin('Container.SetViewMode(55)')
	else: xbmc.executebuiltin('Container.SetViewMode(55)')

def CLEANUP(text):

	text = str(text)
	text = text.replace('\\r','')
	text = text.replace('\\n','')
	text = text.replace('\\t','')
	text = text.replace('\\','')
	text = text.replace('<br />','\n')
	text = text.replace('<hr />','')
	text = text.replace('&#039;',"'")
	text = text.replace('&#39;',"'")
	text = text.replace('&quot;','"')
	text = text.replace('&rsquo;',"'")
	text = text.replace('&amp;',"&")
	text = text.replace('&#8211;',"&")
	text = text.replace('&#8217;',"'")
	text = text.replace('&#038;',"&")
	text = text.replace('&#8211;',"-")
	text = text.replace('&#8216;',"'")
	text = text.replace('&#8230;',"...")
	text = text.replace('&#8220;',"'")
	text = text.replace('&#8221;',"'")
	text = text.replace('&#8212;',"_")
	text = text.lstrip(' ')
	text = text.lstrip('	')
	text = strip_non_ascii(text)
	return text

####################################################################################################################
####################################################################################################################

def get_params():

	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
				params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
					param[splitparams[0]]=splitparams[1]
	return param

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None; description=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanart=urllib.unquote_plus(params["fanart"])
except: pass
try: description=urllib.unquote_plus(params["description"])
except: pass
 
if mode==None or url==None or len(url)<1: GetMenu()

elif mode==2:GetContent(url)
elif mode==4:grabresolve(url)

elif mode==99:PLAYLINK(name,url,iconimage)

if mode==None or url==None or len(url)<1: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=False)
else: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)