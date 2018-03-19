#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import os
import re
import sys
import urllib
import urllib2
import urlparse
import Main
import json
import base64
import resolveurl


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()



#############################################################
#################### SET ADDON ID ###########################
_addon_id_  = 'plugin.video.kickoff'
_self_  = xbmcaddon.Addon(id=_addon_id_)
icon  = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_, 'icon.png'))

#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_ = _self_.getSetting('Theme')
_images_    = '/resources/' + _theme_	

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image    = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'kickofflist.jpg'))
Listbg = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'listbg.png'))
Addon_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'icon.png'))



########## Function To Call That Starts The Window ##########
def listwindow(ta):
    global data
    global List
    
    data = ta
    window = list_window('kickoff')
    window.doModal()
    del window

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data
    
    
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

def passed(self, title):

    global Item_Title
    global Item_Link
    global Item_Desc
    global Item_Icon

    Item_Title =  []
    Item_Link  =  []
    Item_Desc  =  []
    Item_Icon  =  []
    
    title = title.upper()
    Item_Title.append('[COLOR yellow]' + title + '[/COLOR]')
    Item_Link.append('')
    Item_Desc.append('Kick Off By @Nemzzy668')
    Item_Icon.append(Addon_Image)
    self.List.addItem('[COLOR yellow]' + title + '[/COLOR]')
    self.textbox.setText('Kick Off By @Nemzzy668')
    self.Show_Logo.setImage(Addon_Image)
    
    if 'LIVE CHANNELS' in title:
        url = 'https://www.livefootballol.me/acestream-channel-list-2018.html'
        link = Get_Data(url).replace('\n', '').replace('\r','')
        grab = re.compile ('<tr>(.+?)</tr>').findall(link)
        for items in grab:
            title = re.compile ('<strong>(.+?)</strong>').findall(items)[0].replace('AceStream','')
            if len(title) ==1 or '&nbsp;' in title:
                title = re.compile ('<strong>(.+?)</strong>').findall(items)[1].replace('AceStream','')
            if len(title) > 40:
                title = re.compile ('<a.+?>(.+?)</a>').findall(items)[0].replace('AceStream','')
            url = re.compile ('<td>(.+?)</td>').findall(items)[2]
            lang = re.compile ('<td>(.+?)</td>').findall(items)[3]
            qual = re.compile ('<td>(.+?)</td>').findall(items)[4]
            title = title.strip()
            url = url.strip()
            url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
            Item_Link.append(url1)
            Item_Title.append(title)
            Item_Desc.append(title)
            Item_Icon.append(Addon_Image)
            self.List.addItem(title + ' :: ' + lang + ' ::[COLOR yellow] ' + qual + '[/COLOR]')
                
    if 'ACESTREAM LINKS' in title:
        url = 'https://www.livefootballol.me/live-football-streaming-2018.html'
        link = Get_Data(url).replace('\n', '').replace('\r','')
        match = re.compile('<div class="content clearfix">(.+?)</list>').findall(link)[0]
        grabgames = re.compile ('<li>([0-9]+:[0-9]+).*?<a href="(.*?)">(.*?)</a>').findall(match)
        for time,url,game in grabgames:
            game = game.replace('-',' VS ')
            if not 'http' in url:
                url = 'https://www.livefootballol.me' + url
            if 'http://www.footyzilla.com/unibet.php' in url:
                url = 'No Url'
            Item_Title.append(game)
            Item_Desc.append(game)
            image = Addon_Image
            Item_Icon.append(image)
            Item_Link.append(url)
            self.List.addItem("[COLOR yellow]" + time + "[/COLOR]" + ' ' + game)
            
    if 'NORMAL LINKS' in title:
        url = 'https://www.reddit.com/r/soccerstreams/'
        link = Get_Data(url).replace('\n', '').replace('\r','')
        match = re.compile ('data-event-action="title"(.+?)<span class="domain">').findall(link)
        for links in match:
            #try:
              title = re.compile ('rel=.+?>(.+?)</a>').findall(links)[0]
              url = re.compile ('href="(.+?)"').findall(links)[0]
              url = 'https://www.reddit.com' + url
              icon = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
              if 'GMT' in title:
                title = CLEANUP(title)
                desc = 'Sports Devil Required To Play These Links'
                Item_Desc.append(desc)
                Item_Title.append(title)
                Item_Link.append(url)
                Item_Icon.append(icon)
                self.List.addItem(title)
            
            
            
    if 'CHAMPIONS LEAGUE' in title:
        url = 'https://www.livefootballol.me/streaming/ucl-2017/'
        link = Get_Data(url).replace('\n', '').replace('\r','')
        match = re.compile('<td>(.+?)</td>').findall(link)
        if len(match) < 1:
            result = '[COLOR yellow]Returning Feb 2018[/COLOR]'
            url =''
            Item_Title.append(result)
            Item_Desc.append(result)
            image = Addon_Image
            Item_Icon.append(image)
            Item_Link.append(url)
            self.List.addItem(result)
        else:
            for Item in match:
                url = re.compile ('<a href="(.+?)"').findall(Item)[0]
                game = re.compile ('<a href=".+?">(.+?)</a>').findall(Item)[0].replace('-','[COLOR yellow]Vs[/COLOR]')
                Item_Title.append(game)
                Item_Desc.append(game)
                image = Addon_Image
                Item_Icon.append(image)
                url = 'http://www.livefootballol.me' + url
                Item_Link.append(url)
                self.List.addItem(game)
                
    if 'REPLAY' in title:
        url = 'http://www.goalsarena.org/en/'
        link = Get_Data(url).replace('\n', '').replace('\r','').replace('\t','')
        match = re.compile ('<div class="videos"(.+?)<div class="moduletable-none">').findall(link)[0]
        grab = re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(match)
        for link1,game in grab:
            link1 = 'REPLAY:' + link1
            Item_Title.append(game)
            Item_Link.append(link1)
            image = Addon_Image
            Item_Icon.append(image)
            Item_Desc.append(game)
            self.List.addItem(game)
            
    if 'OTHER' in title:
        result = '[COLOR yellow]Domestic Cup Games Will Appear Here[/COLOR]'
        url =''
        Item_Title.append(result)
        Item_Desc.append(result)
        image = Addon_Image
        Item_Icon.append(image)
        Item_Link.append(url)
        self.List.addItem(result)

    
def List_Selected(self):
    global Media_Link

    if 'plugin://' in Media_Link:
        Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player ().play(Media_Link, Show_List, False)

    if 'LIVE:' in Media_Link:
        Media_Link = Media_Link.replace('LIVE:', '')
        link = Get_Data(Media_Link)
        play = re.compile ('<source src="(.+?)"').findall(link)[0]
        Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player ().play(play, Show_List, False)
        
    elif 'channels' in Media_Link:
        global Item_Title
        global Item_Link
        global Item_Desc
        global Item_Icon

        Item_Title =  []
        Item_Link  =  []
        Item_Desc  =  []
        Item_Icon  =  []
        link = Get_Data(Media_Link).replace('\n', '').replace('\r','')
        url = re.compile('<div class="uk-text-center"><a href="(.+?)"').findall(link)[0]
        url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
        Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player ().play(url1, Show_List, False)
        
    elif 'https://www.livefootballol.me' in Media_Link:
        self.List.reset()
        self.List.setVisible(True)
        global Item_Title
        global Item_Link
        global Item_Desc
        global Item_Icon
        
        Item_Title =  []
        Item_Link  =  []
        Item_Desc  =  []
        Item_Icon  =  []
        title = 'AceStream Links'
        title = title.upper()
        Item_Title.append('[COLOR blue]' + title + '[/COLOR]')
        Item_Link.append('')
        Item_Desc.append('Kick Off By @Nemzzy668')
        Item_Icon.append(Addon_Image)
        self.List.addItem('[COLOR yellow]' + title + '[/COLOR]')
        self.textbox.setText('Kick Off By @Nemzzy668')
        self.Show_Logo.setImage(Addon_Image)
        
        link = Get_Data(Media_Link).replace('\n', '').replace('\r','')
        match = re.compile('<a href="(.+?)"').findall(link)
        linktitle = 0
        for urls in match:
            if 'acestream' in urls:
                if 'http' in urls:
                    linktitle += 1
                    title = 'Link :: ' + str(linktitle)
                    Item_Title.append(title)
                    Item_Link.append(urls)
                    image = 'https://i.imgur.com/GKvCyIm.png'
                    desc = 'AceStream Links For Games'
                    Item_Desc.append(desc)
                    Item_Icon.append(image)
                    self.List.addItem(title)
                    
        if linktitle == 0:
            title = 'No Links Available Yet, Try Closer To Kick Off'
            Item_Title.append(title)
            self.List.addItem(title)
            
            
    elif 'reddit' in Media_Link:
        self.List.reset()
        self.List.setVisible(True)
        global Item_Title
        global Item_Link
        global Item_Desc
        global Item_Icon

        Item_Title =  []
        Item_Link  =  []
        Item_Desc  =  []
        Item_Icon  =  []
        title = 'Reddit Links'
        title = title.upper()
        Item_Title.append('[COLOR red]' + title + '[/COLOR]')
        Item_Link.append('')
        Item_Desc.append('Kick Off By @Nemzzy668')
        Item_Icon.append(Addon_Image)
        self.List.addItem('[COLOR blue]' + title + '[/COLOR]')
        self.textbox.setText('Kick Off By @Nemzzy668')
        self.Show_Logo.setImage(Addon_Image)
        
        my_list = ["reddit", "redd.it", "facebook", "imgur", "twitter" , "discord" , "soccerstreams", "prntscr"]
        link = Get_Data(Media_Link).replace('\n', '').replace('\r','')
        links = 0
        urls = re.compile ('href="([^"]+)').findall(link)
        for items in urls:
            if 'http' in items:
                if not any(x in items.lower() for x in my_list):
                    links += 1
                    title = "[COLOR red]Link " + str(links) + " [/COLOR]:: " + items
                    desc = 'SportsDevil Required To Play These Links, Not All Will Work So Keep Trying If Link Fails!'
                    icon = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
                    urlplay = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + items
                    Item_Title.append(title)
                    Item_Link.append(urlplay)
                    Item_Icon.append(icon)
                    Item_Desc.append(desc)
                    self.List.addItem(title)
                    
    elif 'SportsDevil' in Media_Link:
        Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player ().play(Media_Link, Show_List, False)
            
    elif 'REPLAY:' in Media_Link:
        Media_Link = Media_Link.replace('REPLAY:','')
        link = Get_Data(Media_Link).replace('\n', '').replace('\r','').replace('\t','')
        source = dialog.select('[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]', ['[COLOR skyblue]Normal[/COLOR]','[COLOR skyblue]Extended[/COLOR]'])
        if source == 0:
            try:
                match = re.compile ('<iframe src="(.+?)"').findall(link)[0]
            except IndexError:
                dialog.notification("[COLOR blue]KICK OFF[/COLOR]", '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]', icon, 9000)
                quit()
            if not 'https:' in match or 'http:' in match:
                match = 'http:' + match
            if 'rutube' in match:
                stream_url = resolveurl.HostedMediaFile(match).resolve()
                Show_List  =  xbmcgui.ListItem(Media_Title)
                xbmc.Player().play(stream_url, Show_List, False)
            if 'streamable' in match:
                resolve = Get_Data(match).replace('\n', '').replace('\r','').replace('\t','')
                playurl = re.compile('<video.*?src="(.*?)"').findall(resolve)[0]
                if not 'http:' in playurl:
                    playurl = 'http:' + playurl
                #stream_url = resolveurl.HostedMediaFile(playurl).resolve()
                Show_List  =  xbmcgui.ListItem(Media_Title)
                xbmc.Player().play(playurl, Show_List, False)
            link2 = Get_Data(match).replace('\n', '').replace('\r','').replace('\t','')
            url = re.compile ('<source src="(.+?)"').findall(link2)[0]
            url = 'https:' + url
            liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
            xbmc.Player ().play(url, liz, False)
            quit(0)
        if source == 1:
            try:
                match = re.compile ('<iframe src="(.+?)"').findall(link)[1]
                if not 'http:' in match or 'https:' in match:
                    match = 'http:' + match
            except IndexError:
                dialog.notification("[COLOR blue]KICK OFF[/COLOR]", '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]', icon, 9000)
                time.sleep(2)
                quit()
            if 'rutube' in match:
                stream_url = resolveurl.HostedMediaFile(match).resolve()
                Show_List  =  xbmcgui.ListItem(Media_Title)
                xbmc.Player().play(stream_url, Show_List, False)
            link2 = Get_Data(match).replace('\n', '').replace('\r','').replace('\t','')
            url = re.compile ('<source src="(.+?)"').findall(link2)[0]
            url = 'https:' + url
            liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
            xbmc.Player ().play(url, liz, False)
            quit(0)
            
            
            


#############################################################
######### Class Containing the GUi Code / Controls ##########
class list_window(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='area51x'):
        super(list_window, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.List, lambda:List_Selected(self))
        
        passed(self, data)
        self.setFocus(self.List)


    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFF00f72c', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)

        self.textbox = pyxbmct.TextBox(textColor='0xFFFFFFFF')
        self.placeControl(self.textbox, 76, 30, 28, 20)

        self.Show_Logo = pyxbmct.Image('')
        self.placeControl(self.Show_Logo, 7, 38, 40, 11)


    def set_active_controls(self):
        self.List =	pyxbmct.List(buttonFocusTexture=Listbg,_space=6,_itemTextYOffset=-7,textColor='0xFFFFFFFF')
        self.placeControl(self.List, 5, 0, 109, 20)
        
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE],
            self.List_update)



    def set_navigation(self):
        pass

    def List_update(self):
        global Media_Title
        global Media_Link
        global Media_Desc
        global Media_Icon

        try:
            if self.getFocus() == self.List:
            
                position = self.List.getSelectedPosition()
                
                Media_Title = Item_Title[position]
                Media_Link  = Item_Link[position]
                Media_Desc = Item_Desc[position]
                
                self.textbox.setText(Media_Desc)
                self.textbox.autoScroll(1000, 1000, 1000)
                
                if Item_Icon[position] is not None:
                    Media_Icon = Item_Icon[position]
                    self.Show_Logo.setImage(Media_Icon)
                else:
                    Media_Icon = 'http://via.placeholder.com/300x220/13b7ff/FFFFFF?text=' + Media_Title
                    self.Show_Logo.setImage(Media_Icon)
                    
        except (RuntimeError, SystemError):
            pass
    
    

