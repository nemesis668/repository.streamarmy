import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,time,hashlib,urlresolver,liveresolverimport base64import HTMLParserimport osaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()dp              = xbmcgui.DialogProgress()messagetext     = 'http://pastebin.com/raw/4B2BhvJz'#baseurl         = 'http://127.0.0.1/Main/Main.xml' #ONLY ACTIVE IN TEST MODEdef CLEANUP(text):    text = str(text)    text = text.replace('\\r','')    text = text.replace('\\n','')    text = text.replace('\\t','')    text = text.replace('\\','')    text = text.replace('<br />','\n')    text = text.replace('<hr />','')    text = text.replace('&#039;',"'")    text = text.replace('&#39;',"'")    text = text.replace('&quot;','"')    text = text.replace('&rsquo;',"'")    text = text.replace('&amp;',"&")    text = text.replace('&#8211;',"&")    text = text.replace('&#8217;',"'")    text = text.replace('&#038;',"&")    text = text.lstrip(' ')    text = text.lstrip('	')    return textdef popup():        message=open_url2(messagetext)        if len(message)>1:                path = xbmcaddon.Addon().getAddonInfo('path')                comparefile = os.path.join(os.path.join(path,''), 'compare.txt')                r = open(comparefile)                compfile = r.read()                       if compfile == message:pass                else:                    showText('[B][COLOR silver]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR silver]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR silver]I[/COLOR][COLOR white]nformation[/COLOR][/B]', message)                    text_file = open(comparefile, "w")                    text_file.write(message)                    text_file.close()                    def showText(heading, text):    id = 10147    xbmc.executebuiltin('ActivateWindow(%d)' % id)    xbmc.sleep(500)    win = xbmcgui.Window(id)    retry = 50    while (retry > 0):        try:            xbmc.sleep(10)            retry -= 1            win.getControl(1).setLabel(heading)            win.getControl(5).setText(text)            return        except:            pass    def SOCCERSTREAMS_CHECK():    try:        supported=open_url_ss('https://pastebin.com/raw/x31tz2j1')                file = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/libs/modules/soccerstreams.py'))        if len(supported)>1:            comparefile = file            r = open(comparefile)            compfile = r.read()                   if compfile == supported:pass            else:                kodi.notify(msg='Updating SoccerStreams Scraper.', duration=7500, sound=True)                time.sleep(2)                text_file = open(comparefile, "w")                text_file.write(supported)                text_file.close()                kodi.notify(msg='SoccerStreams Scraper Updated.', duration=7500, sound=True)    except: pass    def GETMULTI(name,url,iconimage):        streamurl=[]    streamname=[]    streamicon=[]    link=open_url(url)    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]    links=re.compile('<link>(.+?)</link>').findall(urls)    i=1    for sturl in links:        sturl2=sturl        if '(' in sturl:            sturl=sturl.split('(')[0]            caption=str(sturl2.split('(')[1].replace(')',''))            streamurl.append(sturl)            streamname.append(caption)        else:            streamurl.append( sturl )            streamname.append( 'Link '+str(i) )        i=i+1    name='[COLOR silver]'+name+'[/COLOR]'    dialog = xbmcgui.Dialog()    select = dialog.select(name,streamname)    if select < 0:        quit()    else:        url = streamurl[select]        # print url        if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()        elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)        else: stream_url=url        liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)        liz.setPath(stream_url)        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)        dp.create(AddonTitle,"[COLOR yellow]Generating link...[/COLOR]",'[COLOR red]Please wait...[/COLOR]','')           dp.update(0)        time.sleep(2)        xbmc.Player ().play(stream_url, liz, False)def PLAYLINK(name,url,iconimage):        dp.create(AddonTitle,"[COLOR yellow]Generating link...[/COLOR]",'[COLOR red]Please wait...[/COLOR]','')       dp.update(0)    if not "plugin" in url:        try:            if not'http'in url:url='http://'+url        except:             dialog.ok(AddonTitle, "[COLOR yellow]Sorry there was a problem playing this link.[/COLOR]","[COLOR yellow]Please Try Another[/COLOR]")            quit()    if "plugin://" in url:            url = "PlayMedia("+url+")"            xbmc.executebuiltin(url)            quit()    name = name.replace('  ','')    if not 'f4m'in url:        if '.m3u8' in url:            url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon          elif '.ts'in url:            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon      else: url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'        import urlresolver        if urlresolver.HostedMediaFile(url).valid_url():         stream_url = urlresolver.HostedMediaFile(url).resolve()        liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)        liz.setPath(stream_url)        dp.close()        xbmc.Player ().play(stream_url, liz, False)        quit()    else:        stream_url=url        liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)        liz.setPath(stream_url)        dp.close()        xbmc.Player ().play(stream_url, liz, False)        quit()     def PLAY_SOCCERSTREAMS(url):    dp.create(AddonTitle,"[COLOR yellow]Generating link...[/COLOR]",'[COLOR red]Please wait...[/COLOR]','')       dp.update(0)    time.sleep(1)    import liveresolver    import urlresolver    if urlresolver.HostedMediaFile(url).valid_url():         stream_url = urlresolver.HostedMediaFile(url).resolve()        liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)        liz.setPath(stream_url)        xbmc.Player ().play(stream_url, liz, False)    elif liveresolver.isValid(url)==True:         url=liveresolver.resolve(url)        liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)        liz.setPath(stream_url)        xbmc.Player ().play(stream_url, liz, False)    else:        if '.m3u8' in url:             url1 = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage        elif '.ts'in url:             url1 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage                 else:            url1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'                    liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)        liz.setPath(url)                xbmc.Player ().play(url1, liz, False) def PLAYVIDEO(url):    dp.create(AddonTitle,"[COLOR yellow]Generating link...[/COLOR]",'[COLOR red]Please wait...[/COLOR]','')       dp.update(0)    time.sleep(1)    try:        name,url,iconimage = url.split("!SASPLIT!")        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)        xbmc.Player().play(url,liz,False)    except:            xbmc.Player().play(url)        def GetEncodeString(str):    try:        import chardet        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")    except:        try:            str = str.encode("utf-8")        except:            pass    return str    def strip_non_ascii(string):    ''' Returns the string without non ASCII characters'''    stripped = (c for c in string if 0 < ord(c) < 127)    return ''.join(stripped)    def SHOW_PICTURE(url):    SHOW = "ShowPicture(" + url + ')'    xbmc.executebuiltin(SHOW)    sys.exit(1)    def SET_VIEW():    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")    version=float(xbmc_version[:4])    if version >= 11.0 and version <= 11.9:        codename = 'Eden'    elif version >= 12.0 and version <= 12.9:        codename = 'Frodo'    elif version >= 13.0 and version <= 13.9:        codename = 'Gotham'    elif version >= 14.0 and version <= 14.9:        codename = 'Helix'    elif version >= 15.0 and version <= 15.9:        codename = 'Isengard'    elif version >= 16.0 and version <= 16.9:        codename = 'Jarvis'    elif version >= 17.0 and version <= 17.9:        codename = 'Krypton'    else: codename = "Decline"        if codename == "Jarvis":        xbmc.executebuiltin('Container.SetViewMode(50)')    elif codename == "Krypton":        xbmc.executebuiltin('Container.SetViewMode(55)')    else: xbmc.executebuiltin('Container.SetViewMode(50)')    def open_url(url):    try:        req = urllib2.Request(url)        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')        response = urllib2.urlopen(req, timeout=5)        link=response.read()        response.close()        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')        return link    except:quit()    def open_url2(url):        req = urllib2.Request(url)        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')        response = urllib2.urlopen(req)        link=response.read()        response.close()                return link    def GETMULTI_SD(name,url,iconimage):        sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='    streamurl=[]    streamname=[]    streamicon=[]    streamnumber=[]    link=open_url(url)    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(urls)    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]    i=1    for sturl in links:                sturl2=sturl                if '(' in sturl:                        sturl=sturl.split('(')[0]                        caption=str(sturl2.split('(')[1].replace(')',''))                        streamurl.append(sturl)                        streamname.append(caption)                        streamnumber.append('Stream ' + str(i))                else:                        streamurl.append( sturl )                        streamname.append( 'Link '+str(i) )                i=i+1    name='[COLOR red]'+name+'[/COLOR]'    dialog = xbmcgui.Dialog()    select = dialog.select(name,streamname)    if select < 0:        quit()    else:        check = streamname[select]        suffix = "/"        if not check.endswith(suffix):              refer = check + "/"        else:              refer = check        url = sdbase + streamurl[select] + "%26referer=" + refer        print url        xbmc.Player().play(url)        def GET_M3U(name,url,iconimage):    req = urllib2.Request(url)    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')    response = urllib2.urlopen(req)    link=response.read()    response.close()    response=link    response = response.replace('#AAASTREAM:','#A:')    response = response.replace('#EXTINF:','#A:')    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)    li = []    for params, display_name, url in matches:        item_data = {"params": params, "display_name": display_name, "url": url}        li.append(item_data)    list = []    for channel in li:        item_data = {"display_name": channel["display_name"], "url": channel["url"]}        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])        for field, value in matches:            item_data[field.strip().lower().replace('-', '_')] = value.strip()        list.append(item_data)    for channel in list:        name = GetEncodeString(channel["display_name"])        url = GetEncodeString(channel["url"])        url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')        addLink(name ,url, 2, icon, fanart,'')    def addDir(name,url,mode,iconimage,fanart,description=''):    # if baseurl == 'http://127.0.0.1/Main/Main.xml':        # url = url.replace ('http://streamarmy.offshorepastebin.com/', 'http://127.0.0.1/')        if not "http" in iconimage:        iconimage = icon    if not "http" in fanart:        fanart = fanarts    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)    ok=True    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)    liz.setProperty( "fanart_Image", fanart )    liz.setProperty( "icon_Image", iconimage )    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)    return okdef addLink(name, url, mode, iconimage, fanart, description=''):    if not "http" in iconimage:        iconimage = icon    if not "http" in fanart:        fanart = fanarts    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)    ok=True    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)    liz.setProperty( "fanart_Image", fanart )    liz.setProperty( "icon_Image", iconimage )    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)    return ok    def addLinkRegex(name, url, mode, iconimage, fanart, description=''):    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)    ok=True    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)    liz.setProperty('fanart_image', fanart)    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)    return ok    def get_params():        param=[]        paramstring=sys.argv[2]        if len(paramstring)>=2:                params=sys.argv[2]                cleanedparams=params.replace('?','')                if (params[len(params)-1]=='/'):                        params=params[0:len(params)-2]                pairsofparams=cleanedparams.split('&')                param={}                for i in range(len(pairsofparams)):                        splitparams={}                        splitparams=pairsofparams[i].split('=')                        if (len(splitparams))==2:                                param[splitparams[0]]=splitparams[1]                            return param    params=get_params(); url=None; name=None; mode=None; site=None; iconimage=Nonetry: site=urllib.unquote_plus(params["site"])except: passtry: url=urllib.unquote_plus(params["url"])except: passtry: name=urllib.unquote_plus(params["name"])except: passtry: mode=int(params["mode"])except: passtry: iconimage=urllib.unquote_plus(params["iconimage"])except: passtry: fanart=urllib.unquote_plus(params["fanart"])except: pass#<a href=\"([^"]*)\"