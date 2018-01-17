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
import base64
import urllib
import urllib2


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon
from resources.libs import dateimport

dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
addon_id  = 'plugin.video.kickoff'
settingsxml = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id, 'settings.xml'))


#############################################################
#################### SET ADDON ID ###########################
_addon_id_  = 'plugin.video.kickoff'
_self_  = xbmcaddon.Addon(id=_addon_id_)
addon   = Addon(_addon_id_, sys.argv)

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data
    
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

    dialog.ok("KICK OFF","[COLOR yellow]Sadly Google Have taken it upon themselves, to declare my site a phishing scam, this is [COLOR red]False[COLOR yellow] and I have emailed them to resolve this issue, for now you either have to click details and then visit this dangerous site, or use IE, at least Microsoft have brains and don't link to googles shitty service[/COLOR]")
    clearup()
    dateimport.CHECKDIRS()
    dateimport.DateCheck()
    try:
        Main.MainWindow()
    except (RuntimeError, SystemError):
        pass

START()