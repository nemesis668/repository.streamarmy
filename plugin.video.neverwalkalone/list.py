#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import urlresolver

import os
import re
import sys
import urllib
import urllib2
import urlparse
import Main
import livegames
import json


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()

apikey = 'AIzaSyA20yLuOaZeeMPmLdV9H2LiHIWAp2lFafc'

#############################################################
#################### SET ADDON ID ###########################
_addon_id_	= 'plugin.video.neverwalkalone'
_self_			= xbmcaddon.Addon(id=_addon_id_)
icon  = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_, 'icon.png'))

#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'lfclist.jpg'))
Listbg = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'listbg.png'))
Addon_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'addon.png'))


########## Function To Call That Starts The Window ##########
def listwindow(ta):
    global data
    global List
    
    data = ta
    window = list_window('neverwalkalone')
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
    
def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
        response = urllib2.urlopen(req, timeout=5)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('\t','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')
        return link
    except:quit()
    
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
    Item_Title.append('[COLOR red]' + title + '[/COLOR]')
    Item_Link.append('')
    Item_Desc.append('Never Walk Alone By @Nemzzy668')
    Item_Icon.append(Addon_Image)
    self.List.addItem('[COLOR red]' + title + '[/COLOR]')
    self.textbox.setText('Never Walk Alone By @Nemzzy668')
    self.Show_Logo.setImage(Addon_Image)
    
    if 'ACESTREAM' in title:
    
        url = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
        link = open_url(url).replace('\n', '').replace('\r','')
        match = re.compile('<td>(.+?)</td>').findall(link)
        for Item in match:
            url = re.compile ('<a href="(.+?)"').findall(Item)[0]
            game = re.compile ('<a href=".+?">(.+?)</a>').findall(Item)[0].replace('-','[COLOR yellow]Vs[/COLOR]')
            if 'Liverpool' in game:
                Item_Title.append(game)
            if 'Liverpool' in game:
                Item_Desc.append(game)
                image = 'https://i.imgur.com/v9hIXD2.png'
                Item_Icon.append(image)
                url = 'http://www.livefootballol.me' + url
            if 'Liverpool' in game:
                Item_Link.append(url)
            if 'Liverpool' in game:
                self.List.addItem(game)

    elif 'SCRAPER' in title:
        url = 'https://www.reddit.com/r/soccerstreams/'
        link = open_url(url).replace('\n', '').replace('\r','')
        match = re.compile ('data-event-action="title"(.+?)<span class="domain">').findall(link)
        for links in match:
            #try:
              title = re.compile ('rel=.+?>(.+?)</a>').findall(links)[0]
              url = re.compile ('href="(.+?)"').findall(links)[0]
              url = 'https://www.reddit.com' + url
              icon = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
              if 'GMT' in title and 'Liverpool' in title:
                title = CLEANUP(title)
                desc = 'Sports Devil Required To Play These Links'
                Item_Desc.append(desc)
                Item_Title.append(title)
                Item_Link.append(url)
                Item_Icon.append(icon)
                self.List.addItem(title)

            #except:pass

    elif 'REPLAYS' in title:

        url = 'https://www.livefootballol.me/video/england/'
        link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
        match = re.compile ('<td>(.+?)</td>').findall(link)
        for Item in match:
            team = re.compile ('<a href=".+?">(.+?)</a>').findall(Item)[0]
            url = re.compile ('<a href="(.+?)"').findall(Item)[0]
            if 'Liverpool' in team:
                Item_Title.append(team)
                url = 'REPLAYS:https://www.livefootballol.me' + url
                image = 'https://i.imgur.com/v9hIXD2.png'
                desc = team + ' Highlights'
                Item_Icon.append(image)
                Item_Link.append(url)
                Item_Desc.append(desc)
                self.List.addItem(team)
    
    elif 'LEGEND:' in title:
        title = title.replace('LEGEND:','')
        if 'KING KENNY' in title:
            playlistid = 'PLlMN8jQiRupYIhUNbMirOhm-Y7a46corH'
        elif 'IAN RUSH' in title:
            playlistid = 'PLXRgEda5oFoGocCVlBGLfbxHJB5bVe2Ib'
        elif 'GERRARD' in title:
            playlistid = 'PLfRRjD2Du8hsMbz3dZ0YdQAGjGdZr-9m7'
        elif 'SUAREZ' in title:
            playlistid = 'PLlMN8jQiRupbC-Sp12VQp_mEutLFXh8uh'
        elif 'TORRES' in title:
            playlistid = 'PLlMN8jQiRupZng87vO9CSCNe6hRbv4A4E'
        elif 'DOC' in title:
            playlistid = 'PLlMN8jQiRupZOB1H3jEm7hq8cWA7rFbvu'
        url = ('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=%s&key=%s' %(playlistid,apikey))
        link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
        data = json.loads(link)
        grab = data['items']
        for i in grab:
            try:
                title = i['snippet']['title']
                Item_Title.append(title)
                desc = i['snippet']['description']
                Item_Desc.append(desc)
                icon = i['snippet']['thumbnails']['default']['url']
                icon = icon.replace('default','hqdefault')
                Item_Icon.append(icon)
                videos = i['snippet']['resourceId']['videoId']
                videourl = 'https://www.youtube.com/watch?v=' + videos
                Item_Link.append(videourl)
                self.List.addItem(title)
            except: pass
    else: quit()
                
        

def List_Selected(self):

    #self.List.reset()
    #self.List.setVisible(True)
    #dialog.ok("Here",str(Media_Link))
    if 'http://www.livefootballol.me' in Media_Link:
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
        Item_Title.append('[COLOR red]' + title + '[/COLOR]')
        Item_Link.append('')
        Item_Desc.append('Never Walk Alone By @Nemzzy668')
        Item_Icon.append(Addon_Image)
        self.List.addItem('[COLOR red]' + title + '[/COLOR]')
        self.textbox.setText('Never Walk Alone By @Nemzzy668')
        self.Show_Logo.setImage(Addon_Image)
        
        link = open_url(Media_Link).replace('\n', '').replace('\r','')
        match = re.compile('<a href="(.+?)"').findall(link)
        linktitle = 0
        for urls in match:
            if 'acestream' in urls:
                if 'http' in urls:
                    linktitle += 1
                    title = 'Link :: ' + str(linktitle)
                    Item_Title.append(title)
                    Item_Link.append(urls)
                    image = 'https://i.imgur.com/v9hIXD2.png'
                    desc = 'AceStream Links For Liverpool Games'
                    Item_Desc.append(desc)
                    Item_Icon.append(image)
                    self.List.addItem(title)
                    
        if linktitle == 0:
            title = 'No Links Available Yet, Try Closer To Kick Off'
            Item_Title.append(title)
            self.List.addItem(title)
            
    elif 'REPLAYS:' in Media_Link:
        url = Media_Link.replace('REPLAYS:','')
        link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
        play = re.compile('<iframe.+?src="(.+?)"').findall(link)[0]
        url = 'https:' + play
        if urlresolver.HostedMediaFile(url).valid_url():
            stream_url = urlresolver.HostedMediaFile(url).resolve()
            Show_List  =  xbmcgui.ListItem(Media_Title)
            xbmc.Player().play(stream_url, Show_List, False)
            
    elif 'youtube' in Media_Link:
        if urlresolver.HostedMediaFile(Media_Link).valid_url():
            stream_url = urlresolver.HostedMediaFile(Media_Link).resolve()
            Show_List  =  xbmcgui.ListItem(Media_Title)
            xbmc.Player().play(stream_url, Show_List, False)
    
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
        Item_Desc.append('Never Walk Alone By @Nemzzy668')
        Item_Icon.append(Addon_Image)
        self.List.addItem('[COLOR red]' + title + '[/COLOR]')
        self.textbox.setText('Never Walk Alone By @Nemzzy668')
        self.Show_Logo.setImage(Addon_Image)
        
        my_list = ["reddit", "redd.it", "facebook", "imgur", "twitter" , "discord" , "soccerstreams"]
        link = open_url(Media_Link)
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
        
    elif 'channels' in Media_Link:
        global Item_Title
        global Item_Link
        global Item_Desc
        global Item_Icon

        Item_Title =  []
        Item_Link  =  []
        Item_Desc  =  []
        Item_Icon  =  []
        link = open_url(Media_Link).replace('\n', '').replace('\r','')
        url = re.compile('<div class="uk-text-center"><a href="(.+?)"').findall(link)[0]
        url1 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
        Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player ().play(url1, Show_List, False)
            
            
            #dialog.notification("[COLOR red]Never Walk Alone[/COLOR]", '[COLOR red]Sorry File has been removed at source[/COLOR]', icon, 5000)


#############################################################
######### Class Containing the GUi Code / Controls ##########
class list_window(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='neverwalkalone'):
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
        self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)

        self.textbox = pyxbmct.TextBox(textColor='0xFFFFFFFF')
        self.placeControl(self.textbox, 69, 31, 28, 13)

        self.Show_Logo = pyxbmct.Image('')
        self.placeControl(self.Show_Logo, 23, 40, 40, 8)


    def set_active_controls(self):
        self.List =	pyxbmct.List(buttonFocusTexture=Listbg,_space=12,_itemTextYOffset=-7,textColor='0xFFFFFFFF')
        self.placeControl(self.List, 25, 1, 80, 23)
        
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
    

