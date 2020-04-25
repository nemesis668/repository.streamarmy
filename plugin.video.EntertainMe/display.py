#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import os
import re
import requests
import sys
import urllib
import urllib2
import urlparse
import webbrowser
import base64
import json
import time
import datetime
import StorageServer

import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon

dialog = xbmcgui.Dialog()
cache               = StorageServer.StorageServer("entertainme", 0.2)

#############################################################
#################### SET ADDON ID ###########################
_addon_id_ = 'plugin.video.EntertainMe'
_self_ = xbmcaddon.Addon(id=_addon_id_)
username = _self_.getSetting('Username')
password = _self_.getSetting('Password')
Date = time.strftime("%A %B %d")
AddonTitle = '[B][COLOR red]E[COLOR yellow]ntertain Me[/B][/COLOR]'
dp = xbmcgui.DialogProgress()
icon  = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_, 'icon.png'))


#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	


#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bgrelease.gif'))
#LOGO	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'test.jpg'))


#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():

	window = Main('Display')
	window.doModal()
	del window

def tick(self):

    self.DATE.setLabel (str(Date))

def CLEANUP(text):

	text = str(text)
	text = text.replace('\\r','')
	text = text.replace('\\n','')
	text = text.replace('\\t','')
	text = text.replace('\\','')
	text = text.replace('<br />','\n')
	text = text.replace('<hr />','')
	text = text.replace('&#039;',"'")
	text = text.replace('&#39;',"'")
	text = text.replace('&quot;','"')
	text = text.replace('&rsquo;',"'")
	text = text.replace('&amp;',"&")
	text = text.replace('&#8211;',"&")
	text = text.replace('&#8217;',"'")
	text = text.replace('&#038;',"&")
	text = text.replace('&#8211;',"-")
	text = text.replace('&nbsp;',"")
	text = text.replace('&hellip;',"...")
	text = text.replace('&#8220;',"\"")
	text = text.replace('&#8230;',"...")
	text = text.replace('&#8221;',"\"")
	text = text.replace('<em>',"|")
	text = text.replace('</em>',"|")
	text = text.lstrip(' ')
	text = text.lstrip('	')

	return text
def GetTokens():
	try:
		dp.create (AddonTitle,("[COLOR yellow]EntertainMe[/COLOR]"))
		dp.update(0)
		time.sleep(1)
		from cloudscraper2 import CloudScraper
		dp.update (50,("[COLOR pink]Grabbing Cloudflare Token[/COLOR]"))
		scraper = CloudScraper.create_scraper()
		ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
		scraper.headers.update({'User-Agent': ua})
		cookies = scraper.get('http://www.seehd.pl/wp-content/themes/kickass-mediaspace/favicon.png').cookies.get_dict()
		dp.update (100,("[COLOR pink]Secuirty Bypassed, Addon Opening[/COLOR]"))
		time.sleep(1)
		dp.close()
		return (cookies, ua)
	except:
		dialog.ok(AddonTitle,"[COLOR yellow]Failed To Grab Cloudflare Token, Try Again[/COLOR]")
		quit()
#def ReleaseDates():

entries = []
url = 'http://www.seehd.pl/movies-release-dates/'
cookies, ua = cache.cacheFunction(GetTokens)
headers = {'User-Agent': ua}
link = requests.get(url, cookies=cookies, headers=headers).text
content = re.findall('<ul>(.*?)</ul>',link,re.DOTALL)[0]
pattern = r'''<li>(.*?)</li>'''
find = re.findall(pattern,content)
for movies in find:
	movies = CLEANUP(movies)
	entries.append(movies)

filmlist = '\n-----------------------------------------------------------------------\n'.join(entries)


#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

	xbmc.executebuiltin("Dialog.Close(busydialog)")

	def __init__(self, title='EntertainMe'):
		super(Main, self).__init__(title)

		self.setGeometry(1280, 720, 100, 50)
		Background  = pyxbmct.Image(Background_Image)

		self.placeControl(Background, -10, -1, 123, 52)
		

		self.set_info_controls()

		self.set_active_controls()

		self.set_navigation()

		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
		tick(self)
		
		# self.connect(self.button7, lambda:apkinstall(self))


	def set_info_controls(self):
		self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
		self.DATE =  pyxbmct.Label('',textColor='0xFFFFFF00', font='font18')
		self.placeControl(self.Hello, -4, 1, 1, 50)
		self.placeControl(self.DATE,  -9, 42, 12, 15)
		self.textbox = pyxbmct.TextBox(textColor='0xFFFFFF00')
		self.placeControl(self.textbox, 10, 0, 90, 50)
		

	def set_active_controls(self):
		self.textbox.setText(filmlist)
		self.textbox.autoScroll(1000, 1000, 1000)
		# self.button1 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		# self.placeControl(self.button1, 68, 0,  40, 8)


	def set_navigation(self):
		pass
		#tick(self)
		# self.button1.controlRight(self.button2)


	def setAnimation(self, control):
		control.setAnimations([('WindowOpen', 'effect=slide start=2000 end=0 time=1000',),
								('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
	
