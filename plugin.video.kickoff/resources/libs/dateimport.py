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


import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.kickoff'
AddonTitle = "[COLOR aqua]FapZone[/COLOR]"
makefolder = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.kickoff/settings/'))
settingsxml  = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id, 'settings.xml'))

def Get_Data(url):

    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
    response = urllib2.urlopen(req, timeout=30)
    data = response.read()
    response.close()

    return data


def CHECKDIRS():


    if not os.path.exists(os.path.dirname(makefolder)):
        try:
            os.makedirs(os.path.dirname(makefolder))
            with open(settingsxml, "w") as f:
                f.write("<date>000</date>")
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
                
def DateCheck():

    readsettings = open(settingsxml).read().replace('\n', '').replace('\r','').replace('\t','')
    try:
        checkpin = re.compile ('<pin>(.+?)</pin>').findall(readsettings)[0]
        if checkpin == 'EXPIRED':
            dialog.ok(AddonTitle,"[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access KickOff Addon then enter it after clicking ok[/COLOR]")
            string =''
            keyboard = xbmc.Keyboard(string, '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]')
            keyboard.doModal()
            if keyboard.isConfirmed():
                string = keyboard.getText()
                if len(string)>1:
                    term = string.title()
                    with open(settingsxml, "w") as f:
                        f.write("<pin>" + term + "</pin>")
                    DateCheck()
                else: quit()
            else:
                quit()
        if not 'EXPIRED' in checkpin:
            currentpin = re.compile ('<pin>(.+?)</pin>').findall(readsettings)[0]
            pinurlcheck = ('https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % currentpin)
            link = Get_Data(pinurlcheck)
            if len(link) <5 or 'Pin Expired' in link:
                with open(settingsxml, "w") as f:
                    f.write ('<pin>EXPIRED</pin>')
                DateCheck()
            else: return
    except IndexError:
        with open(settingsxml, "w") as f:
            f.write("<pin>EXPIRED</pin>\n")
        DateCheck()