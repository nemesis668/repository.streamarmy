import xbmc

import xbmcaddon

import xbmcgui

import xbmcplugin

import sys



import os

import re

import requests

from common_addon import Addon

dialog = xbmcgui.Dialog()

AddonTitle = '[COLOR red][B]E[COLOR yellow]nterTain Me[/B][/COLOR]'

addon_id            = 'plugin.video.EntertainMe'

addon               = Addon(addon_id, sys.argv)

selfAddon           = xbmcaddon.Addon(id=addon_id)

def checkupdates():

	pin = selfAddon.getSetting('pin')
	if pin == '': pin = 'EXPIRED'
	if pin == 'EXPIRED':
		dialog.ok(AddonTitle,"[COLOR yellow]Please visit [COLOR lime]https://pinsystem.co.uk[COLOR yellow] to generate an Access Token For [COLOR lime]EntertainMe[COLOR yellow] then enter it after clicking ok[/COLOR]")
		string =''
		keyboard = xbmc.Keyboard(string, '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]')
		keyboard.doModal()
		if keyboard.isConfirmed():
			string = keyboard.getText()
			if len(string)>1:
				term = string.title()
				selfAddon.setSetting('pin',term)
				checkupdates()
			else: quit()
		else:
			quit()
	if not 'EXPIRED' in pin:
		pinurlcheck = ('https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % pin)
		link = requests.get(pinurlcheck).content
		if len(link) <=2 or 'Pin Expired' in link:
			selfAddon.setSetting('pin','EXPIRED')
			checkupdates()
		else:
			pass
