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
import urllib
import urllib2
import time

import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon
from resources.libs import dateimport

dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()



#############################################################
#################### SET ADDON ID ###########################
_addon_id_  = 'plugin.video.fapzone'
_self_  = xbmcaddon.Addon(id=_addon_id_)
addon   = Addon(_addon_id_, sys.argv)
AddonTitle = "[COLOR darkgoldenrod]FapZone[/COLOR]"
_theme_ = _self_.getSetting('Theme')
_images_    = '/resources/' + _theme_
Addon_Image = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'addon.png'))

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

    dialog.ok("FAPZONE","[COLOR yellow]Sadly Google Have taken it upon themselves, to declare my site a phishing scam, this is [COLOR red]False[COLOR yellow] and I have emailed them to resolve this issue, for now you either have to click details and then visit this dangerous site, or use IE, at least Microsoft have brains and don't link to googles shitty service[/COLOR]")
    clearup()
    dateimport.CHECKDIRS()
    dateimport.DateCheck()
    try:
        Main.MainWindow()
    except (RuntimeError, SystemError):
        pass

START()