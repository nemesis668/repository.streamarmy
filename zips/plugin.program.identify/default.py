import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,json,os,re,sys,datetime,time,shutil,random,hashlib,urlresolver,liveresolver
from resources.libs.common_addon import Addon
import base64
import HTMLParser
from metahandler import metahandlers
import os


addon_id        = 'plugin.program.identify'
addon           = Addon(addon_id, sys.argv)
selfAddon       = xbmcaddon.Addon(id=addon_id)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
iconimage       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
nextpage        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.jpg'))
CustomDialog    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'resources/skins/DefaultSkin/1080i/default.xml'))
baseurl         = base64.b64decode(b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3JWRWlZSEtZ')
metaset         = selfAddon.getSetting('enable_meta')
ADDON_FOLDER    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id))
DATA_FOLDER     = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id))
FAVOURITES_FILE = xbmc.translatePath(os.path.join(DATA_FOLDER , 'favourites.xml'))
dialog          = xbmcgui.Dialog()
dp              = xbmcgui.DialogProgress()
AddonTitle      = "[COLOR gold][B]Identify[/B][/COLOR]"

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
    text = text.replace('&apos;',"'")
    text = text.lstrip(' ')
    text = text.lstrip('    ')

    return text
    

def GetMenu():

    xbmc.executebuiltin('Container.SetViewMode(500)')
    url = baseurl     
    link=open_url(baseurl)
    match= re.compile('<item>(.+?)</item>').findall(link)

    for item in match:
        try:
            if '<folder>'in item:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url2=re.compile('<folder>(.+?)</folder>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                addDir(name,url2,1,iconimage,fanart)
            elif '<people>' in item:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                url=re.compile('<people>(.+?)</people>').findall(item)[0]
                addDir(name,url,3,iconimage,fanart)
            elif '<image>' in item:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                url=re.compile('<image>(.+?)</image>').findall(item)[0]
                addDir(name,url,8,iconimage,fanart)
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
                        addLink(name,url2,5,iconimage,fanart)
        
        
        except:pass
    SET_VIEW()
    
    
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
            elif '<image>' in item:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                url=re.compile('<image>(.+?)</image>').findall(item)[0]
                addDir(name,url,8,iconimage,fanart)
            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                addItem(name,url2,2,iconimage,fanart)
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
                    addLink(name,url2,5,iconimage,fanart)
        except:pass
    SET_VIEW()
 

def _get_keyboard( default="", heading="", hidden=False ):
    keyboard = xbmc.Keyboard( default, heading, hidden )
    keyboard.doModal()
    if ( keyboard.isConfirmed() ):
        return unicode( keyboard.getText(), "utf-8" )
    return default


    
def addDir(name,url,mode,iconimage,fanart,description='',cm=None):

    if cm == None: cm = []
    if not "http" in iconimage:
        iconimage = icon
    if not "http" in fanart:
        fanart = fanarts
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanart )
    liz.setProperty( "icon_Image", iconimage )
    liz.addContextMenuItems(items=cm, replaceItems=False)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
    
def addLink(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' not in url:
        liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def addLinkRegex(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
    
def addItem(name,url,mode,iconimage,fanart, description=''):

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty( "Fanart_Image", fanart )
    if 'plugin://' not in url:
        liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
    
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
    
def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
        response = urllib2.urlopen(req, timeout=5)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        # print link
        return link
    except:quit()
    
def open_url2(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    return link
    
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
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif codename == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')
    
    
def PLAYLINK(name,url,iconimage):

    if not'http'in url:url='http://'+url
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



    if "plugin://" in url:
        url = "PlayMedia("+url+")"
        xbmc.executebuiltin(url)
        quit()

    if urlresolver.HostedMediaFile(url).valid_url(): 
        stream_url = urlresolver.HostedMediaFile(url).resolve()
    elif liveresolver.isValid(url)==True: 
        stream_url=liveresolver.resolve(url)
    else: stream_url=url
    liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                                    
def PLAYSD(name,url,iconimage):
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    xbmc.Player ().play(url, liz, False)
    
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
    name='[COLOR silver]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        url = streamurl[select]
        # print url
        if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
        elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
        else: stream_url=url
        liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
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
            
def SHOW_PICTURE(url):

    SHOW = "ShowPicture(" + url + ')'
    xbmc.executebuiltin(SHOW)
    sys.exit(1)
 
def TextBox(title, msg, iconimage):
    class TextBoxes(xbmcgui.WindowXMLDialog):
        def onInit(self):
            self.title      = 100
            self.msg        = 101
            self.okbutton   = 102
            self.scrollbar  = 104

            self.showdialog()

        def showdialog(self):
        
            self.getControl(self.title).setLabel(title)
            self.getControl(self.msg).setText(msg)
            self.setFocusId(self.scrollbar)

            
        def onClick(self, controlId):
            if (controlId == self.okbutton):
                self.close()
    
    with open(CustomDialog, "r") as file: content = file.read()
    
    content = re.sub('<texture border="3">(.+?)</texture>','<texture border="3">'+iconimage+'</texture>', content)
    with open(CustomDialog, "w") as file: file.write(content)
    tb = TextBoxes( "default.xml" , xbmcaddon.Addon(id=addon_id).getAddonInfo('path'), 'DefaultSkin', title=title, msg=msg)
    tb.doModal()
    del tb

def PEOPLE(url):

    
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    masterurl = 'http://missingpersons.police.uk'
    match = re.compile ('<li class="Highlight">(.+?)</ul>').findall(link)
    for links in match:
        try:
            icon = re.compile('<img src="(.+?)"').findall(links)[0]
        except: icon = "Null"
        url = re.compile('<a href="(.+?)"').findall(links)[0]
        location = re.compile('<li>(.+?)</li>').findall(links)[0]
        location = CLEANUP(location)
        date = re.compile('<li>(.+?)</li>').findall(links)[2]
        age = re.compile('<li>(.+?)</li>').findall(links)[3]
        if not 'http' in url:
            iconimage = masterurl + icon   
            url1 = masterurl + url
            addDir("[COLOR gold]" + location + " :: " + "Age = (" + age + ") Date :: " + date + "[/COLOR]",url1,4,iconimage,fanart)
    try:
        np = re.compile('<li><a href=\"([^"]*)\" class="next"', re.DOTALL).findall(link)[0]
        newpage = masterurl + np
        addDir("[COLOR red]" + "Next Page -->" + "[/COLOR]",newpage,3,nextpage,fanart)
        
    except:pass       
   
    SET_VIEW()
    
def PEOPLE_INFO(url,iconimage):
    
    
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    image = re.compile ('<div class="ImageGrid">(.+?)</div>').findall(link)[0]
    try:
        image1 = re.compile ('<a href="(.+?)"').findall(image)[0]
    except: image1 = "null"
    iconimage = 'http://missingpersons.police.uk' + image1
    casematch = re.compile ('<div class="Case-Profile">(.+?)</h1>').findall(link)[0]
    caseid = re.compile ('<span>(.+?)</span>').findall(casematch)[0]
    match = re.compile ('<div class="Col Col2_1">(.+?)<div class="Col Col2_2">').findall(link)
    for links in match:
            #try:
            try:
                gender = re.compile ('<td>(.+?)</td>').findall(links)[0]
            except:pass
            try:
                age = re.compile ('<td>(.+?)</td>').findall(links)[1]
            except:pass
            try:
                ethnicity = re.compile ('<td>(.+?)</td>').findall(links)[2]
            except:pass
            try:
                height = re.compile ('<td>(.+?)</td>').findall(links)[3]
                height = height.strip()
            except:pass
            try:
                build = re.compile ('<td>(.+?)</tr>').findall(links)[4]
                if len(build) > 6:
                    build = build.replace('</td>', '')
            except:pass
            try:
                datefound = re.compile ('<td>(.+?)</td>').findall(links)[5]
            except:pass
            try:
                estimatedeath = re.compile ('<td>(.+?)</tr>').findall(links)[6]
                if len(estimatedeath) > 6:
                    estimatedeath = estimatedeath.replace('</td>', '')
            except:pass
            try:
                bodyorremains = re.compile ('<td>(.+?)</td>').findall(links)[7]
            except:pass
            try:
                circumstances = re.compile ('<p>(.+?)</p>',re.DOTALL).findall(links)[0]
                circumstances = CLEANUP(circumstances)
            except:pass
            try:
                posessions = re.compile ('<strong>Possessions</strong><p>(.+?)</p>').findall(links)[0]
                posessions = posessions.strip()
                posessions = CLEANUP(posessions)
            except:
                posessions = "None"
            try:
                TextBox("[COLOR white]Identify[/COLOR]","[B]" "[COLOR aqua]" + "Case ID = " + caseid  + "\n" + "[COLOR gold]" + "Sex = " + "[COLOR white]" + gender + "\n" + "[COLOR gold]" + "Approx Age = " 
                        + "[COLOR white]" + age + "\n" + "[COLOR gold]" + "Ethnicity = " + "[COLOR white]" + ethnicity + "\n" + "[COLOR gold]" + "Height = " + "[COLOR white]" + height + "\n" + "[COLOR gold]" +
                        "Build = " + "[COLOR white]" + build + "\n" + "[COLOR gold]" + "Date Found = " + "[COLOR white]" + datefound + "\n" + "[COLOR gold]" + "Estimated Date Of Death = " + "[COLOR white]" + 
                        estimatedeath + "\n" + "[COLOR gold]" + "Body/Remains Found = " + "[COLOR white]" + bodyorremains + "\n" + "\n" + "[COLOR gold]" + 
                        "Circumstances = " + "[COLOR white]" + circumstances + "\n" + "\n" + "[COLOR gold]" + "Possesions Found With = " + "[COLOR white]" + posessions + "[/COLOR]" "[/B]",iconimage)
            except:pass
    quit()
                                    
params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None; fanart=None
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
elif mode==3:PEOPLE(url)
elif mode==4:PEOPLE_INFO(url,iconimage)
elif mode==5:GETMULTI(name,url,iconimage)
elif mode==7:PLAYSD(name,url,iconimage)
elif mode==8:SHOW_PICTURE(url)
elif mode==999:URL_RESOLVER_SEND_HERE(url)




##Debug String
##dialog.ok("Debug", str (url))
if mode==None or url==None or len(url)<1: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=False)
else: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)

