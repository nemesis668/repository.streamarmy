#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import time

import os
import re
import sys
import Main

import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon
from resources.libs import dateimport

dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
addon_id            = 'plugin.video.neverwalkalone'
settingsxml = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id, 'settings.xml'))

#############################################################
#################### SET ADDON ID ###########################
_addon_id_  = 'plugin.video.neverwalkalone'
_self_  = xbmcaddon.Addon(id=_addon_id_)
addon   = Addon(_addon_id_, sys.argv)

def clearup():

    cachePath     = xbmc.translatePath(os.path.join('special://home/cache'))
    thumbPath     = xbmc.translatePath(os.path.join('special://profile/Thumbnails'))
    packcagesPath = xbmc.translatePath(os.path.join('special://home/addons/packages'))
    
    i =[(cachePath,'Cache'),(thumbPath,'Thumbnails'),(packcagesPath,'Packages')]
    for r in i:
        for root,dirs,files in os.walk(r[0]):
            for f in files:
                if (f.endswith('.log')): continue
                try: os.unlink(os.path.join(root, f))
                except: pass
    xbmc.executebuiltin('Container.Refresh')


def START():

    clearup()
    dateimport.CHECKDIRS()
    dateimport.DateCheck()
    try:
        Main.MainWindow()
    except (RuntimeError, SystemError):
        pass

START()