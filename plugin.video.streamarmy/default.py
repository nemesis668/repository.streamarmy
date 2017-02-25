import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,shutil,urlresolver,random,liveresolver,hashlib
from resources.libs.common_addon import Addon
from resources.libs.modules import regex
import base64
from metahandler import metahandlers

import os


addon_id        = 'plugin.video.streamarmy'
addon           = Addon(addon_id, sys.argv)
selfAddon       = xbmcaddon.Addon(id=addon_id)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
searchicon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'search.jpg'))
nextpage        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.png'))
sd_path         = xbmc.translatePath(os.path.join('special://home/addons/', 'plugin.video.sportsdevil'))
baseurl         = base64.b64decode(b'aHR0cDovL3d3dy5zdHJlYW1hcm15LmNvLnVrL01haW4vTWVudS54bWw=')
ytpl            = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
ytpl2           = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
ytplpg1         = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
ytplpg2         = '&part=snippet&playlistId='
ytplpg3         = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
adultpass       = selfAddon.getSetting('password')
conpass         = selfAddon.getSetting('Conspiracy Password')
metaset         = selfAddon.getSetting('enable_meta')
messagetext     = 'http://streamarmy.co.uk/Main/update.txt'
RUNNER          = base64.b64decode(b'aHR0cDovL2dldGFmbGl4LnVzL2FkZG9uL3lvdXR1YmUucGhw')
#SEARCH_LIST     = 'http://streamarmy.co.uk/Main/searchtext.xml'
dialog          = xbmcgui.Dialog()
dp              = xbmcgui.DialogProgress()
NON_ENCRYPTED_URL = 'http://www.streamarmy.co.uk/Main/Exceptions/Exceptions.xml'
AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"
url_reolver_supports = ["aliez","alldebrid","allvid","anistream","anyfiles","apnasave","blazefile","castamp","clicknupload","cloudmailru","cloudy","daclips","dailymotion","divxstage","ecostream","estream","exashare","facebook","fastplay","filepup","fileweed","flashx","googlevideo","gorillavid","grifthost","hugefiles","indavideo","jetload","kingfiles","letwatch","letwatch","mailru","megadebrid","megamp","mersalaayitten","movdivx","movpod","movshare","mpengine","mpstream","mpupload","myvidstream","nosvideo","novamov","nowvideo","ok","ol_gmu","ol_openload","play_net","play_playedto","playhd","playwire","premiumize_me","purevid","putload","rapidvideo","rapidvideocom","realdebrid","rpnet","rutube","simplydebrid","speedplay","speedvideo","stagevu","streamcloud","streamenet","streaminto","streamplay","teramixer","thevid","thevideo","thevideos","trollvid","tudou","tunepk","tusfiles","twitch","uploadaf","uploadx","uploadz","uptobox","userscloud","usersfiles","veeHD","veeHD","oveoh","vidabc","vidcrazynet","videa","videobee","videocloud","videoget","videohut","videoraj","videorev","videoweed","videowood","videozoo","vidlox","vidmad","vidme","vidto","vidtodo","vidup_me","vidup_vidup_org","vidup_vidzi","vimeo","vivosx","vk","vshare","vshareeu","watchers","watchonline","watchpass","watchvideo","weshare","xvidstage","yourupload","youtube","youwatch","zevera","zstream"]

def open_exception_url(link, splitting = '\n'):
    request = urllib2.Request(link)
    try:
        response = urllib2.urlopen(request)
    except IOError:
        return []
        
    else:
        the_page = response.read()
        return the_page.split(splitting)

exception_data = open_exception_url(NON_ENCRYPTED_URL)

try:
    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
    version=float(xbmc_version[:4])

    if version >= 17.0 and version <= 17.9:

        caches = ["special://cache",
        "special://temp/",
        "/private/var/mobile/Library/Caches/AppleTV/Video/Other",
        "/private/var/mobile/Library/Caches/AppleTV/Video/LocalAndRental"]

        for folders in caches:
            if "special" in folders:
                folders = xbmc.translatePath(folders)
            if os.path.exists(folders):
                cache_dir = os.path.join(folders, "archive_cache")
                if not os.path.exists(cache_dir):
                    os.makedirs(cache_dir)
except: pass

def xor(input_data, key):
    # print '----- xor =========='
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    # print '----- encrypt =========='
    key = 0
    for ch in password:
        key ^= ((2 * ord(ch) + 3) & 0xff)

    return xor(input_data, key)

def decrypt(input_data, password="liverpool"):
    # print '----- decrypt =========='
    return encrypt(input_data, password)

def GetMenu():

        GET_VERSION =  xbmc.translatePath('special://home/addons/' + addon_id + '/addon.xml')
        a=open(GET_VERSION).read()
        b=a.replace('\n',' ').replace('\r',' ')
        match=re.compile('name=".+?".+?version="(.+?)".+?provider-name=".+?">').findall(str(b))
        for item in match:
            addon_version = item
            
        url="http://www.streamarmy.co.uk/Plugins/addons.xml"

        link = open_url(url)
        match=re.compile('<addon id="' + addon_id + '" name=".+?" version="(.+?)" provider-name=".+?">').findall(link)[0]

        addItem('[B][COLOR lime]Your Current Version: '+str(addon_version)+'[/COLOR] | [COLOR yellow]Our Latest Version: ' + match + '[/COLOR][/B]','url',999,icon,fanarts)

        popup()
        xbmc.executebuiltin('Container.SetViewMode(500)')
        url = baseurl     
        # print '------------------ first file --------------'  
        link=open_encrypted_url(baseurl)
        match= re.compile('<item>(.+?)</item>').findall(link)
        #addDir('[B][COLOR lime]S[/COLOR][COLOR red]earch[/COLOR][/B] [B][COLOR lime]S[/COLOR][COLOR red]tream Army[/COLOR][/B]',url,5,searchicon,fanarts)
        for item in match:
            try:
                if '<m3u>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                        addDir(name,url,11,iconimage,fanart)
                elif '<pornscrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<pornscrape>(.+?)</pornscrape>').findall(item)[0]
                        addDir(name,url,16,iconimage,fanart)
                elif '<docs>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<docs>(.+?)</docs>').findall(item)[0]
                        addDir(name,url,24,iconimage,fanart)
                elif '<anime>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<anime>(.+?)</anime>').findall(item)[0]
                        addDir(name,url,32,iconimage,fanart)
                elif '<cartoons>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<cartoons>(.+?)</cartoons>').findall(item)[0]
                        addDir(name,url,35,iconimage,fanart)
                elif '<comics>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<comics>(.+?)</comics>').findall(item)[0]
                        addDir(name,url,38,iconimage,fanart)
                elif '<filmon>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<filmon>(.+?)</filmon>').findall(item)[0]
                        addDir(name,url,26,iconimage,fanart)
                elif '<music>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<music>(.+?)</music>').findall(item)[0]
                        addDir(name,url,28,iconimage,fanart)
                elif '<sportsmama>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<sportsmama>(.+?)</sportsmama>').findall(item)[0]
                        addDir(name,url,12,iconimage,fanart)
                elif "<soccerstreams>" in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        url=re.compile('<soccerstreams>(.+?)</soccerstreams>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addDir(name,url,31,iconimage,fanart,'')
                elif '<channel>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                        addDir(name,url,6,iconimage,fanart)
                elif '<tvput>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<tvputsput>(.+?)</tvput>').findall(item)[0]
                        addDir(name,url,13,iconimage,fanart)
                elif '<moviescrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrape>(.+?)</moviescrape>').findall(item)[0]
                        addDir(name,url,15,iconimage,fanart)
                elif '<moviescrapenorm>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrapenorm>(.+?)</moviescrapenorm>').findall(item)[0]
                        addDir(name,url,22,iconimage,fanart)
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
                             addItem(name,url,4,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,8,iconimage,fanart)

                elif '<folder>'in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    url2=re.compile('<folder>(.+?)</folder>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]

                    if url2 in exception_data:
                        addDir(name,url2,1,iconimage,fanart)
                    else:
                        addDir(name,url2,20,iconimage,fanart)
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


def popup():
        message=open_url2(messagetext)
        if len(message)>1:
                path = xbmcaddon.Addon().getAddonInfo('path')
                comparefile = os.path.join(os.path.join(path,''), 'compare.txt')
                r = open(comparefile)
                compfile = r.read()       
                if compfile == message:pass
                else:
                    showText('[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]', message)
                    text_file = open(comparefile, "w")
                    text_file.write(message)
                    text_file.close()
   
def GetContent(name,url,iconimage,fanart):
        url2=url
        link=open_url(url)
        if 'XXX>yes</XXX' in link:
            if adultpass == '':
                dialog = xbmcgui.Dialog()
                ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','OK')
                if ret == 1:
                    keyb = xbmc.Keyboard('', 'Set Password')
                    keyb.doModal()
                if (keyb.isConfirmed()):
                    passw = keyb.getText()
                    selfAddon.setSetting('password',passw)
                else:quit()
                    
        if 'XXX>yes</XXX' in link:
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

        if 'con>yes</con' in link:
            if conpass == '':
                dialog = xbmcgui.Dialog()
                ret = dialog.yesno('Conspiracy Content', 'You have opted to show Conspiracy content','','Due to the Nature of Content ,Please set a password to prevent accidental access','Cancel','OK')
                if ret == 1:
                    keyb = xbmc.Keyboard('', 'Set Password')
                    keyb.doModal()
                if (keyb.isConfirmed()):
                    passwo = keyb.getText()
                    selfAddon.setSetting('Conspiracy Password',passwo)
                else:quit()
                    
        if 'con>yes</con' in link:
            if conpass <> '':
                dialog = xbmcgui.Dialog()
                ret = dialog.yesno('Conspiracy Content', 'Please enter the password you set','to continue','','Cancel','OK')
                if ret == 1:    
                    keyb = xbmc.Keyboard('', 'Enter Password')
                    keyb.doModal()
                if (keyb.isConfirmed()):
                    passwo = keyb.getText()
                if passwo <> conpass:
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

                    addLinkRegex(name,url,10,image2,fanart2,"")
                
                elif '<sportsmama>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<sportsmama>(.+?)</sportsmama>').findall(item)[0]
                        addDir(name,url,12,iconimage,fanart)
                elif "<soccerstreams>" in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        url=re.compile('<soccerstreams>(.+?)</soccerstreams>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addDir(name,url,31,iconimage,fanart,'')
                elif '<m3u>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                        addDir(name,url,11,iconimage,fanart)
                elif '<anime>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<anime>(.+?)</anime>').findall(item)[0]
                        addDir(name,url,32,iconimage,fanart)
                elif '<comics>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<comics>(.+?)</comics>').findall(item)[0]
                        addDir(name,url,38,iconimage,fanart)
                elif '<cartoons>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<cartoons>(.+?)</cartoons>').findall(item)[0]
                        addDir(name,url,35,iconimage,fanart)
                elif '<docs>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<docs>(.+?)</docs>').findall(item)[0]
                        addDir(name,url,24,iconimage,fanart)
                elif '<filmon>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<filmon>(.+?)</filmon>').findall(item)[0]
                        addDir(name,url,26,iconimage,fanart)
                elif '<music>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<music>(.+?)</music>').findall(item)[0]
                        addDir(name,url,28,iconimage,fanart)
                elif '<pornscrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<pornscrape>(.+?)</pornscrape>').findall(item)[0]
                        addDir(name,url,16,iconimage,fanart)
                elif '<tvput>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<tvput>(.+?)</tvput>').findall(item)[0]
                        addDir(name,url,13,iconimage,fanart)
                elif '<moviescrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrape>(.+?)</moviescrape>').findall(item)[0]
                        addDir(name,url,15,iconimage,fanart)
                elif '<moviescrapenorm>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrapenorm>(.+?)</moviescrapenorm>').findall(item)[0]
                        addDir(name,url,22,iconimage,fanart)
                elif '<channel>' in item:
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
                        addDir(name,iconimage,9,iconimage,fanart)
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
                             addItem(name,url,4,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,8,iconimage,fanart)
    
                elif '<folder>'in item:
                    data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                    for name,url,iconimage,fanart in data:
                        if url in exception_data:
                            addDir(name,url,1,iconimage,fanart)
                        else:
                            addDir(name,url,20,iconimage,fanart)

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


def GetEncrtptedContent(name,url,iconimage,fanart):
    
    # print "------------ In get encrypted content ------------"
    url2=url
    link = open_encrypted_url(url)

    # print "------------ open_encrypted_url complete ------------"

    if 'XXX>yes</XXX' in link:
        if adultpass == '':
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','OK')
            if ret == 1:
                keyb = xbmc.Keyboard('', 'Set Password')
                keyb.doModal()
            if (keyb.isConfirmed()):
                passw = keyb.getText()
                selfAddon.setSetting('password',passw)
            else:quit()
                
    if 'XXX>yes</XXX' in link:
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

    if 'con>yes</con' in link:
        if conpass == '':
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Conspiracy Content', 'You have opted to show Conspiracy content','','Due to the Nature of Content ,Please set a password to prevent accidental access','Cancel','OK')
            if ret == 1:
                keyb = xbmc.Keyboard('', 'Set Password')
                keyb.doModal()
            if (keyb.isConfirmed()):
                passwo = keyb.getText()
                selfAddon.setSetting('Conspiracy Password',passwo)
            else:quit()
                
    if 'con>yes</con' in link:
        if conpass <> '':
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Conspiracy Content', 'Please enter the password you set','to continue','','Cancel','OK')
            if ret == 1:    
                keyb = xbmc.Keyboard('', 'Enter Password')
                keyb.doModal()
            if (keyb.isConfirmed()):
                passwo = keyb.getText()
            if passwo <> conpass:
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

                addLinkRegex(name,url,10,image2,fanart2,"")

            elif '<sportsmama>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<sportsmama>(.+?)</sportsmama>').findall(item)[0]
                    addDir(name,url,12,iconimage,fanart)
            elif "<soccerstreams>" in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        url=re.compile('<soccerstreams>(.+?)</soccerstreams>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addDir(name,url,31,iconimage,fanart,'')
            elif '<m3u>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                    addDir(name,url,11,iconimage,fanart)
            elif '<docs>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<docs>(.+?)</docs>').findall(item)[0]
                        addDir(name,url,24,iconimage,fanart)
            elif '<anime>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<anime>(.+?)</anime>').findall(item)[0]
                        addDir(name,url,32,iconimage,fanart)
            elif '<comics>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<comics>(.+?)</comics>').findall(item)[0]
                        addDir(name,url,38,iconimage,fanart)
            elif '<cartoons>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<cartoons>(.+?)</cartoons>').findall(item)[0]
                        addDir(name,url,35,iconimage,fanart)
            elif '<music>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<music>(.+?)</music>').findall(item)[0]
                        addDir(name,url,28,iconimage,fanart)
            elif '<filmon>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<filmon>(.+?)</filmon>').findall(item)[0]
                        addDir(name,url,26,iconimage,fanart)
            elif '<tvput>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<tvput>(.+?)</tvput>').findall(item)[0]
                    addDir(name,url,13,iconimage,fanart)
            elif '<pornscrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<pornscrape>(.+?)</pornscrape>').findall(item)[0]
                        addDir(name,url,16,iconimage,fanart)
            elif '<moviescrape>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrape>(.+?)</moviescrape>').findall(item)[0]
                        addDir(name,url,15,iconimage,fanart)
            elif '<moviescrapenorm>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviescrapenorm>(.+?)</moviescrapenorm>').findall(item)[0]
                        addDir(name,url,22,iconimage,fanart)
            elif '<moviessearch>yes</moviessearch>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addDir(name,'url',23,iconimage,fanart)
            elif '<channel>' in item:
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
                    addDir(name,iconimage,9,iconimage,fanart)
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
                        addItem(name,url,4,iconimage,fanart)   
                    elif len(links)>1:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addItem(name,url2,8,iconimage,fanart)

            elif '<folder>'in item:
                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                for name,url,iconimage,fanart in data:
                    if url in exception_data:
                        addDir(name,url,1,iconimage,fanart)
                    else:
                        addDir(name,url,20,iconimage,fanart)
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



        
# def YOUTUBE_CHANNEL(url):

    # CHANNEL = RUNNER + url
    # link = open_url(CHANNEL)
    # patron = "<video>(.*?)</video>"
    # videos = re.findall(patron,link,re.DOTALL)

    # items = []
    # for video in videos:
        # item = {}
        # item["name"] = find_single_match(video,"<name>([^<]+)</name>")
        # item["url"] = base64.b64decode(b"cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9") + find_single_match(video,"<id>([^<]+)</id>")
        # item["author"] = find_single_match(video,"<author>([^<]+)</author>")
        # item["iconimage"] = find_single_match(video,"<iconimage>([^<]+)</iconimage>")
        # item["date"] = find_single_match(video,"<date>([^<]+)</date>")
        
        # addLink('[COLOR white]' + item["name"] + ' - on ' + item["date"] + '[/COLOR]',item["url"],7,item["iconimage"],fanart)
        
        
def GET_REGEX(name,url,iconimage):

    r, x = re.findall('(.+?)\|regex=(.+?)$', url)[0]
    r += urllib.unquote_plus(x)
    url = regex.resolve(r)

    PLAYREGEX(name,url,iconimage)

    
def SEARCH():
    keyb = xbmc.Keyboard('', '[COLOR lime]S[/COLOR][COLOR white]earch[/COLOR] [B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B]')
    keyb.doModal()
    if (keyb.isConfirmed()):
        searchterm=keyb.getText()
        searchterm=searchterm.upper()
    else:quit()
    link=open_url(SEARCH_LIST)
    slist=re.compile('<link>(.+?)</link>').findall(link)
    for url in slist:
        url2=url
        link=open_encrypted_url(url)
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
                        
        
def GET_M3U(name,url,iconimage):

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    response=link
    response = response.replace('#AAASTREAM:','#A:')
    response = response.replace('#EXTINF:','#A:')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
    li = []
    for params, display_name, url in matches:
        item_data = {"params": params, "display_name": display_name, "url": url}
        li.append(item_data)
    list = []
    for channel in li:
        item_data = {"display_name": channel["display_name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        list.append(item_data)
    for channel in list:
        name = GetEncodeString(channel["display_name"])
        url = GetEncodeString(channel["url"])
        url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
        addLinkRegex(name ,url, 2, icon, fanart,'')
        
        
        
def GETMULTI(name,url,iconimage):
    streamurl=[]
    streamname=[]
    streamicon=[]
    link=open_encrypted_url(url)
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
    name='[COLOR lime]'+name+'[/COLOR]'
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


def SCRAPE_SPORTSMAMA(url):

    try:
        link=open_url(url).replace('\n','').replace('\t','')
        name=url.split('/')[2]
        name=name.replace('.html','')
        allgames=re.compile('<div class="schedule">(.+?)<br><div id="pagination">').findall(link)[0]
        livegame=re.compile('<a href="(.+?)">.+?<img src="(.+?)"></div>.+?<div class="home cell">.+?<span>(.+?)</span>.+?<span>(.+?)</span>.+?</a>').findall(allgames)
        for url,iconimage,home,away in livegame:
            url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
            addLink(home + ' vs ' + away,url,2,iconimage,fanarts,'')
    except:
        dialog.ok("Stream Army", "Damn, No Links available at the moment, come back closer to the event!")
        quit()
 
 
 
def SCRAPE_ANIME_SHOWNAMES():

    url = 'http://www.animetoon.org/dubbed-anime'

    link = open_url(url)
    match2 = re.compile('<td>(.+?)</td>',re.DOTALL).findall(link)
    
    for links in match2:
        try:
            url = re.compile('<a href="(.+?)">',re.DOTALL).findall(links)[0]
            showname = re.compile ('<a href=".+?">(.+?)</a>',re.DOTALL).findall(links)[0]
            addDir("[COLOR lime]" + showname + "[/COLOR]",url,33,iconimage,fanarts,'')
        except: pass
        
def SCRAPE_ANIME_LINKS(url):
    
    link = open_url(url)
    iconimage = re.compile('img src="(.+?)"',re.DOTALL).findall(link)[2]
    match = re.compile('<div id="videos">(.+?)</div>',re.DOTALL).findall(link)[0]
    match2 = re.compile('<li>(.+?)</li>',re.DOTALL).findall(match)

    for items in match2:
        try:
            name = re.compile('<a href=".+?">(.+?)</a>',re.DOTALL).findall(items)[0]
            url = re.compile('<a href="(.+?)">.+?</a>',re.DOTALL).findall(items)[0]
            addLink("[COLOR lime]" + name + "[/COLOR]",url,34,iconimage,fanarts,'')
        except: pass

def SCRAPE_ANIME_PLAY(name,url,iconimage):

    link = open_url(url)
    vids = re.compile ('<iframe src="(.+?)"',re.DOTALL).findall(link)[0]
    #liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    #xbmc.Player().play(vids,liz,False)
    PLAYLINK(name,vids,iconimage)
    
def SCRAPE_CARTOONS_SHOWNAMES():

    url = 'http://www.toonget.net/cartoon'

    link = open_url(url)
    match2 = re.compile('<td>(.+?)</td>',re.DOTALL).findall(link)
    
    for links in match2:
        try:
            url = re.compile('<a href="(.+?)">',re.DOTALL).findall(links)[0]
            showname = re.compile ('<a href=".+?">(.+?)</a>',re.DOTALL).findall(links)[0]
            addDir("[COLOR lime]" + showname + "[/COLOR]",url,36,iconimage,fanarts,'')
        except: pass
        
def SCRAPE_CARTOON_LINKS(url):
    
    link = open_url(url)
    iconimage = re.compile('img src="(.+?)"',re.DOTALL).findall(link)[2]
    match = re.compile('<div id="videos">(.+?)</div>',re.DOTALL).findall(link)[0]
    match2 = re.compile('<li>(.+?)</li>',re.DOTALL).findall(match)

    for items in match2:
        try:
            name = re.compile('<a href=".+?">(.+?)</a>',re.DOTALL).findall(items)[0]
            url = re.compile('<a href="(.+?)">.+?</a>',re.DOTALL).findall(items)[0]
            addLink("[COLOR lime]" + name + "[/COLOR]",url,37,iconimage,fanarts,'')
        except: pass
        
def SCRAPE_CARTOONS_PLAY(name,url,iconimage):

    link = open_url(url)
    vids = re.compile ('<iframe src="(.+?)"',re.DOTALL).findall(link)[0]
    #liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    #xbmc.Player().play(vids,liz,False)
    PLAYLINK(name,vids,iconimage)
    
def SCRAPE_COMICS():

    url = 'http://www.readcomics.tv/comic-list'
    link = open_url(url)
    match = re.compile('<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>',re.DOTALL).findall(link)[0]
    match2 = re.compile('<li>(.+?)</li>',re.DOTALL).findall(match)
    
    for links in match2:
        try:
            name = re.compile('<a href=".+?">(.+?)</a>',re.DOTALL).findall(links)[0]
            url = re.compile('<a href="(.+?)">.+?</a>',re.DOTALL).findall(links)[0]
            addDir("[COLOR lime]" + name + "[/COLOR]",url,39,iconimage,fanarts,'')
        except: pass
        
def SCRAPE_COMICS_CONTENT(url):

    link = open_url(url)
    image = re.compile('<div class="manga-image"><img src="(.+?)"',re.DOTALL).findall(link)[0]
    name = re.compile ('<h2>(.+?)</h2>',re.DOTALL).findall(link)[0].replace('Read ', '').replace('Online', '')
    current = re.compile('<a class="stread" href="(.+?)">',re.DOTALL).findall(link)[0]
    a = current.split('/')[-1]
    b = a.replace('chapter-',' ')
    b = int(b)
    addDir("[COLOR lime]Issue " + str(b) + "[/COLOR]",current,40,image,fanarts,'')
    match = re.compile ('<ul class="ml-list">(.+?)</ul>',re.DOTALL).findall(link)[0]
    match2 = re.compile ('<li>(.+?)</li>',re.DOTALL).findall(match)
    for links in sorted(match2):
        b = b + 1
        url = re.compile('<a href="(.+?)"',re.DOTALL).findall(links)[0]
        addDir("[COLOR lime]Issue " + str(b) + "[/COLOR]",url,40,image,fanarts,'')
    
def SCRAPE_COMICS_ISSUE(url):

    link = open_url(url).replace('\n','')  
    pages = re.compile('<div class="label">of (.+?)</div>',re.DOTALL).findall(link)[0]

    pages = int(pages)
    main_url= re.compile('<img id="main_img" src="(.+?)"',re.DOTALL).findall(link)[0]
    a = main_url.replace('.jpg','').replace('http://','')
    b = a.split('/')
    c = len(b)
    d = c-1
    e = 1
    string = ""
    for grab in b:
        if e <= d:
            string = string + "/" + grab
            e = e + 1

    start = 1
    string = "http://" + string + "/"

    while start <= pages:
        url = string + str(start) + ".jpg"
        addLinkRegex("[COLOR lime]Page " + str(start) + "[/COLOR]",url,9,url,url,'')
        start = start + 1

def SCRAPE_SOCCERSTREAMS():

    url = 'http://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
    
    link = open_url(url)
    match = re.compile ('{"start(.+?)}').findall(link)
    for items in match:
        if not 'event_status":""' in str(items):
            kickoff = 1
        else: kickoff = 0
        start_date = re.compile('date":"(.+?)"').findall(items)[0]
        comp_name = re.compile('competition_name":"(.+?)"').findall(items)[0]
        comp_logo = re.compile('competition_logo":"(.+?)"').findall(items)[0]
        home_team = re.compile('home_team":"(.+?)"').findall(items)[0]
        home_logo = re.compile('home_team_logo":"(.+?)"').findall(items)[0]
        home_slug = re.compile('home_team_slug":"(.+?)"').findall(items)[0]
        try:
            event_status = re.compile('event_status":"(.+?)"').findall(items)[0]
        except: event_status = "null"
        away_team = re.compile('away_team":"(.+?)"').findall(items)[0]
        away_logo = re.compile('away_team_logo":"(.+?)"').findall(items)[0]
        away_slug = re.compile('away_team_logo":"(.+?)"').findall(items)[0]
        event_id = re.compile('event_id":"(.+?)"').findall(items)[0]
        try:
            game_minute =re.compile('game_minute":"(.+?)"').findall(items)[0]
        except: game_minute = "null"
        home_team_list = home_logo.split("-")
        away_team_list = away_logo.split("-")
        home_team = ""
        i = 0
        for a in home_team_list:
            i = i + 1
            length = len(home_team_list)
            if i < length:
                home_team = home_team +" "+ a
        away_team = ""
        i = 0
        for a in away_team_list:
            i = i + 1
            length = len(away_team_list)
            if i < length:
                away_team = away_team +" "+ a

        start_date = start_date+"!"
        start_date,start_time = start_date.split(' ')
        start_time = start_time.replace(":00!","")
        a,b,c = start_date.split("-")
        start_date = c + "-" + b + "-" + a
        start_time = "[COLOR yellow][B]" + start_time + "[/B][/COLOR]"
        start_date = "[COLOR red][B]" + start_date + "[/B][/COLOR]"
        url = 'http://soccerstreams.net/streams/' + event_id + '/' + home_slug + '_vs_' + away_slug
        name = '[COLOR lime][B]' + home_team.title() + ' vs ' + away_team.title() + '[/B][/COLOR]'
        url = url + "|SPLIT|" + name
        iconimage = 'http://soccerstreams.net/images/teams/' + home_logo
        if kickoff == 0:
            addLink(start_time + ' | ' + name + ' - ' + start_date + ' | [COLOR yellow]'+ comp_name + '[/COLOR]',url,30,iconimage,fanarts,'')
        else:
            game_minute = game_minute.replace('&#039;', "'")
            addLink("[COLOR red][B]" + game_minute + " " + event_status + '[/B][/COLOR] | ' + name + ' - ' + start_date + ' | [COLOR yellow]'+ comp_name + '[/COLOR]',url,30,iconimage,fanarts,'')
        
def SCRAPE_SOCCERSTREAMS_GET_LINKS(name,url,iconimage):

    url,name = url.split("|SPLIT|")
    orig_name = name
    streamurl=[]
    streamname=[]
    streamicon=[]
   
    i = 0
    j = 0
    link2 = open_url(url).replace('\n','').replace('\r','').replace('\t','')
    links = re.compile ('<td class=""(.+?)<i class="fa fa-thumbs-up',re.DOTALL).findall(link2)
    
    for streams in links:
        try:
            name = re.compile ('<td class="clickable">(.+?)<img src=".+?" alt=""></td>.+?<td class="clickable">').findall(streams)[0]
        except:
            name = re.compile ('<td class="clickable">(.+?)</td>.+?<td class="clickable">').findall(streams)[0]
        url = re.compile ('<a href="(.+?)"').findall(streams)[0]
        bitrate = re.compile ('<td class="clickable">(.+?)</td>').findall(streams)[2]
        language = re.compile ('<td class="clickable"><img src=".+?" alt="(.+?)"></td>').findall(streams)[-1]
        try: 
           linkquality = re.compile ('<span class="tag quality-tag">(.+?)</span>').findall(streams)[0]
        except: linkquality = "Unknown"
        name = name.lstrip(" ")
        name = name.replace("  ","").replace(" ","").replace('<img src="http://soccerstreams.net/images/verified.png" alt="">',"")
        if "1080" in linkquality: linkquality = "[COLOR white][B]1080P[/B][/COLOR]"
        elif "720" in linkquality: linkquality = "[COLOR dodgerblue][B]720P[/B][/COLOR]"
        elif "520" in linkquality: linkquality = "[COLOR yellow][B]520P[/B][/COLOR]"
        elif "480" in linkquality: linkquality = "[COLOR green][B]480P[/B][/COLOR]"
        elif "ace" in linkquality.lower(): linkquality = "[COLOR red][B]ACESTREAM[/B][/COLOR]"
        else: linkquality = "[COLOR grey][B]UNKNOWN[/B][/COLOR]"
        if "acestream" in url:
            linkquality = "[COLOR red][B]ACESTREAM[/B][/COLOR]"

        name = "[COLOR blue][B]" + name.title() + "[/B][/COLOR] - " + linkquality + " | [COLOR white] Language: " + language.upper() + " - Bitrate: " + bitrate + "[/COLOR]"
        if "acestream" in url:
            j = j + 1
            if os.path.exists(PLEXUS_PATH):
                streamurl.append(url)
                streamname.append(name)
                i = i + 1
        else:
            streamurl.append(url)
            streamname.append(name)
            i = i + 1

    dialog = xbmcgui.Dialog()
    if i == 0:
        if j >= 1:
            dialog.ok(AddonTitle, "There are acestream links available, however you do not have Plexus set up. Please install Plexus to use these links.")     
        else:
            dialog.ok(AddonTitle, "Sorry, there are no streams available at this time.")     
    else:
        orig_name ='[COLOR mediumpurple]'+orig_name+'[/COLOR]'

        select = dialog.select(orig_name,streamname)
        if select < 0:
            quit()
        else:
            url = streamurl[select]
            check = streamname[select]
            name = urllib.quote_plus(streamname[select])
            import liveresolver
            import urlresolver
            if urlresolver.HostedMediaFile(url).valid_url(): 
                stream_url = urlresolver.HostedMediaFile(url).resolve()
                liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
                liz.setPath(stream_url)
                xbmc.Player ().play(stream_url, liz, False)
            elif liveresolver.isValid(url)==True: 
                url=liveresolver.resolve(url)
                liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
                liz.setPath(stream_url)
                xbmc.Player ().play(stream_url, liz, False)
            elif "acestream" in url: 
                dialog.ok("22", url)
                url = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+" + name
            else:
                if '.m3u8' in url: 
                    url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage
                elif '.ts'in url: 
                    url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage         
                else:
                    sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+name+'%26url='
                    suffix = "/"
                    if not check.endswith(suffix):
                        refer = check + "/"
                    else:
                        refer = check
                    url = sdbase + streamurl[select] + "%26referer=" + refer
                liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
                liz.setPath(url)
                xbmc.Player ().play(url, liz, False)
        
def SCRAPE_MUSIC_VIDS(url):

    current_page = 1
    url = 'http://hdvidmusic.com'
    ep = open_url(url)
    endpa = re.compile('<a href="([^"]*)">>></a></div>',re.DOTALL).findall(ep)[0]
    endpa = endpa.replace('?page=','')
    end_page = int(endpa)

    url = 'http://hdvidmusic.com/?page='+ str(current_page)
    while current_page <= end_page:

        url = 'http://hdvidmusic.com/?page='+ str(current_page)

        link = open_url(url)
        match = re.compile('<div class="cell_container">(.+?)<!--div class="video_rating">',re.DOTALL).findall(link)

        for links in match:
            title = re.compile('<a title="(.+?)" href=".+?">',re.DOTALL).findall(links)[0]
            link = re.compile('<a title=".+?" href="(.+?)">',re.DOTALL).findall(links)[0]
            thumbnail = re.compile('src="(.+?)"/>',re.DOTALL).findall(links)[0]
            quality = re.compile('<div class="video_quality">(.+?)</div>',re.DOTALL).findall(links)[0]
            link2 = 'http://hdvidmusic.com' + link
            thumbnail2 = 'http://hdvidmusic.com' + thumbnail
            addLinkRegex("[COLOR lime]" + title + "[/COLOR]",link2,29,thumbnail2,fanarts,'')
        current_page = current_page + 1
        
        
def PLAY_MUSIC_VIDS(url):

    link2 = open_url(url).replace('?','')
    grabvideo = re.compile('<iframe id\=.+?www(.+?)aut').findall(link2)[0]
    id = grabvideo.split('/')[-1]
    url = 'plugin://plugin.video.youtube/play/?video_id=' + id
    xbmc.Player().play(url)
    
def SCRAPE_DOCS_CATS(url):


        link = open_url(url).replace('&amp;','and')
        # match2 = re.compile('<li.+?=".+?="(.+?)"\ title.+?>(.+?)<.+?li>').findall(link)
        # for url,name in match2:
            # if 'categ' in url:
                # print(name)
                # url2 = "http://documentaryheaven.com" + url
                # addDir("[COLOR lime]" + name + "[/COLOR]",url2,25,icon,fanarts,'')
                
        match = re.compile('<li.+?href="(.+?)".+?>(.+?)</a.+?li>').findall(link)
        for url2, title in match:
            if url2.find('categ') != -1:
                new = url + url2
                addDir("[COLOR lime]" + title + "[/COLOR]",new,25,icon,fanarts,'')
            
def SCRAPE_DOCS_CONTENT(url):

        link2 = open_url(url).replace('&#8217;',"'")
        information = re.compile('<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(link2)
       	for url,thumbnail,name in information:
            link3 = open_url(url)
            videolink = re.compile('<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"').findall(link3)
            for ids in videolink:
                try:
                    reallinks = ids.split("/embed/")[1]
                    endlink = "plugin://plugin.video.youtube/play/?video_id=" + reallinks
                    addLinkRegex("[COLOR lime]" + name.title() + "[/COLOR]",endlink,7,thumbnail,fanarts,'')
                except: pass

        try:
            np = re.compile('<link rel="next" href="(.+?)" />', re.DOTALL).findall(link2)[0]
            addDir("[COLOR red]Next Page -->[/COLOR]",np,25,icon,fanarts,'')
        except: pass

def SCRAPE_PORNSCRAPE_CATS(url):

            link = open_url(url)
            match = re.compile('<a class="site_tag(.+?)/a>').findall(link)

            for link in match:
                url = re.compile('href="(.+?)"').findall(link)[0]
                name = re.compile('/i>(.+?)<').findall(link)[0]
                url2 = "http://xoxfuck.com" + url
                addDir("[COLOR lime]" + name.title() + "[/COLOR]",url2,17,icon,fanarts,'')
        
def SCRAPE_PORNSCRAPE_CONTENT(name,url,iconimage):

    getting = name.split('(')[1]
    getting = getting.replace(')','').replace("[/COLOR]",'')
    getting = int(getting)
    original = url
   
    getting_now = 0
    counter = 1
    i = 0
    j = 6
   
    dp.create("STREAM ARMY","[COLOR lime]Getting video 1 of " + str(getting) + "![/COLOR]")
    dp.update(0)
    while counter < 2000:

        if i == 0:
            link = open_url(original)

            match = re.compile('<div class="inner_block video_box">(.+?)</a>').findall(link)
            for items in match:
                url2 = re.compile('href="(.+?)">').findall(items)[0]
                name = re.compile('<h2.+?>(.+?)<').findall(items)[0]
                iconimage = re.compile('src="(.+?)"').findall(items)[0]
                getting_now = getting_now + 1
                progress = 100 * int(getting_now)/int(getting)
                dp.update(progress,"[COLOR lime]Getting video " + str(getting_now) + " of " + str(getting) + "![/COLOR]")
                addLinkRegex("[COLOR lime]" + name.title() + "[/COLOR]",url2,18,iconimage,fanarts,'')
            i = i + 1
        else:
            url = original + '?load_more=10&loaded=' + str(j)
            link = open_url(url)
            link = link.replace('\\','')
            
            if "no_more_videos" in link:
                counter = 2001
                 
            match = re.compile('<div class="(.+?)</a>').findall(link)
            for items in match:
                if counter < 2000:
                    url2 = re.compile('href="(.+?)">').findall(items)[0]
                    name = re.compile('<h2.+?>(.+?)<').findall(items)[0]
                    iconimage = re.compile('src="(.+?)"').findall(items)[0]
                    getting_now = getting_now + 1
                    progress = 100 * int(getting_now)/int(getting)
                    dp.update(progress,"[COLOR lime]Getting video " + str(getting_now) + " of " + str(getting) + "![/COLOR]")
                    addLinkRegex("[COLOR lime]" + name.title() + "[/COLOR]",url2,18,iconimage,fanarts,'')
            j = j + 10
        counter = counter + 1
    dp.close
    
def SCRAPE_FILMON_CATS():

    url = 'http://www.filmon.com/tv/bbc-news'

    link = open_url(url)
    match = re.compile('{"group_id"(.+?)channels_count').findall(link)
    for groups in match:
        name = re.compile('title":"(.+?)"').findall(groups)[0]
        addDir("[COLOR lime]" + name + "[/COLOR]",groups,27,icon,fanarts,'')
          
def SCRAPE_FILMON_CHANS(url):

    match = re.compile('{"id"(.+?)}').findall(url)
    for channels in match:
        name = re.compile(':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"').findall(channels)[0]
        iconimage = re.compile(':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"').findall(channels)[0]
        url = re.compile(':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"').findall(channels)[0]
        iconimage = iconimage.replace('\\','')
        url2 = 'https://www.filmon.com/tv/' + url
        addLink("[COLOR lime]" + name + "[/COLOR]",url2,2,iconimage,fanarts,'')
        
def PLAY_ADULT(name,url,iconimage):

    link2 = open_url(url)
    links = re.compile('<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">').findall(link2)[0]
    title = re.compile('<title>(.+?)</title>').findall(link2)[0]
    title = title.split(' | ')[0]
    title = title.strip(' ')
    liz = xbmcgui.ListItem(title, iconImage=iconimage, thumbnailImage=iconimage)
    xbmc.Player().play(links,liz,False)

def SCRAPE_TVSHOWSPUT(url):

    try:
        if not "http" in url:
            if "https://" in url:
                url = url.replace("https://","http://")
            link = open_url(url)
            name = re.compile('<title>(.+?)</title>').findall(link)[0].split(' (')[0]
            episodes = re.compile('<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">').findall(link)
            iconimage= re.compile('<meta property="og:image" content="(.+?)"').findall(link)[0]
            
            for url,title in episodes:
                addLinkRegex(title,url,14,iconimage,fanarts,'')
        else:
            link = open_url(url)
            
            match = re.compile('<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>').findall(link)[0]
            string = str(match)
            match2 = re.compile('<td width="100%" class="entry">(.+?)</td>').findall(string)
            iconimage2 = re.compile('<meta property="og:image" content="(.+?)"/>',re.DOTALL).findall(link)[0]
            for items in match2:
                    name = re.compile('title="(.+?)"').findall(items)[0]
                    url = re.compile('<a href="(.+?)"').findall(items)[0]
                    title = name.split(' - ')[1]
                    if not 'http' in url: url='http:'+url
                    addLinkRegex("[COLOR lime]" + name.title() + "[/COLOR]",url,14,iconimage2,fanarts,'')
    except:
        dialog.ok("Stream Army", "Man Down, Man Down we couldn't get a stream!")
        quit()
        
def SEARCH_MOVIES():

     string =''
     keyboard = xbmc.Keyboard(string, 'Search For A Movie')
     keyboard.doModal()
     if keyboard.isConfirmed():
        entry = keyboard.getText()
        term = entry
        string = entry.replace(' ','+')
        if not len(string)>1:
            dialog.ok("STREAM ARMY", "No search term was entered.")
            quit()
            
        string = string.replace(' ','+')
        url="http://housemovie.to/search?q=" + string
        link = open_url(url)
        match = re.compile('<li>(.+?)</li>').findall(link)
        
        for items in match:
            try:
                name=re.compile('<span class="item_name">(.+?)</span>').findall(items)[0]
                url=re.compile('<a href="(.+?)" class="fig_holder">').findall(items)[0]
                iconimage=re.compile('src="(.+?)"').findall(items)[0]
                try:
                    imdb=re.compile('<span class="imdb">(.+?)</span>').findall(items)[0]
                except: imdb = "IMDB Rating Unknown"
                if not "http" in url:
                    url = "http://housemovie.to" + url
                    addLinkRegex("[COLOR lime]" + name.title() + "[/COLOR] - [COLOR yellow][I]" + imdb + "[/I][/COLOR]",url,21,iconimage,fanarts,'')
            except: pass


def SCRAPE_MOVIESCRAPE_CATS(url):

    link = open_url(url)

    match = re.compile('<li>(.+?)</li>').findall(link)

    for links in match:
        try:
            name = re.compile('<a href=".+?">(.+?)</a>').findall(links)[0]
            url2 = re.compile('<a href="(.+?)">.+?</a>').findall(links)[0]
            if "genres" in url2:
                url2 = "http://housemovie.to" + url2
                addDir("[COLOR lime]" + name.title() + "[/COLOR]",url2,19,icon,fanarts,'') 
        except: pass
        
def SCRAPE_MOVIESCRAPE_NORM(url):

    link = open_url(url)

    match = re.compile('<li>(.+?)</li>').findall(link)

    for links in match:
        try:
            name = re.compile('<span class="item_name">(.+?)</span>').findall(links)[0]
            imdb = re.compile('imdb">(.+?)</span>').findall(links)[0]
            if "(SOON)" in name:
                name1 = name.split("(SOON)")[0]
                name = name1.title() + '[COLOR red](Coming Soon)[/COLOR]'
            else: name = name.title()
            url2 = re.compile('<a href="(.+?)">.+?</a>').findall(links)[0]
            iconimage = re.compile('src="(.+?)"').findall(links)[0]
            if "watch" in url2:
                url2 = "http://housemovie.to" + url2
                addLinkRegex("[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + imdb + "[/I][/COLOR]",url2,21,iconimage,fanarts,'')
                
        except: pass
        
        

def SCRAPE_MOVIESCRAPE_MOVIES(name,url,iconimage):

    namelist = []
    urllist  = []
    iconlist = []
    imdblist = []
    combinedlists = []
    
    link = open_url(url).replace('\n','').replace('\r','')

    match = re.compile('<div class="fig_holder">(.+?)</div>').findall(link)
    for links in match:
            name = re.compile('<span class="item_name">(.+?)</span>').findall(links)[0]
            url2 = re.compile('<a href="(.+?)"').findall(links)[0]
            iconimage = re.compile('src="(.+?)"').findall(links)[0]
            try:
                imdb = re.compile('imdb">(.+?)</span>').findall(links)[0]
            except: imdb = "0.0"
            if "imdb" in imdb.lower():
                imdb = imdb.replace("IMDB: ","").replace(" ","")
            if not "." in imdb:
                imdb = imdb + ".0"
            #imdb = float(imdb)
            if "(SOON)" in name:
                name1 = name.split("(SOON)")[0]
                name = name1.title() + '[COLOR red](Coming Soon)[/COLOR]'
            else: name = name.title()
            url2 = "http://housemovie.to" + url2
            
            namelist.append(name)
            urllist.append(url2)
            iconlist.append(iconimage)
            imdblist.append(imdb)
            combinedlists = list(zip(imdblist,namelist,urllist,iconlist))
            
    tup = sorted(combinedlists,reverse=True)
    
    for imdb,name,url2,iconimage in tup:
        if imdb == "0.0":
            imdb = "IMDB Rating Unknown"
        else: imdb = "IMDB: " + imdb
        addLinkRegex("[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + imdb + "[/I][/COLOR]",url2,21,iconimage,fanarts,'') 

    try:
        next_page = re.compile('<a href="([^"]*)" class="page_next">Next</a>').findall(link)[0]
        addDir("[COLOR red]Next Page -->[/COLOR]",next_page,19,icon,fanarts,'') 
    except: pass
    
def SCRAPE_MOVIESCRAPE_LINKS(name,url,iconimage):
    
    streamname = []
    streamurl=[]
    streamicon=[]

    link = open_url(url).replace('\n','').replace('\r','')

    links = re.compile('<div class="md_full_cell">(.+?)</div>').findall(link)

    for urls in links:
        try:
            url = re.compile('<a href="(.+?)"').findall(urls)[0]
            title = re.compile('rel="nofollow">(.+?)</a>').findall(urls)[0]
            url = "http://housemovie.to" + url
            for checks in url_reolver_supports:
                if checks.lower() in title.lower():
                #MOVE BELOW IN BY INDENT
                    streamname.append(title)
                    streamurl.append(url)
                    streamicon.append(iconimage)
        except: pass


    name='[COLOR lime]'+name+'[/COLOR]'
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        url = streamurl[select]
        url = str(url)
        icon = streamicon[select]
        icon = str(icon)

        link = open_url(url).replace('\n','').replace('\r','')

        url = re.compile('<a href="([^"]*)" target="_blank" class="button_type_1">').findall(link)[0]

        try:
            import urlresolver
            if urlresolver.HostedMediaFile(url).valid_url(): 
                stream_url = urlresolver.HostedMediaFile(url).resolve()
                liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
                liz.setPath(stream_url)
                xbmc.Player ().play(stream_url, liz, False)
            else: dialog.ok(AddonTitle, "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]")
        except:
            dialog.ok(AddonTitle, "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]")

def SCRAPE_MULTI_LINK(name,url,iconimage):

    iconimage = "null"
    #REMOVE LINE
    i = 0
    streamurl=[]
    streamname=[]
    streamicon=[]
    
    attempts = 1
    passed = 0
    if "http" in url:
    
        dp.create("Stream Army", "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]")
        dp.update(0)
    
        while attempts < 11:
            progress = 100 * int(attempts)/int(10)
            dp.update(progress, "","[COLOR lime]Connection attempt " + str(attempts) + " of 10[/COLOR]")
            link = open_url(url)

            if passed == 0:
                attempts = attempts + 1
                title = re.compile('title="(.+?)"').findall(link)[0]
                title = title.split(" - ")[0]

                url3 = re.compile('<td class="entry">(.+?)target').findall(link)
                for urls in url3:
                    filt = 1
                    filter_num = len(urls)
                    progress2 = 100 * int(filt)/int(filter_num)
                    dp.update(progress2, "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]","[COLOR lime]Filtering links " + str(filt) + " of " + str(filter_num) + " possible matches[/COLOR]")

                    if not "putlocker.bypassed.info" in urls:
                        url4 = re.compile('<a rel=".+?" href="(.+?)"').findall(urls)[0]
                        i = i + 1
                        streamname.append("Link " + str(i))
                        streamurl.append(url4)
                        streamicon.append(iconimage)
                    passed = 1
                    attempts = 12
                    filt = filt + 1

            if dp.iscanceled():
                sys.exit()
            import time
            time.sleep(1)
            attempts = attempts + 1

    else:

        link2 = open_url(url)
        links = re.compile('<td class="entry">(.+?)</tr>').findall(link2)

        for urls in links:
            url = re.compile('href="(.+?)"').findall(urls)[0]
            if not "putlocker.unblocked.ink" in url:
                i = i + 1
                streamname.append("Link " + str(i))
                streamurl.append(url)
                streamicon.append(iconimage)

    #dp.close()

    if i == 0:
        dialog.ok("Stream Army", "Man Down, Man Down we couldn't get a stream!")
        quit()   
    name='[COLOR lime]'+name+'[/COLOR]'
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        url = streamurl[select]
        url = str(url)
        icon = streamicon[select]
        icon = str(icon)
        import urlresolver
        if urlresolver.HostedMediaFile(url).valid_url(): 
            stream_url = urlresolver.HostedMediaFile(url).resolve()
            liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
            liz.setPath(stream_url)
            xbmc.Player ().play(stream_url, liz, False)
        #else:
        #    dialog.ok("Stream Army", "Man Down, Man Down we couldn't play the stream!")
        #    quit()      
   
def PLAYSD(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)
        
def PLAYREGEX(name,url,iconimage):

    name = name.replace('  ','')
    if not 'f4m'in url:
        if '.m3u8' in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
        elif '.ts'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
    else: url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    
    import urlresolver
    if urlresolver.HostedMediaFile(url).valid_url(): 
        stream_url = urlresolver.HostedMediaFile(url).resolve()
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
        
def PLAYVIDEO(url):

    try:
        name,url,iconimage = url.split("!SASPLIT!")
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        xbmc.Player().play(url,liz,False)
    except:    
        xbmc.Player().play(url)

def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        # print link
        return link
    except:quit()

def open_encrypted_url(url):

    # print "--------- open_encrypted_url --------"
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'obsession')
        response = urllib2.urlopen(req)
        link=response.read()
        # print "--------- link --------", link
        decoded = decrypt(link)
        print "--------- decoded --------", decoded
        response.close()
        decoded=decoded.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        # print decoded
        return decoded
    except:quit()

def open_url2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        # print link
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

def addLinkRegex(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def addLink(name, url, mode, iconimage, fanart, description=''):

    if '.ts'in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' not in url:
        liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addItem(name,url,mode,iconimage,fanart, description=''):

    if '.ts'in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
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
    
    

def GetEncodeString(str):

    try:
        import chardet
        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
    except:
        try:
            str = str.encode("utf-8")
        except:
            pass
    return str

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
elif mode==10:GET_REGEX(name,url,iconimage)
elif mode==11:GET_M3U(name,url,iconimage)
elif mode==12:SCRAPE_SPORTSMAMA(url)
elif mode==13:SCRAPE_TVSHOWSPUT(url)
elif mode==14:SCRAPE_MULTI_LINK(name,url,iconimage)
elif mode==15:SCRAPE_MOVIESCRAPE_CATS(url)
elif mode==16:SCRAPE_PORNSCRAPE_CATS(url)
elif mode==17:SCRAPE_PORNSCRAPE_CONTENT(name,url,iconimage)
elif mode==18:PLAY_ADULT(name,url,iconimage)
elif mode==19:SCRAPE_MOVIESCRAPE_MOVIES(name,url,iconimage)
elif mode==20:GetEncrtptedContent(name,url,iconimage,fanart)
elif mode==21:SCRAPE_MOVIESCRAPE_LINKS(name,url,iconimage)
elif mode==22:SCRAPE_MOVIESCRAPE_NORM(url)
elif mode==23:SEARCH_MOVIES()
elif mode==24:SCRAPE_DOCS_CATS(url)
elif mode==25:SCRAPE_DOCS_CONTENT(url)
elif mode==26:SCRAPE_FILMON_CATS()
elif mode==27:SCRAPE_FILMON_CHANS(url)
elif mode==28:SCRAPE_MUSIC_VIDS(url)
elif mode==29:PLAY_MUSIC_VIDS(url)
elif mode==31:SCRAPE_SOCCERSTREAMS()
elif mode==30:SCRAPE_SOCCERSTREAMS_GET_LINKS(name,url,iconimage)
elif mode==32:SCRAPE_ANIME_SHOWNAMES()
elif mode==33:SCRAPE_ANIME_LINKS(url)
elif mode==34:SCRAPE_ANIME_PLAY(name,url,iconimage)
elif mode==35:SCRAPE_CARTOONS_SHOWNAMES()
elif mode==36:SCRAPE_CARTOON_LINKS(url)
elif mode==37:SCRAPE_CARTOONS_PLAY(name,url,iconimage)
elif mode==38:SCRAPE_COMICS()
elif mode==39:SCRAPE_COMICS_CONTENT(url)
elif mode==40:SCRAPE_COMICS_ISSUE(url)

if mode==None or url==None or len(url)<1: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=False)
else: xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)