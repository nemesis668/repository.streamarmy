import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,hashlibimport base64import HTMLParserimport osfrom resources.libs.modules import satoolsaddon_id        = 'plugin.video.streamarmy'AddonTitle      = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))dialog          = xbmcgui.Dialog()def SCRAPE_SOCCERSTREAMS():           iconimage = 'http://thesportsu.com/wp-content/uploads/2015/06/Soccer-500x500.jpg'    satools.addLink("[COLOR crimson]" "[B]All Kick Off Times In GMT[/B]" "[/COLOR]",'url','2',iconimage,fanarts,'')    satools.addLink("[COLOR crimson]" "[B]Games Might Be Empty Until An Hour Before Kick Off[/B]" "[/COLOR]",'url','2',iconimage,fanarts,'')        url = 'https://soccerstreams.net/'    link = satools.open_url(url)        match = re.compile('<span class="event-time"(.+?)</a>').findall(link)    for links in match:        try:            icon = re.compile('<img src="(.+?)"').findall(links)[0]            if '//cdn.soccerstreams.net/images/competitions/small/uefaeuropaleague.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/uefaeuropaleague.png','http://i.imgur.com/Je9YXo0.jpg')            elif '//cdn.soccerstreams.net/images/competitions/small/libertadoris.png' in icon:                icon = icon.replace ('//cdn.soccerstreams.net/images/competitions/small/libertadoris.png', 'http://i.imgur.com/qq0BTDu.jpg')            elif '//cdn.soccerstreams.net/images/competitions/small/ligue2.png' in icon:                icon = icon.replace ('//cdn.soccerstreams.net/images/competitions/small/ligue2.png', 'http://i.imgur.com/h9h29V9.png')            elif '//cdn.soccerstreams.net/images/competitions/small/belgianjupilerproleague.png' in icon:                icon = icon.replace ('//cdn.soccerstreams.net/images/competitions/small/belgianjupilerproleague.png', 'http://i.imgur.com/rchhNgd.jpg')            elif '//cdn.soccerstreams.net/images/competitions/small/gerbundisliga.png' in icon:                icon =icon.replace('//cdn.soccerstreams.net/images/competitions/small/gerbundisliga.png', 'http://i.imgur.com/ne3jrWI.png')            elif '//cdn.soccerstreams.net/images/competitions/small/ligue1.png' in icon:                icon =icon.replace('//cdn.soccerstreams.net/images/competitions/small/ligue1.png', 'http://i.imgur.com/YKm545U.png')            elif '//cdn.soccerstreams.net/images/competitions/small/laliga.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/laliga.png', 'http://i.imgur.com/Z2OH3eN.png')            elif '//cdn.soccerstreams.net/images/competitions/small/premierleague.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/premierleague.png', 'http://i.imgur.com/t6MJxu1.jpg')            elif '//cdn.soccerstreams.net/images/competitions/small/primeiraliga.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/primeiraliga.png', 'http://i.imgur.com/oqdSl90.png')            elif '//cdn.soccerstreams.net/images/competitions/small/arprimiradivision.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/arprimiradivision.png', 'http://i.imgur.com/z0rWAvp.png')            elif '//cdn.soccerstreams.net/images/competitions/small/mls.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/mls.png', 'http://i.imgur.com/fIGbQxx.png')            elif '//cdn.soccerstreams.net/images/competitions/small/ligamx.png' in icon:                icon = icon.replace('//cdn.soccerstreams.net/images/competitions/small/ligamx.png', 'http://i.imgur.com/iUnA9Gs.jpg')            home = re.compile('alt="(.+?)"').findall(links)[1]            away = re.compile('alt="(.+?)"').findall(links)[2]            url = re.compile ('<a href="(.+?)"').findall(links)[0]            time = re.compile ('data-eventtime=.+?>(.+?)</span>').findall(links)[0]            time = ' '.join(time.split())            satools.addDir("[COLOR yellow]" + time + " :: " + "[COLOR silver]" + home + " " + "[COLOR white]" + "vs" + "[COLOR silver]" + " "  + away  +  "[/COLOR]",url,13,icon,fanarts,'')        except:pass    satools.SET_VIEW()def SCRAPE_SOCCERSTREAMS_GET_LINKS(url,icon):    link = satools.open_url(url)    match = re.compile('<div class="stream_comments parent_comment hidden" >(.+?)</span>').findall(link)    for links in match:        url = re.compile ('data-href="(.+?)"').findall(links)[0]        quality = re.compile ('data-quality="(.+?)"').findall(links)[0]        lang = re.compile ('data-language="(.+?)"').findall(links)[0]        satools.addLinkRegex("[COLOR crimson]" + "P[COLOR silver]lay Stream" + "   " "[COLOR yellow]" + quality + "[COLOR red]" + "   " + "[COLOR white]" + lang + "[/COLOR]",url,5,icon,fanart,'')            satools.SET_VIEW()