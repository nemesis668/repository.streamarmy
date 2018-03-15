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
import base64
import videos


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon
from resources.libs import dateimport

dialog = xbmcgui.Dialog()


#############################################################
#################### SET ADDON ID ###########################
_addon_id_	= 'plugin.video.fapzone'
_self_			= xbmcaddon.Addon(id=_addon_id_)

#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'fapzone.gif'))
Background_Logo	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'model.gif'))
Background_Logo1	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'welcome.gif'))
Listbg = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'listbg.png'))
Addon_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'model.gif'))
Addon_Icon = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Addon_Icon.png'))
SearchF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'searchF.png'))
SearchNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'search.png'))


#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():
    
    global data
    global List
    window = Main('fapzone')
    window.doModal()
    del window
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data

def passed(self, title):

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
    
    title = title.upper()
    Item_Title.append('[COLOR gold]Main ' + title + ' List[/COLOR]')
    Item_Link.append('')
    Item_Desc.append('Welcome To FapZone, Grab The Wipes')
    Item_Icon.append(Addon_Image)
    self.List.addItem('[COLOR yellow]Main Catergory List[/COLOR]')
    self.textbox.setText('Welcome To FapZone By @Nemzzy668 and @_Manc_ We Are Not Resposible For Any Injuries Caused While Using This Add on')
    self.Show_Logo.setImage(Addon_Image)
    
    url = base64.b64decode(b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v')
    link = Get_Data(url)
    match = re.compile ('<li class="">(.+?)</li>').findall(link)
    for links in match:
        title = re.compile ('<strong>(.+?)</strong>').findall(links)[0]
        number = re.compile ('<div class="cllnumber">(.+?)</div>').findall(links)[0]
        url1 = re.compile ('<a href="(.+?)"').findall(links)[0]
        url = 'https://www.eporner.com' + url1
        if not 'All'in title:
            if not 'Homemade' in title:
                Item_Title.append(title)
                Item_Link.append(url)
                Item_Icon.append(Addon_Image)
                self.List.addItem(title)
                Item_Desc.append(title)
                
def Search(self):

    string =''
    keyboard = xbmc.Keyboard(string, '[COLOR red]What Would You Like To Find?[/COLOR]')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        string = string.replace(' ','-')
        if len(string)>1:
            Media_Link = 'https://www.eporner.com/search/' + string
            videos.videowindow(Media_Link)
        else: quit()
    
    
def List_Selected(self):

    videos.videowindow(Media_Link)

#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title=''):
        super(Main, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.List, lambda:List_Selected(self))
        self.connect(self.button1, lambda:Search(self))
        #self.setFocus(self.button1)
        
        passed(self, title)
        self.setFocus(self.List)

    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFFFFD700', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)
        
        self.List =	pyxbmct.List(buttonFocusTexture=Listbg,_space=9,_itemTextYOffset=-7,textColor='0xFFFFD700')
        self.placeControl(self.List, 0, 2, 115, 10)
        
        
        self.textbox = pyxbmct.TextBox(textColor='0xFFFFD700')
        self.placeControl(self.textbox, 95, 18, 30, 30)
        
        self.Show_Logo = pyxbmct.Image('')
        self.placeControl(self.Show_Logo, 25, 18, 70, 30)
        
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE],
            self.List_update)
            

    def set_active_controls(self):
    
        self.button1 = pyxbmct.Button('',   noFocusTexture=SearchNF, focusTexture=SearchF)
        self.placeControl(self.button1, 99, 40,  12, 8)
    
        self.button11 = pyxbmct.Button('',   noFocusTexture=Addon_Icon, focusTexture=Addon_Icon)
        self.placeControl(self.button11, -4, 42,  20, 8)
        self.button12 = pyxbmct.Button('',   noFocusTexture=Background_Logo1, focusTexture=Background_Logo1)
        self.placeControl(self.button12, -4, 16,  25, 26)
        
    def set_navigation(self):
        self.button1.controlLeft(self.List)
        self.List.controlRight(self.button1)
        
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
            