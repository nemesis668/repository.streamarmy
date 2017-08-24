import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,shutil,urlresolver,random,liveresolver,time
from resources.libs.common_addon import Addon
import base64
from metahandler import metahandlers

addon_id        = 'plugin.video.mightyred'
addon           = Addon(addon_id, sys.argv)
selfAddon       = xbmcaddon.Addon(id=addon_id)
AddonTitle      = '[COLOR yellow]Mighty Red[/COLOR]'
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
searchicon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'search.jpg'))
nextpage        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.png'))
sd_path         = xbmc.translatePath(os.path.join('special://home/addons/', 'plugin.video.sportsdevil'))
baseurl         = 'https://pastebin.com/raw/Si0YSXu2'
ytpl            = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
ytpl2           = '&maxResults=50&key=AIzaSyAd-YEOqZz9nXVzGtn3KWzYLbLaajhqIDA'
ytplpg1         = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
ytplpg2         = '&part=snippet&playlistId='
ytplpg3         = '&maxResults=50&key=AIzaSyAvB3XWYEqUQPFoVMWssjqJhyeJOMi3A8g'
adultpass       = selfAddon.getSetting('password')
metaset         = selfAddon.getSetting('enable_meta')
messagetext     = 'https://pastebin.com/raw/KhDD9Czc'
RUNNER 			= base64.b64decode(b'aHR0cDovL3NpbXRlY2gubmV0MTYubmV0L3lvdXR1YmUucGhwP2lkPQ==')
SEARCH_LIST     = base64.b64decode(b'')
dialog          = xbmcgui.Dialog()
intro_done      = xbmc.translatePath('special://home/addons/plugin.video.mightyred/intro')
                                                               
def GetMenu():
    popup()
    xbmc.executebuiltin('Container.SetViewMode(500)')
    url = baseurl
    addDir('[B][COLOR yellow]@Live_Prem_Addon[/COLOR][/B]',url,5,searchicon,fanarts)
    link=open_url(baseurl)
    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:
        try:
            if '<channel>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                    addDir(name,url,6,iconimage,fanart)
            elif '<anfield>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<anfield>(.+?)</anfield>').findall(item)[0]
                    addDir(name,url,11,iconimage,fanart)
            elif '<playlist>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                    addDir(name,url,43,iconimage,fanart)
            elif '<LFCNEWS>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<LFCNEWS>(.+?)</LFCNEWS>').findall(item)[0]
                    addDir(name,url,18,iconimage,fanart)
            elif '<shighlights>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<shighlights>(.+?)</shighlights>').findall(item)[0]
                    addDir(name,url,68,iconimage,fanart)
            if '<sportsdevil>' in item:
                    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                    if len(links)==1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                         url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                         referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                         check = referer
                         suffix = "/"
                         if not check.endswith(suffix):
                             refer = check + "/"
                         else:
                             refer = check
                         link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                         url = link + '%26referer=' +refer
                         addItem(name,url,4,iconimage,fanart)   
                    elif len(links)>1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                         fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                         addItem(name,url2,8,iconimage,fanart)       
            elif '<folder>'in item:
                            data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                            for name,url,iconimage,fanart in data:
                                    addDir(name,url,1,iconimage,fanart)
            else:
                            links=re.compile('<link>(.+?)</link>').findall(item)
                            if len(links)==1:
                                    data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                    lcount=len(match)
                                    for name,url,iconimage,fanart in data:
                                            if 'youtube.com/playlist' in url:
                                                    addDir(name,url,2,iconimage,fanart)
                                            else:
                                                    addLink(name,url,2,iconimage,fanart)
                            elif len(links)>1:
                                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                    addLink(name,url2,3,iconimage,fanart)
        except:pass
        view(link)
    icon = 'http://i.imgur.com/8rqgk8R.png'
    addItem('[B][COLOR yellow]'+'Real Debrid Login'+'[/COLOR]''[/B]','url',17,icon,fanarts)
		
    if not os.path.exists(intro_done):
        intro = 'http://simtechaddons.com/intro/MightyRedIntro.mp4'
        xbmc.Player().play(intro, xbmcgui.ListItem('Welcome to Mighty Reds'))
        os.makedirs(intro_done)
        
        
        
    #view(link)
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
    text = text.lstrip(' ')
    text = text.lstrip('	')

    return text

def popup():
        message=open_url2(messagetext)
        if len(message)>1:
                path = xbmcaddon.Addon().getAddonInfo('path')
                comparefile = os.path.join(os.path.join(path,''), 'compare.txt')
                r = open(comparefile)
                compfile = r.read()       
                if compfile == message:pass
                else:
                        showText('[B][COLOR yellow]Mighty Red[/COLOR][/B] [B][COLOR yellow]Information[/COLOR][/B]', message)
                        text_file = open(comparefile, "w")
                        text_file.write(message)
                        text_file.close()

def resolver_settings():
    urlresolver.display_settings()
                        
def GetContent(name,url,iconimage,fanart):
        url2=url
        link=open_url(url)

        match= re.compile('<item>(.+?)</item>').findall(link)
        for item in match:
            try:
                if '<channel>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                        addDir(name,url,6,iconimage,fanart)
                if '<image>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<image>(.+?)</image>').findall(item)[0]
                        addDir(name,iconimage,9,iconimage,fanart)
                elif '<playlist>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                        addDir(name,url,43,iconimage,fanart)
                if '<sportsdevil>' in item:
                        links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                        if len(links)==1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                             url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                             referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                             check = referer
                             suffix = "/"
                             if not check.endswith(suffix):
                                 refer = check + "/"
                             else:
                                 refer = check
                             link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                             url = link + '%26referer=' +refer
                             addItem(name,url,4,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,8,iconimage,fanart)
    
                elif '<folder>'in item:
                                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                for name,url,iconimage,fanart in data:
                                        addDir(name,url,1,iconimage,fanart)
                else:
                                links=re.compile('<link>(.+?)</link>').findall(item)
                                if len(links)==1:
                                        data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                        lcount=len(match)
                                        for name,url,iconimage,fanart in data:
                                                if 'youtube.com/playlist' in url:
                                                        addDir(name,url,2,iconimage,fanart)
                                                else:
                                                        addLink(name,url,2,iconimage,fanart)
                                elif len(links)>1:
                                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                        addLink(name,url2,3,iconimage,fanart)
            except:pass
            view(link)

def YOUTUBE_CHANNEL(url):

	CHANNEL = RUNNER + url
	link = open_url(CHANNEL)
	patron = "<video>(.*?)</video>"
	videos = re.findall(patron,link,re.DOTALL)

	items = []
	for video in videos:
		item = {}
		item["name"] = find_single_match(video,"<name>([^<]+)</name>")
		item["url"] = base64.b64decode(b"cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9") + find_single_match(video,"<id>([^<]+)</id>")
		item["author"] = find_single_match(video,"<author>([^<]+)</author>")
		item["iconimage"] = find_single_match(video,"<iconimage>([^<]+)</iconimage>")
		item["date"] = find_single_match(video,"<date>([^<]+)</date>")
		
		addLink('[COLOR white]' + item["name"] + ' - on ' + item["date"] + '[/COLOR]',item["url"],7,item["iconimage"],fanart)

def anfield_menu():

    url = 'http://anfieldindex.com/podcasts'
    result = open_url(url)
    match = re.compile('<main class="container podcasts">(.+?)<main class="container">',re.DOTALL).findall(result)[0]
    match2 = re.compile('<a(.+?)</a>',re.DOTALL).findall(match)
    for item in match2:
        try:
            name = re.compile('title="(.+?)"',re.DOTALL).findall(item)[0]
            url = re.compile('href="(.+?)"',re.DOTALL).findall(item)[0]
            iconimage = re.compile('data-src="(.+?)"',re.DOTALL).findall(item)[0]
            url = "http://anfieldindex.com" + url
            addDir('[COLOR red][B]' + name + '[/B][/COLOR]',url,10,iconimage,fanarts)
        except: pass
    xbmc.executebuiltin('Container.SetViewMode(55)')
        
def anfield_index(url):

    result = open_url(url)
    match = re.compile('<article class="card podcast">(.+?)</article>',re.DOTALL).findall(result)
    for item in match:
        try:
            name = re.compile('<h3 class="title primary-color">(.+?)</h3>',re.DOTALL).findall(item)[0]
            url = re.compile('<a target="_blank" href="(.+?)">',re.DOTALL).findall(item)[0]
            iconimage = re.compile('data-src="(.+?)"',re.DOTALL).findall(item)[0]
            name = name.replace('&amp;','&')
            addLink('[COLOR red][B]' + name + '[/B][/COLOR]',url,2,iconimage,fanarts)
        except: pass
    xbmc.executebuiltin('Container.SetViewMode(55)')
	
def SCRAPE_SPORTSHIGHLIGHTS_GAMES():

    url = 'http://www.goalsarena.org/en/'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile ('<div class="videos"(.+?)<div class="moduletable-none">').findall(link)[0]
    grab = re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(match)
    
    for link1,game in grab:
        addDir("[COLOR yellow]" + game + "[/COLOR]",link1,69,icon,fanarts,'')
        
def SCRAPE_SPORTSHIGHLIGHTS_LINKS(url):

    
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    source = dialog.select('[COLOR yellow]Choose Normal Or Extended Highlights[/COLOR]', ['[COLOR yellow]Normal[/COLOR]','[COLOR yellow]Extended[/COLOR]'])
    if source == 0:
        match = re.compile ('<iframe src="(.+?)"').findall(link)[0]
        link2 = open_url(match)
        url = re.compile ('<source src="(.+?)"').findall(link2)[0]
        url = 'https:' + url
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        xbmc.Player ().play(url, liz, False)
        quit(0)
    if source == 1:
        try:
            match = re.compile ('<iframe src="(.+?)"').findall(link)[1]
        except IndexError:
            dialog.notification("[COLOR yellow]Mighty Red[/COLOR]", 'Sorry This Game Doesn\'t Have Extended Highlight Available', icon, 9000)
            time.sleep(2)
            SCRAPE_SPORTSHIGHLIGHTS_LINKS(url)
        link2 = open_url(match)
        url = re.compile ('<source src="(.+?)"').findall(link2)[0]
        url = 'https:' + url
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        xbmc.Player ().play(url, liz, False)
        quit(0)
	
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
    text = text.replace('&nbsp;'," ")
    text = text.lstrip(' ')
    text = text.lstrip('    ')
    
    return text
	
def SEARCH():
	keyb = xbmc.Keyboard('', '[B][COLOR red]@Live_Prem_Addon[/COLOR][/B]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=searchterm.upper()
	else:quit()
	link=open_url(SEARCH_LIST)
	slist=re.compile('<link>(.+?)</link>').findall(link)
	for url in slist:
                url2=url
                link=open_url(url)
                entries= re.compile('<item>(.+?)</item>').findall(link)
                for item in entries:
                        match=re.compile('<title>(.+?)</title>').findall(item)
                        for title in match:
                                title=title.upper()
                                if searchterm in title:
                                    try:
                                        if '<sportsdevil>' in item:
                                                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                                                url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                                                referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                                                link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                                                url = link + '%26referer=' +referer
                                                if 'tp' in url:
                                                        addLink(name,url,4,iconimage,fanarts)       
                                        elif '<folder>'in item:
                                                        data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                                        for name,url,iconimage,fanart in data:
                                                                if 'tp' in url:
                                                                        addDir(name,url,1,iconimage,fanarts)
                                        else:
                                                        links=re.compile('<link>(.+?)</link>').findall(item)
                                                        if len(links)==1:
                                                                data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                                                lcount=len(match)
                                                                for name,url,iconimage,fanart in data:
                                                                        if 'youtube.com/playlist' in url:
                                                                                addDir(name,url,2,iconimage,fanarts)
                                                                        else:
                                                                                if 'tp' in url: 
                                                                                        addLink(name,url,2,iconimage,fanarts)
                                                        elif len(links)>1:
                                                                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                                                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                                                addLink(name,url2,3,iconimage,fanarts)
                                    except:pass       
                        
		
def GETMULTI(name,url,iconimage):
	streamurl=[]
	streamname=[]
	streamicon=[]
	link=open_url(url)
	urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
	iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
	links=re.compile('<link>(.+?)</link>').findall(urls)
	i=1
	for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )
                i=i+1
	name='[COLOR red]'+name+'[/COLOR]'
	dialog = xbmcgui.Dialog()
	select = dialog.select(name,streamname)
	if select < 0:
		quit()
	else:
		url = streamurl[select]
		print url
		if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
                elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
                else: stream_url=url
                liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
                liz.setPath(stream_url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                
def GETMULTI_SD(name,url,iconimage):

    sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
    streamurl=[]
    streamname=[]
    streamicon=[]
    streamnumber=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(urls)
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    i=1

    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                        streamnumber.append('Stream ' + str(i))
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )

                i=i+1
    name='[COLOR red]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        check = streamname[select]
        suffix = "/"
        if not check.endswith(suffix):
              refer = check + "/"
        else:
              refer = check
        url = sdbase + streamurl[select] + "%26referer=" + refer
        print url

        xbmc.Player().play(url)

def PLAYSD(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)
        
def PLAYLINK(name,url,iconimage):
    
    if 'youtube.com/playlist' in url:
        searchterm = url.split('list=')[1]
        ytapi = ytpl + searchterm + ytpl2
        req = urllib2.Request(ytapi)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link = link.replace('\r','').replace('\n','').replace('  ','')     
        match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
        try:
            np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
            ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
            addDir('Next Page >>',ytapi,2,nextpage,fanart)
        except:pass
        for name,ytid in match:
            url = 'https://www.youtube.com/watch?v='+ytid
            iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
            if not 'Private video' in name:
                if not 'Deleted video' in name:
                    addLink(name,url,2,iconimage,fanart)

    if 'https://www.googleapis.com/youtube/v3' in url:
            searchterm = re.compile('playlistId=(.+?)&maxResults').findall(url)[0]
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            link = link.replace('\r','').replace('\n','').replace('  ','')     
            match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
            try:
                    np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
                    ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
                    addDir('Next Page >>',ytapi,2,nextpage,fanart)
            except:pass


   
            for name,ytid in match:
                    url = 'https://www.youtube.com/watch?v='+ytid
                    iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
                    if not 'Private video' in name:
                            if not 'Deleted video' in name:
                                    addLink(name,url,2,iconimage,fanart)

    
    if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
    elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
    else: stream_url=url
    liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

    if 'http' not in url:
        if '.ts'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
        elif 'acestream' in url:
            url = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
            xbmc.Player ().play(url)
        elif urlresolver.HostedMediaFile(url).valid_url():
            url = urlresolver.HostedMediaFile(url).resolve()           
        elif liveresolver.isValid(url)==True:
                url=liveresolver.resolve(url)
        liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        xbmc.Player ().play(url, liz, False)
        quit()
                            
def PLAYVIDEO(url):

	xbmc.Player().play(url)

def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'mat')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        print link
        return link
    except:quit()

def open_url2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'mat')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        print link
        return link
 
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


def addLinkMeta(name,url,mode,iconimage,itemcount,isFolder=False):
        splitName=name.partition('(')
	simplename=""
	simpleyear=""
	if len(splitName)>0:
                simplename=splitName[0]
		simpleyear=splitName[2].partition(')')
	if len(simpleyear)>0:
		simpleyear=simpleyear[0]
	mg = metahandlers.MetaData()
	meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
	liz.setInfo( type="Video", infoLabels= meta )
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
	else: liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
	return ok
	
def addDir(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
    
def YOUTUBE_PLAYLIST(url):

    link = open_url(url)
    match = re.compile('yt-lockup-playlist yt-lockup-grid"(.+?)<div class="yt-lockup-meta">').findall(link)
    for links in match:
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        icon = re.compile ('data-thumb="(.+?)"').findall(links)[0].replace('&amp;', '&')
        title = re.compile ('<div class="yt-lockup-content">.+?title="(.+?)"').findall(links)[0]
        title = CLEANUP(title)
        if not 'http' in url:
            url1 = 'https://www.youtube.com/' + url
            addDir("[COLOR yellow][B]" + title + "[/B][/COLOR]",url1,43,icon,fanart)
    SET_VIEW()

def YOUTUBE_PLAYLIST_PLAY(url):

    link = open_url(url)
    match = re.compile('<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">').findall(link)
    for links in match:
        title = re.compile ('video-title="(.+?)"',re.DOTALL).findall(links)[0]
        title = CLEANUP(title)
        icon = re.compile ('url="(.+?)"',re.DOTALL).findall(links)[0].replace('&amp;', '&')
        fanart = re.compile ('url="(.+?)"',re.DOTALL).findall(links)[0].replace('&amp;', '&')
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        if not 'http' in url:
            if not 'Deleted video' in title:
                url1 = 'https://www.youtube.com' + url
                addLink("[COLOR yellow][B]" + title + "[/B][/COLOR]",url1,2,icon,fanart)
                
        
def TEAMNEWS():

    url = 'http://www.worldfootball.net/teams/liverpool-fc/'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="wfb-news-medium">(.+?)<script type="text/javascript">').findall(link)[0]
    grab = re.compile ('<img src="(.+?)".+?<a href="(.+?)" title="(.+?)"').findall(match)
    for icon,url,title in grab:
        if not 'http' in url:
            url = 'http://www.worldfootball.net' + url
            addLink("[COLOR yellow][B]" + title + "[/B][/COLOR]",url,19,icon,fanarts)

def READNEWS(url):

    link = open_url(url)
    match = re.compile('<div class="wfb-news-content">(.+?)</div>').findall(link)[0].replace('<p>', '').replace('</p>', '').replace('"', '')
    heading = AddonTitle
    showText(heading,match)
    
def showText(heading, text):

    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except: pass

def addItem(name,url,mode,iconimage,fanart, description=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def SHOW_PICTURE(url):

    SHOW = "ShowPicture(" + url + ')'
    xbmc.executebuiltin(SHOW)
    sys.exit(1)

def find_single_match(text,pattern):

    result = ""
    try:    
        single = re.findall(pattern,text, flags=re.DOTALL)
        result = single[0]
    except:
        result = ""

    return result

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
	try:
	    xbmc.sleep(10)
	    retry -= 1
	    win.getControl(1).setLabel(heading)
	    win.getControl(5).setText(text)
	    return
	except:
	    pass

def view(link):
        try:
                match= re.compile('<layouttype>(.+?)</layouttype>').findall(link)[0]
                if layout=='thumbnail': xbmc.executebuiltin('Container.SetViewMode(500)')              
                else:xbmc.executebuiltin('Container.SetViewMode(50)')  
        except:pass

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
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
 
if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:GetContent(name,url,iconimage,fanart)
elif mode==2:PLAYLINK(name,url,iconimage)
elif mode==3:GETMULTI(name,url,iconimage)
elif mode==4:PLAYSD(name,url,iconimage)
elif mode==5:SEARCH()
elif mode==6:YOUTUBE_CHANNEL(url)
elif mode==7:PLAYVIDEO(url)
elif mode==8:GETMULTI_SD(name,url,iconimage)
elif mode==9:SHOW_PICTURE(url)
elif mode==10:anfield_index(url)
elif mode==11:anfield_menu()
elif mode==17:resolver_settings()
elif mode==18:TEAMNEWS()
elif mode==19:READNEWS(url)

elif mode==42:YOUTUBE_PLAYLIST(url)
elif mode==43:YOUTUBE_PLAYLIST_PLAY(url)
elif mode==68:SCRAPE_SPORTSHIGHLIGHTS_GAMES()
elif mode==69:SCRAPE_SPORTSHIGHLIGHTS_LINKS(url)
elif mode==71:YOUTUBE_CHANNEL(url)
elif mode==72:YOUTUBE_CHANNEL_PART2(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
