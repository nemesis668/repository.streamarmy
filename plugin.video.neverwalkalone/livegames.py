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
import list


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()



#############################################################
#################### SET ADDON ID ###########################
_addon_id_	= 'plugin.video.neverwalkalone'
_self_			= xbmcaddon.Addon(id=_addon_id_)

#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'livechoice.jpg'))
Logo_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'logo.png'))
Addon_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'addon.png'))
Listbg = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'listbg.png'))
ButtonaF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'acestreamf.png'))
ButtonaNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'acestream.png'))
ButtonbF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'scraperf.png'))
ButtonbNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'scraper.png'))

########## Function To Call That Starts The Window ##########
def livegameswindow(ta):
    global data
    global List
    
    data = ta
    window = nfl_window('neverwalkalone')
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

def passed(self, title):
    pass


def acestream(self):
    self.close
    list.listwindow('Acestream')
    
def scraper(self):
    self.close
    list.listwindow('Scraper')


#############################################################
######### Class Containing the GUi Code / Controls ##########
class nfl_window(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='neverwalkalone'):
        super(nfl_window, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)
        
        Logo  = pyxbmct.Image(Logo_Image)

        self.placeControl(Logo, -1, 4, 10, 20)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.button1, lambda:acestream(self))
        self.connect(self.button2, lambda:scraper(self))
        self.setFocus(self.button1)


    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)


    def set_active_controls(self):
        self.button1 = pyxbmct.Button('',   focusTexture=ButtonaF,   noFocusTexture=ButtonaNF)
        self.placeControl(self.button1, 28, 6,  78 , 21)
        self.button2 = pyxbmct.Button('',   focusTexture=ButtonbF,   noFocusTexture=ButtonbNF)
        self.placeControl(self.button2, 42, 26,  50 , 15)



    def set_navigation(self):
        self.button1.controlRight(self.button2)
        self.button2.controlLeft(self.button1)
    

