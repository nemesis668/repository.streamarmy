#################################################################
#                     STREAM ARMY BASE CODE                     # 
#                                                               #
#                     Created By @Nemzzy668                     #
#         Feel Free to use any of this code to learn            #

import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,uuid,os,re,sys,base64,json,time,shutil,urlresolver,random,liveresolver,hashlib
from resources.libs.modules import cfscrape
from resources.libs.modules import gofetch
from resources.libs.modules import satools
from resources.libs.common_addon import Addon
from metahandler import metahandlers
from HTMLParser import HTMLParser
from datetime import datetime


addon_id            = 'plugin.video.streamarmy'
addon               = Addon(addon_id, sys.argv)
selfAddon           = xbmcaddon.Addon(id=addon_id)
AddonTitle          = '[COLOR yellow]Stream Army[/COLOR]'
addonPath           = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'plugin.video.streamarmy')
fanarts             = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
dp                  = xbmcgui.DialogProgress()
adultpass           = selfAddon.getSetting('pass')
dialog              = xbmcgui.Dialog()
baseurl             = base64.b64decode(b'aHR0cDovL3N0cmVhbWFybXkuY28udWsvTWFpbi9NYWluLnhtbA==') # Live URL
#baseurl             = base64.b64decode(b'aHR0cDovLzEyNy4wLjAuMS9NYWluL01haW4ueG1s') # Dev Url
F4M_TESTER          = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.f4mTester'))
F4M_PROXY           = xbmc.translatePath(os.path.join('special://home/addons/script.video.F4mProxy'))
SPORTSDEVIL         = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.SportsDevil'))
intro_done          = xbmc.translatePath('special://home/addons/plugin.video.streamarmy/intro')


def GetMenu():
    
    satools.SOCCERSTREAMS_CHECK()
    gettime = int(datetime.now().strftime('%H%M'))
    if (gettime >= 0000) and (gettime <= 1159): a = "Morning"
    elif (gettime >= 1200) and (gettime <= 1759): a = "Afternoon"
    else: a = "Evening"
    satools.addLink ('[COLOR yellow]Good[COLOR red] ' + str(a) + '[COLOR white] From [COLOR yellow]@Nemzzy668[/COLOR][COLOR white] and [COLOR yellow]@_Manc_ [COLOR white] and [COLOR yellow]@LordJD927 [/COLOR]' ,'url','12',icon,fanarts)
    try:
        file = xbmc.translatePath("special://home/userdata/addon_data/script.module.urlresolver/settings.xml")
        a=open(file).read()
        real = re.compile ('<setting id="RealDebridResolver_token"(.+?)/').findall(a)[0]
        real = real.strip()
        url = 'plugin://script.module.urlresolver/?mode=auth_rd'
        icondeb = 'http://i.imgur.com/GSKPJuD.png'
        if 'value=""' in real:
            result = ('[COLOR red]Real Debrid Not Active Click To Pair[/COLOR]')
            satools.addLink('[B][COLOR yellow]D[COLOR white]ebrid Status : '+str(result)+'[/COLOR]''[/B]',url,2,icondeb,fanarts)
        else:
            result = ('[COLOR yellow]Real Debrid Active[/COLOR]')
            satools.addLink('[B][COLOR yellow]D[COLOR white]ebrid Status : '+str(result)+'[/COLOR]''[/B]','url',999,icondeb,fanarts)
    except:pass
    if baseurl =='http://127.0.0.1/Main/Main.xml':
        satools.addLink("[B][COLOR yellow]" + "YOUR IN DEV MODE" + "[/COLOR][/B]",'url',999,icon,fanarts)
    satools.popup()
    satools.addLink("[B][COLOR yellow]" + "-------------------------------------------------------------------------" + "[/COLOR][/B]",'url',999,icon,fanarts)
    url = baseurl     
    link=satools.open_url(baseurl)
    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:
            if '<m3u>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                    satools.addDir(name,url,11,iconimage,fanart)
            elif '<livetv>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<livetv>(.+?)</livetv>').findall(item)[0]
                    satools.addDir(name,url,14,iconimage,fanart)
            elif '<playlist>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                        satools.addDir(name,url,43,iconimage,fanart)
            elif '<transfers>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<transfers>(.+?)</transfers>').findall(item)[0]
                        satools.addDir(name,url,79,iconimage,fanart)
            elif '<sportsdevil>' in item:
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
                         satools.addItem(name,url,4,iconimage,fanart)   
                    elif len(links)>1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                         fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                         satools.addItem(name,url2,8,iconimage,fanart)

            elif '<folder>'in item:
                
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url2=re.compile('<folder>(.+?)</folder>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                satools.addDir(name,url2,1,iconimage,fanart)
                
            else:
                
                links=re.compile('<link>(.+?)</link>').findall(item)
                if len(links)==1:
                    data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                    lcount=len(match)
                    for name,url,iconimage,fanart in data:
                        if 'youtube.com/playlist' in url:
                            satools.addDir(name,url,2,iconimage,fanart)
                        else:
                            satools.addLink(name,url,2,iconimage,fanart)
                elif len(links)>1:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        satools.addLink(name,url2,3,iconimage,fanart)
    if not os.path.exists(intro_done):
        intro = 'http://streamarmy.co.uk/intro.mp4'
        xbmc.Player().play(intro, xbmcgui.ListItem('Welcome to StreamArmy'))
        os.makedirs(intro_done)
    satools.SET_VIEW()    
    
def GetContent(name,url,iconimage,fanart):
    dialog = xbmcgui.Dialog()
    url2=url
    link=satools.open_url(url)

    if 'XXX>yes</XXX' in link:
        password = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.streamarmy/settings.xml')
        a=open(password).read()
        try:
            adultpass = re.compile ('<setting id="pass" value="(.+?)" />').findall(a)[0]
        except IndexError:
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','OK')
            if ret == 1:
                keyb = xbmc.Keyboard('', 'Set Password')
                keyb.doModal()
            if (keyb.isConfirmed()):
                passw = keyb.getText()
                selfAddon.setSetting('pass',passw)
                dialog.ok(AddonTitle, "We will now exit, please re select the menu and enter the password you just set")
                quit()


        if adultpass <> '':
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Adult Content', 'Please enter the password you set','to continue','','Cancel','OK')
            if ret == 1:    
                keyb = xbmc.Keyboard('', 'Enter Password')
                keyb.doModal()
            if (keyb.isConfirmed()):
                passw = keyb.getText()
            if passw <> adultpass:
                quit()
        
        else:quit()

    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:
        try:
            if '<regex>' in item:
                regdata = re.compile('(<regex>.+?</regex>)', re.MULTILINE|re.DOTALL).findall(item)
                regdata = ''.join(regdata)
                reglist = re.compile('(<listrepeat>.+?</listrepeat>)', re.MULTILINE|re.DOTALL).findall(regdata)
                regdata = urllib.quote_plus(regdata)

                reghash = hashlib.md5()
                for i in regdata: reghash.update(str(i))
                reghash = str(reghash.hexdigest())

                item = item.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                item = re.sub('<regex>.+?</regex>','', item)
                item = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', item)
                item = re.sub('<link></link>','', item)

                name = re.sub('<meta>.+?</meta>','', item)
                try: name = re.findall('<title>(.+?)</title>', name)[0]
                except: name = re.findall('<name>(.+?)</name>', name)[0]

                try: date = re.findall('<date>(.+?)</date>', item)[0]
                except: date = ''
                if re.search(r'\d+', date): name += ' [COLOR red] Updated %s[/COLOR]' % date

                try: image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                except: image2 = icon

                try: fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                except: fanart2 = fanarts

                try: meta = re.findall('<meta>(.+?)</meta>', item)[0]
                except: meta = '0'

                try: url = re.findall('<link>(.+?)</link>', item)[0]
                except: url = '0'
                url = url.replace('>search<', '><preset>search</preset>%s<' % meta)
                url = '<preset>search</preset>%s' % meta if url == 'search' else url
                url = url.replace('>searchsd<', '><preset>searchsd</preset>%s<' % meta)
                url = '<preset>searchsd</preset>%s' % meta if url == 'searchsd' else url
                url = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', url)

                if not regdata == '':
                    hash.append({'regex': reghash, 'response': regdata})
                    url += '|regex=%s' % regdata

                satools.addLinkRegex(name,url,10,image2,fanart2,"")
            
            elif '<image>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<image>(.+?)</image>').findall(item)[0]
                    satools.addDir(name,url,9,iconimage,fanart)
            elif '<soccer>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<soccer>(.+?)</soccer>').findall(item)[0]
                    satools.addDir(name,url,12,iconimage,fanart)
            elif '<livetv>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<livetv>(.+?)</livetv>').findall(item)[0]
                    satools.addDir(name,url,14,iconimage,fanart)
            elif '<tvguide>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<tvguide>(.+?)</tvguide>').findall(item)[0]
                    satools.addDir(name,url,16,iconimage,fanart)
            elif '<iptv>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<iptv>(.+?)</iptv>').findall(item)[0]
                    satools.addDir(name,url,21,iconimage,fanart)
            elif '<trendingtv>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<trendingtv>(.+?)</trendingtv>').findall(item)[0]
                    satools.addDir(name,url,23,iconimage,fanart)
            elif '<mama>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<mama>(.+?)</mama>').findall(item)[0]
                    satools.addDir(name,url,24,iconimage,fanart)
            elif '<sportschans>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<sportschans>(.+?)</sportschans>').findall(item)[0]
                    satools.addDir(name,url,25,iconimage,fanart)
            elif '<tvsearch>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<tvsearch>(.+?)</tvsearch>').findall(item)[0]
                    satools.addDir(name,url,26,iconimage,fanart)
            elif '<disney>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<disney>(.+?)</disney>').findall(item)[0]
                    satools.addDir(name,url,27,iconimage,fanart)
            elif '<cinema>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<cinema>(.+?)</cinema>').findall(item)[0]
                    satools.addDir(name,url,29,iconimage,fanart)
            elif '<3d>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<3d>(.+?)</3d>').findall(item)[0]
                    satools.addDir(name,url,32,iconimage,fanart)
            elif '<multisearch>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<multisearch>(.+?)</multisearch>').findall(item)[0]
                    satools.addDir(name,'None',34,iconimage,fanart)
            elif '<genres>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<genres>(.+?)</genres>').findall(item)[0]
                    satools.addDir(name,url,37,iconimage,fanart)
            elif '<years>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<years>(.+?)</years>').findall(item)[0]
                    satools.addDir(name,url,40,iconimage,fanart)
            elif '<youtube>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<youtube>(.+?)</youtube>').findall(item)[0]
                    satools.addDir(name,url,42,iconimage,fanart)
            elif '<playlist>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                    satools.addDir(name,url,43,iconimage,fanart)
            elif '<youtubelive>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<youtubelive>(.+?)</youtubelive>').findall(item)[0]
                    satools.addDir(name,url,44,iconimage,fanart)
            elif '<cctv>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<cctv>(.+?)</cctv>').findall(item)[0]
                    satools.addDir(name,url,46,iconimage,fanart)
            elif '<replays>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<replays>(.+?)</replays>').findall(item)[0]
                    satools.addDir(name,url,49,iconimage,fanart)
            elif '<docs>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<docs>(.+?)</docs>').findall(item)[0]
                    satools.addDir(name,url,52,iconimage,fanart)
            elif '<docs3d>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<docs3d>(.+?)</docs3d>').findall(item)[0]
                    satools.addDir(name,url,54,iconimage,fanart)
            elif '<radio>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<radio>(.+?)</radio>').findall(item)[0]
                    satools.addDir(name,url,56,iconimage,fanart)
            elif '<audiobooks>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<audiobooks>(.+?)</audiobooks>').findall(item)[0]
                    satools.addDir(name,url,59,iconimage,fanart)
            elif '<vrporn>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<vrporn>(.+?)</vrporn>').findall(item)[0]
                    satools.addDir(name,url,62,iconimage,fanart)
            elif '<pornhd>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<pornhd>(.+?)</pornhd>').findall(item)[0]
                    satools.addDir(name,url,65,iconimage,fanart)
            elif '<porncom>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<porncom>(.+?)</porncom>').findall(item)[0]
                    satools.addDir(name,url,68,iconimage,fanart)
            elif '<youtubechan>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<youtubechan>(.+?)</youtubechan>').findall(item)[0]
                    satools.addDir(name,url,71,iconimage,fanart)
            elif '<musicvids>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<musicvids>(.+?)</musicvids>').findall(item)[0]
                    satools.addDir(name,url,73,iconimage,fanart)
            elif '<pawpatrol>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<pawpatrol>(.+?)</pawpatrol>').findall(item)[0]
                    satools.addDir(name,url,76,iconimage,fanart)
            elif '<eporner>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<eporner>(.+?)</eporner>').findall(item)[0]
                    satools.addDir(name,url,81,iconimage,fanart)
            elif '<sportsdevil>' in item:
                    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                    if len(links)==1:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        try:
                            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        except: iconimage = icon
                        try:
                            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]            
                        except: fanart = fanarts
                        url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                        try:
                            referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                        except: referer = url
                        check = referer
                        suffix = "/"
                        if not check.endswith(suffix):
                            refer = check + "/"
                        else:
                            refer = check
                        link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+str(name)+'%26url=' + url
                        url = link + '%26referer=' +refer
                        satools.addLink(name,url,4,iconimage,fanart)   
                    elif len(links)>1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                         fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                         satools.addItem(name,url2,8,iconimage,fanart)

            elif '<folder>'in item:
                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                for name,url,iconimage,fanart in data:
                        satools.addDir(name,url,1,iconimage,fanart)

            else:
                links=re.compile('<link>(.+?)</link>').findall(item)
                if len(links)==1:
                    data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                    lcount=len(match)
                    for name,url,iconimage,fanart in data:
                        if 'youtube.com/playlist' in url:
                            satools.addDir(name,url,2,iconimage,fanart)
                        else:
                            satools.addLink(name,url,2,iconimage,fanart)
                elif len(links)>1:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    satools.addLink(name,url2,3,iconimage,fanart)
        except:pass
    satools.SET_VIEW()
    
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
elif mode==2:satools.PLAYLINK(name,url,iconimage)
elif mode==3:satools.GETMULTI(name,url,iconimage)
elif mode==4:satools.PLAYSD(name,url,iconimage)
elif mode==5:satools.PLAY_SOCCERSTREAMS(url)
elif mode==7:satools.PLAYVIDEO(url)
elif mode==8:satools.GETMULTI_SD(name,url,iconimage)
elif mode==9:satools.SHOW_PICTURE(url)
elif mode==11:satools.GET_M3U(name,url,iconimage)
elif mode==887:satools.SHOW_PICTURE(url)
else: gofetch.getscraper(mode,url,name,iconimage,fanart)

if mode==None or url==None or len(url)<1: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=False)
else: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)

## dialog.ok("Debug", str (next_page))