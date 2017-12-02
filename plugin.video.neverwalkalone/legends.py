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
import json


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
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'legends.jpg'))
ButtonaF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'kennyf.jpg'))
ButtonaNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'kennynf.jpg'))
ButtonbF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'ianrushf.jpg'))
ButtonbNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'ianrushnf.jpg'))
ButtoncF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'gerrardf.jpg'))
ButtoncNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'gerrardnf.jpg'))
ButtondF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'suarezf.jpg'))
ButtondNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'suareznf.jpg'))
ButtoneF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'torresf.jpg'))
ButtoneNF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'torresnf.jpg'))

ButtonfF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'kingkenny.png'))
ButtongF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'buttonrush.png'))
ButtonhF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'buttongerrard.png'))
ButtoniF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'buttonsuarez.png'))
ButtonjF = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'buttontorres.png'))




########## Function To Call That Starts The Window ##########
def legwindow(ta):
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

def sendtolist1(self):
    self.close
    list.listwindow('Legend:King Kenny')
def sendtolist2(self):
    self.close
    list.listwindow('Legend:Ian Rush')
def sendtolist3(self):
    self.close
    list.listwindow('Legend:Gerrard')
def sendtolist4(self):
    self.close
    list.listwindow('Legend:Suarez')
def sendtolist5(self):
    self.close
    list.listwindow('Legend:Torres')




#############################################################
######### Class Containing the GUi Code / Controls ##########
class nfl_window(pyxbmct.AddonFullWindow):

    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='neverwalkalone'):
        super(nfl_window, self).__init__(title)

        self.setGeometry(1280, 720, 100, 50)

        Background  = pyxbmct.Image(Background_Image)

        self.placeControl(Background, -10, -1, 123, 52)

        self.set_info_controls()

        self.set_active_controls()

        self.set_navigation()

        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.button1, lambda:sendtolist1(self))
        self.connect(self.button2, lambda:sendtolist2(self))
        self.connect(self.button3, lambda:sendtolist3(self))
        self.connect(self.button4, lambda:sendtolist4(self))
        self.connect(self.button5, lambda:sendtolist5(self))
        self.setFocus(self.button1)


    def set_info_controls(self):
        self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)


    def set_active_controls(self):
        self.button1 = pyxbmct.Button('',   focusTexture=ButtonaF,   noFocusTexture=ButtonaNF)
        self.placeControl(self.button1, 65, 0,  34 , 10)
        self.button2 = pyxbmct.Button('',   focusTexture=ButtonbF,   noFocusTexture=ButtonbNF)
        self.placeControl(self.button2, 65, 10,  34 , 10)
        self.button3 = pyxbmct.Button('',   focusTexture=ButtoncF,   noFocusTexture=ButtoncNF)
        self.placeControl(self.button3, 65, 20,  34 , 10)
        self.button4 = pyxbmct.Button('',   focusTexture=ButtondF,   noFocusTexture=ButtondNF)
        self.placeControl(self.button4, 65, 30,  34 , 10)
        self.button5 = pyxbmct.Button('',   focusTexture=ButtoneF,   noFocusTexture=ButtoneNF)
        self.placeControl(self.button5, 65, 40,  34 , 10)
        
        self.button6 = pyxbmct.Button('',   focusTexture=ButtonfF,   noFocusTexture=ButtonfF)
        self.placeControl(self.button6, 55, 1,  8 , 8)
        self.button7 = pyxbmct.Button('',   focusTexture=ButtongF,   noFocusTexture=ButtongF)
        self.placeControl(self.button7, 55, 11,  8 , 8)
        self.button8 = pyxbmct.Button('',   focusTexture=ButtonhF,   noFocusTexture=ButtonhF)
        self.placeControl(self.button8, 55, 21,  8 , 8)
        self.button9 = pyxbmct.Button('',   focusTexture=ButtoniF,   noFocusTexture=ButtoniF)
        self.placeControl(self.button9, 55, 31,  8 , 8)
        self.button10 = pyxbmct.Button('',   focusTexture=ButtonjF,   noFocusTexture=ButtonjF)
        self.placeControl(self.button10, 55, 41,  8 , 8)



    def set_navigation(self):
        self.button1.controlRight(self.button2)
        self.button1.controlLeft(self.button5)
        
        self.button2.controlRight(self.button3)
        self.button2.controlLeft(self.button1)
        
        self.button3.controlRight(self.button4)
        self.button3.controlLeft(self.button2)
        
        self.button4.controlRight(self.button5)
        self.button4.controlLeft(self.button3)
        
        self.button5.controlRight(self.button1)
        self.button5.controlLeft(self.button4)
    

