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
import livegames
import list
import legends


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
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'lgf.gif'))
Background_Logo	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'lbgl.gif'))

ButtonaF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'a2.png'))
ButtonaNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'a1.png'))

ButtonbF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'b2.png'))
ButtonbNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'b1.png'))

ButtoncF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'c2.png'))
ButtoncNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'c1.png'))

ButtondF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'd2.png'))
ButtondNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'd1.png'))

ButtoneF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'e2.png'))
ButtoneNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'e1.png'))

#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():

    window = Main('neverwalkalone')
    window.doModal()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    del window

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data
    
def live(self):

    self.close
    livegames.livegameswindow('Acestream')

def replays(self):

    self.close
    list.listwindow('Replays')
    
def legendsw(self):

    self.close
    legends.legwindow('Legends')
    
def docs(self):

    self.close
    list.listwindow('LEGEND:DOC')



#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='guit'):
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        super(Main, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.button1, lambda:live(self))
        self.connect(self.button2, lambda:replays(self))
        self.connect(self.button3, lambda:docs(self))
        self.connect(self.button4, lambda:legendsw(self))
        self.setFocus(self.button1)
        

    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)

    def set_active_controls(self):
        self.button1 = pyxbmct.Button('',   focusTexture=ButtonaF,   noFocusTexture=ButtonaNF)
        self.placeControl(self.button1, 32, 0,  10, 12)
        self.button2 = pyxbmct.Button('',   focusTexture=ButtonbF,   noFocusTexture=ButtonbNF)
        self.placeControl(self.button2, 45, 0,  10, 12)
        self.button3 = pyxbmct.Button('',   focusTexture=ButtoncF,   noFocusTexture=ButtoncNF)
        self.placeControl(self.button3, 58, 0,  10, 12)
        self.button4 = pyxbmct.Button('',   focusTexture=ButtondF,   noFocusTexture=ButtondNF)
        self.placeControl(self.button4, 71, 0,  10, 12)
        self.button5 = pyxbmct.Button('',   focusTexture=ButtoneF,   noFocusTexture=ButtoneNF)
        self.placeControl(self.button5, 84, 0,  10, 12)
        self.button11 = pyxbmct.Button('[COLOR white]Version 1.0[/COLOR]')
        self.placeControl(self.button11, 103, 40,  10, 12)
        
        
        self.button11 = pyxbmct.Button('',   noFocusTexture=Background_Logo, focusTexture=Background_Logo)
        self.placeControl(self.button11, 32, 33,  57, 15)


    def set_navigation(self):
        #set the navigation for if user presses Right when eliment if focused
        self.button1.controlDown(self.button2)
        self.button2.controlDown(self.button3)
        self.button3.controlDown(self.button4)
        self.button4.controlDown(self.button5)
        self.button5.controlDown(self.button1)
        
        self.button1.controlUp(self.button5)
        self.button2.controlUp(self.button1)
        self.button3.controlUp(self.button2)
        self.button4.controlUp(self.button3)
        self.button5.controlUp(self.button4)
        
      
        
        
