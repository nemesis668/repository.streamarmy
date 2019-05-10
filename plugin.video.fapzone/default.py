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


    
def START():

    try:
        Main.MainWindow()
    except (RuntimeError, SystemError):
        pass

START()